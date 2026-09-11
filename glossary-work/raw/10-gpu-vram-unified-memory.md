# Topic 10 · GPU / VRAM / Unified Memory

## Topic Metadata

- **Module:** 10 · Model Serving & Local AI
- **Topic:** GPU / VRAM / Unified Memory
- **Source page:** `gpu-vram-unified-memory.html`
- **Page title:** GPU, VRAM, and Unified Memory · Model Serving & Local AI
- **Extraction scope:** Full visible page body, including navigation labels, headings, definitions, explanatory paragraphs, architecture cards, hardware comparison, analogy labels, memory formula, practical example, quantization flow, related-concept tree, chips, takeaway, and video placeholder.
- **Collection policy:** Maximum raw candidate inventory. Candidates are intentionally broad, overlapping, and not deduplicated or pruned. Technical terms, mechanisms, workflow nodes, metrics, abbreviations, important body words, aliases, synonyms, analogy terms, and potentially confusable concepts are retained for later review.

## Glossary Candidates

| Candidate | Category | Working definition / why it matters | Page evidence or context |
|---|---|---|---|
| GPU | Core hardware concept | Graphics Processing Unit; processor used for highly parallel computation and neural-network work. | Page title; GPU section |
| Graphics Processing Unit | Expansion of GPU | A processor architecture designed to execute many operations in parallel. | Expansion of the GPU abbreviation |
| GPU compute | Hardware capability | The parallel calculation capacity supplied by a GPU. | “GPU compute” in the practical hardware-resource picture |
| compute | Resource | Processing capacity used to perform model calculations. | “enough compute and memory to run” |
| compute resource | Resource concept | Hardware capacity available for inference calculations. | Hardware-resource picture |
| compute capacity | Metric / resource | The amount of processing capability available to a workload. | Implied by “enough compute” |
| parallel computation | Mechanism | Computation performed across many operations or workers at once. | GPU definition |
| highly parallel computation | Mechanism | A computation pattern for which GPUs are designed. | GPU definition |
| parallel processing | Alias / mechanism | Processing many calculation units concurrently. | Synonym candidate for highly parallel computation |
| processor | Hardware concept | A computing component that performs operations. | GPU definition |
| processing unit | Hardware concept | A unit that performs computation; GPU is a specialized example. | Expansion candidate for GPU |
| graphics processor | Alias / hardware concept | Shorter name for a graphics processing unit. | Alias candidate for GPU |
| neural-network inference | Workload | Running a neural network on input data to produce an output. | GPU explanation |
| neural network | Model concept | A model whose inference includes many matrix operations. | “Neural-network inference” |
| inference | Core operation | Executing a model for an input; here it requires compute and runtime memory. | Related concepts; runtime discussion |
| model inference | Alias / operation | The act of running a model during a workload. | “while running”; related concept tree |
| matrix operation | Computation | An operation on matrices that forms a large part of neural-network inference. | GPU explanation |
| matrix operations | Plural / computation | Many large matrix calculations processed efficiently by GPUs. | GPU explanation |
| large matrix operations | Workload characteristic | Matrix computations with enough scale to benefit from GPU parallelism. | GPU explanation |
| neural-network calculations | Alias / computation | Calculations performed during neural-network inference. | GPU explanation |
| model | Core concept | The computational object whose weights and runtime state must be held in memory. | Model-size and runtime sections |
| model size | Metric / concept | The size of the model representation, commonly discussed through its model file or weights. | Related-concept tree |
| model file | Artifact | A stored file that mainly represents model weights, not all memory required at runtime. | “Why model size is not enough” |
| model weights | Model representation | Learned numeric values that must be held for inference. | VRAM section; runtime formula |
| weights | Alias / model representation | Short form for model weights. | “13 GB of weights” |
| stored model weights | Artifact content | Weight data represented by a model file before runtime overhead is added. | Model-size explanation |
| weight memory | Memory use | Memory occupied by model weights. | Runtime formula; quantization flow |
| 13 GB model file | Example quantity | Example model-file size that does not guarantee a 13 GB runtime footprint. | Runtime note |
| 13 GB of weights | Example quantity | Example amount of weight storage in the practical example. | Computer A example |
| 16 GB VRAM | Example capacity | Example dedicated GPU-memory capacity used to test whether a model fits. | Computer A example |
| memory | Core resource | Storage capacity for model weights, caches, activations, temporary data, and overhead. | Hero and architecture sections |
| memory resource | Resource concept | Hardware storage required by the model and its execution state. | Practical hardware-resource question |
| hardware resource picture | Architecture concept | The combined view of compute and memory available to AI workloads. | Hero paragraph |
| available memory | Capacity concept | Memory the workload can use after accounting for the relevant hardware arrangement. | “memory available to that worker” |
| memory capacity | Metric | Amount of memory available to a model/runtime workload. | “does the model have enough ... memory?” |
| memory pool | Architecture concept | A pool from which one or more processors draw memory. | Unified memory definition |
| shared memory pool | Architecture concept | One memory pool usable by both CPU and GPU in a unified-memory architecture. | Unified memory card |
| memory architecture | Architecture concept | The arrangement of CPU, GPU, system RAM, dedicated VRAM, or shared memory. | “Two ways to organize memory” |
| traditional PC | Hardware architecture | Architecture with CPU/system RAM and a discrete GPU/dedicated VRAM arrangement. | Traditional PC card |
| traditional memory architecture | Alias / architecture | Traditional PC organization with separate processor-side and GPU-side memory. | Architecture comparison |
| CPU | Core hardware concept | Central Processing Unit; in the comparison, it uses system RAM or shares unified memory. | Architecture cards; unified memory |
| Central Processing Unit | Expansion of CPU | General-purpose processor paired with system RAM or a shared pool. | Expansion of CPU abbreviation |
| system RAM | Hardware memory | Main memory associated with the CPU in the traditional PC layout. | Traditional PC card |
| RAM | Alias / memory | Random-access memory; shorthand for system RAM or general working memory. | Alias candidate for system RAM |
| main memory | Alias / memory | Memory used by the system and CPU. | Alias candidate for system RAM |
| GPU memory | Alias / memory | Memory used by a GPU; may mean dedicated VRAM or shared memory depending on architecture. | Related to VRAM and unified memory |
| dedicated GPU memory | Memory architecture | Memory reserved/directly available to a discrete GPU. | VRAM definition |
| dedicated memory | Alias / memory architecture | Memory separated for a specific device, especially a discrete GPU. | Dedicated VRAM comparison |
| discrete GPU | Hardware architecture | A GPU represented as a separate graphics processor with its own VRAM. | Traditional PC card; VRAM definition |
| discrete graphics | Alias / hardware architecture | Separate GPU hardware rather than an integrated/shared arrangement. | Alias candidate for discrete GPU |
| discrete GPU memory | Alias / memory architecture | Dedicated memory attached to a discrete GPU. | VRAM section |
| VRAM | Core memory concept | Video Random-Access Memory; memory directly available to a discrete GPU. | Page title; VRAM section |
| Video Random-Access Memory | Expansion of VRAM | Memory directly available to a discrete GPU. | VRAM definition |
| video memory | Alias / memory | Another name for VRAM. | Alias candidate for VRAM |
| dedicated VRAM | Core memory concept | VRAM separated from system RAM and dedicated to the GPU. | Traditional PC card; comparison |
| VRAM capacity | Metric | Amount of dedicated GPU memory available to a workload. | “16 GB VRAM” example |
| VRAM usage | Metric / resource use | The amount of dedicated GPU memory consumed by weights and runtime data. | Implied by fit question |
| VRAM fit | Capacity check | Whether model weights plus runtime requirements fit within available VRAM. | “Does it fit?” example |
| memory fit | Capacity check | Whether the complete workload can fit in its available memory. | Practical example |
| model fit | Capacity check | The model may fit in one workload and fail in another because runtime needs vary. | Example answer |
| Unified Memory | Core architecture concept | A shared memory pool used by CPU and GPU in a unified-memory architecture. | Page title; Unified Memory section |
| unified memory | Case variant / architecture | Shared CPU/GPU memory rather than separate system RAM and dedicated VRAM. | Hardware comparison |
| unified-memory architecture | Architecture | Hardware arrangement in which CPU and GPU draw from one shared pool. | Unified Memory definition |
| shared CPU/GPU memory | Alias / architecture | Memory accessible to both CPU and GPU. | Unified memory definition |
| shared memory | Alias / architecture | Memory shared by CPU and GPU rather than separated into two pools. | Unified memory card |
| CPU + GPU | Hardware relationship | The processor pair that can share one pool in a unified-memory system. | Unified memory architecture card |
| CPU and GPU | Hardware relationship | Two processors drawing from a shared pool in the unified-memory model. | Unified memory explanation |
| Apple Silicon | Hardware example | Common example of a unified-memory architecture. | Unified Memory section |
| Mac | Hardware example | A Mac with unified memory is used to show why capacity labels are not directly equivalent to VRAM labels. | “24 GB unified memory” example |
| 24 GB unified memory | Example capacity | Example shared-memory capacity on a Mac. | Hardware comparison |
| 24 GB VRAM | Example capacity | Example dedicated-VRAM label used for comparison with unified memory. | Hardware comparison |
| separate system RAM | Memory architecture | System RAM separate from GPU VRAM in a traditional PC. | Unified memory comparison |
| separate GPU VRAM | Memory architecture | Dedicated GPU memory separate from system RAM. | Unified memory comparison |
| one shared pool | Architecture description | A single pool from which CPU and GPU draw memory. | Unified memory comparison |
| memory sharing | Mechanism | CPU and GPU using the same memory pool. | Unified memory explanation |
| hardware architecture | Architecture concept | The physical organization that determines whether memory is dedicated or shared. | Architecture comparison |
| processor architecture | Architecture concept | The arrangement of processors and their accessible memory. | GPU and unified-memory definitions |
| memory organization | Architecture concept | How system RAM, VRAM, CPU, and GPU are arranged. | Section heading “Two ways to organize memory” |
| same practical question | Decision concept | Whether the model has enough compute and memory to run, regardless of architecture. | Architecture note |
| enough compute | Capacity requirement | Sufficient processing capability for the workload. | Architecture note |
| enough memory | Capacity requirement | Sufficient storage for weights and runtime state. | Architecture note |
| run the model | Workflow / operation | Execute a model successfully on the available hardware. | Architecture note |
| GPU as worker | Analogy | Analogy in which the GPU is the worker doing calculations. | Worker analogy |
| worker | Analogy term | The entity that performs calculations in the GPU/workbench analogy. | “GPU = worker” |
| compute engine | Alias / analogy | The GPU viewed as the engine performing calculations. | Worker analogy text |
| doing the calculations | Operation | The GPU’s role in carrying out model computations. | Worker analogy |
| VRAM as workbench | Analogy | Analogy in which VRAM is the workspace available to the GPU worker. | Worker analogy |
| workbench | Analogy term | The memory workspace available to the compute worker. | “VRAM = workbench” |
| workspace | Memory analogy | Space used to hold active model and inference data. | Workbench analogy |
| memory available to that worker | Working-memory concept | GPU-accessible memory used during calculations. | Worker analogy |
| runtime data | Runtime state | Data needed while a model is executing, beyond stored weights. | Hero; VRAM section |
| working memory | Runtime resource | Memory used during execution for caches, context, temporary data, and overhead. | “Running the model also needs working memory” |
| runtime memory | Core runtime concept | Memory required while running the model. | On-page navigation; runtime section |
| runtime memory requirement | Capacity requirement | Total memory required by weights and the runtime workload. | Practical example |
| runtime footprint | Memory metric | Actual memory consumed while the model runs. | “more than 13 GB ... while running” |
| runtime working set | Alias / memory metric | Active runtime data held during inference. | Candidate synthesis from working memory |
| runtime overhead | Runtime memory component | Additional memory consumed by the runtime itself beyond weights and caches. | Formula; practical example |
| overhead | Alias / runtime component | Extra memory requirement associated with execution. | “overhead” in formula and example |
| model execution | Workflow | Running the model with its weights and runtime state. | Runtime memory discussion |
| model loading | Workflow node | Bringing model weights into available memory before execution. | Implied by weights and runtime discussion |
| active model | Runtime state | A model currently loaded or executing and consuming memory. | Candidate from “while running” |
| KV cache | Runtime memory component | Cache that consumes memory during sequence generation and varies with workload/context. | Formula; practical example; quantization flow |
| key-value cache | Expansion of KV cache | Cache of attention keys and values retained during generation. | Expansion candidate for KV abbreviation |
| KV-cache memory | Memory component | Memory occupied by the key-value cache. | Formula |
| context-related memory | Runtime memory component | Memory associated with the request’s context. | Formula; practical example |
| context | Workload state | Input/output context that contributes to runtime memory use. | Context-related memory |
| context window | Related concept | Maximum or active context capacity associated with model execution. | Related-concept chip |
| context length | Metric / workload parameter | Amount of context used by a request; affects context-related memory and KV cache. | Candidate from context section |
| temporary data | Runtime memory component | Short-lived data needed during inference. | Formula; practical example |
| inference working data | Runtime memory component | Active data used while computing an inference result. | VRAM section |
| activations | Runtime memory component | Intermediate neural-network values held during computation. | VRAM section |
| activation memory | Alias / runtime component | Memory occupied by intermediate activations. | Alias candidate for activations |
| intermediate values | Alias / runtime component | Values produced between model operations during inference. | Candidate from activations |
| intermediate data | Alias / runtime component | Data held temporarily during model execution. | Candidate from temporary data and activations |
| other inference working data | Broad runtime category | Additional active data required by the inference workload. | VRAM section |
| inference working memory | Alias / runtime resource | Memory for caches, activations, temporary data, and other execution state. | VRAM and runtime sections |
| formula | Resource model | Additive view of runtime memory requirements. | Memory formula card |
| model weights + KV cache + context-related memory + temporary data + runtime overhead | Memory decomposition | The page’s visible decomposition of total runtime memory. | Memory formula |
| additive memory requirement | Mechanism / model | Runtime memory consists of multiple components rather than model weights alone. | Formula and note |
| fixed multiplier | Estimation concept | A single universal multiplier from model-file size to runtime memory; the page says none exists. | Runtime note |
| no single fixed multiplier | Caveat / estimation rule | Runtime memory cannot be predicted by one constant factor for every model and workload. | Runtime note |
| model file size | Metric | Stored artifact size, which is not the same as runtime memory use. | Runtime section |
| runtime memory size | Metric | Memory consumed during execution, potentially larger than model-file size. | Runtime note |
| workload | Workload concept | The particular inference conditions that determine runtime memory needs. | “one workload and fail in another” |
| workload variation | Mechanism | Different context, cache, temporary-data, or overhead conditions change memory needs. | Practical example |
| workload-dependent memory | Metric / caveat | Memory usage varies with the workload rather than only with model-file size. | Runtime note |
| fit in one workload | Capacity outcome | A model can fit under one set of runtime conditions. | Practical example |
| fail in another workload | Capacity outcome | The same model can fail under different runtime conditions. | Practical example |
| memory pressure | Runtime condition | High memory demand that can prevent successful execution. | Candidate implied by fit/fail behavior |
| out-of-memory | Failure mode | Runtime failure when the total requirement exceeds available memory. | Candidate implied by “fail” |
| OOM | Abbreviation / failure mode | Short form for out-of-memory. | Abbreviation candidate for runtime failure |
| capacity planning | Operational concept | Comparing total runtime requirements with available compute and memory. | Candidate implied by practical example |
| memory budgeting | Operational concept | Allocating memory across weights, cache, context, temporary data, and overhead. | Candidate implied by memory formula |
| quantization | Model representation technique | Reduces numerical precision to make the representation more compact and reduce weight memory. | Quantization connection |
| model quantization | Alias / technique | Quantization applied to model weights/representation. | Related concept; quantization flow |
| quantized model | Model representation | A model stored or executed with a lower-precision representation. | Related concept candidate |
| precision | Representation property | Numerical precision used for weights; higher precision uses more bytes. | Quantization flow |
| higher precision model | Model representation | A representation whose weights use more bytes. | Quantization flow |
| high precision | Alias / representation property | Higher numerical precision and larger weight storage. | Quantization flow |
| lower precision | Representation property | Reduced precision used to make the representation more compact. | Quantization flow |
| low precision | Alias / representation property | Lower numerical precision with smaller weight representation. | Quantization flow |
| representation | Model representation | The numerical form in which model weights are stored or used. | Quantization flow |
| numerical representation | Model representation | Precision-dependent representation of model values. | Quantization flow |
| compact representation | Model representation | A smaller representation produced by lower precision. | Quantization flow |
| model representation becomes more compact | Mechanism | Quantization reduces representation size. | Quantization flow |
| bytes | Storage unit | Units used to describe how much memory weights use. | “Weights use more bytes” |
| weight bytes | Storage metric | Number of bytes required to store model weights. | Quantization flow |
| memory reduction | Effect | Decrease in weight-memory requirement from a more compact representation. | Quantization connection |
| lower weight memory | Effect | Lower memory use for weights after quantization. | Quantization flow |
| runtime still matters | Caveat | Quantization does not remove KV-cache and overhead requirements. | Quantization flow |
| KV cache remains | Caveat | KV-cache memory is still required after quantization. | Quantization flow |
| overhead remains | Caveat | Runtime overhead is still present after quantization. | Quantization flow |
| quantization flow | Process | Higher precision model → quantization/lower precision → runtime with remaining working-memory needs. | Connection to quantization |
| higher precision → lower precision | Transformation | The visible precision-reduction step in the page’s flow. | Quantization flow |
| model loading and runtime | Process stages | Stored weights must be made available and then executed with working memory. | Candidate workflow framing |
| execution | Process | Performing the calculations required to run the model. | Runtime and GPU descriptions |
| calculation | Operation | Individual computational work done by the GPU/processor. | Worker analogy |
| hardware fit | Capacity outcome | Whether the selected hardware can support the full workload. | Architecture and example |
| inference performance | Performance concept | Performance outcome related to GPU, memory, runtime constraints, and workload. | Related-concept tree |
| performance | Metric family | Broad outcome affected by available compute and memory. | Related-concept tree |
| latency | Performance metric | Time delay for inference; linked as a related concept but not defined on this page. | Related-concept chip |
| tokens per second | Performance metric | Rate of generated tokens; linked as a related concept but not defined on this page. | Related-concept chip |
| Tokens per Second | Title-case label | Page-title form of the tokens-per-second related concept. | Related-concept chip |
| TPS | Abbreviation | Common abbreviation for tokens per second; not expanded on this page. | Abbreviation candidate from related topic |
| runtime constraints | Constraint concept | Limits imposed by memory, compute, caches, context, and overhead. | Related-concept tree |
| Runtime Constraints | Title-case label | Related-topic title for execution limits. | Related-concept chip |
| model serving | Related architecture concept | Operational context in which hardware resources run model inference. | Module breadcrumb and back link |
| local AI | Related domain | Local execution setting for model workloads. | Module breadcrumb |
| model serving and local AI | Module phrase | Module context for GPU, memory, and runtime resource concepts. | Eyebrow and title metadata |
| resource picture | Architecture phrase | Combined view of compute and memory resources. | Hero paragraph |
| architecture | Structure concept | Organization of CPU, GPU, RAM, VRAM, and shared pools. | On-page navigation; architecture section |
| traditional PC vs unified memory system | Comparison | The page’s central hardware-organization comparison. | Architecture cards |
| system | Hardware context | The complete computer arrangement supplying compute and memory. | Unified-memory architecture |
| shared pool vs separate pools | Comparison | Distinction between unified memory and dedicated-VRAM architecture. | Hardware comparison |
| dedicated VRAM architecture | Architecture | CPU/system RAM and GPU/dedicated VRAM are separate. | Traditional PC and comparison |
| unified memory system | Architecture | CPU and GPU use a common memory pool. | Architecture card |
| practical example | Teaching mechanism | A 16 GB VRAM / 13 GB weights scenario showing that file size alone is insufficient. | “One practical example” |
| Computer A | Example system | Hypothetical system with 16 GB VRAM. | Practical example |
| available | Capacity label | Amount of resource presented as available to Computer A. | “Available: 16 GB VRAM” |
| question: does it fit? | Decision question | Capacity check that must include runtime memory, not weights alone. | Practical example |
| answer: not automatically | Capacity caveat | A model-file/VRAM comparison alone cannot establish successful execution. | Practical example |
| memory pool label | Naming caveat | Equal numeric labels for unified memory and VRAM do not imply equal architecture or behavior. | “24 GB” comparison |
| “24 GB unified memory” | Example label | Shared-memory capacity label on a Mac. | Hardware comparison |
| “24 GB VRAM” | Example label | Dedicated-GPU-memory capacity label on a PC. | Hardware comparison |
| not identical | Comparison caveat | Equal capacity numbers across architectures do not mean equivalent resources. | Hardware comparison |
| related concepts | Navigation concept | Connected topics: Model Size, Quantization, GPU / VRAM / Unified Memory, Runtime Constraints, Inference Performance. | Related concepts section |
| Model Size | Related topic label | Linked concept upstream of quantization and hardware resources. | Concept tree |
| Quantization | Related topic label | Linked representation technique. | Related chip |
| GPU / VRAM / Unified Memory | Topic label | Combined topic label in the concept tree. | Related concept tree |
| Runtime Constraints | Related topic label | Linked downstream concept. | Related chip |
| Inference Performance | Related topic label | Performance outcome downstream of runtime constraints. | Concept tree |
| concept tree | Navigation structure | Sequence connecting model size, quantization, hardware memory, runtime constraints, and performance. | Related concepts |
| explore next | Navigation prompt | Prompt above links to neighboring topics. | Related concepts section |
| remember this | Takeaway label | Summary section emphasizing compute, dedicated memory, and shared memory. | Takeaway section |
| visual explainer | Media label | Label for the video placeholder. | Video card |
| video coming soon | Placeholder state | No technical content is supplied by the video section. | Video caption |

## Potential Missing Concepts

These are intentionally retained as follow-up candidates because they are relevant to the topic or implied by the page, but are not fully defined in the visible source body:

- CUDA, CUDA cores, Tensor Cores, GPU kernel, kernel launch, accelerator, NPU, TPU, integrated GPU, discrete GPU bandwidth, memory bandwidth, PCIe, device transfer, host memory, device memory, pinned memory, zero-copy memory, memory mapping, offloading, CPU offload, GPU offload, multi-GPU, GPU partitioning, sharding, tensor parallelism, pipeline parallelism, distributed memory.
- FP32, FP16, BF16, FP8, INT8, INT4, bytes per parameter, parameter count, quantization-aware training, post-training quantization, dequantization, mixed precision, weight-only quantization, activation quantization.
- attention, attention keys, attention values, sequence length, batch size, batch dimension, prompt processing, prefill, decode, autoregressive generation, generation step, cache growth, cache eviction, cache sharing.
- memory bandwidth, bandwidth-bound workload, compute-bound workload, FLOPS, TOPS, utilization, occupancy, throughput, latency, time to first token, inter-token latency, tokens per second, tail latency.
- operating-system memory, process memory, allocator, fragmentation, reserved memory, free memory, memory reclamation, swap, paging, unified virtual memory, virtual address space, memory reservation, runtime allocator.
- model loader, runtime engine, kernel implementation, backend, driver, framework, model format, checkpoint, safetensors, GGUF, CUDA runtime, Metal, Core ML, Apple GPU, Vulkan, ROCm.
- out-of-memory error, memory allocation failure, fallback, CPU execution, degraded performance, thermal throttling, power limit, clock speed, hardware compatibility, benchmark, profiling, monitoring.

## Aliases / Synonyms

Keep these as separate raw candidates until the later glossary pass decides whether to merge them:

| Candidate | Possible alias/synonym relationship |
|---|---|
| GPU | Graphics Processing Unit; graphics processor; compute engine; worker |
| compute | GPU compute; compute capacity; processing capacity; calculation capacity |
| parallel computation | highly parallel computation; parallel processing |
| CPU | Central Processing Unit; central processor |
| system RAM | RAM; main memory; CPU memory |
| VRAM | Video Random-Access Memory; video memory; dedicated GPU memory; dedicated VRAM |
| dedicated VRAM | dedicated GPU memory; discrete GPU memory; video memory |
| GPU memory | VRAM; dedicated GPU memory; shared GPU-accessible memory, depending on architecture |
| Unified Memory | unified memory; unified-memory architecture; shared memory; shared CPU/GPU memory |
| shared memory pool | one shared pool; unified memory pool; CPU/GPU shared pool |
| discrete GPU | discrete graphics; separate GPU; dedicated GPU |
| memory | memory resource; memory capacity; available memory; working memory, depending on context |
| working memory | runtime memory; runtime working set; inference working memory |
| runtime memory | working memory; runtime footprint; execution memory |
| runtime overhead | overhead; execution overhead; runtime extra memory |
| model weights | weights; stored model weights; weight data |
| weight memory | model-weight memory; memory for weights; weight storage |
| model file | model artifact; stored model representation; weight file, depending on format |
| KV cache | key-value cache; KV-cache memory; attention cache |
| context-related memory | context memory; context-window memory; sequence-related memory |
| temporary data | temporary memory; scratch data; intermediate data |
| activations | activation memory; intermediate values; intermediate activations |
| quantization | model quantization; precision reduction; lower-precision representation |
| higher precision model | high-precision model; higher-precision representation |
| lower precision | low precision; reduced precision; compact representation |
| model size | model-file size; weight size; stored model size |
| runtime requirement | runtime memory requirement; working-memory requirement; execution requirement |
| memory fit | model fit; capacity fit; workload fit |
| out-of-memory | OOM; memory exhaustion; memory allocation failure |
| tokens per second | Tokens per Second; TPS; token generation rate |
| runtime constraints | execution constraints; hardware constraints; memory constraints |
| model serving | serving; local model execution; local AI serving |

## Do Not Confuse Candidates

| Candidate A | Candidate B | Distinction suggested by the page |
|---|---|---|
| GPU | VRAM | GPU is the processor doing calculations; VRAM is memory available to a discrete GPU. |
| GPU | compute | GPU is hardware; compute is the processing capability/work performed by that hardware. |
| GPU | worker | Worker is the page’s analogy for the GPU, not a separate hardware component. |
| VRAM | workbench | Workbench is the analogy for VRAM; VRAM is actual GPU memory. |
| VRAM | system RAM | VRAM is directly available to a discrete GPU; system RAM is main memory in the traditional PC layout. |
| dedicated VRAM | Unified Memory | Dedicated VRAM is separate GPU memory; unified memory is a shared CPU/GPU pool. |
| GPU memory | VRAM | GPU memory can be a broad term; VRAM specifically names memory directly available to a discrete GPU. |
| 24 GB unified memory | 24 GB VRAM | Equal numeric capacities are not architecturally identical because one is shared and one is dedicated. |
| unified memory | shared memory pool | Unified memory is the architecture; shared memory pool is the pool used by CPU and GPU within that architecture. |
| CPU | GPU | CPU and GPU are different processor types; the page contrasts their memory arrangements and roles. |
| CPU + GPU | GPU | CPU + GPU names the pair sharing a pool; GPU alone is the parallel compute processor. |
| model file | model weights | A model file is the stored artifact; weights are the learned numeric content represented by it. |
| model file size | runtime memory size | File size mainly describes stored weights; runtime size adds KV cache, context memory, temporary data, and overhead. |
| model weights | runtime data | Weights are persistent model representation; runtime data is active execution state. |
| memory capacity | memory usage | Capacity is available room; usage is the amount consumed by the workload. |
| working memory | model weights | Working memory supports execution; weights are only one component of the total requirement. |
| runtime memory | VRAM capacity | Runtime memory is a workload requirement; VRAM capacity is one possible hardware limit. |
| KV cache | model weights | KV cache is runtime state that grows/varies with context and generation; weights are model parameters. |
| KV cache | context window | KV cache consumes memory as a runtime structure; context window is a context capacity/parameter. |
| context-related memory | temporary data | Context-related memory reflects context; temporary data is a broader short-lived execution category. |
| activations | KV cache | Activations are intermediate model values; KV cache retains attention-related values for generation. |
| temporary data | runtime overhead | Temporary data is one working-memory component; overhead is additional runtime memory. |
| runtime overhead | model overhead | Runtime overhead belongs to the execution environment, not necessarily to the stored model artifact. |
| quantization | compression | Quantization changes numerical precision/representation; generic compression may use different mechanisms. |
| quantization | pruning | Quantization reduces precision; pruning removes or sparsifies parameters. |
| higher precision | lower precision | Higher precision uses more bytes; lower precision makes the representation more compact. |
| lower precision | no runtime memory | Lower precision reduces weight representation size but does not remove KV cache or overhead. |
| bytes | parameters | Bytes measure storage; parameters are learned model values. |
| model fit | memory fit | Model fit is the outcome for the full workload; memory fit focuses on whether the required memory fits. |
| fit in one workload | fit in every workload | A model may fit under one workload and fail under another. |
| out-of-memory | slow inference | OOM is a capacity failure; slow inference is a performance outcome and may occur without OOM. |
| inference | inference performance | Inference is the execution operation; inference performance is how efficiently it runs. |
| latency | tokens per second | Latency is delay/time; tokens per second is a generation-rate metric. Both are linked but not defined in detail here. |
| tokens per second | throughput | TPS is a token-rate measure; throughput is a broader workload-rate concept. |
| Runtime Constraints | GPU / VRAM / Unified Memory | Runtime constraints are downstream limits; GPU/VRAM/unified memory are hardware/resource concepts contributing to them. |
| Model Size | VRAM capacity | Model size describes the model representation; VRAM capacity describes available dedicated memory. |
| model serving | GPU | Model serving is the operational context; GPU is one hardware resource used by it. |
| Apple Silicon | unified memory | Apple Silicon is a hardware example; unified memory is the architecture/property. |
| Mac | PC | Mac/Apple Silicon is the page’s unified-memory example; traditional PC is the separate-memory comparison. |
| architecture | capacity | Architecture describes organization; capacity describes how much resource is available. |
| hardware | runtime | Hardware supplies compute and memory; runtime uses those resources to execute the model. |
| compute | memory | Compute performs calculations; memory holds weights and runtime data. |
| memory pool | memory capacity | A pool is an organization/container; capacity is its amount. |
| GPU = worker | VRAM = workbench | These are paired analogies, not literal definitions of hardware components. |

## Notes

- The page is introductory and hardware/resource-oriented. It defines the relationship between compute, memory architecture, stored weights, and runtime memory more strongly than it defines implementation APIs or benchmarks.
- The central architecture comparison is: **Traditional PC: CPU → System RAM, GPU → Dedicated VRAM** versus **Unified Memory System: CPU + GPU → Shared memory pool**.
- The practical rule is: a model needs enough **compute** and enough **memory** to run; the architecture changes how the memory is organized, not the need to account for resources.
- The page’s analogy is: **GPU = worker** (the compute engine doing calculations) and **VRAM = workbench** (the memory available to that worker).
- The page explicitly says VRAM can hold **model weights, KV cache, temporary data, activations, and other inference working data**.
- The page’s runtime-memory decomposition is: **model weights + KV cache + context-related memory + temporary data + runtime overhead**.
- A model file mainly represents stored model weights. Running the model requires working memory as well, so a 13 GB model file may require more than 13 GB while running.
- The page explicitly rejects a universal fixed multiplier between model-file size and runtime memory; requirements depend on the model and workload.
- The Computer A example uses **16 GB VRAM** and **13 GB of weights**. The answer is “not automatically” because KV cache, context, temporary data, and overhead also consume memory.
- The same model may fit in one workload and fail in another. This is retained as a key workload-dependence concept rather than flattened into a simple model-size rule.
- The quantization flow is: **higher precision model → more memory → quantization/lower precision → more compact representation → runtime still needs KV cache and overhead**.
- Quantization reduces the representation/weight-memory side of the problem; it does not eliminate runtime memory requirements.
- The visible related-concept chain is: **Model Size → Quantization → GPU / VRAM / Unified Memory → Runtime Constraints → Inference Performance**.
- Related links include Quantization, Context Window, KV Cache, Runtime Constraints, Latency, and Tokens per Second. Their names are retained even where this page does not define them fully.
- The video area says “Video coming soon” and contributes no additional technical definition.
- Repeated labels, case variants, explicit examples, analogy terms, broad body words, and potential alias/confusion pairs are intentionally preserved for the later glossary-normalization pass.
