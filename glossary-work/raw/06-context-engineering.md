# Topic

- Module: 06 · Prompting & System Design
- Topic: Context Engineering
- Source File: `context-engineering.html`
- Collection status: Raw glossary candidate collection; intentionally broad and not deduplicated or trimmed.

## Glossary Candidates

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| What Is Context Engineering? | 什么是上下文工程？ | The topic of deciding what a model should receive for a task. | 研究要给模型看什么信息、怎么给、什么时候更新。 |
| context engineering | 上下文工程 | The process of deciding what information and instructions should be available to a model for a specific task. | 为某个任务挑选和组织模型需要看到的信息与指令。 |
| context | 上下文 | Information currently supplied to a model. | 模型这一次真正拿到、可以参考的信息。 |
| information | 信息 | Facts, instructions, documents, results, or other material supplied for work. | 任务中可以被模型参考的内容。 |
| instruction | 指令 | A direction that tells the model or system what to do. | 告诉模型应该做什么、遵守什么规则的话。 |
| task | 任务 | A piece of work the model is expected to handle. | 当前希望模型完成的一件事。 |
| specific task | 特定任务 | A particular task with its own information and requirements. | 有明确目标、资料和要求的一项具体工作。 |
| task at hand | 手头任务；当前任务 | The task being handled right now. | 模型眼下正在处理的事情。 |
| model should see | 模型应该看到的内容 | The information selected for a model run. | 这一次应该放进模型输入环境里的内容。 |
| information environment | 信息环境 | The full set of information made available to a model. | 模型完成任务时所处的全部信息环境。 |
| full information environment | 完整信息环境 | All relevant instructions, data, history, tools, state, and other context for a run. | 不只是一句提示，而是模型完成任务所需的完整资料包。 |
| context assembly | 上下文组装 | Putting the selected context sources together before a model run. | 在模型运行前把需要的各种信息拼在一起。 |
| context assembly stack | 上下文组装栈 | The layered list of context sources shown before the model. | 按层列出的系统提示、用户请求、历史等上下文来源。 |
| context source | 上下文来源 | A type of information that can enter model context. | 可以为模型提供信息的一类来源。 |
| System Prompt | 系统提示 | Application-level instructions supplied to guide the model. | 应用预先给模型的高层规则和工作方式。 |
| system prompt | 系统提示词 | A prompt containing system-level guidance. | 写给模型的系统层指令。 |
| User Prompt | 用户提示 | The user’s request or instruction supplied to the model. | 用户这次交给模型的要求。 |
| user prompt | 用户提示词 | A prompt containing the user’s task request. | 用户输入的、希望模型处理的提示。 |
| prompt | 提示；提示词 | Text or instructions given to guide a model. | 告诉模型做什么的一段输入；它只是上下文的一部分。 |
| conversation history | 对话历史 | Earlier messages from the ongoing conversation. | 当前对话之前已经发生的消息。 |
| history | 历史记录 | Previous interaction information that may be supplied to the model. | 过去的对话或工作记录。 |
| Retrieved Documents | 检索到的文档 | Documents selected from an external source for the current task. | 从外部资料库找出来、交给模型参考的文档。 |
| retrieved documents / RAG | 检索文档／RAG | Retrieved documents supplied through retrieval-augmented generation. | 先找相关资料，再把资料放进模型上下文。 |
| RAG | 检索增强生成 | A method that supplies retrieved external information to generation. | 先检索资料、再让模型结合资料生成答案的方法。 |
| retrieval | 检索 | Finding relevant information from an external source. | 从资料中找出和问题相关的内容。 |
| external information | 外部信息 | Information brought in from outside the model’s immediate prompt. | 不是原提示本身，而是从外部资料、系统或工具取得的信息。 |
| knowledge | 知识 | Relevant information or source material available for a task. | 能帮助模型回答或完成任务的资料。 |
| tool result | 工具结果 | Information returned by an external tool used during a task. | 搜索、查询、计算或操作工具返回的结果。 |
| tool results | 工具结果（复数） | Results from one or more external tools. | 模型调用工具后拿到的一批结果。 |
| tool | 工具 | An external capability that can provide information or perform work. | 模型可以调用的查询、计算或操作能力。 |
| state | 状态 | The current condition of a workflow or case. | 当前流程或案件进行到哪一步、处于什么情况。 |
| current workflow state | 当前工作流状态 | The present state of the process being handled. | 当前工作流的实时进度和条件。 |
| relevant memory | 相关记忆 | Stored information selected because it matters to the current task. | 过去保存的信息中与这次任务有关的部分。 |
| memory | 记忆 | Information stored or retrievable across work. | 可以跨任务保存、以后再找回的信息。 |
| relevant stored information | 相关存储信息 | Stored information that is useful for the current model run. | 已保存、且这次确实用得上的资料。 |
| examples | 示例 | Example material supplied to help guide a model. | 给模型参考的示范案例或结果。 |
| example | 例子；示例 | A concrete case used for reference. | 用来说明应该怎么做的一个具体案例。 |
| model | 模型 | The system that processes the assembled context and produces an output. | 读取上下文、进行计算并给出结果的模型。 |
| output | 输出 | The result produced by the model after processing context. | 模型处理信息后返回的结果。 |
| model output | 模型输出 | The answer or action proposal returned by a model. | 模型最后给出的回答或行动建议。 |
| input | 输入 | Information supplied to a system or model. | 送进模型或系统的信息。 |
| output schema | 输出模式 | A required structure or format for the model’s output. | 规定模型结果应该有哪些字段、长什么格式。 |
| schema | 模式；结构定义 | A specification describing an expected structure. | 预先规定数据或输出结构的说明。 |
| relevant | 相关的 | Directly useful for the task being handled. | 和当前问题有关、能帮助完成任务。 |
| irrelevant | 不相关的 | Not useful or connected to the current task. | 和当前任务没关系、放进来只会干扰的信息。 |
| current | 当前的；最新的 | Belonging to the present task or present workflow state. | 反映现在情况，而不是过时情况。 |
| well-organized | 组织良好的 | Arranged so that the model can use the material effectively. | 资料按清楚、有用的方式排列。 |
| select | 选择 | Decide which information should be included. | 从很多资料中挑出要给模型看的部分。 |
| selecting context | 选择上下文 | Choosing the context sources and items for a model run. | 决定这一次哪些内容进入模型。 |
| selection | 选择；筛选 | The act of choosing useful information and excluding the rest. | 挑相关资料、排除无关资料的动作。 |
| organize information | 组织信息 | Arrange information in a useful order or structure. | 把资料按模型容易使用的方式整理好。 |
| information organization | 信息组织 | The structure and ordering used for supplied context. | 上下文中资料的排列和结构。 |
| context refresh | 上下文刷新 | Updating the supplied context when information changes. | 情况变化时重新更新模型看到的资料。 |
| refresh context | 刷新上下文 | Replace or update context for a new or changed state. | 让模型重新看到最新的相关信息。 |
| context inclusion | 上下文纳入 | Putting a piece of information into the model’s context. | 把一项资料放进模型可见范围。 |
| context exclusion | 上下文排除 | Keeping a piece of information out of the model’s context. | 不把某项资料交给模型。 |
| should enter | 应该进入 | The question of what belongs in the context. | 哪些内容应该放进模型输入。 |
| should stay out | 应该留在外面 | The question of what should be excluded. | 哪些内容不应该让模型看到。 |
| relevant material | 相关材料 | Material that helps the current decision or task. | 真正有助于当前任务的资料。 |
| decision | 决策 | A choice made using available information. | 根据资料做出的选择。 |
| briefing folder | 简报文件夹 | The human-facing analogy for a prepared set of decision material. | 像给决策者准备的一份资料夹。 |
| briefing folder analogy | 简报文件夹类比 | An analogy for assembling relevant material before a decision. | 用“决策前准备资料夹”帮助理解上下文组装。 |
| decision material | 决策资料 | Information prepared to support a decision. | 为了做判断而提前整理的资料。 |
| preparing a briefing folder | 准备简报文件夹 | Preparing relevant, current, organized material before a decision. | 决策前把相关、最新、整理好的材料准备好。 |
| relevant and current | 相关且最新 | Both useful for the task and up to date. | 既有关联，又没有过时。 |
| missing context | 缺失上下文 | Needed information that was not supplied to the model. | 模型需要、但这次没有提供的信息。 |
| irrelevant context | 不相关上下文 | Supplied material that does not help the current task. | 虽然放进来了，但和任务无关的资料。 |
| missing / irrelevant context | 缺失／不相关上下文 | Context that is incomplete or includes distracting material. | 该有的没给，或给了太多无关资料。 |
| weak answer | 较弱回答 | An answer harmed by missing or irrelevant information. | 因资料不足或不对而不够好的回答。 |
| uninformed answer | 缺乏信息支持的回答 | An answer produced without the needed information. | 模型没有关键资料时给出的回答。 |
| relevant instructions | 相关指令 | Instructions that apply to the current task. | 和当前任务直接有关的规则。 |
| policy | 政策；规则 | An organizational rule used to guide a decision. | 公司或组织规定的处理原则。 |
| relevant policy | 相关政策 | The policy that applies to the current question or case. | 当前问题真正适用的规定。 |
| task-specific response | 任务特定响应 | A response shaped for the current task and its context. | 针对眼前任务定制的回答。 |
| usefulness | 有用性 | How much a response helps the user or task. | 结果对解决问题有多大帮助。 |
| correctness | 正确性 | Whether the response is factually or procedurally right. | 结果是否正确。 |
| guarantee correctness | 保证正确性 | Ensure that a response is always correct. | 让答案百分之百正确；页面明确说相关上下文不能保证这一点。 |
| instructions source | 指令来源 | The part of context containing system and user instructions. | 上下文中放规则和请求的来源类别。 |
| history source | 历史来源 | The part of context containing conversation history. | 上下文中放过去对话的来源类别。 |
| knowledge source | 知识来源 | The part of context containing RAG or retrieved documents. | 上下文中放外部资料的来源类别。 |
| tools source | 工具来源 | The part of context containing tool results. | 上下文中放工具返回结果的来源类别。 |
| state source | 状态来源 | The part of context containing current workflow state. | 上下文中放当前流程状态的来源类别。 |
| memory source | 记忆来源 | The part of context containing relevant stored information. | 上下文中放相关记忆的来源类别。 |
| prompt design | 提示设计 | Designing the wording of an instruction to a model. | 研究一句提示应该怎么写。 |
| Prompt Design vs Context Engineering | 提示设计与上下文工程 | A comparison between wording one instruction and designing the whole information environment. | 前者关注怎么写提示，后者关注模型完整接收什么。 |
| instruction wording | 指令措辞 | The way an instruction is written. | 具体用哪些话告诉模型做事。 |
| full context | 完整上下文 | The prompt plus rules, documents, policies, results, history, and schema. | 不只一句提示，而是完成任务所需的全套资料。 |
| “Check this invoice” | “检查这张发票” | A short example of a user prompt. | 只有一句要求、资料很少的提示示例。 |
| system rules | 系统规则 | Rules supplied by the application or system. | 系统要求模型始终遵守的规则。 |
| invoice | 发票；账单 | A document used as the object of a checking task. | 需要被检查的业务单据。 |
| policy document | 政策文档 | A document describing applicable organizational policy. | 说明公司规定的文档。 |
| context window | 上下文窗口 | The amount of information that can fit in a model’s context. | 模型一次能装下多少输入信息的容量。 |
| capacity constraint | 容量约束 | A limit on how much information can fit. | 上下文能放多少内容的上限。 |
| container capacity | 容器容量 | The amount a context container can hold. | 把上下文看成容器时，它能装下的容量。 |
| design decision | 设计决策 | A choice about what to include in context. | 设计者决定哪些资料应该被放进去。 |
| context-window capacity | 上下文窗口容量 | The maximum context capacity available to the model. | 模型这次最多能接收多少上下文。 |
| context window vs context engineering | 上下文窗口与上下文工程 | Capacity is different from the choice of what to put inside. | 窗口是“能装多少”，工程是“选择装什么”。 |
| memory vs context | 记忆与上下文 | Stored or retrievable information differs from information currently supplied. | 保存过的东西不等于模型这次已经看到。 |
| stored information | 已存储信息 | Information kept for possible later retrieval. | 系统保存起来、以后可能再取出的资料。 |
| retrievable information | 可检索信息 | Information that can be found and selected when needed. | 需要时能够被找回的信息。 |
| current model run | 当前模型运行 | One execution of a model with its supplied context. | 模型这一次实际执行的过程。 |
| model run | 模型运行 | A single processing pass that produces an output. | 模型读取输入并产生结果的一次执行。 |
| retrieve / select | 检索／选择 | Find stored information and choose what enters context. | 先找出来，再挑真正相关的内容。 |
| memory helps | 记忆发挥作用 | Memory helps only when relevant information becomes available to the current run. | 记忆只有被取出并给当前模型时才有用。 |
| customer 123 | 客户 123 | The customer identifier in the refund example. | 示例中要查询退款资格的客户编号。 |
| refund | 退款 | Money returned under applicable policy and case conditions. | 按规则把钱退还给客户。 |
| refund eligibility | 退款资格 | Whether a customer is allowed to receive a refund. | 判断客户是否符合退款条件。 |
| policy question | 政策问题 | A question whose answer depends on rules or policy. | 需要查规定才能回答的问题。 |
| order status | 订单状态 | The result or condition of the customer’s order. | 订单现在是已下单、已发货、已取消等什么状态。 |
| case status | 案件状态 | The current status of the customer case or workflow. | 当前案件处理到哪一步。 |
| current case status | 当前案件状态 | The up-to-date state of the refund case. | 这次退款案件最新的处理状态。 |
| answer / action proposal | 回答／行动提案 | A model response or proposed next action. | 模型给出的说明，或建议接下来做什么。 |
| action proposal | 行动提案 | A suggested action generated after reviewing context. | 模型根据资料建议执行的一步。 |
| irrelevant conversation | 无关对话 | Conversation history unrelated to the current case. | 和本次任务没有关系的旧对话。 |
| unrelated documents | 无关文档 | Documents that do not support the current task. | 与当前问题无关的资料。 |
| unnecessary sensitive information | 不必要的敏感信息 | Sensitive material that is not needed for the task. | 任务不需要、却可能带来隐私风险的资料。 |
| sensitive information | 敏感信息 | Information that should not be exposed without a task need. | 不应随便提供或传播的个人、业务等信息。 |
| right information | 正确信息；合适信息 | Information relevant and necessary for the current task. | 真正需要、而且适合这次任务的资料。 |
| selecting the right information | 选择合适信息 | Choosing necessary context instead of merely adding more. | 重点是挑对资料，不是把资料越加越多。 |
| longer prompt | 更长的提示 | A prompt with more words or instructions. | 字数更多的提示；长不代表一定更好。 |
| more context | 更多上下文 | A larger amount of supplied information. | 放进模型的资料更多；多不代表更相关。 |
| relevant context | 相关上下文 | Context that helps with the current task. | 对眼前问题有帮助的上下文。 |
| context volume | 上下文数量 | The amount of information supplied. | 一次提供给模型的资料量。 |
| method | 方法 | A way to supply or shape information for a model. | 达成上下文目标的一种做法。 |
| external-information method | 外部信息提供方法 | A method such as RAG for bringing outside knowledge into context. | 把外部资料交给模型的一种机制。 |
| stored information is not automatically visible | 已存信息不会自动可见 | Stored memory is not automatically part of the current model run. | 系统保存过，不表示模型此刻就能看到。 |
| related concepts | 相关概念 | Concepts connected to context engineering. | 和上下文工程相邻、互相配合的概念。 |
| system prompts | 系统提示词 | Application guidance supplied at the system level. | 应用给模型的高层指导。 |
| Memory & State | 记忆与状态 | Stored information and current workflow information. | 过去保存的资料与当前流程情况。 |
| structured outputs | 结构化输出 | Outputs constrained to a requested structure or schema. | 按规定字段或格式返回的结果。 |
| structured output | 结构化结果 | A model result organized according to a schema. | 按固定结构生成的回答。 |
| shape instruction | 塑造指令 | Guide how an instruction is formed. | 让提示更清楚、更能引导模型。 |
| retrieve knowledge | 检索知识 | Find useful external information for the model. | 从外部资料中找到模型需要的知识。 |
| stored information and current information | 存储信息与当前信息 | The two kinds of information represented by memory and state. | 过去留下来的资料与眼下实时情况。 |
| model context as a container | 作为容器的模型上下文 | A way to think of the context window as holding selected material. | 把模型上下文想成一个装资料的容器。 |
| context as selected contents | 作为已选内容的上下文 | The material chosen to place inside the capacity. | 容器里实际挑进去的东西。 |
| independent explainer | 独立讲解资源 | A separate explanatory resource linked to the topic. | 不是正文主体、用来辅助解释的内容。 |
| visual explainer | 可视化讲解 | An explanation presented visually. | 用图或视频帮助理解概念。 |
| real resource | 真实资源 | An actual external resource rather than a placeholder. | 真正存在、可以使用的外部内容。 |
| no video resource added | 未添加视频资源 | The page currently has no actual video resource. | 页面这里只是占位，并没有真正的视频。 |

## Potential Missing Concepts

- **context management（上下文管理）**：正文描述选择、组织和刷新，但没有单独定义持续管理上下文的工程实践。
- **context orchestration（上下文编排）**：页面讲了多个来源汇入模型，但没有使用“编排”这个系统设计术语。
- **context pipeline（上下文流水线）**：上下文来源、筛选、组装、模型运行和输出可以形成流水线，正文未单独命名。
- **context budget（上下文预算）**：页面提到窗口容量约束，但没有解释如何在不同来源之间分配容量。
- **token budget（词元预算）**：context window 的工程容量通常按 token 计算，正文没有提到 token。
- **truncation（截断）**：当上下文超过容量时如何删除或截短内容，正文未说明。
- **compression（压缩）**：在有限窗口内压缩历史或文档的方法，正文未展开。
- **summarization（摘要化）**：缩短对话历史或资料以保留重点的方法，正文未定义。
- **context prioritization（上下文优先级排序）**：页面问“什么应该进入”，但没有定义不同资料的优先级规则。
- **recency（新近性）**：页面要求 current，但没有具体说明按时间新旧选择资料。
- **relevance scoring（相关性评分）**：页面强调 relevant，但没有说明如何计算或排序相关性。
- **source attribution（来源归因）**：Retrieved Documents 和 policy 出现，但没有说明如何把回答绑定到来源。
- **provenance（来源链；可追溯性）**：没有定义上下文中每条资料的来源和处理历史。
- **access control（访问控制）**：页面提醒不要放不必要的敏感信息，但没有说明谁能让哪些内容进入上下文。
- **data minimization（数据最小化）**：示例明确排除不必要敏感信息，但未使用这一隐私工程术语。
- **privacy filtering（隐私过滤）**：没有说明在上下文组装前如何识别和遮蔽敏感信息。
- **prompt injection（提示注入）**：页面讨论上下文来源，但未说明检索文档或用户内容可能包含恶意指令。
- **instruction hierarchy（指令层级）**：System Prompt、User Prompt 和工具结果都出现，但未说明冲突时的优先级。
- **conflict resolution（冲突处理）**：没有介绍多个上下文来源互相矛盾时如何裁决。
- **context poisoning（上下文污染）**：未讨论错误、恶意或过时内容进入上下文的问题。
- **stale context（过时上下文）**：页面问何时刷新，但没有具体定义过期信息的检测。
- **context caching（上下文缓存）**：没有介绍重复上下文的缓存与复用。
- **context observability（上下文可观测性）**：没有介绍如何记录一次模型运行实际收到的上下文。
- **context tracing（上下文追踪）**：没有说明如何追踪一项资料从检索到输出的路径。
- **evaluation set（评估集）**：页面提到 usefulness 和 correctness，但没有定义用来评估上下文策略的数据集。
- **context quality metric（上下文质量指标）**：正文没有命名 precision、recall、coverage 或其他上下文质量指标。
- **grounding（基于资料约束）**：RAG 和 retrieved documents 出现，但没有单独解释输出如何受来源约束。
- **citation（引用）**：页面提到资料和政策，但没有说明如何在输出中给出引用。
- **tool calling（工具调用）**：Tool Results 出现，但没有说明模型如何决定调用工具、传参和接收结果。
- **workflow state machine（工作流状态机）**：State 出现，但没有展开状态转换和合法转移。
- **episodic memory（情节记忆）**：Memory 只作一般概念，没有区分记忆类型。
- **semantic memory（语义记忆）**：没有说明保存的事实知识与对话事件记忆的区别。
- **working memory（工作记忆）**：Context 与 Memory 有对照，但没有使用工作记忆来解释当前运行内容。
- **long-term memory（长期记忆）**：页面谈跨工作存储，却没有单独定义长期记忆。
- **short-term memory（短期记忆）**：没有将当前对话或当前上下文与短期记忆区分开。
- **state persistence（状态持久化）**：State 出现，但没有解释跨运行保存工作流状态。
- **structured context（结构化上下文）**：页面提到组织信息和 schema，但未定义上下文本身的结构化设计。
- **context template（上下文模板）**：没有说明如何用模板稳定组装不同任务的上下文。
- **dynamic context（动态上下文）**：页面问何时刷新，但没有定义随任务变化实时生成上下文。
- **static context（静态上下文）**：System Prompt 等较稳定内容出现，但未单独与动态来源比较。
- **multi-turn context（多轮上下文）**：Conversation History 出现，但没有展开多轮对话上下文的保留策略。
- **context drift（上下文漂移）**：没有讨论长对话中目标、状态或相关性逐渐变化。
- **lost in the middle（中间信息丢失）**：没有讨论长上下文中位置影响造成的信息利用问题。
- **context-aware system（上下文感知系统）**：正文描述系统根据当前资料响应，但没有给出该系统类别名称。
- **decision support（决策支持）**：简报文件夹类比涉及决策，但没有正式定义 AI 决策支持。
- **human approval gate（人工批准关卡）**：action proposal 出现，但没有规定哪些行动必须人工批准。
- **audit trail（审计轨迹）**：政策、工具结果和案件状态出现，但没有说明如何留存决策依据。
- **latency（延迟）**：刷新、检索和工具结果可能影响速度，正文没有讨论性能时间。
- **cost（成本）**：更多上下文通常影响计算成本，但正文没有讨论资源或费用。
- **context-window overflow（上下文窗口溢出）**：页面说容量约束，却没有描述超出容量时的失败状态。
- **least privilege（最小权限）**：不必要敏感信息被排除，但没有把它表述为权限原则。
- **data freshness（数据新鲜度）**：current 被强调，但没有定义资料更新时间或新鲜度阈值。
- **policy enforcement（政策执行）**：相关政策进入上下文，但没有说明模型遵守政策的验证和执行机制。
- **structured output validation（结构化输出校验）**：Structured Outputs 作为相关概念出现，但没有说明结果如何被验证。

## Aliases / Synonyms

- context engineering ↔ Context Engineering ↔ 上下文工程 ↔ deciding what the model should see
- context ↔ model context ↔ supplied context ↔ current context ↔ 上下文
- context assembly ↔ context assembly stack ↔ assembling context ↔ 上下文组装
- information environment ↔ full information environment ↔ model’s information environment ↔ 信息环境
- System Prompt ↔ system prompt ↔ system-level instructions ↔ application guidance
- User Prompt ↔ user prompt ↔ user request ↔ user instruction
- prompt ↔ prompt design input ↔ instruction prompt ↔ 提示／提示词
- Conversation History ↔ conversation history ↔ history ↔ previous messages
- Retrieved Documents ↔ retrieved documents ↔ external documents ↔ retrieved knowledge
- Tool Results ↔ tool results ↔ tool output ↔ external tool result
- State ↔ current workflow state ↔ current case status ↔ workflow state
- Relevant Memory ↔ relevant memory ↔ relevant stored information ↔ selected memory
- Examples ↔ examples ↔ example material ↔ demonstrations
- output ↔ model output ↔ response ↔ answer
- full context ↔ complete context ↔ context environment ↔ 完整上下文
- relevant information ↔ relevant context ↔ right information ↔ necessary information
- irrelevant information ↔ irrelevant context ↔ unrelated material ↔ distracting context
- context selection ↔ selecting context ↔ information selection ↔ 上下文筛选
- organize information ↔ information organization ↔ context organization ↔ 组织上下文
- context refresh ↔ refresh context ↔ context update ↔ 更新上下文
- briefing folder ↔ briefing-folder analogy ↔ prepared decision material ↔ 简报资料夹类比
- usefulness ↔ utility ↔ task usefulness ↔ 有用性
- correctness ↔ accuracy of response ↔ response correctness ↔ 正确性（页面只明确讨论 correctness，不给出具体准确率定义）
- context window ↔ context-window capacity ↔ container capacity ↔ 上下文容量
- design decision ↔ inclusion decision ↔ what-to-include decision ↔ 纳入设计决策
- memory ↔ stored information ↔ retrievable information ↔ 记忆／存储信息
- current model run ↔ current run ↔ one model execution ↔ 当前模型运行
- retrieve / select ↔ retrieval and selection ↔ find and choose ↔ 检索／选择
- refund question ↔ “Can customer 123 receive a refund?” ↔ refund eligibility question ↔ 退款资格问题
- order status ↔ tool result about order status ↔ 订单状态结果
- action proposal ↔ proposed action ↔ answer / action proposal ↔ 行动建议
- longer prompt ↔ more words in the prompt ↔ 长提示
- more context ↔ larger context volume ↔ more supplied information
- RAG ↔ retrieval-augmented generation ↔ 检索增强生成（但 RAG 只是供给外部信息的一种方法，不等于整个上下文工程）
- structured outputs ↔ structured output ↔ schema-shaped output ↔ 结构化输出
- prompt design ↔ designing the instruction ↔ how to write the instruction ↔ 提示设计
- context engineering ↔ designing the full information environment ↔ what full information should the model receive

## Do Not Confuse Candidates

- **Context Engineering vs Prompt Design**：Prompt Design 关注“指令应该怎么写”；Context Engineering 关注模型完整接收什么信息环境。Prompt 是上下文的一部分，不是全部上下文。
- **Context Engineering vs Context Window**：Context Engineering 是决定纳入什么的设计决策；Context Window 是能容纳多少信息的容量约束。
- **Context vs Memory**：Context 是当前已经提供给模型的信息；Memory 是跨工作存储或可检索的信息。记忆只有被检索、选择并送入当前运行才会成为上下文。
- **Memory vs State**：Memory 主要是存储或可找回的信息；State 是当前工作流或案件处于什么状态。
- **Context vs Context Window**：上下文是容器内实际装入的内容；上下文窗口是容器本身的容量。
- **RAG vs Context Engineering**：RAG 是把外部知识带入上下文的一种方法；上下文工程还包括系统指令、用户提示、历史、工具结果、状态、记忆和示例等选择与组织。
- **Retrieved Documents vs Conversation History**：检索文档来自外部知识源；对话历史来自当前或之前的对话。
- **Tool Results vs Retrieved Documents**：工具结果是外部工具返回的信息；检索文档是从资料源找回的文档内容，二者可能都进入上下文但来源不同。
- **System Prompt vs User Prompt**：System Prompt 提供应用层指导；User Prompt 表达用户当前请求。
- **User Prompt vs Input**：User Prompt 是一种输入；输入也可以是文档、发票、工具结果或其他数据。
- **More Context vs Better Context**：更多资料不自动等于更好；相关、当前、组织良好的资料比单纯增加数量更重要。
- **Longer Prompt vs Better Prompt**：提示更长不自动带来更好结果；关键是清楚且与任务相关。
- **Relevant Context vs Correctness**：相关上下文可以提升有用性，但不能保证回答正确。
- **Relevant vs Current**：Relevant 表示和任务有关；Current 表示反映当前情况，相关但过时的资料仍可能误导。
- **Stored Information vs Visible Information**：信息被系统存储不等于当前模型运行已经看到了它。
- **Memory vs Context Refresh**：记忆是可供找回的存储；刷新是把最新、相关信息重新提供给当前运行。
- **Policy vs System Rules**：政策可能是被检索进来的业务规则；系统规则通常是应用层直接提供给模型的指导，两者在示例中都是上下文来源。
- **Answer vs Action Proposal**：Answer 是对问题的响应；Action Proposal 是建议接下来采取什么行动，示例把两者并列为输出形式。
- **Current Case Status vs Order Status**：Order Status 是订单这条业务数据；Current Case Status 是退款案件或工作流当前进度。
- **Unrelated Documents vs Unnecessary Sensitive Information**：前者是不相关、会干扰任务的资料；后者即使可能相关，也可能是任务不需要暴露的敏感资料。
- **Context Engineering vs Adding More Information**：上下文工程不是不断添加信息，而是选择正确的信息并排除无关内容。
- **Structured Outputs vs Context Engineering**：Structured Outputs 关注模型输出的结构；Context Engineering 关注模型收到的完整输入环境。
- **Model vs Product**：Model 处理上下文并生成结果；Product 还可能包含界面、规则、数据、工具和运营。
- **Context Assembly vs Model Inference**：Context Assembly 是运行前准备输入；Model 是接收组装后的上下文并产生输出的处理者。
- **Briefing Folder vs Actual Model Context**：简报文件夹只是帮助理解的类比；模型上下文是在推理时实际提供的结构化信息。
- **Independent Explainer vs Core Context Source**：页面的 Independent Explainer / Video 是辅助说明资源，不是退款示例中的核心上下文来源。
- **RAG vs Memory**：RAG 通常强调为当前任务检索外部知识；Memory 强调跨工作保存或可检索的信息，两者可能都要经过选择才进入上下文。
- **History vs Memory**：History 是对话记录；Memory 是跨工作保存或检索的相关信息，二者在系统中可能有交集但不是同一概念。

## Notes

- 本文件是 Module 06 Topic “Context Engineering”的 raw glossary 收集稿；目标是最大化保留正文中出现或由正文直接引出的候选，不做最终去重、归并或取舍。
- 已完整覆盖页面正文的主要结构：定义与 lede、On this page 导航、Context Assembly、briefing folder 类比、Why Context Matters、Sources of Context、Prompt Design 对比、Context Window 对比、Context vs Memory、退款示例、What It Is NOT、Related Concepts、Remember This 和 Video 占位区。
- 页面给出的核心上下文栈按原顺序是：System Prompt、User Prompt、Conversation History、Retrieved Documents / RAG、Tool Results、State、Relevant Memory、Examples；这些词全部单独保留为候选。
- 页面明确提出四个上下文设计问题：WHAT should enter、WHAT should stay out、HOW should information be organized、WHEN should context be refreshed；相关疑问短语也作为候选保留。
- 页面把上下文比作 decision 前的 briefing folder，但同时特别说明这只是理解类比；模型上下文是 inference 时提供的 structured information。
- 页面关于质量的表述是：Relevant context can improve usefulness, but does not guarantee correctness。正文没有列出 accuracy、precision、recall、F1 等具体数值指标，因此未把这些指标伪装成页面原文概念，而是放入 Potential Missing Concepts。
- “Sources of Context” 明确分为 Instructions、History、Knowledge、Tools、State、Memory；其中 Instructions 包含 System Prompt / User Prompt，Knowledge 包含 RAG / Retrieved Documents。
- “Prompt Design vs Context Engineering” 的关键边界是：Prompt 只是 Full Context 的一个部分；示例 Full context = System Rules + Invoice + Policy + Tool Results + History + Output Schema。
- “Context Engineering vs Context Window” 的关键边界是：Context Window = container capacity；Context Engineering = what you choose to put inside。
- “Context vs Memory” 的关键边界是：Memory 是 stored or retrievable across work 的信息；Context 是 currently supplied to the model 的信息；Memory 只有 retrieve / select 后才能帮助当前 model run。
- 退款示例的原始上下文候选包括：System Rules、User Request — Customer 123、Retrieved Policy、Tool Result — order status、State — current case status；输出是 Answer / action proposal。
- 退款示例明确列出 DO NOT INCLUDE：irrelevant conversation、unrelated documents、unnecessary sensitive information；这些既是术语，也是上下文排除规则。
- “What It Is NOT” 明确否定四个等同关系：Context Engineering 不等于 Longer Prompt、不等于 More Context、不等于 RAG、不等于 Memory。
- “Related Concepts” 通过链接关联 Prompt Design、System Prompts、Context Window、RAG、Memory & State 和 Structured Outputs；这些概念作为页面明示的邻接候选保留。
- 页面没有实际视频资源，Video 区只写有 independent explainer、visual explainer 和 no video resource added；这些是页面呈现语境词，不应误认成上下文工程核心机制。
- 正文没有单独命名 quantitative metrics；本 raw 文件仅保留页面实际使用的 qualitative terms（usefulness、correctness、relevant、current、well-organized、capacity constraint），并在 Potential Missing Concepts 补列可能的工程指标与机制。
- 同一个词的大小写、单复数、短语变体和页面中的不同位置在 raw 阶段有意保留；后续规范化阶段再决定是否合并。
