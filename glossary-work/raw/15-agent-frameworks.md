# Topic

Agent Frameworks

Module/Topic/Source File

- Module: 15 · Agent Development
- Topic: Agent Frameworks
- Source File: `agent-frameworks.html`
- Source page title: `Agent Frameworks · Agent Development`

## Glossary Candidates

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Agent Frameworks | 智能体框架；代理框架 | Reusable software building blocks for creating AI agent systems. | 帮开发者搭建 AI 智能体系统的一组可复用软件组件。 |
| agent framework | 智能体框架 | A development layer that organizes models, tools, state, memory, and workflows. | 把模型、工具、状态、记忆和工作流组织起来的开发层。 |
| framework | 框架 | A reusable structure and set of components for building software. | 帮你按固定结构组装软件的一套基础工具和规则。 |
| AI system | AI 系统 | A complete system that uses AI capabilities to perform work. | 使用 AI 能力完成工作的完整系统。 |
| AI application | AI 应用 | A concrete application built from models, tools, logic, and data. | 用模型、工具、逻辑和数据组成的具体 AI 软件。 |
| AI agent system | AI 智能体系统 | An AI system that can reason, use capabilities, and take steps toward a task. | 能思考、使用能力并逐步完成任务的 AI 系统。 |
| agent | 智能体；代理 | A system that can decide or act toward a goal. | 能围绕目标做判断并采取行动的系统。 |
| developer | 开发者 | A person who designs and builds software. | 设计和编写软件的人。 |
| reusable building block | 可复用构建块 | A software part that can be used in more than one system. | 可以在不同系统中重复使用的软件部件。 |
| building block | 构建块 | A component used to assemble a larger system. | 用来拼装更大系统的一个小部件。 |
| model | 模型 | An AI model that provides reasoning or generation capability. | 提供推理或生成能力的 AI 模型。 |
| instructions | 指令 | Guidance telling a model or system what to do. | 告诉模型或系统应该做什么的说明。 |
| tool | 工具 | An external capability that a model or agent can call. | 模型或智能体可以调用的外部能力。 |
| state | 状态 | Information about the current condition or progress of a system. | 系统当前情况或进度的信息。 |
| memory | 记忆 | Information retained for use later in an interaction or workflow. | 保存下来、之后还可以使用的信息。 |
| state / memory | 状态／记忆 | Current workflow information and retained information used by an agent. | 智能体当前的进度信息和可长期使用的信息。 |
| agent logic | 智能体逻辑 | The rules and decisions that determine how an agent behaves. | 决定智能体如何判断、循环和行动的逻辑。 |
| model + instructions + tools + state / memory + agent logic | 模型＋指令＋工具＋状态／记忆＋智能体逻辑 | The page's mental model for the ingredients of an agent framework. | 页面用来说明智能体框架由哪些部分组成的组合模型。 |
| mental model | 心智模型 | A simplified way to understand how a system works. | 用来快速理解系统如何工作的简化图景。 |
| Core | 核心 | The central idea that should be remembered. | 一页内容中最需要记住的中心观点。 |
| system-building layer | 系统构建层 | A layer used to assemble and control an application. | 用来组装和控制应用的一层软件结构。 |
| framework is not the model | 框架不是模型 | A framework builds and organizes a system; the model supplies AI capability. | 框架负责搭系统，模型负责提供 AI 能力，两者不是一回事。 |
| why frameworks exist | 框架为什么存在 | The reasons developers use frameworks to build agent systems. | 开发者为什么要用框架搭建智能体系统。 |
| without a framework | 没有框架 | Building a system while managing common mechanisms manually. | 不使用框架时，开发者自己处理各种通用机制。 |
| with a framework | 使用框架 | Building with reusable orchestration components. | 使用可复用的编排组件来搭建系统。 |
| manually manage | 手动管理 | Control a mechanism directly in application code. | 开发者在代码里亲自处理某个机制。 |
| tool calls | 工具调用 | Requests from an agent or model to an external tool. | 智能体或模型向外部工具发出的调用请求。 |
| state management | 状态管理 | Keeping track of the system's current information and progress. | 保存和更新系统当前信息与进度。 |
| agent loops | 智能体循环 | Repeated cycles in which an agent observes, decides, and acts. | 智能体反复观察、判断和行动的循环。 |
| agent loop | 智能体循环 | One repeating control cycle used by an agent. | 智能体不断处理任务时的一轮循环。 |
| routing | 路由；分流 | Sending a request or step to the appropriate model, tool, or agent. | 把请求或步骤交给合适的模型、工具或智能体。 |
| retries | 重试 | Trying an operation again after a temporary failure. | 某次操作失败后再次尝试。 |
| retry | 重试 | A second or later attempt to complete an operation. | 对同一操作的再次尝试。 |
| multi-agent logic | 多智能体逻辑 | Logic for coordinating several agents. | 让多个智能体协作的规则和控制逻辑。 |
| orchestration | 编排；协调 | Coordinating models, tools, agents, steps, and state. | 统筹模型、工具、智能体、步骤和状态如何配合。 |
| reusable orchestration components | 可复用编排组件 | Reusable software parts that coordinate common system patterns. | 可以重复使用、负责协调常见系统模式的软件部件。 |
| system pattern | 系统模式 | A recurring way of structuring a software system. | 软件系统中反复出现的一种组织方式。 |
| common system pattern | 常见系统模式 | A pattern that appears in many applications. | 很多应用都会遇到的通用结构或做法。 |
| assemble | 组装 | Combine components into a working system. | 把多个部件组合成可以工作的系统。 |
| maintain | 维护 | Keep software working and update it over time. | 让软件持续可用并随着时间进行更新。 |
| simple system | 简单系统 | An application with limited steps or integration needs. | 步骤少、集成要求不高的应用。 |
| framework need | 框架需求 | Whether an application benefits from using a framework. | 一个应用是否真的需要框架来帮助开发。 |
| framework landscape | 框架版图 | A view of major frameworks and how they differ. | 对主要框架及其差异的整体观察。 |
| major framework | 主要框架 | A framework highlighted as an important option in the landscape. | 页面重点介绍的、有代表性的框架。 |
| LangGraph | LangGraph | A framework associated with graph and state orchestration. | 以图结构和状态编排为特点的智能体框架。 |
| graph and state orchestration | 图和状态编排 | Orchestration organized as graph steps plus explicit state. | 用图中的步骤和明确状态来组织智能体流程。 |
| graph orchestration | 图编排 | Organizing workflow steps and transitions as a graph. | 把流程步骤和转换关系组织成图。 |
| state orchestration | 状态编排 | Coordinating workflow behavior through explicit state. | 通过明确的状态来控制工作流怎么运行。 |
| controllable workflow | 可控工作流 | A workflow whose steps and transitions can be explicitly controlled. | 步骤和转换都能被开发者明确控制的工作流。 |
| long-running agent workflow | 长时间运行的智能体工作流 | An agent workflow that continues across many steps or a long duration. | 会持续很久或经历很多步骤的智能体流程。 |
| LangChain | LangChain | A framework for general agent tooling and composable components. | 提供通用智能体工具和可组合组件的框架。 |
| general agent tooling | 通用智能体工具 | Reusable tools and patterns for building agent applications. | 用来构建智能体应用的通用工具和模式。 |
| composing components | 组合组件 | Combining separate model, tool, and retrieval parts. | 把模型、工具和检索等独立部件组合起来。 |
| model component | 模型组件 | A software component that connects an application to a model. | 把应用连接到模型的软件部件。 |
| tool component | 工具组件 | A component that exposes an external capability to an agent. | 把外部能力提供给智能体调用的部件。 |
| retrieval component | 检索组件 | A component that finds relevant information for a task. | 为任务查找相关资料的软件部件。 |
| OpenAI Agents SDK | OpenAI Agents SDK | A provider-native SDK for code-first agents with handoffs and tools. | 面向代码优先智能体、交接和工具调用的 OpenAI 原生 SDK。 |
| Agents SDK | Agents SDK | A shortened reference to OpenAI Agents SDK in the page context. | 页面中对 OpenAI Agents SDK 的简称。 |
| provider-native SDK | 提供商原生 SDK | An SDK designed close to a particular model provider. | 与某个模型提供商紧密配套的开发工具包。 |
| code-first agent | 代码优先智能体 | An agent built and controlled primarily through code. | 主要用代码搭建和控制的智能体。 |
| code-first | 代码优先 | A development approach centered on writing code. | 以编写代码为主要方式的开发方法。 |
| handoff | 交接 | Passing a task or conversation from one agent to another. | 把任务或对话交给另一个智能体继续处理。 |
| handoffs | 交接机制 | Multiple transfers of work between agents. | 多个智能体之间传递工作的机制。 |
| Google ADK | Google ADK | A Google provider-native SDK for building agents. | Google 提供的、围绕其模型生态搭建智能体的 SDK。 |
| ADK | ADK | The abbreviation used for Google ADK. | Google ADK 的英文缩写形式。 |
| agent development kit | 智能体开发套件 | The expanded meaning commonly associated with ADK. | ADK 通常可理解为智能体开发套件。 |
| Google model ecosystem | Google 模型生态 | Google's connected set of models and related services. | Google 的模型及相关服务组成的生态。 |
| AutoGen | AutoGen | A framework focused on multi-agent orchestration. | 重点支持多智能体编排的框架。 |
| multi-agent orchestration | 多智能体编排 | Coordinating several agents and their interactions. | 协调多个智能体及其交互过程。 |
| agent-to-agent conversation | 智能体对智能体对话 | A conversation or message exchange between agents. | 智能体之间互相传递消息和讨论任务。 |
| agent collaboration | 智能体协作 | Several agents working together on a task. | 多个智能体一起完成一个任务。 |
| CrewAI | CrewAI | A role-based multi-agent framework. | 按角色组织多个智能体的框架。 |
| role-based multi-agent | 基于角色的多智能体 | A multi-agent design where agents have assigned roles. | 给多个智能体分配不同职责的设计。 |
| role | 角色 | An assigned responsibility or function for an agent. | 分配给智能体的职责或功能。 |
| specialized agent | 专业化智能体 | An agent designed for a narrower responsibility. | 专门负责某一类工作的智能体。 |
| specialist agent team | 专业智能体团队 | A group of agents with different specialized roles. | 由不同专业分工的智能体组成的团队。 |
| assigned role | 指定角色 | A role explicitly given to an agent. | 明确分配给某个智能体的职责。 |
| Semantic Kernel | Semantic Kernel | An enterprise-oriented framework for integrating AI into applications. | 面向企业、用于把 AI 接入现有应用的框架。 |
| enterprise agent tooling | 企业级智能体工具 | Agent-development tools intended for enterprise applications. | 面向企业应用的智能体开发工具。 |
| existing application | 现有应用 | A software application that already exists and is being extended. | 已经存在、现在要接入 AI 的软件应用。 |
| integrate AI capabilities | 集成 AI 能力 | Add AI functions to an existing application. | 把 AI 功能接入现有应用。 |
| framework category | 框架类别 | A grouping of frameworks based on their main style or use. | 按主要风格或用途划分的框架分组。 |
| graph / state orchestration | 图／状态编排 | A category based on explicit steps, transitions, and state. | 以明确步骤、转换和状态为特征的类别。 |
| explicit steps | 明确步骤 | Steps directly represented in a workflow. | 在工作流中直接表示出来的步骤。 |
| transition | 转换；状态转换 | A move from one workflow step or state to another. | 从一个流程步骤或状态进入另一个的变化。 |
| SDK / provider-native | SDK／提供商原生 | A category of tools close to a model provider. | 与模型提供商紧密配套的 SDK 类别。 |
| model provider | 模型提供商 | An organization that provides models and related AI services. | 提供模型及相关 AI 服务的组织。 |
| multi-agent | 多智能体 | Involving several agents that coordinate or collaborate. | 涉及多个需要协调或协作的智能体。 |
| general agent tooling | 通用智能体工具 | General-purpose components for agent application development. | 面向多种智能体应用的通用开发组件。 |
| categories overlap | 类别重叠 | One framework can fit more than one category. | 一个框架可能同时属于多个类别。 |
| framework vs model | 框架与模型 | A distinction between the development structure and AI capability. | 区分“搭系统的结构”和“提供智能能力的模型”。 |
| reasoning capability | 推理能力 | The ability to work through information and reach an answer or decision. | 根据信息分析并得出答案或决定的能力。 |
| generation capability | 生成能力 | The ability to produce new text or other output. | 产生新的文字或其他输出的能力。 |
| organize | 组织 | Arrange components and their interactions into a coherent system. | 把部件及其互动安排成一个完整系统。 |
| workflow | 工作流 | A sequence of steps used to complete a task. | 为完成任务而按顺序执行的一组步骤。 |
| workflow logic | 工作流逻辑 | Rules controlling how workflow steps proceed. | 控制工作流下一步如何进行的规则。 |
| framework vs agent product | 框架与智能体产品 | A distinction between a developer tool and a ready-to-use user experience. | 区分给开发者用的构建工具和给用户直接使用的产品。 |
| agent product | 智能体产品 | A ready-to-use experience that users interact with. | 用户可以直接使用的智能体产品或体验。 |
| ready-to-use experience | 可直接使用的体验 | A finished interface or service intended for end users. | 已经做好、面向最终用户的界面或服务。 |
| user | 用户 | A person who uses an AI application or product. | 使用 AI 应用或产品的人。 |
| product | 产品 | A finished offering that may include software, interface, and operations. | 面向用户提供的完整软件服务或成品。 |
| framework vs workflow platform | 框架与工作流平台 | A distinction between a code-first development layer and an orchestration platform. | 区分代码优先的开发层和工作流编排平台。 |
| workflow platform | 工作流平台 | A platform for designing and running workflows. | 用来设计和运行工作流的平台。 |
| code-first development layer | 代码优先开发层 | A software layer controlled primarily through application code. | 主要通过应用代码控制的软件开发层。 |
| visual orchestration | 可视化编排 | Designing workflow connections through a visual interface. | 用图形界面设计流程和组件之间的连接。 |
| low-code orchestration | 低代码编排 | Building workflow logic with limited hand-written code. | 只写少量代码就能搭建工作流编排。 |
| visual workflow | 可视化工作流 | A workflow represented and edited visually. | 用图形方式表示和编辑的工作流。 |
| n8n | n8n | An example named as a workflow platform. | 页面举例的工作流平台。 |
| Dify | Dify | An example named as a visual or workflow platform. | 页面举例的可视化或工作流平台。 |
| Codex | Codex | An example of an agent product, contrasted with LangGraph. | 页面中作为智能体产品示例、与 LangGraph 对比的名称。 |
| Manus | Manus | An example of an agent product, contrasted with AutoGen. | 页面中作为智能体产品示例、与 AutoGen 对比的名称。 |
| Claude | Claude | An example of a model in the framework-versus-model comparison. | 页面中用来代表模型的示例名称。 |
| GPT | GPT | An example of a model in the framework-versus-model comparison. | 页面中用来代表模型的示例名称。 |
| Gemini | Gemini | An example of a model in the framework-versus-model comparison. | 页面中用来代表模型的示例名称。 |
| LangGraph / Agents SDK | LangGraph／Agents SDK | Examples labeled as frameworks or SDKs. | 页面中作为框架／SDK 示例的一组名称。 |
| OpenAI | OpenAI | The provider associated with OpenAI Agents SDK. | OpenAI Agents SDK 所属的模型提供商名称。 |
| Google | Google | The provider associated with Google ADK. | Google ADK 所属的模型提供商名称。 |
| Microsoft | Microsoft | The provider associated with AutoGen and Semantic Kernel. | AutoGen 和 Semantic Kernel 所属的组织名称。 |
| framework style | 框架风格 | The main design approach used by a framework. | 一个框架主要采用的设计方式。 |
| typical fit | 典型适用场景 | The kind of application a framework commonly suits. | 某个框架通常比较适合的应用类型。 |
| general tooling | 通用工具 | Tools not limited to one narrow workflow or provider. | 不只服务于单一流程或提供商的通用工具。 |
| enterprise tooling | 企业级工具 | Tools designed for integration and operation in organizations. | 面向组织级应用集成和运行的工具。 |
| provider relationship | 与提供商的关系 | How closely a framework is tied to a model provider. | 框架与某个模型提供商绑定或配套的程度。 |
| multi-provider | 多提供商 | Supporting models or services from more than one provider. | 支持多个模型提供商，而不是只支持一家。 |
| OpenAI-native | OpenAI 原生 | Designed especially around OpenAI's model ecosystem. | 主要围绕 OpenAI 生态设计。 |
| Google-native | Google 原生 | Designed especially around Google's model ecosystem. | 主要围绕 Google 生态设计。 |
| code-first support | 代码优先支持 | Support for building and controlling systems through code. | 支持用代码搭建和控制系统。 |
| multi-agent support | 多智能体支持 | Features that allow several agents to coordinate. | 允许多个智能体协同工作的能力。 |
| Possible | 可能支持 | A comparison value indicating a capability can be built or used. | 表示该能力可以实现或使用，但不是页面强调的核心。 |
| Supported | 支持 | A comparison value indicating a capability is available. | 表示该能力在框架中可用。 |
| Handoffs | 交接 | A comparison value indicating transfer between agents is supported. | 表示框架支持智能体之间交接任务。 |
| Core focus | 核心重点 | A comparison value indicating the capability is central to the framework. | 表示该能力是框架的核心方向。 |
| graph / state | 图／状态 | A comparison style based on graph structure and state. | 比较表中 LangGraph 的风格标签。 |
| general tooling style | 通用工具风格 | A comparison style based on reusable agent tooling. | 比较表中 LangChain 的风格标签。 |
| provider SDK | 提供商 SDK | An SDK closely associated with a model provider. | 与某个模型提供商紧密关联的开发工具包。 |
| multi-agent style | 多智能体风格 | A design style centered on several coordinating agents. | 以多个协作智能体为中心的设计风格。 |
| role-based style | 基于角色的风格 | A design style that assigns roles to agents. | 通过给智能体分配角色来组织系统的风格。 |
| enterprise tooling style | 企业工具风格 | A design style focused on integrating AI into existing applications. | 重点把 AI 集成进现有企业应用的风格。 |
| controlled workflows | 受控工作流 | Workflows whose steps and execution are explicitly managed. | 步骤和执行过程能被明确管理的工作流。 |
| composable agent apps | 可组合智能体应用 | Agent applications assembled from reusable components. | 由可复用组件组合出来的智能体应用。 |
| OpenAI agent systems | OpenAI 智能体系统 | Agent systems built around OpenAI-native capabilities. | 围绕 OpenAI 原生能力构建的智能体系统。 |
| Google model ecosystem | Google 模型生态 | The models and services around Google's provider platform. | Google 提供的模型和相关服务体系。 |
| agent collaboration | 智能体协作 | A typical fit involving agents working together. | 多个智能体共同完成工作的典型场景。 |
| specialist agent teams | 专业智能体团队 | A typical fit involving agents with specialized responsibilities. | 不同智能体承担不同专业职责的典型场景。 |
| existing applications | 现有应用 | A typical fit for integrating AI into already-built software. | 把 AI 接入已有软件的典型场景。 |
| how to think about choosing | 如何思考框架选择 | A decision guide for matching needs to framework types. | 根据开发需求选择框架类别的思考方法。 |
| code-level control | 代码级控制 | Fine-grained control available through application code. | 可以在代码层面精细控制系统行为。 |
| framework or SDK | 框架或 SDK | A code-oriented option for building an agent system. | 用代码构建智能体系统时可考虑的工具类型。 |
| multi-agent patterns | 多智能体模式 | Reusable designs for agents coordinating with one another. | 多个智能体协调工作的可复用设计。 |
| multi-agent-oriented option | 面向多智能体的选项 | A framework choice designed around multi-agent use cases. | 主要面向多智能体场景的框架选择。 |
| provider-native integration | 提供商原生集成 | Integration closely aligned with a provider's own ecosystem. | 与某个提供商自己的模型和服务紧密连接。 |
| provider SDK | 提供商 SDK | An SDK selected for close provider integration. | 为了紧密接入模型提供商而选择的 SDK。 |
| visual workflow need | 可视化工作流需求 | A need to design or manage a workflow visually. | 希望用图形界面设计或管理工作流的需求。 |
| Module 16 | 第 16 模块 | The module referenced for visual workflow topics. | 页面建议去看的、介绍可视化工作流的第 16 模块。 |
| quick comparison | 快速比较 | A compact comparison of frameworks by shared dimensions. | 用几个共同维度快速比较不同框架。 |
| comparison table | 比较表 | A table that compares frameworks, styles, support, and fit. | 把框架的风格、能力和适用场景放在一起比较的表格。 |
| code-first | 代码优先 | A comparison dimension asking whether code is the main development interface. | 比较一个工具是否主要通过代码来开发。 |
| multi-agent support | 多智能体支持 | A comparison dimension for coordination among agents. | 比较框架是否支持多个智能体协作。 |
| provider relationship | 提供商关系 | A comparison dimension for provider independence or alignment. | 比较框架是跨提供商还是偏向某一家。 |
| typical fit | 典型适配 | A comparison dimension describing a framework's common use. | 比较一个框架通常适合什么用途。 |
| agent system | 智能体系统 | A complete system that combines an agent with models, tools, and workflows. | 将智能体、模型、工具和工作流组合起来的完整系统。 |
| organize models | 组织模型 | Decide how models are connected to and used by the system. | 安排系统如何连接和使用模型。 |
| organize tools | 组织工具 | Decide which tools are available and how they are called. | 安排有哪些工具可用以及如何调用。 |
| organize state | 组织状态 | Track and update the current condition of a workflow. | 跟踪和更新工作流当前的情况。 |
| organize workflows | 组织工作流 | Define and coordinate the steps needed to complete work. | 定义并协调完成任务所需的各个步骤。 |
| remember this | 记住这一点 | The short takeaway at the end of the page. | 页面最后用来总结核心概念的一句话。 |
| developer organization | 开发者组织 | The developer-side arrangement of system parts and behavior. | 开发者对系统部件和行为进行的组织安排。 |
| framework layer | 框架层 | The layer between raw model capabilities and an application. | 位于模型能力和具体应用之间的软件层。 |
| application layer | 应用层 | The user-facing or task-specific layer built on lower components. | 建立在底层组件之上的、面向具体任务或用户的一层。 |
| model layer | 模型层 | The layer providing AI reasoning and generation. | 提供 AI 推理和生成能力的一层。 |
| orchestration layer | 编排层 | The layer coordinating tools, state, agents, and workflow steps. | 协调工具、状态、智能体和流程步骤的一层。 |
| external capability | 外部能力 | A function outside the model that can be invoked when needed. | 模型之外、需要时可以被调用的功能。 |
| capability integration | 能力集成 | Connecting models or tools so they work within an application. | 把模型或工具连接到应用中一起工作。 |
| task | 任务 | Work an agent or application is asked to complete. | 智能体或应用被要求完成的事情。 |
| request | 请求 | An instruction or input asking a system to do something. | 要求系统完成某件事的输入或指令。 |
| step | 步骤 | One unit of work in a workflow. | 工作流中的一个具体动作或阶段。 |
| next step | 下一步 | The step selected after the current step. | 当前步骤完成后要执行的步骤。 |
| decision | 决策 | A choice about what the system should do next. | 系统决定下一步怎么做的选择。 |
| execution | 执行 | Carrying out a chosen step, call, or workflow. | 真正把选定的步骤、调用或流程运行起来。 |
| coordination | 协调 | Managing interactions so several parts work together. | 管理多个部件之间的配合。 |
| collaboration | 协作 | Working jointly toward a shared task or result. | 多个角色一起完成同一个目标。 |
| maintainability | 可维护性 | How easy a system is to update, repair, and operate over time. | 系统长期修改、修复和维护的难易程度。 |
| framework choice | 框架选择 | Selecting a framework based on control, agents, providers, or workflow needs. | 根据控制力、智能体、提供商或工作流需求选框架。 |
| model ecosystem | 模型生态 | A provider's connected models, SDKs, and services. | 某个提供商的模型、SDK 和服务组成的整体。 |
| provider independence | 提供商独立性 | The ability to work with multiple model providers. | 不被某一家模型提供商限制的能力。 |
| code-level workflow | 代码级工作流 | A workflow whose behavior is defined in source code. | 用源代码定义行为的工作流。 |
| visual or low-code | 可视化或低代码 | A development style using visual interfaces or limited code. | 通过图形界面或少量代码搭建系统的方式。 |
| ready-made experience | 现成体验 | A product already packaged for users. | 已经包装好、用户拿来就能用的产品体验。 |
| development tool | 开发工具 | Software used by developers to build another application. | 开发者用来构建其他应用的软件。 |
| end user | 最终用户 | The person who uses the completed product or experience. | 真正使用成品应用或服务的人。 |

## Potential Missing Concepts

- **API（应用程序接口）**：正文讲到模型、工具和 SDK，但没有单独说明应用如何通过 API 调用模型或外部服务。
- **library（库）**：页面使用 framework、SDK 和 tooling，但没有解释 library 与 framework 在控制反转和使用范围上的区别。
- **package / module（包／模块）**：可复用组件被反复提到，但没有说明它们在代码组织中的具体封装形式。
- **runtime（运行时）**：页面讨论长时间运行的智能体工作流，但没有定义负责执行这些流程的运行环境。
- **execution engine（执行引擎）**：编排、步骤和转换出现了，但没有说明由什么组件真正驱动工作流执行。
- **workflow graph（工作流图）**：LangGraph 的 graph style 出现了，但没有解释节点和边如何表达流程。
- **node / edge（节点／边）**：图编排的基础结构没有在正文中明确命名。
- **event-driven workflow（事件驱动工作流）**：状态和转换出现了，但没有说明事件如何触发下一步。
- **durable execution（持久化执行）**：long-running workflow 出现了，但没有讨论暂停、恢复和跨进程继续运行。
- **checkpoint（检查点）**：state orchestration 可能需要保存中间状态，但正文未介绍状态快照或检查点。
- **persistence（持久化）**：memory 和 long-running workflows 出现了，但没有说明状态如何跨请求或重启保存。
- **short-term memory / long-term memory（短期记忆／长期记忆）**：页面把 state 和 memory 并列，但没有区分两种记忆范围。
- **context（上下文）**：模型、指令、工具和状态需要组合进上下文，但正文没有展开上下文构造。
- **context window（上下文窗口）**：模型在长流程中可接收的信息量限制没有介绍。
- **prompt（提示词）**：instructions 直接出现，但没有说明 prompt 与一般 instruction 的关系。
- **structured output（结构化输出）**：框架通常需要在组件之间传递稳定格式，页面没有说明输出 schema。
- **schema（模式／结构定义）**：状态和工具参数需要结构约束，但正文未定义 schema。
- **tool schema（工具模式）**：tool calls 被提到，但没有说明工具名称、参数和返回值如何声明。
- **function calling（函数调用）**：tool calls 的常见实现机制未在本页单独解释。
- **tool result（工具结果）**：工具调用后返回的信息是 agent loop 的关键输入，但页面没有展开。
- **planning（规划）**：agent logic 出现了，但没有专门介绍智能体如何先拆解任务再执行。
- **task decomposition（任务分解）**：多步骤 workflow 和 multi-agent patterns 出现，但没有定义将大任务拆成子任务。
- **decision policy（决策策略）**：routing、handoff 和 next step 出现，但没有说明选择规则的形式。
- **reactive agent（反应式智能体）**：agent loops 被提到，但未区分反应式执行与预先规划。
- **supervisor agent（监督者智能体）**：multi-agent orchestration 可能需要协调者，但正文没有这个角色概念。
- **worker agent（工作者智能体）**：specialist agents 出现，但没有定义由上层协调的工作者角色。
- **delegation（任务委派）**：handoff 出现，但没有区分任务委派、转交和协作。
- **conversation state（对话状态）**：agent-to-agent conversations 被提到，但没有说明如何保存对话历史。
- **message passing（消息传递）**：agent collaboration 需要通信机制，但正文未定义消息协议。
- **agent communication protocol（智能体通信协议）**：多智能体协作的消息格式和规则未展开。
- **parallel execution（并行执行）**：多个智能体可能并行工作，但页面只讲协调，没有比较串行与并行。
- **sequential execution（串行执行）**：workflow steps 被提到，但没有明确说明按顺序执行的模式。
- **concurrency（并发）**：长流程和多智能体系统的并发控制没有介绍。
- **async / asynchronous（异步）**：长时间运行和工具调用可能需要异步机制，但正文没有展开。
- **timeout（超时）**：retries 出现了，但没有说明操作超过时限时如何处理。
- **backoff（退避）**：retry 机制通常需要等待策略，页面没有介绍指数退避等做法。
- **failure handling（失败处理）**：retries 被提到，但没有说明失败分类、降级或终止流程。
- **fallback（回退／降级）**：多模型、多工具或多代理流程可能需要备用路径，正文未说明。
- **error propagation（错误传播）**：多个组件编排时错误如何传递没有讨论。
- **idempotency（幂等性）**：重试工具调用可能重复执行副作用，但正文没有说明如何避免。
- **observability（可观测性）**：长流程、路由和工具调用需要追踪，但页面没有介绍日志、指标和追踪。
- **tracing（链路追踪）**：agent loop 和 handoff 的执行链没有说明如何被记录。
- **logging（日志）**：维护和调试框架应用所需的日志没有单独出现。
- **telemetry（遥测）**：运行时状态和性能数据的采集没有展开。
- **evaluation（评估）**：页面谈选择和典型适用场景，但没有说明如何评估框架或智能体效果。
- **agent evaluation（智能体评估）**：没有介绍任务完成率、工具使用正确性或协作质量的评估。
- **latency（延迟）**：多步编排和多智能体调用可能增加等待时间，但正文没有讨论。
- **throughput（吞吐量）**：框架处理请求的规模和并发能力没有说明。
- **cost（成本）**：工具调用、模型调用和长期运行的成本没有讨论。
- **token usage（令牌用量）**：多轮对话和状态传递会影响用量，但页面没有介绍。
- **rate limit（速率限制）**：provider-native SDK 与多提供商调用可能受限制，正文未展开。
- **authentication（身份认证）**：接入模型和外部工具所需的凭证没有说明。
- **authorization（授权）**：工具、状态和 handoff 的权限边界没有介绍。
- **permissions（权限）**：框架如何限制 agent 可调用的工具和数据未展开。
- **sandbox（沙箱）**：工具调用的安全隔离没有在本页说明。
- **guardrails（护栏）**：agent logic 和工具使用需要约束，但正文没有定义安全护栏。
- **human-in-the-loop（人在回路中）**：长流程或高风险行动可能需要人工确认，但页面没有介绍。
- **approval step（审批步骤）**：工作流可以有人工批准节点，但正文未展开。
- **security（安全）**：框架、工具和多智能体交互的攻击面没有讨论。
- **prompt injection（提示注入）**：模型、工具和外部资料组合时的注入风险没有提到。
- **data privacy（数据隐私）**：state、memory 和工具数据的隐私处理没有说明。
- **provider lock-in（提供商锁定）**：provider relationship 出现，但没有讨论绑定一家提供商的长期代价。
- **portability（可移植性）**：multi-provider 与 provider-native 之间的迁移能力没有展开。
- **versioning（版本管理）**：框架、模型和工具升级可能影响流程，但正文未说明兼容策略。
- **backward compatibility（向后兼容）**：现有应用集成和框架升级的兼容性没有讨论。
- **dependency management（依赖管理）**：SDK 和组件组合可能带来依赖问题，页面未介绍。
- **testing（测试）**：框架应用的单元测试、集成测试和流程测试没有说明。
- **simulation（模拟）**：多智能体交互和工具调用可通过模拟测试，但正文未展开。
- **mock tool（模拟工具）**：测试 agent tool calls 所需的替代工具没有介绍。
- **deployment（部署）**：页面讨论应用构建，但没有说明框架应用如何上线。
- **production（生产环境）**：典型 fit 和 enterprise tooling 出现，但生产运行要求未展开。
- **scalability（可扩展性）**：长时间运行和多智能体系统的规模扩展没有讨论。
- **reliability（可靠性）**：retries、state 和 maintainability 被提到，但没有定义长期稳定运行。
- **framework abstraction（框架抽象）**：框架隐藏了底层调用细节，但页面没有讲抽象层的收益与代价。
- **abstraction leakage（抽象泄漏）**：框架仍可能暴露提供商、模型和运行时细节，正文未讨论。
- **opinionated framework（有观点的框架）**：不同框架的风格差异没有解释为设计取舍。
- **vendor-neutral（厂商中立）**：multi-provider 的反面概念没有单独命名。
- **open-source framework（开源框架）**：页面列出多个框架，但没有说明授权和社区维护模式。
- **ecosystem maturity（生态成熟度）**：框架选择时的重要因素没有出现在正文。
- **community support（社区支持）**：主要框架之间的学习资源和社区差异未介绍。
- **documentation（文档）**：框架可用性的重要判断因素没有单独列出。
- **learning curve（学习曲线）**：页面按“如何选择”给建议，但没有比较学习成本。
- **framework benchmark（框架基准测试）**：比较表是静态特征对比，不是性能基准测试；正文未定义 benchmark。
- **agent framework versus workflow automation（智能体框架与工作流自动化）**：页面指向 Module 16，但没有详细说明两者的边界。
- **SDK versus framework（SDK 与框架）**：页面把二者放在同一选择路径中，但没有解释 SDK 通常更贴近提供商。
- **framework versus platform（框架与平台）**：页面区分 workflow platform，但没有给出平台的完整定义。
- **framework versus product（框架与产品）**：页面给出对比示例，但没有总结开发者工具和用户成品的层级关系。
- **agent versus agent product（智能体与智能体产品）**：页面使用 agent product，却没有解释单个 agent、应用和产品的关系。
- **model provider versus framework vendor（模型提供商与框架提供方）**：页面提到 OpenAI、Google、Microsoft 和 CrewAI，但没有区分角色。

## Aliases / Synonyms

- Agent Frameworks ↔ agent frameworks ↔ agent framework ↔ framework for AI agents
- framework ↔ development framework ↔ software framework ↔ application framework
- AI application ↔ AI app ↔ agent application ↔ agent app
- AI agent system ↔ agent system ↔ agent-based AI system
- model ↔ AI model ↔ foundation model（在更具体的上下文中不完全等同）
- instructions ↔ guidance ↔ directives ↔ prompt instructions
- tool ↔ external tool ↔ callable tool ↔ agent tool
- tool call ↔ tool invocation ↔ function call（function call 是常见实现形式，不完全等同）
- state ↔ workflow state ↔ execution state ↔ current state
- memory ↔ agent memory ↔ retained information ↔ persistent context（persistent context 不一定等同于 memory）
- agent logic ↔ agent control logic ↔ decision logic ↔ workflow logic
- orchestration ↔ coordination ↔ workflow coordination ↔ system orchestration
- agent loop ↔ agent loop cycle ↔ observe-decide-act loop ↔ reasoning-action loop
- routing ↔ request routing ↔ model routing ↔ agent routing
- retry ↔ retry attempt ↔ re-attempt ↔ retries
- multi-agent ↔ multi-agent system ↔ multi-agent architecture ↔ agent collaboration system
- graph orchestration ↔ graph-based orchestration ↔ graph and state orchestration
- state orchestration ↔ explicit-state orchestration ↔ stateful workflow orchestration
- controllable workflow ↔ controlled workflow ↔ explicitly managed workflow
- long-running workflow ↔ long-running agent workflow ↔ durable workflow（durable 的实现含义更窄）
- general agent tooling ↔ general-purpose agent tooling ↔ reusable agent tooling
- composable components ↔ reusable components ↔ modular building blocks
- provider-native SDK ↔ provider SDK ↔ provider-specific SDK ↔ native SDK
- code-first ↔ code-oriented ↔ programmatic ↔ code-level
- handoff ↔ agent handoff ↔ task transfer ↔ delegation（delegation 不一定意味着完整交接）
- Google ADK ↔ ADK ↔ Google Agent Development Kit（常见展开名）
- OpenAI Agents SDK ↔ Agents SDK ↔ OpenAI agent SDK
- AutoGen ↔ Microsoft AutoGen（提供商前缀在不同语境中可出现）
- CrewAI ↔ role-based multi-agent framework ↔ specialist-agent framework（描述性别名）
- Semantic Kernel ↔ enterprise agent tooling ↔ Microsoft Semantic Kernel（提供商前缀）
- role-based multi-agent ↔ role-oriented multi-agent ↔ agent team with assigned roles
- specialized agent ↔ specialist agent ↔ task-specific agent
- specialist agent team ↔ specialized agent team ↔ role-based agent team
- framework category ↔ framework type ↔ framework class
- graph / state orchestration ↔ graph-based state orchestration
- SDK / provider-native ↔ provider-native SDK category
- multi-agent-oriented option ↔ multi-agent framework option
- general agent tooling ↔ general framework tooling
- visual orchestration ↔ visual workflow orchestration
- low-code orchestration ↔ low-code workflow building
- visual workflow ↔ graphical workflow ↔ visual automation workflow
- workflow platform ↔ workflow automation platform ↔ orchestration platform
- code-first development layer ↔ programmatic development layer ↔ code-based layer
- ready-to-use experience ↔ ready-made product experience ↔ end-user product
- agent product ↔ AI agent product ↔ user-facing agent application
- model ecosystem ↔ provider ecosystem ↔ model-and-services ecosystem
- multi-provider ↔ cross-provider ↔ provider-agnostic（provider-agnostic 的严格含义更强）
- OpenAI-native ↔ OpenAI-centered ↔ OpenAI provider-native
- Google-native ↔ Google-centered ↔ Google provider-native
- code-level control ↔ programmatic control ↔ fine-grained code control
- multi-agent patterns ↔ multi-agent design patterns ↔ collaboration patterns
- provider-native integration ↔ native provider integration ↔ provider-aligned integration
- typical fit ↔ common use case ↔ intended use ↔ best-fit scenario
- quick comparison ↔ comparison table ↔ framework comparison
- maintainability ↔ ease of maintenance ↔ long-term maintainability
- coordination ↔ orchestration ↔ collaboration management（具体语境下不完全同义）
- framework layer ↔ orchestration layer ↔ development layer（层级含义可能不同）
- framework vs model ↔ framework-versus-model distinction
- framework vs agent product ↔ framework-versus-product distinction
- framework vs workflow platform ↔ framework-versus-platform distinction
- LangGraph ↔ graph/state framework（描述性别名，不是官方别名）
- LangChain ↔ general agent tooling framework（描述性别名，不是官方别名）

## Do Not Confuse Candidates

- **Framework vs model**：模型提供推理和生成能力；框架组织模型、工具、状态和工作流来构建系统。
- **Framework vs AI application**：框架是开发者用来搭系统的层；AI application 是最终实现出来的具体应用。
- **Framework vs agent system**：框架是构建系统的工具和结构；agent system 是模型、工具、状态和逻辑组合后的完整系统。
- **Framework vs agent product**：框架面向开发者；agent product 是用户可以直接使用的成品体验。
- **Framework vs workflow platform**：框架通常是代码优先的开发层；工作流平台常以可视化或低代码编排为主。
- **Framework vs SDK**：二者都可以帮助开发，但 SDK 往往更贴近某个提供商或服务；framework 通常提供更广的系统组织结构。
- **Framework vs library**：库通常由应用主动调用；框架可能规定应用的组织方式和控制流程。
- **Framework vs platform**：框架通常嵌入应用代码；平台可能提供可视化界面、托管运行时和更完整的运营能力。
- **Model vs provider**：模型是可调用的 AI 能力；provider 是提供模型和相关服务的组织或生态。
- **Model vs product**：模型是能力组件；产品还可能包括界面、数据、工具、规则和运营。
- **Agent vs agent product**：agent 是能够围绕目标行动的系统角色；agent product 是包装给用户使用的完整产品。
- **Tool vs model**：工具是外部能力；模型负责推理或生成，通常需要通过调用工具完成外部操作。
- **Tool call vs tool result**：tool call 是发起调用的请求；tool result 是工具返回的信息。
- **State vs memory**：state 通常描述当前工作流状态；memory 更强调保留后供未来使用的信息。
- **State vs context**：state 是系统进度或条件；context 是当前提供给模型理解任务的信息集合，二者可能重叠但不相同。
- **Agent loop vs workflow**：agent loop 是反复观察、判断和行动的控制循环；workflow 是按步骤组织的一组工作流程。
- **Orchestration vs automation**：orchestration 强调协调多个组件；automation 可以只按固定规则自动执行。
- **Routing vs handoff**：routing 可以把请求送到模型、工具或智能体；handoff 特指把任务或对话交给另一个智能体。
- **Handoff vs delegation**：handoff 常表示执行权或对话继续交给另一方；delegation 可以只是委派一个子任务。
- **Retry vs fallback**：retry 再试同一个操作；fallback 改走备用模型、工具或流程。
- **Multi-agent vs multiple tools**：多智能体是多个能判断和行动的 agent；多个工具只是多个外部能力。
- **Multi-agent vs agent team**：multi-agent 是广义架构；agent team 更强调角色分工和协作关系。
- **Role vs capability**：role 是智能体承担的职责；capability 是它能执行的能力。
- **Specialized agent vs model specialization**：specialized agent 是应用层的职责划分；模型专业化可能来自训练或配置。
- **Graph orchestration vs visual workflow**：图编排是代码或数据结构上的组织方式；可视化工作流是通过图形界面编辑流程，二者可以重叠但不等同。
- **Code-first vs low-code**：code-first 主要依靠代码控制；low-code 通过预制组件和少量代码搭建。
- **Provider-native vs multi-provider**：provider-native 偏向某个提供商；multi-provider 强调可连接多个提供商。
- **OpenAI Agents SDK vs OpenAI model**：Agents SDK 是开发工具；OpenAI 模型是被工具调用的模型能力。
- **Google ADK vs Google model**：ADK 是智能体开发套件；Google model 是套件可围绕其构建的模型能力。
- **LangGraph vs LangChain**：LangGraph 强调图和状态编排；LangChain 更偏通用、可组合的 agent tooling；两者有关联但用途侧重点不同。
- **LangGraph vs Codex**：LangGraph 是开发框架；Codex 在页面中作为可直接使用的 agent product 示例。
- **AutoGen vs Manus**：AutoGen 是多智能体编排框架；Manus 在页面中作为 agent product 示例。
- **CrewAI vs role-based workflow**：CrewAI 是具体框架名称；role-based workflow 是一种设计模式，可以在其他框架中实现。
- **Semantic Kernel vs enterprise application**：Semantic Kernel 是集成 AI 的工具；enterprise application 是被集成的现有业务软件。
- **Framework style vs typical fit**：style 描述框架怎么组织能力；typical fit 描述它通常适合什么场景。
- **Framework category vs framework name**：category 是图／状态、多智能体等类别；LangGraph、AutoGen 等是具体名称。
- **General agent tooling vs provider SDK**：通用工具面向多种组件和提供商；provider SDK 更靠近单一提供商生态。
- **Multi-provider vs provider-neutral**：支持多个提供商不一定意味着完全不依赖某个提供商。
- **Visual workflow vs visual product**：可视化工作流是开发方式；可视化产品是用户界面或产品体验。
- **Workflow platform vs workflow**：平台是搭建和运行工作流的工具；workflow 是被搭建出来的步骤序列。
- **Code-level control vs code-only**：有代码级控制不代表系统完全没有界面或预制功能。
- **Long-running workflow vs infinite loop**：长时间运行流程需要持续执行或恢复能力，不等同于没有终点的无限循环。
- **Possible vs Supported vs Core focus**：比较表中的 Possible 表示可以实现，Supported 表示已有支持，Core focus 表示是框架核心方向。
- **Framework is not the model**：页面最重要的边界判断；看到 LangGraph、Agents SDK 等名称时，不应把它们当作 Claude、GPT 或 Gemini 这样的模型。

## Notes

- 本文件是 Module 15 · Agent Development 下 Agent Frameworks 主题的 raw glossary 收集稿，目标是最大化保留候选，不做去重、归并或最终取舍。
- 已完整阅读 `agent-frameworks.html` 的正文内容，包括 lede、页面导航、所有卡片、框架网格、分类网格、对比区域、选择清单、比较表和 Remember this 总结。
- 页面主线心智模型是：MODEL + INSTRUCTIONS + TOOLS + STATE / MEMORY + AGENT LOGIC → AGENT FRAMEWORK → AI APPLICATION。
- 页面最核心的边界表述是：框架帮助开发者构建系统，框架不是模型；框架负责组织模型、工具、状态和工作流。
- “Without a framework”区域明确列出 tool calls、state and agent loops、routing and retries、multi-agent logic，均保留为流程机制候选。
- 主要框架候选按页面出现顺序保留：LangGraph、LangChain、OpenAI Agents SDK、Google ADK、AutoGen、CrewAI、Semantic Kernel。
- 框架提供方和上下文标签也被保留：LangChain、OpenAI、Google、Microsoft、CrewAI，以及 OpenAI-native、Google-native、Multi-provider。
- 页面给出的框架类别是 graph / state orchestration、SDK / provider-native、multi-agent、general agent tooling；页面明确说 categories overlap。
- 页面中的对比边界包括 framework vs model、framework vs agent product、framework vs workflow platform；实例包括 Claude / GPT / Gemini、Codex、Manus、n8n、Dify。
- 页面中的选择判断包括 code-level control、multi-agent patterns、provider-native integration、visual workflow；visual workflow 指向 Module 16。
- 快速比较表的字段保留为候选：Framework、Style、Code-first、Multi-agent support、Provider relationship、Typical fit。
- 比较表中的值也作为候选保留，包括 Graph / state、General tooling、Provider SDK、Multi-agent、Role-based、Enterprise tooling、Yes、Possible、Handoffs、Supported、Core focus、OpenAI-native、Google-native、Multi-provider。
- 本 raw 文件有意保留同一术语在标题、正文、示例、标签和表格中重复出现的版本；后续整理阶段再决定是否合并。
- “Google ADK”的完整展开名并未在页面正文写出；`agent development kit` 作为可能的外部展开名，仅放在候选和 aliases 中，不应视为页面明示内容。
- Claude、GPT、Gemini、Codex、Manus、n8n、Dify 是页面用于区分模型、产品和工作流平台的示例名称，不等同于框架概念本身。
- Framework、SDK、tooling、platform、product、model、provider 是页面需要反复区分的层级词，后续编辑时应避免把它们合并为一个“工具”概念。
- 适用性并非绝对结论：页面用 typical fit 描述常见匹配，并明确不同类别之间存在重叠。
- 本文件未修改网站文件、脚本、CSS、GitHub 或其他非目标内容。
