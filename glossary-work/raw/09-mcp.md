# Topic

Model Context Protocol (MCP)

Module/Topic/Source File

- Module: 09 · Agents, Tools & MCP
- Topic: Topic 04 · What is MCP?
- Source File: `mcp.html`

## Glossary Candidates

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Model Context Protocol | 模型上下文协议 | A standard way for AI applications to connect to external capabilities and context. | 让 AI 应用用统一方式连接外部能力和上下文的一套协议。 |
| MCP | 模型上下文协议（MCP） | Short name for Model Context Protocol. | Model Context Protocol 的英文缩写。 |
| protocol | 协议 | A shared set of rules for communication between systems. | 不同系统之间按照同一套规则沟通的方法。 |
| standard protocol | 标准协议 | A protocol designed to provide a common interface across supported systems. | 让不同系统可以用共同接口连接的一套规范。 |
| standardized interface | 标准化接口 | A common way for software components to connect and interact. | 软件组件用统一方式连接和交互的接口。 |
| AI application | AI 应用 | An application that uses AI capabilities for a user or workflow. | 使用 AI 能力为用户或流程完成工作的应用。 |
| application | 应用 | A concrete software program used for a purpose. | 为某个目的而使用的软件程序。 |
| external capability | 外部能力 | A capability supplied outside the AI application itself. | 不是 AI 应用本身提供、而是来自外部系统的能力。 |
| capability | 能力 | Something a system can do or make available. | 一个系统能够执行或提供的事情。 |
| external context | 外部上下文 | Information supplied from outside the AI application. | 从 AI 应用外部提供、帮助完成任务的信息。 |
| context | 上下文 | Information that helps an application understand or complete a task. | 帮助应用理解任务和作出处理的信息背景。 |
| connect | 连接 | Establish a working relationship between an application and another system. | 让应用和另一个系统建立可工作的关系。 |
| connection | 连接 | The communication relationship between two systems. | 两个系统之间进行通信的关系。 |
| external system | 外部系统 | A system outside the AI application that provides data or actions. | AI 应用之外、提供数据或操作能力的系统。 |
| supported system | 受支持的系统 | A system that follows the required connection rules. | 遵守连接规则、可以被接入的系统。 |
| supported server | 受支持的服务器 | A server that an MCP host can communicate with through MCP. | AI 应用可以按照 MCP 规则连接的服务器。 |
| MCP connection | MCP 连接 | A connection between an MCP client and MCP server. | MCP 客户端和 MCP 服务器之间的协议连接。 |
| MCP host | MCP 主机 | The AI application that provides the experience and coordinates MCP connections. | 提供用户体验并协调 MCP 连接的 AI 应用。 |
| host | 主机 | The application that runs the AI experience and coordinates a connection. | 运行 AI 应用并负责协调连接的应用程序。 |
| host application | 主机应用 | An application that contains an MCP client and communicates with a server. | 内含 MCP 客户端、负责和服务器通信的应用。 |
| user experience | 用户体验 | The way a user interacts with and receives results from an application. | 用户操作应用并获得结果时的整体体验。 |
| coordinate | 协调 | Organize the parts of a connection so they work together. | 让连接中的各个部分配合工作的过程。 |
| MCP client | MCP 客户端 | A client inside the host that communicates with an MCP server. | 位于主机应用内部、负责和 MCP 服务器通信的客户端。 |
| client | 客户端 | The side of a connection that requests or consumes a service. | 连接中发起请求或使用服务的一方。 |
| server | 服务器 | The side that exposes capabilities for a client to use. | 向客户端提供数据或能力的一方。 |
| MCP server | MCP 服务器 | A server that exposes approved tools, resources, or prompts through MCP. | 按 MCP 提供获准工具、资源或提示的服务器。 |
| server connection | 服务器连接 | A communication link from a client to a server. | 客户端与服务器之间的通信链路。 |
| shared rules | 共享规则 | Rules that both communicating sides understand and follow. | 通信双方都理解并遵守的共同规则。 |
| discover | 发现 | Find out what capabilities or context are available. | 查明外部系统提供了哪些能力或上下文。 |
| capability discovery | 能力发现 | The process of learning what a server can provide. | 了解服务器能提供什么工具、资源或其他能力。 |
| context discovery | 上下文发现 | Finding context that an external server makes available. | 找到外部服务器可以提供的相关信息。 |
| exchange | 交换 | Send and receive capabilities, context, or results between systems. | 系统之间发送和接收能力、上下文或结果。 |
| capability exchange | 能力交换 | Sharing information about available capabilities and using them. | 互相传递可用能力信息并按规则使用。 |
| expose | 暴露；提供 | Make a capability available for an application to discover or use. | 把某项能力提供出来，让应用可以发现或使用。 |
| exposed capability | 已提供的能力 | A capability made available by a server. | 服务器已经对外提供的能力。 |
| approved capability | 获准能力 | A capability that is allowed to be made available. | 经过允许、可以被应用使用的能力。 |
| approved tool | 获准工具 | A tool that has been allowed for an application to use. | 已获得允许、可以被应用调用的工具。 |
| approved folder | 获准文件夹 | A folder whose contents an application is allowed to access. | 被允许让应用读取内容的文件夹。 |
| allowed capability | 允许的能力 | A capability that the server permits the application to use. | 服务器允许应用使用的功能。 |
| tool | 工具 | An external capability that can perform an action or operation. | 可以执行某项操作的外部能力。 |
| tools | 工具集合 | Multiple external capabilities available to an AI application. | 可供 AI 应用使用的多个外部功能。 |
| tool exposure | 工具暴露 | Making a tool available through a server interface. | 通过服务器接口把工具提供给应用使用。 |
| tool action | 工具操作 | The specific operation performed by a tool. | 某个工具实际执行的一项具体操作。 |
| tool request | 工具请求 | A request for a tool to perform a specific operation. | 请求工具执行某项具体操作的信息。 |
| resource | 资源 | External information that an application can access as context. | 应用可以访问并用作上下文的外部信息。 |
| resources | 资源集合 | Multiple external information sources exposed by a server. | 服务器提供的多个外部信息来源。 |
| file resource | 文件资源 | File content exposed as information an application can use. | 以资源形式提供给应用读取的文件内容。 |
| data resource | 数据资源 | External data made available to an application. | 提供给应用使用的外部数据。 |
| prompt | 提示；提示模板 | Guidance or a reusable prompt made available to an AI application. | 提供给 AI 应用使用的指导文字或可复用提示。 |
| available prompt | 可用提示 | A prompt that an MCP server makes available to the host. | MCP 服务器提供给主机使用的提示。 |
| external tool | 外部工具 | A tool supplied by a system outside the AI application. | 来自 AI 应用外部系统的工具。 |
| external data | 外部数据 | Data stored or supplied outside the AI application. | 存在于 AI 应用外部、供应用读取的数据。 |
| external capability and context | 外部能力和上下文 | Actions and information supplied by connected systems. | 连接的外部系统提供的操作能力和背景信息。 |
| system capability | 系统能力 | An operation a system can perform or provide. | 系统能够执行或向其他系统提供的功能。 |
| AI connection | AI 连接 | A connection that lets an AI application use an external system. | 让 AI 应用使用外部系统的连接方式。 |
| USB for AI connections | AI 连接的 USB | An analogy for a common standard that lets different systems connect. | 像 USB 一样，为不同 AI 系统提供共同连接标准的比喻。 |
| USB standard | USB 标准 | A common connection standard for devices. | 规定设备如何用共同方式连接的标准。 |
| device | 设备 | Hardware or software component that can connect through a standard. | 可以按照标准连接的硬件或软件组件。 |
| common way | 共同方式 | A method shared by different systems for connecting or communicating. | 不同系统都能采用的连接或通信方法。 |
| AI application host | AI 应用主机 | The application that starts and coordinates an MCP interaction. | 启动并协调 MCP 交互的 AI 应用。 |
| host-side client | 主机侧客户端 | The MCP client running inside the host application. | 运行在主机应用内部的 MCP 客户端。 |
| server-side capability | 服务器侧能力 | A capability provided by the connected MCP server. | 由连接的 MCP 服务器提供的能力。 |
| user request | 用户请求 | A request that tells the AI application what the user wants. | 用户告诉 AI 应用自己想完成什么的请求。 |
| request about documents | 关于文档的请求 | A request involving information in documents. | 需要处理文档内容的用户请求。 |
| document | 文档 | A written file or piece of information. | 保存文字或其他信息的文件。 |
| file | 文件 | A stored unit of information that can be read or used. | 电脑中保存的一份信息。 |
| folder | 文件夹 | A location that groups stored files. | 用来存放和组织多个文件的位置。 |
| file access | 文件访问 | Reading or using file content through an allowed connection. | 按允许的权限读取或使用文件内容。 |
| access | 访问 | The ability to reach or use data or a system. | 能够接触、读取或使用数据和系统的能力。 |
| access rule | 访问规则 | A rule controlling what a connection may reach or do. | 规定连接可以访问什么、不能访问什么的规则。 |
| own access rules | 自身访问规则 | Rules enforced by the server or external system itself. | 由服务器或外部系统自己执行的权限规则。 |
| file content | 文件内容 | The information contained in a file. | 文件中实际保存的文字或其他信息。 |
| relevant file content | 相关文件内容 | File information that helps answer the current request. | 与当前请求有关、可以帮助回答问题的文件信息。 |
| context available to the application | 应用可用上下文 | Information made available for the AI application to use. | AI 应用能够读取并用于处理任务的信息。 |
| business system | 业务系统 | A system used to run or support an organization’s work. | 企业日常业务中使用的软件系统。 |
| developer tool | 开发者工具 | A tool used to build, inspect, or operate software. | 用于开发、检查或运行软件的工具。 |
| database | 数据库 | An organized store of records that can be queried. | 按结构保存、可以查询记录的数据集合。 |
| database query | 数据库查询 | A request to retrieve or work with database information. | 向数据库请求查找或处理信息的操作。 |
| query | 查询 | A request for information from a system. | 向系统提出的查找信息请求。 |
| connect systems | 连接系统 | Make two or more systems communicate and work together. | 让两个或多个系统通信并协作。 |
| result | 结果 | Information returned after a request or operation. | 请求或操作完成后返回的信息。 |
| usable result | 可用结果 | A result that an AI application can use or present. | AI 应用可以继续使用或展示给人的结果。 |
| present for review | 提交审核 | Show a result so a person can inspect it before use. | 把结果展示出来，供人检查后再使用。 |
| review | 审核；复核 | Inspect a result before accepting or acting on it. | 在接受或执行结果前进行检查。 |
| result presentation | 结果呈现 | Showing an external result to the application user. | 把外部系统返回的结果展示给用户。 |
| input | 输入 | Information supplied to begin a task or operation. | 用来启动任务或操作的信息。 |
| output | 输出 | The result returned after a system processes a request. | 系统处理请求后返回的结果。 |
| input-output flow | 输入输出流程 | The movement from a request through processing to a result. | 从请求进入、经过处理到结果返回的流程。 |
| external request | 外部请求 | A request directed to an external system or capability. | 发给外部系统或外部能力的请求。 |
| system interaction | 系统交互 | Communication and actions between connected systems. | 已连接系统之间的通信和操作。 |
| communicate | 通信 | Exchange information between systems. | 系统之间互相传递信息。 |
| user-facing application | 面向用户的应用 | An application that directly provides an experience to a person. | 直接为用户提供操作界面的应用。 |
| application and server | 应用与服务器 | The two sides that use and provide MCP capabilities. | 使用能力的应用和提供能力的服务器两方。 |
| connection layer | 连接层 | The part of a system that manages communication between components. | 管理不同组件之间通信的那一层。 |
| capability layer | 能力层 | The set of tools, resources, and prompts exposed for use. | 对应用提供工具、资源和提示的能力集合。 |
| context layer | 上下文层 | Information supplied to help an AI application complete a task. | 帮助 AI 应用完成任务的信息层。 |
| integration | 集成 | Combining systems so they work together. | 把多个系统接起来，让它们协同工作。 |
| interoperability | 互操作性 | The ability of different systems to work together through shared rules. | 不同系统遵守共同规则后能够互相工作的能力。 |
| standardization | 标准化 | Defining common rules and interfaces for repeated use. | 制定共同规则和接口，让不同系统都能使用。 |
| interface | 接口 | A defined point and method through which a service is used. | 使用某项服务时遵循的连接方式和入口。 |
| service interface | 服务接口 | An interface provided by a service for other software to use. | 服务向其他软件提供的使用入口。 |
| API | 应用程序接口（API） | An interface provided by a service for software to call. | 服务给软件调用的接口，不等于 MCP 本身。 |
| model | 模型 | A computational system that produces or transforms results. | 能根据输入计算、生成或转换结果的系统。 |
| AI model | AI 模型 | A model used to perform an AI task. | 用来完成 AI 任务的模型。 |
| AI agent | AI 智能体 | An application system that can decide and take actions toward a goal. | 能围绕目标作决定并采取行动的应用系统。 |
| agent | 智能体 | A system that can select or perform actions for a goal. | 能为了目标选择或执行行动的系统。 |
| goal | 目标 | The result an agent or system is trying to achieve. | 智能体或系统想要达成的结果。 |
| decision | 决策 | A choice about what action or step to take. | 对下一步做什么作出的选择。 |
| decide | 决定 | Choose what to do based on a goal and information. | 根据目标和信息选择下一步。 |
| action | 行动；动作 | An operation taken by an application or agent. | 应用或智能体实际执行的操作。 |
| tool calling | 工具调用 | A model or application mechanism for requesting a specific tool action. | 模型或应用请求某个工具执行操作的机制。 |
| tool call | 工具调用请求 | A particular request asking a tool to perform an action. | 请求某个工具执行具体动作的一次调用。 |
| specific tool action | 特定工具操作 | One particular operation requested from a tool. | 从工具请求的一项明确操作。 |
| API call | API 调用 | A request sent to an API to use a service. | 向 API 发送请求来使用服务。 |
| protocol vs API | 协议与 API 的区别 | A protocol defines shared communication rules; an API is a service interface. | 协议规定共同沟通规则，API 是服务提供的调用接口。 |
| MCP vs tool calling | MCP 与工具调用的区别 | MCP standardizes discovery and exchange; tool calling requests a specific action. | MCP 规范发现和交换，工具调用请求具体动作。 |
| MCP vs AI agent | MCP 与 AI 智能体的区别 | MCP connects applications to capabilities; an agent decides and acts toward a goal. | MCP 是连接标准，智能体是会围绕目标决策和行动的系统。 |
| MCP is not a tool | MCP 不是工具 | MCP defines how tools can be exposed and used; it is not an individual tool. | MCP 规定工具如何提供和使用，不是某一个具体工具。 |
| MCP is not a model | MCP 不是模型 | MCP is a connection protocol, not a trained AI model. | MCP 是连接协议，不是经过训练的 AI 模型。 |
| MCP is not an agent | MCP 不是智能体 | MCP does not itself decide or act toward a goal. | MCP 本身不会为了目标自主作决定和行动。 |
| MCP is not an API | MCP 不是 API | MCP is a standard protocol that can expose capabilities to AI applications. | MCP 是把能力提供给 AI 应用的标准协议，不是某个服务接口。 |
| capability provider | 能力提供方 | A server or system that makes tools or resources available. | 把工具、资源或其他功能提供出来的服务器或系统。 |
| capability consumer | 能力使用方 | An application that discovers and uses an exposed capability. | 发现并使用外部能力的应用。 |
| resource provider | 资源提供方 | A server that makes external information available. | 把外部信息作为资源提供出来的服务器。 |
| client-server model | 客户端—服务器模型 | A pattern where a client requests services from a server. | 客户端请求服务、服务器提供服务的结构。 |
| host-client-server chain | 主机—客户端—服务器链路 | The path from the AI host through its client to an MCP server. | AI 主机通过客户端连接 MCP 服务器的关系链。 |
| process flow | 流程 | The ordered steps by which a system performs a task. | 系统按顺序完成任务的一组步骤。 |
| process step | 流程步骤 | One stage in an ordered system flow. | 一套流程中的一个阶段。 |
| Host step | Host 步骤 | Run the AI application. | 运行 AI 应用。 |
| Client step | Client 步骤 | Open an MCP connection. | 打开 MCP 连接。 |
| Protocol step | Protocol 步骤 | Use shared rules. | 使用双方共同遵守的规则。 |
| Server step | Server 步骤 | Expose capabilities. | 提供外部能力。 |
| System step | System 步骤 | Reach an external system. | 连接到外部系统。 |
| run the AI application | 运行 AI 应用 | Start the host application that provides the user experience. | 启动负责提供用户体验的 AI 应用。 |
| open an MCP connection | 打开 MCP 连接 | Establish communication between the host client and server. | 建立主机客户端和服务器之间的通信。 |
| use shared rules | 使用共享规则 | Follow the protocol rules when communicating. | 通信时按照 MCP 的共同规则进行。 |
| expose capabilities | 提供能力 | Make tools, resources, or prompts available. | 把工具、资源或提示提供给应用。 |
| reach an external system | 连接外部系统 | Use the server to access a file, database, or other system. | 通过服务器访问文件、数据库或其他系统。 |
| file system | 文件系统 | The organized environment where files and folders are stored. | 管理文件和文件夹的存储环境。 |
| developer environment | 开发环境 | The tools and systems used to build or operate software. | 开发和运行软件时使用的工具与系统环境。 |
| business workflow | 业务流程 | An ordered set of steps used to complete organizational work. | 企业完成一项工作时按顺序执行的步骤。 |
| external integration | 外部集成 | A connection that brings an outside system into an application workflow. | 把外部系统接入应用流程的连接。 |
| approved access | 获准访问 | Access that has been explicitly allowed. | 已被明确允许的访问权限。 |
| permission | 权限 | Authorization to access or use a system capability. | 被允许访问或使用某项能力的资格。 |
| access control | 访问控制 | Rules and checks that limit access to systems or data. | 限制谁能访问什么数据和系统的规则与检查。 |
| security boundary | 安全边界 | The limit separating trusted application behavior from external systems. | 区分应用内部和外部系统、控制风险的界线。 |
| trust boundary | 信任边界 | A boundary across which data or actions require extra trust decisions. | 数据或操作跨过去时需要额外信任判断的界线。 |
| safe connection | 安全连接 | A connection designed to limit harmful or unauthorized access. | 尽量防止有害或未经授权访问的连接。 |
| approved context | 获准上下文 | Context that the application is allowed to receive and use. | 应用被允许接收和使用的信息。 |
| result for review | 待审核结果 | An output shown for a person to inspect before use. | 在使用前交给人检查的输出结果。 |
| reviewable result | 可复核结果 | A result that can be inspected by a person or process. | 可以由人或流程检查的结果。 |
| real-world example | 现实示例 | An example showing how a concept works in practice. | 说明概念在真实场景中如何工作的例子。 |
| everyday example | 日常示例 | A common use case involving ordinary documents or files. | 普通人日常可能遇到的文件或文档使用场景。 |
| business example | 业务示例 | A use case involving organizational data or systems. | 涉及企业数据或业务系统的使用场景。 |
| data access | 数据访问 | Reading or using data through an approved connection. | 通过获准连接读取或使用数据。 |
| file access example | 文件访问示例 | Using an MCP server to expose approved file resources. | 通过 MCP 服务器提供获准文件资源的例子。 |
| database access example | 数据库访问示例 | Using an MCP server to expose an allowed database capability. | 通过 MCP 服务器提供数据库查询能力的例子。 |
| developer-tool example | 开发者工具示例 | Using an MCP server to make a developer capability available. | 通过 MCP 服务器提供开发工具能力的例子。 |
| business-system connection | 业务系统连接 | A connection from an AI application to a business system. | AI 应用连接企业业务系统的方式。 |
| external capability and context standard | 外部能力与上下文标准 | A shared protocol for how applications discover and use external things. | 规定应用如何发现和使用外部能力与信息的共同协议。 |
| MCP ecosystem | MCP 生态 | The hosts, clients, servers, tools, resources, prompts, and systems that work through MCP. | 围绕 MCP 协作的主机、客户端、服务器、工具、资源、提示和外部系统。 |
| protocol boundary | 协议边界 | The part defined by MCP versus behavior defined by the connected system. | MCP 负责的连接规则与外部系统自身行为之间的界线。 |
| system boundary | 系统边界 | The distinction between the AI application and surrounding tools or systems. | AI 应用与周围工具、数据和系统之间的范围界线。 |
| connection standard | 连接标准 | A common specification for establishing communication. | 规定如何建立通信的共同规范。 |
| context exchange | 上下文交换 | Passing useful context between an application and server. | 应用和服务器之间传递有用背景信息。 |
| capability exchange protocol | 能力交换协议 | Rules for discovering and exchanging available capabilities. | 规范能力发现和交换过程的协议。 |
| external system access | 外部系统访问 | Reaching data or actions in a connected outside system. | 访问已连接的外部系统中的数据或操作。 |
| service | 服务 | A system function made available to other software. | 提供给其他软件使用的系统功能。 |
| operation | 操作 | A specific computation, lookup, or action performed by a system. | 系统执行的一次具体计算、查询或动作。 |
| capability result | 能力结果 | The output returned after using an external capability. | 使用外部能力后返回的输出。 |
| server result | 服务器结果 | The result returned by an MCP server after handling a request. | MCP 服务器处理请求后返回的结果。 |
| application result | 应用结果 | The result the AI application can use or present to a user. | AI 应用可以使用或展示给用户的结果。 |
| connection request | 连接请求 | A request used to establish or use a system connection. | 用来建立或使用系统连接的请求。 |
| system access rules | 系统访问规则 | Rules that determine which data or actions may be reached. | 决定可以访问哪些数据或操作的系统规则。 |
| protocol-defined behavior | 协议定义的行为 | Behavior specified by the shared MCP rules. | 由 MCP 共同规则明确规定的行为。 |
| application-defined behavior | 应用定义的行为 | Behavior controlled by the host application or its workflow. | 由主机应用或业务流程控制的行为。 |
| server-defined behavior | 服务器定义的行为 | Behavior controlled by the connected MCP server. | 由连接的 MCP 服务器控制的行为。 |
| no video available | 视频暂不可用 | The page marks its explainer video as not available yet. | 页面说明该主题的视频讲解目前还没有。 |

## Potential Missing Concepts

- **JSON-RPC（JSON-RPC）**：页面只说 MCP 使用共享规则，没有说明很多 MCP 实现所依赖的请求、响应和错误消息格式。
- **transport（传输层）**：页面没有说明客户端和服务器通过什么通信通道传输 MCP 消息。
- **stdio transport（标准输入输出传输）**：页面没有展开本地 MCP 服务器常见的 stdio 连接方式。
- **Streamable HTTP（可流式 HTTP）**：页面没有说明远程 MCP 连接的 HTTP 传输方式。
- **SSE / Server-Sent Events（服务器发送事件）**：页面没有解释曾经常见的 HTTP 事件流传输方式及其适用边界。
- **initialize（初始化）**：页面没有介绍客户端和服务器建立会话时的初始化握手。
- **capability negotiation（能力协商）**：页面提到能力被发现和交换，但没有说明双方如何声明各自支持的能力。
- **protocol version（协议版本）**：页面没有说明客户端和服务器如何协商或校验协议版本。
- **message（消息）**：页面说能力和上下文会被交换，但没有介绍承载这些信息的请求、响应、通知消息。
- **request / response / notification（请求／响应／通知）**：没有区分需要回复的消息和单向通知。
- **tool schema（工具模式）**：页面提到工具，但没有说明工具名称、描述、输入字段和类型如何被声明。
- **input schema（输入模式）**：没有解释工具如何描述可接受的参数结构。
- **structured content（结构化内容）**：没有说明工具结果或资源内容如何按结构返回。
- **content block（内容块）**：页面没有介绍文本、图片或其他结果内容可能如何组织。
- **resource URI（资源 URI）**：页面提到资源，但没有说明资源如何被唯一定位和读取。
- **resource template（资源模板）**：没有说明带变量的资源地址如何让应用按参数访问资源。
- **resource subscription（资源订阅）**：页面没有介绍客户端如何获知资源内容发生变化。
- **roots（根目录）**：页面举了获准文件夹，但没有说明客户端如何声明允许服务器使用的文件系统根目录。
- **prompts vs prompt templates（提示与提示模板）**：页面提到 prompts，但没有区分一次性提示和可复用、带参数的提示模板。
- **sampling（采样）**：没有介绍服务器如何请求主机中的语言模型生成内容。
- **elicitation（信息征询）**：页面没有说明服务器如何向用户请求补充信息或确认。
- **completion（补全）**：没有讨论提示参数或资源模板参数的补全能力。
- **pagination（分页）**：没有说明工具、资源或提示列表很大时如何分批返回。
- **cancellation（取消）**：没有说明客户端如何取消仍在执行的请求。
- **progress notification（进度通知）**：没有介绍长时间工具调用如何向用户报告进度。
- **logging（日志）**：页面没有说明服务器如何把调试或运行信息传给主机。
- **error object（错误对象）**：页面没有讲失败时的错误码、错误消息和可恢复性。
- **timeout（超时）**：没有讨论外部系统响应过慢时连接如何处理。
- **retry（重试）**：没有说明暂时性网络或服务错误是否可以安全重试。
- **authentication（身份认证）**：页面说有访问规则，但没有解释如何证明连接方是谁。
- **authorization（授权）**：页面提到批准和访问规则，但没有区分身份认证与授权决策。
- **OAuth（OAuth）**：没有介绍远程 MCP 服务器可能采用的授权协议。
- **user consent（用户同意）**：没有说明用户何时需要同意服务器读取数据或执行操作。
- **user confirmation（用户确认）**：没有说明高风险工具调用是否应在执行前要求用户确认。
- **least privilege（最小权限）**：页面没有明确说明只授予完成任务所需的最低访问权限。
- **sandboxing（沙箱隔离）**：没有讨论如何把 MCP 服务器或工具限制在隔离环境中运行。
- **trust model（信任模型）**：没有说明主机、客户端、服务器和外部系统之间应如何建立信任。
- **server provenance（服务器来源）**：没有介绍如何判断 MCP 服务器来自谁、是否可信。
- **tool poisoning（工具投毒）**：页面没有讨论恶意工具描述或返回内容影响模型行为的风险。
- **prompt injection through tools or resources（经工具或资源注入的提示攻击）**：没有说明外部内容可能包含操纵模型的指令。
- **data exfiltration（数据外泄）**：没有展开工具或服务器把敏感数据发送到不应到达位置的风险。
- **secret handling（机密处理）**：文件和业务系统可能包含密钥，但页面没有说明密钥如何保护。
- **audit log（审计日志）**：没有介绍谁访问了什么资源、调用了什么工具的可追溯记录。
- **observability（可观测性）**：页面没有说明如何监控 MCP 连接、调用、错误和延迟。
- **latency（延迟）**：没有讨论发现能力、调用服务器和访问外部系统所花的时间。
- **availability（可用性）**：没有说明外部服务器不可用时应用如何继续工作。
- **rate limiting（速率限制）**：没有讨论如何限制工具调用或数据库查询的频率。
- **cost control（成本控制）**：没有说明远程调用、数据库访问或模型使用可能产生的成本。
- **idempotency（幂等性）**：没有解释重试一个会产生副作用的工具调用是否安全。
- **side effect（副作用）**：页面讲到行动和工具，但没有区分只读操作和会改变外部系统的操作。
- **read-only tool（只读工具）**：没有明确介绍只读取信息、不修改系统的工具类型。
- **destructive action（破坏性操作）**：没有说明删除、发送或修改业务数据等高风险动作。
- **human-in-the-loop（人在回路中）**：页面提到 review，但没有展开人在工具调用前后如何审批和接管。
- **approval workflow（审批流程）**：没有说明工具调用从请求、审核到执行的具体流程。
- **failure handling（失败处理）**：没有讨论服务器、工具或外部系统失败后的恢复路径。
- **fallback（备用路径）**：没有说明服务器不可用或能力不支持时应用如何选择替代方案。
- **compatibility（兼容性）**：没有说明不同 MCP 客户端、服务器或版本之间如何保持兼容。
- **conformance（符合规范）**：没有介绍如何测试一个实现是否真正遵守 MCP 规范。
- **MCP SDK（MCP 软件开发工具包）**：页面没有提到帮助开发客户端或服务器的 SDK。
- **MCP server implementation（MCP 服务器实现）**：页面说明服务器能提供能力，但没有说明如何开发或部署服务器。
- **remote server（远程服务器）**：页面没有区分运行在本机与网络另一端的 MCP 服务器。
- **local server（本地服务器）**：页面举了文件访问，但没有说明本地服务器的运行边界。
- **server lifecycle（服务器生命周期）**：没有说明服务器启动、连接、运行、关闭和重启的过程。
- **session（会话）**：页面没有介绍一次 MCP 连接从建立到结束的状态。
- **state（状态）**：没有讨论服务器或工具调用是否保存跨请求状态。
- **statelessness（无状态性）**：没有说明每次请求是否独立处理。
- **context propagation（上下文传递）**：没有解释上下文如何从外部资源经过服务器进入 AI 应用。
- **provenance（来源追踪）**：没有说明返回的文件或数据库内容来自哪里、如何标记来源。
- **citation（引用）**：没有讨论 AI 应用如何在使用外部资源时保留来源引用。
- **data freshness（数据新鲜度）**：没有说明外部资源内容是否最新或何时更新。
- **schema evolution（模式演进）**：没有讨论工具输入输出模式发生变化时如何兼容旧客户端。
- **domain-specific server（领域服务器）**：没有说明一个 MCP 服务器可以专门连接某类业务系统。
- **connector（连接器）**：页面没有把连接外部系统的服务器称作连接器或适配器。
- **adapter（适配器）**：没有解释如何把已有 API 或数据库包装成 MCP 能力。
- **gateway（网关）**：没有讨论一个中间网关如何统一管理多个外部 MCP 服务器。
- **multi-server composition（多服务器组合）**：没有说明一个主机如何同时连接多个 MCP 服务器。
- **tool discovery UI（工具发现界面）**：没有讨论用户如何查看、理解和选择服务器提供的工具。
- **context window impact（上下文窗口影响）**：没有说明外部资源内容会占用模型上下文窗口。
- **relevance filtering（相关性过滤）**：没有介绍应用如何只把与请求相关的资源内容送给模型。
- **data minimization（数据最小化）**：没有说明连接时只发送完成任务所需的最少数据。
- **privacy boundary（隐私边界）**：文档和业务数据可能敏感，但页面没有展开隐私保护范围。
- **security vs safety（安全防护与安全性）**：页面使用 safety，但没有区分系统安全、数据安全与输出安全。
- **governance（治理）**：没有讨论组织如何登记、批准、审查和撤销 MCP 服务器与工具。

## Aliases / Synonyms

- Model Context Protocol ↔ MCP ↔ model context protocol
- MCP host ↔ host ↔ host application ↔ AI application host
- MCP client ↔ client ↔ host-side client
- MCP server ↔ server ↔ server-side capability provider ↔ supported server
- MCP protocol ↔ protocol ↔ standard protocol ↔ connection standard
- external capability ↔ capability ↔ system capability ↔ exposed capability
- external context ↔ context ↔ approved context ↔ context available to the application
- external system ↔ connected system ↔ business system ↔ developer system
- tool ↔ external tool ↔ approved tool ↔ callable capability
- resource ↔ external resource ↔ file resource ↔ data resource
- prompt ↔ available prompt ↔ prompt template（prompt template 是 prompt 的一种更具体形式，不完全同义）
- interface ↔ standardized interface ↔ service interface ↔ API（API 是一种接口，但不等于 MCP）
- connection ↔ MCP connection ↔ AI connection ↔ server connection
- connect ↔ integrate ↔ establish a connection ↔ reach an external system
- discover ↔ capability discovery ↔ context discovery ↔ find available capabilities
- exchange ↔ capability exchange ↔ context exchange ↔ communicate
- expose ↔ make available ↔ provide ↔ publish a capability
- access ↔ file access ↔ data access ↔ external system access
- access rules ↔ own access rules ↔ system access rules ↔ permissions
- approved access ↔ allowed access ↔ authorized access
- user request ↔ request ↔ input ↔ task request（input 的范围比 user request 更广）
- result ↔ output ↔ response ↔ capability result ↔ server result
- review ↔ human review ↔ result review ↔ inspection
- AI agent ↔ agent ↔ goal-directed application system
- tool calling ↔ tool call ↔ tool request ↔ specific tool action request
- model ↔ AI model ↔ trained model（页面只使用 model，没有展开 trained model）
- API ↔ application programming interface ↔ service interface
- external tool and data ↔ tools and resources ↔ external capabilities and context
- host-client-server chain ↔ AI Application / Host → MCP Client → MCP Protocol → MCP Server
- USB for AI connections ↔ USB analogy ↔ common connection standard analogy
- file system ↔ files and folders ↔ approved folder resources
- database ↔ data store ↔ queryable records
- database query ↔ query ↔ request to query a database
- business system ↔ business application ↔ organizational system
- developer tool ↔ development tool ↔ software tool
- system ↔ external system ↔ connected system
- standardization ↔ standard protocol ↔ interoperability

## Do Not Confuse Candidates

- **MCP vs AI application**：MCP 是连接外部能力和上下文的协议；AI application 是使用该协议提供用户体验的应用。
- **MCP vs AI agent**：MCP 规定连接和能力交换；AI agent 是能够围绕目标决定并采取行动的系统。
- **MCP vs model**：MCP 不是训练出来的模型，而是应用与外部系统之间的协议。
- **MCP vs tool**：MCP 不是某个搜索、文件或数据库工具；它规定工具如何被发现和提供。
- **MCP vs tool calling**：MCP 标准化应用与服务器之间的能力发现和交换；tool calling 是请求某个工具执行特定动作的机制。
- **MCP vs API**：API 是服务提供的接口；MCP 是可让 AI 应用接入能力的标准协议。
- **protocol vs interface**：协议是通信双方共同遵守的规则；接口是使用某个服务或组件的入口和方式。
- **host vs client**：host 是提供用户体验并协调连接的 AI 应用；client 是运行在 host 内部、与 server 通信的组件。
- **client vs server**：client 通常发起请求并消费能力；server 提供工具、资源或提示。
- **MCP client vs MCP server**：客户端在主机中使用能力；服务器把批准的能力暴露出来。
- **server vs external system**：MCP server 是连接和暴露能力的服务器；external system 是它实际连接的文件、数据库、开发工具或业务系统。
- **resource vs tool**：resource 主要提供可读取的外部信息；tool 主要提供可以执行的操作。
- **resource vs context**：resource 是外部信息能力的一种；context 是应用完成任务时使用的信息，可能来自资源。
- **prompt vs tool**：prompt 提供指导文字或模板；tool 执行外部操作。
- **prompt vs user request**：prompt 可以是服务器提供的可复用指导；user request 是用户当前提出的任务要求。
- **input vs resource**：input 是当前任务送进系统的信息；resource 是可被应用访问的一类外部信息来源。
- **output vs result**：页面中两者都可指处理后返回的信息，但 output 更偏系统输出，result 更偏请求或操作的结果。
- **approved capability vs available capability**：available 只表示可提供；approved 还强调经过允许或授权。
- **access vs authorization**：access 是实际能够使用；authorization 是决定是否允许使用的控制过程。
- **authentication vs authorization**：authentication 证明“你是谁”；authorization 决定“你能做什么”。页面没有展开两者，但容易混淆。
- **access rules vs protocol rules**：访问规则限制能读什么、做什么；协议规则规定系统如何通信。
- **USB standard vs MCP**：USB 是设备连接标准的类比；MCP 是 AI 应用连接外部能力的实际协议。
- **common interface vs common capability**：接口统一的是连接方式；能力本身仍由服务器或外部系统提供。
- **database vs MCP server**：数据库保存业务记录；MCP server 可以把数据库查询能力通过协议提供给 AI 应用。
- **file vs file resource**：file 是存储中的文件；file resource 是通过服务器暴露给应用使用的文件信息。
- **folder vs approved folder**：folder 是一般存储位置；approved folder 还包含“允许应用访问”的权限含义。
- **developer tool vs MCP tool**：developer tool 是外部开发软件；MCP tool 是通过 MCP 暴露给 AI 应用的可调用能力。
- **business system vs business example**：business system 是被连接的外部系统；business example 是说明连接用途的场景。
- **user experience vs system capability**：user experience 是用户看到和操作的整体体验；system capability 是系统能执行的功能。
- **connection vs integration**：connection 强调建立通信关系；integration 强调让多个系统在工作流中协同。
- **discover vs exchange**：discover 是找出有哪些能力；exchange 是在系统之间传递能力、上下文或结果。
- **expose vs execute**：expose 是把能力提供给应用；execute 是实际执行某项操作。
- **server capability vs tool action**：server capability 是可用功能；tool action 是使用功能后实际执行的一次动作。
- **request vs query**：request 是广义请求；query 通常特指向数据库或系统查询信息。
- **result vs review**：result 是返回的信息；review 是对结果进行检查的过程。
- **review vs approval**：review 是检查；approval 是检查后明确允许继续使用或执行。
- **external context vs model context**：external context 来自外部系统；model context 是模型当前接收到的整体上下文，范围可能更大。
- **context vs context window**：context 是任务相关信息；context window 是模型一次能够处理的上下文容量。
- **AI application vs AI agent**：AI 应用可以只是提供交互和连接；AI agent 还强调面向目标的决策与行动。
- **API call vs MCP connection**：API call 是一次调用某个服务接口；MCP connection 是应用与 MCP server 之间可持续使用的连接关系。
- **tool calling vs API calling**：tool calling 是面向模型或应用的工具请求机制；API calling 是向某个服务接口发送请求，两者可以组合。
- **MCP server vs gateway**：MCP server 提供具体能力；gateway 可能作为中间层代理或统一管理多个服务。
- **local server vs remote server**：local server 与主机在本机或近端运行；remote server 通过网络访问，页面未展开这一区别。
- **capability discovery vs tool discovery**：能力发现可包含工具、资源和提示；工具发现只关注工具。
- **approved tool vs safe tool**：approved 表示被允许；safe 还涉及实际风险，获准并不自动代表绝对安全。
- **system safety vs output quality**：安全关心是否带来风险；质量关心结果是否正确、有用和符合任务。
- **file content vs context**：文件内容是具体数据；只有被选取并送入任务时，才成为应用使用的上下文。
- **server access rules vs host policy**：服务器有自己的访问规则；主机也可能有额外的用户确认或组织政策。
- **protocol boundary vs system boundary**：协议边界说明哪些行为由 MCP 定义；系统边界说明 AI 应用和外部系统各自属于哪里。
- **MCP ecosystem vs MCP protocol**：生态包括实现、应用和外部系统；协议只是其中定义通信规则的部分。

## Notes

- 本文件是 Module 09 Topic 04 的 raw glossary 收集稿，目标是最大化保留 `mcp.html` 正文中出现或明确指向的术语、机制、流程节点、指标性词语、缩写、别名和易混淆概念；不做去重、归并或最终取舍。
- 页面标题是 “What is MCP?”，页面导语把 MCP 定义为让 AI applications 通过 standardized interface 连接 external tools and data 的 protocol。
- 页面定义段明确说明 Model Context Protocol 定义了 AI applications 发现并与 external capabilities and context 交互的 standard way。
- 页面明确指出 MCP 不是 agent、model 或 tool 本身；“What it is NOT”进一步对照 AI Agent、Tool Calling 和 API。
- 页面使用 “USB for AI connections” 作为类比：USB standard 规定 device 如何连接，但不定义 device 本身；MCP 规定 AI application 如何连接 supported servers and capabilities，但不变成 database 或 tool。
- 页面主流程必须保留为：1 · Host → 2 · Client → 3 · Protocol → 4 · Server → 5 · System；对应 Run the AI application、Open an MCP connection、Use shared rules、Expose capabilities、Reach an external system。
- 流程中的 Host 是 host application，负责 user experience 和 coordinate the connection；Client 是 host 内部的 MCP client；Server 提供 approved tools、resources 或 prompts；System 指 files、databases、developer tools 或 business systems。
- 页面正文具体出现的三类服务器侧能力是 tools、resources 和 prompts；raw 阶段将它们分别记录，也保留 tools / resources / external system 的组合表达。
- Everyday example 的输入是关于 approved folder 中 documents 的 request；MCP server exposes file resources；输出是 relevant file content 作为 context 可用。
- Business example 的输入是 query a database 或 use a developer tool 的 request；MCP server exposes the allowed capability and applies its own access rules；输出是 AI application 可以使用或 present for review 的 result。
- Related concepts 的概念链原文是：AI Application / Host → MCP Client → MCP Protocol → MCP Server → Tools / Resources / External System。
- Related concepts 页面链接了 AI Agent、Tool Calling、Agent Loop、Context Window；本 raw 文件保留这些相邻主题名作为上下文候选，但只把前三个在本页有明确边界的内容作为重点对照。
- 页面中的 “approved”“allowed”“own access rules” 表明连接标准本身不等于自动获得所有权限；服务器或外部系统仍会应用自己的访问规则。
- 页面中的 result 可以被 AI application use 或 present for review；这说明 MCP 解决连接与能力提供，不代表每个外部结果都应不经复核直接执行。
- 页面没有展开具体 wire format、transport、authentication、authorization、tool schema、resource URI、session 或安全治理机制；这些被放进 Potential Missing Concepts，而不是当作页面已解释的事实。
- 页面没有列出 latency、throughput、accuracy 等数值指标；“指标”候选只保留与访问、连接、结果、review 相关的可操作性词语，不虚构页面未给出的数值。
- 页面中的 Video 卡片标记为 “not available yet”；这是页面状态信息，不是 MCP 核心概念，但作为低优先级候选和备注保留。
- 页面中的英文大小写和复数形式同时具有语义价值：MCP、MCP Client、MCP Server、Tools、Resources、External System；raw 阶段暂不统一大小写或单复数。
- 同一个英文词在不同上下文中可能对应不同中文译法，例如 host 可译为主机或宿主应用，resource 可译为资源或外部信息；raw 阶段暂时保留上下文差异，后续再统一术语规范。
- “API”在页面中被定义为 interface provided by a service；不要把 MCP 直接写成 API，也不要把 MCP 服务器提供的能力和底层 API 完全等同。
- “Tool Calling”在页面中是 model or application mechanism for requesting a specific tool action；它可以与 MCP 配合，但两者的抽象层次不同。
- “AI Agent”在页面中是 an application system that can decide and take actions toward a goal；MCP 可以成为 agent 的连接方式，但不是 agent 的决策循环。
