#!/usr/bin/env python3
"""Generate the five Enterprise AI Deployment explainers.

The script deliberately reads Azure credentials from the user's existing .env
file at runtime and never prints them. It creates one narrated MP4 per topic
with timed, burned-in captions and changing central diagrams.
"""
from __future__ import annotations

import html
import os
import re
import subprocess
import tempfile
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "vedio"
ENV_FILE = Path("/Users/rebecca/Documents/Codex/2026-09-06/files-pasted-by-the-user-ai/outputs/rebecca-ai-explainer/.env")
W, H = 1280, 720
FONT = "/System/Library/Fonts/Supplemental/Arial.ttf"
BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"

TOPICS = {
    "workflow-discovery": {
        "title": "WORKFLOW DISCOVERY",
        "slug": "workflow-discovery",
        "voice": [
            ("Workflow Discovery", "Keywords: observe, listen, map", "Start with the work people actually do, not the AI feature someone imagined."),
            ("Definition", "Learn the real path from request to result.", "Workflow discovery means watching the handoffs, exceptions, tools, and decisions that shape today's process."),
            ("Plain English", "Follow the busy parts and the awkward parts.", "In simple terms, find where time disappears, where people retype information, and where a judgment call is hard."),
            ("Life sample", "Like tracing one invoice through a busy kitchen.", "You watch the order arrive, the ingredients get checked, the dish gets approved, and the final receipt gets filed."),
            ("Key point", "Choose a costly step with a clear owner.", "A useful AI opportunity has a measurable outcome, an accountable person, and a safe fallback when the system is unsure."),
            ("Conclusion", "A shared map turns a vague wish into a candidate.", "Once the team agrees on the real workflow, technical scoping can start from evidence instead of assumptions."),
        ],
    },
    "technical-scoping": {
        "title": "TECHNICAL SCOPING",
        "slug": "technical-scoping",
        "voice": [
            ("Technical Scoping", "Keywords: capability, data, guardrails", "Turn a promising idea into a small system that can be tested."),
            ("Definition", "Set the boundaries of the AI job.", "Technical scoping names the inputs, outputs, model capabilities, integrations, constraints, and safety checks required for a pilot."),
            ("Plain English", "Decide what the system must do and must not do.", "It is the difference between saying 'use AI for invoices' and specifying one document type, one output, one owner, and one review path."),
            ("Life sample", "Like planning a kitchen before buying appliances.", "You check the room, power, water, tools, cooking steps, and safety rules before promising a working dinner service."),
            ("Key point", "Scope around one measurable outcome.", "A narrow pilot with representative data teaches more than a large demo with unclear success criteria."),
            ("Conclusion", "A good scope makes tradeoffs visible.", "When the boundaries are explicit, the team can choose the right model, integration path, and evaluation plan."),
        ],
    },
    "integration": {
        "title": "INTEGRATION",
        "slug": "integration",
        "voice": [
            ("Integration", "Keywords: APIs, events, permissions", "Connect AI to the systems and controls people already rely on."),
            ("Definition", "Move trusted data in and safe actions out.", "Integration links a model to source systems, identity, business rules, APIs, events, logs, and human approvals."),
            ("Plain English", "Make the AI fit the existing workflow.", "The user should not have to copy information between five tools or wonder whether an action really happened."),
            ("Life sample", "Like a translator carrying a restaurant order.", "The translator reads the menu, sends the order to the kitchen, checks the result, and records who approved the change."),
            ("Key point", "Permissions and audit trails are part of the feature.", "Least-privilege access, validation, retries, and observable tool calls keep useful automation from becoming hidden risk."),
            ("Conclusion", "A connected AI feature earns its place in the flow.", "When systems, people, and evidence line up, evaluation can measure the whole outcome—not just the model's words."),
        ],
    },
    "evaluation": {
        "title": "EVALUATION",
        "slug": "evaluation",
        "voice": [
            ("Evaluation", "Keywords: tasks, metrics, traces", "Prove that the workflow works before scaling it."),
            ("Definition", "Compare real scenarios with an agreed quality bar.", "Evaluation uses representative tasks, expected outcomes, failure cases, latency, cost, and trace evidence to support a deployment decision."),
            ("Plain English", "Test the job, not just the answer.", "A fluent response is not enough if the wrong record was updated, a source was missed, or a human was skipped."),
            ("Life sample", "Like taste-testing a meal before serving guests.", "You check the recipe, the normal plate, the allergy case, the delayed ingredient, and whether the cook knows when to ask for help."),
            ("Key point", "Include failures and handoffs in the scorecard.", "A reliable system detects uncertainty, recovers safely, and leaves evidence that a person can inspect."),
            ("Conclusion", "Evidence tells you whether to launch, change, or stop.", "Evaluation turns a prototype conversation into a clear decision about quality, risk, cost, and the next experiment."),
        ],
    },
    "adoption": {
        "title": "ADOPTION",
        "slug": "adoption",
        "voice": [
            ("Adoption", "Keywords: users, training, feedback", "Make the new workflow easy to trust and easy to use."),
            ("Definition", "Help people change how work gets done.", "Adoption covers user roles, training, rollout steps, feedback loops, ownership, support, and the incentives around the new AI workflow."),
            ("Plain English", "AI is a teammate, not a magic button.", "People need to know what the system can do, when to check it, how to correct it, and who owns the final decision."),
            ("Life sample", "Like introducing a new appliance to a family kitchen.", "Start with one cook, show the safe settings, keep the old method nearby, collect feedback, and expand only when it helps."),
            ("Key point", "Start with visible value and a safe fallback.", "Shadow mode, clear review steps, short training, and fast feedback make trust something the team can build."),
            ("Conclusion", "Adoption is part of the system design.", "A deployment succeeds when people choose it because it makes their work clearer, safer, or faster—not because a demo looked impressive."),
        ],
    },
}


def read_env(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip().strip("'\"")
    return values


def tts(text: str, out_file: Path, key: str, region: str) -> None:
    ssml = f"<speak version='1.0' xml:lang='en-US'><voice name='en-US-JennyNeural'><prosody rate='0%' pitch='0%'>{html.escape(text)}</prosody></voice></speak>"
    url = f"https://{region}.tts.speech.microsoft.com/cognitiveservices/v1"
    # curl is used directly because this Azure endpoint occasionally leaves a
    # chunked urllib response open after returning a valid audio body.
    subprocess.run(["curl", "-fsS", "--connect-timeout", "20", "--max-time", "90", "--retry", "4", "--retry-all-errors", "--retry-delay", "1", "-X", "POST", "-H", f"Ocp-Apim-Subscription-Key: {key}", "-H", "Content-Type: application/ssml+xml", "-H", "X-Microsoft-OutputFormat: audio-24khz-160kbitrate-mono-mp3", "-H", "User-Agent: rebecca-enterprise-ai-explainer", "--data-binary", ssml, "-o", str(out_file), url], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def esc(value: str) -> str:
    return value.replace("\\", "\\\\").replace(":", "\\:").replace("'", "\\'").replace(",", "\\,")


def wrap(text: str, width: int) -> str:
    words = text.split()
    lines, current = [], ""
    for word in words:
        if len(current) + len(word) + 1 > width and current:
            lines.append(current)
            current = word
        else:
            current = f"{current} {word}".strip()
    if current:
        lines.append(current)
    return "\\n".join(lines)


def filter_for(stage: int, heading: str, caption: str, topic_index: int) -> str:
    accent = ["0x78e5bd", "0x7fb1ff", "0xffd47f", "0xff9d9d", "0xbaa7ff"][topic_index]
    h = esc(heading.upper())
    cap = esc(wrap(caption, 62))
    # Main copy stays in a bottom caption panel; the center is reserved for the diagram.
    f = [
        "drawbox=x=0:y=0:w=1280:h=720:color=0x071019:t=fill",
        f"drawbox=x=0:y=0:w=1280:h=8:color={accent}:t=fill",
        f"drawtext=fontfile='{BOLD}':text='{h}':fontcolor=white:fontsize=32:x=64:y=46",
        "drawtext=fontfile='" + FONT + "':text='09  /  ENTERPRISE AI DEPLOYMENT':fontcolor=0x9fb0c3:fontsize=18:x=64:y=94",
        "drawbox=x=42:y=584:w=1196:h=104:color=0x0d1b2a@0.96:t=fill",
        "drawbox=x=42:y=584:w=7:h=104:color=" + accent + ":t=fill",
        f"drawtext=fontfile='{FONT}':text='{cap}':fontcolor=white:fontsize=28:line_spacing=8:x=74:y=605",
    ]
    # Distinct central diagrams. Their transitions are the visual explanation.
    if stage == 0:
        f += [
            f"drawbox=x=470:y=238:w=340:h=150:color=0x102b3a@1:t=fill",
            f"drawbox=x=470:y=238:w=340:h=150:color={accent}:t=5",
            f"drawtext=fontfile='{BOLD}':text='AI DEPLOYMENT':fontcolor=white:fontsize=34:x=518:y=295",
            f"drawtext=fontfile='{FONT}':text='keywords':fontcolor={accent}:fontsize=22:x=590:y=355",
        ]
    elif stage == 1:
        for x, label in [(250, "INPUT"), (530, "AI JOB"), (810, "OUTPUT")]:
            f += [f"drawbox=x={x}:y=270:w=200:h=112:color=0x102b3a:t=fill", f"drawbox=x={x}:y=270:w=200:h=112:color={accent}:t=3", f"drawtext=fontfile='{BOLD}':text='{label}':fontcolor=white:fontsize=27:x={x+38}:y=312"]
        f += ["drawtext=fontfile='" + BOLD + "':text='→':fontcolor=0xffffff:fontsize=42:x=473:y=302", "drawtext=fontfile='" + BOLD + "':text='→':fontcolor=0xffffff:fontsize=42:x=753:y=302"]
    elif stage == 2:
        f += [
            f"drawbox=x=380:y=218:w=520:h=60:color=0x163047:t=fill",
            f"drawbox=x=380:y=302:w=410:h=60:color=0x1a384a:t=fill",
            f"drawbox=x=380:y=386:w=300:h=60:color={accent}@0.35:t=fill",
            "drawtext=fontfile='" + BOLD + "':text='TODAY':fontcolor=white:fontsize=25:x=595:y=235",
            "drawtext=fontfile='" + BOLD + "':text='BETTER':fontcolor=white:fontsize=25:x=545:y=319",
            "drawtext=fontfile='" + BOLD + "':text='SAFE':fontcolor=white:fontsize=25:x=490:y=403",
        ]
    elif stage == 3:
        for i, (x, label) in enumerate([(250, "1  NOTICE"), (520, "2  CHECK"), (790, "3  ACT")]):
            y = 250 + i * 45
            f += [f"drawbox=x={x}:y={y}:w=240:h=74:color=0x13283a:t=fill", f"drawbox=x={x}:y={y}:w=240:h=74:color={accent}:t=3", f"drawtext=fontfile='{BOLD}':text='{label}':fontcolor=white:fontsize=23:x={x+22}:y={y+25}"]
        f += ["drawtext=fontfile='" + BOLD + "':text='workflow sample':fontcolor=0x9fb0c3:fontsize=20:x=512:y=470"]
    elif stage == 4:
        f += [
            f"drawbox=x=420:y=230:w=440:h=150:color=0x102b3a:t=fill",
            f"drawbox=x=420:y=230:w=440:h=150:color={accent}:t=5",
            "drawtext=fontfile='" + BOLD + "':text='OWNER':fontcolor=0x9fb0c3:fontsize=20:x=470:y=265",
            "drawtext=fontfile='" + BOLD + "':text='EVIDENCE':fontcolor=0x9fb0c3:fontsize=20:x=610:y=265",
            "drawtext=fontfile='" + BOLD + "':text='FALLBACK':fontcolor=0x9fb0c3:fontsize=20:x=760:y=265",
            f"drawtext=fontfile='{BOLD}':text='✓':fontcolor={accent}:fontsize=66:x=610:y=300",
        ]
    else:
        f += [
            f"drawbox=x=410:y=235:w=460:h=135:color={accent}@0.22:t=fill",
            f"drawbox=x=410:y=235:w=460:h=135:color={accent}:t=5",
            "drawtext=fontfile='" + BOLD + "':text='READY TO LEARN':fontcolor=white:fontsize=34:x=490:y=285",
            "drawtext=fontfile='" + FONT + "':text='discover  →  scope  →  connect  →  prove  →  use':fontcolor=0x9fb0c3:fontsize=20:x=360:y=420",
        ]
    return ",".join(f)


def svg_text(text: str, x: int, y: int, size: int, color: str, weight: str = "400", width: int = 62, line_gap: int = 38) -> str:
    lines = wrap(text, width).split("\\n")
    return "".join(f'<text x="{x}" y="{y + i * line_gap}" fill="{color}" font-family="Arial" font-size="{size}" font-weight="{weight}">{html.escape(line)}</text>' for i, line in enumerate(lines))


def svg_for(stage: int, heading: str, caption: str, topic_index: int) -> str:
    accent = ["#78e5bd", "#7fb1ff", "#ffd47f", "#ff9d9d", "#baa7ff"][topic_index]
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">', '<rect width="1280" height="720" fill="#071019"/>', f'<rect width="1280" height="8" fill="{accent}"/>', svg_text(heading.upper(), 64, 78, 32, "#ffffff", "700", 42), svg_text("09  /  ENTERPRISE AI DEPLOYMENT", 64, 118, 18, "#9fb0c3", "400", 42), '<rect x="42" y="584" width="1196" height="104" rx="8" fill="#0d1b2a"/>', f'<rect x="42" y="584" width="7" height="104" fill="{accent}"/>', svg_text(caption, 74, 625, 28, "#ffffff", "400", 62, 38)]
    def box(x: int, y: int, w: int, h: int, fill: str, stroke: str = "none", sw: int = 0) -> None:
        parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')
    def center(text: str, x: int, y: int, size: int, color: str = "#ffffff", weight: str = "700") -> None:
        parts.append(svg_text(text, x, y, size, color, weight, 34, size + 8))
    if stage == 0:
        box(470, 238, 340, 150, "#102b3a", accent, 5); center("AI DEPLOYMENT", 518, 305, 34); center("keywords", 590, 356, 22, accent)
    elif stage == 1:
        for x, label in [(250, "INPUT"), (530, "AI JOB"), (810, "OUTPUT")]: box(x, 270, 200, 112, "#102b3a", accent, 3); center(label, x + 38, 338, 27)
        center("→", 473, 342, 42); center("→", 753, 342, 42)
    elif stage == 2:
        for y, w, label, fill in [(218, 520, "TODAY", "#163047"), (302, 410, "BETTER", "#1a384a"), (386, 300, "SAFE", accent)]: box(380, y, w, 60, fill, accent if label == "SAFE" else "none", 2); center(label, 380 + int((w - len(label) * 15) / 2), y + 39, 25)
    elif stage == 3:
        for i, (x, label) in enumerate([(250, "1  NOTICE"), (520, "2  CHECK"), (790, "3  ACT")]):
            y = 250 + i * 45; box(x, y, 240, 74, "#13283a", accent, 3); center(label, x + 22, y + 47, 23)
        center("workflow sample", 512, 470, 20, "#9fb0c3", "400")
    elif stage == 4:
        box(420, 230, 440, 150, "#102b3a", accent, 5)
        for x, label in [(470, "OWNER"), (610, "EVIDENCE"), (760, "FALLBACK")]: center(label, x, 275, 20, "#9fb0c3")
        center("✓", 610, 350, 66, accent)
    else:
        box(410, 235, 460, 135, "#173348", accent, 5); center("READY TO LEARN", 490, 315, 34)
        center("discover  →  scope  →  connect  →  prove  →  use", 360, 430, 20, "#9fb0c3", "400")
    parts.append("</svg>")
    return "".join(parts)


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def main() -> None:
    env = {**read_env(ENV_FILE), **os.environ}
    key, region = env.get("AZURE_SPEECH_KEY"), env.get("AZURE_SPEECH_REGION")
    if not key or not region:
        raise SystemExit("Azure speech configuration is missing")
    OUT.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="enterprise-ai-video-") as tmp:
        tmp_path = Path(tmp)
        for topic_index, data in enumerate(TOPICS.values()):
            pieces: list[Path] = []
            for stage, (heading, caption, spoken) in enumerate(data["voice"]):
                audio = tmp_path / f"{data['slug']}-{stage}.mp3"
                segment = tmp_path / f"{data['slug']}-{stage}.mp4"
                frame = tmp_path / f"{data['slug']}-{stage}.svg"
                png = tmp_path / f"{data['slug']}-{stage}.png"
                tts(f"{heading}. {spoken}", audio, key, region)
                duration = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=nw=1:nk=1", str(audio)], text=True).strip())
                frame.write_text(svg_for(stage, heading, caption, topic_index), encoding="utf-8")
                run(["sips", "-s", "format", "png", str(frame), "--out", str(png)])
                frames = max(1, round(duration * 30))
                run(["ffmpeg", "-y", "-loop", "1", "-i", str(png), "-i", str(audio), "-t", f"{duration:.3f}", "-vf", f"zoompan=z='min(zoom+0.0009,1.035)':d=1:s={W}x{H}:fps=30", "-c:v", "libx264", "-preset", "medium", "-crf", "21", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k", "-shortest", str(segment)])
                pieces.append(segment)
            concat = tmp_path / f"{data['slug']}.txt"
            concat.write_text("\n".join(f"file '{p}'" for p in pieces), encoding="utf-8")
            target = OUT / f"{data['slug']}.mp4"
            run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat), "-c", "copy", "-movflags", "+faststart", str(target)])
            print(f"generated {target.name}")


if __name__ == "__main__":
    main()
