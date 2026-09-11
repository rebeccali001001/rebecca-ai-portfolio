# Topic

Runtime Constraints

## Topic Metadata

- Module: 10 · Model Serving & Local AI
- Topic: Runtime Constraints
- Source File: `runtime-constraints.html`
- Page Title: What are Runtime Constraints?
- Source Eyebrow: 07 · Model Serving & Local AI · Topic 05
- Source Type: Beginner explainer topic page with definition, analogy, process flow, examples, contrasts, related concepts, and video metadata
- Collection Policy: Maximal raw candidate collection; overlapping, repeated, broad, and potentially non-glossary items are intentionally retained for later review.

## Glossary Candidates

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Runtime Constraints | 运行时约束 | Limits that shape how an AI system can run in practice. | AI 系统真正运行时受到的各种限制。 |
| runtime constraint | 运行时约束 | A limit on how a system operates while running. | 系统运行过程中不能超出的条件。 |
| runtime | 运行时 | The period and environment in which software is executing. | 程序实际跑起来的时间和环境。 |
| constraint | 约束；限制 | A condition that limits available choices or behavior. | 会限制选择或做法的条件。 |
| limit | 限制 | A boundary on an amount, capability, or behavior. | 某件事最多能做到的边界。 |
| AI system | AI 系统；人工智能系统 | A system that uses AI models or methods to produce results. | 用 AI 模型或方法处理事情的一整套系统。 |
| system | 系统 | Connected parts that work together for a purpose. | 多个部分配合完成任务的整体。 |
| resources | 资源 | Things such as memory, compute, time, and money available to a system. | 系统可以使用的内存、计算力、时间和钱等。 |
| available resources | 可用资源 | Resources that the current environment can provide. | 当前环境实际能拿出来使用的资源。 |
| time | 时间 | A runtime resource or deadline available for work. | 系统可以花费或必须遵守的时间。 |
| cost | 成本 | Money or resource usage required to operate a system. | 运行系统需要付出的钱或资源代价。 |
| environment | 环境 | The hardware, software, network, and operating conditions around a system. | 系统运行所在的硬件、软件、网络和条件。 |
| current environment | 当前环境 | The environment available at a particular deployment or execution point. | 这次部署或运行时实际拥有的环境。 |
| running | 运行中 | Currently executing or serving work. | 程序正在实际工作。 |
| memory | 内存 | Fast storage used to hold model data and active work. | 运行模型时临时放模型和数据的空间。 |
| available memory | 可用内存 | Memory that the model and workload can actually use. | 当前设备真正能给模型使用的内存。 |
| limited memory | 内存受限 | A condition where available memory is small relative to the workload. | 可用内存不够大，模型或任务容易放不下。 |
| compute | 计算资源；算力 | Processing capacity used to perform computation. | 模型执行计算时可用的处理能力。 |
| power | 功耗；电力 | Electrical energy or power available for operating a system. | 设备运行时能用的电力或消耗的电量。 |
| network access | 网络访问 | Ability to reach network services or data. | 系统能不能连接网络和外部服务。 |
| network | 网络 | Connectivity used to communicate with other systems. | 设备与外部服务通信的连接。 |
| concurrency | 并发 | Number of tasks or requests handled at the same time. | 同一时间一起处理多少任务或请求。 |
| deployment location | 部署位置 | Where a model or system is run. | 模型或系统实际放在哪里运行。 |
| local | 本地 | Running on the user’s device or nearby controlled hardware. | 在自己的电脑、手机或本地服务器上运行。 |
| local AI | 本地 AI | AI that runs on a local device or local environment. | 不完全依赖远程服务、在本地设备上运行的 AI。 |
| device | 设备 | Hardware on which a model or system can run. | 承载模型运行的电脑、手机或其他硬件。 |
| model choice | 模型选择 | Selecting a model that fits the task and constraints. | 根据任务和限制挑一个合适的模型。 |
| choose a model | 选择模型 | Pick a model for a workload. | 为任务挑选一个模型。 |
| select a model | 选择模型 | Choose a model from available options. | 从可用模型中选一个。 |
| model | 模型 | A learned computational mechanism that maps inputs to outputs. | 根据输入产生输出的已训练程序或结构。 |
| system design | 系统设计 | Planning how components work together under requirements and limits. | 设计整个系统怎样组合、怎样运行。 |
| design decision | 设计决策 | A choice about how a system should be built or operated. | 关于系统该怎么搭建和运行的选择。 |
| real system | 真实系统 | An implemented system operating in an actual environment. | 真正部署并给人使用的系统。 |
| available | 可用的 | Ready and possible to use in the current situation. | 当前条件下确实能使用的。 |
| fit the limits | 符合限制 | Stay within the available technical boundaries. | 不超过现有资源和条件。 |
| fit available memory | 放进可用内存 | Be small enough to load and run in available memory. | 模型大小不超过设备能提供的内存。 |
| workload | 工作负载 | The amount and type of work given to a system. | 系统一次或持续要处理的任务量和任务类型。 |
| context | 上下文 | Information supplied around a request for the model to use. | 附在问题周围、帮助模型理解的背景信息。 |
| context window | 上下文窗口 | The maximum context a model can handle in one interaction. | 模型一次能接收的上下文总量上限。 |
| token | 词元；令牌 | A small unit of text processed by a language model. | 语言模型处理文字时使用的小单位。 |
| token limit | 词元限制 | A cap on how many tokens can be accepted or produced. | 一次能处理或生成的文字单位数量上限。 |
| token budget | 词元预算 | A planned token allowance for a request or workload. | 给一次请求分配的文字单位额度。 |
| batch size | 批大小 | Number of inputs processed together in one batch. | 一次打包处理多少条输入。 |
| request | 请求 | A call asking a system to perform work. | 用户或程序要求系统完成的一次调用。 |
| input | 输入 | Information sent into a model or system. | 送进模型或系统的信息。 |
| output | 输出 | The result returned by a model or system. | 模型或系统返回的结果。 |
| result | 结果 | What the system produces after processing. | 系统处理后得到的东西。 |
| latency | 延迟 | Time between a request and the corresponding response. | 从发出请求到收到回应所花的时间。 |
| strict latency limit | 严格延迟限制 | A hard maximum response time for a workflow. | 工作流程要求响应不能超过的时间上限。 |
| response time | 响应时间 | Time taken to return a response. | 系统返回回答所需的时间。 |
| response-time target | 响应时间目标 | A desired or required response time. | 希望系统达到的响应速度目标。 |
| speed | 速度 | How quickly a system processes work or returns results. | 系统处理任务和返回结果有多快。 |
| tokens per second | 每秒词元数 | Number of tokens processed or generated per second. | 一秒钟能处理或生成多少词元。 |
| throughput | 吞吐量 | Amount of work completed per unit of time. | 单位时间内系统能完成多少工作。 |
| quality | 质量 | How useful, accurate, or acceptable a result is. | 结果是否有用、准确、符合要求。 |
| model quality | 模型质量 | How useful or accurate a model’s results are. | 模型输出有多好、多准确。 |
| useful | 有用的 | Helpful for the intended user or task. | 对任务或用户确实有帮助。 |
| accurate | 准确的 | Close to the correct or intended result. | 和正确答案或真实情况接近。 |
| service target | 服务目标 | A performance or quality level a service is expected to meet. | 服务必须达到的速度、质量或可靠性标准。 |
| access needs | 访问需求 | The access a workload needs to data, services, or networks. | 任务需要访问哪些数据、服务或网络。 |
| operating limit | 运行上限；操作限制 | A technical boundary on how a system may operate. | 系统技术上能运行到的边界。 |
| technical operating limit | 技术运行限制 | A limit imposed by the operating setup rather than by user preference. | 由技术环境决定的运行边界。 |
| product requirement | 产品需求 | A user or business need that a product should satisfy. | 用户或业务希望产品做到的事情。 |
| user need | 用户需求 | A need or outcome important to the user. | 用户真正想解决的问题或想得到的结果。 |
| business need | 业务需求 | A need arising from an organization’s goals or workflow. | 企业流程、目标或经营上的需要。 |
| permanent rule | 永久规则 | A rule intended not to change with available resources. | 不随当前资源变化而改变的固定规则。 |
| rule | 规则 | An explicit condition governing behavior. | 预先规定系统该怎么做的条件。 |
| resource-dependent | 依赖资源的 | Changing when available resources change. | 资源变了，结果或可行做法也会变。 |
| hardware | 硬件 | Physical equipment used to run a system. | 电脑、手机、芯片等看得见的设备。 |
| hardware constraint | 硬件约束 | A limit imposed by the physical device. | 设备本身的内存、算力或功耗限制。 |
| software environment | 软件环境 | Operating system, runtime, libraries, and services around the model. | 模型运行依赖的操作系统、程序库和服务。 |
| network constraint | 网络约束 | A limit on connectivity, bandwidth, or reachability. | 网络连接、速度或可访问范围的限制。 |
| deployment | 部署 | Putting a model or system into an environment where it runs. | 把模型或系统放到实际环境里运行。 |
| deployment environment | 部署环境 | The specific hardware and software setup used for deployment. | 模型上线时依赖的具体软硬件条件。 |
| model serving | 模型服务 | Operating a model so it can answer prediction requests. | 让模型在线接收请求并返回结果。 |
| serving | 提供服务；服务化 | Making a model available to applications or users. | 把模型包装成别人可以调用的服务。 |
| inference | 推理 | Applying a trained model to new input. | 用已经训练好的模型处理新输入。 |
| inference workload | 推理工作负载 | The requests and computation handled during inference. | 模型实际回答请求时承担的任务量。 |
| inference request | 推理请求 | A request for a model to produce an output. | 要求模型生成一次结果的请求。 |
| runtime environment | 运行时环境 | The environment in which inference or serving executes. | 模型实际执行推理的环境。 |
| model runtime | 模型运行时 | Software and settings used to execute a model. | 负责让模型跑起来的软件和配置。 |
| workload configuration | 工作负载配置 | Settings controlling how a workload is executed. | 控制任务怎样运行的一组设置。 |
| configure | 配置 | Set operational options for a system. | 调整系统运行所需的选项。 |
| configuration | 配置 | Selected settings that control system behavior. | 决定系统怎么工作的设置。 |
| control context | 控制上下文 | Limit or shape the context sent to a model. | 控制交给模型的背景信息量和内容。 |
| control batch size | 控制批大小 | Choose how many inputs are processed together. | 调整一次同时处理几条输入。 |
| control concurrency | 控制并发 | Choose how many tasks run simultaneously. | 调整同一时间并行处理多少任务。 |
| measure | 测量 | Collect values describing limits or behavior. | 用数据记录资源和运行表现。 |
| measurement | 测量；测量结果 | An observed value or the act of collecting it. | 观察并记录下来的数值或过程。 |
| list the limits | 列出限制 | Identify the boundaries the system must obey. | 先把所有不能超过的条件列出来。 |
| record | 记录 | Write down observed requirements or measurements. | 把需求和测量结果保存下来。 |
| match | 匹配 | Make a model and runtime align with constraints. | 让模型和运行环境彼此合适。 |
| match a model to constraints | 让模型匹配约束 | Select a model that fits the available conditions. | 按实际限制挑选能运行的模型。 |
| choose | 选择 | Pick one option from alternatives. | 在多个方案中挑一个。 |
| test | 测试 | Run checks to observe whether the design works. | 实际试跑，看看系统是否达到要求。 |
| real behavior | 真实表现 | What the system actually does during execution. | 系统真正跑起来时表现出来的情况。 |
| adjust | 调整 | Change the design or settings in response to measurements. | 根据测试结果修改方案或配置。 |
| change the design | 改变设计 | Modify how the system is structured or operated. | 重新安排系统的组成或运行方式。 |
| reduce work | 减少工作量 | Lower the computation or amount of work required. | 让系统少处理一些内容或任务。 |
| fallback | 备用方案；降级路径 | An alternative used when the preferred path cannot meet constraints. | 首选方案不行时临时改用的方案。 |
| fallback model | 备用模型 | A smaller or alternative model used when needed. | 主模型不适用时接替工作的模型。 |
| change the runtime | 更换运行时 | Use a different execution software or environment. | 换一套让模型运行的软件或环境。 |
| workflow | 工作流程 | A sequence of steps that turns input into an outcome. | 从输入到结果的一连串步骤。 |
| support workflow | 客服支持流程 | A workflow that handles support requests and responses. | 处理客户问题和回复的工作流程。 |
| response | 响应；回答 | Output returned after a request. | 系统收到请求后返回的内容。 |
| cooking analogy | 烹饪类比 | An analogy comparing system constraints with a small kitchen. | 用小厨房来比喻资源有限的运行环境。 |
| small kitchen | 小厨房 | The limited environment in the page’s analogy. | 类比中空间和资源有限的厨房。 |
| tools | 工具 | Equipment available for completing work. | 做事情时可以使用的设备或程序。 |
| counter space | 台面空间 | Physical working space available in the analogy. | 厨房里能摆放和操作东西的空间。 |
| ingredients | 食材；原料 | Materials available for making an output in the analogy. | 做出结果所需的原料，类比系统输入和资源。 |
| plan | 计划；方案 | A way of arranging work to fit available conditions. | 根据手头条件安排怎么做的方案。 |
| resource fit | 资源适配 | Degree to which a workload fits available resources. | 任务和现有资源是否匹配。 |
| limited-memory model deployment | 受限内存模型部署 | Running a model when the device cannot hold a larger model. | 设备内存有限时部署能放得下的模型。 |
| oversized model | 过大的模型 | A model too large for the target device or runtime. | 对目标设备来说装不下或跑不动的模型。 |
| smaller model | 更小的模型 | A model requiring fewer resources than another model. | 占用更少资源、比较容易运行的模型。 |
| quantization | 量化 | Representing model values with lower precision to reduce resource use. | 用更省空间的数字表示模型，减少内存和计算需要。 |
| memory footprint | 内存占用 | Amount of memory used by a model or workload. | 模型和任务实际占掉的内存大小。 |
| business example | 业务示例 | An example involving a real business workflow. | 放在企业流程里的具体例子。 |
| response-time requirement | 响应时间要求 | A requirement about how quickly the system must respond. | 要求系统必须在多长时间内回答。 |
| caching | 缓存 | Reusing stored results or data to avoid repeated work. | 把以前算过的结果暂存起来，减少重复计算。 |
| streaming | 流式传输；流式生成 | Sending or producing output progressively instead of all at once. | 结果边生成边传给用户，不必等全部完成。 |
| strict | 严格的 | Leaving little room beyond a required limit. | 几乎不能超出的。 |
| service | 服务 | A running system that accepts requests and returns results. | 持续接收请求并提供结果的程序。 |
| model quality vs runtime constraint | 模型质量与运行时约束 | Result usefulness and operating limits are different dimensions. | 输出好不好与能不能按条件跑起来是两回事。 |
| runtime constraint vs product requirement | 运行时约束与产品需求 | Technical operating limits differ from user or business needs. | 技术限制不等于用户或业务想要的功能。 |
| runtime constraint vs permanent rule | 运行时约束与永久规则 | Runtime limits depend on the current environment; permanent rules do not. | 运行限制会随资源变化，固定规则通常不会。 |
| model quality | 模型质量 | Usefulness or accuracy of a model’s output. | 模型结果是否好用、准确。 |
| product requirement | 产品需求 | A user or business outcome the product should deliver. | 产品需要满足的用户或业务目标。 |
| permanent | 永久的；固定的 | Intended to remain unchanged. | 设计上不会因当前情况改变的。 |
| model serving pipeline | 模型服务流水线 | The path from a request through model execution to a response. | 请求进入模型、执行并返回结果的整条链路。 |
| hardware / network / token budget | 硬件 / 网络 / 词元预算 | Three constraint sources connected to runtime constraints. | 会共同限制模型运行的硬件、网络和文字额度。 |
| quality trade-off | 质量权衡 | Accepting a quality change to satisfy resource or speed limits. | 为了速度、成本或资源而接受一定质量变化。 |
| resource trade-off | 资源权衡 | Balancing memory, compute, time, cost, and quality. | 在内存、算力、时间、成本和质量之间取舍。 |
| latency / cost / quality | 延迟 / 成本 / 质量 | Three outcomes affected by runtime constraints. | 运行限制会同时影响速度、花费和结果好坏。 |
| Ollama | Ollama | A local model-running tool named as a related concept. | 一个可以帮助在本地运行模型的工具名称。 |
| KV Cache | KV 缓存 | Cached key-value attention states used during generation. | 生成文字时暂存注意力计算结果、减少重复计算的缓存。 |
| KV | 键值；Key-Value | Short name for key-value states in attention caching. | KV Cache 中 Key 和 Value 的缩写。 |
| Tokens per Second | 每秒词元数 | A speed measure for token processing or generation. | 衡量每秒能处理或生成多少词元的指标。 |
| AI | 人工智能（AI） | Short name for Artificial Intelligence. | 人工智能的英文缩写。 |
| local deployment | 本地部署 | Running a model on local hardware. | 把模型放在自己的设备或本地服务器上运行。 |
| cloud deployment | 云端部署 | Running a model on remote cloud infrastructure. | 把模型放在远程云服务器上运行。 |
| operating context | 运行上下文 | The complete conditions in which a system executes. | 系统运行时所处的全部条件。 |
| execution | 执行 | The act of carrying out computation or a request. | 系统真正开始处理任务。 |
| capacity | 容量；承载能力 | The maximum work or data a system can handle. | 系统最多能承受多少任务、数据或请求。 |
| constraint-aware design | 约束感知设计 | Designing with runtime limits as first-class inputs. | 从一开始就把运行限制放进设计考虑。 |
| target | 目标 | A required result or operating level. | 希望系统达到的结果或水平。 |
| meet a target | 达到目标 | Achieve the required operating or quality level. | 达到规定的速度、质量或服务标准。 |
| practical | 实际可行的 | Able to work under real operating conditions. | 在真实条件下确实能做到。 |
| in practice | 在实践中 | In actual operation rather than only in theory. | 不是理论上，而是真正运行时。 |
| model-system fit | 模型与系统适配 | How well a model fits the complete operating setup. | 模型是否适合整个运行环境和任务。 |
| operational constraint | 运营约束；运行约束 | A limitation affecting ongoing operation. | 影响系统日常运行的限制。 |
| runtime decision | 运行时决策 | A choice made about how to execute a workload. | 根据当前运行条件决定怎么执行任务。 |
| independent explainer | 独立讲解视频 | A separately provided visual explanation. | 页面里附带的独立视频讲解。 |

## Potential Missing Concepts

- The page defines runtime constraints broadly but does not quantify memory capacity, GPU/CPU compute, VRAM, unified memory, bandwidth, or storage limits.
- The page names latency, speed, tokens per second, and response-time targets but does not distinguish latency from throughput, time to first token, inter-token latency, tail latency, SLA, SLO, or deadline miss.
- The page names cost but does not explain cost per request, token pricing, utilization, amortized hardware cost, energy cost, or cost-quality trade-offs.
- The page names concurrency and batch size but does not cover queueing, batching strategies, dynamic batching, backpressure, rate limits, saturation, autoscaling, or admission control.
- The page mentions memory and quantization but does not explain model size, precision, bit width, activation memory, KV-cache growth, memory bandwidth, offloading, paging, or out-of-memory failure.
- The page names context, token limits, token budget, and Context Window but does not explain tokenization, prompt length, input/output token accounting, truncation, context compaction, or long-context cost.
- The page names network access and deployment location but does not distinguish local, edge, on-premises, private cloud, public cloud, remote API, bandwidth, network latency, offline operation, and data residency.
- The page names model serving and runtime but does not explain serving architecture, inference engine, worker process, request routing, load balancing, replicas, cold start, warm start, health checks, and graceful degradation.
- The page names caching and streaming but does not cover cache hit rate, cache invalidation, prefix caching, response buffering, partial output, cancellation, retries, timeouts, or idempotency.
- The page gives a five-step Measure–Match–Configure–Test–Adjust loop but does not define observability, instrumentation, profiling, benchmark design, representative workload, baseline, regression testing, or capacity planning.
- The page compares runtime constraints with model quality and product requirements but does not explain non-functional requirements, availability, reliability, maintainability, security, privacy, compliance, or safety constraints.
- The page uses a small-kitchen analogy but does not discuss trade-offs between model size, quality, latency, cost, power, portability, and operational complexity.
- The page mentions a fallback but does not explain fallback triggers, model routing, cascading failures, error handling, retry budgets, circuit breakers, or human escalation.
- The page mentions quantization, Ollama, Context Window, KV Cache, and Tokens per Second as related concepts but does not teach their mechanisms or how they interact.
- The page does not explain hardware selection, GPU versus CPU inference, accelerator support, VRAM, memory bandwidth, thermal limits, battery limits, or power-performance trade-offs for local AI.
- The page does not explain how runtime constraints change across development, testing, staging, and production environments.
- The page does not distinguish a hard constraint from a soft target, a requirement from a measured observation, or a constraint from a preference.
- The page does not cover quality evaluation methods, accuracy, task success, user satisfaction, hallucination rate, or quality degradation caused by shorter context or smaller models.
- The page does not explain how to document constraints, set thresholds, alert on violations, monitor drift, or revise constraints as workload and hardware change.

## Aliases / Synonyms

- Runtime Constraints / runtime constraints / runtime limits / operating constraints / 运行时约束 / 运行时限制 / 运行约束
- runtime / runtime environment / model runtime / execution environment / 运行时 / 运行时环境 / 执行环境
- limit / constraint / boundary / cap / limitation / 限制 / 约束 / 上限 / 边界
- resources / available resources / resource budget / 资源 / 可用资源 / 资源预算
- memory / available memory / RAM capacity / memory capacity / 内存 / 可用内存 / 内存容量
- compute / compute capacity / processing capacity / compute budget / 算力 / 计算能力 / 计算预算
- latency / response time / response-time delay / 延迟 / 响应时间
- strict latency limit / response-time target / latency requirement / deadline / 严格延迟限制 / 响应时间目标 / 延迟要求 / 截止时间
- speed / tokens per second / generation speed / token throughput / 速度 / 每秒词元数 / 生成速度 / 词元吞吐量（相关但不完全同义）
- throughput / requests per second / work per unit time / 吞吐量 / 每秒请求数 / 单位时间工作量
- concurrency / simultaneous requests / parallel work / 并发 / 同时请求 / 并行工作
- cost / operating cost / inference cost / serving cost / 成本 / 运行成本 / 推理成本 / 服务成本
- power / power budget / energy use / battery budget / 功耗 / 功率预算 / 能耗 / 电池预算
- network access / connectivity / external access / 网络访问 / 连接能力 / 外部访问
- deployment location / deployment environment / execution location / 部署位置 / 部署环境 / 运行位置
- local AI / local inference / on-device AI / 本地 AI / 本地推理 / 端侧 AI
- model choice / model selection / model matching / 模型选择 / 模型挑选 / 模型匹配
- system design / architecture design / runtime design / 系统设计 / 架构设计 / 运行设计
- workload / inference workload / request load / work volume / 工作负载 / 推理负载 / 请求负载 / 工作量
- context / prompt context / request context / 上下文 / 提示上下文 / 请求上下文
- context window / context limit / context capacity / 上下文窗口 / 上下文限制 / 上下文容量
- token limit / token budget / token cap / token allowance / 词元限制 / 词元预算 / 词元上限 / 词元额度（预算和硬限制不总是同义）
- batch size / batch count / inputs per batch / 批大小 / 每批输入数
- configure / configuration / operational settings / 配置 / 配置项 / 运行设置
- measure / measurement / benchmark / profile / 测量 / 测量结果 / 基准测试 / 性能分析（不完全同义）
- test / runtime test / load test / performance test / 测试 / 运行时测试 / 负载测试 / 性能测试
- adjust / tune / reconfigure / optimize / 调整 / 调参 / 重新配置 / 优化（不完全同义）
- fallback / fallback path / backup path / degradation path / 备用方案 / 备用路径 / 降级路径
- quantization / lower-precision representation / reduced-precision model / 量化 / 低精度表示 / 降精度模型
- caching / result cache / prompt cache / KV cache / 缓存 / 结果缓存 / 提示缓存 / KV 缓存（KV Cache 是一种特定缓存）
- streaming / streamed response / incremental output / 流式传输 / 流式响应 / 增量输出
- model serving / inference serving / prediction service / model service / 模型服务 / 推理服务 / 预测服务 / 模型服务化
- model quality / output quality / result usefulness / result accuracy / 模型质量 / 输出质量 / 结果有用性 / 结果准确性
- product requirement / user requirement / business requirement / 产品需求 / 用户需求 / 业务需求（语境不同）
- permanent rule / fixed rule / invariant rule / 永久规则 / 固定规则 / 不变规则
- smaller model / compact model / lightweight model / 小模型 / 紧凑模型 / 轻量模型
- oversized model / too-large model / model too large for device / 过大模型 / 对设备而言太大的模型
- response / answer / returned result / system output / 响应 / 回答 / 返回结果 / 系统输出
- hardware / device / physical infrastructure / 硬件 / 设备 / 物理基础设施
- Ollama / local model runner / local model tool / Ollama / 本地模型运行工具
- KV Cache / key-value cache / attention-state cache / KV 缓存 / 键值缓存 / 注意力状态缓存
- AI / Artificial Intelligence / 人工智能 / AI

## Do Not Confuse Candidates

- Runtime constraint vs model quality: a runtime constraint limits how the system operates; model quality describes how useful or accurate the result is.
- Runtime constraint vs product requirement: a runtime constraint is a technical operating limit; a product requirement is a user or business need.
- Runtime constraint vs permanent rule: a runtime constraint depends on the current environment and resources; a permanent rule is intended not to change with resources.
- Runtime vs deployment: runtime is the execution period and environment; deployment is the act of placing a system into an environment.
- Runtime environment vs deployment location: the environment includes the conditions and dependencies; the location is where the system runs.
- Resource vs capacity: a resource is something available to use; capacity is the amount the system can handle.
- Memory vs compute: memory holds model data and active work; compute performs the calculations.
- Memory vs memory footprint: memory is the resource; memory footprint is how much of it a model or workload uses.
- Latency vs speed: latency is time for a response or stage; speed is a broader description of how quickly work happens.
- Latency vs throughput: latency concerns one request’s timing; throughput concerns the amount completed over time.
- Response time vs tokens per second: response time covers waiting for a response; tokens per second measures token processing or generation rate.
- Strict latency limit vs response-time target: a strict limit is a hard boundary; a target is a desired or required level that may be tracked as a goal.
- Cost vs power: cost is the money or total resource burden; power is electrical consumption or availability.
- Concurrency vs batch size: concurrency is simultaneous work or requests; batch size is how many inputs are grouped for processing.
- Context vs context window: context is the supplied information; context window is the maximum context capacity.
- Token limit vs token budget: a token limit is a cap; a token budget is an allocation or planning allowance.
- Input vs context: input is all information sent for a request; context is the surrounding information used to inform the model.
- Output vs response: output is any produced result; response is the result returned for a request.
- Model choice vs model quality: choosing a model is a design decision under constraints; quality is an observed property of its results.
- Smaller model vs quantization: a smaller model changes the model itself; quantization changes how model values are represented and stored.
- Quantization vs pruning: quantization lowers numerical precision; pruning removes or sparsifies parts of a model.
- Caching vs streaming: caching reuses stored work; streaming delivers output progressively.
- KV Cache vs general cache: KV Cache stores attention key-value states for generation; a general cache may store arbitrary data or results.
- Model serving vs inference: serving makes a model available as a service; inference is the act of applying the model to input.
- Model serving vs deployment: deployment places a system in an environment; serving handles requests after it is available.
- Local AI vs cloud AI: local AI runs on local hardware; cloud AI runs on remote infrastructure or an API.
- Hardware vs device: hardware is the physical equipment category; device is a particular piece of equipment.
- Network access vs deployment location: network access describes connectivity; deployment location describes where the system runs.
- Product requirement vs technical operating limit: a product requirement expresses desired value; an operating limit expresses what the current setup can support.
- Business need vs runtime constraint: a business need motivates an outcome; a runtime constraint may limit how that outcome is delivered.
- Quality vs accuracy: accuracy is one possible measure; quality is broader and may include usefulness, relevance, and user acceptance.
- Fallback vs optimization: a fallback changes to an alternative path; optimization improves the current path.
- Test vs measure: measurement collects values; testing uses planned checks to determine whether requirements are met.
- Configure vs adjust: configuration sets initial options; adjustment changes them after observing behavior.
- Available resources vs required resources: available resources are what the environment provides; required resources are what the workload needs.
- Runtime constraint vs failure: a constraint is a boundary; failure occurs when the design cannot operate within that boundary.
- Runtime constraint vs trade-off: a constraint limits the solution space; a trade-off is a choice among competing outcomes.
- Model vs model runtime: the model contains learned behavior; the runtime executes it.
- Model runtime vs operating system: the model runtime provides model execution support; the operating system manages the broader device environment.
- Token budget vs financial budget: token budget counts model text units; financial budget limits money.
- Response-time target vs service target: a response-time target covers timing; a service target may include timing, quality, availability, or other dimensions.
- Permanent rule vs configuration: a permanent rule is intended to stay fixed; configuration can change with workload or environment.
- Local deployment vs local-only requirement: local deployment is a placement choice; local-only is a constraint on where execution may occur.

## Notes

- The full body of `runtime-constraints.html` was read, including visible navigation labels, definition, analogy, five process steps, both examples, all three “What it is NOT” comparisons, related-concept chain, related links, takeaway, and video metadata.
- Candidate coverage follows the page’s wording: resources, time, cost, environment, memory, compute, latency, token limits, power, network access, concurrency, deployment location, model choice, system design, context, batch size, speed, quality, caching, streaming, fallback, quantization, and service target.
- Process candidates are intentionally retained: Measure, Match, Configure, Test, Adjust; list the limits; choose a model; set the workload; measure real behavior; change the design.
- Example candidates are intentionally retained: local AI, limited memory, oversized model, device, quantization, smaller model, support workflow, strict latency limit, caching, streaming, and response-time target.
- The source page uses `KV Cache`, `Context Window`, `Ollama`, `Latency`, `Cost`, `Quality`, and `Tokens per Second` as related concepts; these remain candidates even where the page does not define their full mechanisms.
- “Runtime constraint,” “model quality,” “product requirement,” and “permanent rule” are kept as separate candidates because the page explicitly contrasts them.
- “No deduplication” means overlapping wording, abbreviations, broad terms, process labels, aliases, and likely review candidates are retained; later editorial passes may decide which entries become final glossary terms.
- The source is beginner-oriented. Simple English and Chinese explanations are plain-language working descriptions, not a claim that every candidate is fully defined by the page.
- No website files, video files, or GitHub state were modified by this collection pass.
