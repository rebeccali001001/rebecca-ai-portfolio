# Missing AI Glossary Terms

The entries below are important follow-up concepts identified from the raw files' Potential Missing Concepts sections and from coverage gaps in the final semantic glossary. They are not presented as source-defined glossary entries.

| Missing Term | Module | Topic | Why Important | Recommended Action |
|---|---|---|---|---|
| Markov Decision Process (MDP) | 01 | Reinforcement Learning | The formal state, action, transition, and reward model behind reinforcement-learning problems is not defined. | Add a foundational RL concept page and distinguish MDP from a generic workflow. |
| Q-Learning | 01 | Reinforcement Learning | A canonical value-based RL algorithm is absent even though reward and policy concepts appear. | Add an algorithm entry with state-action value and update intuition. |
| Policy Gradient | 01 | Reinforcement Learning | A major family of policy-optimization algorithms is missing from the RL path. | Add a method entry and contrast it with value-based learning. |
| Multi-Layer Perceptron (MLP) | 02 | Neural Networks | The common fully connected network name is absent from the architecture coverage. | Add an architecture entry and distinguish it from a generic neural network. |
| Sparse Attention | 02 | Attention | Attention sparsity is useful for long-context efficiency but is not represented as a standalone concept. | Add a mechanism entry with the accuracy/compute trade-off. |
| U-Net | 02 | Diffusion Models | The dominant denoising architecture is not covered by the diffusion glossary. | Add a model-component entry and explain its role in denoising. |
| Classifier-Free Guidance | 02 | Diffusion Models | A standard control method for conditional diffusion is absent. | Add a method entry with guidance-strength intuition. |
| DDPM | 02 | Diffusion Models | The canonical diffusion training/sampling family is missing as an important abbreviation. | Add DDPM and expand the acronym. |
| Mixture of Experts (MoE) | 03 | Model Types & Families | Sparse expert routing is a major modern model architecture and is not retained in the final set. | Add a model-architecture entry and distinguish experts from layers. |
| Vision-Language-Action Model (VLA) | 03 | Model Types & Families | The model family connecting perception, language, and actions is an important agent/robotics concept. | Add a model-type entry with modality boundaries. |
| QLoRA | 04 | Fine-Tuning | Quantized LoRA is a common practical fine-tuning method missing from the source candidates. | Add it as a companion entry to LoRA and quantization. |
| Direct Preference Optimization (DPO) | 04 | Preference Learning / RLHF | A widely used preference-optimization method is not present in the raw candidate inventory. | Add DPO and compare it with RLHF at a high level. |
| Proximal Policy Optimization (PPO) | 04 | Preference Learning / RLHF | The standard RL optimizer used in many RLHF pipelines is absent. | Add PPO as an algorithm entry, not as a synonym for RLHF. |
| RLAIF | 04 | Preference Learning / RLHF | AI-generated preference feedback is a common alignment variant that is not covered. | Add the acronym and distinguish AI feedback from human feedback. |
| Constitutional AI | 04 | Preference Learning / RLHF | A named safety/alignment approach is missing from the preference-learning coverage. | Add a method entry and link it to self-critique and principles. |
| Logits | 05 | Next-Token Prediction | The pre-softmax scores used in token selection are missing from the decoding explanation. | Add a decoding-mechanics entry and distinguish logits from probabilities. |
| Nucleus Sampling | 05 | Sampling / Temperature | Top-p is a standard decoding method but is not consistently represented as a standalone concept. | Add the full name and link it to Top-p Sampling. |
| Speculative Decoding | 05 | Inference | A key latency optimization using a draft model is absent from the inference glossary. | Add a serving-optimization entry and explain quality preservation. |
| Paged KV Cache | 05 | KV Cache | Paged cache management is central to efficient serving but is not fully covered. | Add a systems entry and relate it to memory fragmentation. |
| Constrained Decoding | 06 | Structured Outputs | Format-constrained token generation is an important mechanism missing from structured output coverage. | Add a mechanism entry and distinguish it from post-hoc parsing. |
| Role Prompting | 06 | Prompt Design | Assigning a role is common prompt practice but is not a first-class concept. | Add it as a prompting technique with limits. |
| Developer Prompt | 06 | System Prompts | Many production APIs use a developer-instruction layer that is not represented. | Add it and distinguish it from system and user messages. |
| ControlNet | 07 | Image Generation | A standard conditioning/control architecture is absent from image-generation coverage. | Add a model-component entry and explain conditioning inputs. |
| Latent Diffusion | 07 | Image Generation | The latent-space form of diffusion is important for understanding modern image models. | Add a mechanism entry and distinguish latent from pixel space. |
| Cosine Similarity | 08 | Vector Search | The common measure for comparing embedding direction is absent from vector search. | Add a similarity metric with a small geometric explanation. |
| Dot Product | 08 | Vector Search | A common vector similarity operation is not retained as an independent concept. | Add it and contrast it with cosine similarity. |
| Euclidean Distance | 08 | Vector Search | Distance-based nearest-neighbor search needs a canonical distance metric entry. | Add it and explain when magnitude matters. |
| BM25 | 08 | Retrieval | The standard lexical retrieval algorithm is missing, leaving keyword search underspecified. | Add BM25 and compare it with semantic and hybrid search. |
| HNSW | 08 | Vector Search | A widely used approximate-nearest-neighbor index is absent. | Add HNSW as an index-structure entry. |
| FAISS | 08 | Vector Search | A widely used vector-search library is not represented in the implementation layer. | Add it as a named library, clearly separate from a vector database. |
| Mean Reciprocal Rank (MRR) | 08 | Reranking | A standard ranking metric is missing from the retrieval evaluation vocabulary. | Add MRR and define its rank-sensitive behavior. |
| Normalized Discounted Cumulative Gain (NDCG) | 08 | Reranking | A standard graded-relevance ranking metric is absent. | Add NDCG and explain why higher ranks matter more. |
| Precision@k | 08 | Reranking | Top-k retrieval quality needs a precision-at-k metric entry. | Add the notation and define k explicitly. |
| Recall@k | 08 | Reranking | Top-k retrieval coverage needs a recall-at-k metric entry. | Add the notation and define the relevant set. |
| State Machine | 09 | Agent Loop | Explicit state-machine orchestration is important for controllable agents but is absent. | Add a control-architecture entry and contrast it with free-form loops. |
| Planner-Executor Pattern | 09 | Planning | Separating planning from execution is a common agent design pattern not represented. | Add a pattern entry and list its handoff risks. |
| Autoscaling | 10 | Model Serving | Production serving needs a capacity-control concept beyond raw throughput and latency. | Add autoscaling with trigger and capacity semantics. |
| Model Sharding | 10 | Model Serving | Splitting a model across devices is a standard deployment strategy missing from runtime coverage. | Add a systems entry and distinguish it from tensor parallelism. |
| FP16 | 10 | Quantization | Common numeric formats are not named even though precision and quantization are discussed. | Add a precision-format entry and link it to memory and quality. |
| BF16 | 10 | Quantization | BFloat16 is a common training/serving format absent from the precision vocabulary. | Add it beside FP16 and explain the practical distinction. |
| ROC-AUC | 11 | Evaluation | Binary-classification evaluation lacks a threshold-independent ranking metric. | Add ROC-AUC and define what is being ranked. |
| BLEU | 11 | Evaluation | Text-generation evaluation lacks a canonical machine-translation overlap metric. | Add BLEU with a caveat about reference overlap. |
| ROUGE | 11 | Evaluation | Summarization evaluation lacks a canonical reference-overlap metric. | Add ROUGE and distinguish it from factuality. |
| Model Card | 11 | Permissions & Safety | Model documentation for intended use, limitations, and evaluation is missing. | Add model cards as a governance/documentation concept. |
| Dataset Card | 11 | Permissions & Safety | Dataset documentation is needed to make training-data provenance and limitations inspectable. | Add dataset cards and connect them to data governance. |
| PII Redaction | 11 | Permissions & Safety | Privacy controls need a concrete transformation concept beyond general privacy. | Add redaction and distinguish it from access control. |
| Blue-Green Deployment | 12 | Deployment | A second release strategy is useful for explaining safe rollout and rollback. | Add blue-green deployment and contrast it with canary release. |
| Service-Level Objective (SLO) | 12 | Monitoring | Operational monitoring lacks a target-based reliability concept. | Add SLO and distinguish it from an observed metric. |
| Alerting | 12 | Monitoring | Monitoring needs an explicit action-trigger concept. | Add alerting with threshold and routing semantics. |
| Model License | 13 | Open vs Closed / Local Models | Open weights do not by themselves explain what users may legally do. | Add licensing as a separate ecosystem concept. |
| Codebase Indexing | 14 | AI Assistants & Coding Tools | Repository-aware assistants need an explicit indexing/retrieval concept. | Add it and connect it to repository context. |
| Agent Evaluation | 15 | Agent Frameworks | Agent quality needs task-level evaluation beyond model benchmarks. | Add agent evaluation with success and failure criteria. |
| Idempotency | 16 | AI Workflow Platforms | Workflow retries need a way to avoid applying the same side effect twice. | Add idempotency as a reliability concept. |
| OAuth | 17 | Data, APIs & Authentication | Modern API authentication needs a delegated-authorization protocol concept. | Add OAuth and distinguish it from authentication itself. |
| JSON Web Token (JWT) | 17 | Data, APIs & Authentication | Token-based identity propagation is missing from API authentication coverage. | Add JWT and describe signed claims without treating it as encryption. |
| Role-Based Access Control (RBAC) | 17 | Data, APIs & Authentication | Permission design lacks the standard role-based model. | Add RBAC and distinguish roles from individual permissions. |
| Row-Level Security (RLS) | 17 | Data, APIs & Authentication | Database-level authorization needs an explicit row-filtering concept. | Add RLS and distinguish it from application checks. |
| CORS | 17 | Data, APIs & Authentication | Browser-to-API integration needs a cross-origin policy concept. | Add CORS with browser scope and server response behavior. |
| CSRF | 17 | Data, APIs & Authentication | Session-based web security lacks a cross-site request-forgery concept. | Add CSRF and distinguish it from XSS and prompt injection. |
| TLS | 17 | Data, APIs & Authentication | Transport security needs a protocol-level encryption concept. | Add TLS and link HTTPS to it. |
| Rate Limiting | 17 | Data, APIs & Authentication | Shared APIs need an abuse and capacity control concept. | Add rate limiting with request-window semantics. |
| Pagination | 17 | Data, APIs & Authentication | Large API responses need a standard result-partitioning concept. | Add pagination and distinguish it from chunking. |
| Primary Key | 18 | Backend & Data Platforms | Database identity is not represented in the supporting architecture vocabulary. | Add primary key and distinguish it from a model parameter. |
| Foreign Key | 18 | Backend & Data Platforms | Relational integrity needs a cross-table reference concept. | Add foreign key with referential-integrity intuition. |
| Database Index | 18 | Backend & Data Platforms | Database performance needs an explicit lookup-acceleration concept. | Add an index and distinguish it from a vector index. |
| Transaction | 18 | Backend & Data Platforms | Multi-step data changes need an all-or-nothing consistency concept. | Add transactions with commit/rollback semantics. |
| Docker | 18 | Web & Cloud Platforms | Deployment vocabulary lacks the standard container packaging technology. | Add Docker as a named technology and define the container boundary. |
| Kubernetes | 18 | Web & Cloud Platforms | Production container orchestration is absent from the cloud-platform coverage. | Add Kubernetes as an orchestration platform. |

Missing entries listed: **68**.
