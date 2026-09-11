# Semantic Duplicate and Exclusion Audit

## Exact statistics

- All-raw rows read: **24,356**.
- Header/artifact rows excluded before review: **22**.
- Candidate rows reviewed: **24,334**.
- Unique candidate labels after whitespace/case/format normalization: **14,468**.
- Exact repeated raw rows within those labels: **9,866**.
- Retained semantic concepts: **470**.
- Unique source-label/concept mappings into retained concepts: **955**.
- Semantic merge count (mappings minus one representative mapping per retained concept): **485**.
- Unique labels excluded as generic, structural, brand/example, or long-tail wording: **13,887**.
- Source coverage: **108/108 raw files**, **19/19 modules**.

The merge count is mapping-level rather than row-level: exact repeated source rows are counted separately above, while each distinct source label/concept mapping is listed once in the audit table.

## Retained concepts by module

| Module | Retained concepts | Source files contributing rows |
|---|---:|---:|
| 01 | 53 | 77 |
| 02 | 46 | 41 |
| 03 | 32 | 57 |
| 04 | 29 | 42 |
| 05 | 28 | 50 |
| 06 | 16 | 53 |
| 07 | 17 | 24 |
| 08 | 34 | 46 |
| 09 | 32 | 69 |
| 10 | 33 | 57 |
| 11 | 43 | 71 |
| 12 | 24 | 53 |
| 13 | 19 | 21 |
| 14 | 11 | 12 |
| 15 | 6 | 5 |
| 16 | 9 | 5 |
| 17 | 16 | 37 |
| 18 | 11 | 8 |
| 19 | 11 | 9 |

## Semantic merges

| Original Term | Merged Into | Reason | Source Topic |
|---|---|---|---|
| A/B test | A/B Test | Same normalized label; repeated source occurrence consolidated | 01 / Machine Learning; 03 / Foundation Models |
| Access control | Access Control | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| access control | Access Control | Same normalized label; repeated source occurrence consolidated | 08 / Grounding; 08 / Rag; 08 / Retrieval; 08 / Vector Search; 09 / Human in the Loop; 09 / Model Context Protocol (MCP); 10 / Model Serving; 11 / Permissions Safety; 12 / Adoption; 12 / Deployment; 12 / Integration; 17 / Data, APIs & Authentication; 18 / Backend & Data Platforms |
| Accuracy | Accuracy | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 01 / Machine Learning; 03 / Foundation Models |
| accuracy | Accuracy | Same normalized label; repeated source occurrence consolidated | 01 / Supervised Learning; 03 / Large Language Models; 03 / Multimodal Models; 03 / Vision Foundation Models; 04 / Prompting Vs Rag Vs Fine Tuning; 04 / Training Data; 05 / Inference; 05 / Sampling Temperature; 06 / Structured Outputs |
| action | Action | Same normalized label; repeated source occurrence consolidated | 01 / Artificial Intelligence; 01 / Reinforcement Learning; 09 / AI Agent; 09 / Agent Loop; 09 / Human in the Loop; 09 / Model Context Protocol (MCP); 09 / Planning; 09 / Skills / Plugins; 09 / Tool Calling; 10 / Api; 11 / Failure Modes; 11 / Functional Tests; 11 / Guardrails; 11 / Permissions Safety; 12 / Continuous Improvement; 15 / How AI Agents Are Built; 16 / AI Workflow Platforms; 16 / Automation Platforms; 17 / Frontend & Backend |
| Action | Action | Same normalized label; repeated source occurrence consolidated | 01 / Machine Learning; 01 / Reinforcement Learning; 03 / Foundation Models |
| ACTION | Action | Same normalized label; repeated source occurrence consolidated | 11 / Permissions Safety; 16 / Automation Platforms |
| Activation | Activation | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning |
| activation | Activation | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models |
| Activation Function | Activation Function | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 02 / Layers |
| agent architecture | Agent Architecture | Same normalized label; repeated source occurrence consolidated | 09 / Agent Loop |
| agent collaboration | Agent Collaboration | Same normalized label; repeated source occurrence consolidated | 15 / Agent Frameworks; 15 / How AI Agents Are Built |
| agent framework | Agent Framework | Same normalized label; repeated source occurrence consolidated | 15 / Agent Frameworks; 15 / How AI Agents Are Built; 16 / AI Workflow Platforms |
| AGENT FRAMEWORK | Agent Framework | Same normalized label; repeated source occurrence consolidated | 16 / AI Workflow Platforms |
| user goal | Agent Goal | Synonym or expanded/short form merged into one concept | 09 / Human in the Loop; 14 / General Agents & Computer Use; 15 / How AI Agents Are Built |
| agent loop | Agent Loop | Same normalized label; repeated source occurrence consolidated | 01 / Reinforcement Learning; 09 / AI Agent; 09 / Agent Loop; 09 / Human in the Loop; 09 / Memory State; 09 / Planning; 14 / AI Assistants & Coding Tools; 14 / General Agents & Computer Use; 15 / Agent Frameworks; 15 / How AI Agents Are Built |
| Agent Loop | Agent Loop | Same normalized label; repeated source occurrence consolidated | 01 / Reinforcement Learning; 09 / Agent Loop; 09 / Memory State; 09 / Multi-Agent Systems; 09 / Tool Calling |
| Memory | Agent Memory | Important abbreviation merged into the canonical expanded concept | 01 / Deep Learning; 03 / Foundation Models; 05 / Context Window; 09 / Memory State; 09 / Multi-Agent Systems |
| memory | Agent Memory | Important abbreviation merged into the canonical expanded concept | 03 / Large Language Models; 06 / Context Engineering; 09 / AI Agent; 09 / Memory State; 09 / Planning; 10 / GPU, VRAM & Unified Memory; 10 / Local AI vs Cloud AI; 10 / Model Serving; 10 / Quantization; 10 / Runtime Constraints; 10 / Vllm; 11 / Hallucination; 13 / Open vs Closed / Local Models; 15 / Agent Frameworks; 15 / How AI Agents Are Built; 16 / AI Workflow Platforms |
| memory component | Agent Memory | Synonym or expanded/short form merged into one concept | 15 / How AI Agents Are Built |
| State | Agent State | Important abbreviation merged into the canonical expanded concept | 01 / Machine Learning; 01 / Reinforcement Learning; 03 / Foundation Models; 09 / Memory State |
| state | Agent State | Important abbreviation merged into the canonical expanded concept | 01 / Reinforcement Learning; 02 / RNN / LSTM; 05 / KV Cache; 06 / Context Engineering; 06 / Prompt Design; 09 / Agent Loop; 09 / Memory State; 09 / Multi-Agent Systems; 09 / Planning; 14 / General Agents & Computer Use; 15 / Agent Frameworks; 15 / How AI Agents Are Built; 19 / Data Technologies |
| State management | Agent State | Case, hyphen, spacing, or capitalization variant merged | 03 / Foundation Models |
| state management | Agent State | Synonym or expanded/short form merged into one concept | 15 / Agent Frameworks |
| State persistence | Agent State | Case, hyphen, spacing, or capitalization variant merged | 03 / Foundation Models |
| agent system | Agent System | Same normalized label; repeated source occurrence consolidated | 14 / AI Assistants & Coding Tools; 15 / Agent Frameworks; 15 / How AI Agents Are Built |
| agent-environment interaction | Agent-Environment Interaction | Same normalized label; repeated source occurrence consolidated | 01 / Reinforcement Learning |
| agentic coding | Agentic Coding | Same normalized label; repeated source occurrence consolidated | 14 / AI Assistants & Coding Tools |
| Agents SDK | Agents SDK | Same normalized label; repeated source occurrence consolidated | 15 / Agent Frameworks; 16 / AI Workflow Platforms |
| Adoption | AI Adoption | Case, hyphen, spacing, or capitalization variant merged | 11 / Evaluation; 12 / Continuous Improvement; 12 / Integration; 12 / Technical Scoping; 12 / Workflow Discovery |
| adoption | AI Adoption | Synonym or expanded/short form merged into one concept | 12 / Adoption; 12 / Deployment; 12 / Integration; 12 / Monitoring; 19 / Frontend Technologies |
| AI Adoption | AI Adoption | Same normalized label; repeated source occurrence consolidated | 12 / Adoption |
| Agent | AI Agent | Important abbreviation merged into the canonical expanded concept | 01 / Machine Learning; 01 / Reinforcement Learning; 03 / Foundation Models; 10 / Api |
| agent | AI Agent | Important abbreviation merged into the canonical expanded concept | 01 / Reinforcement Learning; 09 / AI Agent; 09 / Human in the Loop; 09 / Memory State; 09 / Model Context Protocol (MCP); 09 / Multi-Agent Systems; 09 / Planning; 09 / Skills / Plugins; 10 / Api; 10 / Ollama; 10 / Vllm; 11 / Guardrails; 11 / Permissions Safety; 11 / Prompt Injection; 12 / Adoption; 13 / Major AI Providers; 14 / General Agents & Computer Use; 15 / Agent Frameworks; 15 / How AI Agents Are Built; 16 / AI Workflow Platforms; 16 / Automation Platforms |
| AI agent | AI Agent | Same normalized label; repeated source occurrence consolidated | 01 / Reinforcement Learning; 09 / AI Agent; 09 / Human in the Loop; 09 / Memory State; 09 / Model Context Protocol (MCP); 09 / Planning; 09 / Skills / Plugins; 11 / Permissions Safety; 14 / General Agents & Computer Use; 15 / How AI Agents Are Built |
| AI Agent | AI Agent | Same normalized label; repeated source occurrence consolidated | 09 / Memory State; 09 / Multi-Agent Systems; 09 / Tool Calling; 10 / Ollama; 12 / Technical Scoping |
| AI agents | AI Agent | Case, hyphen, spacing, or capitalization variant merged | 14 / AI Assistants & Coding Tools |
| AI assistant | AI Assistant | Same normalized label; repeated source occurrence consolidated | 12 / Adoption; 12 / Deployment; 14 / AI Assistants & Coding Tools; 14 / General Agents & Computer Use |
| AI IDE | AI IDE | Same normalized label; repeated source occurrence consolidated | 14 / AI Assistants & Coding Tools |
| AI opportunity assessment | AI Opportunity Assessment | Same normalized label; repeated source occurrence consolidated | 12 / Workflow Discovery |
| AI application | AI Product | Case, hyphen, spacing, or capitalization variant merged | 04 / Prompting Vs Rag Vs Fine Tuning; 06 / System Prompts; 09 / Model Context Protocol (MCP); 09 / Skills / Plugins; 09 / Tool Calling; 10 / Api; 11 / Permissions Safety; 15 / Agent Frameworks; 15 / How AI Agents Are Built |
| AI product | AI Product | Same normalized label; repeated source occurrence consolidated | 01 / Artificial Intelligence; 03 / Large Language Models; 05 / Tokenization; 08 / Vector Database; 09 / Memory State; 11 / Functional Tests; 12 / Adoption; 13 / Major AI Providers; 17 / Frontend & Backend |
| AI provider | AI Provider | Same normalized label; repeated source occurrence consolidated | 13 / Major AI Providers |
| AI step | AI Step | Same normalized label; repeated source occurrence consolidated | 16 / Automation Platforms |
| AI STEP | AI Step | Same normalized label; repeated source occurrence consolidated | 16 / Automation Platforms |
| AI WORKFLOW PLATFORM | AI Workflow Platform | Same normalized label; repeated source occurrence consolidated | 16 / AI Workflow Platforms |
| AI workflow platform | AI Workflow Platform | Same normalized label; repeated source occurrence consolidated | 16 / AI Workflow Platforms; 16 / Automation Platforms |
| AI Workflow Platform | AI Workflow Platform | Same normalized label; repeated source occurrence consolidated | 16 / Automation Platforms |
| Algorithm | Algorithm | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 01 / Machine Learning |
| algorithm | Algorithm | Same normalized label; repeated source occurrence consolidated | 01 / Supervised Learning; 03 / Vision Foundation Models; 04 / Training Data |
| Alignment | Alignment | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| alignment | Alignment | Same normalized label; repeated source occurrence consolidated | 03 / Multimodal Models; 04 / Pre Training; 04 / Preference Learning Rlhf; 07 / Image Generation |
| alignment training | Alignment Training | Same normalized label; repeated source occurrence consolidated | 04 / Preference Learning Rlhf |
| Anthropic | Anthropic | Same normalized label; repeated source occurrence consolidated | 13 / Major AI Providers; 13 / Model Types & Families; 14 / AI Assistants & Coding Tools |
| API endpoint | API Endpoint | Same normalized label; repeated source occurrence consolidated | 10 / Api |
| Endpoint | API Endpoint | Case, hyphen, spacing, or capitalization variant merged | 01 / Deep Learning |
| endpoint | API Endpoint | Synonym or expanded/short form merged into one concept | 05 / Inference; 10 / Model Serving; 19 / Backend Technologies |
| API integration | API Integration | Same normalized label; repeated source occurrence consolidated | 06 / Structured Outputs; 12 / Integration; 19 / Backend Technologies |
| API orchestration | API Orchestration | Same normalized label; repeated source occurrence consolidated | 16 / Automation Platforms |
| API request | API Request | Same normalized label; repeated source occurrence consolidated | 05 / Inference; 10 / Api; 10 / Model Serving; 10 / Vllm; 17 / Data, APIs & Authentication; 19 / Product Services |
| API response | API Response | Same normalized label; repeated source occurrence consolidated | 10 / Api; 10 / Model Serving; 17 / Data, APIs & Authentication |
| API | Application Programming Interface (API) | Important abbreviation merged into the canonical expanded concept | 01 / Deep Learning; 03 / Foundation Models; 03 / Large Language Models; 03 / Multimodal Models; 07 / Image Generation; 08 / Vector Search; 09 / Human in the Loop; 09 / Model Context Protocol (MCP); 10 / Api; 10 / Local AI vs Cloud AI; 10 / Model Serving; 10 / Ollama; 10 / Vllm; 12 / Deployment; 12 / Integration; 13 / Major AI Providers; 13 / Open vs Closed / Local Models; 14 / General Agents & Computer Use; 15 / How AI Agents Are Built; 16 / AI Workflow Platforms; 16 / Automation Platforms; 17 / Data, APIs & Authentication; 17 / Frontend & Backend; 18 / Backend & Data Platforms; 18 / Web & Cloud Platforms; 19 / Backend Technologies; 19 / Product Services |
| Application Programming Interface | Application Programming Interface (API) | Case, hyphen, spacing, or capitalization variant merged | 10 / Api; 17 / Data, APIs & Authentication; 19 / Product Services |
| application programming interface | Application Programming Interface (API) | Synonym or expanded/short form merged into one concept | 10 / Model Serving; 16 / AI Workflow Platforms |
| approval checkpoint | Approval Gate | Synonym or expanded/short form merged into one concept | 14 / General Agents & Computer Use |
| approval gate | Approval Gate | Same normalized label; repeated source occurrence consolidated | 09 / Human in the Loop; 11 / Guardrails; 11 / Permissions Safety |
| ANN | Approximate Nearest Neighbor (ANN) | Important abbreviation merged into the canonical expanded concept | 02 / Neural Networks; 08 / Vector Search |
| approximate nearest neighbor | Approximate Nearest Neighbor (ANN) | Synonym or expanded/short form merged into one concept | 08 / Vector Search |
| AI | Artificial Intelligence (AI) | Important abbreviation merged into the canonical expanded concept | 01 / Artificial Intelligence; 01 / Deep Learning; 01 / Machine Learning; 01 / Reinforcement Learning; 03 / Large Language Models; 03 / Scientific Models; 04 / Training Data; 05 / Tokenization; 06 / Prompt Design; 06 / Structured Outputs; 07 / Audio Generation; 07 / Generative Ai; 07 / Image Generation; 07 / Multimodal Ai; 07 / Video Generation; 09 / Human in the Loop; 09 / Multi-Agent Systems; 09 / Tool Calling; 10 / Local AI vs Cloud AI; 10 / Model Serving; 10 / Runtime Constraints; 11 / Deployment Readiness; 11 / Evaluation; 11 / Functional Tests; 12 / Adoption; 12 / Technical Scoping; 13 / Major AI Providers; 17 / Frontend & Backend; 19 / Product Services |
| Artificial Intelligence | Artificial Intelligence (AI) | Case, hyphen, spacing, or capitalization variant merged | 01 / Artificial Intelligence; 01 / Deep Learning; 01 / Machine Learning; 01 / Supervised Learning; 01 / Unsupervised Learning; 03 / Large Language Models; 07 / Multimodal Ai |
| artificial intelligence | Artificial Intelligence (AI) | Synonym or expanded/short form merged into one concept | 03 / Scientific Models; 04 / Training Data; 06 / Prompt Design; 06 / Structured Outputs; 07 / Audio Generation; 07 / Generative Ai; 07 / Image Generation; 07 / Video Generation; 10 / Latency; 11 / Deployment Readiness; 11 / Evaluation; 13 / Major AI Providers; 19 / Product Services |
| Artificial intelligence | Artificial Intelligence (AI) | Case, hyphen, spacing, or capitalization variant merged | 05 / Token |
| Attention | Attention | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 02 / Attention; 02 / Diffusion Models; 02 / Layers; 02 / Transformer |
| attention | Attention | Same normalized label; repeated source occurrence consolidated | 02 / RNN / LSTM; 02 / Transformer; 03 / Large Language Models; 03 / Multimodal Models; 04 / Pre Training; 05 / KV Cache |
| attention mechanism | Attention | Synonym or expanded/short form merged into one concept | 02 / Attention; 02 / Transformer; 07 / Image Generation |
| attention head | Attention Head | Same normalized label; repeated source occurrence consolidated | 02 / Attention |
| attention mask | Attention Mask | Same normalized label; repeated source occurrence consolidated | 02 / Attention |
| attention weight | Attention Weight | Same normalized label; repeated source occurrence consolidated | 02 / Attention; 02 / Transformer |
| Audio Generation | Audio Generation | Same normalized label; repeated source occurrence consolidated | 03 / Speech Audio Models; 07 / Audio Generation |
| audio generation | Audio Generation | Same normalized label; repeated source occurrence consolidated | 03 / Speech Audio Models; 07 / Audio Generation; 07 / Multimodal Ai |
| Audio-Language Model | Audio-Language Model | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning |
| Audit log | Audit Log | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| audit log | Audit Log | Same normalized label; repeated source occurrence consolidated | 08 / Grounding; 09 / Human in the Loop |
| authentication | Authentication | Same normalized label; repeated source occurrence consolidated | 09 / Human in the Loop; 10 / Model Serving; 12 / Deployment; 12 / Integration; 17 / Data, APIs & Authentication; 17 / Frontend & Backend; 18 / Backend & Data Platforms; 19 / Backend Technologies; 19 / Product Services |
| AUTHENTICATION | Authentication | Same normalized label; repeated source occurrence consolidated | 17 / Data, APIs & Authentication; 19 / Product Services |
| Authentication | Authentication | Same normalized label; repeated source occurrence consolidated | 17 / Frontend & Backend |
| authorization | Authorization | Same normalized label; repeated source occurrence consolidated | 08 / Retrieval; 09 / Human in the Loop; 09 / Tool Calling; 10 / Model Serving; 11 / Permissions Safety; 12 / Deployment; 12 / Integration; 17 / Data, APIs & Authentication |
| AUTHORIZATION | Authorization | Same normalized label; repeated source occurrence consolidated | 17 / Data, APIs & Authentication |
| autocomplete | Autocomplete | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models; 05 / Next Token Prediction; 14 / AI Assistants & Coding Tools |
| Autoencoder | Autoencoder | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning |
| autoencoder | Autoencoder | Same normalized label; repeated source occurrence consolidated | 01 / Unsupervised Learning; 07 / Image Generation |
| ASR | Automatic Speech Recognition (ASR) | Important abbreviation merged into the canonical expanded concept | 03 / Multimodal Models; 03 / Speech Audio Models |
| automatic speech recognition | Automatic Speech Recognition (ASR) | Synonym or expanded/short form merged into one concept | 03 / Speech Audio Models |
| Speech Recognition | Automatic Speech Recognition (ASR) | Case, hyphen, spacing, or capitalization variant merged | 01 / Deep Learning; 03 / Speech Audio Models |
| speech recognition | Automatic Speech Recognition (ASR) | Synonym or expanded/short form merged into one concept | 03 / Multimodal Models; 03 / Speech Audio Models; 05 / Inference; 07 / Audio Generation |
| AUTOMATION PLATFORM | Automation Platform | Same normalized label; repeated source occurrence consolidated | 16 / AI Workflow Platforms |
| automation platform | Automation Platform | Same normalized label; repeated source occurrence consolidated | 16 / AI Workflow Platforms; 16 / Automation Platforms |
| autoregressive generation | Autoregressive Generation | Same normalized label; repeated source occurrence consolidated | 02 / Attention; 03 / Large Language Models; 05 / Inference; 05 / KV Cache; 05 / Next Token Prediction; 05 / Token |
| Autoregressive Model | Autoregressive Modeling | Case, hyphen, spacing, or capitalization variant merged | 02 / Diffusion Models |
| autoregressive model | Autoregressive Modeling | Synonym or expanded/short form merged into one concept | 03 / Large Language Models |
| Availability | Availability | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 03 / Foundation Models |
| availability | Availability | Same normalized label; repeated source occurrence consolidated | 08 / Grounding; 10 / Local AI vs Cloud AI; 10 / Model Serving; 11 / Failure Handling; 12 / Deployment; 13 / Model Types & Families; 14 / General Agents & Computer Use; 17 / Deployment & Operations |
| backend | Backend | Same normalized label; repeated source occurrence consolidated | 10 / Api; 10 / Vllm; 17 / Data, APIs & Authentication; 17 / Frontend & Backend; 18 / Web & Cloud Platforms; 19 / Backend Technologies; 19 / Product Services |
| Backend | Backend | Same normalized label; repeated source occurrence consolidated | 10 / Api; 17 / Frontend & Backend |
| backend platform | Backend Platform | Same normalized label; repeated source occurrence consolidated | 18 / Backend & Data Platforms; 19 / Backend Technologies; 19 / Product Services |
| Backpropagation | Backpropagation | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning |
| backpropagation | Backpropagation | Same normalized label; repeated source occurrence consolidated | 02 / Attention; 03 / Large Language Models; 03 / Parameters; 04 / Pre Training |
| base model | Base Model | Same normalized label; repeated source occurrence consolidated | 01 / Artificial Intelligence; 03 / Large Language Models; 03 / Vision Foundation Models; 04 / Fine Tuning; 04 / Pre Training; 04 / Prompting Vs Rag Vs Fine Tuning |
| Base model | Base Model | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models; 04 / Fine Tuning |
| Batch | Batch | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 01 / Machine Learning |
| batch | Batch | Same normalized label; repeated source occurrence consolidated | 01 / Supervised Learning; 03 / Large Language Models; 04 / Pre Training; 04 / Training Data; 05 / KV Cache; 10 / Model Serving; 10 / Vllm |
| batch inference | Batch Inference | Same normalized label; repeated source occurrence consolidated | 05 / Inference |
| Batch Size | Batch Size | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning |
| batch size | Batch Size | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models; 04 / Pre Training; 05 / KV Cache; 10 / Runtime Constraints |
| Benchmark | Benchmark | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 01 / Machine Learning; 03 / Foundation Models |
| benchmark | Benchmark | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models; 03 / Multimodal Models; 03 / Scientific Models; 07 / Image Generation; 08 / Retrieval; 11 / Benchmarks; 11 / Hallucination; 12 / Deployment |
| bi-encoder | Bi-Encoder | Same normalized label; repeated source occurrence consolidated | 08 / Embeddings; 08 / Reranking; 08 / Vector Search |
| Bias | Bias | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 01 / Machine Learning; 02 / Layers; 03 / Foundation Models |
| bias | Bias | Same normalized label; repeated source occurrence consolidated | 01 / Supervised Learning; 03 / Multimodal Models; 03 / Parameters; 04 / Preference Learning Rlhf; 04 / Training Data; 05 / Inference; 07 / Image Generation; 09 / Human in the Loop; 11 / Failure Modes; 11 / Hallucination |
| browser agent | Browser Agent | Same normalized label; repeated source occurrence consolidated | 14 / General Agents & Computer Use |
| cache | Cache | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models; 05 / KV Cache; 18 / Web & Cloud Platforms; 19 / Data Technologies |
| Calibration | Calibration | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 01 / Machine Learning; 03 / Foundation Models |
| calibration | Calibration | Same normalized label; repeated source occurrence consolidated | 01 / Supervised Learning; 02 / Attention; 04 / Training Data; 09 / Human in the Loop; 10 / Quantization; 11 / Hallucination |
| Canary deployment | Canary Deployment | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| causal language model | Causal Language Modeling | Synonym or expanded/short form merged into one concept | 03 / Large Language Models |
| causal language modeling | Causal Language Modeling | Same normalized label; repeated source occurrence consolidated | 04 / Pre Training |
| Chain of thought | Chain-of-Thought | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| chatbot | Chatbot | Same normalized label; repeated source occurrence consolidated | 09 / AI Agent; 09 / Planning; 16 / AI Workflow Platforms |
| Checkpoint | Checkpoint | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning |
| checkpoint | Checkpoint | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models; 03 / Parameters; 04 / Pre Training; 09 / Human in the Loop |
| model checkpoint | Checkpoint | Synonym or expanded/short form merged into one concept | 07 / Image Generation |
| Chunk | Chunk | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| chunk | Chunk | Same normalized label; repeated source occurrence consolidated | 08 / Chunking; 08 / Embeddings; 08 / Grounding; 08 / Rag; 08 / Retrieval; 08 / Vector Database |
| Chunking | Chunking | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models; 08 / Chunking |
| chunking | Chunking | Same normalized label; repeated source occurrence consolidated | 08 / Embeddings; 08 / Grounding; 08 / Rag; 08 / Retrieval |
| Document 鈫?Chunking | Chunking | Case, hyphen, spacing, or capitalization variant merged | 08 / Chunking |
| Citation | Citation | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| citation | Citation | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models; 08 / Grounding; 08 / Rag; 08 / Retrieval; 14 / AI Assistants & Coding Tools |
| classification | Classification | Same normalized label; repeated source occurrence consolidated | 01 / Artificial Intelligence; 01 / Supervised Learning; 02 / Neural Networks; 02 / Transformer; 03 / Multimodal Models; 03 / Vision Foundation Models; 04 / Instruction Tuning; 05 / Inference; 11 / Failure Handling; 16 / Automation Platforms |
| Classification | Classification | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 01 / Machine Learning; 02 / CNN; 02 / Layers |
| Claude | Claude | Same normalized label; repeated source occurrence consolidated | 13 / Major AI Providers; 13 / Model Types & Families; 14 / AI Assistants & Coding Tools; 15 / Agent Frameworks |
| client | Client | Same normalized label; repeated source occurrence consolidated | 09 / Model Context Protocol (MCP); 19 / Backend Technologies |
| Cloud AI | Cloud AI | Same normalized label; repeated source occurrence consolidated | 10 / Local AI vs Cloud AI |
| cloud deployment | Cloud Deployment | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models; 10 / Api; 10 / Local AI vs Cloud AI; 10 / Runtime Constraints; 13 / Open vs Closed / Local Models; 17 / Deployment & Operations |
| Cloud model | Cloud Model | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| cloud model | Cloud Model | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models; 07 / Image Generation; 10 / Local AI vs Cloud AI; 13 / Open vs Closed / Local Models |
| cloud platform | Cloud Platform | Same normalized label; repeated source occurrence consolidated | 13 / Open vs Closed / Local Models; 18 / Web & Cloud Platforms |
| Clustering | Clustering | Same normalized label; repeated source occurrence consolidated | 01 / Machine Learning |
| clustering | Clustering | Same normalized label; repeated source occurrence consolidated | 01 / Unsupervised Learning |
| code completion | Code Completion | Same normalized label; repeated source occurrence consolidated | 07 / Code Generation; 11 / Benchmarks |
| code generation | Code Generation | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models; 07 / Code Generation; 07 / Image Generation; 07 / Text Generation; 11 / Benchmarks |
| Code Generation | Code Generation | Same normalized label; repeated source occurrence consolidated | 07 / Code Generation; 07 / Image Generation; 07 / Text Generation |
| code review | Code Review | Same normalized label; repeated source occurrence consolidated | 07 / Code Generation |
| codebase | Codebase | Same normalized label; repeated source occurrence consolidated | 19 / Backend Technologies |
| Coding Agent | Coding Agent | Same normalized label; repeated source occurrence consolidated | 05 / Context Window |
| coding agent | Coding Agent | Same normalized label; repeated source occurrence consolidated | 07 / Code Generation; 14 / AI Assistants & Coding Tools |
| coding assistant | Coding Assistant | Same normalized label; repeated source occurrence consolidated | 14 / AI Assistants & Coding Tools |
| Computational Unit | Computational Unit | Same normalized label; repeated source occurrence consolidated | 02 / Layers |
| computational unit | Computational Unit | Same normalized label; repeated source occurrence consolidated | 02 / Neural Networks |
| computational units | Computational Unit | Synonym or expanded/short form merged into one concept | 02 / Neural Networks |
| Compute | Compute | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 03 / Foundation Models |
| compute | Compute | Same normalized label; repeated source occurrence consolidated | 03 / Parameters; 04 / Pre Training; 04 / Prompting Vs Rag Vs Fine Tuning; 05 / Inference; 05 / KV Cache; 07 / Image Generation; 08 / Grounding; 10 / GPU, VRAM & Unified Memory; 10 / Local AI vs Cloud AI; 10 / Model Serving; 10 / Quantization; 10 / Runtime Constraints; 13 / Open vs Closed / Local Models |
| computer use | Computer Use | Same normalized label; repeated source occurrence consolidated | 14 / AI Assistants & Coding Tools; 14 / General Agents & Computer Use |
| Computer Use | Computer Use | Same normalized label; repeated source occurrence consolidated | 14 / General Agents & Computer Use |
| Concept Drift | Concept Drift | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning |
| Concept drift | Concept Drift | Same normalized label; repeated source occurrence consolidated | 01 / Machine Learning; 03 / Foundation Models |
| concept drift | Concept Drift | Same normalized label; repeated source occurrence consolidated | 01 / Supervised Learning; 04 / Training Data; 12 / Deployment |
| conditional generation | Conditional Generation | Same normalized label; repeated source occurrence consolidated | 07 / Image Generation |
| Confusion Matrix | Confusion Matrix | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning |
| Confusion matrix | Confusion Matrix | Same normalized label; repeated source occurrence consolidated | 01 / Machine Learning |
| confusion matrix | Confusion Matrix | Same normalized label; repeated source occurrence consolidated | 01 / Supervised Learning; 04 / Training Data |
| connector | Connector | Same normalized label; repeated source occurrence consolidated | 14 / General Agents & Computer Use |
| CDN | Content Delivery Network (CDN) | Important abbreviation merged into the canonical expanded concept | 17 / Deployment & Operations; 18 / Web & Cloud Platforms |
| Content Delivery Network | Content Delivery Network (CDN) | Case, hyphen, spacing, or capitalization variant merged | 17 / Deployment & Operations |
| content delivery network | Content Delivery Network (CDN) | Synonym or expanded/short form merged into one concept | 18 / Web & Cloud Platforms |
| content filter | Content Filter | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models; 12 / Deployment |
| content moderation | Content Moderation | Same normalized label; repeated source occurrence consolidated | 09 / Human in the Loop |
| Moderation | Content Moderation | Case, hyphen, spacing, or capitalization variant merged | 03 / Foundation Models |
| moderation | Content Moderation | Synonym or expanded/short form merged into one concept | 03 / Large Language Models; 12 / Deployment |
| Context assembly | Context Assembly | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| context assembly | Context Assembly | Same normalized label; repeated source occurrence consolidated | 04 / Prompting Vs Rag Vs Fine Tuning; 06 / Context Engineering; 08 / Grounding; 08 / Rag; 10 / Latency |
| context building | Context Assembly | Synonym or expanded/short form merged into one concept | 08 / Rag |
| Context budget | Context Budget | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models; 05 / Context Window |
| context budget | Context Budget | Same normalized label; repeated source occurrence consolidated | 08 / Grounding; 08 / Rag |
| token budget | Context Budget | Synonym or expanded/short form merged into one concept | 02 / Attention; 05 / Inference; 05 / Token; 05 / Tokenization; 08 / Grounding; 08 / Rag; 10 / Runtime Constraints |
| Token budget | Context Budget | Case, hyphen, spacing, or capitalization variant merged | 03 / Foundation Models; 05 / Context Window |
| context engineering | Context Engineering | Same normalized label; repeated source occurrence consolidated | 06 / Context Engineering; 06 / Prompt Design |
| Context Engineering | Context Engineering | Same normalized label; repeated source occurrence consolidated | 06 / Prompt Design |
| Context grounding | Context Grounding | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| Context length | Context Length | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models; 05 / Context Window |
| context length | Context Length | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models; 05 / Token; 05 / Tokenization; 10 / GPU, VRAM & Unified Memory; 13 / Open vs Closed / Local Models |
| Context overflow | Context Overflow | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models; 05 / Context Window |
| Context retrieval | Context Retrieval | Same normalized label; repeated source occurrence consolidated | 05 / Context Window |
| Context Window | Context Window | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 05 / Context Window; 05 / Token; 07 / Text Generation; 08 / Rag; 09 / Memory State; 10 / Ollama; 10 / Tokens per Second |
| context window | Context Window | Same normalized label; repeated source occurrence consolidated | 02 / Attention; 02 / Transformer; 03 / Large Language Models; 03 / Multimodal Models; 04 / Pre Training; 04 / Prompting Vs Rag Vs Fine Tuning; 05 / Inference; 05 / KV Cache; 05 / Next Token Prediction; 05 / Sampling Temperature; 05 / Token; 05 / Tokenization; 06 / Context Engineering; 07 / Text Generation; 08 / Grounding; 08 / Rag; 09 / Memory State; 10 / GPU, VRAM & Unified Memory; 10 / Model Serving; 10 / Runtime Constraints; 10 / Tokens per Second |
| Context window | Context Window | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| continuous batching | Continuous Batching | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models |
| continuous deployment | Continuous Deployment | Same normalized label; repeated source occurrence consolidated | 12 / Deployment |
| Continuous Deployment | Continuous Deployment | Same normalized label; repeated source occurrence consolidated | 17 / Deployment & Operations |
| Continuous improvement | Continuous Improvement | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| continuous improvement | Continuous Improvement | Same normalized label; repeated source occurrence consolidated | 04 / Preference Learning Rlhf; 09 / Human in the Loop; 11 / Failure Handling; 12 / Adoption; 12 / Monitoring |
| Continuous Improvement | Continuous Improvement | Same normalized label; repeated source occurrence consolidated | 12 / Continuous Improvement |
| Convolution | Convolution | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning |
| Convolution filter | Convolution Kernel | Case, hyphen, spacing, or capitalization variant merged | 02 / CNN |
| Convolution filters | Convolution Kernel | Case, hyphen, spacing, or capitalization variant merged | 02 / CNN |
| Kernel | Convolution Kernel | Important abbreviation merged into the canonical expanded concept | 01 / Deep Learning |
| CNN | Convolutional Neural Network (CNN) | Important abbreviation merged into the canonical expanded concept | 01 / Deep Learning; 02 / CNN; 02 / Layers; 02 / Neural Networks; 07 / Image Generation |
| Convolutional Neural Network | Convolutional Neural Network (CNN) | Case, hyphen, spacing, or capitalization variant merged | 01 / Deep Learning; 02 / CNN; 02 / Layers |
| Convolutional neural network | Convolutional Neural Network (CNN) | Case, hyphen, spacing, or capitalization variant merged | 02 / CNN |
| convolutional neural network | Convolutional Neural Network (CNN) | Synonym or expanded/short form merged into one concept | 02 / Neural Networks; 07 / Image Generation |
| convolutional neural network (CNN) | Convolutional Neural Network (CNN) | Same normalized label; repeated source occurrence consolidated | 03 / Vision Foundation Models |
| cost per token | Cost per Token | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models |
| CPU | CPU | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models; 10 / GPU, VRAM & Unified Memory; 10 / Model Serving; 10 / Quantization |
| cross-attention | Cross-Attention | Same normalized label; repeated source occurrence consolidated | 02 / Attention; 03 / Multimodal Models |
| cross-encoder | Cross-Encoder | Same normalized label; repeated source occurrence consolidated | 08 / Embeddings; 08 / Reranking; 08 / Vector Search |
| cross-entropy loss | Cross-Entropy Loss | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models; 04 / Pre Training |
| Data Augmentation | Data Augmentation | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning |
| Data augmentation | Data Augmentation | Same normalized label; repeated source occurrence consolidated | 01 / Machine Learning |
| data contamination | Data Contamination | Same normalized label; repeated source occurrence consolidated | 04 / Pre Training |
| Data curation | Data Curation | Same normalized label; repeated source occurrence consolidated | 01 / Machine Learning; 03 / Foundation Models |
| data curation | Data Curation | Same normalized label; repeated source occurrence consolidated | 04 / Training Data |
| Data Drift | Data Drift | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning |
| Data drift | Data Drift | Same normalized label; repeated source occurrence consolidated | 01 / Machine Learning; 03 / Foundation Models |
| data drift | Data Drift | Same normalized label; repeated source occurrence consolidated | 01 / Supervised Learning; 01 / Unsupervised Learning; 04 / Training Data; 08 / Vector Search; 12 / Deployment |
| data filtering | Data Filtering | Same normalized label; repeated source occurrence consolidated | 04 / Pre Training |
| Data Leakage | Data Leakage | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning |
| Data leakage | Data Leakage | Same normalized label; repeated source occurrence consolidated | 01 / Machine Learning; 03 / Foundation Models |
| data leakage | Data Leakage | Same normalized label; repeated source occurrence consolidated | 01 / Supervised Learning; 02 / Attention; 03 / Large Language Models; 04 / Pre Training; 04 / Training Data; 08 / Grounding |
| data pipeline | Data Pipeline | Same normalized label; repeated source occurrence consolidated | 19 / Backend Technologies |
| Data preprocessing | Data Preprocessing | Same normalized label; repeated source occurrence consolidated | 01 / Machine Learning |
| data preprocessing | Data Preprocessing | Same normalized label; repeated source occurrence consolidated | 01 / Unsupervised Learning |
| Preprocessing | Data Preprocessing | Case, hyphen, spacing, or capitalization variant merged | 01 / Deep Learning |
| preprocessing | Data Preprocessing | Synonym or expanded/short form merged into one concept | 04 / Training Data; 05 / Inference; 05 / Tokenization |
| Data provenance | Data Provenance | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| data provenance | Data Provenance | Same normalized label; repeated source occurrence consolidated | 11 / Hallucination |
| Data quality | Data Quality | Same normalized label; repeated source occurrence consolidated | 01 / Machine Learning |
| data quality | Data Quality | Same normalized label; repeated source occurrence consolidated | 01 / Unsupervised Learning; 03 / Parameters; 04 / Pre Training; 04 / Preference Learning Rlhf; 04 / Training Data; 05 / Inference; 06 / Structured Outputs; 12 / Workflow Discovery |
| database | Database | Same normalized label; repeated source occurrence consolidated | 01 / Artificial Intelligence; 03 / Large Language Models; 03 / Parameters; 03 / Scientific Models; 06 / Structured Outputs; 08 / Embeddings; 08 / Grounding; 08 / Rag; 08 / Retrieval; 08 / Vector Database; 09 / Model Context Protocol (MCP); 15 / How AI Agents Are Built; 16 / AI Workflow Platforms; 17 / Data, APIs & Authentication; 17 / Frontend & Backend; 18 / Backend & Data Platforms; 18 / Web & Cloud Platforms; 19 / Data Technologies |
| Database | Database | Same normalized label; repeated source occurrence consolidated | 01 / Machine Learning; 03 / Foundation Models; 17 / Frontend & Backend |
| DATABASE | Database | Same normalized label; repeated source occurrence consolidated | 17 / Data, APIs & Authentication |
| Dataset | Dataset | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 01 / Machine Learning; 03 / Foundation Models |
| dataset | Dataset | Same normalized label; repeated source occurrence consolidated | 01 / Supervised Learning; 01 / Unsupervised Learning; 03 / Large Language Models; 03 / Vision Foundation Models; 04 / Instruction Tuning; 04 / Pre Training; 04 / Training Data |
| decode phase | Decode Phase | Same normalized label; repeated source occurrence consolidated | 05 / KV Cache |
| Decoder | Decoder | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning |
| decoder | Decoder | Same normalized label; repeated source occurrence consolidated | 03 / Multimodal Models; 05 / Sampling Temperature; 07 / Audio Generation; 07 / Image Generation |
| decoder-only model | Decoder-Only Model | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models |
| decoding | Decoding | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models; 05 / Inference; 05 / KV Cache; 05 / Next Token Prediction; 05 / Sampling Temperature; 05 / Token; 05 / Tokenization; 07 / Audio Generation; 07 / Video Generation |
| deduplication | Deduplication | Same normalized label; repeated source occurrence consolidated | 04 / Pre Training; 08 / Retrieval |
| deep learning | Deep Learning (DL) | Synonym or expanded/short form merged into one concept | 01 / Artificial Intelligence; 01 / Supervised Learning; 02 / Neural Networks; 04 / Training Data; 07 / Generative Ai |
| Deep Learning | Deep Learning (DL) | Case, hyphen, spacing, or capitalization variant merged | 01 / Deep Learning; 01 / Machine Learning; 01 / Unsupervised Learning; 02 / CNN; 02 / Diffusion Models; 02 / Layers; 02 / Neural Networks; 02 / RNN / LSTM; 07 / Audio Generation; 07 / Generative Ai |
| Deep learning | Deep Learning (DL) | Case, hyphen, spacing, or capitalization variant merged | 02 / CNN |
| DL | Deep Learning (DL) | Important abbreviation merged into the canonical expanded concept | 01 / Artificial Intelligence; 01 / Deep Learning; 01 / Machine Learning |
| Deep Neural Network | Deep Neural Network (DNN) | Case, hyphen, spacing, or capitalization variant merged | 01 / Deep Learning |
| deep neural network | Deep Neural Network (DNN) | Synonym or expanded/short form merged into one concept | 02 / Neural Networks; 07 / Image Generation |
| DNN | Deep Neural Network (DNN) | Important abbreviation merged into the canonical expanded concept | 01 / Deep Learning |
| DeepSeek | DeepSeek | Same normalized label; repeated source occurrence consolidated | 10 / Ollama; 13 / Major AI Providers; 13 / Model Types & Families |
| Denoising | Denoising | Same normalized label; repeated source occurrence consolidated | 02 / Diffusion Models |
| denoising | Denoising | Same normalized label; repeated source occurrence consolidated | 07 / Image Generation |
| Denoising Process | Denoising | Case, hyphen, spacing, or capitalization variant merged | 02 / Diffusion Models |
| denoising process | Denoising | Synonym or expanded/short form merged into one concept | 07 / Image Generation |
| deploy preview | Deploy Preview | Same normalized label; repeated source occurrence consolidated | 18 / Web & Cloud Platforms |
| Deployment | Deployment | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 01 / Machine Learning; 11 / Deployment Readiness; 12 / Deployment |
| deployment | Deployment | Same normalized label; repeated source occurrence consolidated | 01 / Supervised Learning; 01 / Unsupervised Learning; 02 / Attention; 03 / Large Language Models; 04 / Pre Training; 04 / Training Data; 05 / Inference; 07 / Image Generation; 09 / Human in the Loop; 10 / Model Serving; 10 / Quantization; 10 / Runtime Constraints; 11 / Benchmarks; 11 / Deployment Readiness; 11 / Hallucination; 12 / Adoption; 12 / Continuous Improvement; 12 / Technical Scoping; 13 / Major AI Providers; 14 / General Agents & Computer Use; 17 / Deployment & Operations; 18 / Web & Cloud Platforms; 19 / Backend Technologies |
| Deployment readiness | Deployment Readiness | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models; 11 / Deployment Readiness |
| deployment readiness | Deployment Readiness | Same normalized label; repeated source occurrence consolidated | 11 / Benchmarks; 11 / Deployment Readiness; 11 / Failure Modes; 11 / Functional Tests; 11 / Guardrails; 11 / Permissions Safety; 12 / Adoption; 12 / Deployment |
| Deployment Readiness | Deployment Readiness | Same normalized label; repeated source occurrence consolidated | 11 / Deployment Readiness; 11 / Evaluation; 11 / Failure Modes; 11 / Functional Tests; 11 / Guardrails; 11 / Permissions Safety |
| deployment-readiness | Deployment Readiness | Same normalized label; repeated source occurrence consolidated | 11 / Deployment Readiness |
| developer platform | Developer Platform | Same normalized label; repeated source occurrence consolidated | 18 / Developer Platforms |
| DEVELOPER PLATFORM | Developer Platform | Same normalized label; repeated source occurrence consolidated | 18 / Developer Platforms |
| Diffusion Model | Diffusion Model | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 02 / Diffusion Models; 07 / Image Generation |
| diffusion model | Diffusion Model | Same normalized label; repeated source occurrence consolidated | 07 / Image Generation |
| Dimensionality reduction | Dimensionality Reduction | Same normalized label; repeated source occurrence consolidated | 01 / Machine Learning |
| dimensionality reduction | Dimensionality Reduction | Same normalized label; repeated source occurrence consolidated | 01 / Unsupervised Learning |
| Corpus | Document Corpus | Important abbreviation merged into the canonical expanded concept | 03 / Foundation Models |
| corpus | Document Corpus | Important abbreviation merged into the canonical expanded concept | 03 / Large Language Models; 04 / Pre Training; 08 / Embeddings; 08 / Rag; 08 / Reranking; 08 / Retrieval; 08 / Semantic Search; 08 / Vector Search |
| source collection | Document Corpus | Synonym or expanded/short form merged into one concept | 08 / Rag; 08 / Retrieval |
| document database | Document Database | Same normalized label; repeated source occurrence consolidated | 18 / Backend & Data Platforms; 19 / Data Technologies |
| dynamic batching | Dynamic Batching | Same normalized label; repeated source occurrence consolidated | 10 / Model Serving |
| edge compute | Edge Compute | Same normalized label; repeated source occurrence consolidated | 18 / Web & Cloud Platforms |
| Edge Detection | Edge Detection | Same normalized label; repeated source occurrence consolidated | 02 / Layers |
| edge function | Edge Function | Same normalized label; repeated source occurrence consolidated | 18 / Backend & Data Platforms |
| Edge Functions | Edge Function | Case, hyphen, spacing, or capitalization variant merged | 18 / Backend & Data Platforms |
| edge network | Edge Network | Same normalized label; repeated source occurrence consolidated | 18 / Web & Cloud Platforms |
| Embedding | Embedding | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 03 / Foundation Models; 08 / Vector Search; 13 / Model Types & Families |
| embedding | Embedding | Same normalized label; repeated source occurrence consolidated | 01 / Unsupervised Learning; 03 / Large Language Models; 03 / Multimodal Models; 03 / Vision Foundation Models; 04 / Pre Training; 08 / Chunking; 08 / Embeddings; 08 / Grounding; 08 / Rag; 08 / Reranking; 08 / Retrieval; 08 / Semantic Search; 08 / Vector Database; 08 / Vector Search |
| embeddings | Embedding | Synonym or expanded/short form merged into one concept | 08 / Chunking; 08 / Embeddings; 08 / Rag; 08 / Semantic Search; 08 / Vector Database; 08 / Vector Search; 13 / Model Types & Families |
| Embeddings | Embedding | Case, hyphen, spacing, or capitalization variant merged | 08 / Rag; 08 / Retrieval; 08 / Semantic Search |
| embedding model | Embedding Model | Same normalized label; repeated source occurrence consolidated | 08 / Embeddings; 08 / Rag; 08 / Retrieval; 08 / Semantic Search; 08 / Vector Database; 08 / Vector Search; 13 / Model Types & Families |
| Encoder | Encoder | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning |
| encoder | Encoder | Same normalized label; repeated source occurrence consolidated | 03 / Multimodal Models; 07 / Audio Generation; 07 / Image Generation |
| encoder-decoder model | Encoder-Decoder Model | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models |
| encoder-only model | Encoder-Only Model | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models |
| end-of-sequence token | End-of-Sequence Token (EOS) | Case, hyphen, spacing, or capitalization variant merged | 03 / Large Language Models; 05 / Tokenization |
| Epoch | Epoch | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 01 / Machine Learning |
| epoch | Epoch | Same normalized label; repeated source occurrence consolidated | 01 / Supervised Learning; 03 / Large Language Models; 03 / Parameters; 04 / Pre Training; 04 / Training Data |
| Error handling | Error Handling | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| error handling | Error Handling | Same normalized label; repeated source occurrence consolidated | 05 / Inference; 06 / Structured Outputs; 10 / Model Serving |
| error rate | Error Rate | Same normalized label; repeated source occurrence consolidated | 05 / Inference; 11 / Failure Handling |
| evaluation | Evaluation | Same normalized label; repeated source occurrence consolidated | 01 / Artificial Intelligence; 01 / Supervised Learning; 01 / Unsupervised Learning; 03 / Large Language Models; 03 / Multimodal Models; 03 / Scientific Models; 04 / Fine Tuning; 04 / Prompting Vs Rag Vs Fine Tuning; 04 / Training Data; 05 / Inference; 05 / Sampling Temperature; 07 / Image Generation; 07 / Text Generation; 08 / Grounding; 08 / Semantic Search; 09 / Multi-Agent Systems; 11 / Benchmarks; 11 / Deployment Readiness; 11 / Evaluation; 11 / Failure Modes; 11 / Functional Tests; 11 / Guardrails; 11 / Hallucination; 11 / Permissions Safety; 11 / Prompt Injection; 12 / Adoption; 12 / Deployment; 12 / Integration; 12 / Monitoring; 12 / Technical Scoping |
| Evaluation | Evaluation | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 01 / Machine Learning; 03 / Foundation Models; 04 / Fine Tuning; 11 / Deployment Readiness; 11 / Evaluation; 11 / Functional Tests; 11 / Guardrails; 12 / Continuous Improvement; 12 / Integration; 12 / Monitoring; 12 / Technical Scoping; 12 / Workflow Discovery |
| model evaluation | Evaluation | Synonym or expanded/short form merged into one concept | 01 / Supervised Learning; 04 / Preference Learning Rlhf; 04 / Training Data; 11 / Benchmarks |
| Model evaluation | Evaluation | Case, hyphen, spacing, or capitalization variant merged | 03 / Foundation Models |
| Evaluation Metric | Evaluation Metric | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning |
| Evaluation metric | Evaluation Metric | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| evaluation metric | Evaluation Metric | Same normalized label; repeated source occurrence consolidated | 04 / Instruction Tuning; 04 / Pre Training |
| Explainability | Explainability | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 01 / Machine Learning; 03 / Foundation Models |
| explainability | Explainability | Same normalized label; repeated source occurrence consolidated | 01 / Supervised Learning; 04 / Training Data; 05 / Inference; 08 / Grounding; 09 / Human in the Loop; 12 / Adoption |
| Express | Express | Same normalized label; repeated source occurrence consolidated | 19 / Backend Technologies |
| F1 Score | F1 Score | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning |
| F1 score | F1 Score | Same normalized label; repeated source occurrence consolidated | 01 / Machine Learning; 01 / Supervised Learning; 03 / Foundation Models; 03 / Multimodal Models; 04 / Training Data; 05 / Inference; 11 / Hallucination |
| fabricated content | Fabricated Content | Same normalized label; repeated source occurrence consolidated | 11 / Hallucination |
| factuality | Factuality | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models; 08 / Grounding; 11 / Hallucination |
| failure handling | Failure Handling | Same normalized label; repeated source occurrence consolidated | 06 / Structured Outputs; 09 / Agent Loop; 11 / Benchmarks; 11 / Deployment Readiness; 11 / Failure Handling; 11 / Failure Modes; 11 / Functional Tests; 11 / Guardrails; 11 / Permissions Safety; 11 / Prompt Injection; 12 / Deployment |
| Failure Handling | Failure Handling | Same normalized label; repeated source occurrence consolidated | 06 / Structured Outputs; 09 / Tool Calling; 11 / Deployment Readiness; 11 / Failure Handling; 11 / Failure Modes; 11 / Functional Tests; 11 / Guardrails; 11 / Permissions Safety; 12 / Continuous Improvement |
| failure mode | Failure Mode | Same normalized label; repeated source occurrence consolidated | 01 / Supervised Learning; 04 / Training Data; 07 / Image Generation; 08 / Grounding; 09 / Human in the Loop; 11 / Benchmarks; 11 / Failure Handling; 11 / Failure Modes; 11 / Hallucination |
| Failure mode | Failure Mode | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| Fairness | Fairness | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 01 / Machine Learning; 03 / Foundation Models |
| fairness | Fairness | Same normalized label; repeated source occurrence consolidated | 01 / Supervised Learning; 03 / Multimodal Models; 04 / Training Data; 05 / Inference; 09 / Human in the Loop |
| faithfulness | Faithfulness | Same normalized label; repeated source occurrence consolidated | 02 / Attention; 08 / Rag; 11 / Hallucination |
| Faithfulness | Faithfulness | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| Fallback | Fallback | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| fallback | Fallback | Same normalized label; repeated source occurrence consolidated | 05 / Inference; 06 / Structured Outputs; 08 / Grounding; 09 / Human in the Loop; 10 / Runtime Constraints; 11 / Deployment Readiness; 11 / Failure Handling; 11 / Failure Modes; 12 / Deployment; 12 / Technical Scoping |
| FastAPI | FastAPI | Same normalized label; repeated source occurrence consolidated | 17 / Frontend & Backend; 19 / Backend Technologies |
| Feature | Feature | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 01 / Machine Learning; 02 / CNN |
| feature | Feature | Same normalized label; repeated source occurrence consolidated | 01 / Supervised Learning; 01 / Unsupervised Learning; 02 / Neural Networks; 03 / Vision Foundation Models; 04 / Pre Training; 07 / Image Generation; 08 / Embeddings |
| Feature Representation | Feature Representation | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning |
| feature representation | Feature Representation | Same normalized label; repeated source occurrence consolidated | 07 / Image Generation; 08 / Vector Search |
| Feature vector | Feature Vector | Same normalized label; repeated source occurrence consolidated | 01 / Machine Learning |
| feature vector | Feature Vector | Same normalized label; repeated source occurrence consolidated | 01 / Supervised Learning |
| feed-forward network | Feed-Forward Network | Same normalized label; repeated source occurrence consolidated | 02 / Attention; 03 / Large Language Models |
| Feed-Forward Network | Feed-Forward Network | Same normalized label; repeated source occurrence consolidated | 02 / Layers |
| file storage | File Storage | Same normalized label; repeated source occurrence consolidated | 17 / Data, APIs & Authentication; 18 / Backend & Data Platforms |
| fine-tuning | Fine-Tuning | Same normalized label; repeated source occurrence consolidated | 01 / Artificial Intelligence; 03 / Large Language Models; 03 / Multimodal Models; 03 / Parameters; 03 / Vision Foundation Models; 04 / Fine Tuning; 04 / Instruction Tuning; 04 / Pre Training; 04 / Preference Learning Rlhf; 04 / Prompting Vs Rag Vs Fine Tuning; 04 / Training Data; 08 / Grounding; 08 / Rag; 10 / Quantization; 12 / Continuous Improvement |
| Fine-tuning | Fine-Tuning | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 01 / Machine Learning; 03 / Foundation Models; 04 / Fine Tuning; 04 / Preference Learning Rlhf |
| foundation model | Foundation Model | Same normalized label; repeated source occurrence consolidated | 01 / Artificial Intelligence; 03 / Large Language Models; 03 / Multimodal Models; 03 / Scientific Models; 03 / Speech Audio Models; 03 / Vision Foundation Models; 04 / Fine Tuning; 04 / Instruction Tuning; 04 / Pre Training; 04 / Prompting Vs Rag Vs Fine Tuning; 04 / Training Data; 07 / Code Generation; 07 / Multimodal Ai; 13 / Model Types & Families |
| Foundation Model | Foundation Model | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 01 / Machine Learning; 03 / Foundation Models; 04 / Instruction Tuning; 13 / Model Types & Families |
| Frontend | Frontend | Same normalized label; repeated source occurrence consolidated | 17 / Frontend & Backend |
| frontend | Frontend | Same normalized label; repeated source occurrence consolidated | 17 / Frontend & Backend; 18 / Web & Cloud Platforms; 19 / Backend Technologies; 19 / Frontend Technologies |
| Function calling | Function Calling | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| function calling | Function Calling | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models |
| functional test | Functional Test | Same normalized label; repeated source occurrence consolidated | 09 / Agent Loop; 11 / Benchmarks; 11 / Deployment Readiness; 11 / Evaluation; 11 / Functional Tests |
| Functional Test | Functional Test | Same normalized label; repeated source occurrence consolidated | 11 / Evaluation |
| functional-test | Functional Test | Same normalized label; repeated source occurrence consolidated | 11 / Functional Tests |
| Gemini | Gemini | Same normalized label; repeated source occurrence consolidated | 13 / Major AI Providers; 13 / Model Types & Families; 14 / AI Assistants & Coding Tools; 15 / Agent Frameworks |
| Generalization | Generalization | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 01 / Machine Learning; 02 / Layers; 03 / Foundation Models |
| generalization | Generalization | Same normalized label; repeated source occurrence consolidated | 01 / Supervised Learning; 03 / Large Language Models; 03 / Parameters; 03 / Scientific Models; 04 / Instruction Tuning; 04 / Pre Training; 04 / Training Data; 05 / Inference |
| GAN | Generative Adversarial Network (GAN) | Important abbreviation merged into the canonical expanded concept | 01 / Deep Learning; 02 / Diffusion Models; 07 / Image Generation |
| Generative Adversarial Network | Generative Adversarial Network (GAN) | Case, hyphen, spacing, or capitalization variant merged | 01 / Deep Learning; 02 / Diffusion Models |
| generative adversarial network | Generative Adversarial Network (GAN) | Synonym or expanded/short form merged into one concept | 07 / Image Generation |
| generative AI | Generative AI | Same normalized label; repeated source occurrence consolidated | 01 / Artificial Intelligence; 03 / Large Language Models; 03 / Multimodal Models; 07 / Audio Generation; 07 / Generative Ai; 07 / Image Generation; 07 / Multimodal Ai; 07 / Text Generation |
| Generative AI | Generative AI | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 01 / Machine Learning; 02 / Diffusion Models; 03 / Foundation Models; 03 / Multimodal Models; 07 / Code Generation; 07 / Generative Ai; 07 / Image Generation; 07 / Multimodal Ai; 07 / Text Generation |
| generative model | Generative Model | Same normalized label; repeated source occurrence consolidated | 01 / Artificial Intelligence; 03 / Large Language Models; 04 / Prompting Vs Rag Vs Fine Tuning; 07 / Audio Generation; 07 / Generative Ai; 07 / Image Generation; 08 / Semantic Search |
| Generative Model | Generative Model | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 02 / Diffusion Models; 07 / Image Generation |
| Generative model | Generative Model | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| GPT | GPT | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models; 13 / Major AI Providers; 13 / Model Types & Families; 14 / AI Assistants & Coding Tools; 15 / Agent Frameworks |
| GPU | GPU | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 03 / Large Language Models; 04 / Pre Training; 07 / Image Generation; 10 / GPU, VRAM & Unified Memory; 10 / Model Serving; 10 / Quantization; 10 / Vllm |
| Gradient | Gradient | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning |
| gradient | Gradient | Same normalized label; repeated source occurrence consolidated | 01 / Supervised Learning; 02 / Attention; 03 / Large Language Models; 03 / Parameters; 04 / Pre Training; 04 / Training Data |
| Gradient Descent | Gradient Descent | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning |
| Gradient descent | Gradient Descent | Same normalized label; repeated source occurrence consolidated | 01 / Machine Learning |
| gradient descent | Gradient Descent | Same normalized label; repeated source occurrence consolidated | 01 / Supervised Learning; 03 / Large Language Models; 03 / Parameters; 04 / Pre Training; 04 / Training Data |
| greedy decoding | Greedy Decoding | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models; 05 / Inference; 05 / Token |
| Groundedness | Groundedness | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| groundedness | Groundedness | Same normalized label; repeated source occurrence consolidated | 08 / Rag; 11 / Hallucination |
| Grounding | Grounding | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models; 08 / Grounding; 08 / Rag; 11 / Evaluation |
| grounding | Grounding | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models; 03 / Multimodal Models; 04 / Prompting Vs Rag Vs Fine Tuning; 07 / Text Generation; 08 / Grounding; 08 / Rag; 08 / Retrieval; 08 / Vector Search; 11 / Deployment Readiness; 11 / Hallucination |
| GROUNDING | Grounding | Same normalized label; repeated source occurrence consolidated | 11 / Hallucination |
| Guardrail | Guardrail | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| guardrail | Guardrail | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models; 03 / Multimodal Models; 07 / Image Generation; 08 / Grounding; 09 / Agent Loop; 09 / Human in the Loop; 11 / Failure Handling; 11 / Failure Modes; 11 / Guardrails; 11 / Hallucination; 11 / Permissions Safety; 12 / Adoption; 12 / Deployment |
| Hallucination | Hallucination | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models; 11 / Hallucination |
| hallucination | Hallucination | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models; 03 / Multimodal Models; 05 / Inference; 07 / Image Generation; 08 / Grounding; 08 / Rag; 08 / Retrieval; 08 / Vector Search; 11 / Failure Modes; 11 / Prompt Injection |
| HALLUCINATION | Hallucination | Same normalized label; repeated source occurrence consolidated | 11 / Hallucination |
| Hidden Layer | Hidden Layer | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 02 / Layers |
| hidden layer | Hidden Layer | Same normalized label; repeated source occurrence consolidated | 02 / Neural Networks |
| Hidden Layers | Hidden Layer | Case, hyphen, spacing, or capitalization variant merged | 02 / Layers; 02 / Neural Networks |
| hidden layers | Hidden Layer | Synonym or expanded/short form merged into one concept | 02 / Neural Networks |
| hidden state | Hidden State | Same normalized label; repeated source occurrence consolidated | 02 / RNN / LSTM; 03 / Large Language Models; 05 / KV Cache |
| HTTP | HTTP | Same normalized label; repeated source occurrence consolidated | 10 / Model Serving; 19 / Backend Technologies |
| Human evaluation | Human Evaluation | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| human evaluation | Human Evaluation | Same normalized label; repeated source occurrence consolidated | 09 / Human in the Loop |
| Human feedback | Human Feedback | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| Human Feedback | Human Feedback | Same normalized label; repeated source occurrence consolidated | 04 / Preference Learning Rlhf |
| human feedback | Human Feedback | Same normalized label; repeated source occurrence consolidated | 04 / Preference Learning Rlhf; 04 / Training Data; 09 / Human in the Loop |
| human oversight | Human Oversight | Same normalized label; repeated source occurrence consolidated | 03 / Multimodal Models; 04 / Preference Learning Rlhf; 04 / Training Data; 05 / Inference; 08 / Grounding; 09 / AI Agent; 09 / Human in the Loop; 09 / Planning; 11 / Permissions Safety; 12 / Adoption; 12 / Workflow Discovery; 14 / General Agents & Computer Use |
| human review | Human Review | Same normalized label; repeated source occurrence consolidated | 01 / Artificial Intelligence; 01 / Supervised Learning; 01 / Unsupervised Learning; 03 / Large Language Models; 03 / Multimodal Models; 04 / Training Data; 05 / Inference; 06 / System Prompts; 07 / Code Generation; 07 / Image Generation; 09 / AI Agent; 09 / Human in the Loop; 09 / Planning; 11 / Deployment Readiness; 11 / Evaluation; 11 / Failure Handling; 11 / Failure Modes; 11 / Hallucination; 12 / Adoption; 12 / Deployment; 12 / Integration; 12 / Workflow Discovery; 15 / How AI Agents Are Built |
| Human Review | Human Review | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning |
| Human review | Human Review | Same normalized label; repeated source occurrence consolidated | 01 / Machine Learning; 03 / Foundation Models |
| HUMAN REVIEW | Human Review | Same normalized label; repeated source occurrence consolidated | 11 / Hallucination |
| HITL | Human-in-the-Loop (HITL) | Important abbreviation merged into the canonical expanded concept | 05 / Inference; 08 / Grounding; 09 / Human in the Loop |
| Human in the Loop | Human-in-the-Loop (HITL) | Case, hyphen, spacing, or capitalization variant merged | 09 / Human in the Loop; 09 / Multi-Agent Systems; 11 / Guardrails; 11 / Permissions Safety |
| human in the loop | Human-in-the-Loop (HITL) | Synonym or expanded/short form merged into one concept | 09 / Skills / Plugins; 11 / Guardrails; 11 / Permissions Safety; 11 / Prompt Injection |
| human-in-the-loop | Human-in-the-Loop (HITL) | Case, hyphen, spacing, or capitalization variant merged | 01 / Artificial Intelligence; 03 / Multimodal Models; 04 / Preference Learning Rlhf; 04 / Training Data; 05 / Inference; 08 / Grounding; 09 / AI Agent; 09 / Agent Loop; 09 / Human in the Loop; 09 / Planning; 11 / Failure Handling; 11 / Failure Modes; 11 / Permissions Safety; 12 / Adoption; 12 / Deployment; 12 / Integration; 12 / Workflow Discovery; 14 / AI Assistants & Coding Tools |
| Human-in-the-loop | Human-in-the-Loop (HITL) | Case, hyphen, spacing, or capitalization variant merged | 01 / Deep Learning; 01 / Machine Learning; 03 / Foundation Models; 11 / Guardrails |
| hybrid search | Hybrid Search | Same normalized label; repeated source occurrence consolidated | 08 / Reranking; 08 / Retrieval; 08 / Vector Search |
| Hyperparameter | Hyperparameter | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 01 / Machine Learning |
| hyperparameter | Hyperparameter | Same normalized label; repeated source occurrence consolidated | 01 / Supervised Learning; 04 / Training Data |
| image captioning | Image Captioning | Same normalized label; repeated source occurrence consolidated | 03 / Multimodal Models; 03 / Vision Foundation Models |
| Image classification | Image Classification | Same normalized label; repeated source occurrence consolidated | 02 / CNN |
| Image Classification | Image Classification | Same normalized label; repeated source occurrence consolidated | 02 / Neural Networks |
| image classification | Image Classification | Same normalized label; repeated source occurrence consolidated | 02 / Neural Networks; 03 / Multimodal Models; 03 / Vision Foundation Models; 05 / Inference |
| Image Generation | Image Generation | Same normalized label; repeated source occurrence consolidated | 02 / Diffusion Models; 07 / Image Generation |
| Image generation | Image Generation | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models; 13 / Model Types & Families |
| image generation | Image Generation | Same normalized label; repeated source occurrence consolidated | 03 / Vision Foundation Models; 07 / Generative Ai; 07 / Image Generation; 07 / Multimodal Ai; 07 / Video Generation |
| Image Generator | Image Generator | Same normalized label; repeated source occurrence consolidated | 02 / CNN |
| Image generator | Image Generator | Same normalized label; repeated source occurrence consolidated | 02 / CNN |
| image generator | Image Generator | Same normalized label; repeated source occurrence consolidated | 03 / Vision Foundation Models |
| image-text alignment | Image-Text Alignment | Same normalized label; repeated source occurrence consolidated | 03 / Multimodal Models; 03 / Vision Foundation Models; 07 / Image Generation |
| image-text contrastive learning | Image-Text Contrastive Learning | Same normalized label; repeated source occurrence consolidated | 03 / Multimodal Models |
| Image-to-Image | Image-to-Image Generation | Case, hyphen, spacing, or capitalization variant merged | 02 / Diffusion Models |
| image-to-image | Image-to-Image Generation | Case, hyphen, spacing, or capitalization variant merged | 03 / Multimodal Models; 07 / Image Generation; 13 / Model Types & Families |
| image-to-text | Image-to-Text | Same normalized label; repeated source occurrence consolidated | 03 / Multimodal Models |
| In-context learning | In-Context Learning | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| inference | Inference | Same normalized label; repeated source occurrence consolidated | 01 / Artificial Intelligence; 01 / Supervised Learning; 01 / Unsupervised Learning; 02 / Attention; 02 / Transformer; 03 / Large Language Models; 03 / Multimodal Models; 03 / Parameters; 03 / Vision Foundation Models; 04 / Pre Training; 04 / Prompting Vs Rag Vs Fine Tuning; 04 / Training Data; 05 / Inference; 05 / KV Cache; 05 / Next Token Prediction; 05 / Sampling Temperature; 05 / Token; 05 / Tokenization; 06 / System Prompts; 07 / Image Generation; 07 / Text Generation; 10 / Api; 10 / GPU, VRAM & Unified Memory; 10 / Local AI vs Cloud AI; 10 / Model Serving; 10 / Ollama; 10 / Quantization; 10 / Runtime Constraints; 10 / Tokens per Second; 10 / Vllm; 13 / Open vs Closed / Local Models |
| Inference | Inference | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 01 / Machine Learning; 02 / CNN; 03 / Foundation Models; 05 / Context Window; 07 / Text Generation; 10 / Ollama; 10 / Tokens per Second |
| inference optimization | Inference Optimization | Same normalized label; repeated source occurrence consolidated | 02 / Transformer; 05 / Inference |
| Inference Pipeline | Inference Pipeline | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning |
| inference pipeline | Inference Pipeline | Same normalized label; repeated source occurrence consolidated | 05 / Inference; 05 / KV Cache; 10 / Vllm |
| Inference request | Inference Request | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| inference request | Inference Request | Same normalized label; repeated source occurrence consolidated | 05 / Inference; 05 / KV Cache; 10 / Model Serving; 10 / Runtime Constraints; 13 / Open vs Closed / Local Models |
| inference server | Inference Server | Same normalized label; repeated source occurrence consolidated | 10 / Vllm |
| inpainting | Inpainting | Same normalized label; repeated source occurrence consolidated | 07 / Image Generation |
| input modality | Input Modality | Same normalized label; repeated source occurrence consolidated | 03 / Multimodal Models; 05 / Inference; 07 / Multimodal Ai; 13 / Model Types & Families |
| input token | Input Token | Same normalized label; repeated source occurrence consolidated | 02 / Transformer; 05 / Token |
| Instruction hierarchy | Instruction Hierarchy | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| instruction hierarchy | Instruction Hierarchy | Same normalized label; repeated source occurrence consolidated | 04 / Prompting Vs Rag Vs Fine Tuning; 06 / System Prompts; 08 / Grounding; 11 / Prompt Injection |
| Instruction tuning | Instruction Tuning | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| instruction tuning | Instruction Tuning | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models; 03 / Multimodal Models; 04 / Instruction Tuning; 04 / Pre Training; 04 / Training Data |
| Instruction Tuning | Instruction Tuning | Same normalized label; repeated source occurrence consolidated | 04 / Instruction Tuning |
| integration | Integration | Same normalized label; repeated source occurrence consolidated | 09 / Human in the Loop; 09 / Model Context Protocol (MCP); 12 / Adoption; 12 / Continuous Improvement; 12 / Deployment; 12 / Technical Scoping; 13 / Major AI Providers; 15 / How AI Agents Are Built; 17 / Frontend & Backend; 18 / Developer Platforms; 19 / Backend Technologies; 19 / Frontend Technologies; 19 / Product Services |
| Integration | Integration | Same normalized label; repeated source occurrence consolidated | 12 / Integration; 12 / Technical Scoping; 12 / Workflow Discovery |
| Jailbreak | Jailbreak | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| jailbreak | Jailbreak | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models |
| JavaScript | JavaScript | Same normalized label; repeated source occurrence consolidated | 07 / Text Generation; 17 / Frontend & Backend; 19 / Backend Technologies; 19 / Frontend Technologies |
| JSON | JSON | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models; 04 / Instruction Tuning; 06 / Structured Outputs; 07 / Text Generation; 11 / Failure Handling; 18 / Backend & Data Platforms |
| key-value (KV) cache | Key-Value Cache (KV Cache) | Case, hyphen, spacing, or capitalization variant merged | 02 / Transformer |
| key-value cache | Key-Value Cache (KV Cache) | Case, hyphen, spacing, or capitalization variant merged | 02 / Attention; 02 / Transformer; 05 / Inference; 05 / KV Cache; 05 / Next Token Prediction; 10 / GPU, VRAM & Unified Memory; 10 / Tokens per Second |
| Key-value cache | Key-Value Cache (KV Cache) | Case, hyphen, spacing, or capitalization variant merged | 05 / Context Window |
| KV cache | Key-Value Cache (KV Cache) | Case, hyphen, spacing, or capitalization variant merged | 02 / Attention; 03 / Large Language Models; 05 / Inference; 10 / GPU, VRAM & Unified Memory; 10 / Tokens per Second; 13 / Open vs Closed / Local Models |
| KV Cache | Key-Value Cache (KV Cache) | Case, hyphen, spacing, or capitalization variant merged | 02 / Transformer; 05 / Context Window; 05 / KV Cache; 05 / Next Token Prediction; 10 / Runtime Constraints; 10 / Tokens per Second |
| keyword search | Keyword Search | Same normalized label; repeated source occurrence consolidated | 08 / Grounding; 08 / Rag; 08 / Reranking; 08 / Retrieval; 08 / Semantic Search; 08 / Vector Search |
| Keyword Search | Keyword Search | Same normalized label; repeated source occurrence consolidated | 08 / Semantic Search; 08 / Vector Search |
| Knowledge base | Knowledge Base | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| knowledge base | Knowledge Base | Same normalized label; repeated source occurrence consolidated | 04 / Prompting Vs Rag Vs Fine Tuning; 08 / Grounding; 08 / Rag |
| knowledge database | Knowledge Base | Synonym or expanded/short form merged into one concept | 03 / Parameters |
| label | Label | Same normalized label; repeated source occurrence consolidated | 01 / Artificial Intelligence; 01 / Reinforcement Learning; 01 / Supervised Learning; 02 / Neural Networks; 02 / RNN / LSTM; 03 / Multimodal Models; 03 / Parameters; 03 / Vision Foundation Models; 04 / Fine Tuning; 04 / Training Data; 05 / Inference; 08 / Embeddings |
| Label | Label | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 01 / Machine Learning |
| label quality | Label Quality | Same normalized label; repeated source occurrence consolidated | 01 / Supervised Learning; 04 / Preference Learning Rlhf |
| LangGraph | LangGraph | Same normalized label; repeated source occurrence consolidated | 15 / Agent Frameworks; 16 / AI Workflow Platforms |
| language model | Language Model | Same normalized label; repeated source occurrence consolidated | 01 / Artificial Intelligence; 02 / Attention; 02 / RNN / LSTM; 02 / Transformer; 03 / Large Language Models; 03 / Multimodal Models; 03 / Parameters; 04 / Fine Tuning; 04 / Pre Training; 05 / Inference; 05 / Next Token Prediction; 05 / Sampling Temperature; 05 / Token; 05 / Tokenization; 06 / System Prompts; 07 / Text Generation; 08 / Grounding; 08 / Rag; 08 / Reranking; 10 / Ollama; 10 / Vllm; 11 / Hallucination; 13 / Model Types & Families |
| Language Model | Language Model | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 05 / Token |
| Language model | Language Model | Same normalized label; repeated source occurrence consolidated | 01 / Machine Learning; 03 / Foundation Models |
| large language model | Large Language Model (LLM) | Synonym or expanded/short form merged into one concept | 02 / Attention; 02 / Transformer; 03 / Large Language Models; 03 / Multimodal Models; 03 / Scientific Models; 03 / Speech Audio Models; 04 / Pre Training; 06 / Structured Outputs; 06 / System Prompts; 07 / Generative Ai; 07 / Text Generation; 08 / Grounding; 09 / AI Agent; 09 / Planning; 10 / Ollama; 10 / Vllm; 16 / AI Workflow Platforms |
| Large Language Model | Large Language Model (LLM) | Case, hyphen, spacing, or capitalization variant merged | 03 / Foundation Models; 03 / Large Language Models; 03 / Vision Foundation Models; 05 / Token; 13 / Model Types & Families |
| LLM | Large Language Model (LLM) | Important abbreviation merged into the canonical expanded concept | 02 / Attention; 02 / Transformer; 03 / Foundation Models; 03 / Large Language Models; 03 / Multimodal Models; 03 / Scientific Models; 03 / Speech Audio Models; 03 / Vision Foundation Models; 04 / Fine Tuning; 04 / Pre Training; 05 / Token; 05 / Tokenization; 06 / Structured Outputs; 06 / System Prompts; 07 / Generative Ai; 07 / Text Generation; 08 / Grounding; 09 / AI Agent; 09 / Multi-Agent Systems; 09 / Planning; 10 / Ollama; 10 / Vllm; 13 / Model Types & Families; 16 / AI Workflow Platforms |
| Latency | Latency | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 01 / Machine Learning; 03 / Foundation Models; 10 / Latency; 10 / Model Serving; 10 / Tokens per Second; 12 / Monitoring |
| latency | Latency | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models; 04 / Prompting Vs Rag Vs Fine Tuning; 05 / Inference; 05 / KV Cache; 05 / Token; 07 / Image Generation; 08 / Embeddings; 08 / Grounding; 08 / Rag; 08 / Reranking; 08 / Retrieval; 08 / Semantic Search; 08 / Vector Search; 09 / Human in the Loop; 09 / Multi-Agent Systems; 10 / GPU, VRAM & Unified Memory; 10 / Latency; 10 / Local AI vs Cloud AI; 10 / Quantization; 10 / Runtime Constraints; 10 / Tokens per Second; 10 / Vllm; 11 / Benchmarks; 11 / Deployment Readiness; 11 / Evaluation; 12 / Deployment; 12 / Monitoring; 17 / Deployment & Operations |
| response time | Latency | Synonym or expanded/short form merged into one concept | 10 / Latency; 10 / Runtime Constraints; 10 / Tokens per Second; 10 / Vllm; 12 / Deployment; 17 / Deployment & Operations |
| latency breakdown | Latency Breakdown | Same normalized label; repeated source occurrence consolidated | 10 / Latency |
| layer | Layer | Same normalized label; repeated source occurrence consolidated | 01 / Artificial Intelligence; 02 / Neural Networks; 02 / Transformer; 03 / Large Language Models; 04 / Pre Training; 10 / Model Serving; 11 / Guardrails; 13 / Major AI Providers; 16 / AI Workflow Platforms; 17 / Frontend & Backend; 19 / Backend Technologies; 19 / Frontend Technologies |
| Layer | Layer | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 02 / CNN; 02 / Layers |
| layers | Layer | Important abbreviation merged into the canonical expanded concept | 02 / Neural Networks; 02 / Transformer; 11 / Guardrails |
| Neural Network Layer | Layer | Case, hyphen, spacing, or capitalization variant merged | 02 / Layers |
| neural network layer | Layer | Synonym or expanded/short form merged into one concept | 02 / Transformer; 03 / Large Language Models |
| neural-network layer | Layer | Case, hyphen, spacing, or capitalization variant merged | 02 / Attention; 02 / Transformer |
| layer normalization | Layer Normalization | Same normalized label; repeated source occurrence consolidated | 02 / Attention; 03 / Large Language Models |
| Layer Normalization | Layer Normalization | Same normalized label; repeated source occurrence consolidated | 02 / Layers |
| Learning Rate | Learning Rate | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning |
| Learning rate | Learning Rate | Same normalized label; repeated source occurrence consolidated | 01 / Machine Learning |
| learning rate | Learning Rate | Same normalized label; repeated source occurrence consolidated | 01 / Supervised Learning; 03 / Large Language Models; 03 / Parameters; 04 / Pre Training; 04 / Training Data |
| Least privilege | Least Privilege | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| least privilege | Least Privilege | Same normalized label; repeated source occurrence consolidated | 09 / Human in the Loop; 11 / Permissions Safety; 11 / Prompt Injection; 12 / Deployment |
| Least Privilege | Least Privilege | Same normalized label; repeated source occurrence consolidated | 11 / Permissions Safety |
| Llama | Llama | Same normalized label; repeated source occurrence consolidated | 10 / Ollama; 13 / Major AI Providers; 13 / Model Types & Families |
| LLM chain | LLM Chain | Same normalized label; repeated source occurrence consolidated | 16 / AI Workflow Platforms |
| local AI | Local AI | Same normalized label; repeated source occurrence consolidated | 10 / GPU, VRAM & Unified Memory; 10 / Ollama; 10 / Quantization; 10 / Runtime Constraints; 10 / Vllm; 13 / Open vs Closed / Local Models |
| Local AI | Local AI | Same normalized label; repeated source occurrence consolidated | 10 / Local AI vs Cloud AI; 10 / Ollama |
| Local model | Local Model | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| local model | Local Model | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models; 07 / Image Generation; 10 / Local AI vs Cloud AI; 10 / Ollama; 10 / Quantization; 13 / Open vs Closed / Local Models |
| local models | Local Model | Synonym or expanded/short form merged into one concept | 13 / Major AI Providers |
| logit | Logit | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models; 05 / Inference |
| Long Short-Term Memory | Long Short-Term Memory (LSTM) | Case, hyphen, spacing, or capitalization variant merged | 01 / Deep Learning; 02 / RNN / LSTM |
| LSTM | Long Short-Term Memory (LSTM) | Important abbreviation merged into the canonical expanded concept | 01 / Deep Learning; 02 / RNN / LSTM |
| Long-term memory | Long-Term Memory | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| long-term memory | Long-Term Memory | Same normalized label; repeated source occurrence consolidated | 05 / KV Cache |
| Loss Function | Loss Function | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning |
| Loss function | Loss Function | Same normalized label; repeated source occurrence consolidated | 01 / Machine Learning |
| loss function | Loss Function | Same normalized label; repeated source occurrence consolidated | 01 / Supervised Learning; 03 / Large Language Models; 03 / Parameters; 04 / Pre Training; 04 / Training Data |
| LoRA | Low-Rank Adaptation (LoRA) | Important abbreviation merged into the canonical expanded concept | 03 / Foundation Models; 03 / Multimodal Models; 03 / Parameters |
| machine learning | Machine Learning (ML) | Synonym or expanded/short form merged into one concept | 01 / Artificial Intelligence; 01 / Reinforcement Learning; 02 / Neural Networks; 04 / Training Data |
| Machine Learning | Machine Learning (ML) | Case, hyphen, spacing, or capitalization variant merged | 01 / Deep Learning; 01 / Machine Learning; 01 / Reinforcement Learning; 01 / Supervised Learning; 01 / Unsupervised Learning; 02 / Neural Networks |
| ML | Machine Learning (ML) | Important abbreviation merged into the canonical expanded concept | 01 / Artificial Intelligence; 01 / Deep Learning; 01 / Machine Learning; 01 / Reinforcement Learning; 04 / Training Data |
| managed database | Managed Database | Same normalized label; repeated source occurrence consolidated | 18 / Backend & Data Platforms; 18 / Web & Cloud Platforms |
| masked language modeling | Masked Language Modeling | Same normalized label; repeated source occurrence consolidated | 04 / Pre Training |
| MCP client | MCP Client | Same normalized label; repeated source occurrence consolidated | 09 / Model Context Protocol (MCP) |
| MCP server | MCP Server | Same normalized label; repeated source occurrence consolidated | 09 / Model Context Protocol (MCP) |
| Mean Squared Error | Mean Squared Error (MSE) | Case, hyphen, spacing, or capitalization variant merged | 01 / Deep Learning |
| Mean squared error | Mean Squared Error (MSE) | Case, hyphen, spacing, or capitalization variant merged | 01 / Machine Learning |
| mean squared error | Mean Squared Error (MSE) | Synonym or expanded/short form merged into one concept | 01 / Supervised Learning; 04 / Training Data |
| MSE | Mean Squared Error (MSE) | Important abbreviation merged into the canonical expanded concept | 01 / Deep Learning |
| memory footprint | Memory Footprint | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models; 03 / Parameters; 05 / KV Cache; 10 / Quantization; 10 / Runtime Constraints; 10 / Vllm |
| Meta AI | Meta AI | Same normalized label; repeated source occurrence consolidated | 13 / Major AI Providers |
| middleware | Middleware | Same normalized label; repeated source occurrence consolidated | 10 / Vllm |
| Mini-batch | Mini-Batch | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 01 / Machine Learning |
| mini-batch | Mini-Batch | Same normalized label; repeated source occurrence consolidated | 01 / Supervised Learning; 04 / Training Data |
| missing-token prediction | Missing-Token Prediction | Same normalized label; repeated source occurrence consolidated | 04 / Pre Training |
| Mistral AI | Mistral AI | Same normalized label; repeated source occurrence consolidated | 13 / Major AI Providers |
| mixed precision | Mixed Precision | Same normalized label; repeated source occurrence consolidated | 10 / Quantization |
| Modality | Modality | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 13 / Major AI Providers |
| modality | Modality | Same normalized label; repeated source occurrence consolidated | 03 / Multimodal Models; 03 / Speech Audio Models; 03 / Vision Foundation Models; 07 / Audio Generation; 07 / Image Generation; 07 / Multimodal Ai; 07 / Video Generation; 08 / Embeddings; 13 / Model Types & Families |
| modality fusion | Modality Fusion | Same normalized label; repeated source occurrence consolidated | 03 / Multimodal Models |
| model API | Model API | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models; 19 / Product Services |
| Model Capacity | Model Capacity | Same normalized label; repeated source occurrence consolidated | 02 / Layers |
| model capacity | Model Capacity | Same normalized label; repeated source occurrence consolidated | 03 / Parameters |
| MCP | Model Context Protocol (MCP) | Important abbreviation merged into the canonical expanded concept | 09 / AI Agent; 09 / Human in the Loop; 09 / Memory State; 09 / Model Context Protocol (MCP); 09 / Multi-Agent Systems; 09 / Skills / Plugins; 10 / Api; 15 / How AI Agents Are Built |
| Model Context Protocol | Model Context Protocol (MCP) | Case, hyphen, spacing, or capitalization variant merged | 09 / Model Context Protocol (MCP); 09 / Skills / Plugins; 10 / Api |
| Model family | Model Family | Same normalized label; repeated source occurrence consolidated | 01 / Machine Learning; 03 / Foundation Models; 13 / Major AI Providers; 13 / Model Types & Families |
| model family | Model Family | Same normalized label; repeated source occurrence consolidated | 01 / Supervised Learning; 03 / Large Language Models; 03 / Scientific Models; 03 / Vision Foundation Models; 07 / Image Generation; 10 / Quantization; 10 / Vllm; 13 / Major AI Providers; 13 / Open vs Closed / Local Models; 14 / AI Assistants & Coding Tools |
| Model Family | Model Family | Same normalized label; repeated source occurrence consolidated | 02 / Diffusion Models |
| MODEL FAMILY | Model Family | Same normalized label; repeated source occurrence consolidated | 13 / Major AI Providers |
| Model Parameter | Model Parameter | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning |
| model parameter | Model Parameter | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models; 04 / Pre Training |
| model parameters | Model Parameter | Synonym or expanded/short form merged into one concept | 01 / Artificial Intelligence; 02 / Attention; 03 / Parameters; 04 / Fine Tuning; 04 / Prompting Vs Rag Vs Fine Tuning; 04 / Training Data; 05 / Inference; 05 / KV Cache; 05 / Next Token Prediction; 06 / System Prompts; 07 / Image Generation; 07 / Text Generation; 09 / Memory State; 10 / Quantization; 12 / Continuous Improvement |
| Model parameters | Model Parameter | Case, hyphen, spacing, or capitalization variant merged | 01 / Machine Learning; 03 / Foundation Models |
| Parameter | Model Parameter | Case, hyphen, spacing, or capitalization variant merged | 01 / Deep Learning; 02 / Layers |
| parameter | Model Parameter | Synonym or expanded/short form merged into one concept | 01 / Supervised Learning; 03 / Large Language Models; 04 / Fine Tuning; 04 / Pre Training; 04 / Training Data; 05 / KV Cache; 05 / Token |
| Parameters | Model Parameter | Case, hyphen, spacing, or capitalization variant merged | 01 / Machine Learning; 03 / Foundation Models; 03 / Parameters; 04 / Fine Tuning; 05 / Token |
| parameters | Model Parameter | Synonym or expanded/short form merged into one concept | 02 / Neural Networks; 03 / Parameters; 04 / Instruction Tuning; 04 / Prompting Vs Rag Vs Fine Tuning; 05 / Inference; 06 / System Prompts; 10 / Quantization |
| model runtime | Model Runtime | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models; 10 / Model Serving; 10 / Ollama; 10 / Runtime Constraints; 10 / Vllm; 13 / Open vs Closed / Local Models |
| Runtime | Model Runtime | Case, hyphen, spacing, or capitalization variant merged | 01 / Deep Learning |
| runtime | Model Runtime | Synonym or expanded/short form merged into one concept | 04 / Fine Tuning; 04 / Instruction Tuning; 04 / Prompting Vs Rag Vs Fine Tuning; 05 / Inference; 05 / KV Cache; 06 / System Prompts; 07 / Text Generation; 08 / Grounding; 08 / Rag; 10 / Api; 10 / Local AI vs Cloud AI; 10 / Model Serving; 10 / Ollama; 10 / Quantization; 10 / Runtime Constraints; 10 / Vllm; 13 / Open vs Closed / Local Models; 15 / How AI Agents Are Built; 18 / Web & Cloud Platforms; 19 / Backend Technologies |
| RUNTIME | Model Runtime | Case, hyphen, spacing, or capitalization variant merged | 10 / Model Serving |
| Model Serving | Model Serving | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 10 / Model Serving; 10 / Vllm |
| Model serving | Model Serving | Same normalized label; repeated source occurrence consolidated | 01 / Machine Learning; 03 / Foundation Models |
| model serving | Model Serving | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models; 05 / Inference; 05 / KV Cache; 07 / Image Generation; 10 / GPU, VRAM & Unified Memory; 10 / Local AI vs Cloud AI; 10 / Ollama; 10 / Quantization; 10 / Runtime Constraints; 10 / Vllm; 13 / Open vs Closed / Local Models |
| Model Size | Model Size | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 10 / GPU, VRAM & Unified Memory |
| model size | Model Size | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models; 03 / Parameters; 10 / GPU, VRAM & Unified Memory; 10 / Local AI vs Cloud AI; 10 / Quantization |
| Model Type | Model Type | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 02 / Diffusion Models |
| Model type | Model Type | Same normalized label; repeated source occurrence consolidated | 01 / Machine Learning; 03 / Foundation Models; 13 / Model Types & Families |
| model type | Model Type | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models; 04 / Training Data; 07 / Text Generation |
| Monitoring | Monitoring | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 01 / Machine Learning; 03 / Foundation Models; 12 / Continuous Improvement; 12 / Monitoring |
| monitoring | Monitoring | Same normalized label; repeated source occurrence consolidated | 01 / Supervised Learning; 01 / Unsupervised Learning; 04 / Training Data; 08 / Grounding; 09 / Human in the Loop; 10 / Model Serving; 11 / Deployment Readiness; 11 / Failure Modes; 11 / Functional Tests; 11 / Hallucination; 12 / Continuous Improvement; 12 / Deployment; 12 / Integration; 12 / Monitoring; 16 / AI Workflow Platforms; 17 / Deployment & Operations; 19 / Product Services |
| MONITORING | Monitoring | Same normalized label; repeated source occurrence consolidated | 17 / Deployment & Operations; 19 / Product Services |
| multi-agent orchestration | Multi-Agent Orchestration | Same normalized label; repeated source occurrence consolidated | 15 / Agent Frameworks |
| Multi-Agent System | Multi-Agent System | Same normalized label; repeated source occurrence consolidated | 09 / Multi-Agent Systems |
| multi-agent system | Multi-Agent System | Same normalized label; repeated source occurrence consolidated | 09 / Multi-Agent Systems; 15 / How AI Agents Are Built |
| Multi-Agent Systems | Multi-Agent System | Case, hyphen, spacing, or capitalization variant merged | 09 / Multi-Agent Systems |
| multi-agent systems | Multi-Agent System | Case, hyphen, spacing, or capitalization variant merged | 09 / Multi-Agent Systems |
| multi-head attention | Multi-Head Attention | Same normalized label; repeated source occurrence consolidated | 02 / Attention |
| multimodal AI | Multimodal AI | Same normalized label; repeated source occurrence consolidated | 03 / Multimodal Models; 03 / Speech Audio Models; 07 / Image Generation; 07 / Video Generation |
| Multimodal AI | Multimodal AI | Same normalized label; repeated source occurrence consolidated | 07 / Image Generation; 07 / Multimodal Ai |
| Multimodal Model | Multimodal Model | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 03 / Multimodal Models; 13 / Model Types & Families |
| Multimodal model | Multimodal Model | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| multimodal model | Multimodal Model | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models; 03 / Multimodal Models; 03 / Scientific Models; 03 / Vision Foundation Models; 07 / Image Generation; 07 / Multimodal Ai; 13 / Model Types & Families |
| Neural Net | Neural Network | Case, hyphen, spacing, or capitalization variant merged | 01 / Deep Learning |
| neural network | Neural Network | Same normalized label; repeated source occurrence consolidated | 01 / Artificial Intelligence; 01 / Supervised Learning; 02 / Attention; 02 / Neural Networks; 02 / RNN / LSTM; 03 / Large Language Models; 03 / Multimodal Models; 04 / Pre Training; 04 / Training Data; 07 / Image Generation; 10 / GPU, VRAM & Unified Memory |
| Neural Network | Neural Network | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 02 / CNN; 02 / Diffusion Models; 02 / Layers; 02 / Neural Networks |
| Neural network | Neural Network | Same normalized label; repeated source occurrence consolidated | 01 / Machine Learning; 02 / CNN |
| Neural Networks | Neural Network | Case, hyphen, spacing, or capitalization variant merged | 02 / Neural Networks; 02 / RNN / LSTM; 02 / Transformer |
| neural networks | Neural Network | Synonym or expanded/short form merged into one concept | 02 / Neural Networks; 02 / Transformer |
| Neural network architecture | Neural Network Architecture | Same normalized label; repeated source occurrence consolidated | 02 / CNN |
| Neural Network Architecture | Neural Network Architecture | Same normalized label; repeated source occurrence consolidated | 02 / Layers |
| neural network architecture | Neural Network Architecture | Same normalized label; repeated source occurrence consolidated | 02 / Transformer |
| Neural-network architecture | Neural Network Architecture | Same normalized label; repeated source occurrence consolidated | 02 / CNN |
| Neural-Network Architecture | Neural Network Architecture | Same normalized label; repeated source occurrence consolidated | 02 / Diffusion Models |
| neural-network architecture | Neural Network Architecture | Same normalized label; repeated source occurrence consolidated | 02 / RNN / LSTM; 02 / Transformer |
| next token prediction | Next-Token Prediction | Same normalized label; repeated source occurrence consolidated | 02 / RNN / LSTM; 05 / Next Token Prediction |
| next-token prediction | Next-Token Prediction | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models; 03 / Parameters; 04 / Pre Training; 05 / Inference; 05 / Next Token Prediction; 05 / Sampling Temperature; 05 / Token; 07 / Text Generation |
| Next-token Prediction | Next-Token Prediction | Same normalized label; repeated source occurrence consolidated | 05 / Next Token Prediction; 07 / Text Generation |
| Next.js | Next.js | Same normalized label; repeated source occurrence consolidated | 17 / Frontend & Backend; 18 / Web & Cloud Platforms; 19 / Frontend Technologies |
| Node runtime | Node.js | Case, hyphen, spacing, or capitalization variant merged | 19 / Backend Technologies |
| Node.js | Node.js | Same normalized label; repeated source occurrence consolidated | 17 / Frontend & Backend; 19 / Backend Technologies |
| numerical precision | Numerical Precision | Same normalized label; repeated source occurrence consolidated | 10 / Quantization |
| original precision | Numerical Precision | Synonym or expanded/short form merged into one concept | 13 / Open vs Closed / Local Models |
| parameter precision | Numerical Precision | Synonym or expanded/short form merged into one concept | 03 / Parameters |
| observability | Observability | Same normalized label; repeated source occurrence consolidated | 08 / Grounding; 08 / Retrieval; 09 / Agent Loop; 10 / Model Serving; 11 / Failure Handling; 11 / Failure Modes; 12 / Deployment; 12 / Integration; 17 / Deployment & Operations |
| observation | Observation | Same normalized label; repeated source occurrence consolidated | 01 / Unsupervised Learning; 09 / AI Agent; 09 / Agent Loop; 09 / Human in the Loop; 09 / Planning; 12 / Workflow Discovery; 15 / How AI Agents Are Built |
| Offline evaluation | Offline Evaluation | Same normalized label; repeated source occurrence consolidated | 01 / Machine Learning; 03 / Foundation Models |
| offline evaluation | Offline Evaluation | Same normalized label; repeated source occurrence consolidated | 04 / Training Data; 08 / Retrieval |
| Ollama | Ollama | Same normalized label; repeated source occurrence consolidated | 10 / Model Serving; 10 / Ollama; 10 / Quantization; 10 / Runtime Constraints; 10 / Vllm; 13 / Open vs Closed / Local Models |
| ollama | Ollama | Same normalized label; repeated source occurrence consolidated | 10 / Ollama |
| Online evaluation | Online Evaluation | Same normalized label; repeated source occurrence consolidated | 01 / Machine Learning; 03 / Foundation Models |
| online evaluation | Online Evaluation | Same normalized label; repeated source occurrence consolidated | 04 / Training Data; 08 / Retrieval |
| Open source | Open-Source Model | Case, hyphen, spacing, or capitalization variant merged | 18 / Developer Platforms |
| open-source | Open-Source Model | Case, hyphen, spacing, or capitalization variant merged | 13 / Open vs Closed / Local Models |
| open-source model | Open-Source Model | Same normalized label; repeated source occurrence consolidated | 13 / Open vs Closed / Local Models |
| Open-weight | Open-Weight Model | Case, hyphen, spacing, or capitalization variant merged | 13 / Major AI Providers |
| open-weight | Open-Weight Model | Case, hyphen, spacing, or capitalization variant merged | 13 / Major AI Providers; 13 / Open vs Closed / Local Models |
| open-weight model | Open-Weight Model | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models; 13 / Major AI Providers; 13 / Open vs Closed / Local Models |
| OpenAI | OpenAI | Same normalized label; repeated source occurrence consolidated | 13 / Major AI Providers; 13 / Model Types & Families; 14 / AI Assistants & Coding Tools; 15 / Agent Frameworks |
| OCR | Optical Character Recognition (OCR) | Important abbreviation merged into the canonical expanded concept | 03 / Multimodal Models; 12 / Monitoring |
| optical character recognition | Optical Character Recognition (OCR) | Synonym or expanded/short form merged into one concept | 03 / Multimodal Models |
| optical character recognition (OCR) | Optical Character Recognition (OCR) | Same normalized label; repeated source occurrence consolidated | 03 / Vision Foundation Models |
| Optimizer | Optimizer | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning |
| optimizer | Optimizer | Same normalized label; repeated source occurrence consolidated | 01 / Supervised Learning; 03 / Large Language Models; 03 / Parameters; 04 / Pre Training; 04 / Training Data |
| outpainting | Outpainting | Same normalized label; repeated source occurrence consolidated | 07 / Image Generation |
| output modality | Output Modality | Same normalized label; repeated source occurrence consolidated | 03 / Multimodal Models; 05 / Inference; 07 / Multimodal Ai; 13 / Model Types & Families |
| parser | Output Parser | Important abbreviation merged into the canonical expanded concept | 06 / Structured Outputs |
| output schema | Output Schema | Same normalized label; repeated source occurrence consolidated | 06 / Context Engineering; 11 / Benchmarks |
| Schema | Output Schema | Important abbreviation merged into the canonical expanded concept | 03 / Foundation Models |
| schema | Output Schema | Important abbreviation merged into the canonical expanded concept | 04 / Fine Tuning; 04 / Instruction Tuning; 06 / Context Engineering; 06 / Structured Outputs; 06 / System Prompts; 07 / Code Generation; 07 / Generative Ai; 10 / Api; 11 / Functional Tests; 12 / Integration |
| output token | Output Token | Same normalized label; repeated source occurrence consolidated | 05 / Token; 07 / Text Generation; 10 / Latency; 10 / Vllm |
| Overfitting | Overfitting | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 01 / Machine Learning |
| overfitting | Overfitting | Same normalized label; repeated source occurrence consolidated | 01 / Supervised Learning; 03 / Large Language Models; 03 / Parameters; 04 / Pre Training; 05 / Inference |
| Parameter Count | Parameter Count | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning |
| parameter count | Parameter Count | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models; 03 / Parameters; 04 / Pre Training; 10 / Quantization |
| Parameter-efficient fine-tuning | Parameter-Efficient Fine-Tuning (PEFT) | Case, hyphen, spacing, or capitalization variant merged | 03 / Foundation Models |
| parameter-efficient fine-tuning | Parameter-Efficient Fine-Tuning (PEFT) | Case, hyphen, spacing, or capitalization variant merged | 03 / Parameters |
| pattern recognition | Pattern Recognition | Same normalized label; repeated source occurrence consolidated | 01 / Artificial Intelligence |
| Pattern recognition | Pattern Recognition | Same normalized label; repeated source occurrence consolidated | 02 / CNN |
| Permission | Permission | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| permission | Permission | Same normalized label; repeated source occurrence consolidated | 06 / Prompt Design; 08 / Retrieval; 08 / Vector Search; 09 / Agent Loop; 09 / Human in the Loop; 09 / Model Context Protocol (MCP); 09 / Skills / Plugins; 11 / Benchmarks; 11 / Guardrails; 11 / Permissions Safety; 11 / Prompt Injection; 12 / Integration; 14 / AI Assistants & Coding Tools; 14 / General Agents & Computer Use; 15 / How AI Agents Are Built; 16 / AI Workflow Platforms; 17 / Data, APIs & Authentication; 17 / Frontend & Backend |
| PERMISSION | Permission | Same normalized label; repeated source occurrence consolidated | 11 / Guardrails; 11 / Permissions Safety |
| Personally identifiable information | Personally Identifiable Information (PII) | Case, hyphen, spacing, or capitalization variant merged | 03 / Foundation Models |
| personally identifiable information | Personally Identifiable Information (PII) | Synonym or expanded/short form merged into one concept | 09 / Human in the Loop; 12 / Deployment |
| PII | Personally Identifiable Information (PII) | Important abbreviation merged into the canonical expanded concept | 03 / Large Language Models; 09 / Human in the Loop; 12 / Deployment |
| plan | Plan | Same normalized label; repeated source occurrence consolidated | 09 / AI Agent; 09 / Planning; 10 / Runtime Constraints; 11 / Deployment Readiness; 14 / AI Assistants & Coding Tools; 14 / General Agents & Computer Use; 15 / How AI Agents Are Built; 18 / Web & Cloud Platforms |
| Planning | Planning | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models; 09 / Multi-Agent Systems |
| planning | Planning | Same normalized label; repeated source occurrence consolidated | 07 / Video Generation; 09 / AI Agent; 09 / Agent Loop; 09 / Multi-Agent Systems; 09 / Planning; 15 / How AI Agents Are Built; 18 / Developer Platforms |
| plugin | Plugin | Same normalized label; repeated source occurrence consolidated | 09 / Skills / Plugins; 16 / AI Workflow Platforms; 19 / Backend Technologies |
| Pooling | Pooling | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning |
| Pooling Layer | Pooling | Case, hyphen, spacing, or capitalization variant merged | 02 / Layers |
| position embedding | Positional Encoding | Synonym or expanded/short form merged into one concept | 03 / Large Language Models |
| positional encoding | Positional Encoding | Same normalized label; repeated source occurrence consolidated | 02 / Attention; 03 / Large Language Models; 04 / Pre Training |
| Postgres | PostgreSQL | Case, hyphen, spacing, or capitalization variant merged | 18 / Backend & Data Platforms; 19 / Data Technologies |
| PostgreSQL | PostgreSQL | Same normalized label; repeated source occurrence consolidated | 17 / Data, APIs & Authentication; 18 / Backend & Data Platforms; 18 / Web & Cloud Platforms; 19 / Data Technologies |
| Pre-trained model | Pre-Trained Model | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| pre-trained model | Pre-Trained Model | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models; 03 / Vision Foundation Models; 04 / Fine Tuning; 04 / Instruction Tuning |
| pretrained model | Pre-Trained Model | Synonym or expanded/short form merged into one concept | 04 / Pre Training |
| pre-training | Pre-Training | Same normalized label; repeated source occurrence consolidated | 01 / Artificial Intelligence; 03 / Multimodal Models; 03 / Scientific Models; 03 / Vision Foundation Models; 04 / Fine Tuning; 04 / Instruction Tuning; 04 / Training Data |
| Pre-training | Pre-Training | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models; 04 / Fine Tuning; 04 / Instruction Tuning; 04 / Pre Training; 05 / Token |
| Pretraining | Pre-Training | Case, hyphen, spacing, or capitalization variant merged | 01 / Deep Learning |
| pretraining | Pre-Training | Synonym or expanded/short form merged into one concept | 03 / Large Language Models |
| Training objective | Pre-Training Objective | Case, hyphen, spacing, or capitalization variant merged | 03 / Foundation Models |
| training objective | Pre-Training Objective | Synonym or expanded/short form merged into one concept | 03 / Large Language Models; 04 / Pre Training; 04 / Preference Learning Rlhf; 08 / Embeddings |
| Precision | Precision | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 01 / Machine Learning; 03 / Foundation Models |
| precision | Precision | Same normalized label; repeated source occurrence consolidated | 01 / Supervised Learning; 03 / Multimodal Models; 03 / Vision Foundation Models; 04 / Training Data; 05 / Inference; 08 / Reranking; 08 / Retrieval; 08 / Semantic Search; 08 / Vector Search; 09 / Human in the Loop; 10 / GPU, VRAM & Unified Memory; 10 / Quantization; 11 / Hallucination |
| prediction | Prediction | Same normalized label; repeated source occurrence consolidated | 01 / Artificial Intelligence; 01 / Supervised Learning; 01 / Unsupervised Learning; 02 / Neural Networks; 02 / RNN / LSTM; 02 / Transformer; 03 / Large Language Models; 03 / Parameters; 03 / Scientific Models; 04 / Pre Training; 04 / Training Data; 05 / Inference; 05 / Next Token Prediction; 05 / Sampling Temperature; 07 / Generative Ai; 07 / Text Generation; 10 / Tokens per Second |
| Prediction | Prediction | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 01 / Machine Learning; 02 / CNN; 02 / Layers; 05 / Next Token Prediction |
| Preference learning | Preference Learning | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| preference learning | Preference Learning | Same normalized label; repeated source occurrence consolidated | 04 / Pre Training; 04 / Preference Learning Rlhf; 04 / Training Data |
| Preference Learning | Preference Learning | Same normalized label; repeated source occurrence consolidated | 04 / Preference Learning Rlhf |
| preference model | Preference Model | Same normalized label; repeated source occurrence consolidated | 04 / Preference Learning Rlhf |
| prefill | Prefill | Same normalized label; repeated source occurrence consolidated | 05 / KV Cache; 10 / Latency |
| Privacy | Privacy | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 01 / Machine Learning; 03 / Foundation Models |
| privacy | Privacy | Same normalized label; repeated source occurrence consolidated | 01 / Supervised Learning; 01 / Unsupervised Learning; 02 / Attention; 03 / Large Language Models; 03 / Multimodal Models; 04 / Training Data; 05 / Inference; 08 / Grounding; 08 / Vector Search; 09 / Human in the Loop; 10 / Local AI vs Cloud AI; 12 / Deployment; 19 / Product Services |
| production AI | Production AI | Same normalized label; repeated source occurrence consolidated | 12 / Continuous Improvement |
| production monitoring | Production Monitoring | Same normalized label; repeated source occurrence consolidated | 04 / Training Data; 11 / Functional Tests; 17 / Deployment & Operations |
| prompt | Prompt | Same normalized label; repeated source occurrence consolidated | 01 / Artificial Intelligence; 03 / Large Language Models; 03 / Multimodal Models; 03 / Parameters; 03 / Scientific Models; 03 / Speech Audio Models; 03 / Vision Foundation Models; 04 / Fine Tuning; 04 / Instruction Tuning; 04 / Pre Training; 04 / Preference Learning Rlhf; 04 / Prompting Vs Rag Vs Fine Tuning; 04 / Training Data; 05 / Inference; 05 / KV Cache; 05 / Next Token Prediction; 06 / Context Engineering; 06 / Prompt Design; 06 / System Prompts; 07 / Audio Generation; 07 / Generative Ai; 07 / Image Generation; 07 / Multimodal Ai; 07 / Text Generation; 08 / Grounding; 08 / Rag; 09 / Model Context Protocol (MCP); 10 / Api; 10 / Latency; 10 / Model Serving; 10 / Ollama; 11 / Hallucination; 12 / Continuous Improvement; 12 / Monitoring; 13 / Model Types & Families; 16 / AI Workflow Platforms |
| Prompt | Prompt | Same normalized label; repeated source occurrence consolidated | 02 / Diffusion Models; 03 / Foundation Models; 04 / Preference Learning Rlhf; 05 / Context Window; 07 / Generative Ai; 10 / Ollama |
| PROMPT | Prompt | Same normalized label; repeated source occurrence consolidated | 16 / AI Workflow Platforms |
| Prompt design | Prompt Engineering | Case, hyphen, spacing, or capitalization variant merged | 03 / Foundation Models |
| prompt design | Prompt Engineering | Synonym or expanded/short form merged into one concept | 04 / Prompting Vs Rag Vs Fine Tuning; 06 / Context Engineering; 06 / Prompt Design; 06 / System Prompts |
| Prompt Design | Prompt Engineering | Case, hyphen, spacing, or capitalization variant merged | 06 / Prompt Design; 12 / Continuous Improvement |
| Prompt engineering | Prompt Engineering | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| prompt engineering | Prompt Engineering | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models; 04 / Prompting Vs Rag Vs Fine Tuning; 06 / System Prompts; 07 / Image Generation |
| prompting | Prompt Engineering | Synonym or expanded/short form merged into one concept | 01 / Artificial Intelligence; 03 / Scientific Models; 03 / Vision Foundation Models; 04 / Fine Tuning; 04 / Pre Training; 04 / Prompting Vs Rag Vs Fine Tuning |
| Prompting | Prompt Engineering | Case, hyphen, spacing, or capitalization variant merged | 01 / Machine Learning; 03 / Foundation Models; 04 / Instruction Tuning; 04 / Prompting Vs Rag Vs Fine Tuning |
| prompt injection | Prompt Injection | Same normalized label; repeated source occurrence consolidated | 02 / Attention; 03 / Large Language Models; 08 / Grounding; 09 / Human in the Loop; 11 / Guardrails; 11 / Permissions Safety |
| Prompt injection | Prompt Injection | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| Prompt Injection | Prompt Injection | Same normalized label; repeated source occurrence consolidated | 11 / Guardrails; 11 / Permissions Safety; 11 / Prompt Injection |
| Prompt leakage | Prompt Leakage | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| Prompt template | Prompt Template | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| Closed model | Proprietary Model | Case, hyphen, spacing, or capitalization variant merged | 03 / Foundation Models |
| closed model | Proprietary Model | Synonym or expanded/short form merged into one concept | 03 / Large Language Models; 13 / Open vs Closed / Local Models |
| provider strategy | Provider Strategy | Same normalized label; repeated source occurrence consolidated | 13 / Major AI Providers |
| Python | Python | Same normalized label; repeated source occurrence consolidated | 07 / Text Generation; 17 / Frontend & Backend; 19 / Backend Technologies |
| Quantization | Quantization | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 10 / GPU, VRAM & Unified Memory; 10 / Model Serving; 10 / Quantization; 10 / Vllm |
| quantization | Quantization | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models; 03 / Parameters; 05 / Inference; 10 / GPU, VRAM & Unified Memory; 10 / Ollama; 10 / Runtime Constraints; 13 / Open vs Closed / Local Models |
| query rewriting | Query Rewriting | Same normalized label; repeated source occurrence consolidated | 08 / Rag |
| Qwen | Qwen | Same normalized label; repeated source occurrence consolidated | 10 / Ollama; 13 / Major AI Providers; 13 / Model Types & Families |
| RAG pipeline | RAG Pipeline | Same normalized label; repeated source occurrence consolidated | 16 / AI Workflow Platforms |
| React | React | Same normalized label; repeated source occurrence consolidated | 17 / Frontend & Backend; 19 / Frontend Technologies |
| Reasoning | Reasoning | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models; 13 / Model Types & Families |
| reasoning | Reasoning | Same normalized label; repeated source occurrence consolidated | 03 / Multimodal Models; 05 / Inference; 07 / Multimodal Ai; 09 / Planning; 11 / Benchmarks; 15 / How AI Agents Are Built |
| Recall | Recall | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 01 / Machine Learning; 03 / Foundation Models |
| recall | Recall | Same normalized label; repeated source occurrence consolidated | 01 / Supervised Learning; 03 / Multimodal Models; 03 / Vision Foundation Models; 04 / Training Data; 05 / Inference; 08 / Reranking; 08 / Retrieval; 08 / Semantic Search; 08 / Vector Search; 09 / Human in the Loop; 11 / Hallucination |
| recommendation system | Recommendation System | Same normalized label; repeated source occurrence consolidated | 01 / Reinforcement Learning; 09 / Human in the Loop |
| Recommender system | Recommendation System | Case, hyphen, spacing, or capitalization variant merged | 01 / Machine Learning |
| Recurrent Neural Network | Recurrent Neural Network (RNN) | Case, hyphen, spacing, or capitalization variant merged | 01 / Deep Learning; 02 / CNN; 02 / Layers; 02 / RNN / LSTM |
| recurrent neural network | Recurrent Neural Network (RNN) | Synonym or expanded/short form merged into one concept | 02 / Neural Networks |
| RNN | Recurrent Neural Network (RNN) | Important abbreviation merged into the canonical expanded concept | 01 / Deep Learning; 02 / CNN; 02 / Layers; 02 / Neural Networks; 02 / RNN / LSTM |
| Red teaming | Red Teaming | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| red teaming | Red Teaming | Same normalized label; repeated source occurrence consolidated | 09 / Human in the Loop; 11 / Hallucination |
| Regression | Regression | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 01 / Machine Learning |
| regression | Regression | Same normalized label; repeated source occurrence consolidated | 01 / Supervised Learning; 02 / Neural Networks; 04 / Fine Tuning |
| reinforcement learning | Reinforcement Learning (RL) | Synonym or expanded/short form merged into one concept | 01 / Artificial Intelligence; 01 / Reinforcement Learning; 01 / Unsupervised Learning; 04 / Preference Learning Rlhf; 04 / Training Data |
| Reinforcement Learning | Reinforcement Learning (RL) | Case, hyphen, spacing, or capitalization variant merged | 01 / Deep Learning; 01 / Machine Learning; 01 / Reinforcement Learning; 01 / Unsupervised Learning; 04 / Preference Learning Rlhf |
| RL | Reinforcement Learning (RL) | Important abbreviation merged into the canonical expanded concept | 01 / Reinforcement Learning; 04 / Preference Learning Rlhf |
| Reinforcement Learning from Human Feedback | Reinforcement Learning from Human Feedback (RLHF) | Case, hyphen, spacing, or capitalization variant merged | 01 / Deep Learning; 04 / Preference Learning Rlhf |
| reinforcement learning from human feedback | Reinforcement Learning from Human Feedback (RLHF) | Synonym or expanded/short form merged into one concept | 03 / Large Language Models; 04 / Preference Learning Rlhf |
| RLHF | Reinforcement Learning from Human Feedback (RLHF) | Important abbreviation merged into the canonical expanded concept | 01 / Deep Learning; 03 / Foundation Models; 03 / Large Language Models; 04 / Pre Training; 04 / Preference Learning Rlhf |
| rlHF | Reinforcement Learning from Human Feedback (RLHF) | Important abbreviation merged into the canonical expanded concept | 04 / Preference Learning Rlhf |
| relational database | Relational Database | Same normalized label; repeated source occurrence consolidated | 18 / Backend & Data Platforms; 19 / Data Technologies |
| readiness gate | Release Gate | Synonym or expanded/short form merged into one concept | 11 / Deployment Readiness; 12 / Deployment |
| release gate | Release Gate | Same normalized label; repeated source occurrence consolidated | 11 / Deployment Readiness |
| Reliability | Reliability | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 01 / Machine Learning; 03 / Foundation Models |
| reliability | Reliability | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models; 04 / Instruction Tuning; 05 / Inference; 06 / Structured Outputs; 07 / Image Generation; 07 / Text Generation; 09 / Human in the Loop; 11 / Benchmarks; 11 / Evaluation; 11 / Failure Handling; 11 / Failure Modes; 11 / Hallucination; 11 / Permissions Safety; 11 / Prompt Injection; 12 / Deployment; 17 / Deployment & Operations; 19 / Product Services |
| repository context | Repository Context | Same normalized label; repeated source occurrence consolidated | 14 / AI Assistants & Coding Tools |
| representation | Representation | Same normalized label; repeated source occurrence consolidated | 01 / Artificial Intelligence; 02 / Attention; 02 / Neural Networks; 02 / Transformer; 03 / Multimodal Models; 03 / Scientific Models; 03 / Speech Audio Models; 04 / Pre Training; 04 / Training Data; 05 / Inference; 05 / Tokenization; 07 / Audio Generation; 07 / Generative Ai; 07 / Image Generation; 07 / Multimodal Ai; 07 / Video Generation; 08 / Embeddings; 08 / Semantic Search; 08 / Vector Database; 08 / Vector Search; 10 / GPU, VRAM & Unified Memory |
| Representation | Representation | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 01 / Machine Learning; 02 / CNN; 02 / Layers; 07 / Generative Ai |
| reranker | Reranker | Same normalized label; repeated source occurrence consolidated | 08 / Rag; 08 / Reranking |
| re-ranking | Reranking | Case, hyphen, spacing, or capitalization variant merged | 08 / Reranking |
| rerank | Reranking | Important abbreviation merged into the canonical expanded concept | 08 / Reranking |
| Reranking | Reranking | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models; 08 / Reranking |
| reranking | Reranking | Same normalized label; repeated source occurrence consolidated | 08 / Embeddings; 08 / Grounding; 08 / Rag; 08 / Reranking; 08 / Retrieval; 08 / Vector Search |
| residual connection | Residual Connection | Same normalized label; repeated source occurrence consolidated | 02 / Attention; 03 / Large Language Models |
| Residual Connection | Residual Connection | Same normalized label; repeated source occurrence consolidated | 02 / Layers |
| Responsible AI | Responsible AI | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 03 / Foundation Models |
| responsible AI | Responsible AI | Same normalized label; repeated source occurrence consolidated | 09 / Human in the Loop |
| REST APIs | REST API | Case, hyphen, spacing, or capitalization variant merged | 17 / Data, APIs & Authentication |
| retrieval | Retrieval | Same normalized label; repeated source occurrence consolidated | 01 / Artificial Intelligence; 02 / Attention; 03 / Large Language Models; 03 / Multimodal Models; 03 / Parameters; 04 / Pre Training; 04 / Prompting Vs Rag Vs Fine Tuning; 06 / Context Engineering; 06 / Prompt Design; 07 / Generative Ai; 07 / Image Generation; 07 / Text Generation; 08 / Chunking; 08 / Embeddings; 08 / Grounding; 08 / Rag; 08 / Reranking; 08 / Retrieval; 08 / Semantic Search; 08 / Vector Database; 08 / Vector Search; 11 / Hallucination; 12 / Continuous Improvement; 13 / Model Types & Families; 19 / Data Technologies |
| Retrieval | Retrieval | Same normalized label; repeated source occurrence consolidated | 01 / Machine Learning; 03 / Foundation Models; 05 / Context Window; 08 / Rag; 08 / Retrieval; 08 / Semantic Search |
| retrieval pipeline | Retrieval Pipeline | Same normalized label; repeated source occurrence consolidated | 04 / Prompting Vs Rag Vs Fine Tuning; 08 / Rag; 08 / Retrieval; 08 / Semantic Search |
| RAG | Retrieval-Augmented Generation (RAG) | Important abbreviation merged into the canonical expanded concept | 01 / Artificial Intelligence; 03 / Foundation Models; 03 / Large Language Models; 03 / Multimodal Models; 04 / Fine Tuning; 04 / Instruction Tuning; 04 / Pre Training; 04 / Prompting Vs Rag Vs Fine Tuning; 05 / Context Window; 06 / Context Engineering; 07 / Text Generation; 08 / Chunking; 08 / Embeddings; 08 / Grounding; 08 / Rag; 08 / Reranking; 08 / Retrieval; 08 / Semantic Search; 08 / Vector Database; 08 / Vector Search; 10 / Model Serving; 11 / Hallucination; 12 / Continuous Improvement; 15 / How AI Agents Are Built; 16 / AI Workflow Platforms; 16 / Automation Platforms; 19 / Data Technologies |
| retrieval-augmented generation | Retrieval-Augmented Generation (RAG) | Case, hyphen, spacing, or capitalization variant merged | 02 / Attention; 04 / Fine Tuning; 04 / Pre Training; 08 / Chunking; 08 / Grounding; 08 / Rag; 08 / Retrieval; 08 / Semantic Search; 08 / Vector Database; 08 / Vector Search; 11 / Hallucination; 12 / Continuous Improvement; 16 / AI Workflow Platforms |
| Retrieval-Augmented Generation | Retrieval-Augmented Generation (RAG) | Case, hyphen, spacing, or capitalization variant merged | 03 / Foundation Models; 04 / Instruction Tuning; 04 / Prompting Vs Rag Vs Fine Tuning; 05 / Context Window; 07 / Text Generation; 08 / Rag; 08 / Reranking; 08 / Retrieval; 10 / Model Serving |
| Retriever | Retriever | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| retriever | Retriever | Same normalized label; repeated source occurrence consolidated | 08 / Reranking; 08 / Retrieval; 16 / AI Workflow Platforms |
| Retry | Retry | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| retry | Retry | Same normalized label; repeated source occurrence consolidated | 05 / Inference; 06 / Structured Outputs; 09 / Agent Loop; 09 / Human in the Loop; 11 / Failure Handling; 12 / Deployment; 15 / Agent Frameworks |
| reward model | Reward Model | Same normalized label; repeated source occurrence consolidated | 04 / Preference Learning Rlhf |
| reward signal | Reward Signal | Same normalized label; repeated source occurrence consolidated | 01 / Reinforcement Learning; 04 / Preference Learning Rlhf |
| Reward signal | Reward Signal | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| RLS | RLS | Same normalized label; repeated source occurrence consolidated | 18 / Backend & Data Platforms |
| Rollback | Rollback | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 03 / Foundation Models |
| rollback | Rollback | Same normalized label; repeated source occurrence consolidated | 09 / Human in the Loop; 11 / Deployment Readiness; 11 / Failure Handling; 12 / Deployment |
| Runtime constraint | Runtime Constraints | Case, hyphen, spacing, or capitalization variant merged | 03 / Foundation Models |
| runtime constraint | Runtime Constraints | Synonym or expanded/short form merged into one concept | 10 / Quantization; 10 / Runtime Constraints |
| runtime constraints | Runtime Constraints | Same normalized label; repeated source occurrence consolidated | 10 / GPU, VRAM & Unified Memory |
| Runtime Constraints | Runtime Constraints | Same normalized label; repeated source occurrence consolidated | 10 / GPU, VRAM & Unified Memory; 10 / Ollama; 10 / Runtime Constraints; 10 / Vllm |
| SaaS | SaaS | Same normalized label; repeated source occurrence consolidated | 16 / Automation Platforms |
| safety filter | Safety Filter | Same normalized label; repeated source occurrence consolidated | 07 / Image Generation |
| Sampling | Sampling | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 01 / Machine Learning; 05 / Next Token Prediction |
| sampling | Sampling | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models; 05 / Inference; 05 / Next Token Prediction; 05 / Sampling Temperature; 05 / Token; 07 / Image Generation; 07 / Text Generation |
| scaled dot-product attention | Scaled Dot-Product Attention | Same normalized label; repeated source occurrence consolidated | 02 / Attention |
| schema drift | Schema Drift | Same normalized label; repeated source occurrence consolidated | 12 / Deployment |
| Schema validation | Schema Validation | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models; 06 / Structured Outputs |
| schema validation | Schema Validation | Same normalized label; repeated source occurrence consolidated | 06 / Structured Outputs; 11 / Benchmarks; 11 / Failure Handling |
| scientific foundation model | Scientific Foundation Model | Same normalized label; repeated source occurrence consolidated | 03 / Scientific Models |
| scientific model | Scientific Model | Same normalized label; repeated source occurrence consolidated | 03 / Scientific Models |
| search | Search | Same normalized label; repeated source occurrence consolidated | 07 / Image Generation; 07 / Text Generation; 08 / Chunking; 08 / Embeddings; 08 / Rag; 08 / Semantic Search; 08 / Vector Database; 08 / Vector Search; 09 / Agent Loop; 09 / Planning; 11 / Guardrails; 13 / Model Types & Families; 14 / General Agents & Computer Use |
| Search | Search | Same normalized label; repeated source occurrence consolidated | 08 / Rag; 08 / Retrieval |
| SEARCH | Search | Same normalized label; repeated source occurrence consolidated | 19 / Product Services |
| search engine | Search Engine | Same normalized label; repeated source occurrence consolidated | 01 / Artificial Intelligence; 03 / Large Language Models; 07 / Generative Ai; 08 / Retrieval |
| Search query | Search Query | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| search query | Search Query | Same normalized label; repeated source occurrence consolidated | 08 / Chunking; 08 / Rag; 08 / Semantic Search; 09 / Planning |
| self-attention | Self-Attention | Same normalized label; repeated source occurrence consolidated | 02 / Attention; 03 / Large Language Models; 04 / Pre Training; 05 / KV Cache |
| self-hosted | Self-Hosted Model | Case, hyphen, spacing, or capitalization variant merged | 13 / Open vs Closed / Local Models; 16 / Automation Platforms |
| self-hosted model | Self-Hosted Model | Same normalized label; repeated source occurrence consolidated | 13 / Open vs Closed / Local Models |
| Self-supervised Learning | Self-Supervised Learning | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning |
| Self-supervised learning | Self-Supervised Learning | Same normalized label; repeated source occurrence consolidated | 01 / Machine Learning |
| self-supervised learning | Self-Supervised Learning | Same normalized label; repeated source occurrence consolidated | 01 / Unsupervised Learning; 03 / Vision Foundation Models; 04 / Pre Training |
| Semantic search | Semantic Search | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| semantic search | Semantic Search | Same normalized label; repeated source occurrence consolidated | 08 / Chunking; 08 / Embeddings; 08 / Rag; 08 / Retrieval; 08 / Semantic Search; 08 / Vector Search |
| Semantic Search | Semantic Search | Same normalized label; repeated source occurrence consolidated | 08 / Semantic Search |
| Semi-supervised Learning | Semi-Supervised Learning | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning |
| Semi-supervised learning | Semi-Supervised Learning | Same normalized label; repeated source occurrence consolidated | 01 / Machine Learning |
| sequence model | Sequence Model | Same normalized label; repeated source occurrence consolidated | 02 / RNN / LSTM |
| server | Server | Same normalized label; repeated source occurrence consolidated | 09 / Model Context Protocol (MCP); 10 / Model Serving; 17 / Frontend & Backend; 18 / Developer Platforms |
| serverless | Serverless | Same normalized label; repeated source occurrence consolidated | 18 / Web & Cloud Platforms |
| service | Service | Same normalized label; repeated source occurrence consolidated | 09 / Model Context Protocol (MCP); 10 / Model Serving; 10 / Ollama; 10 / Runtime Constraints; 10 / Vllm; 17 / Data, APIs & Authentication; 17 / Frontend & Backend; 18 / Web & Cloud Platforms; 19 / Backend Technologies |
| Short-term memory | Short-Term Memory | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| Similarity search | Similarity Search | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| similarity search | Similarity Search | Same normalized label; repeated source occurrence consolidated | 08 / Vector Database |
| Similarity Search | Similarity Search | Same normalized label; repeated source occurrence consolidated | 08 / Vector Search |
| skill | Skill | Same normalized label; repeated source occurrence consolidated | 09 / Skills / Plugins |
| small language model | Small Language Model (SLM) | Synonym or expanded/short form merged into one concept | 03 / Large Language Models |
| softmax | Softmax | Same normalized label; repeated source occurrence consolidated | 02 / Attention; 03 / Large Language Models; 04 / Pre Training |
| SDK | Software Development Kit (SDK) | Important abbreviation merged into the canonical expanded concept | 16 / AI Workflow Platforms; 18 / Backend & Data Platforms |
| software development kit | Software Development Kit (SDK) | Synonym or expanded/short form merged into one concept | 16 / AI Workflow Platforms |
| Source attribution | Source Attribution | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| source attribution | Source Attribution | Same normalized label; repeated source occurrence consolidated | 08 / Grounding; 08 / Rag; 08 / Retrieval; 11 / Hallucination |
| special token | Special Token | Same normalized label; repeated source occurrence consolidated | 05 / Token; 05 / Tokenization |
| specialized model | Specialized Model | Same normalized label; repeated source occurrence consolidated | 04 / Fine Tuning; 13 / Model Types & Families |
| specification gaming | Specification Gaming | Same normalized label; repeated source occurrence consolidated | 04 / Preference Learning Rlhf |
| Speech Model | Speech Model | Same normalized label; repeated source occurrence consolidated | 03 / Speech Audio Models |
| speech model | Speech Model | Same normalized label; repeated source occurrence consolidated | 03 / Speech Audio Models; 03 / Vision Foundation Models; 05 / Inference; 07 / Multimodal Ai; 13 / Model Types & Families |
| Structured Output | Structured Output | Same normalized label; repeated source occurrence consolidated | 02 / Diffusion Models |
| Structured output | Structured Output | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| structured output | Structured Output | Same normalized label; repeated source occurrence consolidated | 04 / Fine Tuning; 04 / Instruction Tuning; 06 / Context Engineering; 06 / Prompt Design; 06 / Structured Outputs; 06 / System Prompts; 09 / AI Agent |
| structured outputs | Structured Output | Synonym or expanded/short form merged into one concept | 06 / Context Engineering; 06 / Prompt Design; 06 / Structured Outputs; 06 / System Prompts; 07 / Generative Ai; 09 / AI Agent; 11 / Functional Tests |
| Structured Outputs | Structured Output | Case, hyphen, spacing, or capitalization variant merged | 06 / Prompt Design; 06 / Structured Outputs; 07 / Generative Ai; 07 / Text Generation; 08 / Grounding; 09 / Tool Calling; 11 / Failure Handling; 11 / Functional Tests |
| subword token | Subword Token | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models |
| SFT | Supervised Fine-Tuning (SFT) | Important abbreviation merged into the canonical expanded concept | 03 / Large Language Models; 04 / Instruction Tuning |
| supervised fine-tuning | Supervised Fine-Tuning (SFT) | Case, hyphen, spacing, or capitalization variant merged | 03 / Large Language Models |
| Supervised Fine-Tuning | Supervised Fine-Tuning (SFT) | Case, hyphen, spacing, or capitalization variant merged | 04 / Instruction Tuning |
| supervised learning | Supervised Learning | Same normalized label; repeated source occurrence consolidated | 01 / Artificial Intelligence; 01 / Reinforcement Learning; 01 / Unsupervised Learning; 04 / Instruction Tuning; 04 / Training Data |
| Supervised Learning | Supervised Learning | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 01 / Machine Learning; 01 / Reinforcement Learning; 01 / Supervised Learning; 01 / Unsupervised Learning |
| System instruction | System Prompt | Case, hyphen, spacing, or capitalization variant merged | 05 / Context Window |
| system instruction | System Prompt | Synonym or expanded/short form merged into one concept | 06 / System Prompts; 08 / Rag; 11 / Guardrails; 11 / Prompt Injection |
| SYSTEM INSTRUCTION | System Prompt | Case, hyphen, spacing, or capitalization variant merged | 11 / Guardrails |
| System prompt | System Prompt | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| system prompt | System Prompt | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models; 03 / Multimodal Models; 04 / Prompting Vs Rag Vs Fine Tuning; 06 / Context Engineering; 06 / Prompt Design; 06 / Structured Outputs; 06 / System Prompts; 09 / AI Agent; 09 / Agent Loop; 15 / How AI Agents Are Built |
| System Prompt | System Prompt | Same normalized label; repeated source occurrence consolidated | 06 / Context Engineering; 06 / Prompt Design; 06 / System Prompts |
| system prompts | System Prompt | Synonym or expanded/short form merged into one concept | 06 / Context Engineering; 06 / Prompt Design; 09 / AI Agent |
| System Prompts | System Prompt | Case, hyphen, spacing, or capitalization variant merged | 06 / Structured Outputs; 06 / System Prompts; 11 / Failure Handling |
| Target | Target Variable | Important abbreviation merged into the canonical expanded concept | 01 / Deep Learning; 01 / Machine Learning |
| target | Target Variable | Important abbreviation merged into the canonical expanded concept | 01 / Supervised Learning; 03 / Parameters; 04 / Pre Training; 04 / Training Data; 10 / Runtime Constraints; 11 / Deployment Readiness |
| Task decomposition | Task Decomposition | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| task decomposition | Task Decomposition | Same normalized label; repeated source occurrence consolidated | 09 / Planning |
| technical scoping | Technical Scoping | Same normalized label; repeated source occurrence consolidated | 12 / Deployment; 12 / Integration; 12 / Technical Scoping; 12 / Workflow Discovery |
| Technical Scoping | Technical Scoping | Same normalized label; repeated source occurrence consolidated | 12 / Integration; 12 / Technical Scoping; 12 / Workflow Discovery |
| temperature | Temperature | Same normalized label; repeated source occurrence consolidated | 02 / Attention; 03 / Large Language Models; 05 / Inference; 05 / Next Token Prediction; 05 / Sampling Temperature; 05 / Token; 07 / Text Generation |
| Test case | Test Case | Same normalized label; repeated source occurrence consolidated | 01 / Machine Learning; 03 / Foundation Models |
| test case | Test Case | Same normalized label; repeated source occurrence consolidated | 07 / Code Generation; 11 / Failure Modes; 11 / Functional Tests; 11 / Hallucination |
| Test Set | Test Set | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning |
| Test set | Test Set | Same normalized label; repeated source occurrence consolidated | 01 / Machine Learning; 03 / Foundation Models |
| test set | Test Set | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models; 04 / Pre Training; 04 / Prompting Vs Rag Vs Fine Tuning; 04 / Training Data; 11 / Benchmarks |
| Text Generation | Text Generation | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 07 / Text Generation; 09 / Tool Calling |
| Text generation | Text Generation | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| text generation | Text Generation | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models; 05 / KV Cache; 05 / Next Token Prediction; 07 / Text Generation; 09 / Tool Calling |
| Text-to-Image | Text-to-Image Generation | Case, hyphen, spacing, or capitalization variant merged | 02 / Diffusion Models |
| text-to-image | Text-to-Image Generation | Case, hyphen, spacing, or capitalization variant merged | 03 / Multimodal Models; 07 / Image Generation; 07 / Multimodal Ai; 13 / Model Types & Families |
| speech synthesis | Text-to-Speech (TTS) | Synonym or expanded/short form merged into one concept | 03 / Speech Audio Models |
| text to speech | Text-to-Speech (TTS) | Synonym or expanded/short form merged into one concept | 07 / Audio Generation |
| text-to-speech | Text-to-Speech (TTS) | Case, hyphen, spacing, or capitalization variant merged | 03 / Multimodal Models; 03 / Speech Audio Models; 07 / Audio Generation |
| Text-to-Speech | Text-to-Speech (TTS) | Case, hyphen, spacing, or capitalization variant merged | 03 / Speech Audio Models |
| Text-to-speech (TTS) | Text-to-Speech (TTS) | Same normalized label; repeated source occurrence consolidated | 07 / Audio Generation |
| TTS | Text-to-Speech (TTS) | Important abbreviation merged into the canonical expanded concept | 03 / Multimodal Models; 03 / Speech Audio Models; 07 / Audio Generation |
| text-to-video | Text-to-Video Generation | Case, hyphen, spacing, or capitalization variant merged | 03 / Multimodal Models; 07 / Video Generation; 13 / Model Types & Families |
| Text-to-video | Text-to-Video Generation | Case, hyphen, spacing, or capitalization variant merged | 07 / Video Generation |
| text-to-video generation | Text-to-Video Generation | Same normalized label; repeated source occurrence consolidated | 07 / Video Generation |
| Throughput | Throughput | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 01 / Machine Learning; 03 / Foundation Models |
| throughput | Throughput | Same normalized label; repeated source occurrence consolidated | 02 / Attention; 03 / Large Language Models; 04 / Pre Training; 05 / Inference; 05 / KV Cache; 05 / Token; 07 / Image Generation; 08 / Embeddings; 08 / Rag; 08 / Reranking; 08 / Retrieval; 08 / Semantic Search; 08 / Vector Search; 09 / Human in the Loop; 10 / Latency; 10 / Model Serving; 10 / Quantization; 10 / Runtime Constraints; 10 / Tokens per Second; 10 / Vllm; 12 / Deployment |
| time to first token | Time to First Token (TTFT) | Synonym or expanded/short form merged into one concept | 05 / KV Cache; 10 / Latency; 10 / Model Serving; 10 / Tokens per Second |
| Time to First Token | Time to First Token (TTFT) | Case, hyphen, spacing, or capitalization variant merged | 10 / Tokens per Second |
| TTFT | Time to First Token (TTFT) | Important abbreviation merged into the canonical expanded concept | 10 / Latency; 10 / Tokens per Second |
| Timeout | Timeout | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| timeout | Timeout | Same normalized label; repeated source occurrence consolidated | 05 / Inference; 09 / Agent Loop; 09 / Human in the Loop; 10 / Latency; 11 / Failure Handling; 11 / Failure Modes; 12 / Deployment |
| token | Token | Same normalized label; repeated source occurrence consolidated | 01 / Artificial Intelligence; 02 / Attention; 02 / Transformer; 03 / Large Language Models; 03 / Multimodal Models; 03 / Parameters; 03 / Scientific Models; 04 / Pre Training; 05 / Inference; 05 / KV Cache; 05 / Next Token Prediction; 05 / Sampling Temperature; 05 / Token; 05 / Tokenization; 07 / Generative Ai; 07 / Text Generation; 08 / Chunking; 08 / Embeddings; 10 / Latency; 10 / Model Serving; 10 / Runtime Constraints; 10 / Tokens per Second |
| Token | Token | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 02 / Layers; 02 / Transformer; 03 / Foundation Models; 05 / Context Window; 05 / Token; 07 / Text Generation; 08 / Rag; 10 / Tokens per Second |
| Token Sequence | Token Sequence | Same normalized label; repeated source occurrence consolidated | 02 / Layers |
| token sequence | Token Sequence | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models; 04 / Pre Training; 05 / Inference; 05 / KV Cache; 05 / Next Token Prediction; 05 / Token; 05 / Tokenization |
| Tokenization | Tokenization | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 05 / Context Window; 05 / Tokenization |
| tokenization | Tokenization | Same normalized label; repeated source occurrence consolidated | 02 / Attention; 03 / Large Language Models; 04 / Pre Training; 05 / Inference; 05 / Next Token Prediction; 05 / Token; 10 / Tokens per Second |
| tokenizer | Tokenizer | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models; 04 / Pre Training; 05 / Token; 05 / Tokenization |
| Tokenizer | Tokenizer | Same normalized label; repeated source occurrence consolidated | 05 / Token |
| token per second | Tokens per Second (TPS) | Synonym or expanded/short form merged into one concept | 10 / Tokens per Second |
| token throughput | Tokens per Second (TPS) | Synonym or expanded/short form merged into one concept | 03 / Large Language Models |
| tokens per second | Tokens per Second (TPS) | Synonym or expanded/short form merged into one concept | 04 / Pre Training; 05 / Inference; 05 / KV Cache; 05 / Token; 10 / GPU, VRAM & Unified Memory; 10 / Latency; 10 / Model Serving; 10 / Quantization; 10 / Runtime Constraints; 10 / Tokens per Second; 10 / Vllm |
| Tokens per Second | Tokens per Second (TPS) | Case, hyphen, spacing, or capitalization variant merged | 10 / GPU, VRAM & Unified Memory; 10 / Runtime Constraints; 10 / Tokens per Second |
| TPS | Tokens per Second (TPS) | Important abbreviation merged into the canonical expanded concept | 10 / GPU, VRAM & Unified Memory; 10 / Latency; 10 / Model Serving; 10 / Tokens per Second; 10 / Vllm |
| tool | Tool | Same normalized label; repeated source occurrence consolidated | 01 / Artificial Intelligence; 03 / Large Language Models; 03 / Multimodal Models; 06 / Context Engineering; 06 / Prompt Design; 09 / AI Agent; 09 / Agent Loop; 09 / Model Context Protocol (MCP); 09 / Planning; 09 / Skills / Plugins; 09 / Tool Calling; 10 / Api; 10 / Vllm; 11 / Failure Modes; 11 / Guardrails; 11 / Permissions Safety; 11 / Prompt Injection; 12 / Adoption; 12 / Continuous Improvement; 12 / Integration; 12 / Technical Scoping; 14 / General Agents & Computer Use; 15 / Agent Frameworks; 15 / How AI Agents Are Built; 16 / AI Workflow Platforms; 17 / Data, APIs & Authentication; 19 / Backend Technologies |
| Tool | Tool | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| Tool call | Tool Calling | Case, hyphen, spacing, or capitalization variant merged | 05 / Context Window |
| tool call | Tool Calling | Synonym or expanded/short form merged into one concept | 08 / Grounding; 09 / AI Agent; 09 / Agent Loop; 09 / Human in the Loop; 09 / Model Context Protocol (MCP); 09 / Tool Calling; 11 / Failure Handling; 11 / Functional Tests; 15 / How AI Agents Are Built |
| Tool calling | Tool Calling | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models; 09 / Tool Calling |
| tool calling | Tool Calling | Same normalized label; repeated source occurrence consolidated | 03 / Multimodal Models; 06 / Structured Outputs; 06 / System Prompts; 09 / AI Agent; 09 / Model Context Protocol (MCP); 09 / Planning; 09 / Skills / Plugins; 09 / Tool Calling; 10 / Api; 11 / Failure Handling; 11 / Permissions Safety; 11 / Prompt Injection; 12 / Integration; 14 / AI Assistants & Coding Tools; 14 / General Agents & Computer Use |
| Tool Calling | Tool Calling | Same normalized label; repeated source occurrence consolidated | 06 / Structured Outputs; 07 / Code Generation; 09 / Multi-Agent Systems; 09 / Planning; 09 / Tool Calling; 10 / Api; 11 / Failure Handling; 11 / Permissions Safety; 12 / Integration; 12 / Technical Scoping |
| tool-calling | Tool Calling | Same normalized label; repeated source occurrence consolidated | 09 / Tool Calling |
| Tool result | Tool Result | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models; 05 / Context Window |
| tool result | Tool Result | Same normalized label; repeated source occurrence consolidated | 06 / Context Engineering; 06 / Prompt Design; 06 / System Prompts; 08 / Grounding; 09 / Planning; 09 / Tool Calling; 11 / Prompt Injection |
| Tool Result | Tool Result | Same normalized label; repeated source occurrence consolidated | 09 / Tool Calling |
| Tool schema | Tool Schema | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| Tool use | Tool Use | Same normalized label; repeated source occurrence consolidated | 01 / Machine Learning; 03 / Foundation Models |
| tool use | Tool Use | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models; 09 / AI Agent; 09 / Agent Loop; 11 / Prompt Injection |
| top-k retrieval | Top-k Retrieval | Same normalized label; repeated source occurrence consolidated | 08 / Grounding; 08 / Retrieval; 08 / Semantic Search |
| top-k | Top-k Sampling | Important abbreviation merged into the canonical expanded concept | 08 / Retrieval; 08 / Semantic Search |
| top-k sampling | Top-k Sampling | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models |
| top-p sampling | Top-p Sampling | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models |
| model training | Training | Synonym or expanded/short form merged into one concept | 01 / Supervised Learning; 03 / Scientific Models; 04 / Preference Learning Rlhf; 04 / Training Data; 06 / System Prompts; 12 / Integration |
| Model training | Training | Case, hyphen, spacing, or capitalization variant merged | 03 / Foundation Models |
| training | Training | Same normalized label; repeated source occurrence consolidated | 01 / Artificial Intelligence; 01 / Supervised Learning; 01 / Unsupervised Learning; 02 / Attention; 02 / Neural Networks; 03 / Large Language Models; 03 / Parameters; 03 / Scientific Models; 03 / Vision Foundation Models; 04 / Instruction Tuning; 04 / Preference Learning Rlhf; 04 / Prompting Vs Rag Vs Fine Tuning; 04 / Training Data; 05 / Inference; 05 / Next Token Prediction; 06 / System Prompts; 07 / Generative Ai; 07 / Image Generation; 07 / Text Generation; 08 / Grounding; 08 / Rag; 09 / Human in the Loop; 10 / Quantization; 12 / Adoption |
| Training | Training | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 01 / Machine Learning; 02 / CNN; 02 / Diffusion Models; 03 / Foundation Models; 05 / Context Window |
| Training process | Training | Case, hyphen, spacing, or capitalization variant merged | 01 / Machine Learning; 03 / Foundation Models |
| Training Process | Training | Case, hyphen, spacing, or capitalization variant merged | 02 / Diffusion Models |
| training process | Training | Synonym or expanded/short form merged into one concept | 04 / Fine Tuning; 04 / Pre Training; 04 / Training Data |
| training data | Training Data | Same normalized label; repeated source occurrence consolidated | 01 / Artificial Intelligence; 01 / Supervised Learning; 01 / Unsupervised Learning; 02 / Attention; 03 / Large Language Models; 03 / Parameters; 03 / Scientific Models; 04 / Pre Training; 04 / Training Data; 07 / Image Generation |
| Training Data | Training Data | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 02 / Diffusion Models; 04 / Training Data |
| Training data | Training Data | Same normalized label; repeated source occurrence consolidated | 01 / Machine Learning; 03 / Foundation Models |
| Training Example | Training Example | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning |
| training example | Training Example | Same normalized label; repeated source occurrence consolidated | 01 / Supervised Learning; 03 / Parameters; 03 / Vision Foundation Models; 04 / Fine Tuning; 04 / Instruction Tuning; 04 / Pre Training; 04 / Training Data |
| Training Pipeline | Training Pipeline | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning |
| Training pipeline | Training Pipeline | Same normalized label; repeated source occurrence consolidated | 01 / Machine Learning; 03 / Foundation Models |
| training pipeline | Training Pipeline | Same normalized label; repeated source occurrence consolidated | 04 / Training Data |
| Training Set | Training Set | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning |
| Training set | Training Set | Same normalized label; repeated source occurrence consolidated | 01 / Machine Learning; 03 / Foundation Models |
| training set | Training Set | Same normalized label; repeated source occurrence consolidated | 04 / Training Data |
| Transfer Learning | Transfer Learning | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning |
| Transfer learning | Transfer Learning | Same normalized label; repeated source occurrence consolidated | 01 / Machine Learning; 03 / Foundation Models |
| transfer learning | Transfer Learning | Same normalized label; repeated source occurrence consolidated | 03 / Vision Foundation Models |
| Transformer | Transformer | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 02 / Attention; 02 / CNN; 02 / Diffusion Models; 02 / Layers; 02 / Neural Networks; 02 / RNN / LSTM; 02 / Transformer; 03 / Large Language Models; 03 / Multimodal Models; 05 / KV Cache; 05 / Token |
| transformer | Transformer | Same normalized label; repeated source occurrence consolidated | 02 / Transformer; 03 / Vision Foundation Models; 04 / Pre Training; 07 / Image Generation |
| Transformer architecture | Transformer Architecture | Same normalized label; repeated source occurrence consolidated | 02 / Attention; 02 / RNN / LSTM; 02 / Transformer |
| Transformer Architecture | Transformer Architecture | Same normalized label; repeated source occurrence consolidated | 02 / Layers |
| transformer architecture | Transformer Architecture | Same normalized label; repeated source occurrence consolidated | 02 / Neural Networks |
| Transformer block | Transformer Block | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models |
| Transformer layer | Transformer Layer | Same normalized label; repeated source occurrence consolidated | 02 / Attention; 03 / Large Language Models; 05 / KV Cache |
| trigger | Trigger | Same normalized label; repeated source occurrence consolidated | 16 / AI Workflow Platforms; 16 / Automation Platforms; 17 / Deployment & Operations |
| TRIGGER | Trigger | Same normalized label; repeated source occurrence consolidated | 16 / Automation Platforms |
| TypeScript | TypeScript | Same normalized label; repeated source occurrence consolidated | 19 / Backend Technologies; 19 / Frontend Technologies |
| Underfitting | Underfitting | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 01 / Machine Learning |
| underfitting | Underfitting | Same normalized label; repeated source occurrence consolidated | 01 / Supervised Learning; 04 / Pre Training; 05 / Inference |
| Unified Memory | Unified Memory | Same normalized label; repeated source occurrence consolidated | 10 / GPU, VRAM & Unified Memory |
| unified memory | Unified Memory | Same normalized label; repeated source occurrence consolidated | 10 / GPU, VRAM & Unified Memory |
| unsupervised learning | Unsupervised Learning | Same normalized label; repeated source occurrence consolidated | 01 / Artificial Intelligence; 01 / Reinforcement Learning; 04 / Pre Training; 04 / Training Data |
| Unsupervised Learning | Unsupervised Learning | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 01 / Machine Learning; 01 / Reinforcement Learning; 01 / Unsupervised Learning |
| Unsupervised learning | Unsupervised Learning | Same normalized label; repeated source occurrence consolidated | 01 / Unsupervised Learning |
| unsupported claim | Unsupported Claim | Same normalized label; repeated source occurrence consolidated | 08 / Grounding; 11 / Guardrails; 11 / Hallucination |
| user feedback | User Feedback | Same normalized label; repeated source occurrence consolidated | 04 / Preference Learning Rlhf; 11 / Evaluation; 12 / Adoption; 12 / Continuous Improvement |
| User Feedback | User Feedback | Same normalized label; repeated source occurrence consolidated | 11 / Evaluation |
| User prompt | User Prompt | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| user prompt | User Prompt | Same normalized label; repeated source occurrence consolidated | 04 / Prompting Vs Rag Vs Fine Tuning; 06 / Context Engineering; 06 / Prompt Design; 06 / System Prompts |
| User Prompt | User Prompt | Same normalized label; repeated source occurrence consolidated | 06 / Context Engineering |
| user prompts | User Prompt | Synonym or expanded/short form merged into one concept | 06 / Prompt Design |
| Validation Set | Validation Set | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning |
| Validation set | Validation Set | Same normalized label; repeated source occurrence consolidated | 01 / Machine Learning; 03 / Foundation Models |
| validation set | Validation Set | Same normalized label; repeated source occurrence consolidated | 03 / Large Language Models; 04 / Pre Training; 04 / Training Data |
| VAE | Variational Autoencoder (VAE) | Important abbreviation merged into the canonical expanded concept | 02 / Diffusion Models; 07 / Image Generation |
| Variational Autoencoder | Variational Autoencoder (VAE) | Case, hyphen, spacing, or capitalization variant merged | 02 / Diffusion Models |
| variational autoencoder | Variational Autoencoder (VAE) | Synonym or expanded/short form merged into one concept | 07 / Image Generation |
| Vector | Vector | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 03 / Foundation Models |
| vector | Vector | Same normalized label; repeated source occurrence consolidated | 01 / Unsupervised Learning; 08 / Embeddings; 08 / Rag; 08 / Reranking; 08 / Retrieval; 08 / Semantic Search; 08 / Vector Database; 08 / Vector Search |
| Vector database | Vector Database | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| vector database | Vector Database | Same normalized label; repeated source occurrence consolidated | 08 / Chunking; 08 / Embeddings; 08 / Grounding; 08 / Rag; 08 / Retrieval; 08 / Vector Database; 08 / Vector Search; 19 / Data Technologies |
| Vector Database | Vector Database | Same normalized label; repeated source occurrence consolidated | 08 / Vector Database |
| vector index | Vector Index | Same normalized label; repeated source occurrence consolidated | 08 / Retrieval; 08 / Vector Database; 08 / Vector Search |
| Vector Index | Vector Index | Same normalized label; repeated source occurrence consolidated | 08 / Vector Search |
| vector representation | Vector Representation | Same normalized label; repeated source occurrence consolidated | 02 / Attention; 08 / Embeddings; 08 / Vector Database; 08 / Vector Search; 19 / Data Technologies |
| vector representations | Vector Representation | Synonym or expanded/short form merged into one concept | 08 / Vector Search; 19 / Data Technologies |
| vector search | Vector Search | Same normalized label; repeated source occurrence consolidated | 08 / Embeddings; 08 / Grounding; 08 / Rag; 08 / Reranking; 08 / Retrieval; 08 / Semantic Search; 08 / Vector Database; 08 / Vector Search; 19 / Data Technologies |
| Vector Search | Vector Search | Same normalized label; repeated source occurrence consolidated | 08 / Rag; 08 / Retrieval; 08 / Semantic Search; 08 / Vector Search |
| Video Generation | Video Generation | Same normalized label; repeated source occurrence consolidated | 02 / Diffusion Models; 07 / Audio Generation; 07 / Image Generation; 07 / Video Generation |
| video generation | Video Generation | Same normalized label; repeated source occurrence consolidated | 07 / Image Generation; 07 / Multimodal Ai; 07 / Video Generation |
| Video generation | Video Generation | Same normalized label; repeated source occurrence consolidated | 07 / Video Generation; 13 / Model Types & Families |
| Vision Foundation Model | Vision Foundation Model | Same normalized label; repeated source occurrence consolidated | 03 / Vision Foundation Models |
| vision foundation model | Vision Foundation Model | Same normalized label; repeated source occurrence consolidated | 03 / Vision Foundation Models |
| vision transformer | Vision Transformer (ViT) | Synonym or expanded/short form merged into one concept | 02 / Attention |
| Vision Transformer | Vision Transformer (ViT) | Case, hyphen, spacing, or capitalization variant merged | 02 / Attention |
| vision transformer (ViT) | Vision Transformer (ViT) | Same normalized label; repeated source occurrence consolidated | 03 / Vision Foundation Models |
| ViT | Vision Transformer (ViT) | Important abbreviation merged into the canonical expanded concept | 02 / Attention |
| Vision-Language Model | Vision-Language Model (VLM) | Case, hyphen, spacing, or capitalization variant merged | 01 / Deep Learning |
| vision-language model | Vision-Language Model (VLM) | Case, hyphen, spacing, or capitalization variant merged | 03 / Multimodal Models |
| VLM | Vision-Language Model (VLM) | Important abbreviation merged into the canonical expanded concept | 03 / Multimodal Models |
| visual question answering | Visual Question Answering (VQA) | Synonym or expanded/short form merged into one concept | 03 / Multimodal Models |
| visual question answering (VQA) | Visual Question Answering (VQA) | Same normalized label; repeated source occurrence consolidated | 03 / Vision Foundation Models |
| VQA | Visual Question Answering (VQA) | Important abbreviation merged into the canonical expanded concept | 03 / Multimodal Models |
| vLLM | vLLM | Same normalized label; repeated source occurrence consolidated | 10 / Model Serving; 10 / Vllm; 13 / Open vs Closed / Local Models |
| VRAM | VRAM | Same normalized label; repeated source occurrence consolidated | 05 / KV Cache; 07 / Image Generation; 10 / GPU, VRAM & Unified Memory; 10 / Vllm |
| model weights | Weight | Synonym or expanded/short form merged into one concept | 04 / Pre Training; 05 / KV Cache; 10 / GPU, VRAM & Unified Memory; 10 / Model Serving; 10 / Ollama; 10 / Vllm; 13 / Open vs Closed / Local Models |
| Weight | Weight | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning; 02 / Layers |
| weight | Weight | Same normalized label; repeated source occurrence consolidated | 01 / Supervised Learning; 03 / Parameters |
| Weights | Weight | Case, hyphen, spacing, or capitalization variant merged | 01 / Machine Learning; 02 / Layers |
| weights | Weight | Synonym or expanded/short form merged into one concept | 03 / Large Language Models; 04 / Pre Training; 10 / GPU, VRAM & Unified Memory; 10 / Model Serving; 10 / Ollama; 10 / Vllm; 13 / Major AI Providers; 13 / Open vs Closed / Local Models |
| Workflow Automation | Workflow Automation | Same normalized label; repeated source occurrence consolidated | 01 / Deep Learning |
| workflow discovery | Workflow Discovery | Same normalized label; repeated source occurrence consolidated | 12 / Adoption; 12 / Deployment; 12 / Integration; 12 / Technical Scoping; 12 / Workflow Discovery |
| Workflow Discovery | Workflow Discovery | Same normalized label; repeated source occurrence consolidated | 12 / Integration; 12 / Technical Scoping; 12 / Workflow Discovery |
| workflow fit | Workflow Fit | Same normalized label; repeated source occurrence consolidated | 11 / Benchmarks; 12 / Adoption |
| workflow map | Workflow Map | Same normalized label; repeated source occurrence consolidated | 12 / Technical Scoping; 12 / Workflow Discovery |
| Workflow Map | Workflow Map | Same normalized label; repeated source occurrence consolidated | 12 / Workflow Discovery |
| Orchestration | Workflow Orchestration | Case, hyphen, spacing, or capitalization variant merged | 03 / Foundation Models |
| orchestration | Workflow Orchestration | Synonym or expanded/short form merged into one concept | 09 / Agent Loop; 09 / Human in the Loop; 09 / Skills / Plugins; 15 / Agent Frameworks; 15 / How AI Agents Are Built; 16 / AI Workflow Platforms |
| Workflow orchestration | Workflow Orchestration | Same normalized label; repeated source occurrence consolidated | 03 / Foundation Models |
| workflow orchestration | Workflow Orchestration | Same normalized label; repeated source occurrence consolidated | 09 / Human in the Loop |

## Exclusion summary

| Exclusion reason | Unique labels |
|---|---:|
| Generic or context-specific wording without an independent AI concept | 12178 |
| Comparison sentence or non-atomic phrase | 944 |
| Page structure, example, or explanatory label | 334 |
| Generic short word without a stable AI-specific meaning | 256 |
| Long-tail phrase without an independent glossary concept | 172 |
| Ordinary English function word | 3 |

## Exclusion examples

### Generic or context-specific wording without an independent AI concept

`1 路 Condition`; `1 路 Define`; `1 路 Goal`; `1 路 Input`; `1 路 Prompt`; `100% review`; `13 GB model file`; `13 GB of weights`; `16 GB VRAM`; `2 路 Assign`; `2 路 Encode`; `2 路 Representation`; `2 路 Request`; `20 candidates`; `20 TPS`; `24 GB unified memory`; `24 GB VRAM`; `24/7 operations`; `3 路 Generate`; `3 路 Generation`; `3 路 Validate`; `3 路 Work`; `4 路 Create frames`; `4 路 Decode`; `4 路 Exchange`; `4 路 Execute`; `鈥?4 GB unified memory鈥?`; `鈥?4 GB VRAM鈥?`; `4 路 Repeat`; `4 路 Validate`; `40 TPS`; `5 路 Decode`; `5 路 Handle`; `5 路 Output`; `5 路 Return`; `5 路 Review`; `6 路 Output`; `a coordinator or shared task`; `A Demo`; `a prompt`

### Generic short word without a stable AI-specific meaning

`10%`; `$10,000`; `11%`; `13`; `15%`; `18%`; `2%`; `30 days`; `4%`; `$500`; `52%`; `60 days`; `87%`; `a task`; `act`; `add it`; `app`; `apps`; `ask`; `back link`; `bank`; `bit`; `blue`; `book`; `book open`; `bot`; `bots`; `bug`; `bug only`; `bugs`; `call`; `call tool`; `can`; `cap`; `car`; `card`; `cars`; `case`; `cat`; `chat`

### Comparison sentence or non-atomic phrase

`access vs location`; `action loop toward a goal`; `adapt to the current state`; `Adaptation path versus hierarchy`; `Adaptation versus pre-training`; `add a token`; `add the next token`; `add the selected token`; `add to an index`; `added to a search index`; `adjust the distribution`; `agent inside an editor`; `agent system versus model`; `agent uses model capability inside an action loop`; `agent versus workflow`; `AI / System: extracts fields and sends exceptions to a review queue`; `AI assistant vs coding agent vs AI IDE`; `AI does not equal a search engine`; `AI does not equal automation`; `AI does not equal ChatGPT`; `AI does not equal human creativity`; `AI does not equal the human mind`; `鈥渇ailure handling鈥?versus 鈥渞etry鈥?`; `鈥渇ailure handling鈥?versus 鈥渋gnoring errors鈥?`; `鈥渇ailure handling鈥?versus 鈥渆rror message鈥?`; `鈥渞ain on a window鈥?`; `annual leave entitlement in the HR policy`; `answer a question`; `answer the question`; `answer with the book open`; `API around a database`; `API connection vs AI integration`; `API is the interface`; `API used by a tool`; `API vs MCP`; `API vs serving engine`; `API vs tool calling`; `appearance of a word`; `application can use the result`; `Application fit versus evaluation`

### Page structure, example, or explanatory label

`account lookup example`; `across locations`; `AI product example`; `analogy`; `analogy limitation`; `analogy section`; `analogy simplified`; `API location`; `artist analogy`; `Assembly Line Analogy`; `attention allocation`; `attention visualization`; `audio-visual`; `autocomplete analogy`; `backend returns result (example)`; `behavior example`; `benchmark result analogy`; `briefing folder analogy`; `Broad education analogy`; `broad examples`; `broad visual patterns`; `broad visual representation`; `broad visual understanding`; `Build / Refine Visual Representation`; `Build richer visual features`; `business example`; `Business example 路 Support assistant`; `cached page result`; `Calendar event example`; `category label`; `Cloudflare Pages`; `common platform examples`; `compare predictions with examples`; `comparison section`; `contact-card example`; `Context budget allocation`; `Context capacity allocation`; `control-loop analogy`; `cooking analogy`; `correct labels in advance`

### Long-tail phrase without an independent glossary concept

`Add rules 鈫?Add request 鈫?Add context 鈫?Generate 鈫?Review`; `additional training focused on following instructions`; `AI does not need to appear in every automation workflow`; `AI IDE / development environment (category)`; `AI integration is not API connection only`; `AI integration is not automation without review`; `AI integration is not model training`; `answer employee leave-policy questions accurately`; `app 鈫?network / API 鈫?cloud provider 鈫?model`; `application 鈫?API 鈫?model serving 鈫?vLLM 鈫?model 鈫?GPU`; `application architecture takes time to learn`; `application 鈫?Ollama 鈫?model 鈫?quantization 鈫?hardware 鈫?inference`; `application 鈫?system prompt + user prompt + context 鈫?LLM 鈫?output`; `attention + stacked neural network layers`; `Backend = server-side processing / application logic`; `base model 鈫?target examples 鈫?additional training 鈫?specialized model 鈫?evaluation`; `broad data 鈫?pre-training 鈫?base model 鈫?adaptation`; `Broad education leading to specialized tasks`; `build APIs and application logic on top of them`; `build, integrate, evaluate, readiness, deploy, real users, monitor`; `business need 鈫?Workflow discovery 鈫?Technical scope 鈫?Prototype 鈫?Evaluation 鈫?Deployment`; `chat, autocomplete, agent loops, editors, terminals, and human approval`; `check errors, timeouts, schema, and evidence`; `Claude = model family + branded product`; `coding agent adds tools and actions`; `combine audio with text and images`; `combine models, prompts, knowledge, and tools`; `connect triggers, applications, data, and actions`; `constrain inputs, outputs, actions, and access`; `Content is represented as model-readable units`; `Context fills up 鈫?information may be compacted`; `Context fills up 鈫?information may be summarized`; `Context fills up 鈫?old information may be removed`; `context 鈫?inference 鈫?first token 鈫?tokens per second 鈫?complete output`; `create new sound rather than only analyzing existing audio`; `creates new content from patterns learned during training`; `current task information 鈫?selected facts 鈫?current context`; `data quality does not guarantee perfection`; `decentralized coordination instead of one central coordinator`; `decoder turns it into playable audio`

### Ordinary English function word

`IS`; `of`; `The`
