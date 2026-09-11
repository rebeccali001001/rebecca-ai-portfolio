# Topic

How Are AI Agents Built?

Module/Topic/Source File

- Module: 15 · Agent Development
- Topic: How Are AI Agents Built?
- Source File: `how-agents-are-built.html`
- Source page title: `How Are AI Agents Built?`
- Page family / navigation label: `Agent Development`

## Glossary Candidates

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| How Are AI Agents Built? | AI 智能体是如何构建的？ | The question of how models, instructions, tools, state, and loops become an agent system. | 研究模型、指令、工具、状态和循环怎样组合成智能体系统。 |
| AI agent | AI 智能体 | A system that combines model intelligence with instructions, tools, state, and an execution loop. | 把模型能力、规则、工具、状态和执行循环组合起来完成目标的系统。 |
| agent | 智能体；代理 | A system that can work toward a goal by deciding and taking steps. | 能围绕目标做判断并采取步骤的系统。 |
| agent system | 智能体系统 | A complete system that uses model capability inside an action loop. | 把模型能力放进执行循环中、能够行动的完整系统。 |
| AI agent system | AI 智能体系统 | An AI system composed of a model, instructions, tools, state, and a loop. | 由模型、指令、工具、状态和循环组成的 AI 系统。 |
| system | 系统 | A set of connected parts that work together for an outcome. | 多个相互连接、共同产生结果的部分。 |
| model | 模型 | The component that generates or reasons about a useful next step. | 负责生成内容或判断下一步怎么做的 AI 部件。 |
| AI model | AI 模型 | A model that provides generation or reasoning capability. | 提供生成或推理能力的模型。 |
| model intelligence | 模型智能 | The useful generation and reasoning ability supplied by a model. | 模型提供的生成、分析和判断能力。 |
| model capability | 模型能力 | The capability an agent system obtains from its model. | 智能体系统从模型那里获得的能力。 |
| capability | 能力 | Something a system can do. | 系统能够完成的一种事情。 |
| reasoning | 推理 | Working through information to decide or produce an answer. | 根据已有信息分析并得出判断或答案。 |
| reasoning capability | 推理能力 | The ability to analyze information and choose a useful next step. | 分析信息并选择有用下一步的能力。 |
| generation | 生成 | Producing text or another output. | 产生文字或其他输出。 |
| generation capability | 生成能力 | The ability to produce new output. | 产生新的文字或其他结果的能力。 |
| next useful step | 下一步有用行动 | The next action or decision that helps move a task forward. | 能让任务继续推进的下一步动作或判断。 |
| instructions | 指令 | Guidance that tells the model or system what to do. | 告诉模型或系统应该做什么的说明。 |
| instruction | 指令 | One piece of guidance for the system. | 给系统的一条具体要求。 |
| system prompt | 系统提示词 | Instructions that set the role, rules, context, and boundaries. | 规定系统角色、规则、上下文和边界的提示词。 |
| instructions / system prompt | 指令／系统提示词 | The directing layer that guides agent behavior. | 负责引导智能体行为的规则层。 |
| role | 角色 | The function or identity assigned to an agent or system. | 给智能体或系统安排的身份和职责。 |
| rules | 规则 | Requirements that constrain how the system behaves. | 限制系统应该怎样行动的要求。 |
| context | 上下文 | Information supplied so the model can understand the task. | 帮模型理解任务背景的信息。 |
| boundaries | 边界 | Limits describing what the system should or should not do. | 规定系统能做什么、不能做什么的范围。 |
| tool | 工具 | An external capability that an agent can call to act in the world. | 智能体可以调用、用来影响外部世界的能力。 |
| tools | 工具 | Approved external capabilities available to the agent system. | 智能体系统可以使用的一组经过批准的外部能力。 |
| approved tool | 已批准工具 | A tool that the system is allowed to call. | 系统被允许调用的工具。 |
| approved action | 已批准行动 | An action that the system is permitted to take. | 系统获准执行的动作。 |
| external capability | 外部能力 | A capability provided outside the model itself. | 不是模型本身、由外部系统提供的能力。 |
| external action | 外部行动 | An action that changes or queries something outside the agent. | 查询或改变智能体外部事物的动作。 |
| action | 行动；动作 | A step taken by an agent or a tool. | 智能体或工具实际执行的一步。 |
| act | 行动 | The building-block function of taking an approved action. | 构建块中“真正做事情”的部分。 |
| tool call | 工具调用 | A request from the agent system to run a tool. | 智能体系统发给工具、要求它执行操作的请求。 |
| tool calls | 工具调用（复数） | Multiple requests to external tools during a task. | 一个任务中对外部工具发起的多次请求。 |
| get_order("123") | get_order("123") 订单查询调用 | An example tool call that retrieves order 123. | 一个调用工具查询 123 号订单的例子。 |
| API | API；应用程序接口 | A structured interface through which software can request capabilities. | 软件按约定方式请求外部功能的接口。 |
| API / MCP | API／MCP | Structured bridges from an agent system to external capabilities. | 把智能体系统连接到外部能力的结构化桥梁。 |
| MCP | MCP；模型上下文协议 | A structured bridge for connecting an agent or model to external capabilities. | 用标准化方式把模型或智能体接到外部能力的协议。 |
| API bridge | API 桥接 | A connection that exposes an external capability through an API. | 通过 API 把外部能力接进来的连接层。 |
| MCP bridge | MCP 桥接 | A structured MCP connection to an external capability. | 通过 MCP 接入外部能力的结构化连接。 |
| structured bridge | 结构化桥梁 | A defined interface between the agent system and outside capabilities. | 在智能体系统与外部能力之间按固定格式连接的接口。 |
| state | 状态 | Information about the current condition or progress of a task. | 表示任务当前情况或进度的信息。 |
| state / memory | 状态／记忆 | Current task information plus retained information used by the system. | 当前任务信息和以后仍可使用的保留信息。 |
| memory | 记忆 | Information retained for later use. | 保存下来、之后还可以使用的信息。 |
| task context | 任务上下文 | Contextual information needed to work on the current task. | 完成当前任务时需要知道的背景信息。 |
| task history | 任务历史 | Earlier events, actions, or messages in a task. | 任务之前发生过的事件、动作或消息。 |
| useful information | 有用信息 | Information worth keeping or using for the task. | 对任务有帮助、值得保存或使用的信息。 |
| current state | 当前状态 | The system's condition at the present point in execution. | 系统执行到当前时刻所处的情况。 |
| state update | 状态更新 | Changing stored task information after an observation or action. | 观察或行动后修改保存的任务信息。 |
| update state | 更新状态 | Record what happened so the next step has current information. | 记录刚发生的事情，让下一步知道最新情况。 |
| execution loop | 执行循环 | A repeating cycle that lets the agent observe, decide, act, and update state. | 让智能体反复观察、判断、行动和更新状态的循环。 |
| agent loop | 智能体循环 | The repeated control cycle used to work toward a goal. | 智能体围绕目标不断处理任务的一轮轮循环。 |
| action loop | 行动循环 | A loop in which the system chooses and performs actions. | 系统不断选择并执行动作的循环。 |
| loop | 循环 | A repeated sequence of processing steps. | 反复执行的一组步骤。 |
| cycle | 周期；循环轮次 | One pass through the loop. | 循环完整走过一遍。 |
| goal | 目标 | The result the user or agent system is trying to achieve. | 用户或智能体系统想要达成的结果。 |
| user goal | 用户目标 | The outcome requested by the user. | 用户希望系统完成的事情。 |
| result | 结果 | The outcome produced after the system works on a goal. | 系统处理目标后产生的成果。 |
| observe | 观察 | Read the current task situation or an external result. | 查看当前任务情况或外部系统返回的信息。 |
| observation | 观察结果 | Information received while the agent is working. | 智能体处理任务时收到的信息。 |
| plan | 计划 | A proposed sequence or approach for reaching a goal. | 为达到目标而拟定的步骤或方法。 |
| planning | 规划 | The process of deciding how to reach a goal. | 思考怎样完成目标的过程。 |
| decide | 决策 | Choose what the agent should do next. | 选择智能体下一步应该做什么。 |
| decision | 决定 | The selected next step or course of action. | 被选中的下一步或行动方向。 |
| plan / decide | 规划／决策 | The loop stage where the system determines the next step. | 循环中决定下一步方案的阶段。 |
| act | 行动 | Execute the chosen approved step. | 执行已经选定并获准的步骤。 |
| observe result | 观察结果 | Inspect what happened after an action. | 查看动作执行后发生了什么。 |
| update state | 更新状态 | Store the new situation before continuing the loop. | 在继续循环前保存最新情况。 |
| goal completed | 目标完成 | A stop outcome in which the requested goal has been achieved. | 任务已经达成、循环可以停止的情况。 |
| completed goal | 已完成目标 | A goal that no longer needs more agent steps. | 不需要智能体继续处理的目标。 |
| blocked | 受阻 | A stop outcome in which the system cannot continue. | 系统无法继续推进任务的情况。 |
| approval required | 需要批准 | A stop or pause outcome requiring a person to review an action. | 需要人先检查或同意才能继续的情况。 |
| failure | 失败 | An unsuccessful execution outcome. | 一次执行没有成功的结果。 |
| stop condition | 停止条件 | A condition that ends or pauses the agent loop. | 达到后让智能体循环结束或暂停的条件。 |
| failure / stop condition | 失败／停止条件 | Failure or another defined condition that ends the loop. | 失败或其他预先规定的结束循环条件。 |
| stop | 停止 | End further automatic action. | 不再继续自动执行动作。 |
| pause | 暂停 | Temporarily halt the loop until a condition or person responds. | 暂时停住循环，等条件满足或人回应。 |
| loop continuation | 循环继续 | Continuing the cycle until a stopping condition is reached. | 在到达停止条件前继续重复处理。 |
| control | 控制 | The layer that limits, observes, and can stop system actions. | 限制、监控并能停止系统行动的控制层。 |
| permissions | 权限 | Rules describing what the system is allowed to access or do. | 规定系统能访问什么、能做什么的许可。 |
| permission | 权限 | Authorization for a particular access or action. | 对某项访问或动作的授权。 |
| limits | 限制 | Boundaries on what or how much the system can do. | 对系统可以做什么或做多少的约束。 |
| logs | 日志 | Records of system events, calls, and actions. | 记录系统事件、调用和动作的记录。 |
| logging | 日志记录 | The practice of recording execution details. | 把执行过程细节记录下来的做法。 |
| human approval | 人工批准 | A person reviews or confirms a sensitive action. | 人检查或确认敏感动作后，系统才继续。 |
| human review | 人工审核 | A person examines a proposed result or action. | 人检查系统提出的结果或动作。 |
| review | 审核；检查 | Examine an action before it is carried out. | 在动作执行前检查它是否合适。 |
| confirm | 确认 | Explicitly approve a proposed action. | 明确表示同意某个待执行动作。 |
| sensitive action | 敏感行动 | An action important or risky enough to need human review. | 因为重要或有风险而需要人检查的动作。 |
| automatic action | 自动行动 | An action the system can perform without a person reviewing it first. | 不必先经过人工检查就能执行的动作。 |
| approved action versus sensitive action | 已批准行动与敏感行动 | An approved action is allowed; a sensitive action may still require review. | “允许做”不代表“可以不经人检查就做”。 |
| external systems | 外部系统 | Systems outside the agent that provide data or actions. | 智能体之外、提供数据或执行动作的系统。 |
| browser | 浏览器 | An external environment an agent may use as a tool. | 智能体可能通过工具操作的网页环境。 |
| database | 数据库 | A system that stores structured information an agent may query. | 保存结构化信息、智能体可以查询的系统。 |
| files | 文件 | Stored documents or data an agent may read or change. | 智能体可能读取或修改的文档或数据。 |
| business apps | 业务应用 | External applications used to perform organizational work. | 用来完成业务工作的外部应用。 |
| business system | 业务系统 | A system containing business data or operations. | 保存业务数据或执行业务操作的系统。 |
| world | 外部世界 | The real or software environment affected by agent actions. | 智能体动作会查询或改变的现实／软件环境。 |
| building block | 构建块 | A component used to assemble a larger system. | 用来拼装更大系统的一个小部件。 |
| core building block | 核心构建块 | One of the fundamental pieces of an agent system. | 智能体系统不可缺少的基础部件。 |
| six pieces | 六个部分 | Model, instructions, tools, state / memory, API / MCP, and control. | 页面用六个部分解释智能体是怎么组成的。 |
| think | 思考 | The label for model generation and reasoning. | 页面用来表示模型进行生成和推理的动作标签。 |
| direct | 引导 | The label for instructions and system prompt. | 页面用来表示指令引导系统行为的动作标签。 |
| remember | 记住 | The label for state and memory. | 页面用来表示系统保存任务信息的动作标签。 |
| connect | 连接 | The label for API and MCP bridges. | 页面用来表示系统接通外部能力的动作标签。 |
| control | 控制 | The label for permissions and human approval. | 页面用来表示权限与人工批准的动作标签。 |
| model component | 模型组件 | The model part of the agent architecture. | 智能体架构中提供智能能力的模型部分。 |
| instruction component | 指令组件 | The part that sets role, rules, context, and boundaries. | 负责规定角色、规则、上下文和边界的部分。 |
| tool component | 工具组件 | The part that exposes approved external actions. | 把获准的外部动作提供给系统调用的部分。 |
| state component | 状态组件 | The part that tracks current task information. | 跟踪任务当前信息的部分。 |
| memory component | 记忆组件 | The part that retains useful information. | 保存有用信息、供之后使用的部分。 |
| API component | API 组件 | The interface part connecting the agent to an external capability. | 把智能体连接到外部能力的接口部分。 |
| MCP component | MCP 组件 | The protocol-based connection part for external capabilities. | 用协议连接外部能力的部分。 |
| control component | 控制组件 | The part implementing permissions, limits, logs, and approvals. | 实施权限、限制、日志和批准机制的部分。 |
| architecture | 架构 | The arrangement of components and connections in a system. | 系统各部件及其连接方式的整体结构。 |
| main architecture | 主架构 | The page's model of moving from a user goal to a result. | 页面展示从用户目标走向结果的系统结构。 |
| architecture stack | 架构堆栈 | The vertical sequence from goal through system and external systems to result. | 从目标经过系统和外部系统到结果的纵向流程。 |
| architecture node | 架构节点 | A labeled component or stage in the architecture diagram. | 架构图中代表部件或阶段的节点。 |
| system boundary | 系统边界 | The distinction between the agent system and external systems. | 区分智能体内部与外部系统的边界。 |
| user goal to result | 从用户目标到结果 | The end-to-end path through which an agent handles a request. | 智能体把用户请求处理成结果的完整路径。 |
| user goal → agent system → tools / MCP / APIs → external systems → result | 用户目标→智能体系统→工具／MCP／API→外部系统→结果 | The page's high-level architecture flow. | 页面展示的从目标到结果的总流程。 |
| approved actions the system can call | 系统可调用的已批准动作 | Actions exposed through tools, MCP, or APIs. | 通过工具、MCP 或 API 提供给系统的获准动作。 |
| review or confirm sensitive actions | 审核或确认敏感行动 | Human control applied before a sensitive action proceeds. | 敏感动作继续前由人检查或同意。 |
| permissions, limits, logs, and stop conditions | 权限、限制、日志和停止条件 | Control mechanisms around agent execution. | 围绕智能体执行设置的一组控制机制。 |
| task | 任务 | Work that the agent system is asked to complete. | 用户交给智能体系统完成的一件工作。 |
| task completion | 任务完成 | Reaching the requested outcome. | 达到用户要求的结果。 |
| task context and history | 任务上下文与历史 | Current background plus earlier task information. | 当前背景和之前发生过的任务信息。 |
| useful information retention | 有用信息保留 | Keeping information for a later step or interaction. | 把以后还可能用到的信息保存下来。 |
| dynamic decision | 动态决策 | Choosing the next step based on the current situation. | 根据当前情况临时决定下一步。 |
| predefined step | 预定义步骤 | A step specified before execution begins. | 在运行前就规定好的步骤。 |
| dynamic | 动态的 | Able to change the next step according to observations. | 会根据观察结果改变下一步。 |
| predefined | 预定义的 | Set in advance rather than selected at runtime. | 提前设定、运行时不临时决定的。 |
| agent versus workflow | 智能体与工作流 | A distinction between dynamic agent decisions and predefined workflow steps. | 区分智能体的动态判断和工作流的预设步骤。 |
| agent | 智能体 | A system that can dynamically decide the next steps. | 能动态判断下一步怎么做的系统。 |
| workflow | 工作流 | A sequence of steps often defined in advance. | 通常提前规定好的一串工作步骤。 |
| predefined workflow | 预定义工作流 | A workflow whose steps are specified before running. | 运行前就设定好步骤的工作流。 |
| dynamic workflow | 动态工作流 | A workflow whose next step can vary during execution. | 执行过程中下一步可能变化的工作流。 |
| combined system | 组合系统 | A real system that uses both agents and workflows. | 同时使用智能体和工作流的实际系统。 |
| real systems can combine both | 真实系统可以二者结合 | Agents and predefined workflows can coexist in one product. | 一个产品里可以同时有动态智能体和固定工作流。 |
| single agent + tools | 单智能体＋工具 | One agent uses a set of tools to complete a task. | 一个智能体调用一组工具完成任务。 |
| single agent | 单智能体 | An architecture with one primary agent. | 主要由一个智能体负责处理的架构。 |
| agent + tools | 智能体＋工具 | An agent architecture in which external actions are available. | 智能体可以调用外部动作的组合。 |
| agent + RAG | 智能体＋RAG | An agent retrieves relevant knowledge before acting. | 智能体先检索相关知识，再决定行动。 |
| RAG | RAG；检索增强生成 | Retrieval-augmented generation that supplies relevant information before generation or action. | 先查找相关资料，再让模型生成或行动的方法。 |
| retrieve | 检索 | Find relevant information for the current task. | 为当前任务找出相关信息。 |
| relevant knowledge | 相关知识 | Information useful for making the next decision. | 对下一步判断有帮助的知识。 |
| retrieve before acting | 行动前检索 | Look up relevant knowledge before taking an action. | 做动作前先查资料。 |
| agent + human approval | 智能体＋人工批准 | The agent proposes actions while a person controls sensitive steps. | 智能体提出动作，人控制敏感步骤。 |
| propose an action | 提出行动建议 | Suggest an action without necessarily executing it immediately. | 先建议要做什么，不一定马上执行。 |
| person controls sensitive steps | 人控制敏感步骤 | A human retains authority over risky or important actions. | 重要或有风险的步骤仍由人掌握决定权。 |
| multi-agent | 多智能体 | An architecture in which several agents coordinate on a task. | 多个智能体一起协调完成任务的架构。 |
| multi-agent system | 多智能体系统 | A system composed of several cooperating agents. | 由多个协作智能体组成的系统。 |
| specialized agent | 专业化智能体 | An agent responsible for a narrower part of a larger task. | 专门负责大任务中某一小部分工作的智能体。 |
| specialized agents | 专业化智能体（复数） | Several agents with different responsibilities. | 分别负责不同工作的多个智能体。 |
| coordinate | 协调 | Arrange agents or actions so they work together. | 让多个智能体或动作互相配合。 |
| coordination | 协调 | The process of making components cooperate. | 让不同部件配合工作的过程。 |
| larger task | 更大任务 | A task that can be divided among several specialized agents. | 可以拆给多个专业智能体处理的复杂任务。 |
| agent collaboration | 智能体协作 | Several agents working together toward one outcome. | 多个智能体共同完成一个结果。 |
| agent team | 智能体团队 | A group of agents cooperating on a task. | 一组共同处理任务的智能体。 |
| common agent pattern | 常见智能体模式 | A recurring architecture for combining agents with capabilities or control. | 反复出现的智能体系统组织方式。 |
| agent pattern | 智能体模式 | A recognizable way to structure an agent system. | 组织智能体系统的一种典型方法。 |
| framework | 框架 | Software that helps developers assemble and manage agent-system pieces. | 帮开发者组装和管理智能体各部分的软件结构。 |
| agent framework | 智能体框架 | A framework for assembling models, tools, state, and loops. | 用来组装模型、工具、状态和循环的框架。 |
| framework layer | 框架层 | The development layer that organizes agent-system components. | 负责组织智能体部件的开发层。 |
| building blocks | 构建块（复数） | The model, tools, state, and loop that a framework assembles. | 框架用来组装的模型、工具、状态和循环等部件。 |
| framework assembly | 框架组装 | Combining the pieces into a functioning agent system. | 把各个部件组合成可运行的智能体系统。 |
| assemble | 组装 | Combine parts into a working system. | 把多个部分合成一个能工作的系统。 |
| manage | 管理 | Operate, coordinate, and control system pieces. | 运行、协调和控制系统各个部分。 |
| orchestration | 编排；协调 | Organizing how models, tools, state, and loops work together. | 统筹模型、工具、状态和循环如何配合。 |
| reusable pattern | 可复用模式 | A design approach that can be used across systems. | 可以在不同系统中重复采用的设计方式。 |
| reusable building block | 可复用构建块 | A component that can be reused in multiple applications. | 可以在多个应用中重复使用的软件部件。 |
| application | 应用 | A concrete software experience built from system components. | 用这些系统部件做成的具体软件。 |
| AI application | AI 应用 | An application that uses AI capabilities to provide a useful experience. | 使用 AI 能力为人提供实际体验的软件。 |
| agent application | 智能体应用 | An application built around an agent system. | 以智能体系统为核心的应用。 |
| useful experience | 有用体验 | A result or interface that helps people accomplish something. | 能帮助人完成事情的实际体验。 |
| people | 人们；用户 | The people who use or benefit from the application. | 使用应用或从应用结果中受益的人。 |
| framework to application | 从框架到应用 | The path from reusable development pieces to a user-facing experience. | 从开发用的可复用部件到用户体验的过程。 |
| building blocks → framework → application | 构建块→框架→应用 | The page's concise relationship between system parts, development layer, and product experience. | 页面总结的“基础部件—框架—应用”层级关系。 |
| agent system equation | 智能体系统公式 | Model + Tools + State + Loop = Agent System. | 模型加工具、状态和循环，就组成智能体系统。 |
| Model + Tools + State + Loop = Agent System | 模型＋工具＋状态＋循环＝智能体系统 | A compact formula summarizing the architecture. | 用一句公式概括智能体系统的关键组成。 |
| capability versus system | 能力与系统 | The distinction between what a model can do and the system built around it. | 区分模型能提供的能力和围绕模型搭出的系统。 |
| model versus agent | 模型与智能体 | A model generates and reasons; an agent system uses that capability in an action loop. | 模型负责生成和推理，智能体把能力放进循环中行动。 |
| model versus agent system | 模型与智能体系统 | A comparison of a model component with the complete action-oriented system. | 比较单独的模型部件和完整的行动系统。 |
| framework versus model | 框架与模型 | A framework organizes a system; a model supplies AI capability. | 框架负责搭系统，模型负责提供 AI 能力。 |
| agent system versus model | 智能体系统与模型 | The system has tools, state, and a loop in addition to the model. | 智能体系统除了模型，还包括工具、状态和循环。 |
| action-oriented system | 面向行动的系统 | A system designed to take steps toward a goal. | 会围绕目标实际采取步骤的系统。 |
| framework versus workflow | 框架与工作流 | A framework assembles components; a workflow organizes task steps. | 框架负责组装系统，工作流负责组织任务步骤。 |
| agent versus workflow | 智能体与工作流 | An agent can dynamically decide; a workflow often follows predefined steps. | 智能体可动态判断，工作流通常按预设步骤走。 |
| framework versus application | 框架与应用 | A framework is a development structure; an application is the built experience. | 框架是开发结构，应用是做出来给人使用的软件。 |
| framework versus agent product | 框架与智能体产品 | A framework is for building; an agent product is a ready-to-use experience. | 框架给开发者搭建系统，智能体产品给用户直接使用。 |
| framework versus workflow platform | 框架与工作流平台 | A framework organizes code and components; a platform may provide workflow-building capabilities. | 框架偏开发层，工作流平台偏设计和运行工作流。 |
| dynamic versus predefined | 动态与预定义 | A contrast between runtime decisions and steps set in advance. | 区分运行时临时判断和提前写好的步骤。 |
| model generates and reasons | 模型生成并推理 | The model's core contribution in the comparison. | 页面用来概括模型核心作用的表述。 |
| agent uses model capability inside an action loop | 智能体在行动循环中使用模型能力 | The system-level role of the model. | 智能体把模型能力放进循环，持续观察和行动。 |
| action loop toward a goal | 朝目标前进的行动循环 | Repeatedly observe, decide, act, and update until the goal or stop condition. | 反复观察、判断、行动、更新，直到完成或停止。 |
| check order 123 and draft an update email | 查询 123 号订单并起草更新邮件 | The page's end-to-end example task. | 页面用来说明智能体工作过程的示例任务。 |
| order ID | 订单编号 | The identifier the agent reads before querying an order. | 智能体先读取、再用来查询订单的编号。 |
| order status | 订单状态 | The status returned by the order system. | 订单系统返回的订单当前状态。 |
| system returns status | 系统返回状态 | The external system provides the result of the order query. | 外部系统把订单查询结果返回给智能体。 |
| draft email | 起草邮件 | Produce an email draft based on the retrieved status. | 根据查到的状态写出邮件草稿。 |
| update email | 更新邮件 | An email communicating the latest order information. | 告知最新订单信息的邮件。 |
| send if approved | 获准后发送 | Send the drafted email only after human approval. | 人批准后才真正发送邮件。 |
| human reviews → send if approved | 人工审核→获准后发送 | The example's human-controlled final action. | 示例中最后由人审核，批准后才发送。 |
| example flow | 示例流程 | The ordered sequence used to illustrate agent execution. | 页面用来解释智能体执行过程的一串步骤。 |
| user goal step | 用户目标步骤 | The first step in the example flow. | 示例流程中先明确用户想完成什么。 |
| read order ID | 读取订单编号 | The agent extracts the identifier needed for the tool call. | 智能体找出调用查询工具所需的编号。 |
| call external tool | 调用外部工具 | Use a tool to retrieve or change outside information. | 用工具查询或改变外部信息。 |
| return value | 返回值 | Information returned by a tool or external system. | 工具或外部系统返回的信息。 |
| agent drafts | 智能体起草 | The agent produces a draft rather than immediately sending it. | 智能体先写草稿，不直接发送。 |
| final action | 最终动作 | The action that completes the example after approval. | 经过批准后完成示例任务的最后一步。 |
| acceptance check | 验收检查 | A check of whether the page's core ideas can be explained. | 检查是否掌握页面核心概念的验收项。 |
| page pass / fail | 页面通过／不通过 | The page's acceptance status condition. | 页面用来表示学习验收是否通过的条件。 |
| explain what an agent is made of | 解释智能体由什么组成 | Explain model, instructions, tools, state, loop, and control. | 能说清智能体由哪些部分组成。 |
| tools / state / MCP | 工具／状态／MCP | A compact acceptance-check grouping of important agent mechanisms. | 验收中要求掌握的工具、状态和 MCP。 |
| important boundary | 重要边界 | A distinction needed to avoid treating a model, framework, workflow, or product as the same thing. | 防止把模型、框架、工作流和产品混为一谈的关键区分。 |
| system composition | 系统组合 | The way multiple components combine into an agent. | 多个部件组合成智能体的方式。 |
| component | 部件；组件 | One part of a larger system. | 更大系统中的一个组成部分。 |
| integration | 集成 | Connecting an agent to tools or external systems. | 把智能体和工具、外部系统连接起来。 |
| execution | 执行 | Running a planned or selected action. | 真正运行某个计划或动作。 |
| runtime | 运行时 | The period when the agent system is actively executing. | 智能体系统实际运行和做决定的阶段。 |
| action selection | 动作选择 | Choosing which approved action to take next. | 从可用动作中选下一步做什么。 |
| action result | 动作结果 | What an external action produced. | 外部动作执行后产生的结果。 |
| progress | 进度 | How far the system has moved toward the goal. | 任务距离完成还有多远。 |
| task status | 任务状态 | The current condition such as active, blocked, or completed. | 任务当前是进行中、受阻还是已完成等情况。 |
| completion status | 完成状态 | Whether the goal has been completed. | 目标是否已经完成的状态。 |
| blocked status | 受阻状态 | A status showing the system cannot continue. | 表示系统无法继续推进的状态。 |
| approval status | 批准状态 | Whether a required human approval has been received. | 所需人工批准是否已经得到的状态。 |
| failure status | 失败状态 | A status showing that execution did not succeed. | 表示执行没有成功的状态。 |
| control plane | 控制面 | The permission, approval, logging, and stopping controls around execution. | 围绕执行提供权限、审批、记录和停止能力的一层。 |
| safety control | 安全控制 | A control that prevents or pauses unsafe actions. | 防止或暂停不安全动作的控制。 |
| governance | 治理 | Rules and oversight for how the agent operates. | 规定和监督智能体如何运行的机制。 |
| trust boundary | 信任边界 | The boundary between approved agent behavior and outside effects. | 获准的智能体行为与外部影响之间的界线。 |

## Potential Missing Concepts

以下概念与本页主题直接相关，但没有在 `how-agents-are-built.html` 正文中被完整定义或展开；保留它们供后续词汇整理时判断是否需要补充：

- **tool schema / function schema（工具模式／函数模式）**：页面有 `get_order("123")` 的工具调用示例，但没有解释工具参数、返回值和 schema。
- **function calling（函数调用）**：工具调用的常见实现方式，正文只写了 tool call，没有展开底层调用格式。
- **tool result（工具结果）**：示例有“系统返回状态”，但没有把 tool result 作为独立机制定义。
- **observation space（观察空间）**：页面写 observe 和 observe result，但没有说明智能体能看到哪些输入。
- **action space（动作空间）**：页面写 approved actions，但没有定义所有可选动作的集合。
- **planning strategy（规划策略）**：页面有 plan / decide，但没有比较分解、重规划或直接行动等策略。
- **reasoning trace（推理轨迹）**：页面提到 reasoning，但没有讨论是否记录或展示内部推理过程。
- **state machine（状态机）**：state 和 loop 出现，但没有用状态机形式定义状态转换。
- **transition（状态转换）**：流程会在步骤间推进，但正文没有单独定义转换规则。
- **event（事件）**：observe result 和 state update 隐含事件驱动场景，但没有展开事件模型。
- **context window（上下文窗口）**：task context 出现，但没有说明模型可接收上下文的容量限制。
- **short-term memory（短期记忆）**：state / task history 相关，但没有区分短期与长期记忆。
- **long-term memory（长期记忆）**：memory 出现，但没有说明持久化或跨任务记忆。
- **memory retrieval（记忆检索）**：页面写 useful information，但没有说明如何取回记忆。
- **persistent state（持久状态）**：状态更新被提到，但没有说明保存介质或恢复能力。
- **checkpoint（检查点）**：长任务可能需要保存恢复点，但正文没有说明。
- **session（会话）**：task context and history 出现，但没有定义会话边界。
- **identity（身份）**：system prompt 的 role 出现，但没有讨论 agent identity 或用户身份。
- **tool selection（工具选择）**：工具可调用，但没有介绍模型如何从多个工具中选择一个。
- **tool permissions（工具权限）**：permissions 出现，但没有说明按工具、用户或资源授权的粒度。
- **least privilege（最小权限）**：control 和 permissions 出现，但没有提出最小权限原则。
- **sandbox（沙箱）**：浏览器、文件和业务应用属于外部环境，但没有说明隔离执行。
- **confirmation gate（确认闸门）**：human approval 出现，但没有定义批准节点的实现方式。
- **human-in-the-loop（人在回路中）**：页面实际描述了人工审核，但没有使用这个标准术语展开。
- **human-on-the-loop（人在监督回路中）**：control 和 logs 可能支持监督，但正文没有区分监督与逐步批准。
- **guardrail（安全护栏）**：permissions、limits 和 stop conditions 有护栏作用，但未单独定义 guardrail。
- **policy（策略）**：rules 和 boundaries 出现，但没有把策略作为可执行对象讨论。
- **policy enforcement（策略执行）**：control 被提到，但没有说明如何强制执行规则。
- **audit trail（审计轨迹）**：logs 出现，但没有说明审计所需的完整性、查询和保留策略。
- **observability（可观测性）**：logs 出现，但没有讨论 traces、metrics 和运行可见性。
- **trace（追踪记录）**：执行循环适合追踪，但正文没有定义 trace。
- **latency（延迟）**：页面没有性能指标；循环、工具和人工批准可能影响响应时间。
- **cost（成本）**：页面没有讨论模型调用、工具调用或循环次数的成本。
- **token usage（Token 用量）**：context 和 model 出现，但正文没有讨论 Token 消耗。
- **throughput（吞吐量）**：页面没有讨论系统单位时间能处理多少任务。
- **reliability（可靠性）**：failure 和 stop condition 出现，但没有定义长期稳定性。
- **retry（重试）**：失败处理没有展开，因此没有说明哪些失败可以重试。
- **timeout（超时）**：stop condition 可能包括超时，但正文没有命名它。
- **fallback（降级／备用路径）**：blocked 和 failure 出现，但没有说明备用工具或备用流程。
- **error handling（错误处理）**：failure 被列为停止条件，但没有说明错误分类和恢复方式。
- **idempotency（幂等性）**：订单查询和发送邮件示例可能涉及重复执行风险，但页面没有讨论。
- **side effect（副作用）**：发送邮件属于可能改变外部世界的动作，正文未单独定义副作用。
- **dry run（试运行）**：draft email 与 send if approved 暗示预览式流程，但没有介绍 dry run。
- **evaluation（评估）**：acceptance check 是页面学习验收，不是对智能体任务质量的运行评估。
- **success metric（成功指标）**：goal completed 被列出，但没有定义成功率、准确率或任务完成时间。
- **task success rate（任务成功率）**：页面没有数值化智能体是否完成目标。
- **approval rate（批准率）**：human approval 出现，但没有统计批准比例。
- **failure rate（失败率）**：failure 出现，但没有统计失败频率。
- **loop count（循环次数）**：loop 出现，但页面没有把轮数作为指标。
- **tool-call count（工具调用次数）**：tool call 出现，但没有讨论调用次数限制或成本。
- **agent runtime（智能体运行时）**：execution loop 出现，但没有介绍负责执行循环的软件运行时。
- **orchestrator（编排器）**：framework 和 orchestration 出现，但没有明确负责调度的组件名称。
- **controller（控制器）**：control 出现，但没有定义单独的控制器组件。
- **planner（规划器）**：planning 出现，但没有区分规划器和模型。
- **executor（执行器）**：act 出现，但没有定义专门执行动作的组件。
- **router（路由器）**：动态决定下一步可能需要路由，但正文没有展开路由逻辑。
- **workflow engine（工作流引擎）**：workflow 出现，但没有说明运行预定义步骤的引擎。
- **agent runtime state（智能体运行状态）**：state 出现，但没有区分持久状态、临时状态和运行时状态。
- **multi-agent communication（多智能体通信）**：multi-agent 出现，但没有说明智能体如何交换消息。
- **delegation（委派）**：多智能体可以分工，但正文没有用 delegation 解释任务转交。
- **handoff（交接）**：多个智能体可能互相转交，但页面没有展开 handoff 机制。
- **supervisor agent（监督智能体）**：multi-agent coordination 出现，但没有介绍监督者模式。
- **specialist routing（专业智能体路由）**：specialized agents 出现，但没有说明如何选择专业智能体。
- **parallel execution（并行执行）**：multi-agent 可能并行，但正文没有比较串行和并行。
- **sequential execution（串行执行）**：example flow 是串行展示，但没有明确讨论串行执行。
- **subtask（子任务）**：larger task 和 specialized agents 出现，但没有定义子任务边界。
- **workflow automation（工作流自动化）**：workflow 出现，但页面没有展开与智能体的边界。
- **automation（自动化）**：automatic action 出现，但没有定义自动化系统。
- **agent autonomy（智能体自主性）**：dynamic decision 出现，但没有讨论自主程度和限制。
- **bounded autonomy（受限自主性）**：permissions、limits 和 approval 暗示受限自主，但正文没有命名。
- **open-loop system（开环系统）**：agent loop 是闭环式的，但页面没有做控制理论对比。
- **closed-loop system（闭环系统）**：observe、act、observe result、update state 构成闭环，但未单独定义。
- **feedback loop（反馈循环）**：观察结果会更新状态，但正文没有使用 feedback 术语。
- **replanning（重新规划）**：循环可根据结果决定下一步，但没有说明何时重规划。
- **termination（终止）**：stop condition 出现，但没有定义终止处理。
- **human escalation（升级给人工）**：approval required 和 blocked 出现，但没有说明升级路径。
- **access control（访问控制）**：permissions 出现，但没有说明资源访问控制机制。
- **data privacy（数据隐私）**：database、files、business apps 和 memory 出现，但没有讨论数据隐私。
- **prompt injection（提示注入）**：instructions、tools 和外部系统组合可能产生风险，但页面未提及。
- **tool misuse（工具误用）**：approved actions 和 human approval 出现，但没有讨论工具误用。
- **model hallucination（模型幻觉）**：model reasoning 出现，但没有讨论模型错误生成。
- **security（安全）**：control 有安全含义，但正文没有完整安全模型。
- **data grounding（数据扎根）**：RAG 和 relevant knowledge 出现，但没有解释 grounding 的验证边界。
- **deployment（部署）**：页面讲如何构建，但没有说明构建后的上线方式。
- **production environment（生产环境）**：外部系统与业务应用出现，但没有讨论生产运行。
- **scalability（可扩展性）**：multi-agent 和 larger task 出现，但没有说明规模扩展。
- **versioning（版本管理）**：模型、工具和指令都可能变化，但正文没有版本策略。
- **testing（测试）**：acceptance check 不是软件测试，页面没有介绍 agent 测试。
- **simulation（模拟）**：工具和外部系统动作可能需要模拟，但正文未展开。
- **mock tool（模拟工具）**：示例有工具调用，但没有测试替身概念。
- **framework abstraction（框架抽象）**：framework 负责组装部件，但正文未讨论抽象的收益与代价。
- **framework versus platform（框架与平台）**：workflow platform 被隐含对比，但没有完整定义 platform。
- **SDK versus framework（SDK 与框架）**：API / MCP 与 framework 出现，但没有解释 SDK 的层级差异。
- **agent versus agent product（智能体与智能体产品）**：application 和 people 出现，但没有完整区分产品包装层。

## Aliases / Synonyms

- AI agent ↔ agent ↔ intelligent agent（常见英文别名；页面主要使用 AI agent / agent）
- agent system ↔ AI agent system ↔ AI agent architecture
- model ↔ AI model ↔ model capability provider（最后一项是描述性说法）
- model intelligence ↔ model capability ↔ reasoning and generation capability
- reasoning ↔ reasoning capability ↔ model reasoning
- generation ↔ generation capability ↔ content generation
- instructions ↔ instruction ↔ guidance ↔ directives
- system prompt ↔ system instructions ↔ prompt instructions
- role ↔ assigned role ↔ system role
- rules ↔ behavioral rules ↔ operating rules
- context ↔ task context ↔ current context
- boundaries ↔ constraints ↔ operating boundaries
- tool ↔ external tool ↔ callable tool ↔ agent tool
- tools ↔ tool set ↔ available tools ↔ approved tools
- approved action ↔ allowed action ↔ permitted action
- tool call ↔ tool invocation ↔ function call（function call 是常见实现形式，不完全等同）
- API ↔ application programming interface ↔ API interface
- MCP ↔ Model Context Protocol ↔ MCP connection
- API / MCP ↔ structured bridge ↔ external capability bridge
- state ↔ current state ↔ execution state ↔ workflow state
- state update ↔ update state ↔ state transition（transition 不一定等于更新）
- memory ↔ agent memory ↔ retained information
- task history ↔ interaction history ↔ execution history
- execution loop ↔ agent loop ↔ action loop ↔ observe-decide-act loop
- loop ↔ cycle ↔ repeated control cycle
- goal ↔ user goal ↔ task goal ↔ desired outcome
- result ↔ task result ↔ outcome ↔ completed output
- observe ↔ inspect ↔ read current situation
- observation ↔ observation result ↔ external result
- plan ↔ planning ↔ plan / decide
- decide ↔ make a decision ↔ choose next step
- act ↔ action ↔ execute action
- observe result ↔ inspect action result ↔ read tool result
- goal completed ↔ task completed ↔ completion
- blocked ↔ unable to continue ↔ blocked state
- approval required ↔ human approval required ↔ confirmation required
- failure ↔ execution failure ↔ unsuccessful outcome
- stop condition ↔ termination condition ↔ stopping rule
- control ↔ execution control ↔ control layer
- permissions ↔ permission rules ↔ access permissions
- limits ↔ constraints ↔ execution limits
- logs ↔ execution logs ↔ activity records
- human approval ↔ human review ↔ human confirmation ↔ person-in-the-loop approval
- review ↔ inspect ↔ human review
- confirm ↔ approve ↔ authorize
- sensitive action ↔ high-impact action ↔ action requiring review
- external systems ↔ outside systems ↔ connected systems
- browser ↔ web browser ↔ browser environment
- database ↔ data store ↔ database system
- files ↔ file system ↔ documents and files
- business apps ↔ business applications ↔ enterprise applications
- building block ↔ component ↔ system part
- six pieces ↔ six building blocks ↔ core building blocks
- think ↔ reason ↔ generate and reason
- direct ↔ instruct ↔ guide
- remember ↔ retain ↔ store information
- connect ↔ integrate ↔ bridge to external capabilities
- architecture ↔ system architecture ↔ agent architecture
- architecture stack ↔ architecture flow ↔ end-to-end system flow
- user goal to result ↔ goal-to-result flow ↔ end-to-end agent flow
- task context and history ↔ context and history ↔ task information
- dynamic decision ↔ runtime decision ↔ adaptive decision
- predefined step ↔ fixed step ↔ preconfigured step
- dynamic ↔ adaptive ↔ runtime-selected
- predefined ↔ fixed ↔ specified in advance
- workflow ↔ task workflow ↔ process flow ↔ sequence of steps
- predefined workflow ↔ fixed workflow ↔ scripted workflow
- single agent + tools ↔ single-agent tool use ↔ one-agent tool pattern
- agent + RAG ↔ retrieval-augmented agent ↔ agent with retrieval
- RAG ↔ retrieval-augmented generation ↔ retrieval-enhanced generation
- retrieve ↔ look up ↔ fetch relevant knowledge
- relevant knowledge ↔ relevant information ↔ task-relevant context
- agent + human approval ↔ human-approved agent ↔ human-in-the-loop agent
- propose an action ↔ suggest an action ↔ recommend an action
- multi-agent ↔ multi-agent system ↔ multiple-agent architecture
- specialized agent ↔ specialist agent ↔ task-specific agent
- coordinate ↔ collaborate ↔ orchestrate
- agent team ↔ specialist agent team ↔ multi-agent team
- common agent pattern ↔ agent pattern ↔ agent architecture pattern
- framework ↔ software framework ↔ development framework
- agent framework ↔ framework for AI agents ↔ agent development framework
- framework layer ↔ development layer ↔ orchestration layer
- assemble ↔ compose ↔ put together
- manage ↔ coordinate ↔ operate
- orchestration ↔ coordination ↔ system orchestration
- reusable pattern ↔ reusable design ↔ repeatable pattern
- application ↔ AI application ↔ agent application
- useful experience ↔ user experience ↔ end-user experience
- framework to application ↔ building-blocks-to-application path ↔ development path
- agent system equation ↔ agent system formula ↔ model-tools-state-loop formula
- capability versus system ↔ capability vs system ↔ model capability versus complete system
- model versus agent ↔ model vs agent ↔ model-versus-agent distinction
- framework versus model ↔ framework vs model ↔ framework-versus-model boundary
- framework versus workflow ↔ framework vs workflow
- framework versus application ↔ framework vs app
- framework versus agent product ↔ framework vs product
- framework versus workflow platform ↔ framework vs platform
- check order 123 and draft an update email ↔ order lookup and email-draft example
- order ID ↔ order identifier ↔ order number
- order status ↔ order state ↔ current order information
- draft email ↔ compose email ↔ prepare email draft
- send if approved ↔ send after approval ↔ approved sending
- example flow ↔ example workflow ↔ illustrative agent flow
- acceptance check ↔ acceptance criteria ↔ page pass / fail check
- task status ↔ execution status ↔ current task condition
- progress ↔ task progress ↔ completion progress
- control plane ↔ control layer ↔ governance layer
- safety control ↔ guardrail ↔ protective control
- trust boundary ↔ system boundary ↔ permission boundary

## Do Not Confuse Candidates

- **Model vs agent system**：模型主要提供生成和推理能力；智能体系统还需要指令、工具、状态和循环，才能围绕目标行动。
- **Model vs agent**：页面的简化边界是“模型生成并推理”，而“智能体在行动循环中使用模型能力”。不要把一个模型名称直接当成完整智能体。
- **Framework vs model**：框架负责组装、编排和管理系统部件；模型负责提供 AI 能力。框架不是模型。
- **Framework vs agent system**：框架是用于构建系统的开发结构；agent system 是模型、指令、工具、状态和执行逻辑组合后的运行系统。
- **Framework vs AI application**：框架面向开发者，帮助搭建系统；AI application 是具体的用户软件和体验。
- **Framework vs agent product**：框架不是给用户直接使用的成品；agent product 是把系统包装成可用产品后的体验。
- **Framework vs workflow**：框架提供组装和管理能力；workflow 是完成任务的一串步骤。
- **Framework vs workflow platform**：框架偏向代码和系统组织；workflow platform 可能提供更完整的工作流设计与运行环境，页面没有进一步定义平台边界。
- **Agent vs workflow**：agent 可以根据观察动态决定下一步；workflow 通常按照预定义步骤执行。真实系统可以同时包含二者。
- **Agent loop vs workflow**：agent loop 是反复观察、规划／决策、行动、观察结果和更新状态的控制循环；workflow 是按步骤组织的流程，二者可以结合但不是同义词。
- **State vs memory**：state 更强调当前任务或执行进度；memory 更强调保留后供未来使用的信息，页面把二者并列但没有声称它们完全相同。
- **State vs context**：state 是系统当前情况；context 是提供给模型理解任务的信息集合，可能重叠但用途不同。
- **State update vs state transition**：更新状态是写入新信息；状态转换是从一个状态进入另一个状态，页面没有正式定义状态机。
- **Tool vs model**：工具提供外部动作或数据访问；模型提供生成和推理，通常需要通过工具调用影响外部系统。
- **Tool call vs tool result**：tool call 是发起调用的请求；tool result 是工具或外部系统返回的信息。
- **Tool vs API / MCP**：tool 是可执行能力；API 或 MCP 是把能力结构化暴露给系统的连接方式，页面将 Tools / MCP / APIs 放在架构连接层中，但三者不是完全同一层。
- **API vs MCP**：API 是广义的软件接口；MCP 是用于连接模型／智能体与外部能力的特定协议，不能把所有 API 都叫 MCP。
- **Approved action vs automatic action**：approved 表示被允许；automatic 表示不需要每次人工确认即可执行，某个动作可以被允许但仍要求人工批准。
- **Human approval vs human review**：review 是检查；approval 是检查后明确同意。页面示例是人审核，获准后才发送。
- **Permissions vs human approval**：permissions 是系统预先拥有的访问或行动授权；human approval 是某一步由人临时确认，二者共同形成控制。
- **Sensitive action vs external action**：外部动作不一定敏感；敏感动作是足够重要或有风险、需要人工检查的外部动作。
- **Control vs tool**：工具让系统能够行动；控制机制规定哪些行动能发生、是否需要批准以及何时停止。
- **Logs vs memory**：日志是执行记录；memory 是系统为后续任务保留和使用的信息，二者可能都存储数据但目的不同。
- **Goal vs result**：goal 是想达到的目标；result 是处理后产生的结果。
- **Observe vs act**：observe 读取情况；act 改变或查询外部世界，页面把两者作为循环中的不同阶段。
- **Plan vs decide**：plan 更像行动方案；decide 是从可能方案中选择下一步，页面把它们合并为 Plan / Decide 阶段。
- **Failure vs blocked**：failure 表示某次执行没有成功；blocked 表示系统无法继续，可能由缺少信息、权限或批准造成。
- **Failure vs stop condition**：failure 是一种结果；stop condition 是让循环停止或暂停的规则，页面把 failure / stop condition 并列为停止原因。
- **Goal completed vs stop**：目标完成会让循环停止，但停止也可能因为 blocked、approval required 或 failure，停止不等于成功。
- **RAG vs memory**：RAG 是行动或生成前检索相关知识的模式；memory 是保留信息的机制，RAG 可以使用记忆但不等于记忆。
- **RAG vs tool use**：RAG 是一种具体的检索增强模式；工具是更广义的外部能力，检索可以通过工具实现但工具不只用于检索。
- **Single agent + tools vs multi-agent**：多个工具不等于多个智能体；single agent + tools 仍然只有一个主要 agent。
- **Multi-agent vs multiple tools**：multi-agent 是多个能判断和行动的智能体；多个工具只是多个外部能力。
- **Specialized agent vs specialized tool**：专业化智能体负责判断和行动；专业化工具通常只提供某项外部能力。
- **Multi-agent vs workflow**：多智能体描述参与者数量和协作架构；工作流描述步骤组织方式，两者可同时存在。
- **Dynamic decision vs predefined step**：动态决策在运行时依观察结果选择；预定义步骤在运行前已设定。
- **Dynamic workflow vs agent**：动态工作流可能有变化步骤，但不一定具备模型推理和自主行动能力；agent 是页面强调的系统概念。
- **Framework vs orchestration**：framework 是提供组织能力的软件结构；orchestration 是协调模型、工具、状态和步骤的行为或机制。
- **Orchestration vs automation**：编排强调多个组件如何配合；自动化强调是否无需人工执行，固定流程也可以自动化。
- **Application vs product**：页面使用 application 和 useful experience，但没有展开完整产品运营层；不要把应用、产品和框架当作同一层。
- **Browser / database / files / business apps vs agent**：这些是外部系统或环境，不是智能体本身；智能体通过工具、API 或 MCP 与它们连接。
- **MCP vs model**：MCP 是连接协议，不能与被连接的模型混淆。
- **MCP vs framework**：MCP 提供结构化桥梁；框架负责组装更完整的 agent system，二者可以配合。
- **System prompt vs model**：system prompt 是指导模型行为的指令层；不是模型参数或模型本身。
- **State / memory vs logs**：状态和记忆服务于继续处理任务；日志主要用于记录发生过什么。
- **Human approval vs full manual workflow**：有人工批准节点不代表整个流程都是人工执行；页面示例中大部分步骤由系统完成，最终发送由人批准。
- **Tool call vs external action**：tool call 是请求形式；external action 是实际查询或改变外部系统的动作。
- **Order ID vs order status**：order ID 用来定位订单；order status 是查询返回的订单情况。
- **Draft email vs send email**：draft email 是可审核的草稿；send if approved 才是经过确认后的外部发送动作。
- **Acceptance check vs evaluation**：页面的 acceptance check 是对读者能否解释概念的验收，不是对 agent 输出质量的系统评估。
- **Control plane vs execution loop**：控制面规定权限、审批、日志和停止条件；执行循环负责具体的观察、决策和行动。
- **Capability vs permission**：capability 是能做什么；permission 是是否获准做，拥有工具能力不代表每次都被授权。
- **Approval required vs blocked**：需要批准可能只是暂时暂停并可继续；blocked 表示系统当前无法继续，页面把二者列为不同停止状态。
- **Agent system equation vs complete production architecture**：`Model + Tools + State + Loop = Agent System` 是页面的简化心智模型，不是生产系统的完整组件清单。

## Notes

- 本文件是 Module 15 · Agent Development 下 `How Are AI Agents Built?` 主题的 raw glossary 收集稿，目标是最大化保留候选，不做去重、归并或最终取舍。
- 已完整阅读 `how-agents-are-built.html` 的正文内容，包括页面导航、lede、主架构图、六个核心构建块、Agent Loop、订单与邮件示例、四种常见模式、框架适配流程、两个对比卡片、Remember this 总结和 Acceptance check。
- 页面主线心智模型是：用户目标 → Agent System → Tools / MCP / APIs → External Systems → Result；Human Approval 与 Control 横向约束敏感行动。
- 页面明确将 AI agent 描述为“不是一个模型或一个工具”，而是结合 model intelligence、instructions、tools、state 和 execution loop 的 system；相关词形和拆分候选均保留。
- 六个核心构建块按页面标签保留为：Model、Instructions / System Prompt、Tools、State / Memory、API / MCP、Permissions / Human Approval；同时保留 THINK、DIRECT、ACT、REMEMBER、CONNECT、CONTROL 这些动作标签。
- Agent Loop 的页面顺序完整保留为：GOAL → OBSERVE → PLAN / DECIDE → ACT → OBSERVE RESULT → UPDATE STATE；停止条件完整保留为 Goal completed、Blocked、Approval required、Failure / stop condition。
- 页面示例的每个流程节点均保留：User Goal、Agent reads order ID、Tool call `get_order("123")`、System returns status、Agent updates state、Agent drafts email、Human reviews → send if approved。
- 四种常见模式完整保留为：Single Agent + Tools、Agent + RAG、Agent + Human Approval、Multi-Agent；相关机制词包括检索相关知识、提出动作、人工控制敏感步骤和专业化智能体协作。
- 页面用 `Model + Tools + State + Loop = Agent System` 做简化公式；Instructions、API / MCP、Permissions / Human Approval 在其他架构区域出现，因此没有把公式误当成页面所有部件的唯一清单。
- 页面明确的边界包括 Model vs Agent、Agent vs Workflow，以及“agent 是 system”而不是单一模型或工具；这些边界在 Do Not Confuse 中单独保留。
- 页面没有数字型性能指标。`Goal completed`、`Blocked`、`Approval required`、`Failure / stop condition` 是循环状态／停止结果，已按“指标／状态候选”保留，但不应误称为页面给出的数值 KPI。
- 页面未展开 latency、cost、token usage、throughput、success rate 等运行指标；它们被放入 Potential Missing Concepts，作为后续整理时的缺口候选。
- 页面中的 `MCP`、`API`、`RAG` 和 `get_order("123")` 分别作为连接协议／接口、检索增强模式和工具调用示例保留；没有把它们当作同义词。
- 页面中的 `Browser · Database · Files · Business Apps` 是外部系统示例，不是 agent 本身；`Tools / MCP / APIs` 是连接或调用层。
- 本文件有意保留单复数、标题词、动作标签、流程节点、对比短语和正文重要词的重复／变体；后续整理阶段再决定是否合并。
- Potential Missing Concepts 只列出与本页直接相邻但正文没有完整展开的概念，不代表这些概念已由本页定义。
- 本文件只写入 `glossary-work/raw/15-how-agents-are-built.md`，未修改网站 HTML、CSS、脚本、GitHub 或其他非目标内容。
