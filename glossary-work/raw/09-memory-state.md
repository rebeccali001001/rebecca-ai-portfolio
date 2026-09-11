# Topic

Memory & State

## Topic Metadata

- Module: 09 · Agents, Tools & MCP
- Topic: Memory & State
- Topic Number: 06
- Source Page Context: 09 · Agents, Tools & MCP · Topic 06 (as shown in the HTML)
- Source File: `memory-state.html`
- Source Title: What are Memory and State in an AI Agent?
- Source Description: State tracks what is happening in the current task, while memory can preserve useful information across steps or interactions.
- Raw-stage policy: Maximum candidate inventory; retain overlapping, repeated, surface-form, alias, and potentially confusable candidates for later normalization.

## Glossary Candidates

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Memory & State | 记忆与状态 | The pair of mechanisms used to track current work and retain useful information. | 一起说明“现在进行到哪儿”和“以后还能记住什么”的两个概念。 |
| Memory and state | 记忆和状态 | Ways an AI agent keeps track of information while it works and across interactions. | AI 智能体在工作中以及多次互动之间保存和跟踪信息的方式。 |
| Memory | 记忆 | Information retained or retrieved beyond the immediate step. | 不只在当前一步使用、还能保存或取回的信息。 |
| memory | 记忆 | Lowercase wording for memory. | “Memory”的小写写法。 |
| State | 状态 | Current task information. | 当前任务正在发生的情况和信息。 |
| state | 状态 | Lowercase wording for state. | “State”的小写写法。 |
| Context | 上下文 | Information physically or logically available for the current step. | 当前这一步能直接看到、使用的背景信息。 |
| context | 上下文 | Lowercase wording for context. | “Context”的小写写法。 |
| Context Window | 上下文窗口 | What the model can currently see. | 模型此刻能够看到和处理的信息范围。 |
| context window | 上下文窗口 | The information visible to the model right now. | 模型现在可见的信息空间。 |
| Context Window ≠ Memory | 上下文窗口不等于记忆 | Context is visible now, while memory is stored for later. | 上下文是现在看得到的，记忆是保存起来以后再用的。 |
| Memory ≠ Context Window | 记忆不等于上下文窗口 | Memory is stored for later; context is visible now. | 记忆留给以后使用；上下文是当前能看到的内容。 |
| Memory ≠ State | 记忆不等于状态 | Memory can persist; state tracks current progress. | 记忆可以保留下来，状态记录当前进度。 |
| Memory ≠ Model Parameters | 记忆不等于模型参数 | Memory is external information; parameters are learned values. | 记忆是外部保存的信息，参数是模型学到的数值。 |
| AI agent | AI 智能体 | An agent that keeps track of information while it works and across interactions. | 能在工作时跟踪信息、并在互动之间保留信息的 AI 系统。 |
| AI Agent | AI 智能体 | Capitalized wording for an AI agent. | “AI agent”的首字母大写写法。 |
| agent | 智能体 | Short form for an AI agent in this page context. | “AI agent”的简称。 |
| information | 信息 | Facts or task details tracked, stored, or retrieved by the agent. | 智能体跟踪、保存或取回的事实和任务细节。 |
| keep track of information | 跟踪信息 | Maintain awareness of information while working. | 在工作过程中持续记录和掌握信息。 |
| track information | 跟踪信息 | Follow information as the task progresses. | 随任务推进记录信息的变化。 |
| keep track | 持续跟踪 | Continue recording what matters during a task. | 持续记下当前任务中重要的内容。 |
| while it works | 工作期间 | During the agent's active work. | 智能体正在执行任务的这段时间。 |
| across interactions | 跨互动 | Over more than one interaction or exchange. | 不只限于一次交流，而是跨多次交流。 |
| interaction | 互动 | An exchange in which the agent works with a user or system. | 智能体和用户或系统之间的一次交流。 |
| current task | 当前任务 | The task being worked on now. | 当前正在处理的工作。 |
| current task information | 当前任务信息 | Information about the task in progress. | 关于正在进行任务的信息。 |
| immediate step | 当前一步 | The single step that is happening now. | 当前正在执行的一个步骤。 |
| beyond the immediate step | 超出当前一步 | Information usable after the present step. | 当前步骤结束后仍可能使用的信息。 |
| retained information | 保留的信息 | Information kept for later use. | 保存下来、以后还可以使用的信息。 |
| retrieved information | 取回的信息 | Information brought back when it is needed. | 需要时从存储中重新拿回的信息。 |
| retain | 保留 | Keep information available beyond the current step. | 让信息不只在当前一步存在。 |
| retrieve | 取回；检索 | Bring stored information back for current use. | 把之前保存的信息拿回来使用。 |
| preserve | 保存；保留 | Keep selected information for later. | 把选中的信息留给以后使用。 |
| persist | 持续存在 | Continue to exist after the current step or task moment. | 当前步骤结束后信息仍然存在。 |
| persistence | 持久性 | The ability of information to remain available over time. | 信息能跨时间保留下来的特性。 |
| useful information | 有用信息 | Information that may help the agent later. | 以后可能帮助完成任务的信息。 |
| selected facts | 选定的事实 | Facts chosen as worth saving. | 被挑出来、认为值得保存的事实。 |
| fact | 事实 | A piece of information selected for possible later use. | 以后可能用得上的一条信息。 |
| save information | 保存信息 | Store information that may help later. | 把以后可能有帮助的信息存下来。 |
| help later | 以后有帮助 | Be useful in a later step or interaction. | 在后续步骤或交流中派上用场。 |
| current context | 当前上下文 | The context available during the current step. | 当前这一步可以使用的上下文。 |
| retrieved context | 取回的上下文 | Relevant memory brought into the current context. | 从记忆中取回、放进当前上下文的相关信息。 |
| bring memory into context | 把记忆带入上下文 | Add relevant stored information to what is currently available. | 把相关记忆加入当前可见的信息。 |
| relevant memory | 相关记忆 | Stored information that helps with the current task. | 对当前任务有帮助的已保存信息。 |
| current progress | 当前进度 | How far the present task has progressed. | 当前任务已经做到哪一步。 |
| track current progress | 跟踪当前进度 | Record and follow the task's progress. | 记录并持续了解任务进展。 |
| current task progress | 当前任务进度 | Progress of the task being performed now. | 正在执行的任务的进展情况。 |
| notes | 笔记；记录 | Information currently written down for active work. | 为当前工作写下来的记录。 |
| notes currently open | 当前打开的笔记 | Notes available on the desk right now in the analogy. | 类比中此刻摊开放在桌面上的笔记。 |
| open notes | 打开的笔记 | Notes immediately available for use. | 现在可以直接查看的笔记。 |
| desk | 桌面 | The analogy's surface representing current availability. | 类比中代表“当前可见范围”的桌面。 |
| notebook | 笔记本 | The analogy's object representing retained memory. | 类比中代表可长期保存信息的笔记本。 |
| filing cabinet | 文件柜 | The analogy's object representing stored memory. | 类比中代表把资料存起来以后再找的文件柜。 |
| notes currently open on your desk | 桌面上当前打开的笔记 | An analogy for state. | 用桌面上打开的笔记来比喻当前状态。 |
| notebook or filing cabinet | 笔记本或文件柜 | An analogy for memory. | 用笔记本或文件柜来比喻可保存的记忆。 |
| information physically available on the desk | 桌面上物理可见的信息 | An analogy for context. | 用桌面上眼前可见的信息来比喻上下文。 |
| analogy | 类比 | A comparison used to make memory, state, and context easier to understand. | 用熟悉的东西帮助理解抽象概念。 |
| Think of it like... | 可以把它想成…… | The page's analogy section. | 页面用类比解释概念的部分。 |
| task | 任务 | A piece of work the agent is carrying out. | 智能体要完成的一件工作。 |
| Task | 任务 | The task node in the related-concepts chain. | 关联概念链条中的“任务”节点。 |
| Task Starts | 任务开始 | The first stage of the page's process. | 页面流程的第一阶段。 |
| task start | 任务开始 | The point at which a task begins. | 任务正式启动的时刻。 |
| create state | 创建状态 | Record the goal and current task information when a task starts. | 任务开始时记录目标和当前任务信息。 |
| Create State | 创建状态 | The first named operation in the process. | 流程中的第一个操作：建立当前状态记录。 |
| create state step | 创建状态步骤 | The process step that initializes state. | 初始化状态的流程步骤。 |
| record the goal | 记录目标 | Write down what the task is trying to achieve. | 记下这项任务想要达到什么结果。 |
| goal | 目标 | The intended result recorded at task start. | 任务一开始就记录的想要达成的结果。 |
| record current task information | 记录当前任务信息 | Save the details of the task in progress. | 把正在进行的任务详情记录下来。 |
| Agent Acts | 智能体行动 | The second stage of the page's process. | 页面流程的第二阶段。 |
| agent acts | 智能体行动 | The agent takes a step during the task. | 智能体在任务中执行一步行动。 |
| act | 行动 | Take a step in the current task. | 在当前任务中执行一个步骤。 |
| take a step | 采取一步行动 | Perform one action in the workflow. | 在工作流程中完成一个动作。 |
| update state | 更新状态 | Record the result after the agent takes a step. | 智能体行动后把结果记入状态。 |
| Update State | 更新状态 | The second named operation in the process. | 流程中的第二个操作：更新当前状态记录。 |
| update current state | 更新当前状态 | Change the task record to reflect the latest action and result. | 根据最新行动和结果修改任务记录。 |
| action result | 行动结果 | The result produced by a step the agent takes. | 智能体执行一步后得到的结果。 |
| record its result | 记录其结果 | Save the result of the agent's step in state. | 把智能体这一步的结果记录到状态中。 |
| result | 结果 | The outcome of an action or task step. | 一个动作或任务步骤产生的结果。 |
| Store Useful Information | 保存有用信息 | The third stage of the page's process. | 页面流程的第三阶段。 |
| store useful information step | 保存有用信息步骤 | The process step that selects information for later use. | 挑选信息并为后续使用保存下来的流程步骤。 |
| store | 存储；保存 | Keep selected information for later retrieval. | 把选中的信息存起来，以后可以取回。 |
| preserve selected facts | 保留选定事实 | Save facts likely to help later. | 保存以后可能有帮助的事实。 |
| likely to help later | 可能有助于后续 | Having a reasonable chance of being useful in a later step. | 以后步骤中可能派上用场。 |
| Retrieve Memory | 取回记忆 | The fourth stage of the page's process. | 页面流程的第四阶段。 |
| retrieve memory step | 取回记忆步骤 | Bring relevant memory into the current context. | 把相关记忆带回当前上下文的流程步骤。 |
| Continue | 继续 | Proceed after relevant memory is retrieved. | 取回相关记忆后继续任务。 |
| continue | 继续 | Move on with the task after updating available information. | 更新可用信息后继续完成任务。 |
| bring relevant memory into the current context | 把相关记忆带入当前上下文 | Retrieve useful stored information for the current task. | 把当前任务需要的已保存信息取回来。 |
| process | 流程；过程 | The ordered way memory and state are handled during a task. | 任务中处理状态和记忆的一连串步骤。 |
| process flow | 流程图；流程 | The page's ordered four-step sequence. | 页面展示的四步有序流程。 |
| step | 步骤 | One stage or action in the process. | 流程中的一个阶段或动作。 |
| four-step process | 四步流程 | Task Starts, Agent Acts, Store Useful Information, Retrieve Memory. | 任务开始、智能体行动、保存有用信息、取回记忆四步。 |
| current task information → selected facts → current context | 当前任务信息→选定事实→当前上下文 | A compressed view of recording, storing, and retrieving information. | 把记录、保存、取回信息压缩成的一条流程线。 |
| Real-world examples | 现实世界例子 | Examples showing how state and memory work in practical situations. | 用实际场景说明状态和记忆如何工作。 |
| real-world example | 现实世界示例 | A practical example used on the page. | 页面上的实际使用场景。 |
| Everyday | 日常场景 | The category for the trip-planning example. | 页面中旅行规划例子的日常类别。 |
| trip planning | 旅行规划 | The everyday scenario used to illustrate state and memory. | 页面用来说明状态和记忆的日常场景。 |
| trip-planning example | 旅行规划示例 | An example in which current itinerary is state and hotel preference is memory. | 当前行程是状态、酒店区域偏好是记忆的例子。 |
| itinerary | 行程；行程安排 | The current trip plan held in state. | 状态中记录的当前旅行安排。 |
| current itinerary | 当前行程 | The itinerary for the trip being planned now. | 正在规划的这次旅行的行程。 |
| preferred hotel area | 偏好的酒店区域 | A hotel-area preference recalled from memory. | 从记忆中取回的酒店区域偏好。 |
| hotel area preference | 酒店区域偏好 | A preferred area for choosing a hotel. | 选择酒店时偏好的地理区域。 |
| AI product | AI 产品 | The category for the support-agent example. | 页面中客服智能体例子的 AI 产品类别。 |
| support agent | 客服智能体 | An AI product agent that handles an open support case. | 处理客服案件的 AI 智能体。 |
| Support agent | 客服智能体 | Capitalized wording for the support-agent example. | “support agent”的首字母大写写法。 |
| support-agent example | 客服智能体示例 | An example in which an open case is state and customer history is memory. | 开放案件是状态、客户历史是记忆的例子。 |
| support case | 客服案件 | A customer-support issue currently being handled. | 当前正在处理的客户支持问题。 |
| open case | 未关闭案件 | The active case held in state. | 状态中记录的尚未处理完的案件。 |
| customer history | 客户历史 | Prior customer information retrieved as memory. | 作为记忆取回的客户过往信息。 |
| prior customer history | 过往客户历史 | Customer information from earlier interactions. | 客户以前互动留下的历史信息。 |
| What it is NOT | 它不是什么 | The page section that distinguishes memory from related concepts. | 页面用来说明记忆不等于哪些概念的部分。 |
| misconception | 误解 | An incorrect equation between memory and another concept. | 把记忆和另一个概念错误地当成一回事。 |
| distinction | 区分 | A boundary between memory, state, context, and parameters. | 记忆、状态、上下文、参数之间的区别。 |
| visible now | 现在可见 | Available to the model at the current moment. | 模型此刻能看到的内容。 |
| stored for later | 为以后存储 | Kept so it can be used in a later step or interaction. | 保存起来，之后某一步或某次交流再使用。 |
| can persist | 可以持续保留 | Can remain available beyond the current task moment. | 不会随着当前一步结束就消失。 |
| tracks current progress | 跟踪当前进度 | Follows how the task is advancing now. | 记录任务目前做到哪一步。 |
| external information | 外部信息 | Information kept outside the model's learned parameters. | 存在模型参数之外的信息。 |
| model parameters | 模型参数 | Learned values inside a model. | 模型训练后形成的内部数值。 |
| learned values | 学到的数值 | Values learned during model training. | 模型训练过程中学到的数值。 |
| external memory | 外部记忆 | Memory stored outside the model itself. | 存在模型外部、由系统保存的记忆。 |
| learned knowledge | 学到的知识 | Knowledge encoded in model parameters. | 编码在模型参数中的知识。 |
| Related concepts | 相关概念 | Concepts connected to memory and state on the page. | 页面列出的与记忆和状态有关的概念。 |
| related concepts chain | 相关概念链条 | Task → State → Agent action → Updated state → Memory → Retrieved context. | 从任务到状态、行动、更新状态、记忆再到取回上下文的关系链。 |
| Task → State | 任务→状态 | A task gives rise to current task state. | 任务开始后要用状态记录当前情况。 |
| State → Agent action | 状态→智能体行动 | Current state informs the agent's next action. | 当前状态帮助智能体决定并执行下一步。 |
| Agent action | 智能体行动 | An action taken by the agent in the task. | 智能体在任务中执行的动作。 |
| Updated state | 更新后的状态 | State after an agent action and its result are recorded. | 记录行动和结果后形成的新状态。 |
| Memory → Retrieved context | 记忆→取回的上下文 | Stored memory becomes available in current context when retrieved. | 记忆取回后会成为当前上下文可用的信息。 |
| Agent Loop | 智能体循环 | A related concept linked from the page. | 页面链接的相关概念，表示智能体反复行动和更新的循环。 |
| agent loop | 智能体循环 | Lowercase wording for agent loop. | “Agent Loop”的小写写法。 |
| AI Agent link | AI 智能体链接 | The related-concept link back to AI agent. | 页面相关概念区指向 AI agent 的链接。 |
| Remember this | 请记住 | The page's summary section. | 页面最后总结重点的部分。 |
| summary | 总结 | A concise restatement of the main distinction. | 对主要区别的简短重述。 |
| note | 备注；要点 | The highlighted reminder about state and memory. | 页面突出显示的记忆与状态要点。 |
| current task tracker | 当前任务跟踪器 | A descriptive name for state based on the page's definition. | 根据页面定义对“状态”的通俗叫法。 |
| retained-information store | 保留信息存储 | A descriptive name for memory based on the page's definition. | 根据页面定义对“记忆”的通俗叫法。 |
| current visibility | 当前可见范围 | A descriptive name for context based on the page's definition. | 根据页面定义对“上下文”的通俗叫法。 |
| Video | 视频 | The page section reserved for an explainer. | 页面预留的讲解视频部分。 |
| video | 视频 | Lowercase wording for the video section. | “Video”的小写写法。 |
| no video is available | 暂无视频 | The page's current video status. | 页面说明目前没有可用视频。 |
| page body | 页面正文 | The visible topic content used for glossary extraction. | 本次词汇收集所依据的可见主题正文。 |
| source page | 来源页面 | The HTML page from which candidates were collected. | 候选词条来源的 HTML 页面。 |
| topic | 主题 | A page focused on one concept. | 专门解释一个概念的页面主题。 |
| module | 模块 | The larger topic grouping containing the page. | 包含本页面的一组更大主题。 |
| Topic 06 | 主题 06 | The page's topic number within the module. | 本页面在模块中的编号。 |
| Agents, Tools & MCP | 智能体、工具与 MCP | The topic group named in the page navigation and metadata. | 页面所属的智能体、工具与 MCP 主题组。 |
| MCP | 模型上下文协议；MCP | An acronym appearing in the surrounding topic-group label; not defined in this page's body. | 只出现在页面上级主题名称中的缩写，本页正文没有解释协议细节。 |
| definition | 定义 | A concise explanation of what memory and state are. | 用简短文字说明记忆和状态是什么。 |
| lede | 导语；摘要句 | The introductory sentence framing the topic. | 页面开头概括主题重点的一句话。 |
| on this page | 本页内容 | Navigation labels for the page sections. | 页面目录中列出各个内容区的导航。 |
| navigation | 导航 | Links that move between page sections. | 帮助跳到页面不同部分的链接。 |
| section | 内容区；部分 | A named block of the topic page. | 页面中有标题的一块内容。 |
| card | 卡片 | A layout container for a page section. | 页面用来承载一块内容的布局容器。 |
| process card | 流程卡片 | A card presenting one stage of the process. | 展示某一个流程阶段的卡片。 |
| example card | 示例卡片 | A card presenting one practical example. | 展示一个实际例子的卡片。 |
| concept tree | 概念树 | The visual chain connecting task, state, action, memory, and context. | 用树状或链状关系展示概念连接。 |
| chip | 概念标签；链接标签 | A small linked label for a related concept. | 页面中指向相关概念的小标签链接。 |
| back link | 返回链接 | The link returning to the parent topic page. | 回到上一级主题页面的链接。 |
| current | 当前的 | Existing or available at the present task moment. | 现在这个时刻的。 |
| later | 以后；后续 | A time after the current step or interaction. | 当前步骤或交流之后。 |
| relevant | 相关的 | Directly useful to the current task or context. | 和当前任务直接有关、能帮上忙的。 |
| immediate | 眼前的；即时的 | Happening in the present step. | 就发生在当前这一步的。 |
| selected | 选定的 | Chosen from available information. | 从一批信息中挑选出来的。 |
| preserve useful information across steps or interactions | 跨步骤或互动保留有用信息 | Keep helpful information available beyond one step or exchange. | 把有用信息跨多个步骤或交流保存下来。 |
| state tracks the current task | 状态跟踪当前任务 | State records what is happening in the task now. | 状态用来记录当前任务发生了什么。 |
| memory preserves information | 记忆保留信息 | Memory keeps information that may be useful later. | 记忆保存以后可能有用的信息。 |
| memory can preserve useful information | 记忆可以保留有用信息 | Memory retains selected information for future use. | 记忆把选中的有用信息留到以后使用。 |
| memory retrieves information | 记忆取回信息 | Memory brings stored information back into current context. | 记忆把保存的信息取回当前上下文。 |
| state and memory distinction | 状态与记忆的区别 | State concerns current progress; memory concerns retained or retrieved information. | 状态看当前进度，记忆看保存或取回的信息。 |
| context and memory distinction | 上下文与记忆的区别 | Context is visible now; memory can be stored for later. | 上下文现在可见，记忆可以留到以后。 |
| state and model parameters distinction | 状态与模型参数的区别 | State is current task information; parameters are learned model values. | 状态是当前任务信息，参数是模型学到的数值。 |

## Potential Missing Concepts

These concepts are useful for a fuller AI-agent memory/state glossary but are not explicitly defined, measured, or named as mechanisms in the page body. They are kept separate from direct page candidates.

- **short-term memory（短期记忆）**：页面谈到当前任务和跨步骤保留，但没有把短期记忆作为独立类型定义。
- **long-term memory（长期记忆）**：页面说 memory 可以跨 interactions 保留，但没有定义长期记忆的存储周期或边界。
- **working memory（工作记忆）**：state 和 current context 有相关含义，但页面没有使用这一术语。
- **episodic memory（情景记忆）**：页面举了行程和客户历史例子，但没有说明按事件保存的记忆类型。
- **semantic memory（语义记忆）**：selected facts 可能接近事实型记忆，但页面没有区分事实和事件记忆。
- **procedural memory（程序记忆）**：页面有流程步骤，但没有讨论保存“如何做事”的记忆。
- **conversation memory（对话记忆）**：页面提到跨 interactions，却没有专门说明对话历史如何保存。
- **persistent memory（持久化记忆）**：memory can persist 被表达为区别，但没有说明持久化介质或生命周期。
- **ephemeral state（临时状态）**：current task state 可能是临时的，但页面没有说明状态何时清除。
- **state transition（状态转移）**：流程显示状态更新，但没有形式化说明状态如何从一个值变到下一个值。
- **state machine（状态机）**：页面有阶段和状态，但没有把 agent 建模为有限状态机或其他状态机。
- **state schema（状态模式）**：页面说 record goal and current task information，但没有定义状态字段或数据结构。
- **state store（状态存储）**：页面说明状态要记录，却没有说明由什么存储组件保存。
- **checkpoint（检查点）**：更新状态与保存事实可能形成检查点，但页面没有命名或描述检查点机制。
- **snapshot（快照）**：current state 可能被快照化，但正文没有提到状态快照。
- **memory store（记忆存储）**：notebook / filing cabinet 是类比，不是实际存储组件定义。
- **external memory system（外部记忆系统）**：页面区分 external information and model parameters，但没有说明外部系统架构。
- **database（数据库）**：filing cabinet 类比存储，却没有提到数据库或表结构。
- **key-value store（键值存储）**：没有说明按键检索记忆的实现方式。
- **vector database（向量数据库）**：没有说明使用向量或嵌入保存、检索记忆。
- **embedding（嵌入）**：retrieve memory 出现，但没有描述语义向量表示。
- **similarity search（相似度搜索）**：relevant memory 出现，但没有解释如何判断相关性。
- **retrieval strategy（检索策略）**：页面只说 bring relevant memory，没有定义检索规则。
- **memory ranking（记忆排序）**：没有说明多个候选记忆如何排序。
- **relevance scoring（相关性评分）**：relevant memory 出现，但没有给出数值评分。
- **memory write policy（记忆写入策略）**：页面说 preserve selected facts，却没有说明由谁、按什么规则选择。
- **memory read policy（记忆读取策略）**：页面说 retrieve memory，却没有说明何时读取、读取多少。
- **memory consolidation（记忆整合）**：没有讨论如何把多条信息合并为更稳定的记忆。
- **memory summarization（记忆摘要）**：没有说明如何压缩长期信息以节省上下文空间。
- **memory deletion（记忆删除）**：没有提到过期、删除或遗忘机制。
- **memory expiration（记忆过期）**：没有定义信息何时失效。
- **memory freshness（记忆新鲜度）**：没有说明旧客户历史或旧偏好是否需要更新。
- **memory provenance（记忆来源）**：没有说明保存事实的来源、时间或可信度。
- **memory conflict resolution（记忆冲突解决）**：没有说明新旧事实或偏好冲突时如何处理。
- **source of truth（事实来源）**：没有定义当 state、memory、context 不一致时以谁为准。
- **context assembly（上下文组装）**：bring relevant memory into current context 被提到，但没有展开组装过程。
- **context management（上下文管理）**：没有说明如何控制当前上下文中的信息。
- **context selection（上下文选择）**：没有说明从可用信息中选择哪些内容给模型看。
- **context compression（上下文压缩）**：没有讨论上下文过长时如何压缩。
- **context window limit（上下文窗口限制）**：Context Window 被定义为可见信息，但没有介绍容量限制。
- **working context（工作上下文）**：current context 有近似含义，但页面没有将其作为术语定义。
- **model input（模型输入）**：页面说 what the model can currently see，却没有具体区分输入字段。
- **model parameters（模型参数）**：页面将其作为对照概念提到，但没有解释参数训练、更新或存储细节。
- **parameter update（参数更新）**：页面说 parameters are learned values，但没有讨论运行时是否更新参数。
- **external knowledge（外部知识）**：external information 出现，但没有讨论知识库和记忆的边界。
- **personalization（个性化）**：preferred hotel area 和 customer history 暗示个性化，但没有命名该目标。
- **user profile（用户画像）**：customer history / preference 相关，但页面没有描述用户画像结构。
- **preference memory（偏好记忆）**：hotel area preference 是例子，但没有把偏好记忆作为类型定义。
- **customer memory（客户记忆）**：prior customer history 是例子，但没有讨论客户数据的记忆治理。
- **task memory（任务记忆）**：页面说 current task information，却没有定义任务级记忆的生命周期。
- **cross-session memory（跨会话记忆）**：across interactions 出现，但没有明确 session 边界。
- **session state（会话状态）**：current task state 有相关含义，但没有区分会话状态和长期状态。
- **state serialization（状态序列化）**：record state 被提到，却没有说明状态如何编码或传输。
- **state restoration（状态恢复）**：retrieve memory 不等于恢复完整 state；页面没有说明恢复机制。
- **event log（事件日志）**：record result 与 prior history 相关，但没有把每次变化记录为事件日志。
- **trajectory（轨迹）**：流程有多个步骤，但没有定义完整的任务轨迹。
- **agent loop（智能体循环）**：本页把 Agent Loop 作为关联链接，但没有展开循环结构。
- **observation（观察）**：agent action 之后有 result，但页面没有用 observation 术语说明反馈。
- **feedback（反馈）**：result 可影响 updated state，但没有定义反馈信号。
- **planning（规划）**：页面只有 task starts / acts / continue，没有展开计划生成。
- **task completion（任务完成）**：页面讨论 current progress，却没有定义完成条件。
- **goal completion（目标完成）**：record goal 出现，但没有定义如何判断目标已经达成。
- **termination condition（终止条件）**：continue 出现，但没有说明何时停止任务。
- **memory trigger（记忆触发器）**：没有说明什么事件会触发保存或取回记忆。
- **retrieval trigger（检索触发器）**：retrieve memory 是步骤名，但没有定义触发规则。
- **write trigger（写入触发器）**：store useful information 是步骤名，但没有定义何时写入。
- **memory controller（记忆控制器）**：没有说明哪个组件管理读写记忆。
- **orchestrator（编排器）**：流程存在，但没有命名负责协调 state、memory、context 的组件。
- **agent runtime（智能体运行时）**：页面描述工作过程，但没有说明运行时环境。
- **application state（应用状态）**：state 可能由应用保存，但正文没有区分智能体状态和应用状态。
- **world state（世界状态）**：旅行和客户案例涉及外部世界，但没有定义外部世界状态。
- **source state（来源状态）**：没有说明客户系统、行程系统等外部来源的状态。
- **consistency（一致性）**：没有讨论 state、memory、context 与现实信息是否一致。
- **staleness（陈旧性）**：prior history 和 preferred area 可能过时，但页面没有讨论陈旧信息。
- **accuracy（准确性）**：页面没有指标来判断保存或取回的信息是否正确。
- **memory recall accuracy（记忆召回准确率）**：relevant memory 被提到，但没有量化取回是否相关。
- **retrieval precision（检索精确率）**：没有指标衡量取回内容中有多少真正相关。
- **retrieval recall（检索召回率）**：没有指标衡量所有相关记忆中有多少被取回。
- **task success rate（任务成功率）**：页面没有显式性能指标。
- **state update latency（状态更新延迟）**：没有讨论记录行动结果所需的时间。
- **memory retrieval latency（记忆检索延迟）**：没有讨论取回记忆的耗时。
- **storage cost（存储成本）**：没有讨论保存客户历史或其他信息的成本。
- **context cost（上下文成本）**：没有讨论把记忆放入上下文所消耗的 token 或计算资源。
- **token usage（令牌用量）**：Context Window 出现，但没有说明令牌容量或费用。
- **privacy（隐私）**：customer history 和 preferences 可能是敏感信息，但页面没有讨论隐私。
- **data retention（数据保留）**：memory retain 出现，但没有规定保留期限。
- **data deletion（数据删除）**：页面没有讨论删除客户历史或偏好的要求。
- **access control（访问控制）**：没有说明谁可以读取或写入记忆。
- **authorization（授权）**：没有讨论读取客户历史需要什么授权。
- **security（安全）**：没有讨论外部记忆或上下文中的信息保护。
- **prompt injection（提示注入）**：没有讨论被取回的记忆可能包含恶意指令。
- **memory poisoning（记忆投毒）**：没有讨论错误或恶意信息被写入长期记忆。
- **audit trail（审计轨迹）**：没有说明谁在何时保存、读取或更新了记忆。
- **observability（可观测性）**：没有说明如何监控 state / memory 的读写和检索效果。
- **human review（人工复核）**：本页没有列出人工复核流程，不能从例子直接推断。
- **personal data（个人数据）**：customer history 可能包含个人数据，但页面没有展开数据类别。
- **memory governance（记忆治理）**：没有讨论策略、权限、生命周期和合规管理。
- **model fine-tuning（模型微调）**：model parameters 被提到，但没有讨论通过训练把信息写进模型。
- **in-context learning（上下文学习）**：context window 出现，但没有定义通过当前上下文影响模型行为的学习方式。
- **knowledge base（知识库）**：filing cabinet 是类比，页面没有命名知识库。
- **cache（缓存）**：当前信息和保存信息相关，但页面没有讨论缓存语义或失效策略。
- **checkpointing（检查点保存）**：state update 可能需要 checkpointing，但正文没有说明持久化步骤。
- **multi-agent memory（多智能体记忆）**：页面只讨论单个 AI agent，没有涉及多个智能体共享状态。
- **shared state（共享状态）**：没有说明多个组件或 agent 是否共享 state。
- **memory isolation（记忆隔离）**：没有讨论不同用户、任务或会话之间的记忆隔离。

## Aliases / Synonyms

- Memory ↔ retained information ↔ stored information ↔ information preserved for later
- Memory ↔ external memory ↔ retained context（相关但不完全同义；context 不一定被持久保存）
- State ↔ current task information ↔ current task state ↔ current progress record
- State ↔ working state ↔ task state（working state 和 task state 是合理扩展词，本页没有逐字使用）
- Context ↔ current context ↔ available information ↔ information visible now
- Context Window ↔ context window ↔ model-visible context ↔ current visibility range（后两项是解释性别名）
- Retrieved context ↔ brought-in context ↔ relevant memory in current context
- Retain ↔ preserve ↔ keep ↔ save
- Retrieve ↔ bring back ↔ recall ↔ fetch
- Store ↔ save ↔ preserve ↔ write
- Useful information ↔ helpful information ↔ information likely to help later
- Selected facts ↔ chosen facts ↔ facts worth preserving
- Current task ↔ task in progress ↔ active task
- Current progress ↔ task progress ↔ progress of the current task
- Agent action ↔ agent acts ↔ action taken by the agent ↔ step taken by the agent
- Update state ↔ record the result ↔ refresh current state ↔ change task state
- Create State ↔ initialize state ↔ record initial state
- Retrieve Memory ↔ recall memory ↔ fetch relevant memory ↔ bring memory into context
- Continue ↔ proceed ↔ move to the next step
- Task Starts ↔ task start ↔ begin the task ↔ initialize the task
- Store Useful Information ↔ preserve useful facts ↔ save information for later
- Task → State → Agent action → Updated state → Memory → Retrieved context ↔ memory/state workflow ↔ state-and-memory flow
- Notes currently open on your desk ↔ open desk notes ↔ current working notes（类比表达）
- Notebook or filing cabinet ↔ retained-information store ↔ memory repository（类比表达；repository 未在正文出现）
- Information physically available on the desk ↔ currently visible information ↔ current context（类比表达）
- Itinerary ↔ trip plan ↔ current travel plan
- Preferred hotel area ↔ hotel-area preference ↔ preferred accommodation area
- Open case ↔ active support case ↔ current customer case
- Customer history ↔ prior customer history ↔ customer record history
- Memory ↔ Context Window：相关但不等价；前者可以保存，后者描述模型当前能看到什么。
- Memory ↔ State：相关但不等价；前者面向留存和取回，后者面向当前任务进度。
- Memory ↔ Model Parameters：相关但不等价；前者是外部信息，后者是模型学到的数值。
- State ↔ Context：相关但不等价；状态是当前任务信息，context 是模型当前可见的信息。
- Current context ↔ retrieved context：前者是当前可用范围，后者强调其中有一部分来自 memory retrieval。
- Remember this ↔ summary ↔ key takeaway ↔ main reminder（页面结构表达）
- What is it? ↔ definition ↔ concept explanation（页面结构表达）
- What it is NOT ↔ misconceptions ↔ distinctions（页面结构表达）
- Real-world examples ↔ practical examples ↔ applied examples
- Agents, Tools & MCP ↔ agent-and-tool topic group ↔ surrounding topic section
- Agent Loop ↔ agent loop（大小写表面形式）
- AI Agent ↔ AI agent ↔ agent（大小写或缩写表面形式）
- Memory and state ↔ memory & state（and / ampersand 表面形式）

## Do Not Confuse Candidates

- **Memory vs Context Window**：memory 是保存或以后取回的信息；context window 是模型当前能看到的信息范围。
- **Memory vs State**：memory 可以跨步骤或互动保留；state 记录当前任务信息和当前进度。
- **Memory vs Model Parameters**：memory 是外部信息；model parameters 是模型训练得到的内部学习值。
- **State vs Context**：state 关注任务正在发生什么；context 关注模型在此刻可用或可见什么。
- **Retrieved context vs all context**：retrieved context 是从 memory 带回来的相关部分；当前 context 还可能包含其他任务信息。
- **Memory vs notebook / filing cabinet**：notebook 和 filing cabinet 只是帮助理解 memory 的类比，不是页面规定的技术存储组件。
- **State vs open desk notes**：open desk notes 是 state 的类比，不表示状态必须以笔记形式存储。
- **Context vs physical desk**：desk 只是 context 的类比，不表示模型真的拥有物理桌面。
- **Retain vs retrieve**：retain / preserve / store 是把信息留下来；retrieve 是之后把信息取回来。
- **Store vs retrieve**：store 是写入或保存；retrieve 是读取或取回，方向相反。
- **Current task information vs selected facts**：current task information 属于当前状态；selected facts 是从过程中挑出来、准备以后使用的信息。
- **Current progress vs goal**：current progress 说明做到哪一步；goal 说明想要达到什么结果。
- **Goal vs result**：goal 是开始时记录的目标；result 是行动后实际得到的结果。
- **Task vs step**：task 是整体工作；step 是完成任务过程中的一个阶段或动作。
- **Agent acts vs Update State**：agent acts 是执行一步；update state 是把这一步的结果记录到状态中。
- **Update State vs Store Useful Information**：update state 记录当前任务最新结果；store useful information 选择可能对以后有帮助的事实。
- **Store Useful Information vs Retrieve Memory**：前者把信息存起来；后者把相关信息取回来。
- **Continue vs Retrieve Memory**：retrieve memory 是带回相关信息；continue 是在信息更新后继续任务。
- **Memory preservation vs memory retrieval**：保存不等于取回；信息可以被保存，但需要另外的检索步骤才能进入当前 context。
- **Open case vs customer history**：open case 是当前 state；customer history 是从过去互动中取回的 memory。
- **Current itinerary vs preferred hotel area**：current itinerary 是当前旅行任务的 state；preferred hotel area 是可复用的偏好 memory。
- **Support agent vs AI agent**：support agent 是 AI agent 的一个应用例子，不是所有 AI agent 的同义词。
- **Trip planning vs support workflow**：trip planning 是日常例子；support workflow 是 AI 产品例子，两者展示不同的 state / memory 内容。
- **AI agent vs Agent Loop**：AI agent 是系统或主体；Agent Loop 是其行动、更新和继续的循环机制，页面仅将其列为关联概念。
- **Agent action vs State**：agent action 是发生的操作；state 是记录任务当前情况的信息。
- **Updated state vs Memory**：updated state 是当前行动后的新状态；memory 是为以后保留或可取回的信息。
- **Context window vs model parameters**：context window 描述运行时当前可见输入；model parameters 是模型中学到的值。
- **Context window vs external memory**：context window 是可见范围；external memory 是可以长期或跨步骤保存的信息来源。
- **External information vs model parameters**：external information 不等于被训练进模型参数的知识。
- **Persistence vs visibility**：持久保存不代表模型当前可见；memory 需要 retrieve 才可能进入 context。
- **Relevance vs persistence**：信息保留下来不代表每次都相关；retrieve memory 还要把相关内容带进当前 context。
- **Selected facts vs all facts**：页面说 preserve selected facts，不能把所有观察到的信息都当成需要保存的 memory。
- **Current context vs current task**：context 是可用信息范围；task 是要完成的工作，两者不是同一对象。
- **State tracking vs task completion**：跟踪进度不等于已经完成任务；页面没有定义完成条件。
- **Memory & State vs model training**：页面讨论运行任务时的信息处理，不等于训练或更新模型参数。
- **AI agent vs memory**：AI agent 是使用 memory / state 的系统；memory 只是其中一种信息机制。
- **Memory vs knowledge base**：本页没有定义知识库；文件柜只是类比，不能直接推出 database 或 vector database 实现。
- **Memory retrieval vs search**：页面只说 retrieve relevant memory，没有规定使用关键词搜索、向量搜索或其他算法。
- **MCP vs Memory**：MCP 只出现在上级主题名称中；本页没有说 MCP 是记忆系统或记忆协议。
- **MCP vs Agent Loop**：两者都出现在相关主题语境中，但本页没有给出 MCP 的协议细节，也没有把它定义为循环机制。
- **Page structure terms vs AI mechanisms**：definition、analogy、process、video、card、chip 等是页面结构或呈现词，不要误当成 memory/state 机制。
- **Analogy vs implementation**：desk、notebook、filing cabinet 是解释用类比，不代表真实系统一定使用这些对象。
- **Video status vs topic content**：No video is available 是媒体状态，不是 memory/state 的技术结论。

## Notes

- 本文件是 Module 09 Topic 06「Memory & State」的 raw glossary 收集稿；按请求保留最大原始候选集合，不做去重、删减或最终术语裁决。
- 来源页的核心定义是：state tracks what is happening in the current task；memory can preserve useful information across steps or interactions。
- 页面明确的三项区分是：State = current task information；Memory = information retained or retrieved beyond the immediate step；Context Window = what the model can currently see。
- 页面类比是：state 像当前摊开在桌面上的 notes；memory 像 notebook 或 filing cabinet；context 像此刻物理可见的 desk information。
- 页面明确的四步流程为：Task Starts → Create State → record the goal and current task information；Agent Acts → Update State → take a step and record its result；Store Useful Information → Preserve selected facts；Retrieve Memory → Continue → bring relevant memory into the current context。
- 页面两个现实例子分别是：Everyday · Trip planning（state = current itinerary；memory = preferred hotel area）和 AI product · Support agent（state = open case；memory = prior customer history）。
- “What it is NOT” 明确给出三组对照：Memory ≠ Context Window；Memory ≠ State；Memory ≠ Model Parameters。
- Related concepts 的原始链条是：Task → State → Agent action → Updated state → Memory → Retrieved context。
- Related concept chips 明确链接到 Agent Loop、Context Window、AI Agent；其中 Agent Loop 只作为关联链接出现，本页没有展开其机制。
- 页面没有显式给出数值 metrics、评测表、性能指标、存储方案、检索算法或生命周期策略；相关扩展候选已放入 Potential Missing Concepts，避免把推测当成正文事实。
- 页面没有展开短期/长期记忆、工作记忆、数据库、向量检索、embedding、状态模式、状态存储、冲突解决、隐私、安全、权限或审计等实现概念；这些仅作为后续扩展候选保留。
- HTML visible source content 也包括导航和页面结构词（What is it?、Think of it like...、How it works、Real-world examples、What it is NOT、Related concepts、Remember this、Video、definition、analogy、process、examples、related concepts、note、card、chip、page body），相关词按“正文重要词/页面术语”保留。
- Video 区明确写的是 “No video is available for this topic yet.”，因此视频相关词是页面状态候选，不应误当成该主题的机制或实例。
- Source page 的 `title` 是 “What are Memory and State in an AI Agent?”；raw 文件按任务命名为 `09-memory-state.md`。
