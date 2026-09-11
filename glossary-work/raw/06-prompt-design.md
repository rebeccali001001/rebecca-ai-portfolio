# Prompt Design

## Module/Topic/Source File

- Module: 06 · Prompting & System Design
- Topic: Prompt Design
- Source File: `prompt-design.html`
- Source page label: `06 · Prompting & System Design`
- Page title: `What Is Prompt Design?`
- Raw-stage scope: maximum source-grounded candidate set; repeated surface forms, capitalization variants, aliases, neighboring concepts, process nodes, example fields, comparison phrases, and beginner-facing wording are intentionally retained.

## Glossary Candidates

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Prompt Design | 提示设计；提示词设计 | The practice of structuring instructions for a model. | 把给 AI 的要求组织得更清楚的方法。 |
| prompt design | 提示设计；提示词设计 | Designing a request so the model can understand and act on it. | 设计一段让模型看懂并执行的要求。 |
| What Is Prompt Design? | 什么是提示设计？ | The question answered by this topic page. | 这个主题要解释的核心问题。 |
| prompt | 提示；提示词 | Text or instructions sent to a model. | 发给模型的文字要求。 |
| prompts | 提示；提示词（复数） | Multiple inputs or instruction sets given to a model. | 给模型的多组输入或要求。 |
| design | 设计 | The deliberate arrangement of parts for a purpose. | 为了达到目的而有意识地安排内容。 |
| practice | 实践；方法 | A repeatable way of doing something. | 可以反复使用的一种做事方法。 |
| structuring instructions | 组织指令 | Arranging instructions into a clear shape. | 把要求按清楚的结构排好。 |
| structure instructions | 组织指令 | Put directions into an understandable order. | 按容易理解的方式安排指令。 |
| instructions | 指令；说明 | Directions telling a model what to do. | 告诉模型应该做什么的要求。 |
| instruction | 指令；说明 | One direction supplied to a model. | 给模型的一条要求。 |
| model | 模型 | The AI system that interprets the prompt and produces a result. | 负责理解要求并生成结果的 AI。 |
| AI | 人工智能 | Artificial intelligence; a system that performs tasks associated with intelligence. | 能执行一些通常需要人来完成的智能任务的技术。 |
| artificial intelligence | 人工智能 | Computer systems that perform tasks such as understanding or generating language. | 能理解和生成内容的计算机系统。 |
| understands the task | 理解任务 | Identifies what the model is being asked to do. | 模型知道到底要做什么。 |
| understand the task | 理解任务 | Figure out the requested work. | 弄清楚要求完成的事情。 |
| task | 任务 | The work the model is asked to perform. | 要模型完成的事情。 |
| relevant context | 相关上下文 | Information that matters for completing the task. | 对完成任务有用的背景信息。 |
| context | 上下文；背景信息 | Information surrounding the request that helps interpretation. | 帮模型理解当前要求的相关背景。 |
| constraints | 约束；限制条件 | Rules that limit how the task should be done. | 规定能怎么做、不能怎么做的条件。 |
| constraint | 约束；限制条件 | One rule or limit on the task or answer. | 对任务或答案的一条限制。 |
| expected result | 预期结果 | The result the requester wants the model to produce. | 希望模型最后交付的结果。 |
| expected output | 预期输出 | The form or content expected from the model. | 希望模型输出的内容或格式。 |
| result | 结果 | What the model produces after handling a task. | 模型处理任务后给出的成果。 |
| output | 输出 | The answer or artifact produced by a model. | 模型生成出来的答案或结果。 |
| answer | 答案；回答 | A response to a request or question. | 模型对问题或要求的回应。 |
| response | 回答；响应 | What the model returns after receiving input. | 模型收到输入后返回的内容。 |
| task, context, constraints, and expected result | 任务、上下文、约束和预期结果 | The four aspects prompt design makes clear. | 提示设计需要说清楚的四类内容。 |
| task, relevant context, constraints, and expected result | 任务、相关上下文、约束和预期结果 | The complete definition phrase used by the page. | 页面定义中列出的四个要点。 |
| make the task explicit | 把任务说清楚 | State the work directly instead of leaving it implied. | 不让模型猜，直接说要做什么。 |
| explicit task | 明确任务 | A task stated directly and clearly. | 已经明确写出来的任务。 |
| explicit | 明确的；直接说出的 | Clearly stated rather than implied. | 明白写出来、不需要猜的。 |
| weak request | 弱请求；模糊请求 | A request with too little detail to guide the work well. | 信息太少、容易让模型猜的要求。 |
| WEAK REQUEST | 弱请求；模糊请求 | The example label for “Check this.” | 页面中“Check this.”这个不完整请求的标签。 |
| “Check this.” | “检查这个。” | An underspecified request used as the weak example. | 只说检查，却没说检查什么、依据和结果格式。 |
| better designed request | 设计得更好的请求 | A request that states task, context, constraints, and output. | 把关键要求写完整的请求。 |
| BETTER DESIGNED REQUEST | 设计得更好的请求 | The improved version of the weak request example. | 页面中结构更清晰的请求示例标签。 |
| task part | 任务部分 | The part that says what the model should do. | 说明模型具体要做什么的部分。 |
| context part | 上下文部分 | The part that says what information matters. | 说明哪些背景资料要参考的部分。 |
| constraints part | 约束部分 | The part that states rules the model should follow. | 说明模型必须遵守哪些限制的部分。 |
| output part | 输出部分 | The part that says what the answer should look like. | 说明结果要长什么样的部分。 |
| four useful parts | 四个有用部分 | Task, context, constraints, and output. | 设计提示时常用的四块内容。 |
| four parts | 四个部分 | The four-part structure presented on the page. | 页面介绍的四项结构。 |
| TASK | 任务 | The first prompt-design part: what should the model do? | 第一部分：模型要完成什么。 |
| CONTEXT | 上下文 | The second prompt-design part: what information matters? | 第二部分：哪些信息重要。 |
| CONSTRAINTS | 约束 | The third prompt-design part: what rules should it follow? | 第三部分：模型要遵守哪些规则。 |
| OUTPUT | 输出 | The fourth prompt-design part: what should the answer look like? | 第四部分：答案应该是什么样。 |
| What should the model do? | 模型应该做什么？ | The question that defines the task part. | 用来明确任务内容的问题。 |
| What information matters? | 哪些信息重要？ | The question that defines the context part. | 用来筛选相关背景的问题。 |
| What rules should it follow? | 模型应该遵守什么规则？ | The question that defines the constraints part. | 用来写清限制条件的问题。 |
| What should the answer look like? | 答案应该是什么样？ | The question that defines the output part. | 用来规定结果形式的问题。 |
| not every prompt needs all four parts explicitly | 不是每个提示都需要明确写出四部分 | The four parts are useful, but none is mandatory in every prompt. | 简单问题不一定要逐项写全。 |
| explicitly | 明确地；显式地 | Written out directly rather than left implicit. | 直接写出来，而不是让人猜。 |
| request | 请求；要求 | Something a user asks the model to handle. | 用户要求模型处理的事情。 |
| better request | 更好的请求 | A request with clearer goals, evidence, boundaries, and output. | 让模型更容易执行的请求。 |
| “Review this invoice.” | “审查这张发票。” | A short invoice-review request used as the bad example. | 只说审查发票，却没说审查什么和怎么返回。 |
| BAD | 不好的示例 | The label for the underspecified invoice request. | 页面中信息不足的发票示例标签。 |
| BETTER | 更好的示例 | The label for the structured invoice request. | 页面中结构更完整的发票示例标签。 |
| review the invoice | 审查发票 | Examine the supplied invoice. | 查看并检查提供的发票。 |
| invoice | 发票 | A document containing billing or transaction information. | 记录费用或交易信息的单据。 |
| invoice review | 发票审查 | Checking an invoice against a requirement. | 按要求检查发票内容。 |
| missing required fields | 缺失的必填字段 | Required pieces of information that are absent. | 本来必须有、但现在没有的信息项。 |
| required fields | 必填字段 | Fields that must be present for the invoice to be complete. | 发票必须填写的信息项。 |
| required field | 必填字段 | One field that is required. | 一个必须存在的字段。 |
| field | 字段；信息项 | One named piece of data in a document or output. | 文档或结果中的一个具体信息格。 |
| fields | 字段；信息项（复数） | Multiple named pieces of data. | 多个具体的信息项。 |
| use the attached invoice | 使用附上的发票 | Use the invoice supplied with the request as evidence. | 只参考随请求附上的发票。 |
| attached invoice | 附件发票 | The invoice provided as an attachment. | 作为附件提供的发票文件。 |
| provided invoice | 已提供的发票 | The invoice made available to the model. | 已经交给模型查看的发票。 |
| provided information | 已提供的信息 | Information supplied in the current request. | 当前请求中实际给出的资料。 |
| use only the provided invoice | 只使用提供的发票 | Limit evidence to the supplied invoice. | 不参考没有提供的其他资料。 |
| provided | 已提供的 | Made available for the task. | 已经交给模型使用的。 |
| context: use the attached invoice | 上下文：使用附上的发票 | The example's context instruction. | 示例中说明参考哪份资料的部分。 |
| review for missing required fields | 检查是否缺少必填字段 | Examine the invoice specifically for absent required data. | 重点检查发票有没有漏填必填项。 |
| do not invent missing fields | 不要编造缺失字段 | Do not fill absent information with guesses. | 缺少的信息不能凭空补出来。 |
| Do not invent missing values | 不要编造缺失值 | Do not create values that are absent from the source. | 原资料没有的数值不能猜着写。 |
| do not invent | 不要编造 | Do not make up unsupported content. | 没有依据的内容不要杜撰。 |
| invent | 编造；虚构 | Create information without evidence. | 没有资料却自己写出内容。 |
| missing values | 缺失值 | Values that are not present in the source. | 原资料中没有填写的值。 |
| missing field | 缺失字段 | A required information item that is absent. | 应该有但没有的信息项。 |
| missing information | 缺失信息 | Information needed for the task but not supplied. | 完成任务需要、但资料里没有的信息。 |
| rules | 规则 | Requirements that the model should obey. | 模型需要遵守的规定。 |
| RULES | 规则 | The example label for the no-invention boundary. | 示例中规定模型行为的部分标签。 |
| boundary | 边界；界限 | A limit on what the model may do. | 规定能做到哪里、不能越过哪里的线。 |
| clear boundary | 明确边界 | A plainly stated limit on the task. | 把不能做什么写清楚。 |
| constraints and rules | 约束和规则 | Requirements that limit the model's behavior. | 用来限制模型做法的要求。 |
| unwanted assumptions | 不希望的假设 | Guesses or interpretations the requester did not intend. | 用户没允许、模型却自行补上的猜测。 |
| assumption | 假设 | A belief used when information is incomplete. | 信息不全时先当成真的判断。 |
| make assumptions | 作出假设 | Fill gaps by guessing what is likely meant. | 信息不够时自行猜意思。 |
| unwanted | 不希望的；不需要的 | Not intended or desired by the requester. | 用户并不想要的。 |
| clear goal | 明确目标 | A plainly stated purpose for the task. | 清楚写出这次要达成什么。 |
| goal | 目标 | The purpose the task is meant to achieve. | 任务想达到的结果。 |
| clear evidence | 明确证据 | The source information the model should rely on. | 模型应该依据的资料说清楚了。 |
| evidence | 证据；依据 | Information used to support a conclusion. | 支持判断的资料。 |
| clear output | 明确输出 | A clearly specified answer or result shape. | 结果形式和内容要求很清楚。 |
| clear | 清楚的；明确的 | Easy to understand without guessing. | 不需要猜就能明白。 |
| why better | 为什么更好 | The explanation of the improved example. | 页面解释改写后好在哪里。 |
| task clarity | 任务清晰度 | How clearly the requested work is stated. | 模型能否清楚知道要做什么。 |
| goal clarity | 目标清晰度 | How clearly the desired purpose is stated. | 想达成什么是否说得明白。 |
| evidence boundary | 证据边界 | The limit on which information may be used. | 规定只能依据哪些资料。 |
| output specification | 输出规范 | A description of the required result form. | 对结果格式、字段或组织方式的说明。 |
| output specification clarity | 输出规范清晰度 | How unambiguously the result format is defined. | 模型是否明确知道答案要长什么样。 |
| status | 状态 | A label describing the review result. | 表示检查结果处于什么状态的字段。 |
| issues | 问题；异常项 | Problems found during the review. | 检查时发现的错误或缺漏。 |
| missing_fields | 缺失字段 | The output field listing absent required fields. | 结果中列出缺少哪些必填项。 |
| notes | 备注 | Additional explanatory comments in the output. | 对结果补充说明的文字。 |
| return status and issues | 返回状态和问题 | The requested output for the first invoice example. | 最后只返回检查状态和发现的问题。 |
| Return: status, missing_fields, notes. | 返回：状态、缺失字段、备注。 | The requested output fields for the second invoice example. | 规定结果必须有这三个字段。 |
| status, missing_fields, notes | 状态、缺失字段、备注 | A three-field output design. | 一种把审查结果整理成三栏的方式。 |
| output fields | 输出字段 | Named pieces of information in the result. | 结果中规定好的信息项。 |
| return | 返回 | Produce the requested result for the requester. | 按要求交付结果。 |
| output shape | 输出形状；输出结构 | The organization and fields of a response. | 答案由哪些部分组成、怎么排列。 |
| format | 格式 | The arrangement or presentation of an output. | 内容呈现和排版的方式。 |
| output format | 输出格式 | The required shape or organization of an answer. | 规定答案要怎样组织或排版。 |
| expected format | 预期格式 | The output arrangement the requester expects. | 用户希望结果采用的格式。 |
| structured output | 结构化输出 | An answer organized into specified fields or structure. | 按规定字段和结构输出的结果。 |
| answer format | 答案格式 | The form in which an answer is returned. | 回答应该采用的形式。 |
| model answer | 模型回答 | The response generated by the model. | 模型生成的答案。 |
| answer should look like | 答案应该是什么样 | A phrase about the expected response form. | 用来规定答案外形和组织方式。 |
| hard for an application to use | 应用难以使用 | A result is not in a reliable machine-usable form. | 输出太随意，软件不好直接处理。 |
| application | 应用；应用程序 | A product or program that uses a model. | 使用模型提供功能的软件。 |
| machine-usable | 机器可用的 | Easy for software to parse or consume. | 软件可以直接读取和处理的。 |
| usable result | 可用结果 | An output that can be acted on or consumed. | 生成后可以真正拿来使用的结果。 |
| application can use the result | 应用可以使用结果 | Software can consume the model's response. | 程序能直接接住并处理模型答案。 |
| Prompt Design vs System Prompt | 提示设计与系统提示的区别 | A comparison between a design practice and an instruction type. | 比较一种设计方法和一种具体指令。 |
| vs | 与……对比；区别 | Short for versus, meaning compared with. | 表示把两个概念放在一起比较。 |
| system prompt | 系统提示；系统提示词 | An application-supplied instruction that guides the model. | 应用给模型的高层指导要求。 |
| System Prompt | 系统提示；系统提示词 | The named instruction type in the comparison. | 对比段落中的系统级提示概念。 |
| system prompts | 系统提示（复数） | Multiple application-supplied guidance instructions. | 多组应用提供的指导。 |
| design practice | 设计实践 | A method for intentionally shaping prompts. | 有意识地设计提示内容的方法。 |
| one type of instruction | 一种指令类型 | A system prompt is one possible kind of instruction. | 系统提示只是指令中的一种。 |
| system instructions | 系统指令 | Instructions supplied at the application/system level. | 应用或系统层给模型的要求。 |
| application-supplied instruction | 应用提供的指令 | Guidance supplied by the surrounding application. | 外层应用交给模型的指导。 |
| supplied by an application | 由应用提供 | Given to the model by its host program. | 由使用模型的软件传给模型。 |
| guide the model | 指导模型 | Influence how the model responds or acts. | 引导模型怎样回答或做事。 |
| guide model behavior | 引导模型行为 | Shape likely model behavior through instructions. | 通过要求影响模型表现。 |
| applies to | 适用于 | Can be used with a particular object or layer. | 某种方法可以用于某个对象。 |
| system instructions, user prompts, examples, and task structure | 系统指令、用户提示、示例和任务结构 | Prompt design can cover several parts of an AI interaction. | 提示设计不只写系统提示，还可设计多种内容。 |
| user prompt | 用户提示；用户请求 | The user's request for the current interaction. | 用户这一次发给模型的问题或要求。 |
| user prompts | 用户提示（复数） | Requests supplied by users. | 用户提供的多条请求。 |
| examples | 示例；例子 | Sample inputs or outputs that show a desired pattern. | 用来告诉模型“像这样做”的例子。 |
| task structure | 任务结构 | The organized breakdown of a task. | 把任务拆成清楚组成部分的方式。 |
| system prompt is broader | 系统提示的范围更窄 | A system prompt is only one artifact within prompt design. | 系统提示只是提示设计的一部分。 |
| prompt design is broader than system prompts | 提示设计比系统提示更广 | Prompt design includes more than system-level instructions. | 提示设计还包括用户提示、示例和任务结构。 |
| Prompt Design vs Context Engineering | 提示设计与上下文工程的区别 | A comparison between writing instructions and assembling full model information. | 比较“怎么写要求”和“给模型什么完整资料”。 |
| Context Engineering | 上下文工程 | Designing the complete set of information a model receives. | 设计模型收到的全部信息集合。 |
| context engineering | 上下文工程 | The broader problem of selecting and assembling model context. | 围绕模型上下文进行选择、组织和装配的方法。 |
| complete set of information | 完整信息集合 | All information supplied to the model for a request. | 模型这次实际收到的全部资料。 |
| information the model receives | 模型收到的信息 | Data and instructions included in the model input. | 传给模型的内容总和。 |
| how instructions are written | 指令如何书写 | The wording and organization of directions. | 要求具体怎么写、怎么排。 |
| what complete set of information the model receives | 模型收到的完整信息集合 | The scope of context engineering. | 上下文工程关注模型到底拿到了哪些信息。 |
| broader context-design problem | 更广的上下文设计问题 | The larger challenge of shaping everything supplied to a model. | 不只设计提示，还设计所有输入资料的问题。 |
| context-design problem | 上下文设计问题 | The problem of deciding what information enters the model context. | 决定给模型哪些资料的设计问题。 |
| one part of | ……的一部分 | A component within a broader system. | 不是全部，只是更大事情中的一块。 |
| system prompt, user prompt, history, retrieved documents, tool results, state, and examples | 系统提示、用户提示、历史记录、检索文档、工具结果、状态和示例 | The kinds of information that may make up complete context. | 模型收到的上下文可能由这些内容共同组成。 |
| history | 历史记录；对话历史 | Earlier interaction content included in the current input. | 之前对话中留下、这次仍提供给模型的内容。 |
| conversation history | 对话历史 | Earlier turns of a conversation. | 前面几轮的聊天内容。 |
| retrieved documents | 检索到的文档 | Documents selected to provide task-relevant information. | 系统找出来给模型参考的资料。 |
| retrieval | 检索 | Finding information relevant to the current task. | 从资料库中找相关信息。 |
| tool results | 工具结果 | Information returned by a tool and supplied to the model. | 工具调用后返回给模型的数据。 |
| tool result | 工具结果 | One result returned from an external or application tool. | 一次工具调用返回的一份结果。 |
| tool | 工具 | An external capability an application may expose to a model. | 应用允许模型使用的外部功能。 |
| state | 状态 | Current information about an application or task. | 系统当前记住的情况。 |
| current state | 当前状态 | The state relevant at the time of the request. | 这一次处理时系统所处的情况。 |
| complete context | 完整上下文 | The full information assembled for the model. | 传给模型的所有相关内容。 |
| model input | 模型输入 | The complete content sent into model processing. | 送进模型的文字、资料和其他信息。 |
| input | 输入 | Content received by the model. | 模型接收到的内容。 |
| assembled input | 组装后的输入 | Input formed from several context sources. | 把多种资料合在一起后的输入。 |
| full input | 完整输入 | Everything supplied to the model for one request. | 模型这次收到的全部东西。 |
| Prompt Design is one part of the broader context-design problem | 提示设计是更广泛上下文设计问题的一部分 | Writing instructions is not the same as designing all model input. | 只把要求写好，并不等于把所有上下文都设计好。 |
| common prompt problems | 常见提示问题 | Recurring failures in prompt structure. | 提示写法中经常出现的缺陷。 |
| vague task | 模糊任务 | A task stated without enough detail. | 没说清楚具体要做什么的任务。 |
| VAGUE TASK | 模糊任务 | The problem label for “Analyze this.” | 页面中任务描述过于模糊的类别。 |
| “Analyze this.” | “分析这个。” | An example of a vague task. | 只说分析，却没有目标、依据或输出要求。 |
| missing context | 缺少上下文 | Required background information is unavailable. | 完成任务需要的资料没有给出。 |
| MISSING CONTEXT | 缺少上下文 | The problem label for unavailable required information. | 页面中背景资料不足的类别。 |
| required information is unavailable | 所需信息不可用 | Information needed for the task cannot be accessed. | 任务需要的资料当前拿不到。 |
| unclear constraints | 不清楚的约束 | Rules or limits are not stated precisely. | 没写清模型应该遵守哪些限制。 |
| UNCLEAR CONSTRAINTS | 不清楚的约束 | The problem label for ambiguous rules. | 页面中限制条件含糊的类别。 |
| unwanted assumptions by the model | 模型作出不希望的假设 | The model fills unclear boundaries with guesses. | 规则没说清时模型可能自行脑补。 |
| unclear output | 不清楚的输出要求 | The expected answer form is not specified. | 没说清最后要返回什么样的结果。 |
| UNCLEAR OUTPUT | 不清楚的输出要求 | The problem label for an ambiguous result form. | 页面中输出要求不明确的类别。 |
| result is hard for an application to use | 结果难以被应用使用 | An unstructured answer is difficult for software to consume. | 结果不规范，程序不好接着处理。 |
| What good prompt design does not guarantee | 好的提示设计不能保证什么 | Limits that remain even when a prompt is clear. | 提示写得好也不能保证的事情。 |
| good prompt | 好的提示 | A clear prompt with a well-defined task and boundaries. | 任务、依据、限制和结果都写得比较清楚的提示。 |
| Good prompt ≠ correct answer | 好提示不等于正确答案 | Clear wording can improve clarity but cannot ensure correctness. | 写得清楚不代表模型一定答对。 |
| correct answer | 正确答案 | An answer that is factually and task-wise right. | 内容真实且符合任务要求的答案。 |
| correctness | 正确性 | Whether an answer is right. | 答案到底对不对。 |
| improve task clarity | 提高任务清晰度 | Make the requested work easier to understand. | 让模型更明白要做什么。 |
| does not guarantee correctness | 不保证正确性 | Clear instructions cannot ensure every answer is right. | 提示再清楚，也不能保证每次都正确。 |
| Good prompt ≠ current knowledge | 好提示不等于当前知识 | Wording alone does not supply fresh information. | 提示写得好不会自动带来最新资料。 |
| current knowledge | 当前知识；最新知识 | Information that is up to date for the request. | 与当前时间和现实一致的资料。 |
| fresh information | 新鲜信息；最新信息 | Recently updated information not already in the prompt. | 最近发生或刚更新的资料。 |
| fresh data | 最新数据 | Up-to-date data available for the task. | 当前最新的数据。 |
| wording | 措辞；文字表达 | The words and phrasing used in a prompt. | 提示里具体使用的文字。 |
| prompt wording | 提示措辞 | The wording used to state instructions. | 写提示时采用的表达方式。 |
| does not automatically provide fresh information | 不会自动提供最新信息 | Prompt wording does not fetch new facts by itself. | 只改文字，不会自动联网或更新知识。 |
| automatically | 自动地 | Without a separate action or capability. | 不需要另外操作就自行发生。 |
| provide | 提供 | Make information available to the model. | 把资料交给模型使用。 |
| Good prompt ≠ tool access | 好提示不等于工具访问权限 | Instructions alone do not grant external capabilities. | 写在提示里的要求不会自动变出工具。 |
| tool access | 工具访问权限 | Permission or capability to use an external tool. | 模型是否真的能调用外部功能。 |
| external capabilities | 外部能力 | Functions outside the model's text generation. | 模型本身以外的操作能力。 |
| external capability | 外部能力 | One ability provided by a surrounding system. | 外部系统提供的一项功能。 |
| permission | 权限 | Authorization to perform an action or access a tool. | 系统允许模型做某件事的资格。 |
| capability | 能力；功能 | What the model or application is able to do. | 模型或应用实际能完成的事情。 |
| instructions do not automatically give permission | 指令不会自动赋予权限 | Asking for an action is not the same as being authorized to do it. | 提示里要求做某事，不等于系统真的允许。 |
| instructions do not automatically give external capabilities | 指令不会自动提供外部能力 | Prompt text cannot create unavailable tools. | 提示文字不能凭空创造外部功能。 |
| related design concepts | 相关设计概念 | Concepts connected to prompt design. | 和提示设计有关的其他概念。 |
| concept | 概念 | An idea or term used to explain a design problem. | 用来说明问题的一种想法或术语。 |
| concept tree | 概念树 | A visual grouping of related concepts. | 把相关概念放在一起看的关系图。 |
| Prompt Design → System Prompts | 提示设计 → 系统提示 | A related-concept relationship shown on the page. | 页面把系统提示列为相关概念。 |
| Prompt Design → Context Engineering | 提示设计 → 上下文工程 | A related-concept relationship shown on the page. | 页面把上下文工程列为相关概念。 |
| Prompt Design → Structured Outputs | 提示设计 → 结构化输出 | A related-concept relationship shown on the page. | 页面把结构化输出列为相关概念。 |
| Structured Outputs | 结构化输出 | Outputs constrained to a defined structure. | 按规定结构返回的结果。 |
| structured outputs | 结构化输出（复数） | Multiple responses following a defined structure. | 多个符合既定结构的结果。 |
| related, not a strict pipeline | 相关但不是严格流水线 | The listed concepts connect without forming mandatory sequential steps. | 它们有关联，但不代表必须按固定顺序执行。 |
| strict pipeline | 严格流水线 | A fixed sequence where every stage must follow the previous one. | 每一步都必须按固定顺序走的流程。 |
| pipeline | 流程；流水线 | A sequence of connected processing stages. | 一串前后相连的处理步骤。 |
| Remember this | 记住这一点 | The page's final takeaway section. | 页面最后要记住的核心结论。 |
| make the task, context, constraints, and expected output clear | 让任务、上下文、约束和预期输出清楚 | The final summary of what prompt design does. | 提示设计就是把四类要求说清楚。 |
| expected output | 预期输出 | The result form the model is expected to return. | 希望模型交付的结果形式。 |
| clear to the model | 对模型清楚 | Stated in a way the model can interpret. | 写到模型比较容易理解。 |
| independent explainer | 独立讲解资源 | An external explanatory resource. | 用来补充讲解主题的外部资源。 |
| video | 视频 | A media resource associated with the topic. | 主题页面预留的视频内容。 |
| resource pending | 资源待补充 | The page says a verified video is not available yet. | 视频资源目前还没准备好。 |
| no verified video resource is available yet | 目前没有已验证的视频资源 | No confirmed video is supplied on the page. | 页面现在没有确认可靠的视频。 |
| verified resource | 已验证资源 | A resource whose availability or reliability has been checked. | 已经检查过来源或可用性的资料。 |
| core idea | 核心思想 | The central point of the topic. | 这页最重要的主旨。 |
| core idea: prompt design makes the task explicit | 核心思想：提示设计让任务明确 | The page's first practical conclusion. | 提示设计首先是把任务直接写清楚。 |
| definition | 定义 | A statement explaining what a term means. | 对一个概念是什么的说明。 |
| lede | 导语；摘要引言 | The short introductory sentence below the title. | 标题下方用一句话概括主题的介绍。 |
| on-page navigation | 页面内导航 | Links to sections on the same page. | 帮读者跳到页面不同部分的链接。 |
| Core idea | 核心思想 | The navigation label for the definition section. | 页面导航中的定义部分。 |
| Four useful parts | 四个有用部分 | The navigation label for the four-part explanation. | 页面导航中的四部分章节。 |
| One real example | 一个真实示例 | The navigation label for the invoice example. | 页面导航中的发票示例章节。 |
| Key distinctions | 关键区别 | The navigation label for concept comparisons. | 页面导航中的概念区别章节。 |
| Common problems | 常见问题 | The navigation label for prompt failures. | 页面导航中的问题章节。 |
| What it does not guarantee | 它不保证什么 | The navigation label for prompt-design limits. | 页面导航中的限制章节。 |
| Related concepts | 相关概念 | The navigation label for connected design terms. | 页面导航中的关联概念章节。 |
| Video | 视频 | The navigation label for the media placeholder. | 页面导航中的视频章节。 |

## Potential Missing Concepts

The page does not define these as formal source concepts, but they are plausible glossary follow-ups or useful audit targets for a later pass. They remain outside the source-grounded candidate table so they are not mistaken for page-defined claims.

- Prompt engineering / prompting / prompt authoring
- Prompt template / prompt schema / reusable prompt
- Few-shot prompting / zero-shot prompting / one-shot prompting
- Chain-of-thought prompting / reasoning prompt / hidden reasoning
- Role prompting / persona prompting
- Delimiters / XML tags / section markers
- Instruction hierarchy / priority / conflict resolution
- Developer message / system message / user message
- Context window / token budget / context length
- Retrieval-augmented generation (RAG) / grounding / citations
- Tool calling / function calling / action authorization
- Structured output schema / JSON schema / schema validation
- Guardrails / safety policy / refusal behavior
- Prompt injection / jailbreak / instruction hijacking
- Hallucination / unsupported claim / fabricated value
- Temperature / sampling / randomness / determinism
- Model capability / model limitation / model selection
- Evaluation set / test case / regression test / benchmark
- Prompt quality / task success rate / answer accuracy / factuality
- Format compliance / schema compliance / constraint adherence
- Precision / recall / F1 score / exact match / pass rate
- Latency / cost / token usage / throughput
- Robustness / consistency / reproducibility / variance across runs
- Human review rate / escalation rate / error rate
- Freshness / recency / source authority / provenance
- Data privacy / sensitive information / access control
- Confidence / uncertainty / abstention / “insufficient information”
- Input validation / output validation / post-processing
- Prompt versioning / experiment log / A/B test
- Model training / fine-tuning / instruction tuning / learned behavior
- Current knowledge and web/search access

## Aliases / Synonyms

- Prompt Design / prompt design / prompt designing / prompt authoring / prompt construction
- prompt / prompt text / prompting text / model request / instruction set
- task / requested task / current task / requested work / goal
- context / relevant context / task context / background information / supporting information
- constraints / constraint / rules / requirements / limits / boundaries
- output / expected output / expected result / answer / response / result
- structured output / structured outputs / structured response / fielded response / schema-shaped response
- system prompt / system prompts / system instruction / system instructions / application-level instruction / application guidance
- user prompt / user prompts / user request / current request / current-turn request
- context engineering / context design / context assembly / full-input design
- tool result / tool results / returned tool information / tool output
- retrieved document / retrieved documents / selected source material / retrieved context
- invoice / attached invoice / provided invoice / source invoice
- field / fields / information field / data field / output field
- missing field / missing fields / missing value / missing values / absent information
- do not invent / do not make up / do not guess / do not fabricate / avoid unsupported values
- review / inspect / check / examine / audit
- clear goal / explicit goal / stated objective / task purpose
- clear evidence / specified evidence / supplied evidence / allowed source
- clear output / specified output / defined output / expected format
- application / AI application / host application / surrounding program
- model / AI model / language model / model component
- tool access / external access / capability access / permission to use a tool
- current knowledge / fresh information / up-to-date information / recent information
- video / explainer video / independent explainer / media resource

## Do Not Confuse Candidates

- **Prompt design vs prompt**: Prompt design is the practice; a prompt is the concrete text or input being designed.
- **Prompt design vs prompt engineering**: The page uses “prompt design”; prompt engineering is a related broader label that is not defined on this page.
- **Task vs goal**: The task is the work to perform; the goal is the intended purpose or success direction.
- **Task vs context**: The task says what to do; context supplies information that helps do it.
- **Context vs constraints**: Context is relevant information; constraints are rules or limits on the work.
- **Constraints vs output**: Constraints govern how the task should be performed; output describes the returned result.
- **Output format vs output content**: Format is the shape or organization; content is what the answer says.
- **Output vs result**: The page uses both as everyday labels for what the model returns; later normalization should preserve the exact source form.
- **Clear prompt vs correct answer**: A clear request improves task clarity but does not guarantee correctness.
- **Fresh information vs prompt wording**: Better wording does not automatically add current knowledge.
- **Tool access vs tool instruction**: Asking to use a tool is not the same as actually having permission or capability to use it.
- **Permission vs capability**: Permission is authorization; capability is whether the system can perform the action.
- **System prompt vs prompt design**: A system prompt is one type of instruction; prompt design can also cover user prompts, examples, and task structure.
- **System prompt vs user prompt**: A system prompt is application-supplied guidance; a user prompt is the request for the current interaction.
- **Context engineering vs prompt design**: Prompt design concerns how instructions are written; context engineering concerns the complete information set received by the model.
- **Complete context vs prompt**: The complete context may include prompts plus history, documents, tool results, state, and examples.
- **Retrieved documents vs context engineering**: Retrieved documents are one possible context source; context engineering is the broader assembly problem.
- **Tool results vs retrieved documents**: Tool results come back from a tool; retrieved documents are selected source materials.
- **History vs current request**: History is earlier interaction content; the current request is what must be handled now.
- **State vs history**: State is current application/task information; history is prior interaction content.
- **Examples vs rules**: Examples demonstrate a pattern; rules explicitly state requirements.
- **Structured output vs output format**: Structured output is a result following a structure; output format is the requirement describing the result shape.
- **Field vs value**: A field is a named information slot; a value is the content placed in that slot.
- **Missing field vs empty field**: A missing field is absent; an empty field exists but has no value.
- **Missing value vs invented value**: A missing value is unavailable; an invented value is an unsupported guess inserted in its place.
- **Invoice vs invoice field**: An invoice is the whole document; a field is one piece of information in it.
- **Review vs correctness**: Review is the act of examining a result; correctness is whether the result is actually right.
- **Clear evidence vs authoritative evidence**: Clear evidence is identified as the source to use; authority concerns whether that source deserves trust, which the page does not define.
- **Application vs model**: The application is the surrounding product or program; the model is the AI component it uses.
- **External capability vs model capability**: External capability comes from an attached system or tool; model capability comes from the model itself.
- **Related concept vs pipeline stage**: The page says related concepts are not a strict pipeline, so their relationship is not a mandatory sequence.
- **Resource pending vs verified resource**: “Resource pending” means the page has no verified video yet; it does not mean the topic lacks all possible external explanations.
- **AI vs AI model**: AI is the broad field/category; an AI model is a particular learned system used in an application.
- **Current knowledge vs current context**: Current knowledge is up-to-date information; current context is everything supplied for this request.
- **Vague task vs missing context**: A vague task is unclear about the work; missing context lacks information needed to perform an otherwise clear task.
- **Unclear constraints vs unclear output**: Unclear constraints leave rules ambiguous; unclear output leaves the required answer form ambiguous.
- **Bad example vs weak request**: “BAD” is the example label; “weak request” describes why the request is insufficient.
- **Better example vs better designed request**: “BETTER” is the example label; “better designed request” describes the improved construction.
- **Status vs issues**: Status summarizes the outcome; issues list specific problems found.
- **Missing_fields vs notes**: `missing_fields` is a named list of absent fields; `notes` is for additional explanation.

## Notes

- The source file was read in full, including the title, meta-level topic framing visible through the page, lede, on-page navigation, core-idea comparison, four useful parts, invoice example, key distinctions, context-engineering comparison, common prompt problems, limitation cards, related-concept tree, takeaway, and video placeholder.
- Primary source wording emphasizes: prompt design, structuring instructions, task, relevant context, constraints, expected result/output, explicitness, request quality, invoice review, attached/provided evidence, required fields, missing values, rules, assumptions, status, issues, output fields, system prompts, user prompts, examples, task structure, context engineering, history, retrieved documents, tool results, state, structured outputs, correctness, current knowledge, fresh information, tool access, permission, external capabilities, and application usability.
- The four core parts are retained as both uppercase labels (`TASK`, `CONTEXT`, `CONSTRAINTS`, `OUTPUT`) and explanatory question phrases because the raw stage preserves visible surface forms.
- The two invoice examples are retained separately. “Return status and issues” and “Return: status, missing_fields, notes.” are not silently collapsed because they specify different output forms in the source.
- The source explicitly uses “do not invent missing fields” and “Do not invent missing values”; both variants are retained, along with “missing fields,” “required fields,” “missing values,” and “issues.”
- The source says not every prompt needs all four parts explicitly. This is retained as a candidate and should not be normalized into a claim that every prompt must have four labeled sections.
- The source contrasts Prompt Design with System Prompt and Context Engineering. These are comparison relationships, not a claim that they form a strict pipeline.
- The page says context engineering may include system prompt, user prompt, history, retrieved documents, tool results, state, and examples. These are retained as individual candidates even though the page does not explain retrieval algorithms, trust boundaries, or tool protocols.
- The source's “good prompt” cards explicitly deny guarantees of correctness, current knowledge, and tool access. Prompt clarity is therefore treated as a design aid, not as a guarantee, knowledge refresh mechanism, or permission mechanism.
- No explicit numeric metric, benchmark, abbreviation beyond “AI,” or formal evaluation procedure appears in the source body. Metric, benchmark, and evaluation terms are listed under Potential Missing Concepts rather than presented as source-defined facts.
- “vs” is retained as a visible comparison abbreviation. “AI” is retained as the visible acronym in the page's AI model/application language. No unsupported acronym is added to the source-grounded table.
- The video section is a placeholder marked “resource pending,” and the page states that no verified video resource is currently available. This is retained as page metadata, not as a glossary claim about prompt design itself.
- Raw-stage policy: preserve capitalization, singular/plural variants, exact source phrases, punctuation-bearing examples, labels, field names, related concepts, aliases, and plausible easily-confused concepts. Do not deduplicate or prune at this stage.
- No website files, CSS, scripts, video assets, or GitHub state were modified.
