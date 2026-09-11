# Topic

What Is an API?

## Module/Topic/Source File

- Module: 10 · Model Serving & Local AI
- Topic: API
- Source File: `api.html`
- Page Title: `What Is an API? · Model Serving & Local AI`

## Glossary Candidates

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| API | 应用程序编程接口；接口 | A defined interface that lets software systems communicate. | 让一个软件按约定向另一个软件请求数据或动作的入口。 |
| Application Programming Interface | 应用程序编程接口 | The expanded form of API. | API 这个缩写的完整英文名称。 |
| interface | 接口 | A boundary through which one system communicates with another. | 两个系统交换信息或请求的连接面。 |
| software system | 软件系统 | Software that can receive requests, process them, or return results. | 能接收请求、处理事情并返回结果的软件。 |
| one software system | 一个软件系统 | The system making or receiving a software request. | 发出请求或接收请求的其中一个软件系统。 |
| another software system | 另一个软件系统 | The separate system contacted by an application. | 被应用联系的另一个独立软件系统。 |
| communicate | 通信；沟通 | Exchange information or requests between systems. | 软件之间互相传递信息。 |
| request | 请求 | A message asking another system for data or an action. | 一个软件向另一个软件提出的要求。 |
| data | 数据 | Information that a system can send, receive, or process. | 软件之间传递的信息。 |
| action | 动作；操作 | Something one system asks another system to perform. | 请求另一个系统帮忙执行的事情。 |
| AI system | AI 系统 | A software system that uses artificial intelligence. | 使用人工智能能力的软件系统。 |
| AI systems | AI 系统（复数） | Multiple systems that use or provide AI capabilities. | 多个使用或提供 AI 能力的系统。 |
| AI service | AI 服务 | A service that exposes AI capability to applications. | 把 AI 能力提供给其他应用使用的服务。 |
| AI service is isolated | AI 服务处于孤立状态 | An AI service cannot easily be used by other applications without an interface. | 没有接口时，AI 服务很难被其他程序调用。 |
| application | 应用程序；应用 | Software that uses an API to request data or actions. | 使用接口来完成工作的软件。 |
| applications | 应用程序（复数） | Multiple software programs that use an interface. | 多个通过接口使用服务的软件。 |
| application uses an API | 应用使用 API | An application sends requests through an API. | 应用通过 API 把需求交给服务。 |
| model request | 模型请求 | A request sent to an AI model, often through an API. | 让模型处理某个输入的请求。 |
| model requests | 模型请求（复数） | Requests sent by applications to a model. | 应用发给模型的多个请求。 |
| response | 响应；回复 | Information returned after a request is processed. | 服务处理请求后返回的结果。 |
| responses | 响应（复数） | Results returned for requests. | 对多个请求返回的结果。 |
| API request | API 请求 | A request sent through an API to another system. | 按接口规则发给另一个系统的请求。 |
| API response | API 响应 | A result returned through an API. | 通过 API 返回给应用的结果。 |
| API is the interface | API 是接口 | The API is the communication boundary, not the model itself. | API 是连接两边的入口，不是里面真正推理的模型。 |
| interface concept | 接口概念 | The general idea of communicating through a defined boundary. | “通过约定好的入口互相通信”这个概念。 |
| communication interface | 通信接口 | An interface used for exchanging messages between systems. | 专门让系统交换请求和结果的接口。 |
| general software interface | 通用软件接口 | An interface for general software communication, not limited to AI. | 不只服务 AI、可用于各种软件通信的接口。 |
| specific software interface | 特定软件接口 | A particular interface exposed by a software system. | 某个具体软件系统提供的接口。 |
| interface for applications | 面向应用的接口 | An interface applications use to reach a service. | 应用程序用来访问服务的入口。 |
| model | 模型 | The AI component that performs inference behind the interface. | 真正根据输入计算并产生 AI 结果的部分。 |
| MODEL | 模型（页面大写标签） | The model component shown behind the AI service. | 图示中位于 AI 服务后面的模型。 |
| model is behind the interface | 模型位于接口之后 | The model is accessed through the API rather than being the API. | 应用先经过 API，API 后面才是模型。 |
| AI system component | AI 系统组件 | A part of an AI system that performs a particular role. | AI 系统中负责某项工作的组成部分。 |
| perform inference | 执行推理 | Use a model to compute an output for an input. | 用模型处理输入并算出结果。 |
| inference | 推理；推断 | Applying a model to an input to produce a result. | 模型根据输入计算答案的过程。 |
| serving | 服务提供；模型服务 | The layer that makes a model available for requests. | 把模型运行起来并接收外部请求的层。 |
| runtime | 运行时 | The software environment that executes a service or model. | 真正负责运行程序和模型的环境。 |
| App | 应用 | A short label for the application in the serving path. | 调用服务的应用程序。 |
| API (serving path) | API（服务链路中的接口） | The interface between an app and the serving layer. | 应用把请求交给服务层时经过的接口。 |
| Serving (serving path) | Serving（服务链路） | The layer that exposes a running model to callers. | 把正在运行的模型提供给调用者的部分。 |
| Runtime (serving path) | Runtime（运行时层） | The execution layer that runs the serving software. | 负责执行服务软件的运行环境。 |
| Model (serving path) | Model（服务链路中的模型） | The final AI component used to produce an output. | 链路最里面实际生成结果的 AI 模型。 |
| App → API → Serving → Runtime → Model | 应用→API→服务→运行时→模型 | A conceptual path from caller to the model. | 请求从应用一路经过接口和运行环境，最后到模型。 |
| application-to-model path | 应用到模型的路径 | The chain connecting an application to a model. | 应用访问模型时经过的整条链路。 |
| prompt | 提示词；提示 | Text or input instructions sent to a model. | 告诉模型要做什么的文字输入。 |
| `{ prompt: "Explain RAG" }` | 提示词请求示例 | An example request object containing a prompt. | 一个用字段写出提示词的请求示例。 |
| Explain RAG | 解释 RAG | The example instruction asking a model to explain RAG. | 示例中要求模型解释 RAG 的指令。 |
| messages | 消息；消息列表 | One or more conversational inputs sent to a model. | 发送给模型的一条或多条对话内容。 |
| settings | 设置；参数设置 | Options that control how a model request is handled. | 控制模型怎样处理请求的选项。 |
| tool definitions | 工具定义 | Descriptions of tools a model may be allowed to request. | 告诉模型有哪些工具、工具需要什么参数的说明。 |
| request field | 请求字段 | A named value included in a request. | 请求对象里表示某项信息的名称和值。 |
| request object | 请求对象 | A structured representation of an API request. | 按字段组织起来的一份请求数据。 |
| request payload | 请求载荷 | The data carried by a request. | 请求实际携带的内容。 |
| text | 文本 | Written content returned by a service. | 服务返回的一段文字。 |
| structured data | 结构化数据 | Data organized into predictable fields or a defined structure. | 按固定格式和字段组织的数据。 |
| tool request | 工具请求 | A request for a tool or function to perform an action. | 模型或服务要求调用某个工具的请求。 |
| error | 错误；错误信息 | A returned indication that processing failed or was invalid. | 请求失败或不符合要求时返回的提示。 |
| usage metadata | 使用情况元数据 | Information describing resource or request usage. | 记录这次调用用了多少资源等信息。 |
| response field | 响应字段 | A named value included in a response. | 返回结果里表示某项信息的名称和值。 |
| response object | 响应对象 | A structured representation of an API response. | 按字段组织起来的一份返回数据。 |
| answer | 答案；回答 | The result produced for a question or prompt. | 模型针对输入生成的回答。 |
| `{ answer: "..." }` | 回答响应示例 | An example response object containing an answer. | 一个用字段装载回答的响应示例。 |
| result returned | 返回结果 | The information sent back after processing. | 处理完成后交回调用方的内容。 |
| request and response | 请求与响应 | The two-way exchange between a caller and a service. | 一边提出要求、一边返回结果的完整交互。 |
| request-response exchange | 请求—响应交换 | A request followed by a corresponding response. | 发出一次请求并收到对应回复的过程。 |
| send a request | 发送请求 | Transfer a request from an application to a service. | 应用把请求发出去。 |
| receive a response | 接收响应 | Get the result returned by a service. | 应用收到服务返回的结果。 |
| return a response | 返回响应 | Send a processed result back to the caller. | 服务把处理结果交回调用方。 |
| call a service | 调用服务 | Ask a service to perform work through its interface. | 通过接口请服务帮忙做事。 |
| caller | 调用方 | The application or system that sends a request. | 发出 API 请求的一方。 |
| called service | 被调用服务 | The service that receives and handles a request. | 接收请求并处理它的服务。 |
| request processing | 请求处理 | Handling the incoming request and producing a result. | 服务接收请求、计算并准备回复。 |
| vendor schema | 厂商数据模式 | A particular provider's format for requests and responses. | 某一家供应商规定的请求和返回格式。 |
| specific vendor schema | 特定厂商模式 | One provider-specific API data format. | 某个厂商专用的字段和数据结构。 |
| conceptual category | 概念类别 | A broad category used to explain possible request or response content. | 为便于理解而归纳出的信息类别。 |
| local API | 本地 API | An API exposed by a service running on the local machine or network. | 在自己的电脑或本地网络上运行的接口。 |
| LOCAL API | 本地 API（页面大写标签） | An API for a locally hosted service. | 页面中表示本地服务接口的标签。 |
| cloud API | 云端 API | An API exposed by a remote provider over a network. | 由远程云服务商提供、通过网络访问的接口。 |
| CLOUD API | 云端 API（页面大写标签） | An API for a remote provider. | 页面中表示远程服务商接口的标签。 |
| local API vs cloud API | 本地 API 与云端 API | A comparison based on where the service runs. | 两者接口作用相同，主要区别是服务在哪里运行。 |
| locally hosted service | 本地托管服务 | A service hosted and running locally. | 服务程序运行在本地设备或本地环境中。 |
| localhost service | localhost 服务 | A service reached through the local host address. | 通过本机地址访问的本地服务。 |
| localhost | 本地主机 | The current computer used to host or access a local service. | 代表“这台电脑自己”的网络地址概念。 |
| remote provider | 远程提供商 | An external provider that hosts and exposes a service. | 在别处运行服务并通过网络提供能力的公司或平台。 |
| service location | 服务位置 | Where the service that receives requests is running. | 服务是在本地还是远程运行。 |
| local service | 本地服务 | A service running close to the calling application. | 和调用应用在同一台电脑或本地环境里的服务。 |
| remote service | 远程服务 | A service running outside the caller's local environment. | 在另一台机器或云端运行的服务。 |
| same interface concept | 相同的接口概念 | Local and cloud APIs can use the same communication idea. | 不论本地还是云端，接口都是连接应用和服务的入口。 |
| location differs | 位置不同 | The execution or hosting location is different. | 本地 API 和云 API 的主要差别在运行地点。 |
| tool calling | 工具调用 | An AI pattern in which a model requests a tool or function. | 模型判断需要外部能力后，要求调用工具或函数。 |
| Tool Calling | 工具调用（页面标题形式） | A model-driven request to invoke a tool or function. | 页面中与 API 对比的模型调用工具模式。 |
| AI pattern | AI 模式 | A recurring way to structure AI behavior or interaction. | AI 系统中反复使用的一种工作方式。 |
| model requests a tool | 模型请求工具 | The model asks for a tool to be invoked. | 模型不直接完成，而是要求某个工具来执行。 |
| tool | 工具 | A callable capability that can perform an operation. | AI 可以请求使用的外部能力。 |
| function | 函数 | A callable operation exposed to a model or program. | 可以按名称和参数执行的一段功能。 |
| tool or function | 工具或函数 | A callable operation requested by a model. | 模型可以要求调用的工具能力或程序函数。 |
| tool uses an API | 工具使用 API | A tool may communicate with another service through an API. | 工具内部也可能通过 API 访问别的服务。 |
| API used by a tool | 工具所使用的 API | An API that supports a tool's implementation. | 支撑某个工具工作的接口。 |
| API vs tool calling | API 与工具调用 | API is a general interface; tool calling is an AI behavior pattern. | API 是更大的接口概念，工具调用是模型请求工具的具体模式。 |
| MCP | 模型上下文协议 | A standardized protocol for connecting AI applications to tools and resources. | 让 AI 应用按统一规则连接工具和资源的协议。 |
| Model Context Protocol | 模型上下文协议 | The expanded form of MCP. | MCP 这个缩写的完整英文名称。 |
| standardized protocol | 标准化协议 | A shared set of rules for connecting systems. | 不同系统都可以遵循的一套统一通信规则。 |
| connecting AI applications | 连接 AI 应用 | Linking AI applications with external capabilities or information. | 把 AI 应用和外部工具、资源接起来。 |
| AI application | AI 应用 | An application that uses or provides AI capabilities. | 使用 AI 能力完成任务的应用程序。 |
| tools and resources | 工具与资源 | Callable capabilities and accessible information sources. | 可以执行操作的工具和可以读取的信息。 |
| resource | 资源 | Information or capability made available to an AI application. | AI 应用可以访问或利用的信息、服务或能力。 |
| MCP may sit above APIs | MCP 可以位于 API 之上 | MCP can provide a higher-level connection pattern that uses APIs underneath. | MCP 可能在更上层，底层仍然可以调用 API。 |
| MCP alongside APIs | MCP 与 API 并行存在 | MCP and APIs can operate together without being the same thing. | MCP 和 API 可以同时出现、各自承担不同角色。 |
| not interchangeable concepts | 不是可互换概念 | Two concepts can relate to each other without meaning the same thing. | 两者有关联，但不能把 API 直接当成 MCP。 |
| API vs MCP | API 与 MCP | API is a specific software interface; MCP is a standardized connection protocol. | API 是具体接口，MCP 是连接 AI、工具和资源的标准协议。 |
| restaurant ordering counter | 餐厅点餐柜台 | A simplified analogy for an API interface. | 把 API 想成顾客和后厨之间负责传递订单的窗口。 |
| restaurant analogy | 餐厅类比 | A teaching analogy that maps software calls to ordering food. | 用点餐来帮助理解请求、处理和响应。 |
| customer | 顾客 | The party making an order in the analogy. | 类比中代表发起请求的应用。 |
| Customer → Application | 顾客→应用 | The analogy's mapping from customer to application. | 顾客对应发出请求的应用程序。 |
| order | 订单；点单 | The customer's request in the restaurant analogy. | 顾客提出的要求，对应 API 请求。 |
| Order → API request | 订单→API 请求 | The analogy mapping an order to an API request. | 点餐单就像应用发给服务的请求。 |
| kitchen | 厨房 | The service-processing side in the analogy. | 类比中代表接收并处理请求的 AI 服务。 |
| Kitchen → AI service | 厨房→AI 服务 | The analogy's mapping from kitchen to AI service. | 厨房对应实际处理请求的 AI 服务。 |
| meal | 餐食；饭菜 | The completed result in the restaurant analogy. | 厨房做好的饭菜，对应 API 响应。 |
| Meal → API response | 餐食→API 响应 | The analogy mapping a meal to an API response. | 送出的饭菜就像服务返回的结果。 |
| analogy simplified | 类比已简化 | A reminder that the restaurant mapping is only approximate. | 餐厅例子只是帮助入门，不等于真实技术细节。 |
| Web App | Web 应用；网页应用 | An application running through the web that can call an AI service. | 在浏览器或网站中运行的应用。 |
| web application | Web 应用 | An application delivered through web technologies. | 用户通过网页使用的软件。 |
| Mobile App | 移动应用 | An application running on a phone or tablet. | 手机或平板上的应用程序。 |
| mobile application | 移动应用 | An application designed for mobile devices. | 面向手机等移动设备的软件。 |
| Excel workflow | Excel 工作流 | A spreadsheet-based process that can call an AI service. | 在 Excel 里按步骤使用 AI 服务的工作流程。 |
| workflow | 工作流；工作流程 | A sequence of steps used to complete work. | 为完成一件事而串起来的一系列步骤。 |
| Agent | 智能体；代理 | A software system that can decide and act, possibly by calling an AI service. | 能根据目标做决定并执行动作的软件。 |
| agent | 智能体；代理（小写形式） | An AI-enabled program that can perform steps or use tools. | 能完成多步任务、可能调用工具的程序。 |
| Backend | 后端 | The server-side software that can call an AI service. | 网站或应用背后负责处理数据和请求的部分。 |
| backend | 后端（小写形式） | The server-side part of an application. | 用户看不到、负责业务处理的服务端程序。 |
| call the AI service | 调用 AI 服务 | Send a request to an AI service through an interface. | 通过 API 请 AI 服务处理输入。 |
| isolated AI service | 孤立的 AI 服务 | An AI service not connected to consuming applications. | 没有连接应用、外部程序无法方便使用的 AI 服务。 |
| service consumer | 服务使用方 | An application or system that consumes a service. | 使用 AI 服务能力的应用或系统。 |
| service provider | 服务提供方 | The system or organization exposing a service. | 提供 AI 能力或其他软件能力的一方。 |
| provider | 提供商 | An organization or system that offers a remote service. | 把服务放在远端并提供给别人使用的一方。 |
| software communication | 软件通信 | The exchange of requests and results between software. | 软件之间传递消息、请求和结果。 |
| data exchange | 数据交换 | Sending information between systems. | 两个系统互相传递数据。 |
| action request | 动作请求 | A request asking a system to perform an operation. | 要求系统执行某个动作的请求。 |
| model input | 模型输入 | Information sent to a model for inference. | 交给模型处理的提示、消息或其他数据。 |
| model output | 模型输出 | Information produced by a model. | 模型处理输入后产生的答案或数据。 |
| API schema | API 模式；接口数据结构 | The defined structure and fields of API data. | 规定请求和响应有哪些字段、怎样组织的格式。 |
| schema | 模式；数据结构 | A description of how structured data is organized. | 数据字段和排列方式的说明。 |
| metadata | 元数据 | Data that describes a request, response, or usage. | 描述数据本身或调用情况的信息。 |
| usage | 使用量；用量 | The amount of service or resources consumed. | 一次或多次调用消耗了多少服务资源。 |
| error response | 错误响应 | A response indicating that a request failed or was invalid. | 请求出错时返回的响应。 |
| structured response | 结构化响应 | A response organized into defined fields. | 按约定字段返回、程序容易读取的结果。 |
| natural-language response | 自然语言响应 | A response returned as ordinary human-readable text. | 以人能直接读懂的文字返回的结果。 |
| API endpoint | API 端点；接口地址 | A network-accessible location for a particular API operation. | 程序实际发送请求的接口地址。 |
| API call | API 调用 | One operation in which a caller sends a request to an API. | 程序通过接口请求一次服务的动作。 |
| API caller | API 调用方 | The program that makes an API call. | 发起 API 调用的程序。 |
| API provider | API 提供方 | The service that exposes an API. | 对外提供接口的服务或厂商。 |
| API contract | API 契约；接口约定 | The rules for what requests and responses must look like. | 调用双方共同遵守的字段、格式和行为约定。 |
| request format | 请求格式 | The required structure of an API request. | 请求必须按照什么样的格式发送。 |
| response format | 响应格式 | The structure used for data returned by an API. | API 返回结果时采用的格式。 |
| application layer | 应用层 | The layer where the consuming application operates. | 最靠近用户、负责发起业务请求的那一层。 |
| service layer | 服务层 | The layer exposing a capability to applications. | 对外接收请求并提供能力的那一层。 |
| model layer | 模型层 | The layer containing the inference model. | 真正运行模型、产生 AI 结果的那一层。 |
| local deployment | 本地部署 | Running the service on local infrastructure. | 把服务安装并运行在自己的设备或环境中。 |
| cloud deployment | 云端部署 | Running the service on a remote provider's infrastructure. | 把服务运行在云端服务器上。 |
| API location | API 所在位置 | The local or remote location of the API service. | 接口背后的服务是在本地还是远程。 |

## Potential Missing Concepts

- authentication / API authentication — 身份验证；页面讨论了 API 通信，但没有展开调用者如何证明身份。
- authorization — 授权；页面未展开谁可以调用哪些操作。
- API key — API 密钥；常见的调用凭证，正文未出现。
- access token — 访问令牌；常见的短期访问凭证，正文未出现。
- HTTP — 超文本传输协议；常见的 API 传输协议，正文未出现。
- HTTPS — 加密的 HTTP；常见的安全传输方式，正文未出现。
- endpoint — 端点；页面讲接口但没有单独给出具体地址概念。
- method / HTTP method — 方法；如 GET、POST 等请求动作，正文未出现。
- status code — 状态码；响应成功或失败的数值标记，正文未出现。
- JSON — JSON 数据格式；页面用对象示例展示字段，但未点名 JSON。
- rate limit — 速率限制；服务对调用频率的约束，正文未出现。
- timeout — 超时；等待响应超过限制的情况，正文未出现。
- retry — 重试；失败后再次发送请求的机制，正文未出现。
- latency — 延迟；请求到响应所花的时间，正文未出现。
- throughput — 吞吐量；单位时间可处理的请求量，正文未出现。
- streaming response — 流式响应；逐步返回生成内容的方式，正文未出现。
- webhook — Webhook；由服务主动通知另一个系统的方式，正文未出现。
- SDK — 软件开发工具包；封装 API 调用的开发工具，正文未出现。
- client — 客户端；发起 API 调用的软件，正文只用 application / caller 表达。
- server — 服务器；接收 API 请求的服务端，正文只用 service / provider 表达。
- REST — REST 风格接口；常见 API 设计风格，正文未出现。
- RPC — 远程过程调用；另一种接口调用抽象，正文未出现。

## Aliases / Synonyms

| Candidate | Alias / Related Wording | Note |
|---|---|---|
| API | Application Programming Interface | API 的全称；正文只直接使用 API。 |
| API | interface | API 是接口的一种具体形式；不能把所有 interface 都等同于 API。 |
| AI service | model service | 页面用 AI service 表达对外服务；model service 是相关但更窄的说法。 |
| response | reply | response 是技术语境中的“响应”；reply 是更口语的“回复”。 |
| request | call | call 常指一次调用，request 更强调发送的数据或要求。 |
| model request | inference request | 发送给模型以执行推理的请求；正文使用 model request。 |
| API request | request payload | API request 是完整请求，payload 是其中携带的数据部分。 |
| API response | response payload | API response 是完整响应，payload 是响应携带的数据部分。 |
| local API | localhost API | 若本地服务通过 localhost 暴露接口，两者可相关但不完全同义。 |
| cloud API | remote API | 云 API 通常是远程 API，但 remote API 也可能不在云端。 |
| remote provider | service provider | remote provider 强调远程位置，service provider 强调提供服务的角色。 |
| application | app | App 是 application 的常用短写；正文链路中使用 App。 |
| Web App | web application | Web App 的展开表达。 |
| Mobile App | mobile application | Mobile App 的展开表达。 |
| Agent | agent | 同一概念的大写/小写写法，保留页面中的两种形式。 |
| Backend | backend | 同一概念的大写/小写写法，保留页面中的两种形式。 |
| tool calling | function calling | AI 请求执行工具或函数的相关表达；正文使用 tool calling。 |
| tool request | function request | 工具请求与函数请求可能指相近动作，但具体协议取决于实现。 |
| MCP | Model Context Protocol | MCP 的全称。 |
| resource | external resource | AI 应用可访问的外部信息或能力；正文直接使用 resource。 |
| serving | model serving | serving 在本页调用链中指提供模型能力的层；model serving 是更完整说法。 |
| runtime | execution environment | 运行时是执行服务或模型的环境；两者相关但范围可能不同。 |
| structured data | structured output | 结构化数据是数据类型，structured output 强调作为输出返回。 |
| usage metadata | usage information | 描述调用用量的元数据信息。 |

## Do Not Confuse Candidates

| Candidate A | Candidate B | Distinction |
|---|---|---|
| API | model | API 是通信接口；model 是执行推理的 AI 组件。 |
| API | AI service | API 是进入服务的接口；AI service 是接口后面提供能力的服务。 |
| API | serving | API 是调用边界；serving 是把模型能力提供出来的服务层。 |
| API | runtime | API 接收请求；runtime 负责执行服务或模型。 |
| API | tool calling | API 是通用软件接口；tool calling 是模型请求工具或函数的 AI 模式。 |
| API | MCP | API 是具体软件接口；MCP 是连接 AI 应用、工具和资源的标准化协议。 |
| API request | prompt | API request 是完整请求；prompt 只是请求中可能包含的一项模型输入。 |
| API response | answer | API response 可能包含答案、文本、结构化数据、错误和元数据；answer 只是其中一种结果。 |
| request | response | request 从调用方发出；response 由被调用服务返回。 |
| request field | response field | 请求字段属于发出的数据；响应字段属于返回的数据。 |
| text | structured data | text 是普通文本；structured data 按字段或结构组织。 |
| tool | function | tool 是较广的可调用能力；function 通常指具体的程序函数。 |
| tool request | API request | tool request 是请求调用工具；API request 是更一般的接口请求，工具本身也可能发 API request。 |
| local API | cloud API | 关键区别是服务位置；两者都是 API。 |
| localhost service | remote provider | localhost service 在本机；remote provider 在外部远程环境。 |
| application | backend | application 是使用服务的整体应用；backend 是其中位于服务端的一部分。 |
| Web App | Mobile App | Web App 通常通过网页运行；Mobile App 面向手机或平板。 |
| Agent | application | Agent 是能进行决策或行动的特定应用形态；普通 application 不一定是 Agent。 |
| service provider | service consumer | provider 提供能力；consumer 使用能力。 |
| schema | data | schema 描述数据结构；data 是按结构传递的实际内容。 |
| metadata | response data | metadata 描述请求、响应或用量；不一定是主要业务结果。 |
| MCP | API endpoint | MCP 是协议；endpoint 是某个 API 操作可访问的具体地址。 |
| interface | endpoint | interface 是抽象的通信边界；endpoint 是接口中可访问的具体位置。 |
| API call | API request | call 强调一次调用行为；request 强调发送给接口的消息或要求。 |
| inference | training | inference 是使用已学模型处理新输入；training 是让模型从数据中学习。 |
| model output | API response | model output 是模型产生的结果；API response 是接口返回的完整响应，可能包含更多字段。 |

## Notes

- This is an intentionally broad, raw candidate inventory for later glossary curation.
- Candidates are collected from the visible headings, explanatory paragraphs, diagrams, code-like examples, labels, comparisons, analogy, and application list in `api.html`.
- Repeated concepts, capitalization variants, exact phrases, aliases, and boundary concepts are retained instead of being deduplicated.
- Request/response field names are conceptual categories from the page, not a claim about any specific vendor schema.
- The restaurant mapping is explicitly marked as simplified; it is an analogy, not an implementation specification.
- “Local” and “cloud” describe service location in this page; the interface concept remains the same.
- “API”, “tool calling”, and “MCP” are related but intentionally kept as separate candidates because the page explicitly contrasts them.
