#!/usr/bin/env python3
"""Local prompt queue for running Codex CLI jobs one at a time or in parallel."""
from __future__ import annotations

import argparse, json, os, subprocess, threading, time, uuid
from concurrent.futures import ThreadPoolExecutor
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).parent
STATE = ROOT / ".codex-batch-state.json"
lock = threading.Lock()
state = {"jobs": [], "running": False, "paused": False, "concurrency": 1, "start_at": None}

def save():
    with lock:
        STATE.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")

def load():
    global state
    if STATE.exists():
        try: state = json.loads(STATE.read_text(encoding="utf-8"))
        except json.JSONDecodeError: pass

def run_job(job):
    with lock: job["status"] = "running"; job["started"] = time.time()
    save()
    command = os.environ.get("CODEX_COMMAND", "codex exec")
    try:
        result = subprocess.run(command.split() + [job["prompt"]], cwd=job.get("cwd") or ROOT,
                                text=True, capture_output=True, timeout=3600)
        with lock:
            job["status"] = "done" if result.returncode == 0 else "failed"
            job["output"] = result.stdout[-4000:]
            job["error"] = result.stderr[-4000:]
            job["finished"] = time.time()
    except Exception as exc:
        with lock: job["status"] = "failed"; job["error"] = str(exc); job["finished"] = time.time()
    save()

def wait_until(start_at):
    if not start_at:
        return
    while True:
        now = time.localtime()
        target_h, target_m = map(int, start_at.split(':'))
        if (now.tm_hour, now.tm_min) >= (target_h, target_m):
            return
        time.sleep(20)

def runner(start_at=None):
    wait_until(start_at)
    while True:
        with lock:
            if not state["running"]: return
            if state["paused"]: jobs = []
            else: jobs = [j for j in state["jobs"] if j["status"] == "pending"][:state["concurrency"]]
            for j in jobs: j["status"] = "claimed"
        if not jobs:
            if all(j["status"] in ("done", "failed") for j in state["jobs"]):
                state["running"] = False; save(); return
            time.sleep(.5); continue
        with ThreadPoolExecutor(max_workers=len(jobs)) as pool:
            list(pool.map(run_job, jobs))

class Handler(BaseHTTPRequestHandler):
    def send_json(self, value, code=200):
        raw = json.dumps(value, ensure_ascii=False).encode()
        self.send_response(code); self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(raw))); self.end_headers(); self.wfile.write(raw)
    def do_GET(self):
        if self.path == "/api/state": self.send_json(state); return
        page = (ROOT / "codex_batch_workbench.html").read_bytes()
        self.send_response(200); self.send_header("Content-Type", "text/html; charset=utf-8"); self.end_headers(); self.wfile.write(page)
    def do_POST(self):
        data = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))))
        if self.path == "/api/queue":
            with lock:
                state["jobs"] = [{"id": str(uuid.uuid4()), "prompt": p, "status": "pending"} for p in data["prompts"] if p.strip()]
                state["concurrency"] = max(1, min(32, int(data.get("concurrency", 1))))
                state["paused"] = False; state["running"] = True; state["start_at"] = data.get("start_at") or None
            save(); threading.Thread(target=runner, args=(state["start_at"],), daemon=True).start(); self.send_json(state); return
        if self.path == "/api/pause":
            state["paused"] = True; save(); self.send_json(state); return
        if self.path == "/api/resume":
            state["paused"] = False; state["running"] = True; save(); threading.Thread(target=runner, args=(state.get("start_at"),), daemon=True).start(); self.send_json(state); return
        self.send_json({"error": "not found"}, 404)

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--port", type=int, default=8765); ap.add_argument("--start-at", default=None, help="daily start time, HH:MM"); ap.add_argument("--queue-jsonl", default=None); ap.add_argument("--concurrency", type=int, default=1); args = ap.parse_args()
    load()
    if args.queue_jsonl:
        rows = [json.loads(line) for line in Path(args.queue_jsonl).read_text(encoding="utf-8").splitlines() if line.strip()]
        state["jobs"] = [{"id": row.get("id", str(uuid.uuid4())), "prompt": row["prompt"], "topic": row.get("topic"), "status": "pending"} for row in rows]
        state["concurrency"] = max(1, min(32, args.concurrency)); state["running"] = True; state["paused"] = False; state["start_at"] = args.start_at
        save(); threading.Thread(target=runner, args=(args.start_at,), daemon=True).start()
    elif args.start_at: state["start_at"] = args.start_at; save()
    print(f"Open http://127.0.0.1:{args.port}"); ThreadingHTTPServer(("127.0.0.1", args.port), Handler).serve_forever()
