#!/usr/bin/env python3
"""Render module 05 explainers with Azure Speech Neural narration.

The Azure key is read only from the existing local .env and is never printed or
written into the repository. Visuals are scene cards rendered by the companion
Swift file, with a small zoom motion per scene and a separate narrated audio
segment for every scene.
"""
from __future__ import annotations

import html
import os
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VIDEO_DIR = ROOT / "vedio"
ENV_PATH = Path("/Users/rebecca/Documents/Codex/2026-09-06/files-pasted-by-the-user-ai/outputs/rebecca-ai-explainer/.env")
VOICE = "en-US-JennyNeural"

TOPICS = {
    "embeddings": [
        "An embedding turns content into coordinates that preserve useful relationships. It helps a machine place similar meanings near each other.",
        "For example, after the vessel sails can land near post-departure cancellation even though the words are different. Embeddings are representations, not answers.",
        "Imagine a librarian pinning every sentence onto a meaning map. A question lands near the policy card that talks about the same idea.",
        "The useful workflow is question to vector, nearby policy chunk, then a careful inspection of the source. Similarity finds a candidate; it does not prove the claim.",
        "The key takeaway is simple: embeddings make meaning searchable. Model choice, chunking, metadata, and source quality still decide whether retrieval works.",
    ],
    "rag": [
        "Retrieval-Augmented Generation, or RAG, retrieves relevant evidence before a language model writes an answer. Retrieve first, generate second.",
        "A RAG system prepares source pages, searches for useful passages, and puts those passages beside the question in the model context.",
        "Imagine an operations assistant asked about a settlement exception. It opens the current policy card first, then drafts an answer and keeps the source with it.",
        "The everyday analogy is a librarian bringing the right page to your desk instead of asking you to trust a memory from years ago.",
        "RAG is useful when knowledge changes, but it cannot repair a missing, stale, inaccessible, or badly chunked source. Retrieval quality needs its own tests.",
    ],
    "vector-search": [
        "Vector search finds items closest to a query in embedding space. It turns a question into a ranked list of candidate evidence.",
        "The basic flow is query, index, and top K. The system can then filter or rerank results using keywords, metadata, permissions, or freshness.",
        "For a delayed shipment claim, the closest cards might describe required documents and the delay policy. A region filter keeps only the current version.",
        "Think of walking to the nearest shelf in a library. The closest book is a strong lead, but you still read the label before using it.",
        "Vector search is a candidate-finding step, not proof. Ranking, access control, freshness, and source quality remain part of retrieval design.",
    ],
    "grounding": [
        "Grounding connects a model response to trusted, task-relevant evidence so a person can inspect the claim.",
        "A grounded workflow selects a source, places it in context, tells the model to stay within that evidence, and preserves a citation or source ID.",
        "For a settlement exception, the answer can cite policy version four point two, section three point one. A reviewer can follow the receipt.",
        "The everyday analogy is a receipt beside a purchase. If the receipt is missing, the honest response is that the claim cannot be confirmed.",
        "Grounding reduces unsupported claims, but it does not make stale or misunderstood evidence automatically correct. Evidence is an honest contract.",
    ],
}


def read_env() -> tuple[str, str]:
    values: dict[str, str] = {}
    for line in ENV_PATH.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    key = values.get("AZURE_SPEECH_KEY") or os.environ.get("AZURE_SPEECH_KEY")
    region = values.get("AZURE_SPEECH_REGION") or os.environ.get("AZURE_SPEECH_REGION")
    if not key or not region:
        raise RuntimeError("Azure Speech configuration is missing")
    return key, region


def azure_wav(text: str, key: str, region: str, output: Path) -> None:
    ssml = (
        "<speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' "
        "xmlns:mstts='http://www.w3.org/2001/mstts' xml:lang='en-US'>"
        f"<voice name='{VOICE}'><prosody rate='0%'>{html.escape(text)}</prosody></voice></speak>"
    ).encode("utf-8")
    endpoint = f"https://{region}.tts.speech.microsoft.com/cognitiveservices/v1"
    ssml_path = output.with_suffix(".ssml")
    ssml_path.write_bytes(ssml)
    try:
        subprocess.run([
            "curl", "-fsS", "--retry", "4", "--retry-all-errors", "--retry-delay", "2",
            "--connect-timeout", "15", "--max-time", "120", "-X", "POST", endpoint,
            "-H", f"Ocp-Apim-Subscription-Key: {key}",
            "-H", "Content-Type: application/ssml+xml",
            "-H", "X-Microsoft-OutputFormat: riff-24khz-16bit-mono-pcm",
            "-H", "User-Agent: module05-explainer-renderer",
            "--data-binary", f"@{ssml_path}", "-o", str(output),
        ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    finally:
        ssml_path.unlink(missing_ok=True)


def run(command: list[str]) -> None:
    subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def duration(path: Path) -> float:
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=nw=1:nk=1", str(path)], check=True, capture_output=True, text=True)
    return float(result.stdout.strip())


def render_topic(slug: str, lines: list[str], key: str, region: str, frames: Path) -> None:
    with tempfile.TemporaryDirectory(prefix=f"module05-{slug}-") as tmp_name:
        tmp = Path(tmp_name)
        segments: list[Path] = []
        for index, narration in enumerate(lines):
            wav = tmp / f"scene-{index:02d}.wav"
            azure_wav(narration, key, region, wav)
            audio_duration = duration(wav)
            segment = tmp / f"scene-{index:02d}.mp4"
            frame = frames / slug / f"scene-{index:02d}.png"
            run([
                "ffmpeg", "-y", "-loop", "1", "-i", str(frame), "-i", str(wav),
                "-vf", "scale=1920:1080:flags=lanczos,format=yuv420p,fade=t=in:st=0:d=0.25",
                "-map", "0:v:0", "-map", "1:a:0", "-c:v", "libx264", "-preset", "medium", "-crf", "20",
                "-t", f"{audio_duration:.3f}", "-c:a", "aac", "-b:a", "160k", "-ar", "24000", "-ac", "1",
                "-shortest", "-movflags", "+faststart", str(segment),
            ])
            segments.append(segment)
        concat = tmp / "concat.txt"
        concat.write_text("\n".join(f"file '{path}'" for path in segments) + "\n", encoding="utf-8")
        output = VIDEO_DIR / f"{slug}.mp4"
        run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat), "-c", "copy", "-movflags", "+faststart", str(output)])
        poster = VIDEO_DIR / f"{slug}.png"
        run(["ffmpeg", "-y", "-ss", "1", "-i", str(output), "-frames:v", "1", "-update", "1", str(poster)])
        print(f"rendered {slug}.mp4 ({duration(output):.1f}s)")


if __name__ == "__main__":
    azure_key, azure_region = read_env()
    with tempfile.TemporaryDirectory(prefix="module05-frames-") as frame_dir:
        frame_root = Path(frame_dir) / "frames"
        run(["swift", str(ROOT / "render_module05_frames.swift"), str(frame_root)])
        for topic_slug, topic_lines in TOPICS.items():
            render_topic(topic_slug, topic_lines, azure_key, azure_region, frame_root)
