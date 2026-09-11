# Topic

Agent Loop

## Topic Metadata

- Module: 06 · Agents, Tools & MCP
- Topic number: Topic 02
- Topic title: What is an Agent Loop?
- Source File: `agent-loop.html`
- Page description: An agent loop is a repeated cycle of deciding, acting, observing, and deciding again.
- Primary page sections: What is it?; Think of it like...; How it works; Real-world examples; What it is NOT; Related concepts; Remember this; Video
- Collection status: Raw candidate collection; intentionally maximized, not deduplicated or finalized.

## Glossary Candidates

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Agent Loop | 智能体循环；代理循环 | A repeated cycle in which an AI system decides, acts, observes, and decides again. | AI 系统反复判断、行动、看结果，再决定下一步的循环。 |
| agent loop | 智能体循环；代理循环 | The control cycle that lets an AI system take steps and choose what to do next. | 让 AI 一步步做事并决定下一步的控制流程。 |
| repeated cycle | 重复循环 | A sequence that happens again after it reaches a later step. | 做完一轮后继续再做下一轮。 |
| cycle | 循环；周期 | A process that returns to an earlier step and repeats. | 流程回到前面重新开始。 |
| control cycle | 控制循环 | A loop that controls what a system does over time. | 管理系统每一步行动的循环机制。 |
| AI system | 人工智能系统 | A system that uses AI to process information and act. | 使用人工智能处理信息和行动的一整套系统。 |
| system | 系统 | A connected set of parts that performs a task. | 许多部分一起完成任务的整体。 |
| goal | 目标 | The objective the system is trying to achieve. | 系统想要完成的事情。 |
| objective | 目标；目的 | The result a task is intended to reach. | 一项任务希望达到的结果。 |
| task | 任务 | Work that the system is asked to perform. | 交给系统要完成的一件事。 |
| task definition | 任务定义 | A description of what the task is and what counts as completion. | 说明要做什么、做到什么程度算完成。 |
| stopping rule | 停止规则 | A rule that says when the system should stop. | 告诉系统什么时候必须停下来的规则。 |
| stop condition | 停止条件 | A condition that tells the loop to finish instead of continuing. | 满足这个条件后循环结束。 |
| controlled stop condition | 受控停止条件 | A checked condition that makes the loop stop safely. | 经过控制、能让系统安全结束的停止标准。 |
| limit | 限制；上限 | A boundary on how long or how much the loop may continue. | 限制循环次数、时间或资源的上限。 |
| validation | 验证；校验 | Checking whether a result or action is acceptable. | 检查结果或行动是否符合要求。 |
| blind continuation | 盲目继续 | Continuing without checking results or limits. | 不看结果、不受限制地一直做下去。 |
| decide | 决定 | Choose the next result or action from available information. | 根据当前信息选择下一步。 |
| decision | 决策；决定 | A choice about what the system should do next. | 系统对下一步做出的选择。 |
| model decision | 模型决策 | A decision selected by the model within the loop. | 模型在循环中选择的下一步。 |
| model | 模型 | The component that selects or proposes an action. | 负责判断或提出行动建议的模型。 |
| action | 行动；动作 | A step the system takes after deciding. | 系统做出决定后真正执行的一步。 |
| action selection | 动作选择 | Choosing one action from available actions. | 从可用动作中选出一个。 |
| select an action | 选择行动 | Pick what the system will do next. | 选定系统接下来要做的事情。 |
| available action | 可用行动 | An action the system is allowed and able to perform. | 系统被允许、也能执行的动作。 |
| act | 行动；执行 | Execute the selected action. | 把选好的动作真正做出来。 |
| execution | 执行 | Carrying out an action in the environment. | 在外部环境中实际执行动作。 |
| allowed action | 允许的行动 | An action permitted by the system’s rules or controls. | 经过规则或权限允许的动作。 |
| tool | 工具 | An external capability the system can call to do something. | AI 可以调用来搜索、读取或操作的外部能力。 |
| tool call | 工具调用 | A request from the system to execute a tool. | 系统请求某个工具帮它做事。 |
| call a tool | 调用工具 | Use an available tool to perform an action. | 让工具执行选定的动作。 |
| tool execution | 工具执行 | The tool carrying out the requested operation. | 工具实际完成被请求的操作。 |
| tool output | 工具输出 | The result returned by a tool after execution. | 工具执行后返回的信息。 |
| observe | 观察；观测 | Read what happened after an action. | 看行动之后发生了什么。 |
| observation | 观察结果；观测 | Information about the result or current state after an action. | 行动后得到的结果或状态信息。 |
| observe the result | 观察结果 | Inspect the outcome of an action. | 检查动作执行后的结果。 |
| read the result | 读取结果 | Take in the returned outcome as information. | 把返回结果读进系统。 |
| result | 结果 | What the system or tool produces after an action. | 系统或工具行动后产生的东西。 |
| outcome | 结果；后果 | The state or effect produced by an action. | 一个动作带来的结果或影响。 |
| environment | 环境 | The outside world or system in which an action happens. | 动作发生的外部世界或软件系统。 |
| system state | 系统状态 | The current information about what the system or environment is like. | 系统或外部环境当前处于什么情况。 |
| state | 状态 | The current condition available to guide the next decision. | 帮助系统决定下一步的当前情况。 |
| context | 上下文 | Information carried into the next decision. | 下一步判断时可以参考的信息。 |
| new context | 新上下文 | Fresh information produced by the latest action or observation. | 最近一次行动或观察带来的新信息。 |
| tool output becomes new context | 工具输出成为新上下文 | A tool result is fed back into the next decision. | 工具返回的结果会成为下一轮判断的依据。 |
| feedback loop | 反馈循环 | A cycle in which results influence later actions. | 前一步结果会影响后一步的循环。 |
| next step | 下一步 | The action or decision that follows the current one. | 当前步骤之后要做的事情。 |
| choose what to do next | 选择下一步 | Select the next action using the current state and goal. | 根据目标和当前情况决定接下来做什么。 |
| finish | 完成；结束 | Stop because the task has reached an acceptable endpoint. | 任务已经达到可以结束的状态。 |
| repeat | 重复 | Run another pass through the loop. | 再进行一轮循环。 |
| continue | 继续 | Keep running because the task is not finished. | 任务还没完成，所以继续做。 |
| ask | 询问 | Request clarification or information from a person. | 信息不够时向人提问。 |
| ask for clarification | 请求澄清 | Ask the user to make an unclear request more specific. | 用户说得不清楚时，请他补充说明。 |
| completion | 完成；完成状态 | The point at which the requested task is done. | 被要求的事情已经做完。 |
| goal setting | 目标设定 | Define the objective before taking actions. | 在行动前明确要达成什么。 |
| set the objective | 设定目标 | State what the system should accomplish. | 说清楚系统要完成什么。 |
| define the task | 定义任务 | Specify the work and expected endpoint. | 明确任务内容和预期结果。 |
| define stopping rules | 定义停止规则 | Specify the conditions and limits for ending the loop. | 规定什么时候、按什么标准结束。 |
| Step 1 · Goal | 第一步·目标 | The first process stage: set the objective and stopping rules. | 第一阶段：先确定目标和停止标准。 |
| Step 2 · Decide | 第二步·决定 | The process stage where the model selects an action. | 第二阶段：模型选择要做的动作。 |
| Step 3 · Act | 第三步·行动 | The process stage where the system executes an allowed action. | 第三阶段：系统真正执行动作。 |
| Step 4 · Observe | 第四步·观察 | The process stage where the system reads the result. | 第四阶段：系统查看动作结果。 |
| Step 5 · Stop | 第五步·停止 | The process stage where the system finishes, asks, or repeats. | 第五阶段：完成、提问，或继续下一轮。 |
| process step | 流程步骤 | One named stage in the agent loop. | 循环中的一个阶段。 |
| process flow | 流程流转 | The ordered movement from one step to the next. | 按顺序从一个步骤走到下一个步骤。 |
| Goal → Decide → Tool → Observe → Decide again → Stop | 目标→决定→工具→观察→再次决定→停止 | A compact representation of the loop. | 用箭头表示智能体循环的主要路线。 |
| decide again | 再次决定 | Make another decision after observing new information. | 看完新结果后重新判断。 |
| iteration | 迭代；一轮循环 | One pass of a repeated process. | 循环执行的一轮。 |
| loop iteration | 循环迭代 | One complete or partial run through loop steps. | 智能体循环跑过的一轮或部分一轮。 |
| route | 路线；路径 | A planned way to reach a destination. | 从当前位置到目标的计划路径。 |
| turn | 转弯；转向 | A change of direction during navigation. | 行进中改变方向的一次转弯。 |
| navigation system | 导航系统 | A system that follows a route and updates directions. | 按路线行驶并根据情况更新指引的系统。 |
| follow a route | 按路线行进 | Move according to a planned sequence of directions. | 按照预先规划的路线前进。 |
| road condition | 道路状况 | The current situation on the road that may affect a route. | 会影响路线的当前道路情况。 |
| update the next turn | 更新下一转向 | Change the next direction after observing new conditions. | 看见道路变化后改变下一步指引。 |
| conditions change | 条件变化 | The environment becomes different from what was expected. | 外部情况发生变化，原计划可能不再合适。 |
| navigation analogy | 导航类比 | Explaining an agent loop through route checking. | 用开车和重新看路线来理解智能体循环。 |
| web research | 网络研究；网页检索 | Research that searches and reads multiple online sources. | 查找并阅读多个网上来源来回答问题。 |
| everyday example | 日常示例 | A common real-world use case. | 普通人可能遇到的实际例子。 |
| business example | 商业示例 | A use case inside a business process. | 企业工作流程中的实际例子。 |
| real-world example | 真实世界示例 | An example of the loop used in practice. | 智能体循环在现实中的一种用法。 |
| input | 输入 | Information supplied to start or guide a task. | 交给系统处理的信息。 |
| question | 问题 | A request for information or an answer. | 用户希望系统回答的事情。 |
| question needing several sources | 需要多个来源的问题 | A question that cannot be responsibly answered from one source alone. | 需要查几份资料才能回答的问题。 |
| source | 来源；资料来源 | A place or document from which information is obtained. | 信息来自的网页、文件或记录。 |
| several sources | 多个来源 | More than one source used for research. | 不止一份的资料来源。 |
| search | 搜索 | Look for relevant information in available sources. | 在资料中寻找相关信息。 |
| search results | 搜索结果 | Information returned by a search. | 搜索后得到的网页或资料列表。 |
| read results | 阅读结果 | Inspect the information returned by a search. | 阅读搜索找到的内容。 |
| refine the query | 优化查询 | Change a search request to get more useful results. | 根据已经看到的结果改写搜索词。 |
| query | 查询；搜索请求 | The terms or request sent to a search system. | 发给搜索系统的检索内容。 |
| query refinement | 查询优化 | Improving a query based on observed results. | 根据结果让搜索问题变得更准确。 |
| sourced answer | 有来源的答案 | An answer supported by identified sources. | 能指出资料出处的回答。 |
| clarification request | 澄清请求 | A request for more information before continuing. | 继续处理前向用户索取补充信息。 |
| support ticket | 支持工单；客服工单 | A recorded customer support request. | 记录客户问题和处理过程的一张工单。 |
| ticket handling | 工单处理 | The process of checking, acting on, and responding to a ticket. | 查看、处理并回复客服工单。 |
| check records | 检查记录 | Look up relevant stored information. | 查询系统里已有的记录。 |
| record | 记录 | Stored information about an item, event, or customer. | 系统保存的一条信息。 |
| propose an action | 提出行动建议 | Suggest what should be done next. | 给出下一步应该做什么的建议。 |
| validate an action | 验证行动 | Check that a proposed or completed action is acceptable. | 检查建议或动作是否正确、允许、合适。 |
| response | 回复；响应 | A message produced in reply to a request. | 针对请求返回的一段话或结果。 |
| update | 更新 | A change made to a record or system state. | 对记录或系统状态做出的改变。 |
| human handoff | 转交人工；人工接管 | Pass the task to a person. | AI 处理不了时交给人继续处理。 |
| handoff | 交接；转交 | Transfer responsibility to another person or system. | 把处理责任交给另一个主体。 |
| human | 人类；人工人员 | A person who may clarify, review, or take over. | 可以补充信息、检查结果或接手任务的人。 |
| human-in-the-loop | 人在回路中 | A workflow where a person remains available to review or decide. | AI 做事时人保留检查或决定权。 |
| one model call | 一次模型调用 | One request that produces one response from one input. | 只把一次输入交给模型、得到一次回答。 |
| model call | 模型调用 | One invocation of a model to produce a response. | 请求模型处理一次输入。 |
| one response | 一次响应 | The output from a single model invocation. | 一次模型调用返回的一份结果。 |
| one input | 一次输入 | The information provided to one model call. | 单次模型调用收到的信息。 |
| multiple decisions | 多次决策 | More than one decision made across a task. | 任务过程中反复做出多个判断。 |
| multiple actions | 多次行动 | More than one operation performed across a task. | 任务过程中执行多个动作。 |
| infinite loop | 无限循环 | A loop that keeps running without reaching a safe end. | 一直运行、没有安全结束点的循环。 |
| safe end | 安全结束 | An endpoint reached without uncontrolled continuation or harm. | 系统受控地完成并停下。 |
| programmed system pattern | 编程系统模式 | A deliberately designed software pattern. | 开发者设计出来的一种软件工作方式。 |
| human reasoning | 人类推理 | Human thinking and reasoning, which the loop does not reproduce exactly. | 人类自己的思考推理方式，不等于这套程序循环。 |
| reproduce exactly | 完全复现 | Match something in every important way. | 一点不差地复制某种能力或过程。 |
| misconception | 误解；常见误区 | A mistaken idea about what a concept means. | 对一个概念的错误理解。 |
| not equal | 不等于 | A warning that two concepts should not be treated as identical. | 提醒这两个概念不是同一个东西。 |
| related concept | 相关概念 | A concept connected to the topic but not identical to it. | 和主题有关、但不一定同义的概念。 |
| functional test | 功能测试 | A test that checks whether a system behaves as intended. | 检查系统功能是否按预期工作的测试。 |
| failure handling | 故障处理；失败处理 | Managing what happens when an action or task fails. | 动作失败时如何应对和继续处理。 |
| video explainer | 视频讲解 | A video that explains a topic visually. | 用视频和画面解释主题。 |
| visual explainer | 可视化讲解 | An explanation supported by visuals. | 借助图示、动画或画面来说明。 |
| captions | 字幕 | Text that represents spoken content in a video. | 视频里显示讲话内容的文字。 |
| independent explainer | 独立讲解内容 | A separate explanatory media item. | 页面之外单独提供的讲解材料。 |
| follow the loop | 遵循循环 | Carry out the ordered cycle of decisions and actions. | 按循环规定的顺序一步步处理。 |
| complete the task | 完成任务 | Reach an acceptable result for the requested work. | 把用户交代的事情做到可接受的结果。 |
| controlled process | 受控流程 | A process constrained by rules, limits, and checks. | 有规则、上限和检查的流程。 |
| agent behavior | 智能体行为 | The observable decisions and actions of an agent. | 智能体实际做出的判断和动作。 |
| agent architecture | 智能体架构 | The design of components and steps supporting an agent. | 支撑智能体运行的组件和流程设计。 |
| planning | 规划 | Decide a sequence of actions to reach a goal. | 为了目标安排要做的步骤。 |
| tool use | 工具使用 | Using external tools as part of completing a task. | 在完成任务时使用外部工具。 |
| observation state | 观测状态 | The state information available after an action. | 动作后系统观察到的当前情况。 |
| termination | 终止 | The event of ending the loop. | 循环结束这件事。 |
| termination criterion | 终止标准 | A rule used to decide whether the loop may stop. | 判断循环能否停止的标准。 |
| safety limit | 安全上限 | A limit that prevents unsafe or unbounded behavior. | 防止系统做得过多或失控的上限。 |
| validation check | 验证检查 | A check performed before accepting a result or continuing. | 接受结果或继续之前做的检查。 |
| action-result cycle | 行动—结果循环 | A cycle in which an action produces an observation for the next decision. | 做动作、看结果，再用结果决定下一步。 |
| decision-action-observation cycle | 决策—行动—观察循环 | A loop built from choosing, executing, and inspecting. | 由选择、执行、查看组成的循环。 |
| decide-act-observe | 决定—行动—观察 | A short name for the core loop sequence. | 智能体循环的核心三步简称。 |
| decide-act-observe-decide | 决定—行动—观察—再决定 | The repeated pattern described by the page. | 决定后行动，观察结果，再次决定。 |
| goal-directed behavior | 目标导向行为 | Behavior organized around reaching a goal. | 围绕目标安排行动，而不是随便输出。 |
| adaptive behavior | 适应性行为 | Behavior that changes when observations or conditions change. | 根据新结果和环境变化调整下一步。 |
| state update | 状态更新 | Change the working state after new information arrives. | 新信息到来后更新系统对当前情况的记录。 |
| next-action decision | 下一动作决策 | The choice of the action that follows the latest observation. | 看完最新结果后选择下一个动作。 |
| action space | 动作空间 | The set of actions available to a system. | 系统可能选择的所有动作集合。 |
| tool-enabled system | 工具增强系统 | A system that can extend its behavior through tools. | 能通过调用工具完成更多事情的系统。 |
| orchestration | 编排 | Coordinate models, tools, steps, and state into a workflow. | 把模型、工具、步骤和状态组织起来协同工作。 |
| workflow | 工作流；工作流程 | An ordered sequence of work steps. | 按顺序连接起来的一组工作步骤。 |
| safe completion | 安全完成 | Finish with the task controlled and within constraints. | 在限制内、可检查地完成任务。 |
| unresolved task | 未解决任务 | A task that still needs more actions or information. | 还没有解决、需要继续处理的任务。 |
| user clarification | 用户澄清 | Extra information supplied by the user. | 用户补充的说明或条件。 |
| source-backed answer | 有来源支撑的答案 | An answer grounded in retrieved or checked sources. | 根据查到并核对过的资料给出的答案。 |
| record update | 记录更新 | A change written to a support or business record. | 对客服或业务记录进行修改。 |
| business process | 业务流程 | A sequence of steps used to run business work. | 企业完成一项工作时的一连串步骤。 |
| system prompt | 系统提示 | High-level instructions that guide system behavior. | 规定系统如何工作的高层指令。 |
| policy | 政策；规则 | A rule or constraint governing allowed behavior. | 规定哪些行为允许、哪些不允许的规则。 |
| permission | 权限 | Authorization to perform an action. | 系统是否允许执行某个动作。 |
| guardrail | 防护栏；护栏 | A control that constrains risky or unwanted behavior. | 防止系统做危险事情的限制措施。 |
| audit trail | 审计轨迹；操作记录 | A record of decisions, actions, and results. | 记录每次判断、行动和结果的过程。 |
| observability | 可观测性 | The ability to inspect what a running system is doing. | 能看清运行中的系统做了什么。 |
| loop state | 循环状态 | The current state of an iteration and its context. | 循环当前这一轮所处的情况。 |
| iteration count | 迭代次数 | How many times the loop has run. | 循环已经执行了多少轮。 |
| timeout | 超时 | A limit that stops waiting or running after too much time. | 时间太久后自动停止等待或运行。 |
| retry | 重试 | Try an action again after a failure or unsuitable result. | 失败或结果不合适时再试一次。 |
| error | 错误；故障 | A problem that prevents an action or task from succeeding. | 阻止动作或任务成功的问题。 |
| failure | 失败 | An action or attempt that does not achieve its intended result. | 一次尝试没有达到预期结果。 |
| retry policy | 重试策略 | Rules for whether and how to try an action again. | 规定什么时候、最多几次可以重试。 |
| escalation | 升级处理 | Transfer a difficult case to a higher level or a person. | 复杂问题交给更高级别或人工处理。 |
| human approval | 人工批准 | A person explicitly approves an action before it happens. | 重要动作执行前必须由人点头同意。 |
| confirmation | 确认 | A check that a planned action is accepted before execution. | 执行动作前再次确认是否可以做。 |
| action authorization | 动作授权 | Permission for the system to perform a selected action. | 允许系统执行某个选定动作。 |
| completion signal | 完成信号 | Information indicating that the task is finished. | 告诉系统任务已经完成的信号。 |
| stop signal | 停止信号 | Information or condition that tells the loop to end. | 告诉循环结束的信号或条件。 |
| safe stopping | 安全停止 | End the loop without leaving unsafe or uncontrolled work. | 停下来时不会留下失控或危险操作。 |
| loop safety | 循环安全 | Controls that keep repeated behavior bounded and acceptable. | 让反复行动有边界、可检查、不会失控。 |

## Potential Missing Concepts

- **LLM / large language model（大语言模型）**：页面说“model”决定动作，但没有说明许多现代 agent loop 会由 LLM 作为决策核心。
- **policy（策略）**：页面有 goal、action 和 stopping rules，但没有定义“根据状态选择动作的策略”。
- **planner（规划器）**：页面强调 decide，但没有区分即时动作选择和先制定多步计划的规划器。
- **controller（控制器）**：control cycle 出现了，但没有单独解释负责推进循环的控制组件。
- **state machine（状态机）**：页面描述明确的 Goal、Decide、Act、Observe、Stop 状态，但没有用状态机形式建模。
- **transition（状态转移）**：没有解释行动或观察如何把系统从一个状态带到下一个状态。
- **event（事件）**：没有说明什么事件会触发一次观察、重试、停止或人工接管。
- **memory（记忆）**：context 出现了，但没有说明短期记忆、长期记忆或跨轮次状态保存。
- **working memory（工作记忆）**：没有解释当前循环保存哪些临时信息。
- **external memory（外部记忆）**：没有说明把历史状态保存到数据库、文件或向量存储中。
- **tool schema（工具模式）**：页面提到 tool，但没有说明工具名称、参数和返回结构如何描述。
- **tool selection（工具选择）**：有“select an action”，但没有明确模型如何在多个工具间选择。
- **tool result parsing（工具结果解析）**：有 read the result，但没有说明非结构化输出如何被解析。
- **function calling（函数调用）**：tool call 的工程实现术语未出现。
- **MCP（Model Context Protocol，模型上下文协议）**：模块标题包含 MCP，但本页没有解释协议如何连接工具与上下文。
- **ReAct（Reasoning and Acting）**：决定、行动、观察的交替模式与 ReAct 相关，但页面没有列出该名称。
- **reasoning（推理）**：页面用 decide，但没有展开模型如何进行推理或规划。
- **chain-of-thought（思维链）**：没有说明内部推理过程与可观察行动之间的区别。
- **agent trajectory（智能体轨迹）**：没有定义一轮任务中状态、动作、观察组成的完整轨迹。
- **episode（回合）**：没有说明从目标开始到停止条件满足的一次完整任务回合。
- **step budget（步骤预算）**：页面说 limits，但没有具体解释最大步骤数。
- **token budget（令牌预算）**：没有讨论循环中上下文和模型调用的 token 上限。
- **time budget（时间预算）**：没有具体讨论循环允许运行多久。
- **cost budget（成本预算）**：没有讨论多次模型调用和工具调用的费用限制。
- **rate limit（速率限制）**：没有说明工具或 API 调用频率限制。
- **latency（延迟）**：没有讨论每一轮决策、工具执行和观察所花的时间。
- **throughput（吞吐量）**：没有讨论系统每单位时间能处理多少任务。
- **success rate（成功率）**：页面没有给出衡量任务是否成功的指标。
- **task completion rate（任务完成率）**：没有说明多少任务达到 stop condition。
- **tool-call success rate（工具调用成功率）**：没有衡量工具是否按预期返回结果。
- **step efficiency（步骤效率）**：没有衡量完成目标用了多少不必要的循环轮次。
- **cost per task（单任务成本）**：没有计算一次 agent loop 的模型、工具或人工成本。
- **accuracy（准确率）**：没有定义结果是否正确的定量指标。
- **precision / recall / F1（精确率／召回率／F1）**：没有给出检索、分类或决策质量的具体指标。
- **reward（奖励）**：循环有 goal 和结果，但没有说明强化学习式奖励如何指导动作。
- **utility（效用）**：没有定义如何比较不同动作对目标的价值。
- **confidence（置信度）**：没有说明模型如何表达下一步选择的信心。
- **uncertainty（不确定性）**：页面有 ask 和 human handoff，但没有给出不确定性估计。
- **verification（核验）**：validation 出现了，但没有区分动作前检查、结果后核验和事实核验。
- **reflection（反思）**：decide again 出现了，但没有明确让 agent 总结错误并调整策略的反思步骤。
- **self-correction（自我纠错）**：没有说明系统发现结果不合适后如何修正。
- **replanning（重新规划）**：路线更新类比出现了，但没有把变化后的计划重建命名为 replanning。
- **fallback（备用路径）**：失败或工具不可用时的替代动作没有展开。
- **rollback（回滚）**：页面提到 update，但没有说明错误变更如何撤销。
- **idempotency（幂等性）**：重试可能重复执行动作，但页面没有讨论如何避免重复副作用。
- **transaction（事务）**：业务记录更新可能需要原子性，但没有解释事务边界。
- **side effect（副作用）**：行动可能改变外部系统，但页面没有讨论不可逆影响。
- **sandbox（沙箱）**：没有说明如何在隔离环境中限制工具动作。
- **permission scope（权限范围）**：allowed action 出现了，但没有说明权限最小化。
- **prompt injection（提示注入）**：web research 和工具调用场景可能遇到不可信内容，但本页没有安全攻击讨论。
- **data exfiltration（数据外泄）**：没有讨论工具或外部内容诱导系统泄露上下文。
- **hallucination（幻觉）**：sourced answer 和 validation 出现了，但没有明确生成错误或虚构信息风险。
- **human oversight（人工监督）**：human handoff 有提及，但没有展开持续监督和审计职责。
- **approval gate（审批闸门）**：没有说明哪些高风险 action 必须先经过人工审批。
- **interruptibility（可中断性）**：没有说明人如何随时暂停或终止循环。
- **deadlock（死锁）**：没有讨论循环在等待资源或相互依赖时无法推进的情况。
- **oscillation（振荡）**：没有讨论 agent 在两个动作之间反复切换而不进展。
- **stagnation（停滞）**：没有讨论连续多轮没有产生新信息或进展。
- **infinite recursion（无限递归）**：与 infinite loop 相邻，但页面没有区分递归调用和循环。
- **observability metrics（可观测性指标）**：没有列出记录决策、工具调用、状态和停止原因的指标。
- **trace（追踪）**：没有定义如何保存一次循环的完整运行轨迹。
- **logging（日志记录）**：没有说明应记录哪些动作、输入、输出和异常。
- **debugging（调试）**：没有说明如何定位某轮决策或工具执行的问题。
- **evaluation harness（评测框架）**：functional tests 出现了，但没有说明批量评测 agent loop 的框架。
- **simulation（模拟）**：导航类比存在，但没有讨论在仿真环境中测试行动。
- **benchmark（基准测试）**：没有比较不同 agent loop 的标准任务或基准。
- **regression test（回归测试）**：没有说明修改循环后如何确保既有任务仍正常。
- **determinism（确定性）**：没有讨论同样输入是否会得到同样的动作序列。
- **temperature（温度）**：没有讨论模型采样随机性如何影响循环行为。
- **concurrency（并发）**：页面只描述单条循环，没有讨论多个动作同时执行。
- **parallel tool calls（并行工具调用）**：没有讨论一次决定后同时调用多个工具。
- **multi-agent loop（多智能体循环）**：没有区分单智能体和多个 agent 协作的循环。
- **sub-agent（子智能体）**：没有讨论把子任务交给另一个智能体。
- **human-in-the-loop policy（人在回路策略）**：human handoff 出现了，但没有定义何时必须转人工。
- **completion criteria（完成标准）**：stop condition 有出现，但没有系统化说明可接受完成的标准。

## Aliases / Synonyms

- Agent Loop ↔ agent loop ↔ agent control loop ↔ intelligent-agent loop
- Agent Loop ↔ decide–act–observe loop ↔ decision–action–observation cycle
- Agent loop ↔ action–observation loop ↔ feedback loop（feedback loop 更宽泛，不一定是 agent loop）
- Decide ↔ make a decision ↔ choose an action ↔ select the next action
- Act ↔ take action ↔ execute an action ↔ perform an action
- Observe ↔ inspect the result ↔ read the result ↔ receive an observation
- Observation ↔ observed result ↔ tool result ↔ execution result（tool result 只是 observation 的一种来源）
- Goal ↔ objective ↔ desired outcome ↔ task objective
- Stop condition ↔ stopping condition ↔ termination condition ↔ completion condition
- Stopping rule ↔ stop rule ↔ termination rule ↔ stopping criterion
- Limit ↔ bound ↔ cap ↔ budget（budget 通常是某类资源的具体上限）
- Tool ↔ external tool ↔ callable capability ↔ action interface
- Tool call ↔ tool invocation ↔ function call ↔ API call（function call/API call 是工程实现的相邻词）
- Tool output ↔ tool result ↔ returned result ↔ observation
- Context ↔ working context ↔ current context ↔ state information
- State ↔ current state ↔ system state ↔ environment state
- Repeat ↔ iterate ↔ run another iteration ↔ continue the loop
- Finish ↔ complete ↔ terminate ↔ stop
- Ask ↔ request clarification ↔ ask for more information ↔ seek user input
- Human handoff ↔ handoff to a human ↔ escalation to a human ↔ manual takeover
- Human review ↔ human oversight ↔ manual review ↔ human verification
- Validation ↔ validation check ↔ result verification ↔ acceptance check
- Web research ↔ online research ↔ web search workflow ↔ source gathering
- Refine the query ↔ revise the query ↔ improve the search query ↔ query expansion
- Support ticket ↔ customer ticket ↔ service ticket ↔ help-desk ticket
- Ticket handling ↔ ticket processing ↔ support workflow ↔ case handling
- Agent behavior ↔ system behavior ↔ runtime behavior ↔ action policy
- Loop iteration ↔ iteration ↔ cycle pass ↔ step cycle
- Process flow ↔ workflow ↔ execution flow ↔ control flow
- Programmed system pattern ↔ software pattern ↔ control pattern ↔ implementation pattern
- Infinite loop ↔ unbounded loop ↔ non-terminating loop ↔ endless loop
- Safe end ↔ safe termination ↔ controlled completion ↔ bounded stop
- MCP ↔ Model Context Protocol（模块上下文相关缩写；本页只出现在模块名中）
- AI Agent ↔ agent ↔ intelligent agent ↔ software agent（不完全等同；agent 是更宽泛的词）
- Functional Tests ↔ functional testing ↔ behavior tests ↔ feature tests
- Failure Handling ↔ error handling ↔ failure recovery ↔ exception handling

## Do Not Confuse Candidates

- **Agent loop vs one model call**：agent loop 可以反复做决定和行动；一次模型调用通常只从一次输入生成一次响应。
- **Agent loop vs infinite loop**：agent loop 需要 limits 和 stop condition；infinite loop 没有安全结束点，会持续运行。
- **Agent loop vs human reasoning**：agent loop 是编程出来的系统模式，不是人类推理过程的完全复现。
- **Agent loop vs workflow**：workflow 可以是预先固定的步骤；agent loop 会根据 observation 和新 context 决定是否重复或改变下一步。
- **Agent loop vs planning**：planning 主要是安排行动序列；agent loop 还包含执行、观察、验证和终止。
- **Agent loop vs state machine**：state machine 是一种形式化建模方式；agent loop 是一种运行控制模式，两者可以结合但不是同义词。
- **Decide vs act**：decide 是选择动作；act 是真正执行被选中的动作。
- **Action vs tool**：action 是要做的事情；tool 是执行某类 action 的外部能力。
- **Tool call vs tool output**：tool call 是发出的请求；tool output 是工具执行后返回的结果。
- **Observe vs decide**：observe 是读取发生了什么；decide 是根据观察选择下一步。
- **Observation vs context**：observation 是新获得的结果；context 是供后续决策使用的更广泛信息集合。
- **Goal vs stop condition**：goal 说明想达成什么；stop condition 说明什么时候可以结束。
- **Stopping rule vs limit**：stopping rule 可以是任务完成或人工接管；limit 通常是次数、时间或资源上限。
- **Finish vs stop**：finish 表示任务达到可接受完成状态；stop 也可能是达到上限、遇到问题或转人工。
- **Repeat vs retry**：repeat 是正常进入下一轮；retry 通常是失败后重做同一个动作。
- **Validation vs observation**：observation 读取结果；validation 判断结果是否合格。
- **Validation vs human review**：validation 可以由系统自动执行；human review 需要人检查或判断。
- **Human handoff vs human-in-the-loop**：handoff 是把任务交给人；human-in-the-loop 是人持续保留检查、批准或接管位置。
- **Clarification request vs human handoff**：clarification request 只是向用户补充提问；handoff 是转移处理责任。
- **Sourced answer vs validated answer**：有来源不代表内容已经被验证；仍需要检查来源和答案是否支持结论。
- **Web research vs search**：search 是一次查找动作；web research 是可能包含多次搜索、阅读、改写查询的完整工作流。
- **Query refinement vs replanning**：query refinement 只修改搜索请求；replanning 可以重建整个任务的行动计划。
- **Support ticket vs ticket handling**：ticket 是被处理的记录；ticket handling 是围绕记录执行的一系列动作。
- **Response vs update**：response 是返回给请求方的信息；update 是对记录或系统状态的修改。
- **Infinite loop vs long-running loop**：长时间运行不一定是错误，只要有边界和停止机制；无限循环缺少安全终点。
- **Safe end vs successful outcome**：安全结束可以是失败后停止或转人工；不一定代表任务成功。
- **Agent loop vs autonomous agent**：agent loop 是控制机制；autonomous agent 是使用该机制并能相对独立行动的系统。
- **Agent loop vs ReAct**：ReAct 是一种特定的推理—行动方法；agent loop 是更宽泛的循环结构。
- **Tool calling vs function calling**：tool calling 是面向外部能力的总称；function calling 是常见的接口实现方式。
- **Model decision vs human decision**：模型决策由模型提出或选择；人类决策由人检查、批准或接管。
- **Action selection vs action execution**：selection 选动作；execution 执行动作。
- **System state vs tool output**：tool output 是一次返回的信息；system state 可能包含多轮上下文和外部状态。
- **Context vs memory**：context 是当前可供模型使用的信息；memory 通常强调跨轮次保存和取回信息。
- **Limit vs guardrail**：limit 是数量、时间等边界；guardrail 是更广泛的安全或行为约束。
- **Error vs failure**：error 是导致问题的错误或异常；failure 是一次尝试没有达成预期结果。
- **Retry vs rollback**：retry 再次尝试动作；rollback 撤销已经发生的变更。
- **Human approval vs human handoff**：approval 是人批准后系统继续；handoff 是人接管后系统不再独立处理该部分。
- **Functional test vs production observation**：functional test 在受控条件下检验行为；production observation 查看真实运行结果。
- **Goal-directed behavior vs human intent**：目标导向行为可以由程序设定；不代表系统拥有人的意图或理解。
- **Decision-making vs human reasoning**：系统可以执行决策步骤，但这不等于复制人类思考。

## Notes

- 本文件是 Module 06 · Agents, Tools & MCP / Topic 02 的 raw glossary 收集稿，目标是最大化保留候选，不做去重、归并或最终取舍。
- 页面核心定义是：agent loop 是让 AI system take a step、observe the result、choose what to do next 的 control cycle。
- 页面明示的组成包括 goal、model decision、action、observation、stop condition；limits 和 validation 用来避免 loop continuing blindly。
- 页面主流程原样保留为五步：1 Goal / Set the objective；2 Decide / Select an action；3 Act / Call a tool；4 Observe / Read the result；5 Stop / Finish or repeat。
- 页面用导航系统作类比：follow a route、observe the road、update the next turn；道路条件变化时会更新下一步。
- Web research 案例的候选链是：question needing several sources → searches → reads results → refines the query → sourced answer or request for clarification。
- Ticket handling 案例的候选链是：support ticket → checks records → proposes an action → validates it → response, update, or human handoff。
- “What it is NOT” 的三组边界必须保留：Agent Loop ≠ One Model Call；Agent Loop ≠ Infinite Loop；Agent Loop ≠ Human Reasoning。
- 相关概念导航原文为：Goal → Decide → Tool → Observe → Decide again → Stop；相关链接是 AI Agent、Tool Calling、Failure Handling、Functional Tests。
- 页面 takeaway 的核心句是：agent loop repeats decision and action steps until a controlled stop condition is met。
- 页面正文没有给出专门的 acronym；MCP 出现在模块标题“Agents, Tools & MCP”中，AI 出现在“AI system”中。raw 阶段保留这些缩写及其展开候选，但不把页面未展开的解释当作正文事实。
- 页面没有提供数值型 metric；因此 success rate、completion rate、latency、cost 等放在 Potential Missing Concepts 和候选扩展中，不能误写成页面已定义指标。
- 页面没有明确使用 planning、memory、ReAct、LLM、state machine 等术语；这些是与页面结构高度相关的潜在补充概念，需在后续取舍阶段标注为 missing，而不是假装直接出现。
- 页面中的 action、result、system、context、task、input、output 等高频通用词被保留，因为它们在 agent loop 的定义和案例里承担了机制含义。
- raw 候选故意保留同一概念的不同粒度，例如 agent loop / repeated cycle / control cycle，以及 observation / result / tool output；后续规范化阶段再决定合并关系。
- 页面视频元素包含 independent explainer、visual explainer、captions、poster、video、English captions 等呈现层词汇；它们不是 agent loop 核心机制，但作为正文可见的重要低优先级候选保留。
- 本文件只产生 glossary-work/raw/09-agent-loop.md，不修改网站页面、脚本、媒体文件或 GitHub。
