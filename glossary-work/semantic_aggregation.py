from __future__ import annotations

import csv
import re
import unicodedata
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path


BASE = Path.cwd()
RAW_DIR = BASE / "glossary-work" / "raw"
MERGED_DIR = BASE / "glossary-work" / "merged"
AUDIT_DIR = BASE / "glossary-work" / "audit"
ALL_RAW = MERGED_DIR / "all-raw-terms.csv"
OUT_CSV = MERGED_DIR / "semantic-glossary.csv"
OUT_MD = MERGED_DIR / "semantic-glossary.md"
OUT_DUP = AUDIT_DIR / "semantic-duplicates-report.md"
OUT_MISSING = AUDIT_DIR / "missing-terms.md"


HEADER_TERMS = {
    "candidate", "candidate a", "candidate b", "english term", "term",
    "concept", "page wording", "page evidence", "page label",
}


def clean_text(value: str) -> str:
    value = unicodedata.normalize("NFKC", value or "")
    value = value.replace("\u2018", "'").replace("\u2019", "'")
    value = value.replace("\u201c", '"').replace("\u201d", '"')
    value = value.replace("\u2013", "-").replace("\u2014", "-")
    return re.sub(r"\s+", " ", value.strip())


def display_term(value: str) -> str:
    return clean_text(value).strip("`").strip()


def norm(value: str) -> str:
    value = display_term(value).casefold()
    value = value.replace("&", " and ")
    value = re.sub(r"[-_]+", " ", value)
    value = re.sub(r"[^a-z0-9+#./ ]+", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def split_md_row(line: str) -> list[str]:
    return [clean_text(cell) for cell in line.strip().strip("|").split("|")]


def topic_label(file_name: str) -> str:
    stem = Path(file_name).stem
    stem = re.sub(r"^\d+-", "", stem)
    replacements = {
        "artificial-intelligence": "Artificial Intelligence",
        "deep-learning": "Deep Learning",
        "machine-learning": "Machine Learning",
        "reinforcement-learning": "Reinforcement Learning",
        "supervised-learning": "Supervised Learning",
        "unsupervised-learning": "Unsupervised Learning",
        "cnn": "CNN",
        "rnn-lstm": "RNN / LSTM",
        "gpu-vram-unified-memory": "GPU, VRAM & Unified Memory",
        "kv-cache": "KV Cache",
        "tokens-per-second": "Tokens per Second",
        "local-vs-cloud": "Local AI vs Cloud AI",
        "mcp": "Model Context Protocol (MCP)",
        "ai-agent": "AI Agent",
        "human-in-the-loop": "Human in the Loop",
        "skills-plugins": "Skills / Plugins",
        "multi-agent-systems": "Multi-Agent Systems",
        "major-ai-providers": "Major AI Providers",
        "model-types-families": "Model Types & Families",
        "open-closed-local-models": "Open vs Closed / Local Models",
        "ai-assistants-coding-tools": "AI Assistants & Coding Tools",
        "general-agents-computer-use": "General Agents & Computer Use",
        "agent-frameworks": "Agent Frameworks",
        "how-agents-are-built": "How AI Agents Are Built",
        "ai-workflow-platforms": "AI Workflow Platforms",
        "automation-platforms": "Automation Platforms",
        "data-api-authentication": "Data, APIs & Authentication",
        "deployment-operations": "Deployment & Operations",
        "frontend-backend": "Frontend & Backend",
        "backend-data-platforms": "Backend & Data Platforms",
        "developer-platforms": "Developer Platforms",
        "web-cloud-platforms": "Web & Cloud Platforms",
        "backend-technologies": "Backend Technologies",
        "data-technologies": "Data Technologies",
        "frontend-technologies": "Frontend Technologies",
        "product-services": "Product Services",
    }
    if stem in replacements:
        return replacements[stem]
    return re.sub(r"\b\w", lambda m: m.group(0).upper(), stem.replace("-", " "))


@dataclass
class Candidate:
    term: str
    cn: str
    simple: str
    explain: str
    module: str
    topic: str
    raw_file: str
    source_file: str = ""
    source_kind: str = "all-raw"


@dataclass
class Group:
    term: str
    module: str
    anchor_file: str
    aliases: list[str] = field(default_factory=list)
    manual_cn: str = ""
    manual_simple: str = ""
    manual_explain: str = ""
    rows: list[Candidate] = field(default_factory=list)


GROUPS: list[Group] = []


def add(module: str, anchor_file: str, term: str, *aliases: str) -> None:
    GROUPS.append(Group(term, module, anchor_file, [term, *aliases]))


# Core concepts and methods. The list is intentionally explicit: it is the
# semantic allow-list, while the raw files remain the evidence universe.
def define_groups() -> None:
    # 01 — AI and machine-learning fundamentals
    add("01", "01-artificial-intelligence.md", "Artificial Intelligence (AI)", "Artificial Intelligence", "AI")
    add("01", "01-machine-learning.md", "Machine Learning (ML)", "Machine Learning", "ML")
    add("01", "01-deep-learning.md", "Deep Learning (DL)", "Deep Learning", "DL")
    add("01", "01-supervised-learning.md", "Supervised Learning")
    add("01", "01-unsupervised-learning.md", "Unsupervised Learning")
    add("01", "01-reinforcement-learning.md", "Reinforcement Learning (RL)", "Reinforcement Learning", "RL")
    add("01", "01-machine-learning.md", "Self-Supervised Learning", "self-supervised learning")
    add("01", "01-machine-learning.md", "Semi-Supervised Learning", "semi-supervised learning")
    add("01", "01-machine-learning.md", "Algorithm")
    add("01", "01-machine-learning.md", "Dataset", "data set", "data-set")
    add("01", "01-machine-learning.md", "Training Data")
    add("01", "01-machine-learning.md", "Feature")
    add("01", "01-supervised-learning.md", "Label")
    add("01", "01-supervised-learning.md", "Target Variable", "target")
    add("01", "01-machine-learning.md", "Prediction")
    add("01", "01-supervised-learning.md", "Classification")
    add("01", "01-supervised-learning.md", "Regression")
    add("01", "01-unsupervised-learning.md", "Clustering")
    add("01", "01-unsupervised-learning.md", "Dimensionality Reduction")
    add("01", "01-machine-learning.md", "Recommendation System", "recommender system")
    add("01", "01-artificial-intelligence.md", "Pattern Recognition")
    add("01", "01-deep-learning.md", "Generalization")
    add("01", "01-deep-learning.md", "Overfitting")
    add("01", "01-deep-learning.md", "Underfitting")
    add("01", "01-deep-learning.md", "Hyperparameter")
    add("01", "01-deep-learning.md", "Weight", "model weight", "model weights", "weights")
    add("01", "01-deep-learning.md", "Bias", "bias term", "model bias parameter")
    add("01", "01-deep-learning.md", "Activation")
    add("01", "01-deep-learning.md", "Activation Function")
    add("01", "01-deep-learning.md", "Loss Function")
    add("01", "01-deep-learning.md", "Cross-Entropy Loss", "cross entropy loss")
    add("01", "01-deep-learning.md", "Mean Squared Error (MSE)", "mean squared error", "MSE")
    add("01", "01-deep-learning.md", "Gradient")
    add("01", "01-deep-learning.md", "Gradient Descent")
    add("01", "01-deep-learning.md", "Backpropagation", "back propagation")
    add("01", "01-deep-learning.md", "Optimizer")
    add("01", "01-deep-learning.md", "Learning Rate")
    add("01", "01-deep-learning.md", "Epoch")
    add("01", "01-deep-learning.md", "Batch")
    add("01", "01-deep-learning.md", "Mini-Batch", "mini batch")
    add("01", "01-deep-learning.md", "Batch Size", "batch size")
    add("01", "01-machine-learning.md", "Training Set")
    add("01", "01-machine-learning.md", "Validation Set")
    add("01", "01-machine-learning.md", "Test Set")
    add("01", "01-machine-learning.md", "Train/Validation/Test Split", "training validation test split")
    add("01", "01-machine-learning.md", "Data Preprocessing", "preprocessing", "data preprocessing")
    add("01", "01-machine-learning.md", "Data Augmentation")
    add("01", "01-machine-learning.md", "Data Curation")
    add("01", "01-machine-learning.md", "Data Quality")
    add("01", "01-machine-learning.md", "Data Leakage")
    add("01", "01-machine-learning.md", "Data Contamination", "contamination")
    add("01", "01-machine-learning.md", "Synthetic Data")
    add("01", "01-machine-learning.md", "Transfer Learning")
    add("01", "01-artificial-intelligence.md", "AI Product", "AI application")
    add("01", "01-artificial-intelligence.md", "Search Engine")
    add("01", "01-artificial-intelligence.md", "Responsible AI")

    # 02 — neural-network and model architectures
    add("02", "02-neural-networks.md", "Neural Network", "neural networks", "neural net")
    add("02", "02-neural-networks.md", "Neural Network Architecture", "neural-network architecture")
    add("02", "02-layers.md", "Layer", "layers", "neural network layer")
    add("02", "02-layers.md", "Hidden Layer", "hidden layers")
    add("02", "02-neural-networks.md", "Computational Unit", "computational units")
    add("02", "02-neural-networks.md", "Deep Neural Network (DNN)", "deep neural network", "DNN")
    add("02", "02-neural-networks.md", "Feed-Forward Network", "feed-forward network", "feedforward network")
    add("02", "02-attention.md", "Attention", "attention mechanism")
    add("02", "02-attention.md", "Self-Attention", "self attention")
    add("02", "02-attention.md", "Multi-Head Attention", "multi-head attention")
    add("02", "02-attention.md", "Cross-Attention", "cross attention")
    add("02", "02-attention.md", "Scaled Dot-Product Attention", "scaled dot product attention")
    add("02", "02-attention.md", "Attention Head")
    add("02", "02-attention.md", "Attention Mask")
    add("02", "02-attention.md", "Attention Weight")
    add("02", "02-transformer.md", "Transformer")
    add("02", "02-transformer.md", "Transformer Architecture")
    add("02", "02-transformer.md", "Transformer Block")
    add("02", "02-transformer.md", "Transformer Layer")
    add("02", "02-transformer.md", "Encoder")
    add("02", "02-transformer.md", "Decoder")
    add("02", "02-transformer.md", "Encoder-Only Model", "encoder only model")
    add("02", "02-transformer.md", "Decoder-Only Model", "decoder only model")
    add("02", "02-transformer.md", "Encoder-Decoder Model", "encoder decoder model")
    add("02", "02-transformer.md", "Feed-Forward Network", "feed forward network", "FFN")
    add("02", "02-transformer.md", "Residual Connection", "residual connections")
    add("02", "02-transformer.md", "Layer Normalization", "layer norm", "layer normalization")
    add("02", "02-transformer.md", "Positional Encoding", "position encoding", "position embedding")
    add("02", "02-cnn.md", "Convolution")
    add("02", "02-cnn.md", "Convolutional Neural Network (CNN)", "convolutional neural network", "CNN")
    add("02", "02-cnn.md", "Convolution Kernel", "convolution filter", "convolution filters", "kernel")
    add("02", "02-cnn.md", "Pooling", "pooling layer")
    add("02", "02-cnn.md", "Image Classification")
    add("02", "02-cnn.md", "Edge Detection")
    add("02", "02-rnn-lstm.md", "Recurrent Neural Network (RNN)", "recurrent neural network", "RNN")
    add("02", "02-rnn-lstm.md", "Long Short-Term Memory (LSTM)", "long short-term memory", "LSTM")
    add("02", "02-rnn-lstm.md", "Hidden State")
    add("02", "02-rnn-lstm.md", "Sequence Model")
    add("02", "02-diffusion-models.md", "Diffusion Model")
    add("02", "02-diffusion-models.md", "Denoising", "denoising process")
    add("02", "02-diffusion-models.md", "Noise Schedule")
    add("02", "02-diffusion-models.md", "Generative Adversarial Network (GAN)", "generative adversarial network", "GAN")
    add("02", "02-diffusion-models.md", "Autoencoder")
    add("02", "02-diffusion-models.md", "Variational Autoencoder (VAE)", "variational autoencoder", "VAE")
    add("02", "02-diffusion-models.md", "Vision Transformer (ViT)", "vision transformer", "ViT")
    add("02", "02-neural-networks.md", "Representation")
    add("02", "02-neural-networks.md", "Feature Representation")
    add("02", "02-neural-networks.md", "Feature Vector")

    # 03 — model types, modalities, and parameterized models
    add("03", "03-foundation-models.md", "Foundation Model")
    add("03", "03-large-language-models.md", "Large Language Model (LLM)", "large language model", "LLM")
    add("03", "03-large-language-models.md", "Small Language Model (SLM)", "small language model", "SLM")
    add("03", "03-large-language-models.md", "Language Model")
    add("03", "03-multimodal-models.md", "Multimodal Model")
    add("03", "03-multimodal-models.md", "Vision-Language Model (VLM)", "vision-language model", "VLM")
    add("03", "03-vision-foundation-models.md", "Vision Foundation Model")
    add("03", "03-speech-audio-models.md", "Speech Model")
    add("03", "03-speech-audio-models.md", "Audio-Language Model")
    add("03", "03-speech-audio-models.md", "Automatic Speech Recognition (ASR)", "automatic speech recognition", "ASR", "speech recognition")
    add("03", "03-speech-audio-models.md", "Text-to-Speech (TTS)", "text-to-speech", "TTS", "speech synthesis", "text-to-speech generation")
    add("03", "03-multimodal-models.md", "Modality")
    add("03", "03-multimodal-models.md", "Input Modality")
    add("03", "03-multimodal-models.md", "Output Modality")
    add("03", "03-multimodal-models.md", "Modality Fusion")
    add("03", "03-multimodal-models.md", "Image Captioning")
    add("03", "03-multimodal-models.md", "Visual Question Answering (VQA)", "visual question answering", "VQA")
    add("03", "03-vision-foundation-models.md", "Optical Character Recognition (OCR)", "optical character recognition", "OCR")
    add("03", "03-multimodal-models.md", "Image-Text Alignment")
    add("03", "03-multimodal-models.md", "Image-Text Contrastive Learning")
    add("03", "03-multimodal-models.md", "Image-to-Text")
    add("03", "03-multimodal-models.md", "Text-to-Audio")
    add("03", "03-parameters.md", "Model Parameter", "model parameters", "parameter", "parameters")
    add("03", "03-parameters.md", "Model Size")
    add("03", "03-parameters.md", "Parameter Count")
    add("03", "03-parameters.md", "Model Capacity")
    add("03", "03-scientific-models.md", "Scientific Model")
    add("03", "03-scientific-models.md", "Scientific Foundation Model")
    add("03", "03-foundation-models.md", "Pre-Trained Model", "pretrained model", "pre-trained model")
    add("03", "03-foundation-models.md", "Base Model")
    add("03", "03-foundation-models.md", "General-Purpose Model", "general purpose model")
    add("03", "03-foundation-models.md", "Specialized Model", "specialized models")
    add("03", "03-foundation-models.md", "Model API", "model api")
    add("03", "03-foundation-models.md", "Model Runtime")
    add("03", "03-foundation-models.md", "Checkpoint", "model checkpoint")

    # 04 — pre-training, fine-tuning, and alignment
    add("04", "04-pre-training.md", "Pre-Training", "pretraining", "pre-training")
    add("04", "04-pre-training.md", "Training", "model training", "training process")
    add("04", "04-pre-training.md", "Pre-Training Objective", "training objective")
    add("04", "04-pre-training.md", "Next-Token Prediction", "next token prediction", "next-token prediction")
    add("04", "04-pre-training.md", "Missing-Token Prediction", "missing token prediction", "missing-token prediction")
    add("04", "04-pre-training.md", "Masked Language Modeling", "masked language model", "MLM")
    add("04", "04-pre-training.md", "Causal Language Modeling", "causal language model")
    add("04", "04-pre-training.md", "Autoregressive Modeling", "autoregressive model")
    add("04", "04-fine-tuning.md", "Fine-Tuning", "fine tuning", "fine-tuning")
    add("04", "04-fine-tuning.md", "Supervised Fine-Tuning (SFT)", "supervised fine-tuning", "SFT")
    add("04", "04-instruction-tuning.md", "Instruction Tuning", "instruction tuning")
    add("04", "04-fine-tuning.md", "Parameter-Efficient Fine-Tuning (PEFT)", "parameter-efficient fine-tuning", "PEFT")
    add("04", "04-fine-tuning.md", "Low-Rank Adaptation (LoRA)", "low-rank adaptation", "LoRA")
    add("04", "04-preference-learning-rlhf.md", "Preference Learning")
    add("04", "04-preference-learning-rlhf.md", "Reinforcement Learning from Human Feedback (RLHF)", "reinforcement learning from human feedback", "RLHF", "rlHF")
    add("04", "04-preference-learning-rlhf.md", "Human Feedback")
    add("04", "04-preference-learning-rlhf.md", "Reward Model")
    add("04", "04-preference-learning-rlhf.md", "Preference Model")
    add("04", "04-preference-learning-rlhf.md", "Reward Signal")
    add("04", "04-training-data.md", "Data Curation")
    add("04", "04-training-data.md", "Training Example")
    add("04", "04-training-data.md", "Training Pipeline")
    add("04", "04-training-data.md", "Data Provenance")
    add("04", "04-training-data.md", "Dataset Quality")
    add("04", "04-training-data.md", "Deduplication")
    add("04", "04-training-data.md", "Data Filtering")
    add("04", "04-training-data.md", "Label Quality")
    add("04", "04-preference-learning-rlhf.md", "Alignment")
    add("04", "04-preference-learning-rlhf.md", "Alignment Training")
    add("04", "04-preference-learning-rlhf.md", "Specification Gaming")
    add("04", "04-fine-tuning.md", "Catastrophic Forgetting")

    # 05 — inference, context, tokens, and decoding
    add("05", "05-inference.md", "Inference")
    add("05", "05-inference.md", "Inference Pipeline")
    add("05", "05-inference.md", "Inference Request")
    add("05", "05-context-window.md", "Context Window")
    add("05", "05-context-window.md", "Context Length")
    add("05", "05-context-window.md", "Context Budget", "token budget")
    add("05", "05-context-window.md", "Context Overflow")
    add("05", "05-token.md", "Token")
    add("05", "05-token.md", "Input Token")
    add("05", "05-token.md", "Output Token")
    add("05", "05-token.md", "Token Sequence")
    add("05", "05-tokenization.md", "Tokenization")
    add("05", "05-tokenization.md", "Tokenizer")
    add("05", "05-tokenization.md", "Subword Token")
    add("05", "05-tokenization.md", "Special Token")
    add("05", "05-next-token-prediction.md", "Logit", "logits")
    add("05", "05-next-token-prediction.md", "Softmax")
    add("05", "05-sampling-temperature.md", "Sampling")
    add("05", "05-sampling-temperature.md", "Temperature")
    add("05", "05-sampling-temperature.md", "Top-k Sampling", "top-k")
    add("05", "05-sampling-temperature.md", "Top-p Sampling", "top-p", "nucleus sampling")
    add("05", "05-sampling-temperature.md", "Greedy Decoding", "greedy decoding")
    add("05", "05-sampling-temperature.md", "Beam Search", "beam search")
    add("05", "05-sampling-temperature.md", "Decoding")
    add("05", "05-token.md", "End-of-Sequence Token (EOS)", "end-of-sequence token", "EOS")
    add("05", "05-token.md", "Stop Sequence", "stop sequences")
    add("05", "05-token.md", "Maximum Output Length", "max output length")
    add("05", "05-kv-cache.md", "Key-Value Cache (KV Cache)", "key-value cache", "key-value (KV) cache", "KV cache", "KV Cache")
    add("05", "05-kv-cache.md", "Prefill")
    add("05", "05-kv-cache.md", "Decode Phase", "decode phase", "decoding phase")
    add("05", "05-next-token-prediction.md", "Autoregressive Generation", "autoregressive generation")
    add("05", "05-next-token-prediction.md", "Next-Token Prediction", "next token prediction", "next-token prediction")

    # 06 — prompts, context engineering, and structured outputs
    add("06", "06-prompt-design.md", "Prompt")
    add("06", "06-prompt-design.md", "Prompt Engineering", "prompt engineering", "prompting", "prompt design")
    add("06", "06-prompt-design.md", "Prompt Template", "prompt templates")
    add("06", "06-system-prompts.md", "System Prompt", "system prompts", "system instruction")
    add("06", "06-prompt-design.md", "User Prompt", "user prompts")
    add("06", "06-prompt-design.md", "Few-Shot Prompting", "few-shot prompting", "few shot prompting")
    add("06", "06-prompt-design.md", "Zero-Shot Prompting", "zero-shot prompting", "zero shot prompting")
    add("06", "06-prompt-design.md", "In-Context Learning", "in context learning")
    add("06", "06-prompt-design.md", "Chain-of-Thought", "chain of thought", "CoT")
    add("06", "06-context-engineering.md", "Context Engineering")
    add("06", "06-context-engineering.md", "Context Assembly", "context building")
    add("06", "06-context-engineering.md", "Context Grounding")
    add("06", "06-structured-outputs.md", "Structured Output", "structured outputs")
    add("06", "06-structured-outputs.md", "Output Schema", "schema")
    add("06", "06-structured-outputs.md", "JSON")
    add("06", "06-structured-outputs.md", "JSON Schema")
    add("06", "06-structured-outputs.md", "Output Parser", "parser")
    add("06", "06-structured-outputs.md", "Schema Validation")
    add("06", "06-prompt-design.md", "Prompt Chaining")
    add("06", "06-system-prompts.md", "Instruction Hierarchy")

    # 07 — generative and multimodal capabilities
    add("07", "07-generative-ai.md", "Generative AI")
    add("07", "07-generative-ai.md", "Generative Model")
    add("07", "07-text-generation.md", "Text Generation")
    add("07", "07-image-generation.md", "Image Generation")
    add("07", "07-video-generation.md", "Video Generation")
    add("07", "07-audio-generation.md", "Audio Generation")
    add("07", "07-code-generation.md", "Code Generation")
    add("07", "07-multimodal-ai.md", "Multimodal AI")
    add("07", "07-image-generation.md", "Image Generator")
    add("07", "07-image-generation.md", "Text-to-Image Generation", "text-to-image")
    add("07", "07-image-generation.md", "Image-to-Image Generation", "image-to-image")
    add("07", "07-video-generation.md", "Text-to-Video Generation", "text-to-video")
    add("07", "07-audio-generation.md", "Voice Cloning")
    add("07", "07-image-generation.md", "Inpainting")
    add("07", "07-image-generation.md", "Outpainting")
    add("07", "07-text-generation.md", "Conditional Generation")
    add("07", "07-code-generation.md", "Code Completion")
    add("07", "07-code-generation.md", "Code Review")
    add("07", "07-multimodal-ai.md", "Modality")

    # 08 — embeddings, search, retrieval, RAG, and grounding
    add("08", "08-embeddings.md", "Embedding", "embeddings")
    add("08", "08-embeddings.md", "Embedding Model")
    add("08", "08-embeddings.md", "Vector Representation", "vector representations")
    add("08", "08-embeddings.md", "Vector")
    add("08", "08-vector-database.md", "Vector Database")
    add("08", "08-vector-database.md", "Vector Index")
    add("08", "08-vector-search.md", "Vector Search")
    add("08", "08-semantic-search.md", "Semantic Search")
    add("08", "08-retrieval.md", "Search")
    add("08", "08-retrieval.md", "Search Query", "search query")
    add("08", "08-retrieval.md", "Keyword Search")
    add("08", "08-semantic-search.md", "Hybrid Search")
    add("08", "08-retrieval.md", "Similarity Search")
    add("08", "08-retrieval.md", "Retrieval")
    add("08", "08-retrieval.md", "Retriever")
    add("08", "08-rag.md", "Retrieval-Augmented Generation (RAG)", "retrieval-augmented generation", "retrieval augmented generation", "RAG")
    add("08", "08-reranking.md", "Reranking", "re-ranking", "rerank", "re-rank")
    add("08", "08-reranking.md", "Reranker")
    add("08", "08-reranking.md", "Cross-Encoder")
    add("08", "08-reranking.md", "Bi-Encoder")
    add("08", "08-chunking.md", "Chunk")
    add("08", "08-chunking.md", "Chunking", "document chunking")
    add("08", "08-chunking.md", "Chunk Overlap")
    add("08", "08-rag.md", "Knowledge Base", "knowledge database")
    add("08", "08-rag.md", "Document Corpus", "corpus", "source collection")
    add("08", "08-grounding.md", "Grounding")
    add("08", "08-grounding.md", "Groundedness")
    add("08", "08-grounding.md", "Faithfulness")
    add("08", "08-grounding.md", "Citation")
    add("08", "08-grounding.md", "Source Attribution")
    add("08", "08-rag.md", "Context Retrieval")
    add("08", "08-retrieval.md", "Top-k Retrieval", "top k retrieval")
    add("08", "08-retrieval.md", "Retrieval Pipeline")
    add("08", "08-retrieval.md", "Query Rewriting")
    add("08", "08-vector-search.md", "Approximate Nearest Neighbor (ANN)", "approximate nearest neighbor", "ANN")

    # 09 — agents and tool use
    add("09", "09-ai-agent.md", "AI Agent", "AI agents", "agent")
    add("09", "09-agent-loop.md", "Agent Loop", "agent loop")
    add("09", "09-agent-loop.md", "Agent-Environment Interaction", "agent environment interaction")
    add("09", "09-ai-agent.md", "Agent System", "agentic system", "agent system")
    add("09", "09-ai-agent.md", "Agent Goal", "user goal")
    add("09", "09-memory-state.md", "Agent State", "state", "state management", "state persistence")
    add("09", "09-memory-state.md", "Agent Memory", "memory", "memory component")
    add("09", "09-memory-state.md", "Short-Term Memory", "short-term memory")
    add("09", "09-memory-state.md", "Long-Term Memory", "long-term memory")
    add("09", "09-memory-state.md", "Persistent Memory")
    add("09", "09-planning.md", "Planning")
    add("09", "09-planning.md", "Task Decomposition")
    add("09", "09-planning.md", "Plan")
    add("09", "09-planning.md", "Reasoning")
    add("09", "09-tool-calling.md", "Tool Calling", "tool calling", "tool call")
    add("09", "09-tool-calling.md", "Function Calling", "function calling")
    add("09", "09-tool-calling.md", "Tool Use", "tool use")
    add("09", "09-tool-calling.md", "Tool")
    add("09", "09-tool-calling.md", "Tool Schema")
    add("09", "09-tool-calling.md", "Tool Result")
    add("09", "09-agent-loop.md", "Action")
    add("09", "09-agent-loop.md", "Observation")
    add("09", "09-human-in-the-loop.md", "Human-in-the-Loop (HITL)", "human in the loop", "HITL")
    add("09", "09-human-in-the-loop.md", "Human Oversight")
    add("09", "09-human-in-the-loop.md", "Approval Gate", "approval checkpoint")
    add("09", "09-multi-agent-systems.md", "Multi-Agent System", "multi-agent system", "multi-agent systems")
    add("09", "09-multi-agent-systems.md", "Agent Collaboration")
    add("09", "09-multi-agent-systems.md", "Agent Delegation")
    add("09", "09-mcp.md", "Model Context Protocol (MCP)", "Model Context Protocol", "MCP")
    add("09", "09-mcp.md", "MCP Server")
    add("09", "09-mcp.md", "MCP Client")
    add("09", "09-skills-plugins.md", "Skill")
    add("09", "09-skills-plugins.md", "Plugin")
    add("09", "09-skills-plugins.md", "Agent Framework")
    add("09", "09-agent-loop.md", "Workflow Orchestration", "orchestration")

    # 10 — APIs, runtimes, serving, and performance
    add("10", "10-api.md", "Application Programming Interface (API)", "Application Programming Interface", "API")
    add("10", "10-api.md", "API Endpoint", "endpoint")
    add("10", "10-api.md", "API Request", "api request")
    add("10", "10-api.md", "API Response", "api response")
    add("10", "10-api.md", "Software Development Kit (SDK)", "software development kit", "SDK")
    add("10", "10-model-serving.md", "Model Serving")
    add("10", "10-model-serving.md", "Inference Server")
    add("10", "10-model-serving.md", "Model Runtime", "runtime")
    add("10", "10-runtime-constraints.md", "Runtime Constraints", "runtime constraint")
    add("10", "10-gpu-vram-unified-memory.md", "GPU")
    add("10", "10-gpu-vram-unified-memory.md", "CPU")
    add("10", "10-gpu-vram-unified-memory.md", "VRAM")
    add("10", "10-gpu-vram-unified-memory.md", "Unified Memory")
    add("10", "10-gpu-vram-unified-memory.md", "Memory Footprint")
    add("10", "10-gpu-vram-unified-memory.md", "Compute")
    add("10", "10-local-vs-cloud.md", "Local AI")
    add("10", "10-local-vs-cloud.md", "Cloud AI")
    add("10", "10-local-vs-cloud.md", "Self-Hosted Model", "self-hosted", "self hosted")
    add("10", "10-local-vs-cloud.md", "Edge Inference")
    add("10", "10-quantization.md", "Quantization")
    add("10", "10-quantization.md", "Model Compression")
    add("10", "10-quantization.md", "Mixed Precision")
    add("10", "10-quantization.md", "Numerical Precision", "parameter precision", "original precision")
    add("10", "10-model-serving.md", "Batch Inference")
    add("10", "10-model-serving.md", "Dynamic Batching")
    add("10", "10-vllm.md", "Continuous Batching")
    add("10", "10-vllm.md", "Paged Attention")
    add("10", "10-latency.md", "Latency", "response time")
    add("10", "10-latency.md", "Latency Breakdown")
    add("10", "10-latency.md", "Time to First Token (TTFT)", "time to first token", "TTFT")
    add("10", "10-latency.md", "Throughput")
    add("10", "10-tokens-per-second.md", "Tokens per Second (TPS)", "tokens per second", "token per second", "TPS", "token throughput")
    add("10", "10-vllm.md", "vLLM")
    add("10", "10-ollama.md", "Ollama")
    add("10", "10-vllm.md", "Tensor Parallelism")
    add("10", "10-vllm.md", "Pipeline Parallelism")
    add("10", "10-model-serving.md", "Inference Optimization")
    add("10", "10-latency.md", "Cost per Token")

    # 11 — evaluation, failures, safety, and permissions
    add("11", "11-evaluation.md", "Evaluation", "model evaluation")
    add("11", "11-benchmarks.md", "Benchmark")
    add("11", "11-benchmarks.md", "Benchmark Dataset")
    add("11", "11-evaluation.md", "Evaluation Metric")
    add("11", "11-evaluation.md", "Accuracy")
    add("11", "11-evaluation.md", "Precision")
    add("11", "11-evaluation.md", "Recall")
    add("11", "11-evaluation.md", "F1 Score", "F1 score")
    add("11", "11-evaluation.md", "Confusion Matrix")
    add("11", "11-evaluation.md", "Calibration")
    add("11", "11-evaluation.md", "Offline Evaluation")
    add("11", "11-evaluation.md", "Online Evaluation")
    add("11", "11-evaluation.md", "Human Evaluation")
    add("11", "11-evaluation.md", "Model-Based Evaluation", "model based evaluation")
    add("11", "11-evaluation.md", "LLM-as-a-Judge", "LLM as a judge")
    add("11", "11-functional-tests.md", "Functional Test")
    add("11", "11-functional-tests.md", "Regression Test")
    add("11", "11-functional-tests.md", "End-to-End Test", "end to end test")
    add("11", "11-functional-tests.md", "Test Case")
    add("11", "11-failure-modes.md", "Failure Mode")
    add("11", "11-failure-handling.md", "Failure Handling")
    add("11", "11-failure-handling.md", "Retry")
    add("11", "11-failure-handling.md", "Fallback")
    add("11", "11-failure-handling.md", "Timeout")
    add("11", "11-failure-handling.md", "Error Handling")
    add("11", "11-hallucination.md", "Hallucination")
    add("11", "11-hallucination.md", "Factuality")
    add("11", "11-hallucination.md", "Unsupported Claim")
    add("11", "11-hallucination.md", "Fabricated Content")
    add("11", "11-guardrails.md", "Guardrail")
    add("11", "11-guardrails.md", "Safety Filter")
    add("11", "11-guardrails.md", "Content Filter")
    add("11", "11-guardrails.md", "Content Moderation", "moderation")
    add("11", "11-prompt-injection.md", "Prompt Injection")
    add("11", "11-prompt-injection.md", "Prompt Leakage")
    add("11", "11-prompt-injection.md", "Jailbreak")
    add("11", "11-guardrails.md", "Adversarial Attack")
    add("11", "11-guardrails.md", "Red Teaming", "red teaming")
    add("11", "11-guardrails.md", "Toxicity")
    add("11", "11-permissions-safety.md", "Privacy")
    add("11", "11-permissions-safety.md", "Personally Identifiable Information (PII)", "personally identifiable information", "PII")
    add("11", "11-permissions-safety.md", "Permission")
    add("11", "11-permissions-safety.md", "Access Control")
    add("11", "11-permissions-safety.md", "Authentication")
    add("11", "11-permissions-safety.md", "Authorization")
    add("11", "11-permissions-safety.md", "Least Privilege")
    add("11", "11-permissions-safety.md", "Audit Log")
    add("11", "11-permissions-safety.md", "Fairness")
    add("11", "11-permissions-safety.md", "Explainability")
    add("11", "11-permissions-safety.md", "Human Review")
    add("11", "11-deployment-readiness.md", "Deployment Readiness")
    add("11", "11-deployment-readiness.md", "Release Gate", "readiness gate")

    # 12 — product lifecycle and operations
    add("12", "12-adoption.md", "AI Adoption", "adoption")
    add("12", "12-adoption.md", "Workflow Fit")
    add("12", "12-workflow-discovery.md", "Workflow Discovery")
    add("12", "12-technical-scoping.md", "Technical Scoping")
    add("12", "12-integration.md", "Integration")
    add("12", "12-deployment.md", "Deployment")
    add("12", "12-monitoring.md", "Monitoring")
    add("12", "12-monitoring.md", "Observability")
    add("12", "12-monitoring.md", "Production Monitoring")
    add("12", "12-continuous-improvement.md", "Continuous Improvement")
    add("12", "12-monitoring.md", "Data Drift")
    add("12", "12-monitoring.md", "Concept Drift")
    add("12", "12-monitoring.md", "Schema Drift")
    add("12", "12-monitoring.md", "Error Rate")
    add("12", "12-deployment.md", "Availability")
    add("12", "12-deployment.md", "Reliability")
    add("12", "12-deployment.md", "Rollback")
    add("12", "12-deployment.md", "Canary Deployment")
    add("12", "12-deployment.md", "A/B Test", "A/B testing")
    add("12", "12-integration.md", "API Integration")
    add("12", "12-integration.md", "Data Integration")
    add("12", "12-workflow-discovery.md", "Workflow Map")
    add("12", "12-adoption.md", "User Feedback")
    add("12", "12-adoption.md", "AI Opportunity Assessment")
    add("12", "12-deployment.md", "Production AI")

    # 13–16 — ecosystem, assistants, agent frameworks, and workflow platforms
    add("13", "13-major-ai-providers.md", "AI Provider")
    add("13", "13-major-ai-providers.md", "Model Family")
    add("13", "13-major-ai-providers.md", "Provider Strategy")
    add("13", "13-model-types-families.md", "Model Type")
    add("13", "13-open-closed-local-models.md", "Open-Weight Model", "open weight model", "open-weight")
    add("13", "13-open-closed-local-models.md", "Open-Source Model", "open source model", "open-source")
    add("13", "13-open-closed-local-models.md", "Proprietary Model", "closed model", "closed-source model")
    add("13", "13-open-closed-local-models.md", "Local Model", "local models")
    add("13", "13-open-closed-local-models.md", "Cloud Model", "cloud model")
    add("13", "13-major-ai-providers.md", "AI Ecosystem")
    add("13", "13-major-ai-providers.md", "OpenAI")
    add("13", "13-major-ai-providers.md", "Anthropic")
    add("13", "13-major-ai-providers.md", "Google AI")
    add("13", "13-major-ai-providers.md", "Meta AI")
    add("13", "13-major-ai-providers.md", "Mistral AI")
    add("13", "13-major-ai-providers.md", "DeepSeek")
    add("13", "13-major-ai-providers.md", "Qwen")
    add("13", "13-major-ai-providers.md", "GPT")
    add("13", "13-major-ai-providers.md", "Claude")
    add("13", "13-major-ai-providers.md", "Gemini")
    add("13", "13-major-ai-providers.md", "Llama")
    add("14", "14-ai-assistants-coding-tools.md", "AI Assistant")
    add("14", "14-ai-assistants-coding-tools.md", "Chatbot")
    add("14", "14-ai-assistants-coding-tools.md", "Coding Assistant")
    add("14", "14-ai-assistants-coding-tools.md", "Coding Agent")
    add("14", "14-ai-assistants-coding-tools.md", "AI IDE")
    add("14", "14-ai-assistants-coding-tools.md", "Autocomplete", "code autocomplete")
    add("14", "14-ai-assistants-coding-tools.md", "Computer Use")
    add("14", "14-general-agents-computer-use.md", "Browser Agent")
    add("14", "14-general-agents-computer-use.md", "Terminal Agent")
    add("14", "14-ai-assistants-coding-tools.md", "Repository Context")
    add("14", "14-ai-assistants-coding-tools.md", "Codebase")
    add("14", "14-ai-assistants-coding-tools.md", "Agentic Coding")
    add("15", "15-agent-frameworks.md", "Agent Framework")
    add("15", "15-agent-frameworks.md", "Agents SDK")
    add("15", "15-agent-frameworks.md", "LangGraph")
    add("15", "15-how-agents-are-built.md", "Agent Architecture")
    add("15", "15-how-agents-are-built.md", "Agent Orchestration")
    add("15", "15-how-agents-are-built.md", "State Graph")
    add("15", "15-how-agents-are-built.md", "Agent Runtime")
    add("15", "15-how-agents-are-built.md", "Multi-Agent Orchestration")
    add("15", "15-how-agents-are-built.md", "Planner")
    add("15", "15-how-agents-are-built.md", "Executor")
    add("15", "15-how-agents-are-built.md", "Tool Router")
    add("15", "15-how-agents-are-built.md", "Middleware")
    add("16", "16-ai-workflow-platforms.md", "AI Workflow Platform")
    add("16", "16-automation-platforms.md", "Workflow Automation")
    add("16", "16-automation-platforms.md", "Automation Platform")
    add("16", "16-ai-workflow-platforms.md", "Low-Code Platform", "low code platform")
    add("16", "16-ai-workflow-platforms.md", "No-Code Platform", "no code platform")
    add("16", "16-ai-workflow-platforms.md", "AI Step")
    add("16", "16-ai-workflow-platforms.md", "LLM Chain")
    add("16", "16-ai-workflow-platforms.md", "RAG Pipeline")
    add("16", "16-ai-workflow-platforms.md", "Trigger")
    add("16", "16-ai-workflow-platforms.md", "Action")
    add("16", "16-ai-workflow-platforms.md", "Connector")
    add("16", "16-ai-workflow-platforms.md", "API Orchestration")
    add("16", "16-automation-platforms.md", "Event-Driven Workflow", "event driven workflow")
    add("16", "16-automation-platforms.md", "Human Approval Step")

    # 17–19 — product architecture and supporting technologies
    add("17", "17-data-api-authentication.md", "Authentication")
    add("17", "17-data-api-authentication.md", "Authorization")
    add("17", "17-data-api-authentication.md", "REST API", "REST APIs", "REST interface")
    add("17", "17-data-api-authentication.md", "HTTP")
    add("17", "17-data-api-authentication.md", "HTTPS")
    add("17", "17-data-api-authentication.md", "Database")
    add("17", "17-data-api-authentication.md", "Relational Database")
    add("17", "17-data-api-authentication.md", "Document Database")
    add("17", "17-data-api-authentication.md", "Object Storage")
    add("17", "17-data-api-authentication.md", "File Storage")
    add("17", "17-data-api-authentication.md", "Content Delivery Network (CDN)", "content delivery network", "CDN")
    add("17", "17-data-api-authentication.md", "Backend")
    add("17", "17-frontend-backend.md", "Frontend")
    add("17", "17-frontend-backend.md", "Client")
    add("17", "17-frontend-backend.md", "Server")
    add("17", "17-frontend-backend.md", "Service")
    add("17", "17-frontend-backend.md", "Microservice", "microservices")
    add("17", "17-deployment-operations.md", "Cloud Deployment")
    add("17", "17-deployment-operations.md", "Build Pipeline")
    add("17", "17-deployment-operations.md", "Continuous Deployment")
    add("17", "17-deployment-operations.md", "Environment Variable")
    add("17", "17-deployment-operations.md", "Secret")
    add("18", "18-backend-data-platforms.md", "Backend Platform")
    add("18", "18-backend-data-platforms.md", "Managed Database")
    add("18", "18-backend-data-platforms.md", "Edge Function", "edge functions")
    add("18", "18-web-cloud-platforms.md", "Serverless")
    add("18", "18-web-cloud-platforms.md", "Edge Compute")
    add("18", "18-web-cloud-platforms.md", "Edge Network")
    add("18", "18-developer-platforms.md", "Developer Platform")
    add("18", "18-developer-platforms.md", "Deploy Preview")
    add("18", "18-backend-data-platforms.md", "PostgreSQL", "Postgres")
    add("18", "18-backend-data-platforms.md", "NoSQL Database")
    add("18", "18-backend-data-platforms.md", "RLS")
    add("18", "18-web-cloud-platforms.md", "Cloud Platform")
    add("19", "19-backend-technologies.md", "JavaScript")
    add("19", "19-backend-technologies.md", "TypeScript")
    add("19", "19-backend-technologies.md", "Python")
    add("19", "19-backend-technologies.md", "Node.js", "Node runtime")
    add("19", "19-backend-technologies.md", "FastAPI")
    add("19", "19-backend-technologies.md", "Express")
    add("19", "19-frontend-technologies.md", "React")
    add("19", "19-frontend-technologies.md", "Next.js")
    add("19", "19-backend-technologies.md", "Redis")
    add("19", "19-backend-technologies.md", "Cache")
    add("19", "19-backend-technologies.md", "Key-Value Store")
    add("19", "19-data-technologies.md", "Data Warehouse")
    add("19", "19-data-technologies.md", "Data Pipeline")
    add("19", "19-data-technologies.md", "Vector Database")
    add("19", "19-product-services.md", "SaaS")
    add("19", "19-product-services.md", "Payment API")
    add("19", "19-product-services.md", "Webhook")


OVERRIDES: dict[str, tuple[str, str, str]] = {
    "Artificial Intelligence (AI)": ("人工智能（AI）", "Technology that lets computers perform tasks that normally need human intelligence.", "让计算机完成通常需要人类理解、判断或创造力的事情。"),
    "Machine Learning (ML)": ("机器学习（ML）", "A way for computers to learn patterns from data and use them to make predictions or decisions.", "不把规则一条条写死，而是让系统从数据中学规律。"),
    "Deep Learning (DL)": ("深度学习（DL）", "Machine learning that uses neural networks with many layers.", "用很多层神经网络学习复杂规律的方法。"),
    "Supervised Learning": ("监督学习", "Learning from examples that include the expected answer or label.", "训练资料里已经给了正确答案，模型照着学习。"),
    "Unsupervised Learning": ("无监督学习", "Learning patterns from data without provided answer labels.", "没有标准答案，模型自己寻找数据中的结构。"),
    "Reinforcement Learning (RL)": ("强化学习（RL）", "Learning by trying actions and using rewards or penalties as feedback.", "模型不断尝试行动，根据奖励或惩罚学会怎么做。"),
    "Dataset": ("数据集", "An organized collection of examples used for analysis or model development.", "按一定方式整理好、供模型学习或测试的一批数据。"),
    "Feature": ("特征", "A measurable property or signal used to make a prediction.", "模型用来判断问题的一项数据特征。"),
    "Label": ("标签", "The expected category or answer attached to a training example.", "训练例子旁边标注的正确类别或答案。"),
    "Prediction": ("预测", "A result a model estimates from an input.", "模型根据输入猜出的结果。"),
    "Classification": ("分类", "Assigning an input to one or more predefined categories.", "把内容放进一个或多个预先定义的类别。"),
    "Regression": ("回归", "Predicting a numeric value rather than a category.", "预测一个数值，例如价格或温度。"),
    "Clustering": ("聚类", "Grouping similar data points without predefined labels.", "把相似的数据自动分成一组组。"),
    "Generalization": ("泛化", "Performing well on new data that was not in the training examples.", "不只会背训练题，遇到新资料也能做好。"),
    "Overfitting": ("过拟合", "Learning the training examples too closely and performing poorly on new data.", "把练习题背得太熟，换题就不会了。"),
    "Underfitting": ("欠拟合", "Failing to learn enough of the useful pattern in the data.", "连训练资料里的主要规律都没有学好。"),
    "Hyperparameter": ("超参数", "A setting chosen before or around training, such as learning rate or batch size.", "训练前或训练过程中由人设定的控制旋钮。"),
    "Parameter": ("参数", "A numeric value a model learns and uses in its computation.", "模型训练时自己调整、用来计算输出的数字。"),
    "Weight": ("权重", "A learned number that controls how strongly one signal affects another.", "决定某个输入信号影响有多大的数字。"),
    "Bias": ("偏置", "A learned offset added to a model computation.", "模型计算中用来调整基础输出的内部数字。"),
    "Activation Function": ("激活函数", "A function that transforms a unit's input into its output.", "决定神经网络单元如何把输入变成输出的函数。"),
    "Loss Function": ("损失函数", "A function that measures how far a model output is from the desired answer.", "用一个数字表示模型答得有多偏，训练会努力把它变小。"),
    "Cross-Entropy Loss": ("交叉熵损失", "A loss used especially for comparing predicted probabilities with the correct class.", "比较模型给出的类别概率和正确类别的差距。"),
    "Gradient Descent": ("梯度下降", "An optimization method that updates parameters in the direction that reduces loss.", "沿着让错误变小的方向一点点调整模型参数。"),
    "Backpropagation": ("反向传播", "Sending error information backward through a network to update its parameters.", "把误差信息从后往前传，帮助各层调整参数。"),
    "Optimizer": ("优化器", "A method that changes model parameters during training.", "负责按照训练反馈更新参数的算法。"),
    "Epoch": ("训练轮次", "One complete pass through the training dataset.", "把整份训练资料完整看一遍。"),
    "Batch": ("批次", "A group of examples processed together.", "一次放进模型一起计算的一小组样本。"),
    "Batch Size": ("批大小", "The number of examples processed in one batch.", "每次一起计算多少个训练样本。"),
    "Neural Network": ("神经网络", "A model made of connected computational units that transform inputs into outputs.", "由许多相连计算单元组成、能从数据学习的模型。"),
    "Attention": ("注意力机制", "A mechanism that gives more computation to the parts of an input that matter most.", "让模型在处理一句话或一张图时重点看更有用的部分。"),
    "Self-Attention": ("自注意力", "Attention in which elements of a sequence compare with other elements in the same sequence.", "一句话中的每个词都可以参考同一句话里的其他词。"),
    "Multi-Head Attention": ("多头注意力", "Several attention operations that can focus on different relationships in parallel.", "同时用几组注意力去看不同类型的关系。"),
    "Cross-Attention": ("交叉注意力", "Attention that connects one sequence or modality to another.", "让一类输入去关注另一类输入中的相关信息。"),
    "Transformer": ("Transformer 架构", "A neural-network architecture built around attention and stacked processing blocks.", "以注意力为核心、把多个处理模块堆叠起来的网络架构。"),
    "Convolutional Neural Network (CNN)": ("卷积神经网络（CNN）", "A neural network that is effective at learning local spatial patterns such as image features.", "擅长从图像局部区域学习边缘、纹理等模式的网络。"),
    "Recurrent Neural Network (RNN)": ("循环神经网络（RNN）", "A neural network that processes sequences while carrying information from earlier steps.", "处理序列时把前面步骤的信息带到后面的网络。"),
    "Long Short-Term Memory (LSTM)": ("长短期记忆网络（LSTM）", "A recurrent architecture designed to keep useful information over longer sequences.", "一种更擅长在较长序列中保留重要信息的循环网络。"),
    "Diffusion Model": ("扩散模型", "A generative model that learns to reverse a gradual noising process.", "学习把逐步加噪的数据还原成图像、声音等内容的生成模型。"),
    "Foundation Model": ("基础模型", "A broadly trained model that can be adapted to many downstream tasks.", "先用大量通用数据训练，再拿去适配不同任务的模型。"),
    "Large Language Model (LLM)": ("大语言模型（LLM）", "A language model trained at large scale to understand and generate text.", "用大量文字训练、能理解和生成语言的模型。"),
    "Multimodal Model": ("多模态模型", "A model that works with more than one type of input or output, such as text, images, audio, or video.", "能同时处理文字、图片、声音或视频等不同信息类型的模型。"),
    "Model Parameter": ("模型参数", "A learned numeric value that determines part of a model's behavior.", "模型通过训练学出来、决定行为的一组数字。"),
    "Vision Foundation Model": ("视觉基础模型", "A broadly trained model that learns reusable visual representations from large amounts of image or visual data.", "先用大量图像或视觉数据训练，再适配多个视觉任务的模型。"),
    "Pre-Training": ("预训练", "Broad initial training on a large dataset before task-specific adaptation.", "先用大量通用资料打基础，再针对具体任务调整。"),
    "Training": ("训练", "The process of optimizing a model's learned parameters from data.", "让模型从数据中调整内部参数、逐步学会任务规律的过程。"),
    "Fine-Tuning": ("微调", "Additional training that adapts an existing model to a task, style, or domain.", "在已有模型上继续训练，让它更适合某个任务或领域。"),
    "Supervised Fine-Tuning (SFT)": ("监督微调（SFT）", "Fine-tuning on examples that include desired answers or behaviors.", "用带有理想答案的例子继续训练模型。"),
    "Instruction Tuning": ("指令微调", "Training a model to follow natural-language instructions reliably.", "专门训练模型更好地理解并执行人类指令。"),
    "Low-Rank Adaptation (LoRA)": ("低秩适配（LoRA）", "A parameter-efficient fine-tuning method that learns a small low-rank update.", "不改动全部大参数，只训练一小组低秩更新来适配模型。"),
    "Reinforcement Learning from Human Feedback (RLHF)": ("基于人类反馈的强化学习（RLHF）", "Using human preferences as feedback to improve a model's behavior.", "让人评价模型答案，再用这些偏好反馈改进模型。"),
    "Token": ("词元", "A small unit of text or other data that a model processes.", "模型处理文字时使用的小片段，不一定刚好等于一个汉字或单词。"),
    "Tokenization": ("词元化", "Splitting input text into the tokens a model can process.", "把文字切成模型能识别的小单位。"),
    "Context Window": ("上下文窗口", "The maximum amount of input and output context a model can handle at once.", "模型一次能看到和处理的文字容量上限。"),
    "Inference": ("推理", "Running a trained model on an input to produce an output.", "把训练好的模型真正拿来回答问题或生成结果。"),
    "Key-Value Cache (KV Cache)": ("键值缓存（KV Cache）", "Cached attention information reused while generating a sequence.", "生成长回答时把已经算过的注意力信息存起来，减少重复计算。"),
    "Unified Memory": ("统一内存", "A shared memory pool that can be used by the CPU and GPU instead of separate system RAM and VRAM.", "CPU 和 GPU 可以共同使用的一块内存，不必完全分成两套。"),
    "Dynamic Batching": ("动态批处理", "Forming batches from requests that arrive at runtime so the serving system can process them together.", "请求陆续到来时，运行中把它们临时凑成一批一起处理。"),
    "Temperature": ("温度参数", "A sampling setting that controls how varied or conservative model outputs are.", "调节模型回答更稳定还是更多样的参数。"),
    "Prompt": ("提示词", "The instructions and input given to a model.", "发给模型的问题、要求和补充资料。"),
    "Prompt Engineering": ("提示词工程", "Designing prompts so a model is more likely to produce the desired result.", "通过设计提示词让模型更稳定地完成任务。"),
    "System Prompt": ("系统提示词", "Instructions supplied by the application to set a model's role, rules, or behavior.", "应用预先给模型的身份、规则和行为要求。"),
    "Context Engineering": ("上下文工程", "Designing and assembling the information a model receives at runtime.", "设计模型在运行时到底看到哪些资料、以什么顺序看到。"),
    "Structured Output": ("结构化输出", "Model output constrained to a predictable format such as JSON fields.", "要求模型按固定字段和格式返回结果。"),
    "JSON": ("JSON 数据格式", "A text format for representing structured data with objects, arrays, and values.", "一种用文字表达字段、列表和数据值的常见格式。"),
    "JSON Schema": ("JSON Schema 数据模式", "A formal description of the fields and value types allowed in JSON data.", "规定 JSON 必须有哪些字段、每个字段是什么类型。"),
    "Generative AI": ("生成式人工智能", "AI that creates new text, images, audio, video, code, or other content.", "能够生成新内容，而不只是分类或检索已有内容的 AI。"),
    "Embedding": ("嵌入向量", "A learned numeric representation that captures useful relationships between items.", "把文字、图片等内容变成一串能比较相似度的数字。"),
    "Vector Database": ("向量数据库", "A database designed to store and search vector representations.", "专门保存和查找嵌入向量的数据库。"),
    "Vector Search": ("向量搜索", "Searching for items whose vectors are close to a query vector.", "按内容的数字表示寻找相似资料。"),
    "Semantic Search": ("语义搜索", "Search that matches meaning rather than only exact words.", "理解问题意思后寻找相关内容，不只看字面是否相同。"),
    "Search": ("搜索", "Looking through a collection to find possible matches.", "在资料集合里找可能相关的内容。"),
    "Retrieval": ("检索", "Finding and returning information relevant to a query.", "从资料库里找出并取回和问题有关的资料。"),
    "Retrieval-Augmented Generation (RAG)": ("检索增强生成（RAG）", "A system that retrieves information and gives it to a model before the model answers.", "先查资料，再把资料交给模型回答。"),
    "Reranking": ("重排序", "Reordering retrieved results with a stronger relevance model.", "先找出候选资料，再用更精细的模型重新排顺序。"),
    "Chunking": ("分块", "Splitting documents into smaller pieces for storage or retrieval.", "把长文档切成适合保存和检索的小段。"),
    "Grounding": ("事实接地", "Connecting a model answer to supplied external evidence.", "让回答有外部资料依据，而不是完全凭模型记忆生成。"),
    "Citation": ("引用", "A reference that points to the source supporting a claim.", "在答案旁边标出这句话依据的资料来源。"),
    "AI Agent": ("AI 智能体", "A system that uses a model, tools, and a control loop to pursue a goal.", "能理解目标、调用工具并多步行动的 AI 系统。"),
    "Agent Loop": ("智能体循环", "A repeated cycle in which an agent observes, reasons, acts, and checks the result.", "智能体反复观察、思考、行动，再检查结果的循环。"),
    "Agent State": ("智能体状态", "The current task information an agent needs to continue its work.", "记录智能体目前做到哪一步、掌握什么信息。"),
    "Agent Memory": ("智能体记忆", "Information retained so an agent can use it later in a task or across sessions.", "智能体保存下来、之后还能使用的资料。"),
    "Planning": ("规划", "Breaking a goal into steps and deciding how to reach it.", "把大目标拆成步骤并安排完成顺序。"),
    "Tool Calling": ("工具调用", "Letting a model request an external function, API, or tool.", "让模型请求外部程序、接口或工具帮它做事。"),
    "Function Calling": ("函数调用", "A structured request from a model to run a named function with arguments.", "模型按约定的函数名和参数请求程序执行动作。"),
    "Human-in-the-Loop (HITL)": ("人在回路（HITL）", "A workflow in which a person reviews, approves, corrects, or completes AI work.", "关键步骤保留人工检查、批准或接管。"),
    "Model Context Protocol (MCP)": ("模型上下文协议（MCP）", "A protocol for connecting models or agents with tools and external context.", "让模型或智能体按统一方式连接工具和外部资料的协议。"),
    "Multi-Agent System": ("多智能体系统", "A system in which multiple agents coordinate or divide work.", "多个智能体分工、协作或互相检查的系统。"),
    "Application Programming Interface (API)": ("应用程序编程接口（API）", "A defined way for software systems to request data or actions from one another.", "不同软件按约定方式互相请求数据或动作的入口。"),
    "Model Serving": ("模型服务", "Making a model available to applications through a running service.", "把模型放进持续运行的服务，供应用调用。"),
    "Quantization": ("量化", "Reducing the numeric precision of model values to lower memory or compute cost.", "用更少的数字精度保存模型，以减少内存和计算开销。"),
    "GPU": ("图形处理器（GPU）", "A processor designed for highly parallel numerical computation, often used for AI.", "能同时做大量数字计算、常用于训练和推理的处理器。"),
    "VRAM": ("显存（VRAM）", "Memory on a GPU used to hold model weights, activations, and data.", "GPU 上用来放模型和计算数据的内存。"),
    "Latency": ("延迟", "The time a system takes to respond to a request.", "从发出请求到得到响应要等多久。"),
    "Throughput": ("吞吐量", "The amount of work a system completes in a given period of time.", "系统在一段时间内能处理多少请求或数据。"),
    "Time to First Token (TTFT)": ("首词元时间（TTFT）", "The time from sending a request until the first generated token arrives.", "发出请求后，看到模型第一个字词需要等多久。"),
    "Tokens per Second (TPS)": ("每秒词元数（TPS）", "The number of output tokens a system generates per second.", "模型每秒能生成多少个词元。"),
    "vLLM": ("vLLM 推理引擎", "An inference and serving engine optimized for running large language models.", "用于高效运行和提供大语言模型服务的推理引擎。"),
    "Ollama": ("Ollama 本地运行工具", "A tool that makes it convenient to run language models locally.", "方便在本地电脑运行语言模型的工具。"),
    "Evaluation": ("评测", "Measuring a model or system against defined tasks, examples, or criteria.", "用规定的任务和标准检查模型或系统表现。"),
    "Benchmark": ("基准测试", "A standard task or dataset used to compare models.", "用统一题目或数据比较不同模型的测试。"),
    "Accuracy": ("准确率", "The fraction of predictions that are correct.", "所有判断中答对的比例。"),
    "Precision": ("精确率", "Among predicted positive cases, the fraction that is actually positive.", "模型说“是”的结果里，真正是“是”的比例。"),
    "Recall": ("召回率", "Among actual positive cases, the fraction the model finds.", "所有真正的目标里，模型找出来的比例。"),
    "F1 Score": ("F1 分数", "A combined measure of precision and recall.", "综合衡量精确率和召回率的指标。"),
    "Calibration": ("校准", "How well a model's confidence matches its actual success frequency.", "模型说自己有多确定，长期看是否和实际正确率相符。"),
    "Hallucination": ("幻觉", "Fluent model output that is unsupported, fabricated, or incorrect.", "回答听起来很像真的，但其实没有依据或内容是编出来的。"),
    "Fabricated Content": ("编造内容", "Invented content presented as though it were retrieved, observed, or known.", "模型把没有依据的内容写出来，还让人以为它是真实资料。"),
    "Guardrail": ("安全护栏", "A rule or control that limits unsafe, invalid, or unauthorized model behavior.", "限制模型不能做危险、违规或未经允许事情的控制。"),
    "Prompt Injection": ("提示词注入", "An attack that puts instructions in input content to manipulate a model or agent.", "把恶意指令藏进输入资料，诱导模型违反原本规则。"),
    "Jailbreak": ("越狱", "An attempt to bypass a model's safety or behavior restrictions.", "试图绕过模型安全限制，让它做本来不该做的事。"),
    "Privacy": ("隐私", "Protecting personal or sensitive information from improper use or disclosure.", "避免个人或敏感资料被不当使用或泄露。"),
    "Personally Identifiable Information (PII)": ("个人可识别信息（PII）", "Information that can identify a specific person directly or when combined with other data.", "能够直接或组合识别某个人的资料。"),
    "Authentication": ("身份认证", "Checking who a user or system is.", "确认“你是谁”。"),
    "Authorization": ("授权", "Deciding what an identified user or system is allowed to do.", "确认“你能做什么”。"),
    "Least Privilege": ("最小权限", "Giving an identity only the access needed for its task.", "只给用户或程序完成工作所必需的最少权限。"),
    "Monitoring": ("监控", "Continuously watching system behavior, quality, and operational signals.", "持续观察系统运行、质量和风险信号。"),
    "Observability": ("可观测性", "The ability to understand system behavior from logs, metrics, traces, and events.", "通过日志、指标和追踪信息看懂系统发生了什么。"),
    "Data Drift": ("数据漂移", "A change over time in the characteristics of input data.", "线上收到的数据和过去训练或观察到的数据变了。"),
    "Concept Drift": ("概念漂移", "A change in the relationship between inputs and outcomes over time.", "同样的输入和结果之间的规律随时间变了。"),
    "Schema Drift": ("模式漂移", "An unexpected change in the fields or structure of data.", "数据字段或结构发生了程序没有预期的变化。"),
    "Deployment": ("部署", "Making a model or application available for real use.", "把模型或应用放到真实环境中运行。"),
    "Workflow Discovery": ("工作流发现", "Finding and understanding a real workflow before deciding where AI fits.", "先弄清楚真实工作怎么做，再判断 AI 应该放在哪一步。"),
    "Technical Scoping": ("技术范围界定", "Defining the data, interfaces, controls, and system boundaries for a solution.", "明确要用哪些数据、接口、控制和系统边界。"),
    "AI Provider": ("AI 提供商", "A company that develops and makes models or AI services available.", "开发模型并提供 AI 产品或接口的公司。"),
    "OpenAI": ("OpenAI 人工智能公司", "An AI company and provider associated with GPT models and AI products.", "一家开发 GPT 等模型并提供 AI 产品和接口的公司。"),
    "Anthropic": ("Anthropic 人工智能公司", "An AI company and provider associated with Claude models.", "一家开发 Claude 等模型的 AI 公司。"),
    "Google AI": ("Google AI", "Google's AI organization and model ecosystem, including Gemini.", "Google 旗下负责 AI 模型和相关产品的组织与生态。"),
    "Meta AI": ("Meta AI 人工智能组织", "Meta's AI organization and model ecosystem, including Llama.", "Meta 旗下负责 AI 模型和相关产品的组织与生态。"),
    "Mistral AI": ("Mistral AI 人工智能公司", "An AI company and provider associated with the Mistral model family.", "一家开发 Mistral 模型家族的 AI 公司。"),
    "DeepSeek": ("DeepSeek AI 模型与提供商", "An AI model family and provider name used in the model landscape.", "AI 模型家族和提供商名称之一。"),
    "Qwen": ("通义千问（Qwen）", "An AI model family associated with Alibaba Cloud.", "阿里云旗下的 AI 模型家族。"),
    "GPT": ("GPT 生成式预训练模型", "A family of generative pre-trained transformer language models.", "一类以 Transformer 为基础、经过预训练并能生成内容的语言模型。"),
    "Claude": ("Claude 大语言模型", "A large language model family developed by Anthropic.", "Anthropic 开发的大语言模型家族。"),
    "Gemini": ("Gemini 多模态模型", "A multimodal model family developed by Google.", "Google 开发的多模态模型家族。"),
    "Llama": ("Llama 大语言模型", "A large language model family developed by Meta.", "Meta 开发的大语言模型家族。"),
    "Model Family": ("模型家族", "A related group of models released under one model line or brand.", "同一条产品线或品牌下的一组相关模型。"),
    "Open-Weight Model": ("开放权重模型", "A model whose trained weights are made available for others to use or run.", "把训练后的模型权重公开出来、允许别人使用或运行的模型。"),
    "Proprietary Model": ("专有模型", "A model controlled by an organization whose weights or implementation are not broadly open.", "由某家公司控制、权重或实现没有完全公开的模型。"),
    "AI Assistant": ("AI 助手", "A user-facing AI system that helps with questions, content, or tasks.", "帮助用户回答问题、生成内容或完成任务的 AI 产品。"),
    "Coding Agent": ("编程智能体", "An agent that can inspect code and take software-development actions.", "能查看代码并执行开发操作的智能体。"),
    "AI IDE": ("AI 集成开发环境", "A development environment that integrates AI into coding and software work.", "把 AI 深度放进写代码环境里的开发工具。"),
    "Computer Use": ("计算机操作", "An AI capability that interacts with a graphical interface, browser, or desktop.", "让 AI 像用户一样操作界面、浏览器或桌面。"),
    "Agent Framework": ("智能体框架", "Software components that help developers build, orchestrate, and run agents.", "帮助开发者组装、编排和运行智能体的软件框架。"),
    "Agents SDK": ("智能体 SDK", "A software development kit for building applications with AI agents.", "帮助开发者构建 AI 智能体应用的一组软件工具。"),
    "LangGraph": ("LangGraph 智能体框架", "A framework for building stateful agent workflows as graphs.", "把智能体步骤和状态连接成图来编排工作流的框架。"),
    "LLM Chain": ("LLM 链", "A connected sequence of large language model operations or components.", "把多个大语言模型处理步骤按顺序连接起来。"),
    "RAG Pipeline": ("RAG 流水线", "A pipeline that retrieves knowledge and uses it to generate an answer.", "把检索资料和回答生成连起来的一组处理步骤。"),
    "AI Workflow Platform": ("AI 工作流平台", "A platform for assembling repeatable flows that combine models, tools, data, and human steps.", "把模型、工具、数据和人工步骤连成可重复流程的平台。"),
    "Workflow Automation": ("工作流自动化", "Using software to run repeatable workflow steps with limited manual effort.", "用软件自动执行重复的工作步骤。"),
    "REST API": ("REST API 接口", "An API style that exposes resources and actions through standard web conventions.", "按常见 Web 规则通过接口访问资源和操作。"),
    "HTTP": ("HTTP 网络协议", "The protocol commonly used to exchange requests and responses on the web.", "网页和服务之间传递请求与响应的基础协议。"),
    "HTTPS": ("HTTPS", "HTTP protected with encrypted transport security.", "带加密保护的 HTTP 通信。"),
    "Database": ("数据库", "A system that stores and retrieves structured application data.", "专门保存、查询和更新结构化数据的系统。"),
    "Relational Database": ("关系型数据库", "A database that organizes data into related tables.", "把数据放在相互关联的表里的数据库。"),
    "Object Storage": ("对象存储", "Storage for files and blobs addressed as objects rather than database rows.", "按对象保存图片、视频、PDF 等文件的存储。"),
    "Content Delivery Network (CDN)": ("内容分发网络（CDN）", "A distributed network that serves content from locations closer to users.", "把内容放到离用户更近的节点来加快访问。"),
    "Backend": ("后端", "Server-side software that handles data, business logic, and APIs.", "在服务器上处理数据、业务和接口的部分。"),
    "Frontend": ("前端", "The user-facing part of an application that runs in a browser or client.", "用户看到并操作的界面部分。"),
    "Serverless": ("无服务器架构", "A deployment model where the platform runs servers for application code on demand.", "开发者不用自己管理服务器，平台按需运行代码。"),
    "PostgreSQL": ("PostgreSQL 关系型数据库", "An open-source relational database system.", "一种常用的开源关系型数据库。"),
    "NoSQL Database": ("NoSQL 数据库", "A database that uses non-relational data models such as documents or key-value pairs.", "不要求所有数据都放进固定关系表的数据库。"),
    "React": ("React 前端库", "A JavaScript library for building user interfaces from reusable components.", "用可复用组件构建网页界面的 JavaScript 库。"),
    "Next.js": ("Next.js Web 框架", "A React-based framework for building web applications.", "基于 React、用于构建 Web 应用的框架。"),
    "Python": ("Python 编程语言", "A general-purpose programming language widely used for AI and backend work.", "常用于 AI、数据处理和后端开发的编程语言。"),
    "TypeScript": ("TypeScript 编程语言", "A typed programming language that extends JavaScript.", "给 JavaScript 增加类型系统的编程语言。"),
    "Node.js": ("Node.js 运行环境", "A runtime for executing JavaScript outside the browser.", "让 JavaScript 能在浏览器之外运行的环境。"),
    "JavaScript": ("JavaScript 编程语言", "A programming language widely used for web interfaces and Node.js services.", "网页交互和 Node.js 服务常用的编程语言。"),
    "FastAPI": ("FastAPI Python 接口框架", "A modern Python framework for building APIs.", "用 Python 快速构建 Web 接口的框架。"),
    "Express": ("Express Node.js 框架", "A lightweight Node.js framework for building web servers and APIs.", "用 Node.js 构建网页服务器和接口的轻量框架。"),
    "Cache": ("缓存", "Temporarily stored data used to avoid repeating expensive work.", "把常用或已计算过的内容暂存起来，减少重复工作。"),
    "Webhook": ("Webhook", "A callback delivered over HTTP when an event occurs.", "发生事件时，系统主动通过 HTTP 通知另一个系统。"),
}


MISSING_SPECS = [
    ("01", "Reinforcement Learning", "Markov Decision Process (MDP)", "The formal state, action, transition, and reward model behind reinforcement-learning problems is not defined.", "Add a foundational RL concept page and distinguish MDP from a generic workflow."),
    ("01", "Reinforcement Learning", "Q-Learning", "A canonical value-based RL algorithm is absent even though reward and policy concepts appear.", "Add an algorithm entry with state-action value and update intuition."),
    ("01", "Reinforcement Learning", "Policy Gradient", "A major family of policy-optimization algorithms is missing from the RL path.", "Add a method entry and contrast it with value-based learning."),
    ("02", "Neural Networks", "Multi-Layer Perceptron (MLP)", "The common fully connected network name is absent from the architecture coverage.", "Add an architecture entry and distinguish it from a generic neural network."),
    ("02", "Attention", "Sparse Attention", "Attention sparsity is useful for long-context efficiency but is not represented as a standalone concept.", "Add a mechanism entry with the accuracy/compute trade-off."),
    ("02", "Diffusion Models", "U-Net", "The dominant denoising architecture is not covered by the diffusion glossary.", "Add a model-component entry and explain its role in denoising."),
    ("02", "Diffusion Models", "Classifier-Free Guidance", "A standard control method for conditional diffusion is absent.", "Add a method entry with guidance-strength intuition."),
    ("02", "Diffusion Models", "DDPM", "The canonical diffusion training/sampling family is missing as an important abbreviation.", "Add DDPM and expand the acronym."),
    ("03", "Model Types & Families", "Mixture of Experts (MoE)", "Sparse expert routing is a major modern model architecture and is not retained in the final set.", "Add a model-architecture entry and distinguish experts from layers."),
    ("03", "Model Types & Families", "Vision-Language-Action Model (VLA)", "The model family connecting perception, language, and actions is an important agent/robotics concept.", "Add a model-type entry with modality boundaries."),
    ("04", "Fine-Tuning", "QLoRA", "Quantized LoRA is a common practical fine-tuning method missing from the source candidates.", "Add it as a companion entry to LoRA and quantization."),
    ("04", "Preference Learning / RLHF", "Direct Preference Optimization (DPO)", "A widely used preference-optimization method is not present in the raw candidate inventory.", "Add DPO and compare it with RLHF at a high level."),
    ("04", "Preference Learning / RLHF", "Proximal Policy Optimization (PPO)", "The standard RL optimizer used in many RLHF pipelines is absent.", "Add PPO as an algorithm entry, not as a synonym for RLHF."),
    ("04", "Preference Learning / RLHF", "RLAIF", "AI-generated preference feedback is a common alignment variant that is not covered.", "Add the acronym and distinguish AI feedback from human feedback."),
    ("04", "Preference Learning / RLHF", "Constitutional AI", "A named safety/alignment approach is missing from the preference-learning coverage.", "Add a method entry and link it to self-critique and principles."),
    ("05", "Next-Token Prediction", "Logits", "The pre-softmax scores used in token selection are missing from the decoding explanation.", "Add a decoding-mechanics entry and distinguish logits from probabilities."),
    ("05", "Sampling / Temperature", "Nucleus Sampling", "Top-p is a standard decoding method but is not consistently represented as a standalone concept.", "Add the full name and link it to Top-p Sampling."),
    ("05", "Inference", "Speculative Decoding", "A key latency optimization using a draft model is absent from the inference glossary.", "Add a serving-optimization entry and explain quality preservation."),
    ("05", "KV Cache", "Paged KV Cache", "Paged cache management is central to efficient serving but is not fully covered.", "Add a systems entry and relate it to memory fragmentation."),
    ("06", "Structured Outputs", "Constrained Decoding", "Format-constrained token generation is an important mechanism missing from structured output coverage.", "Add a mechanism entry and distinguish it from post-hoc parsing."),
    ("06", "Prompt Design", "Role Prompting", "Assigning a role is common prompt practice but is not a first-class concept.", "Add it as a prompting technique with limits."),
    ("06", "System Prompts", "Developer Prompt", "Many production APIs use a developer-instruction layer that is not represented.", "Add it and distinguish it from system and user messages."),
    ("07", "Image Generation", "ControlNet", "A standard conditioning/control architecture is absent from image-generation coverage.", "Add a model-component entry and explain conditioning inputs."),
    ("07", "Image Generation", "Latent Diffusion", "The latent-space form of diffusion is important for understanding modern image models.", "Add a mechanism entry and distinguish latent from pixel space."),
    ("08", "Vector Search", "Cosine Similarity", "The common measure for comparing embedding direction is absent from vector search.", "Add a similarity metric with a small geometric explanation."),
    ("08", "Vector Search", "Dot Product", "A common vector similarity operation is not retained as an independent concept.", "Add it and contrast it with cosine similarity."),
    ("08", "Vector Search", "Euclidean Distance", "Distance-based nearest-neighbor search needs a canonical distance metric entry.", "Add it and explain when magnitude matters."),
    ("08", "Retrieval", "BM25", "The standard lexical retrieval algorithm is missing, leaving keyword search underspecified.", "Add BM25 and compare it with semantic and hybrid search."),
    ("08", "Vector Search", "HNSW", "A widely used approximate-nearest-neighbor index is absent.", "Add HNSW as an index-structure entry."),
    ("08", "Vector Search", "FAISS", "A widely used vector-search library is not represented in the implementation layer.", "Add it as a named library, clearly separate from a vector database."),
    ("08", "Reranking", "Mean Reciprocal Rank (MRR)", "A standard ranking metric is missing from the retrieval evaluation vocabulary.", "Add MRR and define its rank-sensitive behavior."),
    ("08", "Reranking", "Normalized Discounted Cumulative Gain (NDCG)", "A standard graded-relevance ranking metric is absent.", "Add NDCG and explain why higher ranks matter more."),
    ("08", "Reranking", "Precision@k", "Top-k retrieval quality needs a precision-at-k metric entry.", "Add the notation and define k explicitly."),
    ("08", "Reranking", "Recall@k", "Top-k retrieval coverage needs a recall-at-k metric entry.", "Add the notation and define the relevant set."),
    ("09", "Agent Loop", "ReAct", "The reasoning-and-acting agent pattern is missing from the agent-loop concepts.", "Add ReAct and distinguish it from a generic agent loop."),
    ("09", "Agent Loop", "State Machine", "Explicit state-machine orchestration is important for controllable agents but is absent.", "Add a control-architecture entry and contrast it with free-form loops."),
    ("09", "Planning", "Planner-Executor Pattern", "Separating planning from execution is a common agent design pattern not represented.", "Add a pattern entry and list its handoff risks."),
    ("10", "Model Serving", "Autoscaling", "Production serving needs a capacity-control concept beyond raw throughput and latency.", "Add autoscaling with trigger and capacity semantics."),
    ("10", "Model Serving", "Model Sharding", "Splitting a model across devices is a standard deployment strategy missing from runtime coverage.", "Add a systems entry and distinguish it from tensor parallelism."),
    ("10", "Quantization", "FP16", "Common numeric formats are not named even though precision and quantization are discussed.", "Add a precision-format entry and link it to memory and quality."),
    ("10", "Quantization", "BF16", "BFloat16 is a common training/serving format absent from the precision vocabulary.", "Add it beside FP16 and explain the practical distinction."),
    ("11", "Evaluation", "ROC-AUC", "Binary-classification evaluation lacks a threshold-independent ranking metric.", "Add ROC-AUC and define what is being ranked."),
    ("11", "Evaluation", "BLEU", "Text-generation evaluation lacks a canonical machine-translation overlap metric.", "Add BLEU with a caveat about reference overlap."),
    ("11", "Evaluation", "ROUGE", "Summarization evaluation lacks a canonical reference-overlap metric.", "Add ROUGE and distinguish it from factuality."),
    ("11", "Guardrails", "Jailbreak", "The attack category deserves explicit coverage even when safety restrictions are mentioned.", "Add a security entry and connect it to prompt injection."),
    ("11", "Guardrails", "Red Teaming", "Adversarial safety testing is not a first-class evaluation concept.", "Add red teaming with test-scenario examples."),
    ("11", "Permissions & Safety", "Model Card", "Model documentation for intended use, limitations, and evaluation is missing.", "Add model cards as a governance/documentation concept."),
    ("11", "Permissions & Safety", "Dataset Card", "Dataset documentation is needed to make training-data provenance and limitations inspectable.", "Add dataset cards and connect them to data governance."),
    ("11", "Permissions & Safety", "PII Redaction", "Privacy controls need a concrete transformation concept beyond general privacy.", "Add redaction and distinguish it from access control."),
    ("12", "Deployment", "Blue-Green Deployment", "A second release strategy is useful for explaining safe rollout and rollback.", "Add blue-green deployment and contrast it with canary release."),
    ("12", "Monitoring", "Service-Level Objective (SLO)", "Operational monitoring lacks a target-based reliability concept.", "Add SLO and distinguish it from an observed metric."),
    ("12", "Monitoring", "Alerting", "Monitoring needs an explicit action-trigger concept.", "Add alerting with threshold and routing semantics."),
    ("13", "Open vs Closed / Local Models", "Model License", "Open weights do not by themselves explain what users may legally do.", "Add licensing as a separate ecosystem concept."),
    ("14", "AI Assistants & Coding Tools", "Codebase Indexing", "Repository-aware assistants need an explicit indexing/retrieval concept.", "Add it and connect it to repository context."),
    ("15", "Agent Frameworks", "Agent Evaluation", "Agent quality needs task-level evaluation beyond model benchmarks.", "Add agent evaluation with success and failure criteria."),
    ("16", "AI Workflow Platforms", "Idempotency", "Workflow retries need a way to avoid applying the same side effect twice.", "Add idempotency as a reliability concept."),
    ("17", "Data, APIs & Authentication", "OAuth", "Modern API authentication needs a delegated-authorization protocol concept.", "Add OAuth and distinguish it from authentication itself."),
    ("17", "Data, APIs & Authentication", "JSON Web Token (JWT)", "Token-based identity propagation is missing from API authentication coverage.", "Add JWT and describe signed claims without treating it as encryption."),
    ("17", "Data, APIs & Authentication", "Role-Based Access Control (RBAC)", "Permission design lacks the standard role-based model.", "Add RBAC and distinguish roles from individual permissions."),
    ("17", "Data, APIs & Authentication", "Row-Level Security (RLS)", "Database-level authorization needs an explicit row-filtering concept.", "Add RLS and distinguish it from application checks."),
    ("17", "Data, APIs & Authentication", "CORS", "Browser-to-API integration needs a cross-origin policy concept.", "Add CORS with browser scope and server response behavior."),
    ("17", "Data, APIs & Authentication", "CSRF", "Session-based web security lacks a cross-site request-forgery concept.", "Add CSRF and distinguish it from XSS and prompt injection."),
    ("17", "Data, APIs & Authentication", "TLS", "Transport security needs a protocol-level encryption concept.", "Add TLS and link HTTPS to it."),
    ("17", "Data, APIs & Authentication", "Rate Limiting", "Shared APIs need an abuse and capacity control concept.", "Add rate limiting with request-window semantics."),
    ("17", "Data, APIs & Authentication", "Idempotency", "Retry-safe API design requires an explicit idempotency concept.", "Add it with a payment/API example."),
    ("17", "Data, APIs & Authentication", "Pagination", "Large API responses need a standard result-partitioning concept.", "Add pagination and distinguish it from chunking."),
    ("18", "Backend & Data Platforms", "Primary Key", "Database identity is not represented in the supporting architecture vocabulary.", "Add primary key and distinguish it from a model parameter."),
    ("18", "Backend & Data Platforms", "Foreign Key", "Relational integrity needs a cross-table reference concept.", "Add foreign key with referential-integrity intuition."),
    ("18", "Backend & Data Platforms", "Database Index", "Database performance needs an explicit lookup-acceleration concept.", "Add an index and distinguish it from a vector index."),
    ("18", "Backend & Data Platforms", "Transaction", "Multi-step data changes need an all-or-nothing consistency concept.", "Add transactions with commit/rollback semantics."),
    ("18", "Web & Cloud Platforms", "Docker", "Deployment vocabulary lacks the standard container packaging technology.", "Add Docker as a named technology and define the container boundary."),
    ("18", "Web & Cloud Platforms", "Kubernetes", "Production container orchestration is absent from the cloud-platform coverage.", "Add Kubernetes as an orchestration platform."),
    ("19", "Backend Technologies", "FastAPI", "The Python API framework is referenced in technology comparisons but not retained.", "Add it as a named framework and keep framework/runtime distinct."),
    ("19", "Backend Technologies", "Express", "The Node.js web framework is referenced but not retained.", "Add it as a named framework and distinguish it from Node.js."),
]


def load_all_raw() -> tuple[list[Candidate], int, int]:
    rows: list[Candidate] = []
    all_count = 0
    header_count = 0
    with ALL_RAW.open("r", encoding="utf-8-sig", newline="") as handle:
        for raw in csv.DictReader(handle):
            all_count += 1
            term = display_term(raw.get("EnglishTerm", ""))
            if not term or norm(term) in HEADER_TERMS:
                header_count += 1
                continue
            rows.append(Candidate(
                term=term,
                cn=clean_text(raw.get("Chinese", "")),
                simple=clean_text(raw.get("SimpleEnglish", "")),
                explain=clean_text(raw.get("ChineseExplanation", "")),
                module=clean_text(raw.get("Module", "")),
                topic=clean_text(raw.get("Topic", "")),
                raw_file=clean_text(raw.get("RawFile", "")),
                source_file=clean_text(raw.get("SourceFile", "")),
            ))
    return rows, all_count, header_count


def load_markdown_evidence() -> tuple[list[Candidate], list[Candidate]]:
    canonical: list[Candidate] = []
    variable: list[Candidate] = []
    for path in sorted(RAW_DIR.glob("*.md")):
        lines = path.read_text(encoding="utf-8").splitlines()
        start = next((i for i, line in enumerate(lines) if line.strip() == "## Glossary Candidates"), 0)
        in_table = False
        header: list[str] = []
        for line in lines[start + 1:]:
            if not in_table and line.startswith("|"):
                cells = split_md_row(line)
                if cells and cells[0].casefold() in {"english term", "candidate", "term", "concept"}:
                    in_table = True
                    header = cells
                    continue
            if in_table and re.match(r"^\|[- :|]+\|$", line):
                continue
            if in_table and line.startswith("|"):
                cells = split_md_row(line)
                if len(cells) >= 4:
                    row = Candidate(
                        term=display_term(cells[0]),
                        cn=cells[1] if header and header[0].casefold() == "english term" else "",
                        simple=cells[2],
                        explain=cells[3],
                        module=path.name[:2],
                        topic=topic_label(path.name),
                        raw_file=path.name,
                        source_file=path.stem + ".html",
                        source_kind="raw-markdown",
                    )
                    (canonical if header and header[0].casefold() == "english term" else variable).append(row)
            elif in_table and line.strip() and not line.startswith("|"):
                break
    return canonical, variable


def quality_score(row: Candidate, group: Group) -> int:
    text = f"{row.simple} {row.explain}".casefold()
    score = 0
    if row.raw_file == group.anchor_file:
        score += 100
    if norm(row.term) == norm(group.term):
        score += 45
    if row.cn and "category" not in row.cn.casefold():
        score += 20
    if 20 <= len(row.simple) <= 220:
        score += 10
    if any(bad in text for bad in ["page label", "navigation", "section", "placeholder", "not explicitly", "potential missing"]):
        score -= 35
    if "�" in row.simple or "�?" in row.simple or "�" in row.cn:
        score -= 50
    return score


def choose_definition(group: Group, canonical: list[Candidate], variable: list[Candidate]) -> tuple[str, str, str]:
    if group.term in OVERRIDES:
        return OVERRIDES[group.term]
    aliases = {norm(a) for a in group.aliases}
    choices = [row for row in canonical if norm(row.term) in aliases]
    if choices:
        row = max(choices, key=lambda r: quality_score(r, group))
        return row.cn, row.simple, row.explain
    choices = [row for row in variable if norm(row.term) in aliases]
    if choices:
        row = max(choices, key=lambda r: quality_score(r, group))
        return infer_cn(group.term), row.simple, f"围绕 {group.term} 的专业定义或工程语境。"
    return "", "", ""


def infer_cn(term: str) -> str:
    # Only used for a small number of technical rows in candidate-only tables.
    dictionary = {
        "accuracy": "准确率", "precision": "精确率", "recall": "召回率", "evaluation": "评测",
        "benchmark": "基准测试", "guardrail": "安全护栏", "hallucination": "幻觉", "factuality": "事实性",
        "workflow fit": "工作流匹配度", "workflow discovery": "工作流发现", "technical scoping": "技术范围界定",
        "monitoring": "监控", "observability": "可观测性", "deployment readiness": "部署就绪度",
        "failure mode": "失败模式", "failure handling": "失败处理", "retry": "重试", "fallback": "回退",
        "timeout": "超时", "error handling": "错误处理", "permission": "权限", "access control": "访问控制",
        "ai provider": "AI 提供商", "model family": "模型家族", "provider strategy": "提供商策略",
        "openai": "OpenAI", "anthropic": "Anthropic", "google ai": "Google AI", "meta ai": "Meta AI",
        "mistral ai": "Mistral AI", "deepseek": "DeepSeek", "qwen": "通义千问（Qwen）", "gpt": "GPT",
        "claude": "Claude", "gemini": "Gemini", "llama": "Llama", "ai assistant": "AI 助手",
        "chatbot": "聊天机器人", "coding assistant": "编程助手", "coding agent": "编程智能体", "ai ide": "AI 集成开发环境",
        "computer use": "计算机操作", "agent framework": "智能体框架", "agents sdk": "智能体 SDK",
        "langgraph": "LangGraph", "agent architecture": "智能体架构", "agent orchestration": "智能体编排",
        "state graph": "状态图", "agent runtime": "智能体运行时", "planner": "规划器", "executor": "执行器",
        "tool router": "工具路由器", "middleware": "中间件", "ai workflow platform": "AI 工作流平台",
        "workflow automation": "工作流自动化", "automation platform": "自动化平台", "low code platform": "低代码平台",
        "no code platform": "无代码平台", "ai step": "AI 步骤", "llm chain": "LLM 链", "rag pipeline": "RAG 流水线",
        "trigger": "触发器", "action": "动作", "connector": "连接器", "api orchestration": "API 编排",
        "human approval step": "人工批准步骤", "backend platform": "后端平台", "managed database": "托管数据库",
        "edge function": "边缘函数", "serverless": "无服务器架构", "edge compute": "边缘计算", "edge network": "边缘网络",
        "developer platform": "开发者平台", "deploy preview": "部署预览", "rls": "行级安全（RLS）", "cloud platform": "云平台",
        "javascript": "JavaScript", "typescript": "TypeScript", "python": "Python", "node.js": "Node.js",
        "fastapi": "FastAPI", "express": "Express", "react": "React", "next.js": "Next.js", "redis": "Redis",
        "cache": "缓存", "key value store": "键值存储", "data warehouse": "数据仓库", "data pipeline": "数据流水线",
        "saas": "软件即服务（SaaS）", "payment api": "支付 API", "webhook": "Webhook",
    }
    return dictionary.get(norm(term), "")


PRIMARY_ANCHORS = {
    "Data Curation": "04-training-data.md",
    "Feed-Forward Network": "02-transformer.md",
    "Modality": "03-multimodal-models.md",
    "Model Runtime": "10-model-serving.md",
    "Next-Token Prediction": "04-pre-training.md",
    "Vector Database": "08-vector-database.md",
    "Action": "09-agent-loop.md",
    "Agent Framework": "15-agent-frameworks.md",
    "Authentication": "17-data-api-authentication.md",
    "Authorization": "17-data-api-authentication.md",
}


def coalesce_duplicate_groups() -> None:
    """Ensure every output concept has exactly one primary category."""
    by_term: dict[str, Group] = {}
    order: list[str] = []
    for group in GROUPS:
        key = group.term
        if key not in by_term:
            by_term[key] = group
            order.append(key)
            continue
        current = by_term[key]
        preferred_anchor = PRIMARY_ANCHORS.get(key)
        if preferred_anchor and group.anchor_file == preferred_anchor:
            group.aliases = list(dict.fromkeys([*group.aliases, *current.aliases]))
            by_term[key] = group
        else:
            current.aliases = list(dict.fromkeys([*current.aliases, *group.aliases]))
    GROUPS[:] = [by_term[key] for key in order]


def source_topic_text(group: Group, rows: list[Candidate]) -> str:
    return f"{group.module} / {topic_label(group.anchor_file)}"


def escape_md(value: str) -> str:
    return clean_text(value).replace("|", "\\|").replace("\n", " ")


def reason_for_merge(original: str, group: Group) -> str:
    original_norm = norm(original)
    base_norm = norm(group.term)
    alias_norms = {norm(a) for a in group.aliases}
    if original_norm == base_norm:
        return "Same normalized label; repeated source occurrence consolidated"
    if original_norm in {norm(a) for a in group.aliases[1:]} and len(display_term(original)) <= 6:
        return "Important abbreviation merged into the canonical expanded concept"
    if "-" in original or original.casefold() != original or original_norm == base_norm:
        return "Case, hyphen, spacing, or capitalization variant merged"
    if original_norm in alias_norms:
        return "Synonym or expanded/short form merged into one concept"
    return "Semantically equivalent wording merged"


def dropped_reason(term: str) -> str:
    t = display_term(term)
    n = norm(t)
    words = n.split()
    if t.startswith("`") or "http" in t.casefold() or t.endswith((".html", ".md")):
        return "Navigation, asset, URL, or page-label artifact"
    if any(x in n for x in ["does not equal", "versus", " vs ", " -> ", "—", " the ", " a ", " an "]):
        return "Comparison sentence or non-atomic phrase"
    if len(words) >= 6:
        return "Long-tail phrase without an independent glossary concept"
    if n in {"a", "an", "the", "and", "or", "of", "to", "from", "with", "for", "in", "on", "at", "as", "by", "is", "are", "be"}:
        return "Ordinary English function word"
    if any(x in n for x in ["example", "page", "section", "label", "visual", "placeholder", "heading", "analogy", "location"]):
        return "Page structure, example, or explanatory label"
    if len(words) <= 2 and all(len(w) <= 4 for w in words) and not re.search(r"[A-Z]", t):
        return "Generic short word without a stable AI-specific meaning"
    return "Generic or context-specific wording without an independent AI concept"


def build_outputs() -> dict:
    define_groups()
    coalesce_duplicate_groups()
    raw_rows, all_raw_count, header_count = load_all_raw()
    canonical, variable = load_markdown_evidence()
    by_norm: dict[str, list[Candidate]] = defaultdict(list)
    for row in raw_rows:
        by_norm[norm(row.term)].append(row)

    alias_owner: dict[str, Group] = {}
    collisions: list[tuple[str, str, str]] = []
    for group in GROUPS:
        for alias in group.aliases:
            key = norm(alias)
            if not key:
                continue
            if key in alias_owner and alias_owner[key].term != group.term:
                collisions.append((key, alias_owner[key].term, group.term))
                continue
            alias_owner[key] = group

    for group in GROUPS:
        seen: set[int] = set()
        for alias in group.aliases:
            for row in by_norm.get(norm(alias), []):
                ident = id(row)
                if ident not in seen:
                    group.rows.append(row)
                    seen.add(ident)

    retained: list[dict] = []
    for group in GROUPS:
        if not group.rows:
            continue
        cn, simple, explain = choose_definition(group, canonical, variable)
        if not cn:
            cn = infer_cn(group.term)
        if not simple:
            simple = next((r.simple for r in group.rows if r.simple and len(r.simple) > 20), "A named AI or software concept used in the source material.")
        if not explain:
            explain = f"与 {group.term} 相关的专业概念，用于理解 AI 系统或其工程实现。"
        sources = sorted({r.raw_file for r in group.rows if r.raw_file})
        retained.append({
            "group": group,
            "term": group.term,
            "cn": cn,
            "simple": simple,
            "explain": explain,
            "module_topic": source_topic_text(group, group.rows),
            "sources": sources,
            "rows": group.rows,
        })

    retained_norm = {norm(x["term"]) for x in retained}
    matched_row_ids = {id(row) for item in retained for row in item["rows"]}
    clean_unique = {norm(row.term): row.term for row in raw_rows}
    mapped_unique: dict[str, Group] = {}
    for item in retained:
        for row in item["rows"]:
            mapped_unique[norm(row.term)] = item["group"]

    # All unique raw labels that map to a retained concept. Exact duplicates are
    # counted once in the merge table; raw-row repeats are tracked separately.
    merge_rows: list[dict] = []
    for item in retained:
        group = item["group"]
        label_rows: dict[str, list[Candidate]] = defaultdict(list)
        for row in item["rows"]:
            label_rows[display_term(row.term)].append(row)
        for original, original_rows in sorted(label_rows.items(), key=lambda kv: norm(kv[0])):
            source_topics = sorted({f"{r.module} / {topic_label(r.raw_file)}" for r in original_rows})
            merge_rows.append({
                "Original Term": original,
                "Merged Into": group.term,
                "Reason": reason_for_merge(original, group),
                "Source Topic": "; ".join(source_topics),
            })

    # Keep one actual source label per concept out of the semantic merge count.
    # Prefer the expanded form if present; otherwise use the first source label.
    representatives: set[tuple[str, str]] = set()
    for item in retained:
        labels = sorted({display_term(r.term) for r in item["rows"]}, key=lambda x: (len(x), norm(x), x))
        expanded = next((label for alias in item["group"].aliases for label in labels if norm(label) == norm(alias) and len(label) > 3), None)
        representative = expanded or labels[0]
        representatives.add((item["group"].term, representative))
    merged_unique = sum(1 for row in merge_rows if (row["Merged Into"], row["Original Term"]) not in representatives)
    mapped_unique_count = len({(row["Merged Into"], row["Original Term"]) for row in merge_rows})
    exact_duplicate_rows = len(raw_rows) - len(clean_unique)
    dropped_unique = len(clean_unique) - len({norm(row["Original Term"]) for row in merge_rows})

    covered_files = sorted({row.raw_file for item in retained for row in item["rows"]})
    covered_modules = sorted({item["group"].module for item in retained})
    all_files = sorted({row.raw_file for row in raw_rows})
    all_modules = sorted({row.module for row in raw_rows})
    source_counts = Counter(row.raw_file for item in retained for row in item["rows"])
    module_counts = Counter(item["group"].module for item in retained)

    # Build the full dropped summary by unique raw label, without adding a huge
    # second glossary table to the audit file.
    mapped_norms = {norm(row["Original Term"]) for row in merge_rows}
    drop_reason_counts = Counter()
    drop_examples: dict[str, list[str]] = defaultdict(list)
    for key, original in sorted(clean_unique.items()):
        if key in mapped_norms:
            continue
        reason = dropped_reason(original)
        drop_reason_counts[reason] += 1
        if len(drop_examples[reason]) < 40:
            drop_examples[reason].append(original)

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    AUDIT_DIR.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["English Term", "中文", "Simple English", "中文小白理解", "Module/Topic", "Source Raw File"])
        for item in retained:
            writer.writerow([
                item["term"], item["cn"], item["simple"], item["explain"],
                item["module_topic"], "; ".join(item["sources"]),
            ])

    groups_by_topic: dict[str, list[dict]] = defaultdict(list)
    for item in retained:
        groups_by_topic[item["module_topic"]].append(item)
    md_lines = [
        "# Semantic AI Glossary",
        "",
        f"> {len(retained)} retained concepts from {all_raw_count:,} all-raw rows across {len(all_files)} raw files. Header artifacts were excluded before semantic review.",
        "",
        "The glossary keeps one canonical concept per row. Case, hyphenation, plurals, abbreviations, and true aliases are consolidated, while distinct engineering concepts such as Search vs Retrieval vs Reranking, Training vs Fine-Tuning vs Inference, and Latency vs Throughput vs TTFT vs Tokens per Second remain separate.",
        "",
    ]
    for topic in sorted(groups_by_topic, key=lambda x: (x.split(" / ")[0], x)):
        md_lines.extend([f"## {topic}", "", "| English Term | 中文 | Simple English | 中文小白理解 |", "|---|---|---|---|"])
        for item in sorted(groups_by_topic[topic], key=lambda x: x["term"].casefold()):
            md_lines.append("| " + " | ".join([
                escape_md(item["term"]), escape_md(item["cn"]), escape_md(item["simple"]), escape_md(item["explain"])
            ]) + " |")
        md_lines.append("")
    OUT_MD.write_text("\n".join(md_lines).rstrip() + "\n", encoding="utf-8")

    dup_lines = [
        "# Semantic Duplicate and Exclusion Audit",
        "",
        "## Exact statistics",
        "",
        f"- All-raw rows read: **{all_raw_count:,}**.",
        f"- Header/artifact rows excluded before review: **{header_count:,}**.",
        f"- Candidate rows reviewed: **{len(raw_rows):,}**.",
        f"- Unique candidate labels after whitespace/case/format normalization: **{len(clean_unique):,}**.",
        f"- Exact repeated raw rows within those labels: **{exact_duplicate_rows:,}**.",
        f"- Retained semantic concepts: **{len(retained):,}**.",
        f"- Unique source-label/concept mappings into retained concepts: **{mapped_unique_count:,}**.",
        f"- Semantic merge count (mappings minus one representative mapping per retained concept): **{merged_unique:,}**.",
        f"- Unique labels excluded as generic, structural, brand/example, or long-tail wording: **{dropped_unique:,}**.",
        f"- Source coverage: **{len(covered_files)}/{len(all_files)} raw files**, **{len(covered_modules)}/{len(all_modules)} modules**.",
        "",
        "The merge count is mapping-level rather than row-level: exact repeated source rows are counted separately above, while each distinct source label/concept mapping is listed once in the audit table.",
        "",
        "## Retained concepts by module",
        "",
        "| Module | Retained concepts | Source files contributing rows |",
        "|---|---:|---:|",
    ]
    for module in all_modules:
        files = {row.raw_file for item in retained if item["group"].module == module for row in item["rows"]}
        dup_lines.append(f"| {module} | {module_counts.get(module, 0)} | {len(files)} |")
    dup_lines.extend(["", "## Semantic merges", "", "| Original Term | Merged Into | Reason | Source Topic |", "|---|---|---|---|"])
    for row in sorted(merge_rows, key=lambda x: (x["Merged Into"].casefold(), x["Original Term"].casefold(), x["Source Topic"])):
        dup_lines.append("| " + " | ".join(escape_md(row[k]) for k in ["Original Term", "Merged Into", "Reason", "Source Topic"]) + " |")
    dup_lines.extend(["", "## Exclusion summary", "", "| Exclusion reason | Unique labels |", "|---|---:|"])
    for reason, count in drop_reason_counts.most_common():
        dup_lines.append(f"| {escape_md(reason)} | {count} |")
    dup_lines.extend(["", "## Exclusion examples", ""])
    for reason, examples in drop_examples.items():
        dup_lines.append(f"### {reason}")
        dup_lines.append("")
        dup_lines.append("; ".join(f"`{escape_md(x)}`" for x in examples))
        dup_lines.append("")
    if collisions:
        dup_lines.extend(["## Alias collisions reviewed", "", "Some short labels occur in more than one semantic neighborhood. The first explicit group owns the label in this run; no collision changed the required Search/Retrieval/Reranking or Training/Fine-Tuning/Inference distinctions.", ""])
        for key, left, right in collisions:
            dup_lines.append(f"- `{key}`: `{left}` vs `{right}`")
        dup_lines.append("")
    OUT_DUP.write_text("\n".join(dup_lines).rstrip() + "\n", encoding="utf-8")

    # Missing-term report is deliberately separate from the retained glossary:
    # these are valuable next-step concepts not represented by a retained row.
    missing_lines = [
        "# Missing AI Glossary Terms",
        "",
        "The entries below are important follow-up concepts identified from the raw files' Potential Missing Concepts sections and from coverage gaps in the final semantic glossary. They are not presented as source-defined glossary entries.",
        "",
        "| Missing Term | Module | Topic | Why Important | Recommended Action |",
        "|---|---|---|---|---|",
    ]
    missing_seen: set[str] = set()
    for module, topic, term, why, action in MISSING_SPECS:
        key = norm(term)
        if key in retained_norm or key in missing_seen:
            continue
        missing_seen.add(key)
        missing_lines.append("| " + " | ".join(escape_md(x) for x in [term, module, topic, why, action]) + " |")
    missing_lines.extend(["", f"Missing entries listed: **{len(missing_seen)}**.", ""])
    OUT_MISSING.write_text("\n".join(missing_lines), encoding="utf-8")

    return {
        "all_raw_rows": all_raw_count,
        "header_rows": header_count,
        "candidate_rows": len(raw_rows),
        "unique_labels": len(clean_unique),
        "exact_duplicate_rows": exact_duplicate_rows,
        "retained_concepts": len(retained),
        "mapped_unique_labels": mapped_unique_count,
        "merged_unique_labels": merged_unique,
        "dropped_unique_labels": dropped_unique,
        "raw_files": len(all_files),
        "covered_files": len(covered_files),
        "modules": len(all_modules),
        "covered_modules": len(covered_modules),
        "missing_terms": len(missing_seen),
        "collisions": len(collisions),
    }


if __name__ == "__main__":
    result = build_outputs()
    for key, value in result.items():
        print(f"{key}={value}")
