#!/usr/bin/env python3
"""Generate the independent Prompting & System Design topic explainers."""
from __future__ import annotations

import subprocess
import tempfile
from pathlib import Path

from generate_enterprise_videos import OUT, FONT, BOLD, W, H, read_env, tts, svg_for

TOPICS = {
    "system-prompts": {
        "title": "SYSTEM PROMPTS", "slug": "system-prompts", "index": 0,
        "voice": [
            ("System Prompts", "Runtime guidance for an AI application.", "A system prompt is a set of instructions sent by an application to guide the model's behavior. It can define a role, rules, boundaries, tone, or output format, but it does not retrain the model."),
            ("Workplace handbook", "Rules arrive before the customer.", "Think of a system prompt like a workplace handbook. It gives an AI application guidance before it handles the current request. The model is not a person, and the rules do not guarantee every response."),
            ("How it works", "Rules, request, context, generation, review.", "The application prepares system instructions, receives the user's request, adds relevant documents or tool results, runs the model, and reviews important output."),
            ("Support and invoices", "Policy-based answers; marked uncertainty.", "For a refund question, the system can follow company policy and avoid inventing rules. For an invoice, it can extract fields and mark uncertain values for review."),
            ("What it is not", "Guidance is not training or guaranteed control.", "A system prompt is application-level guidance, not the user's current request and not model training. It guides likely behavior, but it cannot guarantee that every output follows every rule."),
            ("Remember", "Guide behavior at runtime; validate important results.", "A system prompt guides an AI application's behavior at runtime. It does not guarantee the output, so important results may still need validation."),
        ],
    },
    "structured-outputs": {
        "title": "STRUCTURED OUTPUTS", "slug": "structured-outputs", "index": 1,
        "voice": [
            ("Structured Outputs", "A predictable shape for model responses.", "A structured output is a model response that follows a defined schema or format. The shape can specify fields, types, required values, and allowed options."),
            ("Like filling out a form", "Fields explain what belongs where.", "Think of structured output like filling out a form. The form tells you which fields to complete and what each field means. A schema gives the model a similar shape, but the response still needs validation."),
            ("How it works", "Define, request, generate, validate, handle.", "The application writes a schema, sends the task, asks the model to fill the defined shape, checks types and required values, and then continues or recovers from a validation failure."),
            ("Contacts and invoices", "Extract fields for the next system.", "A message can become a contact object with name, email, and phone fields. An invoice can become the fields required by a finance system, or an error when validation fails."),
            ("What it is not", "Shape is not accuracy or storage.", "Structured output is not plain text, guaranteed accuracy, or database storage. It checks the response's shape and types; the application still needs to check whether values are correct and decide what to store."),
            ("Remember", "Validate before software uses the result.", "Structured outputs make model responses easier for software to validate and use. The related flow is user request, model response, schema validation, then application action."),
        ],
    },
}

def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def main() -> None:
    env = {**read_env(Path("/Users/rebecca/Documents/Codex/2026-09-06/files-pasted-by-the-user-ai/outputs/rebecca-ai-explainer/.env")), **__import__('os').environ}
    key, region = env.get("AZURE_SPEECH_KEY"), env.get("AZURE_SPEECH_REGION")
    if not key or not region:
        raise SystemExit("Azure speech configuration is missing")
    OUT.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="prompting-video-") as tmp:
        tmp_path = Path(tmp)
        for data in TOPICS.values():
            pieces = []
            subtitle_rows = []
            clock = 0.0
            for stage, (heading, caption, spoken) in enumerate(data["voice"]):
                audio = tmp_path / f"{data['slug']}-{stage}.mp3"
                segment = tmp_path / f"{data['slug']}-{stage}.mp4"
                frame = tmp_path / f"{data['slug']}-{stage}.svg"
                png = tmp_path / f"{data['slug']}-{stage}.png"
                tts(f"{heading}. {spoken}", audio, key, region)
                duration = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=nw=1:nk=1", str(audio)], text=True).strip())
                subtitle_rows.append((clock, clock + duration, f"{heading}. {spoken}"))
                clock += duration
                frame.write_text(svg_for(stage, heading, caption, data["index"]), encoding="utf-8")
                run(["sips", "-s", "format", "png", str(frame), "--out", str(png)])
                run(["ffmpeg", "-y", "-loop", "1", "-i", str(png), "-i", str(audio), "-t", f"{duration:.3f}", "-vf", f"zoompan=z='min(zoom+0.0009,1.035)':d=1:s={W}x{H}:fps=30", "-c:v", "libx264", "-preset", "medium", "-crf", "21", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k", "-shortest", str(segment)])
                pieces.append(segment)
            concat = tmp_path / f"{data['slug']}.txt"
            concat.write_text("\n".join(f"file '{p}'" for p in pieces), encoding="utf-8")
            target = OUT / f"{data['slug']}.mp4"
            run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat), "-c", "copy", "-movflags", "+faststart", str(target)])
            # Keep the page's caption and poster contract alongside the MP4.
            subprocess.run(["ffmpeg", "-y", "-i", str(target), "-vf", "select=eq(n\,0)", "-frames:v", "1", str(OUT / f"{data['slug']}.png")], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            def stamp(value: float) -> str:
                whole = int(value); ms = int(round((value - whole) * 1000))
                if ms == 1000: whole += 1; ms = 0
                return f"{whole // 3600:02d}:{(whole % 3600) // 60:02d}:{whole % 60:02d},{ms:03d}"
            srt = [f"{i}\n{stamp(start)} --> {stamp(end)}\n{text}\n" for i, (start, end, text) in enumerate(subtitle_rows, 1)]
            (OUT / f"{data['slug']}.srt").write_text("\n".join(srt), encoding="utf-8")
            print(f"generated {target}")

if __name__ == "__main__":
    main()
