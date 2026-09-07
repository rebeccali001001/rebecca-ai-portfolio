#!/usr/bin/env python3
"""Render the Agent Loop explainer with Azure narration and WebVTT captions."""
from __future__ import annotations

import os
import subprocess
import tempfile
from pathlib import Path

from generate_enterprise_videos import OUT, read_env, svg_for, tts

ENV_FILE = Path("/Users/rebecca/Documents/Codex/2026-09-06/files-pasted-by-the-user-ai/outputs/rebecca-ai-explainer/.env")
TOPIC = "agent-loop"
SCENES = [
    ("Agent Loop", "A controlled cycle of decide, act, observe, and decide again.", "An agent loop is the control cycle that lets an AI system take a step, observe the result, and choose what to do next."),
    ("Route check", "Like checking a route after every turn.", "Think of it like checking a route after every turn. A navigation system observes the road and updates the next turn when conditions change."),
    ("Set the goal", "Define the task and the stopping rules.", "First, the application defines the goal, constraints, and a clear stopping rule for the task."),
    ("Decide and act", "Choose an allowed action, then call the tool.", "The model selects a next step from the allowed options, and the system carries out that approved tool action."),
    ("Observe and validate", "Tool output becomes context for the next decision.", "The tool result becomes new context. Validation and limits keep the loop from continuing blindly or taking an unsafe action."),
    ("Remember", "Finish, ask for review, or repeat within a controlled boundary.", "An agent loop repeats decisions and actions until it reaches a controlled stop condition, returns a result, or asks a person to review."),
]


def run(command: list[str]) -> None:
    subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def seconds(path: Path) -> float:
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=nw=1:nk=1", str(path)], text=True).strip())


def stamp(value: float) -> str:
    millis = round(value * 1000)
    hours, millis = divmod(millis, 3_600_000)
    minutes, millis = divmod(millis, 60_000)
    seconds, millis = divmod(millis, 1000)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}.{millis:03d}"


def main() -> None:
    env = {**read_env(ENV_FILE), **os.environ}
    key, region = env.get("AZURE_SPEECH_KEY"), env.get("AZURE_SPEECH_REGION")
    if not key or not region:
        raise SystemExit("Azure speech configuration is missing")
    OUT.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="agent-loop-video-") as temp_name:
        temp = Path(temp_name)
        clips, captions = [], []
        cursor = 0.0
        for index, (heading, caption, narration) in enumerate(SCENES):
            audio = temp / f"{index}.mp3"
            svg = temp / f"{index}.svg"
            png = temp / f"{index}.png"
            clip = temp / f"{index}.mp4"
            tts(f"{heading}. {narration}", audio, key, region)
            duration = seconds(audio)
            svg.write_text(svg_for(index, heading, caption, 1), encoding="utf-8")
            run(["sips", "-s", "format", "png", str(svg), "--out", str(png)])
            run(["ffmpeg", "-y", "-loop", "1", "-i", str(png), "-i", str(audio), "-t", f"{duration:.3f}", "-vf", "zoompan=z='min(zoom+0.0009,1.035)':d=1:s=1280x720:fps=30", "-c:v", "libx264", "-preset", "medium", "-crf", "21", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k", "-shortest", str(clip)])
            clips.append(clip)
            captions.append((cursor, cursor + duration, f"{heading}. {narration}"))
            cursor += duration
        concat = temp / "concat.txt"
        concat.write_text("\n".join(f"file '{clip}'" for clip in clips), encoding="utf-8")
        video = OUT / f"{TOPIC}.mp4"
        run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat), "-c", "copy", "-movflags", "+faststart", str(video)])
        run(["ffmpeg", "-y", "-ss", "1", "-i", str(video), "-frames:v", "1", "-update", "1", str(OUT / f"{TOPIC}.png")])
        rows = ["WEBVTT", ""]
        for start, end, text in captions:
            rows.extend([f"{stamp(start)} --> {stamp(end)}", text, ""])
        (OUT / f"{TOPIC}.vtt").write_text("\n".join(rows), encoding="utf-8")
        print(f"generated {video.name} ({seconds(video):.1f}s)")


if __name__ == "__main__":
    main()
