# Topic

Open vs Closed / Local Models

Module/Topic/Source File

- Module: 13 · AI Providers & Models
- Topic: Open vs Closed / Local Models
- Source File: `open-closed-local-models.html`

## Glossary Candidates

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Open vs Closed / Local Models | 开放模型与封闭模型 / 本地模型 | A comparison of model access, weight availability, and inference location. | 比较模型能不能拿到、权重是否公开，以及模型在哪里运行。 |
| AI Providers & Models | AI 提供商与模型 | A topic area about companies, services, and models that provide AI capabilities. | 介绍提供 AI 能力的公司、服务和模型。 |
| model | 模型 | A learned system that produces outputs from inputs. | 学会规律、可以根据输入给出结果的一套程序。 |
| AI model | AI 模型 | A model used to perform an artificial-intelligence task. | 用来完成 AI 任务的模型。 |
| capability | 能力 | What a model or system can do. | 模型或系统能够完成的事情。 |
| model access | 模型访问；模型获取方式 | Who can obtain or use a model and under what terms. | 谁能拿到或使用模型，以及需要遵守什么条件。 |
| access | 访问；获取权限 | The ability or permission to use something. | 能够使用某个东西的机会或权限。 |
| model weights | 模型权重 | Learned numerical values that define much of a model’s behavior. | 模型训练后保留下来的大量数字，决定模型如何工作。 |
| weights | 权重 | Learned values inside a model. | 模型内部学到的数值。 |
| weight availability | 权重可获得性 | Whether model weights can be obtained by users. | 用户能不能拿到模型权重。 |
| weight distribution | 权重分发 | How model weights are made available to users. | 模型权重以什么方式提供给使用者。 |
| weight distribution terms | 权重分发条款 | Conditions governing how weights may be accessed or used. | 规定权重如何获取和使用的条件。 |
| model authorship | 模型作者归属 | Who created or trained a model. | 谁创建或训练了这个模型。 |
| infrastructure | 基础设施 | Hardware and software used to run a service or model. | 运行模型所需的服务器、硬件和软件环境。 |
| infrastructure control | 基础设施控制权 | How much control a user has over the hardware and software environment. | 用户能控制运行模型的硬件和软件到什么程度。 |
| inference | 推理；推断 | Running a trained model to produce a result. | 使用已经训练好的模型生成结果。 |
| inference location | 推理位置 | Where the computation for an inference request happens. | 一次模型计算实际发生在哪里。 |
| where it runs | 运行位置 | The hardware or environment that performs inference. | 执行推理的设备或环境。 |
| Cloud | 云端；云 | Remote provider infrastructure used over a network. | 通过网络使用的远程服务商基础设施。 |
| cloud deployment | 云端部署 | Running a model on provider or other remote infrastructure. | 把模型放在服务商或其他远程服务器上运行。 |
| cloud model | 云端模型 | A model whose inference runs on remote infrastructure. | 推理主要在远程服务器上完成的模型。 |
| local | 本地 | Running on hardware controlled by the user. | 在用户自己控制的设备上运行。 |
| local model | 本地模型 | A model whose inference runs on user-controlled hardware. | 在自己的电脑、工作站或本地服务器上运行推理的模型。 |
| local inference | 本地推理 | Performing inference on a local device or server. | 在自己的设备或本地服务器上完成模型计算。 |
| self-hosted | 自托管 | Running software or a model on infrastructure managed by oneself. | 自己负责部署和管理运行模型的基础设施。 |
| self-hosted model | 自托管模型 | A model operated on infrastructure controlled by the user or organization. | 在自己控制的环境中运行和管理的模型。 |
| user-controlled hardware | 用户控制的硬件 | A laptop, desktop, workstation, or server controlled by the user. | 用户自己拥有或管理的电脑、工作站或服务器。 |
| laptop | 笔记本电脑 | A portable computer that may run smaller local models. | 可能运行较小本地模型的便携电脑。 |
| desktop | 台式电脑 | A personal computer that can provide local compute. | 可以为本地模型提供计算能力的个人电脑。 |
| workstation | 工作站 | A more capable local computer for demanding workloads. | 性能较强、可处理更重任务的本地电脑。 |
| local server | 本地服务器 | A server operated in a local or privately controlled environment. | 在本地或私有环境中运行的服务器。 |
| closed model | 封闭模型 | A model whose weights are generally not provided for direct user operation. | 通常不把权重直接交给用户运行的模型。 |
| closed / hosted | 封闭 / 托管 | A model accessed through a provider-managed product or service. | 通过提供商管理的产品或服务来使用的模型。 |
| hosted model | 托管模型 | A model operated by a provider and exposed through a service. | 由服务商运行、通过服务提供给用户的模型。 |
| closed / hosted model | 封闭式托管模型 | A model with restricted weights that users access through hosted services. | 权重受限制、用户通过托管服务使用的模型。 |
| model weights are not provided | 不提供模型权重 | Users cannot normally download and run the model weights directly. | 用户通常不能下载权重后自己直接运行。 |
| direct model operation | 直接运行模型 | Running model weights yourself instead of calling a hosted service. | 不调用远程服务，而是自己运行模型权重。 |
| consumer product | 面向消费者的产品 | A user-facing application that provides model capabilities. | 普通用户直接使用的 AI 应用或产品。 |
| API | 应用程序编程接口 | A programmatic interface for sending requests to a service. | 软件通过它向服务发送请求、获取结果的接口。 |
| cloud platform | 云平台 | A provider-operated platform for computing and services. | 服务商提供的远程计算和服务平台。 |
| provider | 提供商 | A company or organization that offers a model or service. | 提供模型、API 或产品的公司或组织。 |
| provider-managed infrastructure | 提供商管理的基础设施 | Hardware and operations managed by the service provider. | 由服务商负责维护的服务器、网络和运行环境。 |
| provider dependency | 提供商依赖 | Reliance on one provider’s product, API, or infrastructure. | 使用被某一家服务商的产品、接口或基础设施限制。 |
| usage-based cost | 按使用量计费 | A price that changes with requests, tokens, or other usage. | 用得越多，费用通常越高的收费方式。 |
| data consideration | 数据考量 | A question about how data is sent, stored, or processed. | 需要考虑数据被怎样传输、保存或处理。 |
| governance consideration | 治理考量 | A question about policy, control, compliance, or accountability. | 需要考虑政策、合规、控制权和责任的问题。 |
| data and governance considerations | 数据与治理考量 | Privacy, compliance, control, and accountability issues around model use. | 使用模型时有关隐私、合规、控制和责任的综合问题。 |
| network | 网络 | The connection used to reach a remote service. | 连接本地设备和远程服务的通信网络。 |
| service access | 服务访问 | The ability to reach and use a hosted service. | 能连接并使用远程托管服务。 |
| offline use | 离线使用 | Using a model without sending requests to a remote service. | 不联网或不调用远程模型服务也能使用。 |
| remote model API | 远程模型 API | An API endpoint that runs a model on remote infrastructure. | 在远程服务器运行模型、供本地程序调用的接口。 |
| open-weight | 开放权重 | Model weights available under stated terms or a license. | 模型权重按照明确条款或许可证提供。 |
| open-weight model | 开放权重模型 | A model whose weights can be obtained under stated conditions. | 可以按规定获取模型权重的模型。 |
| open-weight available | 提供开放权重 | Weights or downloadable variants are published for users. | 发布了可供用户获取的权重或下载版本。 |
| stated license | 明示许可证 | A license that explains permitted and restricted uses. | 说明可以怎样使用、不能怎样使用的许可证。 |
| terms of use | 使用条款 | Rules that govern how a model or service may be used. | 规定模型或服务使用方式的规则。 |
| license | 许可证；许可协议 | Legal terms defining rights and restrictions for use. | 规定使用权利和限制的法律文件。 |
| obtain the weights | 获取权重 | Download or otherwise receive the model’s learned weights. | 下载或以其他方式拿到模型内部的权重。 |
| downloadable variant | 可下载变体 | A model version made available for download. | 可以下载到本地使用的模型版本。 |
| compatible software | 兼容软件 | Software that can load or run a model in its format. | 能读取并运行模型格式的软件。 |
| compatible hardware | 兼容硬件 | Hardware capable of meeting a model’s runtime needs. | 能满足模型运行要求的硬件。 |
| local-friendly | 适合本地运行 | Practical to run on commonly available local hardware. | 在常见本地设备上比较容易实际运行。 |
| open-weight ≠ open-source | 开放权重不等于开源 | Having weights available does not necessarily mean all source is available. | 能拿到权重，不代表训练代码和全部源代码都公开。 |
| open-weight ≠ automatically local-friendly | 开放权重不自动等于适合本地 | Available weights may still require too much memory or compute. | 权重公开了，也可能因为太大而无法在自己的电脑上运行。 |
| open-source | 开源 | A broader idea involving source availability and licensing rights. | 通常不只开放权重，还涉及源代码和更广泛的授权权利。 |
| source availability | 源代码可获得性 | Whether the software or training source is available for inspection or use. | 用户能不能查看、取得或使用相关源代码。 |
| licensing rights | 许可权利 | Rights granted by a license, such as use, modification, or redistribution. | 许可证授予的使用、修改或再分发等权利。 |
| actual license | 实际许可证 | The specific legal license attached to the model or release. | 这个模型版本真正附带的具体许可证。 |
| model card | 模型卡片 | Documentation describing a model’s uses, limits, and requirements. | 介绍模型用途、限制、风险和要求的说明文档。 |
| deployment requirement | 部署要求 | Hardware, software, license, or operational conditions needed to run a model. | 部署模型前必须满足的硬件、软件、许可或运行条件。 |
| local-capable | 具备本地运行能力 | Able to run locally under a particular setup. | 在特定设备和软件条件下可以在本地运行。 |
| practical test | 实际可行性测试 | A check of whether a model can really run in the intended environment. | 检查模型在目标设备上是否真的跑得起来。 |
| supported format | 支持的格式 | A file or representation format accepted by the runtime. | 运行时能够读取的模型文件格式。 |
| runtime | 运行时；运行环境 | Software that loads and executes a model. | 负责加载模型并执行推理的软件。 |
| compatible runtime | 兼容运行时 | A runtime that supports the model’s format and operations. | 支持该模型格式和运算方式的运行软件。 |
| serving stack | 服务栈 | The software components used to serve model inference. | 用来提供模型推理服务的一整套软件组件。 |
| serving system | 服务系统 | A system that receives requests and returns model outputs. | 接收请求、运行模型并返回结果的系统。 |
| Ollama | Ollama | A runtime and tool for running compatible models locally. | 帮助用户在本地下载、加载和运行模型的工具。 |
| vLLM | vLLM | A model-serving runtime often used for efficient inference. | 常用于高效提供模型推理服务的运行时。 |
| model serving | 模型服务 | Operating a model so applications can send inference requests. | 把模型运行起来，让应用可以发送推理请求。 |
| local AI | 本地 AI | AI capabilities running on user-controlled devices or infrastructure. | AI 能力在用户自己控制的设备或服务器上运行。 |
| hardware | 硬件 | Physical computing equipment used to run a model. | 运行模型所需的实体设备。 |
| hardware limit | 硬件限制 | A limit caused by available memory, compute, or device capability. | 设备的内存、算力等不够造成的限制。 |
| memory | 内存 | Working storage needed while a model runs. | 模型运行过程中临时存放数据所需的空间。 |
| compute | 计算能力；算力 | The processing capacity available for model operations. | 设备执行模型运算的能力。 |
| enough memory | 足够的内存 | Having enough working storage for weights and runtime state. | 有足够空间装下权重并完成运行。 |
| enough compute | 足够的算力 | Having enough processing capacity for acceptable inference. | 有足够计算能力在可接受时间内完成推理。 |
| model file | 模型文件 | A stored artifact containing model weights or related data. | 保存模型权重等内容的文件。 |
| model file size | 模型文件大小 | The storage size of the model artifact. | 模型文件在磁盘上占用的空间大小。 |
| runtime memory | 运行时内存 | Total memory needed during inference. | 模型实际运行时总共需要的内存。 |
| memory budget | 内存预算 | The amount of memory available for all runtime needs. | 设备能分配给模型运行的内存总量。 |
| KV cache | KV 缓存 | Cached key and value states used during sequence inference. | 生成文字时保存上下文中间状态、避免重复计算的缓存。 |
| context | 上下文 | Input history or information available to the model. | 模型当前可以看到的输入、对话历史或背景信息。 |
| context length | 上下文长度 | How much input or history a model can process in one context. | 一次能处理的文字或历史信息有多长。 |
| temporary memory | 临时内存 | Working memory used for intermediate computations. | 模型计算过程中暂时使用的中间空间。 |
| runtime overhead | 运行时开销 | Extra memory or compute used by the runtime itself. | 运行软件本身额外占用的内存和算力。 |
| concurrency | 并发量；并发请求数 | The number of requests processed at the same time. | 同时处理多少个请求。 |
| format | 格式 | The representation in which model data is stored or loaded. | 模型文件和数据采用的存储表示方式。 |
| inference budget | 推理预算 | The total resource allowance for producing an inference result. | 为一次或一组推理准备的资源上限。 |
| quantization | 量化 | Reducing numerical precision to lower memory needs, with trade-offs. | 用更少的数字精度表示模型，以节省内存，但可能影响质量。 |
| original precision | 原始精度 | The numerical precision used before quantization. | 量化前模型使用的数字精度。 |
| higher precision | 更高精度 | A representation using more precise numerical values. | 用更多位数保存数值、通常更占资源的表示方式。 |
| smaller memory need | 更小的内存需求 | Requiring less memory to load or run a model. | 模型加载和运行时需要的内存更少。 |
| local option | 本地选项 | A model or setup that can reasonably run locally. | 可以在本地设备上实际使用的模型或方案。 |
| quality | 质量 | How good or useful the model’s outputs are. | 模型结果好不好、有没有用。 |
| speed | 速度 | How quickly a model produces results. | 模型生成结果的快慢。 |
| compatibility | 兼容性 | Whether a model works with a particular runtime or hardware. | 模型和运行软件、硬件能不能配合工作。 |
| quality-speed-compatibility trade-off | 质量-速度-兼容性权衡 | Improving one property may affect the others. | 质量、速度和兼容性之间常常需要取舍。 |
| capability difference | 能力差异 | A difference in what models can accomplish or how well they do it. | 不同模型能做的事和完成质量不同。 |
| cloud / closed-first | 云端 / 封闭优先 | A strategy that starts with hosted, restricted-access models. | 优先选择通过云端产品或 API 使用的封闭模型。 |
| hosted product | 托管产品 | A provider-operated product that exposes model capabilities. | 由服务商运行、用户直接使用的产品。 |
| API access | API 访问 | Using a model by sending programmatic requests to its API. | 通过程序向模型接口发送请求来使用模型。 |
| high-end model | 高端模型 | A powerful model that may require substantial infrastructure. | 能力较强、通常需要较多资源的模型。 |
| downloadable model | 可下载模型 | A model version that users can download and operate. | 用户可以下载并尝试自己运行的模型。 |
| model family | 模型家族 | A set of related models released by the same organization or design line. | 同一系列、结构或发布方相关的一组模型。 |
| model variant | 模型变体 | A particular version or configuration of a model family. | 某个模型家族中的具体版本或配置。 |
| representative example | 代表性示例 | An example used to illustrate a broader category. | 用来说明一类情况的示例，不代表永远如此。 |
| permanent label | 永久标签 | A classification assumed never to change. | 认为模型永远属于某一类的固定标签。 |
| current model card | 当前模型卡片 | The latest model documentation to inspect before deployment. | 部署前应查看的最新模型说明。 |
| deployment strategy | 部署策略 | A choice about how and where a model is operated. | 决定模型在哪里、由谁、用什么方式运行。 |
| hybrid ecosystem | 混合生态 | An ecosystem combining hosted and downloadable or open-weight offerings. | 同一个生态中同时有云端服务和可下载模型。 |
| cloud / closed-first strategy | 云端 / 封闭优先策略 | Choosing provider-hosted access before self-hosting. | 先用服务商托管的模型，而不是先自己部署。 |
| open-weight available strategy | 开放权重可用策略 | Choosing models whose weights or variants are published. | 选择发布了权重或可下载版本的模型。 |
| local control | 本地控制权 | Control over the device, runtime, data path, and operations. | 自己决定设备、软件、数据路径和运行方式。 |
| infrastructure customization | 基础设施定制 | Adjusting the hardware and serving environment to one’s needs. | 按自己的需要修改硬件和模型服务环境。 |
| easiest setup | 最简单的设置 | The option requiring the least installation and operations work. | 安装、配置和维护工作最少的方案。 |
| limited hardware | 硬件有限 | Having restricted memory or compute capacity. | 设备内存或算力比较有限。 |
| smaller model | 更小的模型 | A model with lower resource requirements, often at some capability trade-off. | 占用资源较少、能力可能有所取舍的模型。 |
| quantized model | 量化模型 | A model represented with reduced numerical precision. | 用较低数字精度表示、通常更省内存的模型。 |
| pricing | 定价 | How a model or service charges users. | 模型或服务如何向用户收费。 |
| free | 免费 | Having no direct usage price in a particular context. | 在某个使用情境下不收直接费用。 |
| local hardware cost | 本地硬件成本 | The purchase, electricity, maintenance, and replacement cost of local equipment. | 自己购买、用电、维护和更换硬件的成本。 |
| remote infrastructure | 远程基础设施 | Computing resources located away from the user and accessed through a network. | 用户通过网络使用、但设备不在身边的计算资源。 |
| provider or remote infrastructure | 提供商或远程基础设施 | Infrastructure operated by a provider or another remote party. | 由服务商或其他远程方运行的服务器和硬件。 |
| network or service access | 网络或服务访问 | Connectivity or service availability needed for remote inference. | 远程推理需要网络连接或服务可用。 |
| user request | 用户请求 | An input request sent by a user or application to a model. | 用户或应用交给模型处理的一次请求。 |
| request path | 请求路径 | The route a request follows from application to model and back. | 请求从应用到模型、再返回结果所经过的路径。 |
| application | 应用 | Software that sends inputs to or uses outputs from a model. | 调用模型能力来完成任务的软件。 |
| model output | 模型输出 | The result returned by a model. | 模型处理输入后返回的结果。 |
| inference request | 推理请求 | A request asking a model to generate or predict something. | 要求模型生成或预测结果的一次请求。 |
| model runtime | 模型运行时 | Software environment that executes model inference. | 执行模型推理的软件环境。 |
| deployment requirements | 部署要求 | Conditions needed for a model to operate successfully. | 模型能够正常运行必须满足的条件。 |
| model strategy | 模型策略 | A deliberate choice among cloud, local, open-weight, and closed options. | 根据目标和限制选择云端、本地、开放或封闭模型的方式。 |
| access axis | 访问轴 | The dimension from closed/hosted access to open-weight access. | 从封闭托管到开放权重的模型获取维度。 |
| location axis | 位置轴 | The dimension from cloud execution to local/self-hosted execution. | 从云端运行到本地自托管运行的维度。 |
| two axes | 两个维度 | Access and location are separate dimensions of model strategy. | 模型能否获得和模型在哪里运行是两件不同的事。 |
| model access question | 模型访问问题 | Who can obtain weights and under what terms. | 谁能取得权重、需要遵守哪些条件。 |
| inference hardware question | 推理硬件问题 | Which hardware performs the model computation. | 哪些硬件真正执行模型计算。 |
| access vs location | 访问与位置 | Access concerns availability; location concerns where inference runs. | 访问讲能不能拿到，位置讲在哪里计算。 |
| stored artifact | 存储工件 | A file or object saved for later use. | 保存在磁盘上的文件或模型对象。 |
| full inference budget | 完整推理预算 | All resources needed while producing an output. | 生成结果时需要的全部内存和计算资源。 |
| learned weights vs serving software | 学到的权重与服务软件 | The model is learned values; the runtime is software that executes them. | 模型是学到的数字，运行时是负责执行这些数字的软件。 |
| weights plus cache and overhead | 权重加缓存和开销 | Runtime memory includes more than the stored weights. | 实际运行内存不只有模型文件，还包括缓存和额外开销。 |
| open model | 开放模型 | An informal label that may refer to open weights or broader openness. | “开放模型”可能只表示权重开放，也可能泛指更广的开放程度，需看条款。 |
| closed access | 封闭访问 | Access controlled through a product, API, or provider service. | 只能通过产品、接口或服务商提供的方式使用。 |
| cloud-hosted open-weight model | 云端托管的开放权重模型 | An open-weight model operated on cloud infrastructure. | 权重开放但实际推理放在云服务器上的模型。 |
| open-source model | 开源模型 | A model release with broader source and licensing openness. | 在权重之外，通常还开放更多源代码和使用权利的模型。 |
| local / self-hosted option | 本地 / 自托管选项 | A deployment option operated on infrastructure under the user’s control. | 在自己控制的设备或服务器上部署的方案。 |
| hosted / remote option | 托管 / 远程选项 | A deployment option operated by another provider. | 由其他服务商远程运行、用户通过网络使用的方案。 |
| provider-managed hardware | 提供商管理的硬件 | Hardware operated and maintained by a model provider. | 由模型服务商负责运行和维护的硬件。 |
| user-managed hardware | 用户管理的硬件 | Hardware operated and maintained by the user or organization. | 由用户或组织自己运行和维护的硬件。 |
| control boundary | 控制边界 | The point separating what the user controls from what a provider controls. | 用户和服务商各自负责、能控制的范围分界。 |
| governance boundary | 治理边界 | The point at which responsibility for data and operations shifts between parties. | 数据和运行责任在用户与服务商之间如何划分的边界。 |
| model release | 模型发布 | A public or restricted distribution of a model version. | 某个模型版本被正式提供给用户的发布行为。 |
| terms change over time | 条款会随时间变化 | Access, licenses, and deployment policies may be updated. | 模型的访问方式、许可证和部署政策不是永远不变的。 |
| checked date | 核查日期 | The date on which example status or terms were checked. | 例子或条款最近一次被检查的日期。 |
| Anthropic Claude | Anthropic Claude | A commonly hosted model family accessed through products and APIs. | Anthropic 的 Claude 模型家族，通常通过产品和 API 使用。 |
| OpenAI GPT | OpenAI GPT | A model family commonly accessed through hosted products and APIs. | OpenAI 的 GPT 模型家族，通常通过托管产品和 API 使用。 |
| Meta Llama | Meta Llama | A model family with downloadable or open-weight variants under stated terms. | Meta 的 Llama 模型家族，有按条款提供的可下载或开放权重版本。 |
| Google Gemma | Google Gemma | A Google model family with downloadable variants under stated terms. | Google 的 Gemma 模型家族，有按条款提供的可下载版本。 |
| Google Gemini | Google Gemini | A hosted Google model family used as a cloud offering in the example. | Google 的 Gemini 模型家族，在页面例子中作为云端服务出现。 |
| Mistral | Mistral | A provider with hosted services and open-weight or commercial models. | Mistral 提供托管服务，也有开放权重和商业模型。 |
| commercial model | 商业模型 | A model offered under commercial terms or as part of a paid service. | 按商业条款提供、可能需要付费使用的模型。 |
| model family strategy | 模型家族策略 | The access and deployment choices associated with a model family. | 一个模型家族采用云端、开放权重或混合发布的方式。 |
| actual terms | 实际条款 | The current license and usage restrictions that apply to a release. | 某个版本当前真正适用的许可证和使用限制。 |
| deployment requirement check | 部署要求检查 | Reviewing model card, license, format, runtime, and hardware before use. | 使用前检查说明、许可证、格式、运行时和硬件是否匹配。 |

## Potential Missing Concepts

- The page separates access from location, but does not explain a complete two-dimensional matrix of all combinations, such as closed-cloud, closed-self-hosted, open-weight-cloud, and open-weight-local.
- The page uses “open-weight” and “open-source” carefully, but does not explain common license families, acceptable-use restrictions, redistribution, commercial-use rights, derivative models, or how model licenses differ from software licenses.
- The page does not define model cards, system cards, data sheets, provenance, training-data disclosure, or how to audit the actual terms attached to a release.
- The page names provider dependency, cost, data, and governance considerations, but does not explain privacy, data retention, training-on-user-data policies, residency, compliance, auditability, or vendor lock-in in detail.
- The page says local inference runs on user-controlled hardware, but does not explain operating-system support, drivers, CPU/GPU/NPU differences, accelerator backends, device memory, unified memory, VRAM, storage bandwidth, or thermal limits.
- The page gives a runtime-memory formula but does not explain parameter count, precision formats, bytes per parameter, activation memory, batching, prompt processing, generation memory, or how context length changes KV-cache size.
- The page mentions quantization but does not distinguish post-training quantization, quantization-aware training, weight-only quantization, activation quantization, mixed precision, or common formats such as GGUF, GPTQ, AWQ, and bitsandbytes.
- The page mentions Ollama and vLLM but does not explain model loading, tokenizer compatibility, chat templates, batching, continuous batching, scheduling, tensor parallelism, model sharding, or OpenAI-compatible endpoints.
- The page does not cover serving metrics such as latency, throughput, time to first token, tokens per second, queue time, utilization, concurrency limits, or cost per request.
- The page says local can work without a remote API, but does not explain offline security, network isolation, local logging, secrets handling, update management, or supply-chain risks from downloaded model files.
- The page does not explain model provenance, checksums, signing, malware scanning, untrusted model formats, or safe model download practices.
- The page lists cloud and local trade-offs but does not explain total cost of ownership, electricity, hardware depreciation, capacity planning, autoscaling, redundancy, disaster recovery, or service-level agreements.
- The page does not explain hybrid routing, fallback between local and cloud models, workload placement, data classification, or policies for sending only selected requests to a provider.
- The page mentions examples from Anthropic, OpenAI, Meta, Google, and Mistral, but does not provide a current catalog of model versions, modality support, context windows, regional availability, or exact license conditions.
- The page does not explain that “open,” “open-weight,” “open-source,” “free,” “local,” and “self-hosted” are not interchangeable product labels and may be used inconsistently by vendors.
- The page does not cover fine-tuning, adapters, LoRA, prompt caching, distillation, model merging, or other ways to customize an open-weight model.
- The page does not explain whether a model’s tokenizer, vocabulary, architecture code, inference kernels, training code, evaluation data, or training data are also available.
- The page does not cover security, privacy, abuse prevention, content policy, model safety, bias, evaluation, or governance differences between hosted and locally operated models.
- The page does not distinguish storage size, download size, memory required to load, memory required to serve, and disk or network bandwidth required during deployment.
- The page does not explain how model format, runtime version, hardware backend, quantization level, context length, batch size, and concurrent users jointly determine practical local feasibility.

## Aliases / Synonyms

- open-weight / open weights / weights available / downloadable weights / 开放权重 / 权重可获得
- open-weight model / downloadable model / locally deployable model（不一定完全同义）/ 开放权重模型 / 可下载模型
- open-source / source-available / openly licensed / 开源 / 源码可获得 / 开放许可（不一定完全同义）
- closed model / proprietary model / restricted-weight model / 封闭模型 / 专有模型 / 权重受限模型
- hosted model / provider-hosted model / cloud-hosted model / 托管模型 / 提供商托管模型 / 云端托管模型
- cloud / cloud-hosted / remote / hosted / 云端 / 云托管 / 远程 / 托管
- local / on-device / local inference / 本地 / 设备端 / 本地推理
- self-hosted / self-managed / privately hosted / 自托管 / 自管理 / 私有托管
- model access / access policy / availability / 模型访问 / 访问政策 / 可获得性
- model weights / weights / learned weights / parameter weights / 模型权重 / 权重 / 学到的权重 / 参数权重
- license / model license / license terms / 许可证 / 模型许可证 / 许可条款
- terms of use / usage terms / acceptable-use terms / 使用条款 / 使用条件 / 可接受使用条款
- model card / model documentation / model release notes / 模型卡片 / 模型文档 / 模型发布说明
- runtime / inference runtime / model runtime / 运行时 / 推理运行时 / 模型运行时
- serving stack / model-serving stack / inference stack / 服务栈 / 模型服务栈 / 推理栈
- model serving / inference serving / prediction serving / 模型服务 / 推理服务 / 预测服务
- local AI / on-device AI / self-hosted AI / 本地 AI / 设备端 AI / 自托管 AI
- cloud API / hosted API / remote model API / 云端 API / 托管 API / 远程模型 API
- provider / model provider / cloud provider / 服务商 / 模型提供商 / 云服务商
- provider-managed infrastructure / hosted infrastructure / managed infrastructure / 提供商管理的基础设施 / 托管基础设施 / 托管式基础设施
- user-controlled hardware / user-managed hardware / owned hardware / 用户控制的硬件 / 用户管理的硬件 / 自有硬件
- model file size / artifact size / download size（用途不同）/ 模型文件大小 / 工件大小 / 下载大小
- runtime memory / inference memory / serving memory / 运行时内存 / 推理内存 / 服务内存
- memory need / memory requirement / RAM requirement / 内存需求 / 内存要求 / RAM 要求
- compute / compute capacity / processing capacity / 算力 / 计算能力 / 处理能力
- quantization / reduced-precision representation / 量化 / 低精度表示
- quantized model / reduced-precision model / 量化模型 / 低精度模型
- higher precision / original precision / full precision（不一定严格同义）/ 更高精度 / 原始精度 / 全精度
- KV cache / key-value cache / attention cache / KV 缓存 / 键值缓存 / 注意力缓存
- context / prompt context / conversation context / 上下文 / 提示上下文 / 对话上下文
- context length / context window / maximum context / 上下文长度 / 上下文窗口 / 最大上下文
- temporary memory / working memory / intermediate memory / 临时内存 / 工作内存 / 中间内存
- runtime overhead / framework overhead / serving overhead / 运行时开销 / 框架开销 / 服务开销
- concurrency / concurrent requests / parallel requests / 并发 / 并发请求 / 并行请求
- compatible runtime / supported runtime / compatible serving software / 兼容运行时 / 支持的运行时 / 兼容服务软件
- compatible hardware / supported hardware / hardware target / 兼容硬件 / 支持的硬件 / 硬件目标
- local-friendly / locally runnable / practical to run locally / 适合本地运行 / 可本地运行 / 本地运行可行
- offline use / disconnected use / no-remote-API use / 离线使用 / 断网使用 / 不调用远程 API 使用
- provider dependency / vendor dependency / vendor lock-in / 提供商依赖 / 厂商依赖 / 厂商锁定（相关但不完全同义）
- usage-based cost / pay-per-use / token-based pricing / 按使用量计费 / 按次付费 / 按 token 定价
- local hardware cost / ownership cost / infrastructure cost / 本地硬件成本 / 持有成本 / 基础设施成本
- cloud model / remote model / hosted model / 云端模型 / 远程模型 / 托管模型
- local model / on-premises model / self-hosted model / 本地模型 / 本地部署模型 / 自托管模型
- open model / openly available model / “开放模型” / 可开放获取模型（需检查具体含义）
- closed-first / cloud-first / hosted-first / 封闭优先 / 云端优先 / 托管优先
- hybrid ecosystem / mixed model ecosystem / cloud-local mix / 混合生态 / 混合模型生态 / 云本地混合
- high-end model / frontier model / large model（不一定完全同义）/ 高端模型 / 前沿模型 / 大模型
- smaller model / compact model / lightweight model / 小模型 / 紧凑模型 / 轻量模型
- current terms / actual terms / applicable license / 当前条款 / 实际条款 / 适用许可证
- deployment requirements / runtime requirements / system requirements / 部署要求 / 运行要求 / 系统要求
- Anthropic Claude / Claude / Claude API / Anthropic Claude / Claude / Claude API
- OpenAI GPT / GPT / GPT API / OpenAI GPT / GPT / GPT API
- Meta Llama / Llama / Llama weights / Meta Llama / Llama / Llama 权重
- Google Gemma / Gemma / Gemma weights / Google Gemma / Gemma / Gemma 权重
- Google Gemini / Gemini / Gemini API / Google Gemini / Gemini / Gemini API
- Mistral / Mistral models / Mistral API / Mistral / Mistral 模型 / Mistral API
- API access / programmatic access / service access / API 访问 / 程序化访问 / 服务访问
- deployment strategy / serving strategy / model operating strategy / 部署策略 / 服务策略 / 模型运行策略

## Do Not Confuse Candidates

- Closed model vs cloud model: Closed describes who can obtain the weights; cloud describes where inference runs. An open-weight model can still be hosted in the cloud.
- Open-weight vs open-source: Open-weight means weights are available under stated terms; open-source is broader and may involve source availability and licensing rights. Always inspect the actual license.
- Open-weight vs local: Open-weight means the weights can be obtained; local means the model can run practically on hardware under the user’s control.
- Open-weight vs free: A model can have downloadable weights and still have license restrictions, hardware costs, or commercial-use conditions.
- Local vs free: Local describes execution location, not price. Local use still has costs for hardware, electricity, maintenance, storage, and operations.
- Local vs self-hosted: Local emphasizes where inference happens; self-hosted emphasizes who operates the infrastructure. A local machine is commonly self-hosted, but the terms answer different questions.
- Local vs on-device: On-device usually means running on an end-user device; local can also include a workstation or local server.
- Cloud vs remote: Cloud usually refers to provider-operated cloud infrastructure; remote is broader and can include any infrastructure accessed over a network.
- Hosted vs cloud: Hosted means someone else operates the service; cloud is a type of infrastructure or deployment location. A hosted service is not always described with the same cloud label.
- Provider-managed vs user-managed infrastructure: The first places operations and hardware responsibility with the provider; the second places it with the user or organization.
- Model vs model weights: The model is the broader computational artifact; weights are the learned numerical values that make up a central part of it.
- Model vs runtime: The model contains learned behavior; the runtime loads and executes it.
- Model file size vs runtime memory: File size measures stored data; runtime memory also includes KV cache, context, temporary memory, and runtime overhead.
- Model weights vs runtime memory: Weights are one component of the memory budget, not the entire amount needed during inference.
- Model file size vs download size: A stored model artifact may be packaged, compressed, or split differently from the amount transferred during download.
- Runtime vs serving stack: A runtime may execute one model; a serving stack can include the runtime plus APIs, scheduling, batching, monitoring, and infrastructure.
- Model serving vs inference: Inference is one computation; serving is the operational system that makes inference available to applications.
- Inference vs training: Inference applies a learned model; training changes or learns model weights.
- Open-weight model vs open-source runtime: An open-weight model can be run with open-source, source-available, or proprietary software; model openness and runtime openness are separate.
- Open-source model vs open-source software: A model release can have a license different from the runtime, tokenizer, kernels, or application that runs it.
- Supported format vs supported runtime: A format describes how the model is represented; a runtime is the software that can load and execute that representation.
- Compatible hardware vs enough hardware: A device may be technically supported but still too slow or too small in memory for practical use.
- Local-capable vs local-friendly: Local-capable means it can run under some setup; local-friendly suggests it is reasonably practical on common local hardware.
- Enough memory vs enough compute: Memory determines whether the model can fit; compute determines how quickly and efficiently it can run.
- Memory vs storage: Storage keeps the model file; memory is working space needed while the model runs.
- VRAM vs system RAM: VRAM is memory on a GPU; system RAM is general-purpose memory. A model may need one, the other, or both.
- Context vs context length: Context is the information supplied to the model; context length is the amount that can fit in one context.
- Context length vs KV cache: Context length is a limit or size of input history; KV cache is runtime state used to avoid recomputing that history.
- KV cache vs model weights: KV cache changes with requests and context; weights are the learned model values that are normally fixed during inference.
- Temporary memory vs runtime overhead: Temporary memory holds intermediate computation data; runtime overhead is extra resource use from the execution software and serving system.
- Concurrency vs context length: Concurrency is how many requests run together; context length is how much information one request contains. Both can increase memory use.
- Quantization vs compression: Quantization changes numerical representation and often affects computation; generic compression may only reduce storage size.
- Quantization vs pruning: Quantization lowers numerical precision; pruning removes or sparsifies parts of a model.
- Original precision vs full precision: Original precision means the release’s pre-quantized representation; full precision may be used informally and is not always a precise format name.
- Quality vs speed: A faster local configuration may reduce output quality or capability; a higher-quality configuration may need more resources.
- Compatibility vs performance: A model can load successfully but perform poorly; compatibility only means the pieces work together.
- Cloud API vs cloud platform: An API is a programmatic interface; a cloud platform is the broader infrastructure and service environment.
- Consumer product vs API: A consumer product is a user-facing application; an API is an interface for software requests.
- API access vs model access: API access may let a user use a model without obtaining its weights; model access can mean permission to obtain or inspect the weights.
- Provider dependency vs usage-based cost: Dependency is an operational and strategic reliance; usage-based cost is a pricing mechanism.
- Data consideration vs governance consideration: Data considerations focus on handling information; governance includes policy, accountability, compliance, and control more broadly.
- Offline use vs privacy: Offline execution can reduce network transmission, but it does not automatically guarantee privacy or secure local handling.
- Self-hosted vs no cost: Self-hosting transfers responsibility to the operator and does not make hardware, electricity, support, or licenses free.
- High-end model vs large model: High-end refers to capability or positioning; large often refers to scale or resource requirements, and the two are not identical.
- Smaller model vs weaker model: Smaller often means fewer resources, but quality depends on architecture, training, and task.
- Model family vs model variant: A family is the related series; a variant is one particular release or configuration within it.
- Representative example vs permanent label: A page example illustrates a current strategy; provider offerings and licenses can change.
- Current model card vs remembered provider behavior: The current documentation is authoritative for the release being evaluated; older assumptions may be stale.
- Actual license vs marketing label: “Open,” “open-weight,” or “free” in a product description does not replace reading the legal license.
- Downloadable variant vs unrestricted use: The ability to download a model does not imply unrestricted modification, redistribution, or commercial use.
- Cloud-hosted open-weight model vs closed model: Hosting an open-weight model in the cloud does not make its weights closed.
- Local inference vs local model authorship: A locally run model may have been created by a remote provider; location does not identify the author.
- Provider vs runtime: The provider publishes or operates a model or service; the runtime is software used to execute the model.
- Ollama vs vLLM: Both can be part of a model-serving workflow, but their interfaces, deployment patterns, optimization goals, and supported configurations differ.
- Model serving vs model training: Serving handles inference requests for an existing model; training produces or updates weights.
- Runtime memory vs total cost: Memory is a resource requirement; total cost also includes hardware, electricity, engineering, support, and provider fees.
- Open vs accessible: A model may have some open components while still requiring approval, registration, or restricted terms.
- Local vs private: Local execution can improve control, but a private cloud or private server may also be private without being on the user’s device.
- Cloud vs public: Cloud infrastructure can be private, dedicated, or public; “cloud” does not automatically mean public data exposure.

## Notes

- Raw collection intentionally keeps broad coverage, repeated terms, overlapping concepts, and multiple phrasings; do not deduplicate at this stage.
- The primary evidence is the full body of `open-closed-local-models.html`: the title and lede, the two-axis mental model, closed/hosted flow, open-weight flow, open-source comparison, local-capable practical test, local/cloud table, runtime-memory formula, quantization flow, checked examples, choice guide, six “do not confuse” rows, related concepts, and Remember This statement.
- Direct process nodes retained from the page include APP, INTERNET, PROVIDER API, HOSTED MODEL, MODEL WEIGHTS, DOWNLOAD, RUNTIME, YOUR / HOSTED HARDWARE, ORIGINAL / HIGHER PRECISION, QUANTIZATION, SMALLER MEMORY NEED, and MORE LOCAL OPTIONS.
- Direct formula components retained separately include MODEL WEIGHTS, KV CACHE, CONTEXT, TEMPORARY MEMORY, RUNTIME OVERHEAD, and RUNTIME MEMORY.
- The page presents “closed/hosted” and “open-weight” on an access axis, and “cloud” and “local/self-hosted” on a location axis. These are intentionally retained as separate candidate dimensions.
- The page explicitly states that open-weight is not the same as open-source, and that open-weight does not automatically mean local-friendly.
- The page’s practical local test is retained as a candidate chain: open weights + supported format + compatible runtime + enough memory + enough compute → practical local model.
- Runtime examples are retained from the page: Ollama, vLLM, and other compatible serving stacks.
- The page’s examples are time-sensitive and were marked “Checked 2026-09-09”; Anthropic Claude and OpenAI GPT are described as commonly hosted, while Meta Llama, Google Gemma, and many Mistral models are described as having downloadable or open-weight variants under their own terms.
- Google Gemini is retained as a hybrid-ecosystem example alongside downloadable Gemma; Mistral is retained as an example of hosted services alongside open-weight and commercial models.
- “Provider dependency,” “usage-based cost,” “limited infrastructure control,” “data,” and “governance” are retained even where the page presents them as trade-offs rather than formal mechanisms.
- “Local hardware still has costs” is retained to preserve the page’s distinction between execution location and pricing.
- Terms such as latency, throughput, VRAM, RAM, model licenses, security, privacy, and operational controls are included as potential review candidates where they are implied by the page’s hardware, governance, runtime, and deployment discussion, but they are not fully explained in the source page.
- Source links shown on the page include Meta Llama, Google Gemma, Mistral models, and Anthropic Claude documentation; the current model card, license, and deployment requirements should be checked before treating any provider example as permanent.
- This file is a raw candidate inventory for later glossary review. It intentionally does not decide which terms deserve final publication entries.
