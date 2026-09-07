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
    "transformer": [
        "A Transformer is a neural-network architecture that processes relationships between tokens. Its attention mechanism lets the model weigh which parts of the input are useful for each representation or output token.",
        "Think of it like a reading group where every word can look around the table and decide which other words matter for the current task.",
        "The flow is tokens, attention, a repeated stack of attention and feed-forward layers, output scores, and decoding. Text becomes token IDs and vectors; each position weighs relevant context; the stack refines the signal; a final layer scores possible next tokens or task labels.",
        "For pronoun resolution, attention can weigh nearby words and references when a sentence contains it or they. In translation, Transformer layers map relationships across tokens to produce translated text.",
        "A Transformer is an architecture, not an LLM or a product. Attention is one mechanism inside the broader architecture, and a product can use Transformer-based models plus other systems.",
        "Remember this: a Transformer uses attention and stacked neural-network layers to process relationships between tokens.",
    ],
    "token": [
        "A token is a small unit of text processed by a language model. Models process tokens rather than reading text exactly the way humans see words and sentences.",
        "Tokenization can split text in different ways. A familiar English word may be one token or several, long words can be divided into pieces, and Chinese text can use different token units.",
        "Think of tokens as pieces in a model's input stream. The model receives those pieces, predicts token pieces, and turns the sequence back into readable text.",
        "A token is not the same as a word, a character, or a parameter. The exact boundaries depend on the tokenizer and the text.",
        "Remember this: AI models process tokens, not text exactly the way humans see words. Token counts affect context size and usage, but they are not a direct count of words.",
    ],
    "context-window": [
        "The context window is the model's working space. It contains the tokens currently available to the model.",
        "That working space can include system instructions, user messages, uploaded content, retrieved information, tool results, and generated text. Context size is usually measured in tokens.",
        "Think of a context window like a working desk. A long conversation, a large document, or a coding agent can place many items on the desk at once.",
        "A context window is not the same as memory, model knowledge, or maximum answer length. If the desk is full, information may need to be removed, summarized, or retrieved again.",
        "Remember this: the context window is the amount of information a model can work with at one time. It is a runtime boundary, not a guarantee of permanent memory.",
    ],
    "kv-cache": [
        "KV cache is temporary memory used during generation to reuse attention information from earlier tokens. In a Transformer, attention uses key and value states.",
        "Think of KV cache like keeping notes while reading a long document. When you continue reading, you use the notes instead of rereading every earlier page.",
        "The runtime reads the context, creates key and value states, stores them, and uses those cached states when it generates the next token.",
        "As each new token is generated, its key and value states join the cache. The cache uses memory and grows as the sequence grows.",
        "KV cache is not the context window, long-term memory, or model parameters. Remember this: it reuses earlier attention states to make ongoing generation more efficient.",
    ],
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
    "retrieval": [
        "Retrieval is the process of finding and selecting information that is relevant to a query. It returns evidence for a person, an application, or a model.",
        "A retrieval system can combine keywords, vectors, metadata, and filters. It starts by identifying what information the request needs.",
        "The workflow is query, search, rank, filter, and return. Ranking puts useful candidates first; filters can respect access, freshness, and source rules.",
        "Think of finding the right pages in a library. The library holds many pages, but a question needs only a small selection before the next step uses it.",
        "Retrieval finds existing information; it is not generation, and it is not the whole of RAG. Remember: retrieval selects useful evidence before another system or model uses it.",
    ],
}


# Module 07 source of truth: each page is rendered as its own explainer.
TOPICS = {
    "ollama": [
        "Ollama is software that helps you download, run, and manage AI models locally. It provides a runtime around AI models.",
        "Think of Ollama like a media player. The model file is like the movie file, while Ollama is the software that loads and plays it.",
        "A person or local application sends a request to the Ollama API. Ollama loads and manages the selected model, which uses available hardware to generate a response.",
        "For example, Ollama can load a Qwen model for a local chat, serve a local web app through its API, or help switch between several installed models.",
        "Remember: Ollama is not an LLM, model weights, an agent, or ChatGPT. It is software for running and managing AI models locally.",
    ],
    "quantization": [
        "Quantization reduces the numerical precision of a model so it uses less memory and can sometimes run faster. Model parameters are stored as numbers, and quantization represents those values with fewer bits.",
        "Think of it like image compression: a high-resolution image has more detail and a larger file, while a compressed image is smaller but may lose some detail. This is an analogy, not ZIP compression.",
        "The path is original high precision, quantization, a lower-precision representation, and deployment on more limited hardware. Actual behavior depends on the method, runtime, and hardware.",
        "A quantized model may fit on a laptop where full precision does not. It may also help an edge device run a model that would otherwise be impractical.",
        "Remember: quantization saves memory and compute by reducing numerical precision, usually with some trade-off in quality. It is not fine-tuning or a smaller architecture.",
    ],
    "runtime-constraints": [
        "Runtime constraints are limits on the resources, time, cost, and environment available while an AI system is running. They can include memory, compute, latency, token limits, power, network access, concurrency, and deployment location.",
        "Think of it like cooking in a small kitchen. The kitchen limits tools, counter space, ingredients, and time, so the plan must fit the resources available.",
        "The workflow is measure the limits, match a model, configure the workload, test real behavior, and adjust the design. Context, batch size, and concurrency can all matter.",
        "With limited memory, a system might use quantization or a smaller model. With a strict response-time target, it might limit context and use caching or streaming.",
        "Remember: a runtime constraint is not model quality, a product requirement, or a permanent rule. It turns model choice into a real system design decision.",
    ],
    "latency": [
        "Latency is the time between an AI request and the result becoming available. It can include receiving the request, preparing context, running the model, generating tokens, and sending the response.",
        "Think of latency like waiting for a reply on a phone call. The first pause is like time to first token, and the full conversation is like waiting for the complete response.",
        "The path is request, prepare, start, generate, and finish. The application sends prompt and context, the system prepares tokens, then returns output as it grows token by token.",
        "A short chat question with small context and streaming may show first words quickly. A question with a large document may require more context processing before the answer starts.",
        "Remember: latency is not throughput, model quality, or only model speed. It is the total user wait from request to response, including system and network work.",
    ],
    "tokens-per-second": [
        "Tokens per second, or TPS, is the number of output tokens a model generates in one second. It measures generation speed, and tokens are not the same as words.",
        "Think of tokens per second like a printer's pages per minute. A faster printer produces pages sooner, but startup time, document size, and connection also matter.",
        "The loop is input, predict, emit, repeat, and measure. The model receives a request, predicts the next token, returns it, repeats, and divides generated tokens by generation time.",
        "A short answer at forty tokens per second can finish quickly. A detailed report at twenty tokens per second can still take longer because it contains many more output tokens.",
        "Remember: TPS is not words per second, time to first token, or total response time. It is one generation-speed metric inside the whole request experience.",
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
        durations: list[float] = []
        for index, narration in enumerate(lines):
            wav = tmp / f"scene-{index:02d}.wav"
            azure_wav(narration, key, region, wav)
            audio_duration = duration(wav)
            durations.append(audio_duration)
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
        vtt = ["WEBVTT", ""]
        cursor = 0.0
        for index, (line, length) in enumerate(zip(lines, durations), start=1):
            def stamp(value: float) -> str:
                whole = int(value); millis = int(round((value - whole) * 1000))
                if millis == 1000: whole += 1; millis = 0
                return f"00:{whole // 60:02d}:{whole % 60:02d}.{millis:03d}"
            vtt += [f"{index}", f"{stamp(cursor)} --> {stamp(cursor + length)}", line, ""]
            cursor += length
        (VIDEO_DIR / f"{slug}.vtt").write_text("\n".join(vtt), encoding="utf-8")
        print(f"rendered {slug}.mp4 ({duration(output):.1f}s)")


if __name__ == "__main__":
    azure_key, azure_region = read_env()
    with tempfile.TemporaryDirectory(prefix="module05-frames-") as frame_dir:
        frame_root = Path(frame_dir) / "frames"
        run(["swift", str(ROOT / "render_module05_frames.swift"), str(frame_root)])
        for topic_slug in ("ollama", "quantization", "runtime-constraints", "latency", "tokens-per-second"):
            topic_lines = TOPICS[topic_slug]
            render_topic(topic_slug, topic_lines, azure_key, azure_region, frame_root)
