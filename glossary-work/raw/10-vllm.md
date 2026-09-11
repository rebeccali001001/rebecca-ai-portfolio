# Topic

vLLM

## Module/Topic/Source File

- Module: 10 · Model Serving & Local AI
- Topic: vLLM
- Source File: `vllm.html`
- Page Title: `What Is vLLM? · Model Serving & Local AI`
- Collection mode: Raw glossary candidates; preserve broad coverage, repeated occurrences, aliases, and potentially overlapping wording for later review.

## Glossary Candidates

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| vLLM | vLLM | Software for efficiently serving large language models for inference. | 用来高效运行和提供大语言模型服务的软件。 |
| large language model | 大语言模型 | A language model designed to handle a large amount of language knowledge and text. | 能处理大量语言知识和文字的大型模型。 |
| LLM | 大语言模型（LLM） | Short name for large language model. | 大语言模型的英文缩写。 |
| software | 软件 | Programs that perform tasks on a computer. | 让电脑完成任务的程序。 |
| serving | 服务；提供模型服务 | Making a model available for applications to use. | 把模型运行起来，供应用调用。 |
| model serving | 模型服务；模型部署服务 | The software and process that expose a model to users or applications. | 让应用能够使用模型的一整套运行服务。 |
| inference | 推理；推断 | Using a model to produce a result for an input. | 用已经有的模型处理输入并得到结果。 |
| serving and inference engine | 服务与推理引擎 | Software that runs model inference and coordinates access to it. | 负责运行模型推理并安排调用的软件核心。 |
| inference engine | 推理引擎 | A runtime system that executes a model to generate outputs. | 执行模型计算、产生结果的运行系统。 |
| efficiently | 高效地 | Using resources and time with little waste. | 尽量少浪费时间和计算资源地完成任务。 |
| run a model | 运行模型 | Execute a model so it can process requests. | 启动模型，让它真正处理请求。 |
| running a model | 运行模型 | The act of executing a model. | 模型正在被计算机执行。 |
| application | 应用；应用程序 | A program or service that uses the model. | 调用模型能力的软件或服务。 |
| applications | 应用程序（复数） | Multiple programs or services that use the model. | 多个使用模型的程序或服务。 |
| send a request | 发送请求 | Ask a service to perform a model task. | 向模型服务提出一次任务请求。 |
| request | 请求 | A message asking a system to do something. | 请求系统完成某件事的信息。 |
| model request | 模型请求 | A request that asks a model to generate or return a result. | 要求模型处理输入并返回结果的一次调用。 |
| receive a request | 接收请求 | Accept an incoming call from an application. | 服务收到应用发来的任务。 |
| execute inference | 执行推理 | Perform the calculations needed to produce a model output. | 做出模型输出所需的计算。 |
| manage execution | 管理执行 | Coordinate how model computation is run. | 安排计算什么时候、以什么方式执行。 |
| serving performance | 服务性能 | How well a model service handles requests. | 模型服务处理请求的速度和效率。 |
| GPU | 图形处理器；GPU | Hardware that can perform many parallel computations. | 擅长并行计算、常用于运行 AI 的芯片。 |
| memory | 内存；存储空间 | Space used to hold model data and intermediate computations. | 暂时存放模型和计算数据的空间。 |
| GPU / memory resources | GPU／内存资源 | The available hardware capacity used by model serving. | 运行模型时可以使用的显卡算力和内存空间。 |
| model weights | 模型权重 | Learned numerical values that define a trained model. | 训练后保存在模型里的大量数字。 |
| weights | 权重 | Numerical values learned during training. | 模型学习到的内部数值。 |
| between applications and model weights | 应用与模型权重之间 | The layer that connects callers with the stored model. | 连接应用请求和模型内部数字的中间层。 |
| service | 服务 | A running system that accepts requests and returns results. | 持续运行、可以被调用的系统。 |
| API | 应用程序接口；API | An interface through which applications send requests. | 应用调用另一个程序能力的入口。 |
| application requests | 应用请求 | Requests sent by an application to a service. | 应用发给模型服务的任务信息。 |
| usable interface | 可用接口 | A boundary that applications can call in a practical way. | 应用能够按照约定使用的调用入口。 |
| API access | API 访问 | Accessing model capability through an API. | 通过 API 使用模型能力。 |
| API itself | API 本身 | The access boundary, not the model-serving software behind it. | API 是调用入口，不等于后面的模型服务软件。 |
| access boundary | 访问边界 | The point where an external application connects to a service. | 外部应用进入服务的接口边界。 |
| backend | 后端 | Server-side software that handles application work. | 在服务器一侧处理请求的程序。 |
| web app | 网页应用 | An application accessed through a web interface. | 通过网页使用的应用。 |
| agent | 智能体；代理 | An application that can use a model to reason or act. | 能调用模型完成任务或行动的软件。 |
| application layer | 应用层 | The layer where user-facing programs operate. | 用户或业务程序所在的上层。 |
| model layer | 模型层 | The layer containing the model being executed. | 负责保存和执行模型的层。 |
| runtime | 运行时 | Software environment in which a model executes. | 模型实际运行时所处的软件环境。 |
| model runtime | 模型运行时 | A runtime focused on loading and executing models. | 专门负责加载和运行模型的环境。 |
| model runtime / serving tool | 模型运行时／服务工具 | Software that runs a model and makes it usable. | 既能运行模型又能让应用调用的工具。 |
| tool | 工具 | Software used to accomplish a technical task. | 帮助完成某项工作的程序。 |
| running models | 运行模型（复数） | Executing one or more models. | 启动并执行一个或多个模型。 |
| local AI | 本地 AI | AI that runs on local hardware or a local environment. | 在自己的电脑或本地设备上运行的 AI。 |
| server / production-style inference workload | 服务器／生产式推理工作负载 | Inference work intended for a service used by applications or users. | 面向真实服务和多用户调用的推理任务。 |
| production-style | 生产式；面向生产环境的 | Designed for a real, continuously used service. | 按真实上线服务的要求来设计。 |
| inference workload | 推理工作负载 | The requests and computation handled during inference. | 推理服务需要处理的请求和计算量。 |
| workload | 工作负载 | The amount and kind of work a system must handle. | 系统需要承担的任务数量和类型。 |
| multiple requests | 多个请求 | More than one request arriving at a service. | 同时或先后到达的多次调用。 |
| many users | 多个用户 | Several users who may use the same service. | 共同使用一个服务的许多人。 |
| many applications | 多个应用 | Several programs that call the same model service. | 共同调用同一个模型服务的多个程序。 |
| call a service | 调用服务 | Send a request to a running service. | 向正在运行的服务发出请求。 |
| request coordination | 请求协调 | Organizing multiple incoming requests. | 安排多个请求如何一起被处理。 |
| request scheduling | 请求调度 | Deciding when and how each request is processed. | 决定每个请求何时、以什么顺序处理。 |
| scheduling | 调度 | Assigning available compute time or resources to work. | 把计算机会和资源分配给任务。 |
| incoming work | 到来的工作；待处理任务 | Work represented by requests that have arrived. | 已经到达、等待系统处理的任务。 |
| incoming traffic | 到来的流量 | Requests arriving at a service. | 不断进入服务的请求流。 |
| traffic controller | 交通控制器 | An analogy for software that coordinates many requests. | 用来比喻安排请求流量的控制者。 |
| traffic | 流量；请求流 | The stream of requests reaching a service. | 不断进入系统的请求。 |
| destination | 目的地 | The place a request or process is directed toward. | 请求最终要到达的对象或地方。 |
| engine | 引擎 | A core mechanism that performs a task. | 负责核心计算或工作的部分。 |
| coordinate | 协调 | Organize different pieces of work so they operate together. | 把多个任务安排得互相配合。 |
| handle a request | 处理请求 | Perform the work needed to answer a request. | 完成一次请求所需要的处理。 |
| request handling | 请求处理 | The process of receiving and completing requests. | 从收到请求到返回结果的过程。 |
| efficient request handling | 高效请求处理 | Handling requests while minimizing wasted time and resources. | 少浪费资源、快速处理请求。 |
| efficient memory use | 高效内存使用 | Using available memory with limited waste. | 尽量充分利用内存、减少浪费。 |
| available resources | 可用资源 | Hardware capacity currently available to the system. | 系统此时能使用的硬件能力。 |
| fit available resources | 适配可用资源 | Operate within the hardware capacity that exists. | 在现有硬件容量范围内运行。 |
| resource management | 资源管理 | Allocating hardware resources to model work. | 把硬件资源分给不同计算任务。 |
| execution management | 执行管理 | Controlling how computation is started and progressed. | 管理计算的开始、进行和结束。 |
| batching | 批处理；批量处理 | Handling related requests together as a group. | 把多个请求放在一起处理。 |
| batch | 批次；一批请求 | A group of requests processed together. | 一起处理的一组请求。 |
| related requests | 相关请求 | Requests that can be processed together or share work. | 可以一起处理或共享计算的一组请求。 |
| handle requests together | 一起处理请求 | Process more than one request in one coordinated operation. | 一次安排多个请求共同计算。 |
| high throughput | 高吞吐量 | Completing a large amount of serving work over time. | 单位时间处理很多任务。 |
| throughput | 吞吐量 | How much work a system completes over time. | 一段时间内系统完成的工作量。 |
| serving work | 服务工作量 | The inference work completed by a serving system. | 服务系统实际完成的模型计算量。 |
| over time | 随时间；单位时间内 | Measured across a period rather than one request. | 看一段时间里完成了多少事情。 |
| generation rate | 生成速率 | The rate at which a model produces output tokens. | 模型生成文字单位的速度。 |
| tokens per second | 每秒词元数 | The number of tokens generated in one second. | 一秒钟生成多少个词元。 |
| TPS | 每秒词元数（TPS） | Short form often used for tokens per second. | tokens per second 的常见缩写。 |
| latency | 延迟 | How long a request takes from start to result. | 一次请求从开始到得到结果要等多久。 |
| request latency | 请求延迟 | The time taken by one request. | 一次请求花费的时间。 |
| performance | 性能 | How quickly and efficiently a system handles work. | 系统处理任务的速度和效率。 |
| performance concepts | 性能概念 | Terms used to discuss how a service behaves under work. | 描述服务处理任务表现的一组词。 |
| serving performance | 服务性能 | The speed, capacity, and efficiency of a model-serving system. | 模型服务的速度、承载量和资源效率。 |
| speed | 速度 | How quickly work is completed. | 完成任务有多快。 |
| capacity | 承载能力 | How much work a system can handle. | 系统最多能承担多少任务。 |
| resource efficiency | 资源效率 | How much useful work is obtained from available resources. | 同样资源能完成多少有用计算。 |
| model service | 模型服务 | A running service that provides access to a model. | 把模型能力提供给应用使用的服务。 |
| model-serving software | 模型服务软件 | Software that hosts and exposes a model for inference. | 承载模型并提供推理调用的软件。 |
| serving software | 服务软件 | Software that makes a model available to callers. | 让别人可以调用模型的软件。 |
| inference software | 推理软件 | Software used to execute model inference. | 用来运行模型推理的软件。 |
| API request | API 请求 | A request sent through an API boundary. | 通过 API 入口发出的调用。 |
| service receive | 服务接收 | A service accepting a request from a caller. | 服务收到调用方发来的请求。 |
| execution | 执行 | Carrying out a computation or operation. | 真正把计算或操作做出来。 |
| available GPU | 可用 GPU | GPU capacity that the serving system can use. | 服务当前能够使用的显卡能力。 |
| memory resource | 内存资源 | Memory capacity available for model execution. | 可供模型运行使用的内存空间。 |
| run models | 运行模型（复数） | Execute models so they can produce outputs. | 让模型开始计算并生成结果。 |
| model itself | 模型本身 | The learned model, as distinct from its serving software. | 模型这个被训练出来的东西本身。 |
| vLLM runs models | vLLM 运行模型 | vLLM executes model weights; it is not those weights. | vLLM 负责运行模型，不是模型权重本身。 |
| not the model itself | 不是模型本身 | A serving tool is different from the learned model. | 服务工具和训练出来的模型不是同一个东西。 |
| learned model | 学习得到的模型 | A model whose values were learned from data. | 通过训练学到规律的模型。 |
| language model | 语言模型 | A model that learns patterns in language and text. | 学习文字规律并处理语言的模型。 |
| model family | 模型家族；模型系列 | A group of related model architectures or weights. | 一组相关的模型或权重系列。 |
| model weights family | 模型权重系列 | A group of related learned weight sets. | 一组相关的训练后数字集合。 |
| cloud provider | 云服务提供商 | A company that supplies hosted computing infrastructure. | 提供云端计算和服务器资源的公司。 |
| infrastructure provider | 基础设施提供商 | A provider of hardware or hosted computing infrastructure. | 提供服务器、GPU 等底层资源的服务商。 |
| hosted service | 托管服务 | A service run on infrastructure managed by another party. | 由别的机构提供和维护运行环境的服务。 |
| local model use | 本地模型使用 | Running or calling a model in a local environment. | 在本机或本地环境使用模型。 |
| model management | 模型管理 | Downloading, selecting, configuring, or maintaining models. | 下载、选择、配置和维护模型。 |
| developer-friendly | 对开发者友好 | Easy for developers to install, configure, and use. | 方便开发者上手和调用。 |
| local runtime | 本地运行时 | Software that runs a model on local hardware. | 在本地设备上执行模型的软件环境。 |
| high-throughput LLM serving | 高吞吐量大语言模型服务 | Serving many LLM requests efficiently over time. | 高效处理大量大语言模型请求的服务。 |
| server inference | 服务器推理 | Running model inference as a server process. | 把模型推理作为服务器程序运行。 |
| production inference | 生产环境推理 | Inference used by a real application or service. | 真实上线应用使用的模型推理。 |
| usage pattern | 使用模式 | The way a tool or service is normally used. | 一个工具通常被怎样使用。 |
| optimized | 优化的 | Designed to perform especially well for a target use. | 针对某种用法特别改进过的。 |
| optimized for different usage patterns | 针对不同使用模式优化 | Different tools are designed for different kinds of work. | 不同工具各自适合不同场景。 |
| model serving stack | 模型服务栈 | The layers that connect an application to a running model and hardware. | 从应用到模型、GPU 的一层层技术组合。 |
| serving stack | 服务栈 | A sequence of components used to provide a service. | 共同组成服务的一组上下层组件。 |
| application in the serving stack | 服务栈中的应用 | The top-level program that asks for model work. | 服务栈最上面发起调用的程序。 |
| model serving layer | 模型服务层 | The layer that makes a model available for requests. | 让模型可以被请求调用的中间层。 |
| model layer in stack | 服务栈中的模型层 | The model component executed by the serving layer. | 服务层下面真正被运行的模型。 |
| GPU layer | GPU 层 | Hardware used to accelerate model computation. | 用来加速模型计算的硬件层。 |
| application → API → model serving → vLLM → model → GPU | 应用→API→模型服务→vLLM→模型→GPU | A simplified path from a caller to the hardware running the model. | 应用请求经过 API 和 vLLM，最终由 GPU 执行模型。 |
| application request path | 应用请求路径 | The route a request follows through the serving stack. | 请求从应用到模型执行所经过的路线。 |
| compute resource | 计算资源 | Hardware capacity used to perform computation. | 用来做计算的硬件能力。 |
| hardware capacity | 硬件容量 | The amount of computation or memory hardware can provide. | 硬件能提供多少算力和空间。 |
| request time | 请求时间 | Time associated with processing one request. | 处理一次请求花费的时间。 |
| generation | 生成 | Producing output, often text tokens, from an input. | 根据输入逐步产生输出。 |
| output | 输出 | The result returned by a model or service. | 模型或服务返回的结果。 |
| model output | 模型输出 | The content produced by a model. | 模型计算出来的内容。 |
| result | 结果 | What a system returns after processing. | 系统处理后返回的东西。 |
| performance metric | 性能指标 | A measurable value describing system performance. | 用数字衡量系统表现的量。 |
| metric | 指标 | A value used to measure something. | 用来衡量某件事的数字。 |
| processing time | 处理时间 | Time spent handling a request or computation. | 系统实际处理任务花的时间。 |
| work handled | 已处理工作量 | The amount of work completed by the service. | 服务已经完成的任务量。 |
| high-throughput | 高吞吐量的 | Able to complete a large amount of work over time. | 单位时间能处理很多工作。 |
| serving tool | 服务工具 | A tool used to run and expose a model. | 用来运行并提供模型调用的工具。 |
| local model runtime | 本地模型运行时 | A local environment for executing models. | 在本地执行模型的运行环境。 |
| request scheduler | 请求调度器 | A component that decides when requests run. | 决定请求何时运行的组件。 |
| resource scheduler | 资源调度器 | A component that assigns compute resources to work. | 把计算资源分配给任务的组件。 |
| model request scheduling | 模型请求调度 | Organizing the order and timing of model calls. | 安排模型调用顺序和时间。 |
| memory efficiency | 内存效率 | How effectively available memory is used. | 内存被利用得是否充分。 |
| service throughput | 服务吞吐量 | Amount of service work completed per unit of time. | 单位时间服务完成的工作量。 |
| inference performance | 推理性能 | How quickly and efficiently inference runs. | 模型推理的速度和资源效率。 |
| model access | 模型访问 | The ability of an application to use a model. | 应用能够使用模型的能力。 |
| expose a model | 暴露模型能力；提供模型接口 | Make a model available through a service interface. | 通过服务接口把模型提供给外部调用。 |
| model execution | 模型执行 | The actual computation performed by a model. | 模型真正进行计算的过程。 |
| request result | 请求结果 | The output returned for one request. | 某一次请求得到的返回结果。 |
| application-facing | 面向应用的 | Designed to be called by applications. | 主要给应用程序调用的。 |
| hardware-facing | 面向硬件的 | Connected to the resources that execute computation. | 靠近 GPU、内存等执行计算的硬件。 |
| middleware | 中间件 | Software between an application and a lower-level system. | 位于应用和底层系统之间的软件。 |
| serving middleware | 服务中间件 | Middleware that coordinates application access to a model. | 协调应用调用模型的中间软件。 |
| infrastructure | 基础设施 | The hardware and systems that host computation. | 承载软件和计算的服务器、网络等底层资源。 |
| model infrastructure | 模型基础设施 | Hardware and software used to run model services. | 运行模型服务所需的硬件和软件底座。 |
| model service boundary | 模型服务边界 | The boundary between callers and serving implementation. | 调用方与模型服务内部实现之间的界线。 |
| serving request | 服务请求 | A request sent to a model-serving system. | 发给模型服务的一次调用。 |
| call pattern | 调用模式 | The frequency and grouping of requests. | 请求如何出现、多久一次、是否成批出现。 |
| service usage | 服务使用 | The way applications use a model service. | 应用调用模型服务的方式。 |
| model serving vs model | 模型服务与模型 | Serving software runs a model; the model contains learned behavior. | 服务软件负责运行，模型负责提供学到的能力。 |
| vLLM vs LLM | vLLM 与 LLM | vLLM is serving software; an LLM is a language model. | vLLM 是软件，LLM 是被软件运行的语言模型。 |
| vLLM vs Ollama | vLLM 与 Ollama | Both can run or serve models but suit different patterns. | 两者都能运行模型，但常见适用场景不同。 |
| Ollama | Ollama | A developer-friendly local model runtime and management tool. | 方便本地使用和管理模型的运行工具。 |
| local model runtime and management | 本地模型运行与管理 | Running models locally and handling their local setup. | 在本机运行模型并管理模型配置。 |
| server / production-style inference | 服务器／生产式推理 | Inference arranged as a service for real application traffic. | 面向真实应用流量的服务器推理。 |
| real application traffic | 真实应用流量 | Requests generated by actual applications or users. | 真实用户和应用产生的请求。 |
| developer tool | 开发者工具 | A tool intended to help developers build or test software. | 帮开发者开发、测试和调用模型的软件。 |
| service optimization | 服务优化 | Improvements that make a serving system faster or more resource-efficient. | 让模型服务更快、更省资源的改进。 |
| production workload | 生产工作负载 | Real work handled by an operational service. | 已上线系统实际要处理的任务量。 |
| inference workload pattern | 推理工作负载模式 | The shape and behavior of incoming inference requests. | 推理请求的数量、并发和到达方式。 |
| inference service | 推理服务 | A service that accepts inputs and returns model outputs. | 接收输入并返回模型结果的服务。 |
| serving system | 服务系统 | The complete system that handles model requests. | 负责接收请求、运行模型和返回结果的整体。 |
| serving component | 服务组件 | One part of a model-serving system. | 模型服务整体中的一个组成部分。 |
| model component | 模型组件 | The learned model being executed. | 服务中真正被运行的模型部分。 |
| hardware component | 硬件组件 | A physical resource used by the serving system. | 服务运行时使用的物理硬件。 |
| request coordination layer | 请求协调层 | A layer that organizes requests before model execution. | 在模型计算前安排请求的层。 |
| application-to-model path | 应用到模型路径 | The route from an application request to a model output. | 从应用提出请求到模型返回结果的全过程。 |
| usable model API | 可用的模型 API | An API through which applications can access a running model. | 应用可以实际调用运行中模型的接口。 |
| inference call | 推理调用 | One invocation of a model to get an output. | 让模型处理一次输入的调用。 |
| model call | 模型调用 | An application invocation of a model. | 应用请求模型做一次工作。 |
| output generation | 输出生成 | The process of producing an answer or sequence of tokens. | 模型逐步产出回答的过程。 |
| service request rate | 服务请求速率 | How quickly requests arrive at a service. | 请求进入服务的快慢。 |
| request volume | 请求量 | The number of requests handled or received. | 一段时间内请求的数量。 |
| concurrent requests | 并发请求 | Requests being processed at the same time. | 同时正在处理的多个请求。 |
| request queue | 请求队列 | Waiting requests kept until resources are available. | 资源空闲前排队等待的请求。 |
| queueing | 排队 | Waiting for a system to become ready to process work. | 任务暂时等着，等系统有空处理。 |
| scheduling decision | 调度决定 | A decision about which request gets resources next. | 决定下一个先处理哪个请求。 |
| resource allocation | 资源分配 | Giving available hardware capacity to requests. | 把 GPU 或内存分给请求。 |
| service capacity planning | 服务容量规划 | Planning hardware and capacity for expected request load. | 根据预计请求量准备合适的资源。 |
| efficient serving | 高效服务 | Providing model outputs with good speed and resource use. | 又快又省资源地提供模型结果。 |
| model-serving performance | 模型服务性能 | Measured behavior of a system that serves a model. | 模型服务系统在速度和承载量上的表现。 |
| performance trade-off | 性能权衡 | Improving one performance dimension may affect another. | 提高一个指标可能会影响另一个指标。 |
| latency vs throughput | 延迟与吞吐量 | Latency concerns one request; throughput concerns total work over time. | 延迟看一次请求等多久，吞吐量看一段时间做多少事。 |
| tokens per second vs throughput | 每秒词元数与吞吐量 | Tokens per second measures generation rate; throughput covers overall serving work. | 每秒词元数看生成速度，吞吐量看整体处理量。 |
| GPU / memory | GPU／内存 | Hardware compute and storage resources used during model execution. | 模型运行时用到的显卡算力和内存。 |
| model weights vs GPU memory | 模型权重与 GPU 内存 | Weights are model data; GPU memory is where data and computation may be held. | 权重是模型数据，GPU 内存是放数据和做计算的空间。 |
| model vs model weights | 模型与模型权重 | A model includes the learned structure and values; weights are its learned numbers. | 模型是整体，权重是其中保存规律的数字。 |
| API vs serving engine | API 与服务引擎 | API is the calling boundary; the engine performs serving and inference. | API 是入口，服务引擎负责后面的运行。 |
| serving engine vs cloud provider | 服务引擎与云服务商 | An engine is software; a cloud provider supplies infrastructure. | 引擎是软件，云服务商提供底层服务器资源。 |
| local runtime vs serving engine | 本地运行时与服务引擎 | A local runtime emphasizes local use; a serving engine emphasizes coordinated access and serving. | 本地运行时偏向本机使用，服务引擎偏向统一提供调用。 |
| model runtime vs model | 模型运行时与模型 | Runtime executes the model; model contains learned capability. | 运行时执行模型，模型本身包含学到的能力。 |
| vLLM is software | vLLM 是软件 | vLLM is a software layer used to run and serve models. | vLLM 属于软件，不是硬件或模型家族。 |
| vLLM is not a cloud provider | vLLM 不是云服务商 | vLLM does not itself provide hosted infrastructure. | vLLM 本身不等于提供云服务器的公司。 |
| vLLM is not an API | vLLM 不是 API | vLLM can expose or work behind an API, but it is not identical to the boundary. | vLLM 可以支持接口，但它不等于接口本身。 |
| vLLM is not a model family | vLLM 不是模型家族 | vLLM is not a collection of learned model weights. | vLLM 不是一组模型权重。 |
| vLLM is not an LLM | vLLM 不是大语言模型 | vLLM runs LLMs instead of being one. | vLLM 运行大语言模型，但自己不是大语言模型。 |
| vLLM is a serving and inference engine | vLLM 是服务与推理引擎 | vLLM coordinates requests and executes model inference. | vLLM 安排请求并执行模型推理。 |
| remember this | 记住这一点 | A concise summary of the topic. | 用一句话记住主题核心。 |
| efficient large-language-model serving | 高效大语言模型服务 | Serving LLMs with effective use of time and hardware. | 高效利用时间和硬件来提供大语言模型能力。 |
| independent explainer | 独立讲解 | A separately produced explanation of a topic. | 独立制作的主题说明内容。 |
| video | 视频 | A visual or audio explanation resource. | 用影像或声音解释主题的资源。 |
| no video resource attached | 未附加视频资源 | The page currently has no video attached. | 当前页面没有链接实际视频。 |
| related concepts | 相关概念 | Concepts connected to the topic. | 和 vLLM 互相有关、可以一起学习的概念。 |
| Model Serving | 模型服务 | The broader practice of running models for application access. | 让应用可以调用运行中模型的实践。 |
| Runtime Constraints | 运行时约束 | Limits imposed by hardware or runtime conditions. | GPU、内存、速度等对运行模型形成的限制。 |
| GPU / VRAM | GPU／显存 | GPU hardware and its dedicated memory. | 显卡及其专用内存。 |
| VRAM | 显存 | Memory attached to a GPU. | 显卡上的内存空间。 |
| Quantization | 量化 | A technique that represents model values with fewer or lower-precision numbers. | 用更少或更低精度的数字表示模型，节省资源。 |
| Model Serving & Local AI | 模型服务与本地 AI | The broader topic area containing serving and local model use. | 研究模型如何提供服务以及如何在本地运行的领域。 |
| serving problem | 服务问题 | The practical difficulty of handling real model requests efficiently. | 真实应用调用模型时需要解决的效率和资源问题。 |
| direct model loading | 直接加载模型 | Loading model weights without a separate serving layer. | 直接把模型放进内存运行，不先经过专门服务层。 |
| load the model directly | 直接加载模型 | Put the model into a runtime and run it without extra request coordination. | 把模型装进运行环境后直接执行。 |
| loading weights once | 一次性加载权重 | Loading model weights into memory one time. | 把模型数字加载进内存一次。 |
| real applications | 真实应用 | Applications used for actual tasks by users or systems. | 真的在使用、承担业务任务的应用。 |
| users or applications | 用户或应用 | Human users or software callers that send requests. | 发请求的人或程序。 |
| coordinated work | 协调后的工作 | Work organized so multiple tasks can share execution. | 被安排好、互相配合的一组任务。 |
| incoming request | 到来的请求 | A request that has just reached the service. | 刚刚进入服务、等待处理的请求。 |
| service as a model access point | 作为模型访问点的服务 | A running service that applications use to reach a model. | 应用通过这个服务间接访问模型。 |
| model access interface | 模型访问接口 | An interface for applications to use model capability. | 应用使用模型能力的入口。 |
| execution resource | 执行资源 | Hardware used while executing model computation. | 执行模型计算时占用的硬件资源。 |
| model-serving request | 模型服务请求 | A request sent to software that serves a model. | 发给模型服务软件的一次请求。 |
| request processing | 请求处理 | The steps from accepting a request to returning its result. | 从接收请求到返回结果的一系列步骤。 |
| request completion | 请求完成 | The point when a request has produced its result. | 请求已经产生结果、处理结束的时刻。 |
| service output | 服务输出 | The result returned by the serving layer to an application. | 服务层返回给应用的结果。 |
| inference output | 推理输出 | The result produced by model inference. | 模型推理产生的结果。 |
| computational work | 计算工作 | Processing performed by hardware to generate a result. | 硬件为产生结果实际做的计算。 |
| model execution path | 模型执行路径 | The flow through which a model computation is performed. | 模型从被调用到完成计算的流程。 |
| resource-efficient | 资源高效的 | Producing useful work while using resources carefully. | 在较少浪费资源的情况下完成工作。 |
| throughput-oriented | 面向吞吐量的 | Designed to maximize work completed over time. | 重点是单位时间完成更多任务。 |
| latency-oriented | 面向低延迟的 | Designed to minimize the time for a request. | 重点是让单次请求尽快返回。 |
| API-facing service | 面向 API 的服务 | A service intended to receive calls through an API. | 主要通过 API 接受调用的服务。 |
| model-serving API | 模型服务 API | An API that exposes model-serving capability. | 把模型服务能力提供给应用的接口。 |
| service endpoint | 服务端点 | A network location where a service accepts requests. | 服务接收请求的具体地址或入口。 |
| request interface | 请求接口 | The format and boundary used to submit a request. | 提交请求时遵守的入口和格式。 |
| model endpoint | 模型端点 | An endpoint through which a model can be called. | 可以调用模型的网络入口。 |
| model server | 模型服务器 | A process or machine that serves a model. | 运行模型服务程序的进程或机器。 |
| inference server | 推理服务器 | A server process that performs inference for callers. | 为调用方执行推理的服务器程序。 |
| model service process | 模型服务进程 | A running software process that handles model requests. | 正在运行、负责处理模型请求的软件进程。 |
| service process | 服务进程 | A continuously running process that waits for requests. | 持续运行并等待调用的程序。 |
| model deployment runtime | 模型部署运行时 | The runtime environment in which a deployed model serves requests. | 已上线模型进行服务时所处的运行环境。 |
| serve a language model | 提供语言模型服务 | Make a language model callable by applications. | 让应用可以调用语言模型。 |
| serve LLM requests | 提供 LLM 请求服务 | Handle requests that ask an LLM to generate outputs. | 处理要求大语言模型生成结果的请求。 |
| efficient LLM service | 高效 LLM 服务 | A service that handles LLM requests effectively. | 能高效处理大语言模型调用的服务。 |
| model serving software layer | 模型服务软件层 | The software layer between an application and model execution. | 位于应用和模型计算之间的软件层。 |
| application-to-service connection | 应用到服务连接 | The connection used by an application to reach a service. | 应用连接模型服务的通道。 |
| service-to-model connection | 服务到模型连接 | The relationship by which serving software invokes a model. | 服务软件调用模型的关系。 |
| model-to-GPU execution | 模型到 GPU 执行 | Running model computation on GPU hardware. | 把模型计算交给 GPU 执行。 |
| hardware resource utilization | 硬件资源利用率 | How much available hardware capacity is actively used. | GPU、内存等硬件有多少被真正用上。 |
| memory utilization | 内存利用率 | How much available memory is occupied or used. | 内存空间有多少被使用。 |
| GPU utilization | GPU 利用率 | How much GPU compute capacity is actively used. | GPU 算力有多少被使用。 |
| service efficiency | 服务效率 | Useful serving work relative to time and resources used. | 用多少时间和资源完成了多少有效服务。 |
| request efficiency | 请求效率 | How effectively individual or grouped requests are processed. | 请求被处理得快不快、浪费资源多不多。 |
| inference capacity | 推理承载能力 | How many inference requests a system can handle. | 推理系统能承受多少请求。 |
| workload capacity | 工作负载承载能力 | The volume of work a system can sustain. | 系统可以持续承担的工作量。 |
| serving architecture | 服务架构 | The design of components used to serve a model. | 提供模型服务时各组件如何组织。 |
| application architecture | 应用架构 | The design of an application that calls a model service. | 调用模型服务的应用如何组成。 |
| runtime architecture | 运行时架构 | The design of software that executes the model. | 负责执行模型的运行软件如何组成。 |
| inference pipeline | 推理流水线 | The sequence of stages used to process an inference request. | 推理请求从输入到输出经过的一连串步骤。 |
| serving pipeline | 服务流水线 | The stages from request arrival to returned service result. | 从请求进入到服务返回结果的处理链路。 |
| request lifecycle | 请求生命周期 | The stages a request passes through while being served. | 请求从进入、排队、执行到返回的全过程。 |
| model lifecycle in serving | 服务中的模型生命周期 | Loading, running, and maintaining a model in a service. | 模型在服务中被加载、运行和维护的过程。 |
| operational service | 运营中的服务 | A service running continuously for actual use. | 正在持续运行、供真实使用的服务。 |
| application demand | 应用需求 | The requests and capacity needs generated by applications. | 应用产生的调用和资源需求。 |
| serving demand | 服务需求 | The amount of model-serving work requested. | 外部要求模型服务完成的工作量。 |
| model access demand | 模型访问需求 | The demand for applications to use a model. | 应用想调用模型的需求量。 |
| high request concurrency | 高请求并发 | Many requests being processed at overlapping times. | 很多请求同时或交错进行。 |
| request burst | 请求突发 | A sudden increase in incoming requests. | 短时间内请求突然大量增加。 |
| steady request load | 稳定请求负载 | A relatively consistent stream of requests. | 请求量比较稳定的一段流量。 |
| service reliability | 服务可靠性 | The ability to keep handling requests correctly. | 服务持续正常处理请求的能力。 |
| model-serving reliability | 模型服务可靠性 | The reliability of the system that serves model outputs. | 模型服务持续稳定返回结果的能力。 |
| response | 响应 | The result sent back after a request. | 请求完成后返回给调用方的信息。 |
| response time | 响应时间 | Time from request submission to response. | 从发请求到收到回答要多久。 |
| response generation | 响应生成 | Producing a response from a model input. | 根据输入生成回答。 |
| output token | 输出词元 | A small unit produced during language generation. | 语言模型生成出来的一小段文字单位。 |
| token generation | 词元生成 | Producing text units one after another. | 一个接一个地产生文字单位。 |
| token generation rate | 词元生成速率 | The number of output tokens produced per second. | 每秒生成多少个输出词元。 |
| overall serving work | 整体服务工作量 | All model-serving work completed across requests. | 多个请求合起来完成的全部服务计算量。 |
| work over time | 随时间完成的工作 | Total completed work measured during a period. | 一段时间内总共完成了多少工作。 |
| request duration | 请求持续时间 | The elapsed time for one request. | 一次请求从开始到结束经过的时间。 |
| execution duration | 执行持续时间 | The time spent executing model computation. | 真正运行模型计算花费的时间。 |
| serving capacity | 服务承载能力 | The amount of traffic a serving system can handle. | 模型服务可以承担的请求量。 |
| service scalability | 服务可扩展性 | The ability to handle more work by adding or using resources. | 请求变多时，服务继续扩展承载能力的程度。 |
| model service optimization | 模型服务优化 | Improving how a model service uses time and hardware. | 改进模型服务的速度和资源使用。 |
| application integration | 应用集成 | Connecting an application to a model service. | 把应用和模型服务接起来。 |
| model integration | 模型集成 | Adding a model to an application or service workflow. | 把模型接入应用流程。 |
| serving interface | 服务接口 | The interface used to access a serving system. | 调用模型服务的接口。 |
| inference interface | 推理接口 | An interface used to submit inference inputs. | 提交推理请求的接口。 |
| model-serving workflow | 模型服务工作流 | The process by which applications obtain model results. | 应用获得模型结果的完整流程。 |
| operational model service | 运营型模型服务 | A model service intended for ongoing real-world use. | 面向持续真实使用的模型服务。 |
| technical boundary | 技术边界 | A distinction between neighboring technical concepts. | 两个容易混淆的技术概念之间的界线。 |
| common confusion | 常见混淆 | A misunderstanding between similar-looking concepts. | 很多人会混在一起理解的概念。 |
| positioning comparison | 定位比较 | Comparing tools by the roles and use cases they target. | 按工具定位和适用场景比较它们。 |
| common fit | 常见适用场景 | The use case a tool commonly suits. | 某个工具通常比较适合做的事情。 |
| traffic-control analogy | 流量控制类比 | A simplified analogy that treats requests like traffic. | 把请求想成车流来帮助理解调度。 |
| simplified analogy | 简化类比 | An analogy that explains a concept without covering every detail. | 为了入门易懂而省略细节的比喻。 |
| mental model | 心智模型 | A simple way to think about how a system works. | 帮助人理解系统工作方式的脑中图景。 |
| beginner-friendly mental model | 面向初学者的心智模型 | A simplified explanation designed for beginners. | 为新手准备的简单理解方式。 |
| short answer | 简短答案 | A concise definition of the topic. | 用很短的话说明主题是什么。 |
| related topic | 相关主题 | A nearby topic that helps explain the current one. | 和当前主题相邻、能帮助理解的主题。 |
| topic neighborhood | 概念邻域 | A group of concepts connected to the topic. | 围绕主题的一圈相关概念。 |
| keep the nouns separate | 分开理解这些名词 | Do not treat the model, serving software, and API as the same thing. | 不要把模型、服务软件和 API 当成一个东西。 |
| model serving tool | 模型服务工具 | Software used to make a model callable. | 让模型可以被调用的软件工具。 |
| service tool | 服务工具 | A tool for exposing and managing a running service. | 提供和管理运行中服务的工具。 |
| production-style tool | 生产式工具 | A tool suited to real service workloads. | 适合真实上线服务任务的工具。 |
| local-first tool | 本地优先工具 | A tool primarily designed around local model use. | 主要围绕本地运行和使用模型设计的工具。 |
| inference runtime | 推理运行时 | The software environment that executes inference. | 实际执行推理计算的软件环境。 |
| efficient inference runtime | 高效推理运行时 | A runtime optimized to execute inference effectively. | 针对高效推理计算优化的运行环境。 |
| serving runtime | 服务运行时 | A runtime that keeps a model available for incoming calls. | 让模型持续可被请求调用的运行环境。 |
| hardware-backed inference | 硬件支持的推理 | Inference carried out using available compute hardware. | 借助 GPU 等硬件完成模型推理。 |
| memory-backed execution | 基于内存的执行 | Execution that uses memory to hold weights and working data. | 用内存放模型和临时计算数据来运行。 |
| scalable serving | 可扩展服务 | Serving that can accommodate increasing request load. | 请求增加时还能扩大承载量的服务。 |
| request-serving system | 请求服务系统 | A system that receives and completes requests. | 接收请求并把结果返回的系统。 |
| model execution service | 模型执行服务 | A service dedicated to executing models for callers. | 专门为调用方执行模型的服务。 |
| application integration point | 应用集成点 | The place where an application connects to model capability. | 应用接入模型能力的地方。 |
| service abstraction | 服务抽象层 | A layer that hides execution details behind a callable service. | 把模型运行细节藏在可调用服务后面的层。 |
| serving abstraction | 服务抽象 | Treating a running model as a service rather than direct computation. | 把模型运行包装成应用可以调用的服务。 |
| direct computation | 直接计算 | Computation performed without a serving abstraction. | 不经过服务层、直接执行模型计算。 |
| serving efficiency | 服务效率 | The effectiveness of a service at using time and resources. | 服务利用时间和资源的好坏。 |
| model execution efficiency | 模型执行效率 | How effectively the runtime computes model outputs. | 运行时计算模型结果的效率。 |
| request-level performance | 请求级性能 | Performance measured for an individual request. | 以单个请求为单位衡量的表现。 |
| system-level performance | 系统级性能 | Performance measured across the serving system and many requests. | 在整个服务和多请求范围衡量的表现。 |
| service-level metric | 服务级指标 | A metric describing a running model service. | 描述模型服务整体表现的指标。 |
| generation metric | 生成指标 | A metric describing how output is generated. | 描述模型生成速度或数量的指标。 |
| capacity metric | 承载指标 | A metric describing how much work can be handled. | 描述服务能承担多少工作的指标。 |
| efficiency metric | 效率指标 | A metric describing useful work relative to resources. | 描述资源投入和有效产出关系的指标。 |
| model request coordination | 模型请求协调 | Organizing multiple model calls into an efficient execution flow. | 把多个模型调用安排成高效流程。 |
| application demand coordination | 应用需求协调 | Organizing demand from multiple applications. | 安排多个应用发来的需求。 |
| service request coordination | 服务请求协调 | Coordinating requests inside the serving system. | 在服务内部协调各个请求。 |
| request batch | 请求批次 | A group of requests processed as a unit. | 被放在一起处理的一批请求。 |
| batching efficiency | 批处理效率 | How effectively grouped requests use computation. | 多个请求一起处理时资源利用得多好。 |
| memory-aware serving | 感知内存的服务 | Serving designed around available memory constraints. | 根据内存限制来安排模型服务。 |
| GPU-aware serving | 感知 GPU 的服务 | Serving designed around available GPU capacity. | 根据 GPU 能力来安排模型服务。 |
| resource-aware scheduling | 资源感知调度 | Scheduling that considers available hardware resources. | 调度请求时考虑 GPU 和内存是否够用。 |
| execution ordering | 执行顺序 | The order in which requests or computations run. | 各个任务实际运行的先后顺序。 |
| service queue | 服务队列 | Requests waiting inside a service. | 服务内部等待处理的请求列表。 |
| request admission | 请求接入 | Allowing an incoming request into the serving system. | 让新请求进入服务处理。 |
| request dispatch | 请求分发 | Sending a request to the component that handles it. | 把请求交给负责处理的组件。 |
| model dispatch | 模型分发 | Sending computation to the model or hardware that runs it. | 把计算交给模型和对应硬件执行。 |
| result return | 结果返回 | Sending a completed result back to the caller. | 把处理好的结果送回应用。 |
| application caller | 应用调用方 | The application that sends a request. | 发起模型调用的应用。 |
| external caller | 外部调用方 | A user or system outside the serving implementation. | 模型服务之外发起调用的人或系统。 |
| service consumer | 服务使用方 | An application or user that consumes model-service output. | 使用模型服务结果的一方。 |
| model provider layer | 模型提供层 | The layer that exposes model capability to consumers. | 把模型能力提供给使用方的层。 |
| execution backend | 执行后端 | The lower-level system that performs the computation. | 负责底层计算的系统。 |
| GPU backend | GPU 后端 | A computation backend using GPU hardware. | 使用 GPU 进行计算的底层部分。 |
| serving front end | 服务前端 | The request-facing part of a serving system. | 接收应用请求的服务前端部分。 |
| serving back end | 服务后端 | The execution-facing part of a serving system. | 负责模型和硬件执行的服务后端部分。 |
| model-serving boundary | 模型服务边界 | The boundary separating request access from model execution. | 请求入口与模型运行之间的分界。 |
| service implementation | 服务实现 | The internal software that makes the service work. | 服务内部真正实现功能的软件。 |
| serving behavior | 服务行为 | How the service reacts to and processes requests. | 服务收到请求后如何运行和返回结果。 |
| model behavior | 模型行为 | The outputs or responses produced by the learned model. | 模型根据输入表现出来的输出能力。 |
| request behavior | 请求行为 | How requests arrive, wait, and complete. | 请求进入、排队和完成的方式。 |
| execution behavior | 执行行为 | How computation uses resources and progresses. | 计算如何占用资源并推进。 |
| efficient model access | 高效模型访问 | Accessing model capability with low waste and good speed. | 快速且省资源地调用模型。 |
| model access pattern | 模型访问模式 | The way users or applications call a model. | 用户或应用调用模型的规律。 |
| shared model service | 共享模型服务 | One model service used by multiple callers. | 多个用户或应用共用的模型服务。 |
| multi-tenant serving | 多租户服务 | One serving system serving multiple independent callers. | 一个服务同时为多个相互独立的使用方服务。 |
| service sharing | 服务共享 | Multiple callers using the same running service. | 多个调用方共同使用一个服务。 |
| shared resources | 共享资源 | Hardware capacity used by multiple requests or callers. | 多个请求共同使用的 GPU 或内存。 |
| model service efficiency | 模型服务效率 | How well a shared model service uses time and hardware. | 共享模型服务利用资源的好坏。 |
| request mix | 请求组合 | The different request types arriving together. | 同时到来的不同类型请求的组合。 |
| serving scenario | 服务场景 | A situation in which model serving is used. | 模型服务实际被使用的一种情况。 |
| local scenario | 本地场景 | Model use on local hardware or a local developer machine. | 在本地电脑上运行和调用模型的情况。 |
| server scenario | 服务器场景 | Model use through a shared or hosted server. | 通过共享或托管服务器使用模型的情况。 |
| production scenario | 生产场景 | Model use in a live application or business workflow. | 在真实上线应用或业务流程中使用模型。 |
| developer scenario | 开发者场景 | Model use while building, testing, or experimenting. | 开发、测试或试验时使用模型的情况。 |
| serving choice | 服务工具选择 | Choosing a serving tool based on workload and goals. | 根据任务和目标选择模型服务工具。 |
| tool positioning | 工具定位 | The role and common fit of a tool. | 一个工具在技术栈中的角色和适用范围。 |
| software category | 软件类别 | A group of tools with a related role. | 作用相近的一类软件。 |
| model runtime category | 模型运行时类别 | Software focused on executing models. | 主要负责运行模型的一类软件。 |
| serving engine category | 服务引擎类别 | Software focused on serving model requests efficiently. | 主要负责高效提供模型服务的一类软件。 |
| local AI tool category | 本地 AI 工具类别 | Tools focused on using AI models locally. | 主要用于本地使用 AI 模型的一类工具。 |
| high-throughput category | 高吞吐量类别 | Tools or systems optimized for large amounts of work over time. | 重点处理大量持续请求的一类工具或系统。 |
| API-based model access | 基于 API 的模型访问 | Using an API as the route to a model. | 通过 API 访问模型。 |
| model-as-a-service | 模型即服务 | Providing a model through a callable service rather than direct loading. | 把模型包装成应用可以调用的服务。 |
| inference-as-a-service | 推理即服务 | Providing model inference through a service boundary. | 通过服务接口提供模型推理。 |
| service interface to a model | 面向模型的服务接口 | A callable interface that leads to model execution. | 调用后会触发模型运行的服务入口。 |
| service abstraction over model weights | 覆盖模型权重的服务抽象 | A service hides direct access to raw model weights. | 应用不必直接操作模型权重，而是调用服务。 |
| raw model weights | 原始模型权重 | The learned numerical data stored for a model. | 模型训练后保存的原始数字数据。 |
| loaded model | 已加载模型 | A model whose weights have been placed into a runtime. | 权重已经放入运行环境、可以执行的模型。 |
| unloaded model | 未加载模型 | A model whose weights are not currently in the runtime. | 当前还没有放进运行环境的模型。 |
| model loading | 模型加载 | Moving model weights into memory for execution. | 把模型权重放进内存准备运行。 |
| weight loading | 权重加载 | Loading learned values into a runtime. | 把训练出的数字加载到运行环境。 |
| one-time loading | 一次性加载 | Loading something once and reusing it for later requests. | 只加载一次，之后反复使用。 |
| model reuse | 模型复用 | Reusing one loaded model for many requests. | 一个已加载模型处理多次请求。 |
| shared loaded model | 共享已加载模型 | One loaded model instance used by multiple requests. | 多个请求共同使用同一个已加载模型。 |
| model instance | 模型实例 | A running copy of a model in a runtime. | 运行环境中实际启动的一份模型。 |
| model process | 模型进程 | A running process that holds or executes a model. | 载入并运行模型的程序进程。 |
| serving instance | 服务实例 | One running copy of a model-serving service. | 正在运行的一份模型服务。 |
| service instance | 服务实例 | One active process or copy of a service. | 一份当前活跃的服务程序。 |
| inference engine layer | 推理引擎层 | The layer responsible for executing model inference. | 负责真正推理计算的软件层。 |
| serving engine layer | 服务引擎层 | The layer responsible for request-facing model service. | 负责接收请求并提供模型服务的层。 |
| execution engine | 执行引擎 | A core component that runs computations. | 负责执行计算的核心软件。 |
| request execution | 请求执行 | Running the computation required by a request. | 把请求对应的模型计算真正跑起来。 |
| application request execution | 应用请求执行 | Completing model computation requested by an application. | 完成应用要求的模型计算。 |
| efficient request execution | 高效请求执行 | Completing request computation with good use of time and hardware. | 用较少时间和资源完成请求计算。 |
| serving execution | 服务执行 | Execution performed to provide a response through a service. | 为服务调用而进行的模型执行。 |
| inference execution | 推理执行 | The computation that maps an input to an inference result. | 把输入计算成推理结果的过程。 |
| model inference execution | 模型推理执行 | Executing a learned model on an input. | 用训练好的模型处理一个输入。 |
| request-to-result flow | 请求到结果流程 | The flow from request arrival to returned output. | 请求进入后直到结果返回的全过程。 |
| application-to-result flow | 应用到结果流程 | The flow from an application call to its model output. | 应用发起调用后得到模型结果的全过程。 |
| hardware-to-result computation | 硬件到结果计算 | Hardware computation that produces a model result. | GPU 等硬件计算并产出模型结果。 |
| model result serving | 模型结果服务 | Returning model results to application callers. | 把模型结果返回给调用应用。 |
| performance-sensitive serving | 对性能敏感的服务 | Serving where speed and capacity are important design concerns. | 对速度、并发和承载量要求很高的服务。 |
| throughput-sensitive workload | 对吞吐量敏感的工作负载 | A workload where total completed work matters greatly. | 特别重视单位时间完成总任务量的任务。 |
| latency-sensitive workload | 对延迟敏感的工作负载 | A workload where each request must return quickly. | 特别重视单次请求等待时间的任务。 |
| serving objective | 服务目标 | The performance or usability goal of a serving system. | 建设模型服务时希望达到的目标。 |
| inference objective | 推理目标 | The desired speed, quality, or capacity of inference. | 对推理速度、质量或承载量的要求。 |
| efficient hardware use | 高效硬件使用 | Getting more useful model work from hardware. | 让同样的硬件完成更多有用的模型计算。 |
| compute utilization | 计算利用率 | The fraction of compute capacity actively doing useful work. | 计算能力中真正用来做有效工作的比例。 |
| memory footprint | 内存占用 | The amount of memory needed by a model or process. | 模型或程序占用的内存大小。 |
| serving footprint | 服务资源占用 | The resources consumed by a serving system. | 模型服务运行时占用的资源。 |
| resource pressure | 资源压力 | Demand that approaches or exceeds available hardware capacity. | 任务需求快要超过硬件能力的状态。 |
| serving bottleneck | 服务瓶颈 | A constrained component that limits serving performance. | 限制整体服务速度或承载量的环节。 |
| performance bottleneck | 性能瓶颈 | The part that prevents a system from becoming faster. | 拖慢系统表现的主要环节。 |
| request bottleneck | 请求瓶颈 | A constraint that slows request completion. | 让请求完成变慢的限制因素。 |
| memory bottleneck | 内存瓶颈 | A shortage or inefficient use of memory limiting execution. | 内存不够或利用不好，导致运行受限。 |
| GPU bottleneck | GPU 瓶颈 | A GPU compute limit that constrains execution. | GPU 算力不足导致运行受限。 |
| serving optimization target | 服务优化目标 | The dimension chosen for improvement, such as latency or throughput. | 决定要优先改善延迟、吞吐量等哪项表现。 |
| real-world serving | 真实世界服务 | Serving used by actual applications and users. | 真正给用户和应用使用的模型服务。 |
| live service | 在线服务 | A service currently running and accepting requests. | 正在运行并接受调用的服务。 |
| ongoing service | 持续服务 | A service intended to keep operating over time. | 需要持续运行而不是只执行一次的服务。 |
| request-serving architecture | 请求服务架构 | The components and flow used to serve requests. | 处理和返回请求时各组件如何组织。 |
| model-serving architecture | 模型服务架构 | The architecture that connects applications, serving software, models, and hardware. | 连接应用、服务软件、模型和硬件的整体设计。 |
| simplified serving stack | 简化服务栈 | A basic diagram of the layers in a serving system. | 用简单层次图表示模型服务组成。 |
| stack node | 服务栈节点 | One component or layer shown in a serving stack. | 服务栈图中的一个组件或层。 |
| stack layer | 服务栈层 | One level in the sequence from application to hardware. | 从应用到硬件的某一层。 |
| stack flow | 服务栈流程 | The direction in which requests and computation move through layers. | 请求和计算在各层之间流动的方向。 |
| application node | 应用节点 | The application component at the top of the serving stack. | 服务栈最上面的应用组件。 |
| API node | API 节点 | The API component through which requests enter. | 请求进入服务栈的 API 组件。 |
| vLLM node | vLLM 节点 | The vLLM component that performs serving and inference work. | 服务栈中负责运行和服务的 vLLM 部分。 |
| model node | 模型节点 | The learned model component in the stack. | 服务栈中的模型部分。 |
| GPU node | GPU 节点 | The GPU hardware component at the bottom of the stack. | 服务栈最底层的 GPU 硬件部分。 |
| application request as input | 作为输入的应用请求 | A request entering the serving system. | 应用发来的请求就是服务系统的输入。 |
| model result as output | 作为输出的模型结果 | A result returned after inference. | 推理完成后返回给应用的结果。 |
| request scheduling and batching | 请求调度与批处理 | Coordinating request order and grouping requests together. | 安排请求顺序并把适合的请求成批处理。 |
| high-throughput serving and inference | 高吞吐量服务与推理 | Serving and running many model requests over time. | 在一段时间内高效处理很多模型请求。 |
| application-facing model runtime | 面向应用的模型运行时 | A model runtime exposed for application use. | 可以被应用调用的模型运行环境。 |
| production-facing model runtime | 面向生产的模型运行时 | A runtime designed for operational service traffic. | 为真实上线服务流量设计的运行环境。 |
| local-facing model runtime | 面向本地的模型运行时 | A runtime designed for local developer use. | 为本地开发和使用设计的运行环境。 |
| serving performance layer | 服务性能层 | The part of the stack that controls service efficiency. | 影响服务速度和资源效率的部分。 |
| model execution resource layer | 模型执行资源层 | The hardware resource layer used for execution. | 运行模型时使用的 GPU 和内存层。 |
| application-to-GPU stack | 应用到 GPU 的技术栈 | The complete path from application request to hardware execution. | 从应用请求到 GPU 计算的完整技术链路。 |
| service abstraction boundary | 服务抽象边界 | The point where application details are separated from execution details. | 应用不必了解底层执行细节的分界。 |
| caller | 调用方 | The application or system making a request. | 发起请求的一方。 |
| callee | 被调用方 | The service or model receiving and processing a request. | 接收并处理请求的一方。 |
| request producer | 请求产生方 | The application or user that creates requests. | 产生请求的人或程序。 |
| request consumer | 请求处理方 | The system that receives and processes requests. | 接收并处理请求的系统。 |
| model consumer | 模型使用方 | An application or user consuming model outputs. | 使用模型输出的人或程序。 |
| serving provider | 服务提供方 | The software or system that provides model-serving capability. | 提供模型服务能力的软件或系统。 |
| model owner | 模型拥有方 | The party that provides or controls the model weights. | 提供或控制模型权重的一方。 |
| infrastructure owner | 基础设施拥有方 | The party that operates the hardware or cloud infrastructure. | 管理服务器和硬件基础设施的一方。 |
| service role | 服务角色 | The function a component plays in serving. | 一个组件在模型服务中的职责。 |
| vLLM role | vLLM 的角色 | vLLM acts as serving and inference software between applications and models. | vLLM 位于应用和模型之间，负责服务和推理。 |
| LLM role | LLM 的角色 | An LLM supplies learned language behavior and weights. | LLM 提供训练好的语言能力和权重。 |
| API role | API 的角色 | An API defines how applications access a service. | API 规定应用怎样进入和调用服务。 |
| GPU role | GPU 的角色 | A GPU supplies accelerated computation for model execution. | GPU 为模型运行提供加速计算。 |
| memory role | 内存的角色 | Memory holds weights, inputs, and intermediate computation data. | 内存存放权重、输入和临时计算数据。 |
| service role separation | 服务角色分离 | Different layers have different responsibilities. | 技术栈中不同部分各自负责不同事情。 |
| noun separation | 名词分离 | Keeping related but non-identical technical terms distinct. | 把相关但不相同的技术名词分开理解。 |
| concept boundary | 概念边界 | The limit that distinguishes one concept from another. | 判断两个概念是不是同一个的界线。 |
| conceptual confusion | 概念混淆 | Treating separate concepts as if they were identical. | 把不同的东西误认为同一个。 |
| serving tool comparison | 服务工具比较 | Comparing tools by role, workload, and usage pattern. | 按角色、任务和使用方式比较工具。 |
| inference engine comparison | 推理引擎比较 | Comparing systems that execute inference. | 比较不同模型推理运行系统。 |
| local runtime comparison | 本地运行时比较 | Comparing tools for local model use. | 比较适合本地运行模型的工具。 |
| model serving comparison | 模型服务比较 | Comparing ways to expose models to applications. | 比较不同的模型提供服务方式。 |
| API access comparison | API 访问比较 | Comparing how applications reach model capability. | 比较应用如何调用模型。 |
| performance comparison | 性能比较 | Comparing latency, generation rate, or throughput. | 比较等待时间、生成速度和总处理量。 |
| role comparison | 角色比较 | Comparing what each component is responsible for. | 比较各个组件分别负责什么。 |
| usage comparison | 使用场景比较 | Comparing where different tools are commonly used. | 比较不同工具通常用在什么地方。 |
| local usage | 本地使用 | Using a model on local hardware. | 在自己的电脑或设备上使用模型。 |
| server usage | 服务器使用 | Using a model through a server. | 通过服务器调用模型。 |
| application usage | 应用使用 | Using a model from an application workflow. | 在应用业务流程中调用模型。 |
| developer usage | 开发者使用 | Using a model while developing or experimenting. | 开发者开发和试验时使用模型。 |
| production usage | 生产环境使用 | Using a model in a real live service. | 在真实上线服务中使用模型。 |
| model-serving use case | 模型服务用例 | A practical situation in which a model is served. | 一个实际调用模型服务的场景。 |
| serving goal | 服务目标 | The desired behavior of a model-serving system. | 希望模型服务达到的效果。 |
| request goal | 请求目标 | The task an application asks the model to perform. | 应用希望模型完成的事情。 |
| inference goal | 推理目标 | The output that inference should produce. | 推理过程要得到的结果。 |
| performance goal | 性能目标 | A desired latency, throughput, or generation rate. | 期望达到的延迟、吞吐量或生成速度。 |
| efficiency goal | 效率目标 | A desired balance of useful work and resource use. | 希望用较少资源完成更多工作。 |
| model-serving decision | 模型服务决策 | A choice about how and where to run a model service. | 决定模型服务用什么工具、怎样运行。 |
| service architecture decision | 服务架构决策 | A choice about the components and flow of a serving system. | 决定模型服务由哪些层和组件组成。 |
| runtime choice | 运行时选择 | Selecting the software environment for model execution. | 选择用哪种环境运行模型。 |
| tool choice | 工具选择 | Selecting a model-serving or runtime tool. | 选择具体的模型运行或服务工具。 |
| workload fit | 工作负载适配 | How well a tool matches the workload it must handle. | 工具是否适合要处理的任务量和类型。 |
| application fit | 应用适配 | How well a serving tool fits an application’s needs. | 服务工具是否满足应用需求。 |
| production fit | 生产适配 | How well a tool fits real operational serving. | 工具是否适合真实上线使用。 |
| local fit | 本地适配 | How well a tool fits local model use. | 工具是否适合在本地电脑上使用。 |
| performance fit | 性能适配 | How well a tool meets speed and capacity needs. | 工具性能是否满足速度和承载要求。 |
| resource fit | 资源适配 | How well a model and runtime fit available hardware. | 模型和运行时是否适合现有 GPU、内存。 |
| system fit | 系统适配 | How well the complete setup fits its target context. | 整套系统是否适合目标环境。 |
| service readiness | 服务就绪度 | Whether a service can accept and handle requests. | 服务是否已经能稳定接收并处理请求。 |
| model readiness | 模型就绪度 | Whether a model is loaded and ready for inference. | 模型是否已经加载、可以开始推理。 |
| runtime readiness | 运行时就绪度 | Whether the runtime is prepared to execute a model. | 运行环境是否已经准备好执行模型。 |
| GPU readiness | GPU 就绪度 | Whether the GPU is available for model work. | GPU 是否有空闲能力运行模型。 |
| request readiness | 请求就绪度 | Whether a request can enter execution. | 请求是否满足条件、可以开始处理。 |
| service operation | 服务运行 | The ongoing operation of a model service. | 模型服务持续工作。 |
| model operation | 模型运行 | The ongoing execution of a model. | 模型持续处理输入。 |
| inference operation | 推理运行 | The ongoing execution of inference tasks. | 推理任务持续计算和返回结果。 |
| API operation | API 运行 | The operation of an interface accepting calls. | 接口持续接受应用调用。 |
| GPU operation | GPU 运行 | GPU work performed for model computation. | GPU 为模型计算持续工作。 |
| memory operation | 内存运行 | Memory allocation and use during execution. | 运行时不断分配和使用内存。 |
| serving operation | 服务运维；服务运行 | Keeping a model service available and functioning. | 让模型服务一直可用并正常工作。 |
| operational performance | 运行性能 | Performance observed in a real running service. | 真实服务运行时表现出的性能。 |
| model-serving performance terms | 模型服务性能术语 | Terms such as latency, tokens per second, and throughput. | 用来描述模型服务速度和承载量的词。 |
| time-to-result | 得到结果的时间 | The elapsed time until a result is returned. | 从请求开始到结果出现所需时间。 |
| work-per-time | 单位时间工作量 | The amount of work completed during a time interval. | 一段时间能完成多少工作。 |
| output-per-time | 单位时间输出量 | The amount of output generated per unit of time. | 一段时间能生成多少内容。 |
| service efficiency trade-off | 服务效率权衡 | Balancing fast responses, high throughput, and resource use. | 在低延迟、高吞吐和省资源之间做取舍。 |
| simplified performance explanation | 简化性能解释 | A beginner-level explanation of serving metrics. | 用入门方式解释性能指标。 |
| performance measurement | 性能测量 | Measuring how a serving system behaves. | 用数字测试服务表现。 |
| measure latency | 测量延迟 | Record how long a request takes. | 记录一次请求等待了多久。 |
| measure generation rate | 测量生成速率 | Record how many tokens are generated per second. | 记录每秒生成多少词元。 |
| measure throughput | 测量吞吐量 | Record how much serving work completes over time. | 记录一段时间内完成多少服务工作。 |
| serving benchmark | 服务基准测试 | A test used to compare serving performance. | 用来比较模型服务性能的测试。 |
| performance result | 性能结果 | A measured latency, rate, or throughput value. | 测试得到的速度、延迟或处理量数字。 |
| request metric | 请求指标 | A metric measured for requests. | 以请求为单位记录的指标。 |
| service metric | 服务指标 | A metric measured for the whole service. | 描述整个服务表现的指标。 |
| workload metric | 工作负载指标 | A metric describing incoming or completed work. | 描述任务量或处理量的指标。 |
| hardware metric | 硬件指标 | A metric describing GPU or memory use. | 描述 GPU、内存等硬件使用情况的指标。 |
| throughput metric | 吞吐量指标 | A metric for completed work per period. | 衡量单位时间完成多少工作的指标。 |
| latency metric | 延迟指标 | A metric for request waiting or completion time. | 衡量请求耗时的指标。 |
| token-rate metric | 词元速率指标 | A metric for generated tokens per second. | 衡量每秒生成词元数的指标。 |
| execution metric | 执行指标 | A metric describing model computation. | 描述模型计算过程的指标。 |
| serving metric vocabulary | 服务指标词汇 | The terms used to discuss serving performance. | 讨论服务性能时使用的一组词。 |
| model-serving glossary | 模型服务术语表 | A collection of terms related to serving models. | 解释模型服务相关词汇的集合。 |

## Potential Missing Concepts

- **PagedAttention（分页注意力）**：页面只把 vLLM 说成服务／推理引擎，没有解释 vLLM 相关实现中常被讨论的注意力内存管理机制。
- **continuous batching（连续批处理）**：页面提到 batching，但没有解释请求动态加入和离开批次的连续批处理方式。
- **KV cache（键值缓存）**：页面提到内存资源，但没有解释自回归生成时缓存 attention 的 key/value。
- **Paged KV cache（分页 KV 缓存）**：没有说明把 KV cache 按块管理如何减少内存浪费。
- **prefill（预填充）**：没有区分处理输入提示词的阶段和生成输出的阶段。
- **decode（解码）**：没有说明逐 token 生成输出的解码阶段。
- **prefill-decode separation（预填充／解码分离）**：没有说明两类计算可使用不同资源或调度策略。
- **time to first token / TTFT（首 token 时间）**：页面有 latency，但没有单独说明从请求到第一个输出 token 的等待时间。
- **inter-token latency / ITL（token 间延迟）**：没有说明连续输出 token 之间的间隔。
- **end-to-end latency（端到端延迟）**：没有拆解网络、排队、推理和返回结果的总耗时。
- **queue time（排队时间）**：request scheduling 出现了，但没有定义请求等待执行的时间。
- **service time（服务时间）**：没有区分真正执行请求的时间与排队等待时间。
- **batch size（批大小）**：页面说 batching，但没有解释一次批处理包含多少请求或 token。
- **concurrency（并发度）**：multiple requests 出现了，但没有说明同时在途请求数量。
- **request rate（请求速率）**：页面有多个请求，但没有解释单位时间进入多少请求。
- **tokens/sec per request（单请求每秒 token）**：tokens per second 的统计口径没有明确是单请求还是整体服务。
- **aggregate throughput（聚合吞吐量）**：throughput 出现了，但没有说明多个请求合计的 token 或请求处理量。
- **tail latency（尾延迟）**：没有讨论 p95、p99 等慢请求指标。
- **latency-throughput trade-off（延迟—吞吐量权衡）**：页面分别列出 latency 和 throughput，但没有展开二者的取舍。
- **GPU utilization（GPU 利用率）**：GPU 出现了，但没有具体解释 GPU 是否被充分使用。
- **GPU memory utilization（GPU 显存利用率）**：memory resource 出现了，但没有区分显存占用比例。
- **memory fragmentation（内存碎片）**：没有解释可用内存被分成不连续小块而难以利用的问题。
- **memory bandwidth（内存带宽）**：没有解释 GPU 与内存之间搬运数据的速度限制。
- **compute-bound（计算受限）**：没有说明瓶颈来自算力不足的情况。
- **memory-bound（内存受限）**：没有说明瓶颈来自内存容量或带宽的情况。
- **CUDA（CUDA）**：页面写 GPU，但没有说明常见 GPU 软件运行环境。
- **PyTorch（PyTorch）**：没有说明模型执行通常依赖的深度学习框架。
- **Hugging Face Transformers（Hugging Face Transformers）**：没有提到常见模型加载与架构生态。
- **model checkpoint（模型检查点）**：model weights 出现了，但没有定义保存权重的模型文件或检查点。
- **tokenizer（分词器／词元器）**：tokens per second 出现了，但没有解释文本如何切分成 tokens。
- **prompt tokens（输入词元）**：没有区分输入 prompt 的 token 与输出 token。
- **output tokens（输出词元）**：没有单独解释模型生成的 token 数量。
- **context length（上下文长度）**：没有说明一次请求能处理的最大输入与历史 token 数。
- **maximum sequence length（最大序列长度）**：没有说明序列长度对显存和服务能力的影响。
- **sampling（采样）**：页面说生成，但没有介绍随机采样控制输出的方式。
- **temperature（温度）**：没有解释控制生成随机性的常见参数。
- **top-p / nucleus sampling（核采样）**：没有介绍生成时候选 token 的筛选策略。
- **top-k sampling（top-k 采样）**：没有介绍只从概率最高的一小组 token 采样。
- **stopping criteria（停止条件）**：没有说明模型何时停止生成。
- **streaming（流式输出）**：API 和生成出现了，但没有说明边生成边返回 token。
- **streaming response（流式响应）**：没有解释应用如何逐段接收生成结果。
- **OpenAI-compatible API（OpenAI 兼容 API）**：页面只说 API，没有说明常见的兼容接口形式。
- **REST API（REST API）**：API 出现了，但没有说明网络接口的常见实现方式。
- **HTTP endpoint（HTTP 端点）**：没有解释应用通过网络地址发送请求。
- **request schema（请求结构）**：没有定义请求中模型名、提示词、参数等字段。
- **response schema（响应结构）**：没有定义返回文本、token 使用量、状态等字段。
- **authentication（身份验证）**：API access 出现了，但没有讨论谁可以调用服务。
- **authorization（授权）**：没有说明不同调用方能使用哪些模型或资源。
- **rate limiting（限流）**：没有说明服务如何限制请求速率。
- **load balancing（负载均衡）**：多个请求和服务能力出现了，但没有讨论多实例之间的请求分配。
- **replica（副本）**：没有说明同一模型服务的多个运行副本。
- **autoscaling（自动扩缩容）**：production serving 出现了，但没有说明按流量增减实例。
- **health check（健康检查）**：没有介绍服务是否可用的检查机制。
- **readiness probe（就绪探针）**：没有说明模型加载完成后如何被判断为可接收请求。
- **observability（可观测性）**：performance terms 出现了，但没有系统说明日志、指标和追踪。
- **logging（日志）**：没有说明如何记录请求和服务事件。
- **tracing（链路追踪）**：没有说明如何追踪请求经过的各个环节。
- **metrics collection（指标采集）**：页面列出性能词，但没有说明指标如何被收集。
- **error handling（错误处理）**：页面没有说明模型加载失败、请求失败或资源不足时怎么办。
- **timeout（超时）**：latency 出现了，但没有定义等待过久后的失败边界。
- **retry（重试）**：没有说明临时失败时是否重新发送请求。
- **backpressure（背压）**：请求量和资源限制出现了，但没有解释系统如何阻止队列无限增长。
- **admission control（接入控制）**：没有说明资源不足时是否拒绝新请求。
- **priority scheduling（优先级调度）**：request scheduling 出现了，但没有说明不同请求的优先级。
- **fair scheduling（公平调度）**：没有讨论如何防止某类请求长期占用资源。
- **tensor parallelism（张量并行）**：GPU 与服务栈出现了，但没有解释把单个模型的计算分到多个 GPU。
- **pipeline parallelism（流水线并行）**：没有说明把模型不同层放到不同设备上执行。
- **data parallelism（数据并行）**：没有说明多个模型副本分别处理不同请求。
- **distributed inference（分布式推理）**：页面只有单个 GPU 的简化图，没有讨论跨设备推理。
- **multi-GPU serving（多 GPU 服务）**：没有解释服务如何使用多张 GPU。
- **model sharding（模型分片）**：没有说明把模型权重拆到多个设备或进程。
- **CPU offload（CPU 卸载）**：memory resource 出现了，但没有说明把部分权重或缓存放到 CPU 内存。
- **quantization（量化）**：相关链接存在，但正文没有解释低精度权重如何节省显存。
- **weight-only quantization（仅权重量化）**：没有说明只降低权重精度的量化方式。
- **activation quantization（激活量化）**：没有涉及中间激活值的量化。
- **LoRA（低秩适配）**：没有说明如何在同一基础模型上加载轻量适配器。
- **adapter serving（适配器服务）**：没有讨论一个服务支持多个适配器或任务版本。
- **speculative decoding（投机解码）**：没有介绍用小模型辅助大模型生成的加速方法。
- **prefix caching（前缀缓存）**：没有说明共享相同 prompt 前缀的请求如何复用计算。
- **prompt caching（提示缓存）**：没有讨论重复提示词的缓存机制。
- **CUDA graph（CUDA 图）**：没有说明固定计算图如何减少运行开销。
- **kernel（计算内核）**：没有解释 GPU 上执行的底层计算程序。
- **kernel fusion（内核融合）**：没有讨论合并 GPU 操作以减少开销。
- **attention kernel（注意力内核）**：没有解释注意力计算的 GPU 优化实现。
- **scheduler loop（调度循环）**：没有说明服务如何持续检查和安排请求。
- **continuous request processing（连续请求处理）**：页面只用概念性语言说协调，没有讲连续运行机制。
- **prefill batching（预填充批处理）**：没有单独讨论输入处理阶段的批处理。
- **decode batching（解码批处理）**：没有单独讨论生成阶段的批处理。
- **dynamic batching（动态批处理）**：没有说明批次如何随请求动态变化。
- **request cancellation（请求取消）**：没有介绍用户中止生成后如何释放资源。
- **partial output（部分输出）**：没有解释流式生成时尚未完成的中间结果。
- **request state（请求状态）**：没有定义排队、运行、完成、失败等状态。
- **generation state（生成状态）**：没有说明每个请求在逐 token 生成期间保存什么状态。
- **cache reuse（缓存复用）**：页面未具体讲解跨请求复用中间计算。
- **memory paging（内存分页）**：页面没有说明如何把缓存组织成可分页的块。
- **block manager（块管理器）**：没有介绍管理 KV cache 块的组件。
- **token budget（token 预算）**：没有说明输入和输出 token 的上限控制。
- **max tokens（最大 token 数）**：没有解释 API 中常见的最大输出长度参数。
- **context window（上下文窗口）**：没有说明模型一次能看到的 token 范围。
- **prompt length（提示长度）**：没有说明输入长短如何影响 prefill 和内存。
- **output length（输出长度）**：没有说明生成长短如何影响 decode 时间。
- **model parallel serving（模型并行服务）**：没有概括多卡共同运行单模型的服务方式。
- **data parallel serving（数据并行服务）**：没有概括多副本分别处理请求的服务方式。
- **distributed runtime（分布式运行时）**：没有讨论跨机器或跨 GPU 的运行环境。
- **cluster（集群）**：生产式服务出现了，但没有解释多台机器组成的资源集合。
- **node（节点）**：页面图中的 node 是示意块，没有定义分布式计算节点。
- **worker（工作进程）**：没有介绍实际执行模型计算的 worker。
- **controller（控制器）**：traffic controller 只是类比，没有定义系统控制组件。
- **scheduler（调度器）**：页面提到 scheduling，但没有将 scheduler 作为独立组件解释。
- **driver（驱动）**：GPU 出现了，但没有说明 GPU 驱动软件。
- **container（容器）**：生产服务常见部署形式，但页面没有展开。
- **Docker（Docker）**：没有介绍容器化运行 vLLM 的方式。
- **Kubernetes（Kubernetes）**：没有介绍集群编排和扩缩容。
- **Ray（Ray）**：没有说明分布式执行生态中的常见组件。
- **deployment（部署）**：页面用 serving 语境描述运行，但没有定义部署过程。
- **rollout（发布）**：没有说明模型服务版本如何上线。
- **versioning（版本管理）**：没有讨论模型、服务和 API 版本。
- **model registry（模型注册表）**：没有说明如何登记和发现可服务模型。
- **model repository（模型仓库）**：没有解释模型权重的存储和分发位置。
- **download（下载）**：没有涉及模型权重如何获得。
- **configuration（配置）**：没有介绍端口、模型路径、并发等服务参数。
- **command-line interface / CLI（命令行接口）**：没有说明如何启动服务。
- **server launch（服务器启动）**：没有介绍从配置到启动模型服务的过程。
- **port（端口）**：API endpoint 出现了，但没有解释网络端口。
- **network overhead（网络开销）**：latency 出现了，但没有拆解网络传输时间。
- **serialization（序列化）**：没有说明请求和响应如何转换为网络数据。
- **token streaming protocol（token 流式协议）**：没有解释流式结果如何传给应用。
- **client（客户端）**：application 出现了，但没有定义发起 API 请求的客户端。
- **client library（客户端库）**：没有提到应用如何通过 SDK 调用服务。
- **SDK（软件开发工具包）**：没有介绍封装 API 调用的开发库。
- **OpenAI client compatibility（OpenAI 客户端兼容性）**：没有讨论现有客户端能否直接连接服务。
- **model name（模型名称）**：API 请求出现了，但没有说明如何指定要运行的模型。
- **request parameter（请求参数）**：没有展开 temperature、max tokens 等请求选项。
- **generation configuration（生成配置）**：没有介绍影响输出生成的配置集合。
- **sampling parameter（采样参数）**：没有说明控制随机生成的参数。
- **determinism（确定性）**：没有讨论同一请求是否每次得到相同输出。
- **random seed（随机种子）**：没有介绍控制随机性的种子。
- **quality-performance trade-off（质量—性能权衡）**：页面只讲性能，没有说明生成质量和速度可能互相影响。
- **cost（成本）**：没有讨论 GPU 时间、机器和服务运营费用。
- **energy use（能耗）**：没有讨论持续 GPU 推理的能源消耗。
- **capacity planning（容量规划）**：没有解释如何按请求量准备 GPU 资源。
- **resource reservation（资源预留）**：没有说明为模型或请求提前保留内存和 GPU。
- **cold start（冷启动）**：没有解释首次加载模型导致的额外延迟。
- **warm start（热启动）**：没有说明模型已加载时的快速响应状态。
- **model warmup（模型预热）**：没有讨论服务正式接流量前的预热请求。
- **startup latency（启动延迟）**：没有区分服务启动和单次请求延迟。
- **steady-state performance（稳态性能）**：没有说明模型预热后持续运行的性能。
- **failure mode（失败模式）**：没有讨论显存不足、模型加载失败或请求超时。
- **out-of-memory / OOM（内存不足）**：memory resource 出现了，但没有具体定义 OOM。
- **graceful degradation（优雅降级）**：没有说明资源不足时如何降低服务能力而继续工作。
- **fallback（回退）**：没有介绍主服务失败时切换到其他模型或实例。
- **fault tolerance（容错）**：没有说明服务面对硬件或进程故障如何继续运行。
- **availability（可用性）**：没有把服务能否被调用作为独立指标解释。
- **SLA（服务等级协议）**：没有讨论服务承诺的延迟、可用性或容量。
- **service-level objective / SLO（服务等级目标）**：没有定义生产服务性能目标。
- **monitoring（监控）**：页面相关词只在链接邻域中出现，没有展开上线后的监控。
- **alerting（告警）**：没有解释性能或错误超过阈值时如何通知运维。
- **logging and tracing（日志与追踪）**：页面没有介绍排查服务问题的记录手段。
- **security（安全防护）**：页面的 “not a cloud provider” 没有讨论接口和模型服务安全。
- **privacy（隐私）**：没有讨论请求文本、用户数据和模型输入的保护。
- **isolation（隔离）**：多个应用共享服务，但没有说明调用方之间如何隔离资源和数据。
- **multi-tenancy（多租户）**：多个用户或应用出现了，但没有正式解释多租户服务。
- **quota（配额）**：没有定义每个调用方可以使用的请求或资源上限。
- **priority（优先级）**：请求协调出现了，但没有说明优先级策略。
- **fairness in scheduling（调度公平性）**：没有讨论不同请求如何公平获得资源。
- **load shedding（负载丢弃）**：没有说明过载时主动拒绝部分请求。
- **admission rejection（接入拒绝）**：没有说明资源不足时服务如何拒绝请求。
- **backoff（退避）**：没有解释调用方在过载或失败后如何等待再重试。
- **rate control（速率控制）**：没有说明控制请求进入速度的方法。
- **capacity limit（容量限制）**：没有把 GPU／内存上限与最大请求量联系起来。
- **memory limit（内存限制）**：没有说明模型和请求必须适配的显存边界。
- **context memory（上下文内存）**：没有说明长上下文如何占用运行内存。
- **activation memory（激活内存）**：没有区分权重、KV cache 和中间激活的内存。
- **weight memory（权重内存）**：没有单独说明模型权重占用的内存。
- **cache memory（缓存内存）**：没有说明缓存占用的内存来源。
- **memory accounting（内存核算）**：没有介绍如何估算一个服务需要多少内存。
- **resource estimation（资源估算）**：没有说明根据模型大小和请求量估算 GPU 的方法。
- **model size（模型大小）**：model weights 出现了，但没有解释参数规模对资源的影响。
- **parameter count（参数量）**：没有定义模型参数数量。
- **precision（数值精度）**：量化链接存在，但正文没有介绍 FP16、BF16、INT8 等精度。
- **FP16 / BF16 / INT8（低精度格式）**：没有列出常见推理数据格式。
- **mixed precision（混合精度）**：没有介绍不同计算使用不同精度。
- **model compatibility（模型兼容性）**：没有说明哪些模型架构可由 vLLM 运行。
- **architecture support（架构支持）**：没有定义服务引擎对不同模型架构的支持范围。
- **custom model（自定义模型）**：没有说明非标准模型如何接入。
- **multimodal model（多模态模型）**：页面仅聚焦 LLM，没有扩展图文等输入。
- **embedding model（嵌入模型）**：没有讨论生成模型以外的模型服务类型。
- **reranking model（重排序模型）**：没有讨论其他推理服务工作负载。
- **batch inference（批量推理）**：batching 出现了，但没有区分在线服务和离线批量推理。
- **offline inference（离线推理）**：没有讨论不需要实时响应的任务。
- **online inference（在线推理）**：server / production inference 出现了，但没有正式定义在线请求。
- **interactive inference（交互式推理）**：没有讨论人机交互对延迟的要求。
- **batch workload（批量工作负载）**：没有解释一次性处理大量数据的场景。
- **online workload（在线工作负载）**：没有解释实时到达请求的场景。
- **request locality（请求局部性）**：没有讨论相似 prompt 或用户请求的局部性。
- **cache hit（缓存命中）**：没有解释请求复用缓存时的命中情况。
- **cache miss（缓存未命中）**：没有解释没有可复用缓存时的额外计算。
- **reuse distance（复用距离）**：没有讨论缓存复用间隔。
- **throughput scaling（吞吐量扩展）**：没有说明增加 GPU 或实例如何影响吞吐量。
- **latency scaling（延迟扩展）**：没有说明并发增加时延迟如何变化。
- **horizontal scaling（水平扩展）**：没有讨论增加服务副本。
- **vertical scaling（垂直扩展）**：没有讨论换更大 GPU 或更多内存。
- **replication（复制）**：没有讨论复制模型实例以提高承载能力。
- **sharding（分片）**：没有讨论拆分模型或缓存的方式。
- **placement（放置）**：没有说明模型和请求如何放到不同 GPU。
- **device mapping（设备映射）**：没有解释模型组件与硬件设备的对应关系。
- **topology（拓扑）**：没有讨论多 GPU 或多机之间的连接结构。
- **interconnect（互联）**：没有解释 GPU 之间的通信链路。
- **communication overhead（通信开销）**：没有讨论分布式推理中的数据传输成本。
- **synchronization（同步）**：没有解释并行 GPU 之间的同步。
- **distributed scheduling（分布式调度）**：没有讨论跨设备或跨实例调度请求。
- **worker pool（工作进程池）**：没有介绍多个 worker 如何共同服务请求。
- **process isolation（进程隔离）**：没有讨论不同模型实例的进程边界。
- **thread（线程）**：没有解释并发执行的更底层单位。
- **async request（异步请求）**：没有讨论应用提交请求后不必同步等待。
- **synchronous request（同步请求）**：没有讨论调用方阻塞等待响应。
- **event loop（事件循环）**：没有涉及异步服务的实现方式。
- **network server（网络服务器）**：API 和 server 出现了，但没有定义网络监听进程。
- **protocol（协议）**：没有说明应用与服务之间传输请求的规则。
- **serialization format（序列化格式）**：没有说明 JSON 等请求数据格式。
- **JSON（JSON）**：没有具体提及常见 API 数据格式。
- **HTTP（HTTP）**：没有具体提及应用调用服务时常用的网络协议。
- **TLS（TLS）**：没有讨论 API 连接加密。
- **API key（API 密钥）**：没有讨论服务调用凭证。
- **access control（访问控制）**：没有讨论限制谁可以访问模型。
- **tenant isolation（租户隔离）**：没有讨论多用户共享 GPU 时的数据和资源隔离。
- **data residency（数据驻留）**：本地 AI 邻域存在，但没有讨论输入数据留在哪里。
- **model license（模型许可证）**：没有讨论被服务模型的使用许可。
- **acceptable use（可接受使用）**：没有讨论模型服务的使用政策。
- **content safety（内容安全）**：没有讨论生成内容过滤。
- **prompt injection（提示注入）**：API 服务场景可能涉及输入攻击，但页面没有展开。
- **abuse prevention（滥用防护）**：没有讨论如何防止服务被恶意大量调用。
- **audit logging（审计日志）**：没有说明如何记录调用者和模型访问行为。
- **cost per request（单请求成本）**：没有将 GPU 资源与单次调用成本联系起来。
- **resource billing（资源计费）**：没有讨论按 GPU 时间或 token 计费。
- **energy-efficient inference（节能推理）**：没有讨论吞吐量和能耗的关系。
- **sustainability（可持续性）**：没有讨论持续模型服务的环境成本。
- **benchmark methodology（基准测试方法）**：没有说明如何公平比较 Ollama 和 vLLM。
- **workload representative benchmark（代表性工作负载基准）**：没有说明测试请求应接近真实流量。
- **warmup benchmark（预热后基准）**：没有区分首次启动和稳定运行的性能。
- **load test（负载测试）**：没有讨论逐步增加请求量测试容量。
- **stress test（压力测试）**：没有讨论超过正常容量时的行为。
- **capacity test（容量测试）**：没有讨论寻找最大可承载请求量的方法。
- **regression test（回归测试）**：没有讨论版本升级后性能是否退化。
- **compatibility test（兼容性测试）**：没有讨论模型、GPU、框架之间的兼容性。
- **correctness test（正确性测试）**：没有把服务性能与输出正确性分开测试。
- **service quality（服务质量）**：页面重点是性能，没有展开正确性、稳定性和可用性。
- **output quality（输出质量）**：没有讨论生成内容是否符合预期。
- **model quality（模型质量）**：没有区分模型本身质量与服务系统性能。
- **system quality（系统质量）**：没有综合讨论速度、正确性、稳定性和安全。
- **deployment operations（部署运维）**：没有展开部署后的持续运行工作。
- **incident response（故障响应）**：没有讨论服务异常时的排查和恢复。
- **rollback（回滚）**：没有介绍升级失败时恢复旧版本。
- **canary deployment（金丝雀部署）**：没有介绍逐步让新模型接收少量流量。
- **blue-green deployment（蓝绿部署）**：没有介绍两套服务之间切换。
- **model rollout strategy（模型发布策略）**：没有介绍模型版本上线方式。
- **service upgrade（服务升级）**：没有说明升级 vLLM、模型或配置的过程。
- **backward compatibility（向后兼容）**：没有讨论旧客户端是否还能调用新服务。
- **API compatibility（API 兼容性）**：没有讨论接口格式版本兼容。
- **model API contract（模型 API 契约）**：没有定义请求和响应必须遵守的约定。
- **service contract（服务契约）**：没有定义性能、错误和接口承诺。
- **request validation（请求校验）**：没有说明服务如何检查输入是否有效。
- **input validation（输入校验）**：没有讨论提示词、参数和模型名是否合法。
- **output validation（输出校验）**：没有讨论返回结果是否符合格式要求。
- **schema validation（结构校验）**：没有讨论结构化请求和响应的字段检查。
- **model selection（模型选择）**：没有说明应用如何在多个模型间选择。
- **routing（路由）**：没有讨论按模型、租户或负载把请求分发到不同实例。
- **model router（模型路由器）**：没有介绍在多个模型之间选择的组件。
- **request router（请求路由器）**：没有介绍把请求交给不同服务实例的组件。
- **gateway（网关）**：API 访问出现了，但没有讨论位于客户端和模型服务之间的网关。
- **API gateway（API 网关）**：没有介绍统一认证、限流和路由的入口。
- **proxy（代理）**：没有讨论代替客户端转发模型请求的组件。
- **reverse proxy（反向代理）**：没有讨论生产服务常见的网络入口。
- **service mesh（服务网格）**：没有讨论复杂部署中的服务通信管理。
- **orchestration（编排）**：没有讨论多个服务和实例如何被统一管理。
- **container orchestration（容器编排）**：没有介绍 Kubernetes 等系统如何管理 vLLM 服务。
- **cluster scheduling（集群调度）**：没有讨论在多节点 GPU 集群中安排任务。
- **resource scheduler（集群资源调度器）**：没有介绍集群级 GPU 分配。
- **node autoscaling（节点自动扩缩容）**：没有讨论按需求增减计算节点。
- **GPU pool（GPU 资源池）**：没有定义多个 GPU 组成的共享资源池。
- **quota management（配额管理）**：没有讨论多个应用如何分配服务额度。
- **service tenancy（服务租户）**：没有展开共享模型服务中的租户概念。
- **model catalog（模型目录）**：没有讨论可用模型清单。
- **model metadata（模型元数据）**：没有介绍模型名称、版本、精度和资源需求等信息。
- **model artifact（模型制品）**：没有定义可部署的权重文件和配置集合。
- **artifact storage（制品存储）**：没有讨论模型文件如何存储和分发。
- **model download cache（模型下载缓存）**：没有讨论本地重复使用已下载模型。
- **model loading time（模型加载时间）**：没有把加载权重时间单独列为性能因素。
- **initialization time（初始化时间）**：没有解释服务启动、加载和预热的总时间。
- **steady state（稳态）**：没有定义服务完成预热后的正常运行阶段。
- **cold path（冷路径）**：没有讨论首次加载或缓存未命中的路径。
- **hot path（热路径）**：没有讨论模型已加载并重复服务的路径。
- **request admission latency（请求接入延迟）**：没有拆解进入服务前的等待。
- **scheduler overhead（调度开销）**：没有讨论协调大量请求所需的额外计算。
- **API overhead（API 开销）**：没有讨论网络和接口处理带来的额外耗时。
- **model execution overhead（模型执行开销）**：没有区分核心计算之外的运行开销。
- **end-to-end serving overhead（端到端服务开销）**：没有综合网络、调度和返回过程的成本。
- **resource utilization efficiency（资源利用效率）**：没有把硬件利用率和有用输出直接关联。
- **throughput per GPU（每 GPU 吞吐量）**：没有说明单位 GPU 能完成多少服务工作。
- **tokens per GPU second（每 GPU 秒 token 数）**：没有介绍硬件归一化的生成效率指标。
- **cost efficiency（成本效率）**：没有讨论单位成本能服务多少请求或 token。
- **quality of service / QoS（服务质量保障）**：没有讨论不同请求的延迟和可靠性承诺。
- **service priority class（服务优先级类别）**：没有介绍不同用户或请求等级。
- **deadline（截止时间）**：没有讨论请求必须在何时完成。
- **real-time serving（实时服务）**：没有定义对响应时间有严格要求的场景。
- **near-real-time serving（近实时服务）**：没有区分可接受短暂等待的场景。
- **offline serving（离线服务）**：没有讨论非交互式批量输出。
- **interactive serving（交互式服务）**：没有讨论逐 token 返回对用户体验的影响。
- **user experience latency（用户体验延迟）**：没有把技术 latency 与用户感知等待区分开。
- **first-token experience（首 token 体验）**：没有讨论用户第一次看到输出的时间。
- **generation smoothness（生成流畅度）**：没有讨论 token 持续到达是否稳定。
- **service responsiveness（服务响应性）**：没有把快速接受并返回请求作为独立概念。
- **request fairness（请求公平性）**：没有讨论不同请求之间是否公平分配计算资源。
- **starvation（饥饿）**：没有讨论低优先级请求长期得不到执行。
- **head-of-line blocking（队头阻塞）**：没有讨论一个请求阻塞后续请求的问题。
- **work conservation（工作守恒）**：没有讨论资源空闲时是否尽可能处理等待任务。
- **scheduling policy（调度策略）**：没有列出 FIFO、优先级或其他策略。
- **FIFO（先进先出）**：没有解释按到达顺序处理请求。
- **fair-share scheduling（公平份额调度）**：没有解释按使用方分配服务资源。
- **deadline scheduling（截止时间调度）**：没有解释按时限安排请求。
- **preemption（抢占）**：没有讨论暂停一个请求以处理另一个请求。
- **request pause and resume（请求暂停与恢复）**：没有解释生成中的请求如何让出资源后继续。
- **memory reclamation（内存回收）**：没有说明请求完成后如何释放内存。
- **cache eviction（缓存淘汰）**：没有讨论内存不足时移除哪些缓存。
- **resource cleanup（资源清理）**：没有说明失败或取消后如何清理资源。
- **request cancellation cleanup（取消请求清理）**：没有解释取消生成后如何释放状态。
- **leak（资源泄漏）**：没有讨论未释放内存导致的长期问题。
- **stability（稳定性）**：没有把长时间运行不崩溃作为独立服务性质。
- **reproducibility（可复现性）**：没有讨论相同配置和请求能否得到相近结果。
- **deterministic inference（确定性推理）**：没有讨论固定采样设置下的输出一致性。
- **numerical accuracy（数值准确性）**：没有讨论低精度计算对结果的影响。
- **model correctness（模型正确性）**：没有区分运行成功与输出正确。
- **service correctness（服务正确性）**：没有区分服务返回结果与模型本身质量。
- **functional correctness（功能正确性）**：没有讨论 API 是否按契约工作。
- **performance correctness（性能正确性）**：没有讨论指标测量是否符合定义。
- **benchmark reproducibility（基准可复现性）**：没有说明比较性能时如何保持条件一致。
- **observed throughput（观测吞吐量）**：没有区分理论和实测吞吐量。
- **peak throughput（峰值吞吐量）**：没有说明最大压力下能达到的吞吐量。
- **sustained throughput（持续吞吐量）**：没有说明长时间运行可保持的吞吐量。
- **average latency（平均延迟）**：没有说明延迟的平均统计方式。
- **median latency（中位延迟）**：没有介绍 p50 延迟。
- **p95 latency（p95 延迟）**：没有介绍常用尾延迟指标。
- **p99 latency（p99 延迟）**：没有介绍极端慢请求指标。
- **latency distribution（延迟分布）**：没有讨论请求耗时的整体分布。
- **variance（方差）**：没有讨论服务时间波动。
- **jitter（抖动）**：没有讨论响应时间或 token 间隔的波动。
- **token latency distribution（token 延迟分布）**：没有讨论生成速度在不同 token 间的变化。
- **request arrival distribution（请求到达分布）**：没有讨论流量的突发或稳定特征。
- **load profile（负载曲线）**：没有说明测试或生产流量随时间如何变化。
- **workload characterization（工作负载刻画）**：没有解释如何描述请求长度、并发和到达率。
- **request length distribution（请求长度分布）**：没有讨论输入和输出长度的差异。
- **prompt diversity（提示多样性）**：没有讨论不同 prompt 对缓存和批处理的影响。
- **sequence packing（序列打包）**：没有讨论把不同长度序列有效放入批次。
- **padding（填充）**：没有解释批处理中短序列如何补齐长度。
- **ragged batch（不规则批次）**：没有讨论不同长度请求的批处理表示。
- **dynamic sequence length（动态序列长度）**：没有说明请求长度变化如何影响计算。
- **token-level scheduling（token 级调度）**：没有讨论按 token 生成阶段调度请求。
- **iteration-level scheduling（迭代级调度）**：没有讨论每轮生成如何重新安排批次。
- **batch fairness（批次公平性）**：没有讨论不同长度请求在批次中的公平性。
- **compute sharing（计算共享）**：没有具体说明多个请求如何共享 GPU 计算。
- **memory sharing（内存共享）**：没有具体说明多个请求如何共享缓存或权重。
- **weight sharing（权重共享）**：没有说明多个请求可以复用同一份模型权重。
- **prefix sharing（前缀共享）**：没有说明相同提示前缀如何共享计算。
- **request grouping（请求分组）**：没有解释系统按什么条件把请求放在一起。
- **batch formation（批次形成）**：没有解释等待多久、收集多少请求组成批次。
- **batch scheduling（批次调度）**：没有解释多个批次之间如何安排 GPU 时间。
- **microbatch（微批次）**：没有讨论把批次进一步切小的方式。
- **chunked prefill（分块预填充）**：没有讨论把长 prompt 分块处理。
- **long-context serving（长上下文服务）**：没有讨论长上下文对 KV cache 和吞吐的影响。
- **context parallelism（上下文并行）**：没有讨论长上下文跨设备计算。
- **sequence parallelism（序列并行）**：没有介绍沿序列维度分配计算。
- **expert parallelism（专家并行）**：没有讨论 MoE 模型的专家分布。
- **mixture of experts / MoE（混合专家模型）**：页面只说 LLM，没有涉及模型结构变体。
- **expert routing（专家路由）**：没有讨论 MoE 请求如何选择专家。
- **model architecture（模型架构）**：没有解释服务引擎面对不同模型架构的差异。
- **decoder-only model（仅解码器模型）**：没有具体说明常见生成式 LLM 结构。
- **encoder-decoder model（编码器—解码器模型）**：没有说明不同模型结构对服务的影响。
- **attention（注意力）**：没有解释语言模型中的注意力计算。
- **Transformer（Transformer）**：没有展开现代语言模型常见架构。
- **neural network（神经网络）**：页面只使用模型和权重，没有介绍底层模型结构。
- **parameter（参数）**：没有区分权重、参数和模型规模。
- **hyperparameter（超参数）**：没有介绍服务或生成配置与训练参数的区别。
- **checkpoint format（检查点格式）**：没有说明权重文件如何被读取。
- **model format（模型格式）**：没有讨论不同权重格式的兼容性。
- **safetensors（safetensors）**：没有提到常见安全权重格式。
- **weight conversion（权重转换）**：没有说明模型加载前可能需要转换格式。
- **model loading backend（模型加载后端）**：没有讨论负责读取权重的组件。
- **tokenizer loading（分词器加载）**：没有讨论模型服务启动时加载 tokenizer。
- **model configuration（模型配置）**：没有说明架构、词表和最大长度等配置。
- **generation engine（生成引擎）**：没有将文本生成执行部分单列。
- **text generation serving（文本生成服务）**：页面以 LLM inference 为主，但没有专门定义文本生成服务。
- **completion（补全）**：没有介绍文本补全请求形式。
- **chat completion（聊天补全）**：没有介绍对话式生成请求形式。
- **conversation state（对话状态）**：没有讨论多轮对话上下文如何管理。
- **chat template（聊天模板）**：没有讨论消息如何转换为模型 prompt。
- **system message（系统消息）**：没有解释对话请求中的系统指令。
- **user message（用户消息）**：没有解释对话请求中的用户输入。
- **assistant message（助手消息）**：没有解释模型生成的助手回复。
- **prompt formatting（提示格式化）**：没有说明文本如何整理成模型可接受的输入。
- **request normalization（请求规范化）**：没有说明不同客户端请求如何转换为统一格式。
- **response normalization（响应规范化）**：没有说明不同后端输出如何转换为统一响应。
- **compatibility layer（兼容层）**：没有讨论把不同模型或客户端适配到统一接口。
- **backend abstraction（后端抽象）**：没有讨论上层服务如何屏蔽底层执行差异。
- **plugin（插件）**：没有讨论扩展模型服务能力的插件机制。
- **custom backend（自定义后端）**：没有说明如何接入非默认执行后端。
- **extension point（扩展点）**：没有说明服务架构中可扩展的位置。
- **open source（开源）**：页面没有介绍 vLLM 的项目协作和许可证背景。
- **license（许可证）**：页面没有解释软件或模型的授权条件。
- **community project（社区项目）**：页面没有讨论项目生态。
- **documentation（文档）**：页面本身是概念说明，没有引导到工程文档。
- **installation（安装）**：没有说明如何安装 vLLM。
- **environment setup（环境设置）**：没有介绍 Python、CUDA、GPU 等运行环境配置。
- **dependency（依赖）**：没有列出服务软件依赖的库和驱动。
- **version compatibility（版本兼容性）**：没有讨论 vLLM、PyTorch、CUDA 和模型版本关系。
- **hardware compatibility（硬件兼容性）**：没有说明不同 GPU 是否支持相同运行方式。
- **operating system compatibility（操作系统兼容性）**：没有讨论本地部署的操作系统要求。
- **deployment target（部署目标）**：没有区分笔记本、服务器、云 GPU 和集群。
- **cloud GPU（云 GPU）**：云服务商被排除，但没有解释租用的云 GPU。
- **bare metal（裸机）**：没有讨论直接使用物理服务器。
- **virtual machine（虚拟机）**：没有讨论虚拟化环境中的模型服务。
- **edge deployment（边缘部署）**：local AI 邻域存在，但没有涉及边缘设备。
- **on-premises（本地机房部署）**：没有讨论企业自有服务器部署。
- **hybrid deployment（混合部署）**：没有讨论本地与云端结合。
- **remote inference（远程推理）**：没有明确区分本地调用与远程服务调用。
- **network locality（网络位置）**：没有讨论请求方和 GPU 距离对延迟的影响。
- **data transfer（数据传输）**：没有讨论输入输出在网络中的传输。
- **serialization cost（序列化成本）**：没有分析网络格式转换开销。
- **request payload（请求负载内容）**：没有定义请求中实际发送的数据。
- **response payload（响应负载内容）**：没有定义返回给客户端的数据。
- **payload size（负载大小）**：没有讨论长输入输出对网络和内存的影响。
- **network bandwidth（网络带宽）**：没有讨论大响应或多用户时的网络限制。
- **connection pooling（连接池）**：没有介绍客户端与服务端连接复用。
- **keep-alive（长连接）**：没有讨论 HTTP 连接保持。
- **request timeout policy（请求超时策略）**：没有讨论不同请求类型的超时设置。
- **server timeout（服务器超时）**：没有定义服务端等待上限。
- **client timeout（客户端超时）**：没有定义调用方等待上限。
- **retry storm（重试风暴）**：没有讨论失败时大量重试加剧过载。
- **circuit breaker（熔断器）**：没有讨论过载或故障时暂时停止调用。
- **bulkhead isolation（舱壁隔离）**：没有讨论隔离不同调用方资源池。
- **request deduplication（请求去重）**：没有讨论相同请求是否可以合并。
- **idempotency（幂等性）**：没有讨论重试同一请求的影响。
- **caching policy（缓存策略）**：没有定义缓存保留和失效方式。
- **cache invalidation（缓存失效）**：没有讨论模型版本或 prompt 变化后如何清除缓存。
- **model update（模型更新）**：没有讨论替换正在服务的模型权重。
- **hot reload（热加载）**：没有讨论不中断服务加载新配置或模型。
- **rolling update（滚动更新）**：没有讨论逐实例升级服务。
- **draining（排空）**：没有说明升级前如何让已有请求完成。
- **graceful shutdown（优雅关闭）**：没有讨论停止服务时如何处理在途请求。
- **in-flight request（在途请求）**：没有定义服务关闭或更新时正在处理的请求。
- **service restart（服务重启）**：没有讨论重启造成的加载和可用性影响。
- **process crash（进程崩溃）**：没有讨论运行时崩溃的恢复。
- **GPU failure（GPU 故障）**：没有讨论硬件故障对模型服务的影响。
- **node failure（节点故障）**：没有讨论分布式部署中的节点失效。
- **failover（故障切换）**：没有介绍切换到备用实例。
- **redundancy（冗余）**：没有讨论为可靠性准备额外实例。
- **disaster recovery（灾难恢复）**：没有讨论大范围故障后的恢复。
- **backup（备份）**：没有讨论模型权重和配置备份。
- **restore（恢复）**：没有讨论从备份恢复服务。
- **service state（服务状态）**：没有定义运行、降级、失败等整体状态。
- **model state（模型状态）**：没有定义未加载、加载中、就绪、卸载等状态。
- **readiness（就绪状态）**：没有把“可以接受请求”单列为状态。
- **liveness（存活状态）**：没有定义进程是否仍在运行。
- **health（健康状态）**：没有定义服务是否正常工作。
- **availability target（可用性目标）**：没有说明期望服务多长时间可用。
- **error rate（错误率）**：没有列出失败请求占比。
- **success rate（成功率）**：没有列出成功完成请求占比。
- **request drop rate（请求丢弃率）**：没有讨论过载时被丢弃的请求比例。
- **timeout rate（超时率）**：没有讨论超时请求比例。
- **OOM rate（内存不足率）**：没有讨论显存不足导致失败的比例。
- **quality monitoring（质量监控）**：没有讨论输出内容质量随时间变化。
- **drift（漂移）**：没有讨论请求分布或模型表现变化。
- **data drift（数据漂移）**：没有讨论线上输入与预期分布变化。
- **model drift（模型漂移）**：没有讨论更新后行为变化。
- **performance regression（性能回归）**：没有讨论版本升级后变慢。
- **capacity regression（承载回归）**：没有讨论升级后能处理的请求量下降。
- **resource leak（资源泄漏）**：没有讨论长期运行中资源逐渐丢失。
- **memory leak（内存泄漏）**：没有讨论内存持续增长。
- **profiling（性能剖析）**：没有介绍查找执行瓶颈的方法。
- **GPU profiling（GPU 性能剖析）**：没有介绍分析 GPU kernel 和利用率的方法。
- **memory profiling（内存剖析）**：没有介绍分析权重、缓存和激活占用的方法。
- **benchmark dashboard（基准看板）**：没有讨论长期展示性能指标。
- **operational dashboard（运维看板）**：没有讨论生产服务状态可视化。
- **alert threshold（告警阈值）**：没有说明何时触发性能告警。
- **SLA breach（服务等级违约）**：没有讨论指标低于承诺时的处理。
- **capacity alert（容量告警）**：没有讨论 GPU、队列或内存接近上限时告警。
- **queue depth（队列深度）**：没有列出等待请求数量这一指标。
- **active request count（活跃请求数）**：没有列出当前正在处理的请求数量。
- **in-flight token count（在途 token 数）**：没有讨论生成中的 token 状态总量。
- **GPU memory pressure（GPU 显存压力）**：没有把内存不足风险作为指标。
- **GPU utilization target（GPU 利用率目标）**：没有讨论希望 GPU 达到的利用率。
- **throughput target（吞吐量目标）**：没有讨论希望服务达到的处理量。
- **latency target（延迟目标）**：没有讨论希望服务达到的等待时间。
- **token rate target（词元速率目标）**：没有讨论希望达到的生成速率。
- **capacity target（承载目标）**：没有讨论希望支持的并发或请求量。
- **resource budget（资源预算）**：没有说明服务可使用的 GPU、内存或成本上限。
- **performance budget（性能预算）**：没有说明可接受的延迟或错误上限。
- **latency budget（延迟预算）**：没有把端到端等待时间分配给各阶段。
- **memory budget（内存预算）**：没有说明权重、缓存、激活可以各占多少内存。
- **GPU budget（GPU 预算）**：没有说明可供服务使用的 GPU 数量或时间。
- **service budget（服务预算）**：没有综合资源、成本和性能限制。
- **capacity envelope（容量边界）**：没有描述不同输入长度和并发下的可承载范围。
- **operating point（运行点）**：没有讨论服务在某一延迟—吞吐量组合下运行。
- **saturation（饱和）**：没有说明资源被完全占用后的状态。
- **overload（过载）**：没有说明请求需求超过服务能力的情况。
- **underutilization（利用不足）**：没有说明 GPU 空闲而吞吐量低的情况。
- **bottleneck diagnosis（瓶颈诊断）**：没有介绍如何判断限制来自 GPU、内存、调度还是网络。
- **performance tuning（性能调优）**：没有讨论调整批处理、并发和精度的方法。
- **capacity tuning（容量调优）**：没有讨论提升可承载请求量的方法。
- **latency tuning（延迟调优）**：没有讨论降低单请求等待时间的方法。
- **memory tuning（内存调优）**：没有讨论减少内存占用的方法。
- **GPU tuning（GPU 调优）**：没有讨论优化 GPU 计算使用的方法。
- **request tuning（请求调优）**：没有讨论控制输入长度、输出长度和并发。
- **workload tuning（工作负载调优）**：没有讨论调整请求分布来改善服务表现。
- **service configuration tuning（服务配置调优）**：没有讨论服务参数与性能的关系。
- **production readiness（生产就绪）**：没有系统说明上线前需要验证的条件。
- **deployment readiness（部署就绪）**：没有说明模型、硬件、API 和监控是否准备好。
- **operational readiness（运维就绪）**：没有说明告警、故障恢复和容量规划是否准备好。
- **documentation gap（文档缺口）**：本页是入门解释，工程实现和运维细节需要其他资料补充。

## Aliases / Synonyms

- vLLM ↔ vLLM engine ↔ vLLM serving engine ↔ vLLM inference engine
- vLLM ↔ serving and inference software ↔ model-serving software ↔ inference software
- serving ↔ model serving ↔ model service ↔ providing model access
- model serving ↔ serving models ↔ serving a language model ↔ model-serving workload
- inference ↔ model inference ↔ inference execution ↔ serving-time computation
- inference engine ↔ serving engine ↔ execution engine ↔ inference runtime
- model runtime ↔ local runtime ↔ inference runtime ↔ serving runtime
- large language model ↔ LLM ↔ language model（LLM 是 language model 的子集或特定规模类别，不是所有 language model 的完全同义词。）
- model weights ↔ weights ↔ learned values ↔ learned parameters
- application ↔ app ↔ client application ↔ caller（client 也可能专指调用库或网络客户端。）
- request ↔ model request ↔ API request ↔ serving request ↔ inference call
- API ↔ application programming interface ↔ model API ↔ serving interface ↔ inference interface
- API access ↔ model access ↔ application access ↔ access through an interface
- service ↔ model service ↔ inference service ↔ serving system
- model server ↔ inference server ↔ serving instance ↔ model service process
- GPU ↔ graphics processing unit ↔ accelerator（accelerator 范围比 GPU 更宽。）
- GPU / memory resources ↔ compute resources ↔ hardware resources ↔ execution resources
- memory ↔ memory resource ↔ available memory ↔ working memory（memory 不一定专指 GPU 显存。）
- VRAM ↔ GPU memory ↔ graphics memory ↔ 显存
- multiple requests ↔ concurrent requests ↔ request volume ↔ incoming traffic（这些词强调的维度不同，不完全等价。）
- request scheduling ↔ scheduling ↔ request coordination ↔ request dispatch
- scheduler ↔ request scheduler ↔ scheduling component ↔ resource scheduler
- batching ↔ batch processing ↔ request grouping ↔ batch inference（batch inference 还可能指离线批量推理。）
- batch ↔ request batch ↔ batch group ↔ grouped requests
- high throughput ↔ high-throughput serving ↔ throughput-oriented serving ↔ large serving capacity
- throughput ↔ service throughput ↔ serving throughput ↔ completed work per unit time
- tokens per second ↔ token generation rate ↔ generation rate ↔ TPS
- latency ↔ request latency ↔ response time ↔ request duration（response time 可能包含网络往返，语境需确认。）
- performance ↔ serving performance ↔ inference performance ↔ operational performance
- efficient ↔ resource-efficient ↔ high-efficiency ↔ low-waste
- efficient memory use ↔ memory efficiency ↔ efficient memory utilization ↔ memory-aware serving
- resource use ↔ resource utilization ↔ hardware utilization ↔ resource efficiency
- run a model ↔ execute a model ↔ model execution ↔ model inference execution
- load the model ↔ load model weights ↔ model loading ↔ weight loading
- model itself ↔ learned model ↔ language model ↔ model artifact（model artifact 还可能包含配置和 tokenizer。）
- model family ↔ model series ↔ family of model weights ↔ related model collection
- cloud provider ↔ cloud service provider ↔ hosted infrastructure provider ↔ infrastructure provider
- local model use ↔ local AI ↔ local model runtime ↔ local inference
- developer-friendly local runtime ↔ local developer runtime ↔ local model tool ↔ local-first tool
- server inference ↔ production-style inference ↔ production inference ↔ server-side inference
- usage pattern ↔ use pattern ↔ workload pattern ↔ serving scenario
- serving stack ↔ model-serving stack ↔ serving architecture ↔ application-to-GPU stack
- application layer ↔ application node ↔ caller layer ↔ client layer
- model serving layer ↔ serving layer ↔ model-service layer ↔ serving middleware
- model layer ↔ model node ↔ learned-model layer ↔ model execution component
- GPU layer ↔ accelerator layer ↔ hardware execution layer ↔ compute layer
- model output ↔ inference output ↔ service output ↔ response ↔ result
- generated output ↔ generated result ↔ generation result ↔ model response
- traffic controller ↔ request coordinator ↔ request scheduler（traffic controller 是页面明确标注为简化类比的说法。）
- traffic ↔ request traffic ↔ incoming requests ↔ application load
- destination ↔ target model ↔ model endpoint（在类比中 destination 不等同于实际模型组件。）
- application request path ↔ request path ↔ application-to-model path ↔ request-to-result flow
- performance concepts ↔ performance terms ↔ serving metrics vocabulary ↔ model-serving performance terms
- metric ↔ performance metric ↔ serving metric ↔ operational metric
- generation rate ↔ token rate ↔ output rate ↔ tokens per second（generation rate 也可以用于非 token 输出，需看上下文。）
- high-throughput LLM serving ↔ scalable LLM serving ↔ production LLM serving ↔ server LLM inference
- Ollama ↔ local model runtime ↔ local model management tool ↔ developer-friendly local AI tool
- vLLM vs Ollama ↔ serving-tool comparison ↔ local-runtime comparison ↔ model-runtime comparison
- local model management ↔ model management ↔ local model setup ↔ model lifecycle setup
- production-style workload ↔ production workload ↔ real-world serving workload ↔ operational workload
- model-serving software ↔ serving software ↔ model-serving tool ↔ serving tool
- serving and inference engine ↔ model-serving runtime ↔ inference-serving runtime ↔ model execution service
- model access point ↔ service endpoint ↔ model endpoint ↔ API endpoint
- model service boundary ↔ serving boundary ↔ API boundary ↔ access boundary
- application-facing ↔ client-facing ↔ API-facing ↔ caller-facing
- hardware-facing ↔ execution-facing ↔ GPU-facing ↔ backend-facing
- shared model service ↔ multi-tenant serving ↔ shared serving instance ↔ shared inference service
- shared resources ↔ pooled resources ↔ common GPU resources ↔ shared hardware capacity
- request processing ↔ request handling ↔ request execution ↔ request lifecycle
- request completion ↔ request result ↔ response return ↔ result return
- response ↔ reply ↔ returned result ↔ service output
- response time ↔ end-to-end latency ↔ time to result ↔ request duration
- resource allocation ↔ resource assignment ↔ hardware allocation ↔ compute allocation
- request queue ↔ service queue ↔ waiting queue ↔ pending requests
- queueing ↔ waiting ↔ request waiting ↔ queued execution
- request volume ↔ request count ↔ traffic volume ↔ workload volume
- concurrent requests ↔ active requests ↔ in-flight requests ↔ request concurrency
- application integration ↔ model integration ↔ service integration ↔ application-to-model connection
- serving interface ↔ model-serving API ↔ model access interface ↔ service endpoint
- inference interface ↔ model API ↔ generation API ↔ inference endpoint
- execution backend ↔ model backend ↔ GPU backend ↔ compute backend
- serving front end ↔ request-facing layer ↔ API-facing layer ↔ service gateway layer
- serving back end ↔ execution backend ↔ model execution layer ↔ hardware-facing layer
- request producer ↔ caller ↔ client ↔ application
- request consumer ↔ serving system ↔ model server ↔ service provider
- model consumer ↔ service consumer ↔ application user ↔ model user
- serving provider ↔ model service provider ↔ runtime provider ↔ inference provider
- model owner ↔ model provider ↔ weight provider ↔ model publisher
- infrastructure owner ↔ cloud provider ↔ hardware provider ↔ deployment operator
- noun separation ↔ concept separation ↔ role separation ↔ boundary clarification
- common confusion ↔ conceptual confusion ↔ category confusion ↔ role confusion
- workload fit ↔ application fit ↔ production fit ↔ resource fit
- performance fit ↔ latency fit ↔ throughput fit ↔ capacity fit
- local fit ↔ local-use fit ↔ developer fit ↔ local-runtime fit
- service readiness ↔ serving readiness ↔ runtime readiness ↔ inference readiness
- model readiness ↔ model loaded ↔ model available ↔ inference-ready model
- GPU readiness ↔ hardware readiness ↔ compute readiness ↔ resource readiness
- service operation ↔ serving operation ↔ model service operation ↔ online serving
- model operation ↔ model execution ↔ inference operation ↔ runtime execution
- latency-oriented ↔ response-time-oriented ↔ low-latency ↔ interactive-serving-oriented
- throughput-oriented ↔ capacity-oriented ↔ high-throughput ↔ batch-serving-oriented
- request-level performance ↔ per-request performance ↔ single-request latency
- system-level performance ↔ service-level performance ↔ aggregate serving performance
- throughput metric ↔ work-per-time metric ↔ aggregate work metric ↔ service capacity metric
- latency metric ↔ request-time metric ↔ response-time metric ↔ time-to-result metric
- token-rate metric ↔ generation-rate metric ↔ tokens-per-second metric ↔ output-rate metric
- resource metric ↔ GPU metric ↔ memory metric ↔ utilization metric
- model-serving decision ↔ runtime choice ↔ tool choice ↔ serving architecture decision
- tool positioning ↔ software positioning ↔ usage positioning ↔ common fit
- model-as-a-service ↔ inference-as-a-service ↔ model access service ↔ served model
- direct model loading ↔ load the model directly ↔ direct runtime execution ↔ direct inference
- one-time loading ↔ initial model loading ↔ weight initialization ↔ model startup loading
- loaded model ↔ ready model ↔ resident model ↔ active model instance
- serving instance ↔ service instance ↔ model server instance ↔ runtime instance
- model execution path ↔ inference path ↔ request execution path ↔ serving pipeline
- request-to-result flow ↔ request lifecycle ↔ serving workflow ↔ inference workflow
- efficient request execution ↔ efficient inference execution ↔ optimized request handling ↔ efficient serving
- resource utilization ↔ hardware utilization ↔ GPU utilization ↔ compute utilization
- memory footprint ↔ memory usage ↔ resource footprint ↔ serving footprint
- resource pressure ↔ capacity pressure ↔ memory pressure ↔ GPU pressure
- serving bottleneck ↔ performance bottleneck ↔ execution bottleneck ↔ resource bottleneck
- serving optimization ↔ performance optimization ↔ inference optimization ↔ runtime tuning
- real-world serving ↔ live serving ↔ production serving ↔ operational serving
- live service ↔ online service ↔ running service ↔ operational service
- ongoing service ↔ continuous service ↔ long-running service ↔ persistent service
- request-serving architecture ↔ serving architecture ↔ service architecture ↔ inference-serving architecture
- simplified serving stack ↔ conceptual serving stack ↔ basic stack diagram ↔ serving-layer model
- stack node ↔ stack component ↔ serving component ↔ architecture node
- application node ↔ application component ↔ caller component ↔ client component
- API node ↔ API component ↔ interface component ↔ access node
- vLLM node ↔ vLLM layer ↔ serving engine node ↔ inference engine layer
- model node ↔ model component ↔ learned model layer ↔ model execution node
- GPU node ↔ hardware node ↔ accelerator node ↔ execution resource node
- application request as input ↔ request input ↔ serving input ↔ model-service input
- model result as output ↔ inference output ↔ service output ↔ returned output
- request scheduling and batching ↔ scheduling and batching ↔ request coordination and grouping ↔ batch scheduling
- efficient hardware use ↔ hardware utilization efficiency ↔ compute efficiency ↔ GPU efficiency
- resource estimation ↔ capacity estimation ↔ hardware sizing ↔ serving capacity planning
- service capacity ↔ serving capacity ↔ inference capacity ↔ workload capacity
- application demand ↔ serving demand ↔ request demand ↔ model access demand
- steady request load ↔ stable traffic ↔ sustained workload ↔ regular request stream
- request burst ↔ traffic burst ↔ burst load ↔ sudden request increase
- service reliability ↔ serving reliability ↔ runtime reliability ↔ inference-service reliability
- service quality ↔ quality of service ↔ operational quality ↔ model-service quality
- output quality ↔ response quality ↔ generation quality ↔ model result quality
- model quality ↔ model capability ↔ learned-model quality ↔ inference quality
- performance measurement ↔ benchmark ↔ serving benchmark ↔ performance test
- load test ↔ capacity test ↔ stress test ↔ serving performance test
- performance result ↔ benchmark result ↔ measured metric ↔ observed performance
- service readiness ↔ production readiness ↔ deployment readiness ↔ operational readiness
- model-serving performance ↔ latency, tokens per second, throughput ↔ service-speed and capacity measures
- API vs serving engine ↔ interface vs implementation ↔ access boundary vs execution software
- model vs model weights ↔ learned model vs learned numerical values ↔ model artifact vs parameter data
- vLLM vs LLM ↔ serving software vs language model ↔ runtime vs learned model
- vLLM vs Ollama ↔ high-throughput serving vs local model runtime ↔ production-style serving vs developer-friendly local use
- vLLM vs cloud provider ↔ serving software vs infrastructure provider ↔ engine vs hosted infrastructure
- GPU vs memory ↔ compute hardware vs storage capacity ↔ accelerator vs memory resource
- latency vs throughput ↔ per-request time vs work-per-time ↔ responsiveness vs aggregate capacity
- tokens per second vs throughput ↔ generation rate vs overall serving work ↔ token output rate vs completed workload

## Do Not Confuse Candidates

- **vLLM vs LLM**：vLLM 是服务／推理软件；LLM 是被运行的语言模型和其学习到的权重。vLLM runs LLMs，但 vLLM 本身不是 LLM。
- **vLLM vs model weights**：vLLM 是执行软件；model weights 是训练后保存在模型中的数值。软件会加载和运行权重，但不是权重。
- **vLLM vs model family**：vLLM 不是一系列模型权重，也不是模型家族或模型架构。
- **vLLM vs API**：vLLM 可以在 API 后面提供模型服务；API 是应用访问服务的边界，vLLM 是边界后面的服务／推理实现。
- **vLLM vs cloud provider**：vLLM 是软件；cloud provider 是提供服务器、GPU 和托管基础设施的服务商。
- **vLLM vs GPU**：vLLM 使用 GPU 运行模型；GPU 是硬件，不是 vLLM。
- **vLLM vs memory**：vLLM 管理或使用内存资源；memory 是保存权重和计算数据的空间。
- **vLLM vs Ollama**：两者都可用于模型运行或服务，但页面把 Ollama 定位为本地模型使用、管理和开发者友好运行时，把 vLLM 定位为高吞吐量、服务器／生产式推理工具；二者不是完全相同的产品定位。
- **model serving vs model**：model serving 是把模型提供给应用调用的过程和软件；model 是被训练出来的学习机制与权重。
- **serving software vs inference engine**：serving software 的范围可包括 API、调度和资源管理；inference engine 更强调执行模型推理的核心引擎，页面中 vLLM 同时承担两种角色。
- **inference vs serving**：inference 是对输入执行模型计算；serving 还包括接收请求、调度、批处理、资源管理和提供接口。
- **API vs endpoint**：API 是一套调用约定和边界；endpoint 是具体可访问的地址或入口。
- **API vs backend**：API 是外部调用接口；backend 是实现接口和业务逻辑的后端软件。
- **application vs API**：application 是使用模型的程序；API 是它用来调用模型服务的入口。
- **application vs model**：application 是完整的用户或业务程序；model 是其中可能被调用的学习组件。
- **model weights vs GPU memory**：weights 是模型数据；GPU memory 是放置数据并进行计算的硬件空间。
- **GPU vs memory**：GPU 主要提供并行计算能力；memory 主要保存权重、输入、缓存和中间数据。
- **GPU vs GPU / VRAM**：GPU 是处理器硬件；VRAM 是与 GPU 关联的显存，二者相关但不是同一资源。
- **model runtime vs model**：runtime 是执行模型的软件环境；model 是 runtime 要运行的学习模型。
- **model runtime vs model-serving engine**：runtime 可以只关注本地执行；serving engine 还要处理多请求、调度和服务接口。
- **local runtime vs cloud provider**：local runtime 是本地运行模型的软件；cloud provider 是提供远程基础设施的公司或平台。
- **local AI vs local runtime**：local AI 是更宽的使用方式或场景；local runtime 是支持本地运行的软件环境。
- **server vs cloud provider**：server 可以指运行服务的进程或机器；cloud provider 是提供服务器和基础设施的主体。
- **server inference vs cloud inference**：server inference 描述推理作为服务器服务运行；它不一定意味着使用云端基础设施。
- **production-style inference vs local development**：前者强调真实应用流量、并发和服务承载；后者通常强调开发者在本地试用或测试。
- **model management vs model serving**：model management 关注下载、选择和维护模型；model serving 关注让应用持续调用模型。
- **request vs response**：request 是应用发给服务的输入；response 是服务返回的输出。
- **input vs output**：input 是系统接收的信息；output 是系统处理后返回的结果。
- **request handling vs model execution**：request handling 包含接收、排队和返回；model execution 只是其中实际运行模型的计算部分。
- **request scheduling vs batching**：scheduling 决定请求何时或以什么顺序执行；batching 把适合的请求组合起来，二者常配合但不是同义词。
- **batching vs concurrency**：batching 是把请求成组处理；concurrency 是同时处于处理中的请求数量。
- **throughput vs tokens per second**：throughput 统计整体服务在一段时间内完成的工作；tokens per second 关注生成 token 的速率，统计口径可能是单请求或聚合。
- **throughput vs capacity**：throughput 是观测到的单位时间处理量；capacity 是系统理论上或在条件下可承载的工作量。
- **latency vs throughput**：latency 关注一次请求花多久；throughput 关注一段时间完成多少工作。
- **latency vs response time**：页面把 latency 解释为请求耗时；response time 可能包含网络、排队、执行和返回，具体口径要确认。
- **high throughput vs low latency**：高吞吐量不保证每个请求都低延迟；批处理可能提高总处理量，却增加某些请求的等待。
- **generation rate vs throughput**：generation rate 主要是生成 token 的速度；throughput 是服务整体处理量，可能还包括请求数、输入 token 和输出 token。
- **performance vs quality**：performance 关注速度、容量和资源效率；quality 关注模型或输出是否正确、有用和符合需求。
- **serving performance vs model quality**：服务性能可能很好，但模型输出质量仍可能不符合需求；两者需要分别评估。
- **model quality vs service quality**：model quality 是模型能力；service quality 还包括延迟、可用性、错误率和稳定性。
- **model output vs service output**：model output 是模型生成的结果；service output 还可能包含 API 包装、状态和元数据。
- **model vs product**：model 是学习到的能力；product 还包含界面、规则、数据、服务、运维和用户体验。
- **model vs model family**：model 是一个具体模型；model family 是一组相关模型或权重版本。
- **language model vs LLM**：language model 是广义语言模型；LLM 通常指规模较大的语言模型，不是所有 language model 都是 LLM。
- **model weights vs model checkpoint**：weights 是学习到的数字；checkpoint 通常是保存这些数字及相关状态的文件或快照。
- **runtime vs infrastructure**：runtime 是软件执行环境；infrastructure 是承载软件的机器、GPU、网络和存储。
- **inference engine vs GPU**：inference engine 安排和执行模型计算；GPU 提供其中的硬件加速。
- **serving stack vs serving engine**：serving stack 是从应用、API 到模型和 GPU 的完整层次；serving engine 只是其中一个核心软件组件。
- **application layer vs model layer**：application layer 发起业务请求；model layer 提供被运行的学习模型。
- **model layer vs GPU layer**：model layer 是软件模型；GPU layer 是执行模型计算的硬件资源。
- **API access vs model access**：API access 强调通过接口调用；model access 是更宽泛的“能够使用模型”。
- **service endpoint vs model**：endpoint 是网络入口；model 是被入口调用的学习组件。
- **traffic controller vs actual scheduler**：traffic controller 是页面明确标注为简化的交通类比；实际 scheduler 需要根据资源和请求状态做技术决策。
- **traffic vs request**：traffic 是请求的整体流量；request 是其中一次具体调用。
- **destination vs engine**：类比中 model 是 destination or engine；真实技术中模型和执行引擎是不同组件。
- **resource use vs resource capacity**：resource use 是当前用了多少；resource capacity 是最多可提供多少。
- **memory efficiency vs memory capacity**：memory efficiency 是利用得好不好；memory capacity 是空间有多大。
- **GPU utilization vs throughput**：GPU 利用率高不一定代表有效吞吐量高，可能是在做低效或等待操作。
- **request volume vs request rate**：request volume 是请求总量；request rate 是单位时间进入的请求量。
- **concurrent requests vs request volume**：concurrent requests 是同时在途的数量；request volume 可以是一个时间段内的总数。
- **request queue vs request scheduling**：queue 是等待中的请求集合；scheduling 是决定如何安排这些请求的过程。
- **request processing vs request completion**：processing 是整个处理过程；completion 是处理结束并得到结果的时刻。
- **request result vs model result**：request result 是一次 API 调用的返回；model result 是模型计算本身产生的结果。
- **model serving vs model deployment**：serving 强调持续接收请求并提供结果；deployment 强调把模型和软件发布到可运行环境。
- **deployment vs operation**：deployment 是上线或更新过程；operation 是服务上线后的持续运行和维护。
- **production workload vs benchmark workload**：production workload 来自真实应用；benchmark workload 是为了测量性能设计的测试负载。
- **load test vs stress test**：load test 测试正常或预期负载；stress test 通常把系统推到超出正常容量。
- **benchmark vs production metric**：benchmark 是受控比较测试；production metric 是在线真实服务中采集的指标。
- **average latency vs tail latency**：平均延迟描述整体平均；tail latency 关注最慢的一部分请求。
- **first-token latency vs end-to-end latency**：首 token 延迟只到第一个输出单位；端到端延迟通常到完整响应结束。
- **prefill vs decode**：prefill 处理输入上下文；decode 逐步生成输出 token，页面没有展开二者。
- **token vs word**：token 是模型处理的文本单位，不一定等于自然语言中的一个单词。
- **tokens per second vs words per second**：token 速率按模型词元计数，不等于人类阅读中的单词速率。
- **model weights vs parameters**：weights 是参数数值；parameters 可以指这些可学习数值的集合或单个参数。
- **parameters vs hyperparameters**：参数通常由训练学出；超参数通常在训练或服务前由人设定。
- **memory vs KV cache**：memory 是泛称；KV cache 是生成过程中存储注意力中间状态的一类内存数据。
- **batching vs continuous batching**：页面只说一般 batching；continuous batching 是更具体的动态请求调度机制。
- **high throughput vs high concurrency**：高并发可以帮助提高吞吐量，但二者不是同一个指标。
- **efficient serving vs cheap serving**：高效是时间和资源利用好，不必然等同于绝对成本低。
- **resource efficiency vs energy efficiency**：资源效率可包括 GPU、内存和时间；能效专指单位能耗的有效产出。
- **local model use vs local model ownership**：本地运行不代表模型权重一定由用户拥有。
- **cloud provider vs hosted model API**：云服务商提供基础设施；托管模型 API 是在其上提供具体模型调用的服务。
- **Ollama vs cloud API**：Ollama 是本地运行时／管理工具；云 API 是远程服务入口，二者不在同一层。
- **vLLM vs cloud API**：vLLM 是可用于搭建服务的软件；cloud API 是别人已经部署好的远程调用服务。
- **API itself vs API gateway**：API 是调用约定；API gateway 是可能负责认证、限流和路由的中间组件。
- **server process vs server machine**：server process 是软件进程；server machine 是运行它的物理或虚拟机器。
- **model server vs model-serving software**：model server 可指运行中的实例；model-serving software 指实现服务能力的软件类别。
- **serving tool vs model tool**：serving tool 运行并暴露模型；model tool 可能只是管理、转换或评估模型，范围更宽。
- **runtime constraints vs performance metrics**：runtime constraints 是资源和环境限制；performance metrics 是用来测量表现的数值。
- **GPU / VRAM vs model weights**：GPU/VRAM 是运行资源；model weights 是被运行的数据。
- **quantization vs batching**：quantization 改变权重或数值表示以节省资源；batching 改变请求组织方式以提高处理效率。
- **model serving vs model training**：serving 使用已训练模型处理请求；training 调整模型参数以学习规律。页面只聚焦 serving 和 inference。
- **inference vs training**：inference 是使用模型；training 是产生或更新模型权重的过程。
- **production inference vs offline inference**：production inference 通常面向在线请求；offline inference 可以批量处理而不要求即时响应。
- **service performance vs model computation speed**：服务性能包含排队、API、网络和资源管理；模型计算速度只是其中一部分。
- **application request vs model input**：应用请求可能包括模型名、参数和元数据；model input 是真正送进模型的内容。
- **API response vs generated text**：API response 可能包含状态、字段和元数据；generated text 只是其中的内容。
- **simple explanation vs implementation detail**：页面的 traffic controller 和 serving stack 是入门级简化模型，不等于 vLLM 的完整内部实现。
- **related concept vs page-defined concept**：链接到 Quantization、Runtime Constraints、GPU/VRAM 等只表示相关学习方向，本页没有完整定义它们。
- **video label vs actual video**：页面标记为 Video，但明确写着 no video resource attached；不要把占位区当成已附加的视频资源。
- **Model Serving & Local AI vs vLLM**：前者是模块／主题领域；vLLM 是其中一个具体服务与推理工具。
- **remember-this statement vs formal specification**：页面最后的记忆句是教学摘要，不是 vLLM 的完整技术规格或性能保证。

## Notes

- 本文件是 Module 10 Topic「vLLM」的 raw glossary 收集稿，目标是最大化保留正文中的专业术语、机制词、流程节点、指标、缩写、标题词、对比词、别名和易混淆概念。
- 候选按 `vllm.html` 的页面结构和正文顺序展开：短定义、服务问题、交通控制器类比、vLLM 与 LLM 对比、vLLM 与 Ollama 定位比较、服务栈、性能概念、否定性边界、相关概念、记忆句和视频占位。
- 页面明确把 vLLM 定义为 serving and inference engine；它位于 applications 与 model weights 之间，负责接收请求、执行 inference，并利用 GPU／memory resources。
- 页面主线可以简化为：Application → API → vLLM → LLM / Model → GPU / Memory；另一张服务栈图写作 Application → API → Model Serving → vLLM → Model → GPU。
- 页面明确区分了 vLLM、LLM、model family、cloud provider 和 API：vLLM 是软件，LLM 是语言模型，model family 是模型权重系列，cloud provider 是基础设施提供者，API 是访问边界。
- 页面解释“为什么不能只直接加载模型”：真实服务通常要面对 multiple requests、efficient memory use、request scheduling、batching、high throughput 和 API access。
- 页面使用 “traffic controller for model requests” 作为 beginner-friendly mental model，并特别标注 “This analogy is simplified”；因此 traffic controller 只能作为类比候选，不应当被当成 vLLM 的正式组件名。
- 页面把 Ollama 的 common fit 写作 local model use、model management 和 developer-friendly local runtime；把 vLLM 的 common fit 写作 high-throughput LLM serving 和 server / production-style inference workloads。
- 页面明确写出二者都可被看作 model runtimes / serving tools，但 optimized for different usage patterns；这是一种定位比较，不是说两者在所有部署和性能条件下绝对互斥。
- 页面性能部分只明确给出三个指标候选：LATENCY、TOKENS PER SECOND 和 THROUGHPUT；本文件额外保留了可能需要后续定义的更细粒度指标作为 Potential Missing Concepts。
- `GPU / MEMORY`、`GPU`、`GPU / VRAM` 和 `memory` 在页面中承担不同粒度的资源表达：GPU 更偏计算硬件，memory 更偏运行时存储空间，VRAM 是 GPU 关联显存。
- “vLLM runs models. It is not the model itself.” 是本页最重要的边界句之一；应与 “vLLM ≠ LLM” 一起保留，避免把 serving software 当作 model weights。
- 页面没有展开 vLLM 的具体内部机制，因此 PagedAttention、continuous batching、KV cache、tensor parallelism 等放入 Potential Missing Concepts，而不是伪装成正文明确解释过的内容。
- 页面没有给出安装命令、API schema、部署配置、模型兼容表、GPU 型号、基准数字、许可证、集群方案或生产运维步骤；这些缺口均保留在 Potential Missing Concepts 供后续主题或工程资料补充。
- 本 raw 文件中的 Glossary Candidates 有意保留重复和近义的候选，包括同一术语在标题、正文、图示节点和对比段落中的多次出现；后续整理阶段再决定是否合并、排序或降权。
- Aliases / Synonyms 同样保留了不完全同义但容易被并列使用的工程说法，并用括号标出需要谨慎理解的地方；它们不是最终术语规范。
- Do Not Confuse Candidates 以页面明确边界和工程上常见混淆为主，尤其关注 vLLM vs LLM、API、GPU、Ollama、cloud provider、latency、throughput、tokens per second 和 model weights。
- 页面相关链接包括 Model Serving、Ollama、Runtime Constraints、Latency、Tokens per Second 和 Quantization；链接只表示概念邻域，不代表这些主题在本页有完整定义。
- 页面视频区写明 “No video resource attached”，并说明真实来源可用后再添加视频；video、independent explainer 和 no video resource attached 因此作为低优先级页面词保留。
- 中文解释采用面向初学者的直白表达；同一英文词可能对应多个中文译法，raw 阶段不做最终术语统一。
- Source integrity note：本文件只根据本地 `vllm.html` 正文及其可见页面标签整理，没有修改网站文件、外部站点或 GitHub。
