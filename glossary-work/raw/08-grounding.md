# Topic

Grounding

## Topic Metadata

- Requested Module: 08
- Page Module: 05 · Embeddings, RAG & Vector Search
- Page Topic: Topic 04 · Grounding
- Topic Title: What is Grounding?
- Source File: `grounding.html`
- Source Page Description: Grounding connects an AI response to trusted information supplied at runtime.
- Collection Mode: Raw, maximum candidate collection; candidates are intentionally not deduplicated, merged, or reduced.
- Source Page Language: English page with English UI labels and examples.

## Glossary Candidates

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Grounding | 接地；基于外部依据的生成 | Connecting an AI response to trusted information supplied at runtime. | 让 AI 回答建立在当前提供的可靠资料上。 |
| grounding | 接地；外部信息约束 | The practice of tying an answer to evidence available for the current task. | 把回答和这次任务能拿到的证据联系起来。 |
| grounded answer | 有依据的回答；接地回答 | An answer produced with supplied external evidence in view. | 参考了外部资料后生成的回答。 |
| ground an AI response | 让 AI 回答有依据 | Give an AI response a trusted evidence base at runtime. | 在回答时给 AI 一份可信资料作为依据。 |
| AI response | AI 回应 | A response produced by an AI system. | AI 系统返回的一段回答。 |
| response | 回应；响应 | An output returned in response to a question or task. | 系统针对问题或任务返回的结果。 |
| answer | 答案；回答 | A response written for a question or request. | 针对问题或请求写出的回答。 |
| trusted information | 可信信息 | Information considered reliable enough to use for the task. | 被认为可靠、可以拿来参考的信息。 |
| trusted source | 可信来源 | A source selected as reliable for a task. | 被选定为可靠的资料来源。 |
| external information | 外部信息 | Information coming from outside the model’s learned parameters. | 不只是模型原本记住的、从外部提供的信息。 |
| external evidence | 外部证据 | Evidence supplied from outside the model. | 从模型外部拿进来、用来支持回答的资料。 |
| evidence | 证据；依据 | Information that supports an answer or claim. | 用来证明或支撑回答和说法的信息。 |
| evidence base | 证据基础 | The collection of evidence used to support an answer. | 支撑回答的一组资料。 |
| supplied information | 提供的信息 | Information made available to the system for the current task. | 为当前任务提供给系统的信息。 |
| information supplied at runtime | 运行时提供的信息 | Information added while the system is handling a request. | 系统正在处理请求时临时加入的资料。 |
| runtime | 运行时 | The period when a system is executing a request. | 程序真正运行、处理当前请求的时间。 |
| runtime information | 运行时信息 | Information available during execution rather than only training. | 运行时才提供给系统、不是只在训练时出现的信息。 |
| current task | 当前任务 | The task being handled now. | 系统现在正在处理的事情。 |
| current request | 当前请求 | The user request currently being processed. | 用户这次发来的请求。 |
| current context | 当前上下文 | Information relevant to the request being handled. | 与这次问题有关的背景和资料。 |
| model | 模型 | A learned mechanism that produces outputs from inputs. | 根据输入产生结果的学习系统。 |
| AI model | 人工智能模型 | A model used to perform an AI task. | 用来完成 AI 任务的模型。 |
| learned pattern | 学到的模式 | A relationship learned from training examples. | 模型从训练例子中总结出的规律。 |
| plausible text | 看起来合理的文本 | Text that sounds reasonable even if it is not supported or correct. | 读起来像真的、但不一定有证据或正确的文字。 |
| generate plausible text | 生成看似合理的文本 | Produce text that appears reasonable from learned patterns. | 根据学到的规律写出看上去合理的话。 |
| learned patterns | 学到的规律 | Patterns retained by a model after learning from data. | 模型训练后保留下来的规律。 |
| specific evidence | 针对性的证据 | Evidence selected for the particular task or question. | 专门针对当前问题找来的资料。 |
| task evidence | 任务证据 | Evidence used to answer the current task. | 用来完成当前任务的依据。 |
| source | 来源 | A place or object from which information comes. | 信息来自的资料、系统或记录。 |
| source material | 来源材料 | Material supplied as information for a task. | 提供给系统参考的原始资料。 |
| source document | 来源文档 | A document used as the source of evidence. | 作为依据的原始文档。 |
| document | 文档 | Written material that can be supplied or retrieved. | 可以被读取、检索或参考的文字材料。 |
| documents | 文档；文件 | Multiple pieces of written source material. | 多份可以参考的文字资料。 |
| database | 数据库 | A stored collection of records that can be queried. | 按记录保存、可以查询的数据集合。 |
| database record | 数据库记录 | One stored item or row in a database. | 数据库里保存的一条资料。 |
| database records | 数据库记录（复数） | Stored records that can provide current facts. | 可以提供当前事实的多条数据库记录。 |
| web result | 网页结果；网络检索结果 | Information returned from a web search or web source. | 从网络搜索或网页来源拿回来的结果。 |
| web results | 网页结果（复数） | Multiple results returned from the web. | 从网页或网络检索中得到的多条资料。 |
| tool output | 工具输出 | Information returned by an external tool. | 外部工具执行后返回给模型的信息。 |
| tool outputs | 工具输出（复数） | Outputs returned by one or more external tools. | 一个或多个工具返回的结果。 |
| company record | 公司记录 | A record maintained by an organization. | 公司内部保存的一条业务资料。 |
| company records | 公司记录（复数） | Organizational records used as evidence. | 公司内部保存、可供查询的多条记录。 |
| user-provided file | 用户提供的文件 | A file supplied by the user for the current task. | 用户这次上传或提供给系统的文件。 |
| user-provided files | 用户提供的文件（复数） | Files supplied by a user as task evidence. | 用户提供、供系统参考的多份文件。 |
| file | 文件 | A stored piece of user or system information. | 电脑中保存的一份资料。 |
| input | 输入 | Information given to a system. | 送进系统的信息。 |
| question | 问题 | A request for information or an answer. | 用户希望系统回答的事情。 |
| user question | 用户问题 | A question submitted by the user. | 用户实际提出的问题。 |
| user asks | 用户提出的问题 | What the user requests the system to address. | 用户要求系统处理或回答的内容。 |
| need | 需求 | The information or outcome a user requires. | 用户真正需要知道或完成的事情。 |
| identify the need | 识别需求 | Determine what information or outcome is required. | 先弄清用户到底要什么。 |
| understand the question | 理解问题 | Determine the meaning and scope of the request. | 弄清问题的意思和范围。 |
| task scope | 任务范围 | The limits of what the current task covers. | 这次任务要处理、不能超出的范围。 |
| retrieve | 检索；取回 | Find and bring back relevant information. | 从资料库或来源中找回相关信息。 |
| retrieval | 检索 | The process of finding relevant external information. | 从外部资料中找相关内容的过程。 |
| information retrieval | 信息检索 | Finding information that matches a need or query. | 根据需求或问题找回信息。 |
| retrieve evidence | 检索证据 | Find evidence relevant to the question. | 找到能支持当前问题的资料。 |
| find evidence | 查找证据 | Locate information that can support an answer. | 找到可以支撑回答的依据。 |
| fetch information | 获取信息 | Bring information from a source into the task. | 从来源取资料给当前任务使用。 |
| fetch trusted information | 获取可信信息 | Retrieve information from a trusted source. | 从可靠来源取回资料。 |
| relevant information | 相关信息 | Information connected to the question or task. | 和问题真正有关的信息。 |
| relevant evidence | 相关证据 | Evidence that directly helps answer the question. | 能直接帮助回答问题的依据。 |
| trusted and relevant information | 可信且相关的信息 | Information that is both reliable and useful for the request. | 既可靠又确实和问题有关的资料。 |
| relevance | 相关性 | How closely information matches the task. | 资料和问题贴不贴合。 |
| relevant | 相关的 | Connected to the request in a useful way. | 对当前问题有关系、有帮助的。 |
| trusted | 可信的 | Reliable enough for the intended use. | 可靠程度足以用于当前目的的。 |
| source selection | 来源选择 | Choosing which source should supply evidence. | 决定应该相信和使用哪个来源。 |
| source authority | 来源权威性 | The degree to which a source is authoritative. | 一个来源在该领域有多值得信任。 |
| freshness | 新鲜度；时效性 | How current the information is. | 资料是不是最新的。 |
| current information | 当前信息 | Information that reflects the present or latest available state. | 反映现在情况的资料。 |
| current HR document | 当前 HR 文档 | The latest or applicable human-resources document. | 公司目前适用的人力资源文件。 |
| current database records | 当前数据库记录 | Up-to-date records retrieved from a database. | 数据库中最新的业务记录。 |
| current | 当前的；最新的 | Available or applicable now. | 现在有效或现在能拿到的。 |
| add context | 添加上下文 | Put supporting information into the model’s context. | 把资料放进模型当前能看到的背景里。 |
| context | 上下文；背景 | Information available to help interpret and answer a request. | 帮助模型理解问题并回答的背景资料。 |
| model context | 模型上下文 | The information the model can use for the current generation. | 模型这次生成时能看到的全部背景。 |
| context window | 上下文窗口 | The bounded amount of input a model can consider at once. | 模型一次能放进去并处理的信息容量。 |
| supply the evidence | 提供证据 | Place evidence where the model can use it. | 把证据交给模型作为参考。 |
| place evidence into context | 将证据放入上下文 | Add retrieved evidence to the model’s input context. | 把检索结果加入模型输入的背景。 |
| supplied evidence | 已提供的证据 | Evidence made available to the model. | 已经交给模型参考的资料。 |
| context construction | 上下文构建 | Building the information package used for generation. | 把问题和相关资料整理成模型要看的输入。 |
| context assembly | 上下文组装 | Combining user input and supporting evidence. | 将用户问题和证据拼成一份上下文。 |
| generate | 生成 | Produce an answer or other output. | 根据输入产出新的结果。 |
| generation | 生成 | The act of producing a model output. | 模型产出回答或内容的过程。 |
| write the answer | 撰写回答 | Produce a response to the question. | 把问题的答案写出来。 |
| answer generation | 答案生成 | Generating an answer from the request and context. | 根据问题和上下文生成回答。 |
| use the supplied evidence | 使用已提供的证据 | Base the response on the evidence placed in context. | 回答时参考已经提供的资料。 |
| evidence-grounded generation | 基于证据的生成 | Generation guided by supplied evidence. | 依据外部证据生成内容。 |
| response generation | 回应生成 | Producing the final response for a request. | 为用户请求生成最终回应。 |
| generated answer | 生成的答案 | An answer produced by the model. | 模型生成出来的回答。 |
| verify | 验证；核验 | Check whether a result and its claims are supported. | 检查结果和说法是否有依据、是否正确。 |
| verification | 验证；核验 | The process of checking a result. | 检查结果的过程。 |
| check the result | 检查结果 | Review the generated answer for support or correctness. | 看生成的回答是否可靠。 |
| result | 结果 | What the system produces after processing. | 系统处理后得到的东西。 |
| important claim | 重要主张 | A claim that matters enough to require checking. | 对结论很重要、需要重点核对的说法。 |
| claim | 主张；陈述 | A statement presented as true or supported. | 回答中声称为事实的一句话。 |
| show citations | 展示引用 | Display references supporting the answer. | 把回答依据的来源列出来。 |
| citation | 引用；出处 | A reference that points to supporting information. | 指向原始资料的出处标记。 |
| citations | 引用；出处（复数） | References attached to claims or answers. | 回答中列出的多个资料出处。 |
| citation support | 引用支持 | The relationship between a claim and its source. | 引用能不能真的支撑这句话。 |
| source citation | 来源引用 | A citation identifying the source used. | 标出回答资料来自哪里。 |
| review important claims | 复核重要主张 | Check the most consequential statements. | 重点核对会影响结论的说法。 |
| factual support | 事实支持 | Evidence that supports a factual statement. | 能证明事实说法的资料。 |
| answer correctness | 回答正确性 | Whether an answer is factually right. | 回答内容是不是正确。 |
| factual accuracy | 事实准确性 | Agreement between an answer and the underlying facts. | 回答与真实事实是否一致。 |
| correctness | 正确性 | Whether a result is right for the task. | 结果是否答对了。 |
| evidence quality | 证据质量 | How reliable, relevant, and sufficient the evidence is. | 证据是否可靠、相关、足够。 |
| source quality | 来源质量 | How trustworthy and useful a source is. | 资料来源本身好不好、靠不靠谱。 |
| evidence coverage | 证据覆盖度 | How much of an answer is supported by evidence. | 回答中有多少内容被资料支撑。 |
| support rate | 支持率 | The share of claims supported by evidence. | 有证据支撑的说法占全部说法的比例。 |
| claim verification | 主张核验 | Checking a claim against its source. | 把一句话和原始资料逐一对照。 |
| source traceability | 来源可追溯性 | The ability to trace an answer back to its source. | 能从回答追查回原始资料的能力。 |
| auditability | 可审计性 | How easily a result and its sources can be reviewed. | 结果和出处是否方便复查。 |
| answer provenance | 回答来源链；出处链 | Information about where an answer came from. | 能说明回答是根据哪些资料产生的。 |
| provenance | 来源追踪；出处 | The history or origin of information. | 一份信息从哪里来、经过什么步骤。 |
| real-world example | 现实世界示例 | An example showing use in an actual setting. | 真实业务或生活场景中的例子。 |
| business example | 商业示例 | An example from an organization’s workflow. | 企业工作流程中的例子。 |
| company policy | 公司政策 | An organization’s official rule or policy. | 公司正式规定的做法。 |
| policy | 政策；规定 | An official rule or guidance for decisions. | 组织规定应该怎样做的规则。 |
| HR | 人力资源（HR） | Human Resources, the function handling people and employment matters. | 负责员工和雇佣事务的部门或职能。 |
| human resources | 人力资源 | The organizational function related to employees and employment. | 与员工、雇佣和福利有关的组织职能。 |
| maternity leave | 产假 | Leave from work related to childbirth. | 员工生育前后可以休的假期。 |
| question about maternity leave | 关于产假的问题 | A user question asking about maternity-leave policy. | 用户询问公司产假规定的问题。 |
| HR document | 人力资源文档 | A document containing an HR rule or policy. | 记录人力资源规定的文件。 |
| retrieve the current HR document | 检索当前 HR 文档 | Find the applicable HR policy document. | 找到目前适用的公司人力资源文件。 |
| answer based on that document | 基于该文档的回答 | An answer supported by the retrieved document. | 以找到的文件为依据给出的答案。 |
| financial data | 财务数据 | Data about money, income, or financial activity. | 关于收入、金额和财务活动的数据。 |
| question about last month’s revenue | 关于上月收入的问题 | A question asking for the previous month’s revenue. | 用户询问上个月赚了多少钱。 |
| last month | 上个月 | The calendar month immediately before the current month. | 当前月份之前的那一个月。 |
| revenue | 收入；营收 | Money earned by a business over a period. | 企业在一段时间内取得的钱。 |
| monthly revenue | 月度收入；月营收 | Revenue measured for one month. | 按一个月统计的收入。 |
| business metric | 业务指标 | A measurable value used to understand a business. | 用数字观察业务表现的量。 |
| financial metric | 财务指标 | A measurable value about financial performance. | 反映财务表现的数字。 |
| retrieve current database records | 检索当前数据库记录 | Fetch up-to-date records from a database. | 从数据库拿回最新记录。 |
| answer based on retrieved data | 基于检索数据的回答 | An answer using data fetched for the request. | 参考这次找回的数据作出的回答。 |
| retrieved data | 检索到的数据 | Data returned by a retrieval step. | 检索步骤找回的数据。 |
| external knowledge | 外部知识 | Knowledge supplied from sources outside the model. | 从外部文件、数据库或工具加入的知识。 |
| knowledge source | 知识来源 | A source that provides information for answering. | 给系统提供知识的文件、库或服务。 |
| knowledge base | 知识库 | An organized collection of information used for lookup. | 把资料整理在一起、供查询的知识集合。 |
| record lookup | 记录查询 | Finding a stored record. | 查找系统里保存的一条记录。 |
| data lookup | 数据查询 | Finding stored data relevant to a request. | 查找和问题有关的数据。 |
| RAG | 检索增强生成（RAG） | A common architecture that retrieves information and uses it for generation. | 先检索资料，再把资料交给模型生成回答的一种架构。 |
| retrieval-augmented generation | 检索增强生成 | Generation augmented with retrieved external information. | 用检索到的外部资料增强生成。 |
| retrieval-enhanced answer | 检索增强的回答 | An answer improved or supported by retrieved information. | 结合检索结果生成的回答。 |
| architecture | 架构 | A structured way to arrange system components. | 系统各部分如何组合工作的设计。 |
| goal | 目标 | The outcome a method is intended to achieve. | 这种方法想达到的结果。 |
| grounding goal | 接地目标 | Tying answers to external evidence. | 让答案和外部依据建立联系。 |
| method | 方法 | A way of accomplishing a task. | 完成事情的一种做法。 |
| implementation | 实现方式 | The concrete way a goal is built in a system. | 把目标真正做进系统的办法。 |
| common architecture | 常见架构 | A frequently used system design. | 很多人用来实现目标的一种系统结构。 |
| fine-tuning | 微调 | Additional training that changes model behavior. | 在已有模型上继续训练，让行为更适合某类任务。 |
| training | 训练 | Learning model behavior from examples or data. | 用数据让模型学习规律的过程。 |
| model behavior | 模型行为 | How a model responds to inputs. | 模型面对不同输入时会怎样回答或行动。 |
| runtime addition | 运行时添加 | Information added while handling a request. | 处理请求时临时加入的信息。 |
| training-time change | 训练阶段变化 | A change made during model training. | 训练模型时改变模型内部行为。 |
| parameter change | 参数变化 | A change to learned numerical values in a model. | 训练时调整模型内部数字。 |
| knowledge update | 知识更新 | Making a system use newer information. | 让系统参考更新后的资料。 |
| model update | 模型更新 | Changing or replacing the trained model. | 重新训练、微调或替换模型。 |
| guaranteed truth | 保证为真；绝对真相 | A guarantee that an answer is true. | 可以百分之百保证正确的答案状态。 |
| truth | 事实真相 | What is actually true. | 现实中真正成立的情况。 |
| guarantee | 保证 | A promise that a result will always hold. | 无论情况怎样都承诺一定成立。 |
| grounding alone | 仅靠接地 | Grounding without additional checking or controls. | 只把资料给模型、没有别的核验措施。 |
| cannot provide | 无法提供 | Not sufficient to guarantee a result. | 单靠这种方法做不到的事情。 |
| better evidence | 更好的证据 | More relevant, reliable, or current support. | 更相关、更可靠或更及时的依据。 |
| evidence quality limit | 证据质量限制 | The fact that grounding inherits weaknesses in its sources. | 来源本身错了，接地也不能自动变对。 |
| source error | 来源错误 | An error already present in the supplied source. | 外部资料本身就写错的地方。 |
| stale information | 过时信息 | Information that is no longer current. | 已经不再适用的旧资料。 |
| incomplete evidence | 不完整证据 | Evidence that does not cover all necessary facts. | 资料只覆盖一部分、缺少关键内容。 |
| conflicting evidence | 相互冲突的证据 | Evidence sources that disagree with each other. | 不同资料给出互相矛盾的说法。 |
| unsupported claim | 无证据支持的主张 | A claim with no adequate supporting evidence. | 回答中没有资料依据的一句话。 |
| hallucination | 幻觉；虚构信息 | A plausible but unsupported or false model output. | 模型说得像真的、其实没有依据或是错误的内容。 |
| hallucination risk | 幻觉风险 | The possibility that a model generates unsupported content. | 模型生成没有依据内容的可能性。 |
| error | 错误；误差 | A result that differs from the facts or task requirement. | 结果和事实或要求不一致。 |
| uncertainty | 不确定性 | Lack of confidence that a result is correct. | 目前不能确定答案对不对的状态。 |
| review | 复核；审核 | Human or system checking of an output. | 对结果再检查一遍。 |
| manual review | 人工复核 | A person checks the output. | 由人来检查 AI 的结果。 |
| human oversight | 人工监督 | People retain responsibility for reviewing or deciding. | 人保留检查、批准和负责的权力。 |
| approval | 批准 | A person or authority accepts a result for use. | 有权限的人确认结果可以使用。 |
| important result | 重要结果 | A result whose consequences justify extra checking. | 结果影响大、值得额外检查。 |
| high-stakes claim | 高风险主张 | A claim where an error could cause serious harm. | 说错了可能造成严重后果的说法。 |
| risk | 风险 | The possibility of harm, error, or loss. | 可能出问题、造成损失或伤害的可能性。 |
| safety | 安全性 | Protection against harmful or unsafe behavior. | 防止系统造成伤害或危险。 |
| reliable | 可靠的 | Consistently useful and trustworthy. | 多数情况下能稳定、可信地工作。 |
| trustworthy | 值得信任的 | Suitable to rely on for the intended task. | 对这个用途来说可以相信的。 |
| useful | 有用的 | Helpful for the user or task. | 对解决问题真正有帮助的。 |
| answer quality | 回答质量 | How correct, relevant, supported, and useful an answer is. | 回答是否答对、相关、有依据、能使用。 |
| task success | 任务成功 | Whether the system achieves the requested outcome. | 系统有没有完成用户要求的事情。 |
| external evidence workflow | 外部证据工作流 | A workflow that retrieves, supplies, generates, and checks evidence-based answers. | 从找资料到给资料、生成、核验的一整套流程。 |
| grounding pipeline | 接地流水线 | The sequence from question through evidence to verified answer. | 从问题到检索、上下文、生成、核验的流程。 |
| process | 流程；处理过程 | A sequence of steps that turns a request into a result. | 从输入到结果的一连串步骤。 |
| process node | 流程节点 | One named step in a workflow. | 流程中一个明确的环节。 |
| question step | 问题步骤 | The first step of identifying the user’s need. | 流程中先理解用户问题的环节。 |
| retrieve step | 检索步骤 | The step that finds relevant evidence. | 流程中查找资料的环节。 |
| context step | 上下文步骤 | The step that supplies evidence to the model. | 流程中把资料放进上下文的环节。 |
| generate step | 生成步骤 | The step that writes the answer. | 流程中产出回答的环节。 |
| verify step | 验证步骤 | The step that checks the result. | 流程中核查结果和引用的环节。 |
| first step | 第一步 | The initial step in a process. | 流程开始时先做的事情。 |
| final step | 最后一步 | The step at the end of a process. | 流程最后检查结果的事情。 |
| five-step process | 五步流程 | Question, Retrieve, Add context, Generate, and Verify. | 先理解问题，再检索、加上下文、生成、验证。 |
| question → retrieve → context → generate → verify | 问题→检索→上下文→生成→验证 | The page’s five-step grounding flow. | 页面展示的接地流程顺序。 |
| identify the need | 识别需求 | Understand what the user asks for. | 弄清用户真正要什么。 |
| understand what the user asks | 理解用户提问 | Determine the requested information or action. | 识别用户希望得到的答案或行动。 |
| find evidence | 找到证据 | Fetch information that supports the task. | 找到可以支持回答的资料。 |
| supply the evidence | 提供证据 | Put evidence into the model’s context. | 将找到的资料交给模型。 |
| write the answer | 写出答案 | Generate the response using the context. | 根据上下文把回答写出来。 |
| check the result | 检查结果 | Verify important claims or show citations. | 检查答案并展示出处。 |
| trusted source → retrieval → context → LLM → grounded answer → citation | 可信来源→检索→上下文→大语言模型→有依据回答→引用 | The page’s related-concept chain. | 页面给出的从来源到最终引用的概念链。 |
| LLM | 大语言模型（LLM） | Large Language Model; a language model that generates or processes text. | 能处理和生成文字的大型语言模型。 |
| large language model | 大语言模型 | A large model trained to work with language. | 规模较大的文字处理和生成模型。 |
| language model | 语言模型 | A model that learns patterns in language. | 学习语言规律并处理文字的模型。 |
| model context | 模型上下文 | The context supplied to an LLM for a response. | 这次回答时交给大语言模型看的背景信息。 |
| grounded LLM answer | 基于依据的 LLM 回答 | An LLM answer connected to retrieved evidence. | 大语言模型参考资料后生成的回答。 |
| citation chain | 引用链 | The links from a claim to its supporting source. | 从回答中的说法追到原始资料的链路。 |
| related concept | 相关概念 | A concept connected to grounding in the page’s map. | 页面认为和 grounding 有联系的概念。 |
| concept tree | 概念树 | A compact chain showing relationships among concepts. | 用箭头展示概念之间关系的结构。 |
| RAG chip | RAG 相关入口 | A page link that points to the RAG topic. | 页面上通往 RAG 主题的入口。 |
| Retrieval chip | Retrieval 相关入口 | A page link that points to the Retrieval topic. | 页面上通往 Retrieval 主题的入口。 |
| Context Window chip | Context Window 相关入口 | A page link that points to the Context Window topic. | 页面上通往上下文窗口主题的入口。 |
| Structured Outputs chip | Structured Outputs 相关入口 | A page link that points to the Structured Outputs topic. | 页面上通往结构化输出主题的入口。 |
| Structured Outputs | 结构化输出 | Output constrained to a requested structure or schema. | 按规定字段和格式输出的结果。 |
| context window | 上下文窗口 | The model’s available input capacity for the current request. | 模型一次能容纳的输入背景范围。 |
| prompt | 提示词；提示 | Instructions or input used to guide a model. | 告诉模型要做什么的输入。 |
| prompt context | 提示上下文 | The context included with a prompt. | 和提示一起交给模型的背景资料。 |
| user intent | 用户意图 | What the user actually wants to achieve. | 用户问题背后真正想完成的目标。 |
| task intent | 任务意图 | The intended outcome of the task. | 这次任务最终要达成的目的。 |
| answer with the book open | 打开书回答 | An analogy for answering while consulting a source. | 像翻开书查资料后再回答，而不是只凭记忆。 |
| analogy | 类比 | A comparison used to explain an abstract idea. | 用熟悉的事情帮助理解抽象概念。 |
| book | 书本 | The source used in the page’s analogy. | 页面用来比喻外部资料的书。 |
| book open | 书本打开 | Having a source available while answering. | 回答时资料就在手边可以查。 |
| source available | 来源可用 | A source is accessible for the task. | 当前任务可以访问到资料来源。 |
| analogy limitation | 类比限制 | The analogy explains a role but does not prove correctness. | 类比只能帮助理解作用，不代表答案一定正确。 |
| does not guarantee correctness | 不保证正确 | Having evidence does not by itself ensure the answer is right. | 有资料不等于回答一定正确。 |
| correctness guarantee | 正确性保证 | A guarantee that the result is correct. | 对答案正确的承诺。 |
| evidence role | 证据作用 | The role evidence plays in supporting an answer. | 资料在回答中起到支撑作用。 |
| runtime grounding | 运行时接地 | Grounding information supplied during execution. | 模型运行处理请求时才加入资料。 |
| model knowledge | 模型知识 | Information encoded in model parameters from training. | 模型训练后保存在内部参数里的信息。 |
| parametric knowledge | 参数化知识 | Knowledge encoded in model parameters. | 写进模型参数、随模型一起保存的知识。 |
| non-parametric information | 非参数化信息 | External information supplied without retraining the model. | 不改模型参数、运行时从外部加入的信息。 |
| knowledge cutoff | 知识截止时间 | The latest period covered by the model’s original training knowledge. | 模型原本训练资料覆盖到的时间点。 |
| live data | 实时数据 | Current data supplied from a live source. | 从正在变化的系统中拿到的最新数据。 |
| source freshness | 来源时效性 | How recently a source was updated. | 来源资料距离现在有多新。 |
| temporal grounding | 时间接地 | Grounding an answer in information valid for a specific time. | 确保回答参考的是对应时间有效的资料。 |
| domain grounding | 领域接地 | Grounding an answer in a specific domain’s sources. | 用某个专业领域的资料限制回答。 |
| enterprise grounding | 企业接地 | Grounding responses in an organization’s private information. | 用企业内部文件和记录支持回答。 |
| private data | 私有数据 | Data available only to an organization or user. | 只有特定组织或用户能访问的数据。 |
| proprietary data | 专有数据 | Data owned or controlled by an organization. | 属于某个组织、不能随意公开的数据。 |
| permissions | 权限 | Rules about who may access information. | 谁可以看哪些资料的规定。 |
| access control | 访问控制 | Mechanisms that restrict access to sources or data. | 控制谁能访问资料的机制。 |
| authorized source | 获授权来源 | A source the system is permitted to use. | 系统有权限读取的来源。 |
| unauthorized evidence | 未授权证据 | Information the system should not use or disclose. | 系统不该读取或暴露的资料。 |
| privacy | 隐私 | Protection of personal or sensitive information. | 防止个人或敏感资料被不当使用。 |
| sensitive information | 敏感信息 | Information requiring extra protection. | 泄露后可能造成风险的资料。 |
| data leakage | 数据泄露 | Exposing information to an unauthorized party. | 把不该公开的资料泄露出去。 |
| citation correctness | 引用正确性 | Whether a citation actually supports the claim. | 引用的资料是不是真的能支持这句话。 |
| citation completeness | 引用完整性 | Whether important claims have supporting citations. | 重要说法是不是都给了出处。 |
| citation quality | 引用质量 | The reliability and usefulness of citations. | 引用的来源是否可靠、相关。 |
| retrieval precision | 检索精确率 | The share of retrieved items that are relevant. | 找回的资料中有多少真正相关。 |
| retrieval recall | 检索召回率 | The share of relevant items that were retrieved. | 所有相关资料中有多少被找回来。 |
| top-k retrieval | 前 k 项检索 | Returning the k highest-ranked retrieved items. | 只取排序最前面的 k 条资料。 |
| ranking | 排序 | Ordering candidate information by relevance or value. | 按相关程度给资料排先后。 |
| reranking | 重排序 | Reordering retrieved results with a later scoring step. | 检索后再用一次评分重新排序。 |
| retrieval metric | 检索指标 | A measurement of retrieval quality. | 用数字衡量检索效果的指标。 |
| answer faithfulness | 回答忠实度 | How closely an answer stays supported by the provided evidence. | 回答有没有超出、歪曲提供的资料。 |
| groundedness score | 接地度分数 | A score estimating how well an answer is supported by evidence. | 用数字估计回答有多大程度依赖资料依据。 |
| factuality | 事实性 | The degree to which statements match facts. | 回答和事实相符的程度。 |
| evaluation | 评估 | Systematic measurement of result quality. | 按标准系统检查结果好不好。 |
| grounding evaluation | 接地评估 | Evaluation of retrieval, support, and answer quality. | 检查资料找得对不对、回答有没有依据。 |
| evaluation set | 评估集 | Examples used to measure a system. | 用来测试系统表现的一组例子。 |
| golden answer | 标准答案 | A reference answer used for evaluation. | 用来对照检查的标准答案。 |
| reference answer | 参考答案 | An answer used as a comparison target. | 评估系统回答时拿来对比的答案。 |
| human judgment | 人工判断 | A person’s assessment of an answer. | 由人判断回答是否有用和正确。 |
| source attribution | 来源归因 | Identifying which source contributed to an answer. | 说明回答中哪些内容来自哪个来源。 |
| answer citation | 回答引用 | A source reference attached to an answer. | 附在回答上的资料出处。 |
| explainability | 可解释性 | How understandable the reason for an output is. | 能不能说明系统为什么这样回答。 |
| transparency | 透明性 | How visible the sources and reasoning process are. | 用户能不能看清资料来源和依据。 |
| inspectable evidence | 可检查证据 | Evidence that a person can review directly. | 人可以打开并核对的资料。 |
| review important claims | 复核重要主张 | Inspect high-impact claims against sources. | 对重要说法回到原文逐项检查。 |
| answer limitation | 回答限制 | A boundary on what the system can safely claim. | 系统不应该超出证据声称的范围。 |
| abstention | 拒答；暂不回答 | Declining to answer when evidence is insufficient. | 资料不够时选择不乱答。 |
| insufficient evidence | 证据不足 | Not enough support to answer confidently. | 现有资料不够支撑可靠回答。 |
| answer with uncertainty | 带不确定性回答 | State uncertainty when evidence does not settle the question. | 资料不确定时明确说不能完全确定。 |
| fallback | 备用路径 | An alternative response or process when the main path fails. | 正常流程不行时采用的替代办法。 |
| retrieval failure | 检索失败 | Failure to find usable evidence. | 没有找到可用的相关资料。 |
| source unavailable | 来源不可用 | A needed source cannot be accessed. | 需要的资料来源暂时打不开或不存在。 |
| conflicting sources | 冲突来源 | Sources that provide inconsistent information. | 不同来源给出不一致内容。 |
| conflict resolution | 冲突解决 | A method for handling disagreements among sources. | 资料冲突时决定采用哪个说法。 |
| source priority | 来源优先级 | An order of trust among possible sources. | 不同来源之间谁更应该优先采用。 |
| escalation | 升级处理 | Send an uncertain or risky case to a person or higher process. | 复杂或高风险问题交给更高层或人工处理。 |
| operational workflow | 运营流程 | The process used in a real organization. | 企业日常真正执行的一套工作流程。 |
| downstream system | 下游系统 | A later system that consumes the answer or output. | 接收当前系统结果、继续处理的系统。 |
| downstream use | 下游使用 | A later use of the generated answer. | 生成结果之后的下一步用途。 |
| user-provided context | 用户提供的上下文 | Background information supplied by the user. | 用户主动给系统的背景资料。 |
| application context | 应用上下文 | Context provided by the application around a request. | 产品或程序自动附加的背景信息。 |
| tool call | 工具调用 | A request for an external tool to perform an operation. | 模型让搜索、数据库等外部工具做事情。 |
| tool result | 工具结果 | The information returned by a tool call. | 工具调用完成后返回的资料。 |
| web search | 网络搜索 | Searching the web for relevant sources. | 在网络上查找相关资料。 |
| database query | 数据库查询 | A request sent to a database to retrieve records. | 向数据库发出查找记录的请求。 |
| document search | 文档搜索 | Finding relevant content in documents. | 在文件中查找相关内容。 |
| retrieval query | 检索查询 | The query used to find evidence. | 用来检索资料的问题或查询词。 |
| query | 查询；检索问题 | A request used to search for information. | 交给搜索或数据库查找的内容。 |
| query understanding | 查询理解 | Interpreting what information a query needs. | 弄清检索问题真正想找什么。 |
| semantic retrieval | 语义检索 | Retrieval based on meaning rather than exact words. | 按含义找资料，不只看有没有相同词。 |
| vector search | 向量搜索 | Searching representations for semantically similar items. | 按数字向量的相似程度查找内容。 |
| keyword search | 关键词搜索 | Searching for literal words or phrases. | 按字面关键词查找资料。 |
| lexical match | 词面匹配 | A match based on the actual words used. | 只看文字表面是否匹配。 |
| semantic similarity | 语义相似度 | Similarity based on meaning. | 两段内容意思有多接近。 |
| embedding | 嵌入；向量表示 | A numerical representation used to compare meaning or features. | 把问题和资料变成数字来比较含义。 |
| query embedding | 查询嵌入 | A numerical representation of the query. | 把用户问题变成的数字表示。 |
| document embedding | 文档嵌入 | A numerical representation of a document or chunk. | 把文档或片段变成的数字表示。 |
| vector database | 向量数据库 | A database designed to store and search vectors. | 专门保存并查找向量的数据库。 |
| chunk | 文档片段 | A smaller piece of a document used for retrieval. | 把长文档切成的一小段。 |
| chunking | 文档切分 | Splitting a document into retrieval-sized pieces. | 把长资料切成方便检索的小段。 |
| retrieved context | 检索上下文 | The selected evidence passed to the model. | 检索后挑出来交给模型的资料片段。 |
| source context | 来源上下文 | Context originating from a source document or record. | 来自外部资料的上下文。 |
| context relevance | 上下文相关性 | How well supplied context matches the question. | 放进模型的资料和问题贴不贴合。 |
| context sufficiency | 上下文充分性 | Whether the context contains enough information to answer. | 上下文里的资料够不够回答问题。 |
| context pollution | 上下文污染 | Irrelevant or misleading content added to context. | 把无关或错误资料混进模型背景。 |
| prompt injection | 提示注入 | Instructions in retrieved or user content that try to override system behavior. | 外部资料里藏着会诱导模型违背规则的指令。 |
| untrusted content | 不可信内容 | Content that should not automatically be treated as instructions or facts. | 不能直接相信、也不能直接当命令执行的内容。 |
| instruction hierarchy | 指令层级 | Rules determining which instructions take priority. | 不同指令发生冲突时谁优先的规则。 |
| source instructions | 来源中的指令 | Instructions appearing inside retrieved material. | 外部文档或网页里写着的命令。 |
| evidence vs instruction | 证据与指令 | Evidence supports an answer; an instruction asks the model to act. | 资料是用来证明，指令是要求系统做事。 |
| source grounding | 来源接地 | Grounding an answer in a named source. | 把回答明确建立在某个来源上。 |
| document-grounded answer | 基于文档的回答 | An answer grounded in one or more documents. | 以文档内容为依据的回答。 |
| database-grounded answer | 基于数据库的回答 | An answer grounded in retrieved database records. | 以数据库记录为依据的回答。 |
| web-grounded answer | 基于网页的回答 | An answer grounded in web results. | 以网页检索结果为依据的回答。 |
| file-grounded answer | 基于文件的回答 | An answer grounded in user-provided files. | 以用户文件为依据的回答。 |
| fact lookup | 事实查询 | Looking up a specific fact in a source. | 从资料中查一个明确事实。 |
| policy lookup | 政策查询 | Looking up an applicable organizational policy. | 查公司或组织的具体规定。 |
| financial lookup | 财务查询 | Looking up a financial value or record. | 查一个金额、收入或财务记录。 |
| source-backed response | 有来源支持的回应 | A response supported by identifiable sources. | 回答后面能找到明确资料依据。 |
| evidence-backed response | 有证据支持的回应 | A response supported by evidence. | 回答中的说法有资料支撑。 |
| citation-backed answer | 有引用支持的答案 | An answer accompanied by supporting citations. | 带有出处、方便核对的答案。 |
| answer grounded in retrieved data | 基于检索数据的回答 | A response that uses fetched records or documents. | 用检索到的记录或文档写出的回答。 |
| information at answer time | 回答时的信息 | Information available when the answer is generated. | 生成回答的那个时刻能拿到的资料。 |
| temporal validity | 时间有效性 | Whether information is valid for the relevant time. | 资料在所问时间是否仍然适用。 |
| policy validity | 政策有效性 | Whether a policy is currently applicable. | 一条规定现在是否仍然有效。 |
| data validity | 数据有效性 | Whether retrieved data is valid for use. | 找到的数据是否真实、完整、可用。 |
| fact | 事实 | A statement that corresponds to reality or an authoritative record. | 和现实或权威记录一致的情况。 |
| factual record | 事实记录 | A stored record of a factual value or event. | 记录真实数值或事件的资料。 |
| claim support | 主张支持 | Evidence attached to a claim. | 支撑一句主张的资料。 |
| answer span | 回答片段 | A portion of an answer associated with evidence. | 回答中对应某个资料依据的一小段。 |
| evidence span | 证据片段 | The part of a source that supports a claim. | 原文中真正支持某句话的那一段。 |
| quote | 引文 | A piece of source text reproduced in an answer. | 从原资料摘出来的一段话。 |
| quotation | 引述；引用原文 | Source wording used to support a response. | 用原文措辞支持回答。 |
| source excerpt | 来源摘录 | A selected passage from a source. | 从资料中挑出的相关段落。 |
| supporting passage | 支持性段落 | A passage that supports an answer. | 能支撑回答的一段原文。 |
| answer synthesis | 答案综合 | Combining evidence into a coherent response. | 把多份资料整理成连贯的答案。 |
| multi-source synthesis | 多来源综合 | Combining information from several sources. | 把不同来源的信息合并成回答。 |
| source comparison | 来源比较 | Comparing claims or facts across sources. | 对照多个来源的说法。 |
| source reconciliation | 来源调和 | Resolving differences among sources. | 发现来源冲突后做统一处理。 |
| evidence aggregation | 证据聚合 | Combining multiple pieces of evidence. | 把多条资料合起来支持结论。 |
| claim decomposition | 主张拆解 | Breaking a broad answer into checkable claims. | 把大结论拆成一句句可核对的说法。 |
| answer drafting | 答案起草 | Producing a first version of the answer. | 先写出一个还需要检查的版本。 |
| final answer | 最终答案 | The response delivered after generation and checks. | 经过必要检查后交给用户的回答。 |
| answer revision | 回答修订 | Changing an answer after reviewing evidence. | 根据核验结果修改回答。 |
| correction | 更正 | A change that fixes an error. | 把错误的内容改正确。 |
| source link | 来源链接 | A link that lets a user inspect the source. | 用户可以点开查看原始资料的链接。 |
| document ID | 文档 ID | An identifier for a source document. | 用来定位某份文档的编号。 |
| record ID | 记录 ID | An identifier for a database record. | 用来定位某条记录的编号。 |
| metadata | 元数据 | Descriptive information about a source or record. | 描述资料来源、时间、类别等的信息。 |
| source metadata | 来源元数据 | Metadata describing where and when information came from. | 说明资料来源、更新时间等的附加信息。 |
| timestamp | 时间戳 | A recorded time associated with data or an event. | 标记资料或事件发生时间的记录。 |
| update time | 更新时间 | The time when a source or record was last updated. | 资料最近一次被更新的时间。 |
| version | 版本 | A particular state of a source or policy. | 一份资料在某个时点的具体版本。 |
| document version | 文档版本 | A specific revision of a document. | 文档经过修改后的某一版。 |
| policy version | 政策版本 | A specific revision of a policy. | 公司政策的某个正式版本。 |
| source snapshot | 来源快照 | A captured state of a source at a time. | 某个时间点保存下来的资料状态。 |
| retrieval log | 检索日志 | A record of what was searched and returned. | 记录系统查了什么、找到什么的日志。 |
| audit log | 审计日志 | A record used to review system activity. | 方便追查系统做过什么的记录。 |
| observability | 可观测性 | The ability to inspect system behavior and outcomes. | 能看见系统处理过程和结果的程度。 |
| monitoring | 监控 | Ongoing observation of quality and failures. | 持续观察系统质量和异常。 |
| grounding monitoring | 接地监控 | Monitoring source use, support, freshness, and answer quality. | 持续观察资料、引用和回答是否可靠。 |
| production | 生产环境 | The live environment where users receive results. | 真正给用户提供服务的运行环境。 |
| production data | 生产数据 | Current data from a live business system. | 正在真实业务中产生的数据。 |
| latency | 延迟 | Time between a request and a response. | 从提问到得到回答要等多久。 |
| retrieval latency | 检索延迟 | Time spent finding evidence. | 找资料花费的时间。 |
| generation latency | 生成延迟 | Time spent producing the answer. | 模型写出回答花费的时间。 |
| token budget | 词元预算 | The amount of context or output capacity available in tokens. | 模型一次能处理的文字单位额度。 |
| context budget | 上下文预算 | The amount of context that can be supplied. | 能放进模型背景的资料容量。 |
| cost | 成本 | Resources or money required to run the workflow. | 为检索、处理和生成付出的资源或费用。 |
| compute | 计算资源 | Processing resources used by a model or system. | 运行模型和检索流程所需的计算能力。 |
| scalability | 可扩展性 | Ability to handle more requests or data. | 用户和资料变多后还能正常工作。 |
| availability | 可用性 | Whether the needed system or source is reachable. | 系统或资料源能不能正常访问。 |
| failure mode | 失败模式 | A characteristic way a system can fail. | 系统可能出错的一种典型方式。 |
| source failure | 来源故障 | Failure of a source or connector. | 文件库、数据库或网页来源出了问题。 |
| retrieval timeout | 检索超时 | Retrieval does not finish within the allowed time. | 查资料等太久，超过允许时间。 |
| empty retrieval | 空检索结果 | Retrieval returns no usable evidence. | 搜索没有找到可以用的资料。 |
| irrelevant retrieval | 不相关检索结果 | Retrieved content does not help answer the question. | 找回的资料和问题没什么关系。 |
| noisy context | 噪声上下文 | Context containing distracting or irrelevant content. | 上下文里混入很多干扰资料。 |
| context overload | 上下文过载 | Too much context makes useful evidence harder to use. | 塞进太多资料，模型反而难以抓住重点。 |
| evidence prioritization | 证据优先级排序 | Selecting the most useful evidence when space is limited. | 资料太多时先放最重要的部分。 |
| source filtering | 来源过滤 | Excluding sources that are irrelevant or unauthorized. | 只保留相关、有权限、可信的来源。 |
| access-filtered retrieval | 按权限过滤的检索 | Retrieval that respects a user’s access rights. | 检索时只返回这个用户能看的资料。 |
| tenant isolation | 租户隔离 | Keeping one organization’s data separate from another’s. | 不同客户或组织的数据彼此隔离。 |
| policy enforcement | 政策执行 | Applying rules to source use and output. | 确保系统按规定使用资料和生成回答。 |
| guardrail | 防护栏；安全约束 | A rule or control that limits unsafe behavior. | 限制模型乱用资料或乱回答的安全措施。 |
| grounding guardrail | 接地防护 | A control that constrains source use or unsupported claims. | 防止模型脱离资料、越权或编造的规则。 |
| output constraint | 输出约束 | A rule limiting what the system may return. | 限制最终回答内容和格式的规定。 |
| refusal | 拒绝回答 | A response that declines an unsafe or unsupported request. | 因为不安全或没依据而不回答。 |
| safe completion | 安全完成 | A useful response that stays within safety constraints. | 遵守安全限制、仍尽量帮助用户的回答。 |
| grounded refusal | 有依据的拒答 | A refusal that explains the lack of evidence or authorization. | 说明资料不足或无权限后拒绝乱答。 |
| human-in-the-loop | 人在回路中（HITL） | A workflow where a person reviews or approves system output. | AI 做一部分，人保留检查和决定权。 |
| HITL | 人在回路中（HITL） | Short name for human-in-the-loop. | human-in-the-loop 的缩写。 |
| human review workflow | 人工复核流程 | A workflow that routes outputs to people for checking. | 把结果交给人检查的流程。 |
| reviewer | 审核人 | A person who checks an answer or claim. | 负责核对回答的人。 |
| domain expert | 领域专家 | A person with expertise in the relevant subject. | 熟悉该专业领域、能判断答案的人。 |
| HR reviewer | HR 审核人 | An HR person who checks a policy answer. | 负责核对人力资源回答的人员。 |
| financial analyst | 财务分析师 | A person who reviews financial information or results. | 负责检查财务数据和结论的人。 |
| user trust | 用户信任 | The degree to which users can rely on a system. | 用户是否相信系统给出的结果。 |
| calibrated trust | 校准后的信任 | Trust that matches actual system reliability and limits. | 用户相信的程度和系统真实能力相匹配。 |
| overtrust | 过度信任 | Trusting an answer more than its evidence warrants. | 资料不足却把回答当成绝对正确。 |
| undertrust | 信任不足 | Distrusting a useful answer despite adequate support. | 明明有可靠依据却完全不相信。 |
| user-facing explanation | 面向用户的解释 | An explanation presented to help a user understand the answer. | 给用户看的、解释答案依据的说明。 |
| explanation | 解释 | Information about why or how a result was produced. | 说明结果怎么来的、为什么这样答。 |
| source disclosure | 来源披露 | Showing the sources used by the system. | 把系统参考了哪些资料告诉用户。 |
| provenance display | 来源链展示 | Showing the origin path of an answer. | 把回答的资料来源链展示出来。 |
| evidence display | 证据展示 | Showing source passages or records used for the answer. | 把回答依据的原文或记录展示出来。 |
| independent explainer | 独立讲解视频 | A separate explanatory media resource. | 页面附带的独立说明视频。 |
| explainer | 讲解内容 | Content intended to explain a concept. | 用来帮助理解主题的说明内容。 |
| visual explainer | 可视化讲解 | An explainer using visual media. | 用画面解释概念的内容。 |
| video | 视频 | A video resource attached to the topic page. | 页面里的视频资料。 |
| video label | 视频标签 | The label identifying the video section. | 页面用来标识视频区域的文字。 |
| visual explainer video | 可视化讲解视频 | A video that explains grounding visually. | 用画面说明 grounding 的视频。 |
| video playback | 视频播放 | Playing the video resource. | 在页面上播放视频。 |
| poster | 视频封面图 | An image shown before a video plays. | 视频播放前显示的封面图片。 |
| captions | 字幕 | Text displayed to represent spoken video content. | 视频里把声音写成文字显示的字幕。 |
| subtitles | 字幕 | Text translations or transcriptions for video. | 视频的文字字幕。 |
| English captions | 英文字幕 | English text accompanying spoken video. | 与视频语音对应的英文字幕。 |
| source file | 源文件 | The file containing the page or media source. | 产生页面或资料的原始文件。 |
| page | 页面 | The web page explaining the topic. | 展示 grounding 说明内容的网页。 |
| topic | 主题 | The subject covered by the page. | 页面集中讲解的知识主题。 |
| definition | 定义 | A concise explanation of what a concept is. | 用一句话说明概念是什么。 |
| lede | 导语；摘要句 | A short introductory sentence for the topic. | 页面开头帮助读者快速理解的简介。 |
| related concepts | 相关概念 | Concepts connected to the main topic. | 和主题有关系、可以继续学习的概念。 |
| remember this | 记住这一点 | A concise takeaway from the page. | 页面最后希望读者记住的核心句。 |
| takeaway | 核心要点 | The main idea to retain. | 读完后最应该记住的一句话。 |
| What is it? | 它是什么？ | A section introducing the definition. | 页面介绍定义的部分。 |
| Think of it like... | 可以把它想成…… | A section using an analogy. | 页面用类比帮助理解的部分。 |
| How it works | 它如何工作 | A section describing the process. | 页面解释工作流程的部分。 |
| Real-world examples | 现实世界示例 | A section showing practical examples. | 页面展示实际应用场景的部分。 |
| What it is NOT | 它不是什么 | A section distinguishing related concepts. | 页面专门澄清容易混淆概念的部分。 |
| Related concepts | 相关概念 | A section listing connected topics. | 页面列出相邻概念和学习入口的部分。 |
| grounded answer | 有依据的回答 | The final answer tied to trusted external information. | 结论和可靠外部资料连在一起的回答。 |

## Potential Missing Concepts

- **grounding vs retrieval**：页面把 retrieval 放在流程中，但没有单独展开“检索”如何选择、过滤和排序结果。
- **retrieval-augmented generation / RAG implementation**：页面说明 RAG 是实现 grounding 的一种常见架构，但没有展开索引、查询、拼接上下文和生成的工程细节。
- **embedding / vector search**：正文提到 documents、databases 和 web results，却没有说明如何用 embedding、vector database 或 semantic search 找证据。
- **keyword search / lexical retrieval**：页面没有比较字面匹配和语义检索，也没有说明混合检索。
- **reranking**：没有说明初次检索后如何用第二阶段模型重新排序证据。
- **chunking**：没有说明长文档如何切分为可检索片段，也没有讨论 chunk size 和 overlap。
- **context window limits**：页面说把证据放入 context，但没有说明上下文容量限制和过长资料的处理方式。
- **prompt construction**：没有展开把用户问题、检索片段、来源元数据和回答规则组织成 prompt 的方法。
- **source selection policy**：没有说明如何定义可信来源、来源优先级和冲突解决规则。
- **source freshness / temporal validity**：页面用 current HR document 和 current database records 举例，但没有定义时效性检查。
- **data quality**：没有说明错误、缺失、重复或过时的外部资料会如何影响 grounding。
- **evidence sufficiency**：没有定义何时资料足够回答，何时应该 abstain 或升级给人工。
- **citation correctness / completeness**：页面提到 citations，但没有规定每个重要 claim 如何绑定到正确、完整的证据。
- **answer faithfulness / groundedness**：没有给出衡量回答是否忠实于提供资料的具体方法。
- **retrieval precision / recall**：正文没有列出检索质量指标。
- **answer factuality**：正文说 grounding does not guarantee truth，但没有给事实性评估方法。
- **hallucination detection**：页面没有介绍如何发现回答中的无依据内容或虚构来源。
- **uncertainty estimation**：正文提到正确性不被保证，但没有说明如何表示置信度和不确定性。
- **abstention**：没有明确说明证据不足时拒答、部分回答或请求澄清的策略。
- **source conflict resolution**：没有说明不同文档、数据库记录或网页结果相互矛盾时如何处理。
- **multi-source synthesis**：没有展开如何将多份来源合并成一个不重复、不冲突的回答。
- **provenance**：有 citations，但没有细讲从回答片段到证据片段、文档、版本和时间的完整来源链。
- **access control**：页面列出 company records 和 user-provided files，但没有讨论按用户权限过滤检索结果。
- **privacy**：没有展开个人信息、HR 信息和企业私有数据在 grounding 中的保护方式。
- **prompt injection**：检索到的网页或文件可能包含恶意指令，页面没有讨论把证据和指令区分开。
- **data exfiltration**：没有讨论模型被诱导泄露私有来源内容的风险。
- **security boundary**：没有区分模型、检索器、工具、数据源和用户之间的安全边界。
- **human-in-the-loop**：页面提到 review important claims，但没有定义哪些领域或动作必须人工批准。
- **domain expert review**：没有说明 HR、财务等领域专家如何参与高风险答案审核。
- **monitoring**：没有展开生产环境中对来源新鲜度、引用质量和答案支持度的持续监控。
- **logging / audit trail**：没有说明如何记录查询、检索结果、来源版本、模型版本和最终回答。
- **latency**：没有讨论检索、上下文组装和生成带来的额外响应时间。
- **cost / compute**：没有讨论外部搜索、数据库查询和更长上下文带来的成本。
- **availability / fallback**：没有说明数据库、网页或工具不可用时的备用路径。
- **evaluation set**：没有定义用于评估 grounded answers 的测试集和标准答案。
- **baseline comparison**：没有比较无 grounding、普通 RAG、带引用 RAG 等方案的效果。
- **online vs offline grounding**：没有区分实时查询与预先构建索引、预先生成资料的流程。
- **knowledge cutoff**：没有说明 grounding 如何补足模型原始训练知识的时间边界。
- **model update vs knowledge update**：没有明确区分更新模型参数和更新外部知识源。
- **domain grounding**：没有讨论不同领域需要不同来源、术语和验证标准。
- **enterprise grounding**：没有展开企业私有知识库、权限、租户隔离和审计要求。
- **structured outputs**：页面列出 Structured Outputs 作为相关主题，但没有说明结构化格式如何帮助接地后的结果被下游系统使用。
- **tool calling**：tool outputs 是证据来源之一，但页面没有说明调用工具的决策和错误处理。
- **agent workflow**：页面是线性五步流程，没有展开多个工具、反复检索或规划型 agent 的 grounding。
- **claim decomposition**：没有说明如何把复杂回答拆成可逐条验证的 claims。
- **answer editing**：没有说明发现引用不足后如何修订、删减或改写回答。
- **user trust calibration**：没有讨论引用如何帮助用户建立与系统能力相匹配的信任。

## Aliases / Synonyms

- Grounding ↔ grounded generation ↔ evidence-grounded generation ↔ source-grounded generation ↔ context grounding
- grounded answer ↔ evidence-backed answer ↔ source-backed answer ↔ citation-backed answer
- trusted information ↔ reliable information ↔ authoritative information ↔ dependable source material
- external evidence ↔ external information ↔ runtime knowledge ↔ non-parametric information
- runtime grounding ↔ runtime information grounding ↔ inference-time grounding
- runtime ↔ execution time ↔ answer time（具体语境下不一定完全等价）
- source ↔ information source ↔ knowledge source ↔ source material
- document ↔ source document ↔ policy document ↔ reference document
- database record ↔ stored record ↔ business record ↔ explicit record
- web result ↔ search result ↔ web source ↔ retrieved webpage
- tool output ↔ tool result ↔ external-tool response ↔ connector result
- user-provided file ↔ uploaded file ↔ user document ↔ supplied file
- evidence ↔ support ↔ basis ↔ factual support
- evidence base ↔ supporting context ↔ source context ↔ knowledge context
- retrieve ↔ fetch ↔ look up ↔ search for ↔ bring back
- retrieval ↔ information retrieval ↔ lookup ↔ evidence retrieval
- relevant information ↔ pertinent information ↔ task-relevant information ↔ useful context
- relevance ↔ topical relevance ↔ query relevance ↔ task fit
- add context ↔ supply context ↔ inject context ↔ place evidence in context
- context ↔ model context ↔ prompt context ↔ supplied context
- context construction ↔ context assembly ↔ prompt assembly ↔ evidence packaging
- generate ↔ produce ↔ write ↔ synthesize
- generation ↔ answer generation ↔ response generation ↔ text generation
- verify ↔ validate ↔ check ↔ fact-check ↔ review
- verification ↔ validation ↔ checking ↔ fact-checking
- citation ↔ reference ↔ source reference ↔ attribution
- citations ↔ references ↔ supporting sources ↔ source links
- claim ↔ statement ↔ assertion ↔ factual claim
- important claim ↔ high-impact claim ↔ consequential claim ↔ key assertion
- correctness ↔ accuracy ↔ factual accuracy ↔ answer correctness
- trusted ↔ reliable ↔ authoritative ↔ credible
- trustworthy ↔ dependable ↔ reliable enough to use ↔ fit for purpose
- current information ↔ up-to-date information ↔ fresh information ↔ live information
- freshness ↔ recency ↔ currency ↔ update freshness
- RAG ↔ retrieval-augmented generation ↔ retrieval-enhanced generation ↔ retrieval-grounded generation
- retrieval system ↔ search system ↔ information retrieval system ↔ evidence finder
- vector search ↔ semantic search ↔ embedding search ↔ similarity search（实现和范围不完全同义）
- keyword search ↔ lexical search ↔ literal search ↔ exact-term search
- semantic retrieval ↔ meaning-based retrieval ↔ embedding-based retrieval
- retrieved context ↔ retrieved evidence ↔ selected context ↔ evidence context
- groundedness ↔ faithfulness ↔ evidence support（在评估语境下相关，但不完全同义）
- groundedness score ↔ grounding score ↔ evidence-support score
- answer faithfulness ↔ context faithfulness ↔ source faithfulness
- source traceability ↔ provenance ↔ answer provenance ↔ citation traceability
- auditability ↔ inspectability ↔ reviewability ↔ traceability
- source quality ↔ evidence quality ↔ source reliability
- source authority ↔ source credibility ↔ source trustworthiness
- model knowledge ↔ parametric knowledge ↔ learned knowledge
- external knowledge ↔ non-parametric knowledge ↔ retrieved knowledge
- knowledge update ↔ source update ↔ data refresh ↔ information refresh
- model update ↔ retraining ↔ fine-tuning ↔ parameter update（不完全同义）
- fine-tuning ↔ additional training ↔ task-specific training ↔ model adaptation
- human review ↔ manual review ↔ human verification ↔ expert review
- human oversight ↔ human supervision ↔ human-in-the-loop ↔ HITL
- approval ↔ sign-off ↔ authorization ↔ human acceptance
- hallucination ↔ fabricated answer ↔ unsupported generation ↔ plausible falsehood
- unsupported claim ↔ ungrounded claim ↔ uncited claim ↔ evidence-free claim
- insufficient evidence ↔ lack of support ↔ inadequate context ↔ evidence gap
- abstention ↔ refusal to answer ↔ defer to human ↔ safe non-answer
- fallback ↔ backup path ↔ alternative workflow ↔ graceful degradation
- source conflict ↔ conflicting evidence ↔ inconsistent sources ↔ contradictory records
- source priority ↔ trust ranking ↔ authority ranking ↔ source precedence
- retrieval precision ↔ precision@k ↔ relevant-return rate
- retrieval recall ↔ recall@k ↔ relevant-capture rate
- ranking ↔ relevance ranking ↔ result ordering
- reranking ↔ re-ranking ↔ second-stage ranking
- chunk ↔ document chunk ↔ passage ↔ text segment
- chunking ↔ document splitting ↔ text segmentation
- query ↔ retrieval query ↔ search query ↔ user query
- query understanding ↔ intent understanding ↔ query interpretation
- embedding ↔ vector representation ↔ numerical representation
- query embedding ↔ query vector
- document embedding ↔ passage embedding ↔ chunk embedding
- vector database ↔ vector store ↔ similarity-search database
- database lookup ↔ record lookup ↔ data query
- company policy ↔ organizational policy ↔ enterprise policy
- HR ↔ Human Resources ↔ people operations（具体组织名称可能不同）
- maternity leave ↔ parental leave（相关但不完全同义）
- revenue ↔ sales revenue ↔ turnover（不同地区和会计语境下不一定完全同义）
- financial data ↔ finance records ↔ financial information
- current database records ↔ live business records ↔ up-to-date records
- question step ↔ identify-the-need step ↔ query-understanding step
- retrieve step ↔ evidence-finding step ↔ search step
- add-context step ↔ context-supply step ↔ evidence-injection step
- generate step ↔ answer-writing step ↔ response-generation step
- verify step ↔ result-checking step ↔ citation-review step
- answer with the book open ↔ consult-the-source analogy ↔ source-assisted answering
- visual explainer ↔ visual explanation ↔ explainer video
- poster ↔ video thumbnail ↔ cover image
- captions ↔ subtitles ↔ transcript text

## Do Not Confuse Candidates

- **Grounding vs RAG**：Grounding 是把答案和外部证据联系起来的目标或方法；RAG 是实现这一目标的一种常见架构。RAG 通常包含检索和生成，但 grounding 不限于 RAG。
- **Grounding vs retrieval**：Retrieval 只是找到外部资料的步骤；grounding 还包括把资料放进上下文、用于生成并进行验证。
- **Grounding vs fine-tuning**：Grounding 在运行时加入信息；fine-tuning 通过训练改变模型行为和参数。
- **Grounding vs guaranteed truth**：有外部证据不等于答案一定为真；来源可能过时、错误、不完整或与其他来源冲突。
- **Grounding vs citations**：Citations 是展示出处的方式；有引用不自动保证回答正确，引用本身还要检查是否真正支持主张。
- **Grounding vs context**：Context 是模型能看到的信息集合；grounding 是让回答依赖可信、相关的外部 context 的做法。
- **Grounding vs prompt**：Prompt 是给模型的输入或指令；grounding 关注其中的证据是否来自可信外部来源并支撑回答。
- **External evidence vs model knowledge**：外部证据在运行时提供；model knowledge 通常指训练后编码在模型参数中的知识。
- **Runtime information vs training data**：runtime information 是当前请求时临时提供的资料；training data 是训练模型时使用的例子。
- **Knowledge update vs model update**：更新外部知识源可以改变回答依据，不一定要重新训练或替换模型。
- **Current information vs correct information**：资料最新不代表内容一定正确；“current”描述时间，“correct”描述事实是否正确。
- **Trusted source vs authoritative source**：可信来源适合当前使用；权威来源通常有正式身份，但也仍需检查时效和适用范围。
- **Relevant evidence vs sufficient evidence**：资料可能相关但不够完整；relevance 和 sufficiency 是不同标准。
- **Retrieved context vs source document**：Source document 是原始完整资料；retrieved context 可能只是被选出的片段。
- **Source content vs source instructions**：资料内容可以支持事实判断；资料中夹带的指令不应自动拥有更高指令优先级。
- **Evidence vs instruction**：Evidence 是用来支持回答的材料；instruction 是要求模型执行某种行为的命令。
- **Retrieval vs search**：Search 通常指查找动作或系统；retrieval 更强调把相关资料取回供后续任务使用。
- **Retrieval vs recommendation**：Retrieval 找回已有相关资料；recommendation 判断哪些候选对用户可能有用。
- **Semantic retrieval vs keyword retrieval**：语义检索按含义找相近内容；关键词检索按字面词语或短语匹配。
- **Vector search vs grounding**：Vector search 是一种检索技术；grounding 是从来源到有依据回答的更宽流程。
- **Embedding vs retrieved evidence**：Embedding 是数值表示；retrieved evidence 是实际被找回并用于回答的资料。
- **RAG vs vector database**：RAG 是检索加生成的架构；vector database 只是可能用于保存和搜索向量的组件。
- **Context window vs context**：Context 是实际提供的背景信息；context window 是模型一次可容纳的容量限制。
- **Context size vs evidence quality**：放更多资料不代表证据更好；无关、过时或冲突内容可能降低回答质量。
- **Answer generation vs verification**：Generation 产出回答；verification 检查回答是否被证据支持。
- **Verification vs evaluation**：Verification 可以是对当前结果的核验；evaluation 通常是按系统化标准评估整体表现。
- **Citation vs evidence**：Citation 是指向来源的引用标记；evidence 是实际支撑主张的内容。
- **Citation presence vs citation correctness**：有出处不代表出处正确；必须检查引用是否真正支持对应说法。
- **Citation correctness vs citation completeness**：Correctness 关注每条引用是否支持主张；completeness 关注重要主张是否都覆盖到了。
- **Source traceability vs explainability**：Traceability 关注能否追溯到来源；explainability 更广，关注能否理解系统为什么给出结果。
- **Provenance vs citation**：Provenance 是完整来源历史；citation 通常是回答中展示来源的一个接口。
- **Plausible text vs factual text**：文字看上去合理不代表符合事实；grounding 用证据减少这种差距，但不自动消除。
- **Hallucination vs source error**：Hallucination 是模型生成无依据或虚构内容；source error 是外部来源本身已经错误。
- **Unsupported claim vs incorrect claim**：无证据不一定已经被证明错误；incorrect 明确与事实不符。
- **Uncertainty vs error**：不确定性表示还不能判断是否正确；error 表示结果已经和事实或要求不一致。
- **Grounded answer vs correct answer**：回答有证据依据不等于一定正确；正确答案也可能没有展示引用。
- **Freshness vs accuracy**：新资料可能不准确，旧资料也可能仍然准确；时间新旧和事实准确是两条维度。
- **Current HR document vs any HR document**：业务问题应该使用当前适用的 HR 文档，不应随便引用历史版本。
- **Company record vs public web result**：公司记录可能更适合内部事实；网页结果可能公开但不一定适用于该组织。
- **Database record vs database schema**：Record 是一条实际数据；schema 是数据库中字段和结构的定义。
- **Revenue vs profit**：Revenue 是收入；profit 是扣除成本后的利润，两者不能互换。
- **Last month’s revenue vs current revenue**：上月收入是固定历史期间的指标；当前收入可能指本月或实时累计值。
- **Policy question vs policy instruction**：关于政策的问题需要查资料回答；政策文档中的指令不等于给模型的系统指令。
- **Document retrieval vs document generation**：Retrieval 找回已有文档；generation 产生新回答或新内容。
- **User-provided file vs trusted file**：用户提供文件不自动意味着它可靠、最新或有权限使用。
- **Private data vs authorized data**：数据是私有的，不代表当前用户或系统一定有权访问。
- **Access control vs grounding**：权限控制决定能否读取资料；grounding 决定回答是否依赖资料，二者都需要。
- **Privacy vs factuality**：隐私关心资料是否被恰当保护；事实性关心回答是否符合事实。
- **Safety vs answer quality**：质量关心回答是否有用、正确；安全关心回答是否造成风险或伤害。
- **Human review vs human-in-the-loop**：Human review 是一次检查；HITL 是把人工检查或批准设计进完整工作流。
- **Human review vs human approval**：Review 可以只提出问题或建议；approval 是正式接受结果用于后续行动。
- **Domain expert vs general reviewer**：领域专家能判断专业事实和政策适用性；普通审核人不一定具备同等知识。
- **Abstention vs refusal**：Abstention 通常因为证据不足而不猜；refusal 也可能因为安全、权限或政策限制而拒绝。
- **Fallback vs hallucination**：Fallback 是主流程失败时的安全替代路径；hallucination 是模型编造或无依据生成。
- **Source conflict vs model disagreement**：Source conflict 是外部资料互相矛盾；model disagreement 是模型或多个回答之间不同。
- **Retrieval precision vs retrieval recall**：Precision 看找回的内容中有多少相关；recall 看全部相关内容中找回了多少。
- **Groundedness score vs truth score**：Groundedness 衡量回答是否被提供资料支持；不能直接当作“真实程度”或事实保证。
- **Answer faithfulness vs factual accuracy**：Faithfulness 关注是否忠实于给定上下文；factual accuracy 关注是否符合现实事实。
- **Top-k retrieval vs complete retrieval**：Top-k 只取排名前 k 项，不代表找回所有相关资料。
- **Reranking vs retrieval**：Reranking 是检索之后重新排序；不是独立替代整个检索流程。
- **Chunk vs document**：Chunk 是文档的一部分；document 是完整或更大的资料单位。
- **Metadata vs source content**：Metadata 描述来源、时间和类别；source content 是实际被用来支持回答的内容。
- **Document version vs document copy**：Version 是同一文档的不同修订状态；copy 可能只是相同版本的另一份副本。
- **Source link vs source citation**：Link 是可点击的访问路径；citation 是回答中标识依据的引用关系。
- **Source availability vs source authority**：来源可访问不代表来源权威；能打开的资料也可能不可靠。
- **Latency vs quality**：更快的回答不一定更有依据；grounding 流程要在时延和质量间平衡。
- **Monitoring vs one-time verification**：Monitoring 是持续观察；verification 可以只是对某次结果的一次核验。
- **Logging vs citation**：日志供系统审计和排查；引用供用户检查回答来源。
- **Video / poster / captions vs grounding mechanism**：视频、封面和字幕是页面呈现资源，不是 grounding 的核心机制。
- **“Answer with the book open” vs literal book reading**：这是说明“回答时参考来源”的类比，不是要求系统真的阅读一本书。

## Notes

- 本文件是 `grounding.html` 的 raw glossary 收集稿，按要求尽可能保留正文中出现的术语、重要短语、流程节点、示例词、边界词、指标候选、别名和易混淆概念；不做最终去重、归并或删减。
- 页面元信息为 `05 · Embeddings, RAG & Vector Search · Topic 04`；本任务指定输出为 `08-grounding.md`，因此 Requested Module 和 Page Module 都保留。
- 页面核心定义是：`Grounding connects an AI response to trusted information supplied at runtime.` 这是本主题最核心的定义候选。
- Definition 段明确对比了 model 根据 learned patterns 生成 plausible text，和 grounding 为 current task 提供 specific evidence；documents、databases、web results、tool outputs、company records、user-provided files 都是直接列出的证据来源。
- Analogy 段的原文主旨是 `Answer with the book open.`；页面同时明确说明类比解释的是 evidence 的作用，不能保证 answer correct。
- Process 段的完整五步是：`1 · Question / Identify the need`、`2 · Retrieve / Find evidence`、`3 · Add context / Supply the evidence`、`4 · Generate / Write the answer`、`5 · Verify / Check the result`。这些词在候选表中分别保留了标题、动作和解释文本。
- Verify 步骤特别提到 `Show citations or review important claims`；因此 citation、important claim、claim verification、citation correctness 和 citation completeness 都保留为重要候选或缺口候选。
- Real-world examples 包含两个直接业务场景：company policy / maternity leave / current HR document，以及 financial data / last month’s revenue / current database records。`revenue` 也作为业务和财务指标候选保留。
- What it is NOT 直接给出三组边界：`Grounding ≠ RAG`、`Grounding ≠ Fine-tuning`、`Grounding ≠ Guaranteed Truth`。这些对照以及每组的两侧概念都不应在 raw 阶段删除。
- 页面明确说 RAG 是实现 grounding goal 的一种常见 architecture；grounding 是 tying answers to external evidence 的 goal。两者关系保留在候选、Aliases 和 Do Not Confuse 中。
- 页面 related concept tree 是 `Trusted source → Retrieval → Context → LLM → Grounded answer → Citation`；这是页面明确提供的关系链，不应只保留单个节点而丢失箭头关系。
- 页面 Explore next 入口是 `RAG`、`Retrieval`、`Context Window`、`Structured Outputs`；这些链接词和对应概念均保留。
- 页面 Remember this 的核心句是 `Grounding ties an AI answer to trusted external information.`；这是简化版 takeaway，与 definition 候选同时保留。
- 页面正文没有给出具体检索或接地指标；`retrieval precision`、`retrieval recall`、`groundedness score`、`support rate`、`citation completeness` 等放入候选或 Potential Missing Concepts 时，应理解为可供后续扩展的指标，不是页面已定义的数值。
- 页面正文没有明确解释 embedding、vector search、chunking、reranking、prompt injection、permissions 或 privacy；这些概念由页面的 retrieval、source、company records、files、tool outputs 和 runtime context 直接触发，保留在扩展候选中但已在 Potential Missing Concepts 标明未展开。
- `current HR document` 和 `current database records` 使 freshness、update time、version、temporal validity 成为重要扩展方向；当前不应把“current”简单等同于“correct”。
- Grounding 依赖来源质量：若 source error、stale information、incomplete evidence 或 conflicting evidence 存在，grounding alone 仍不能保证 truth。
- 文档、数据库、网页结果、工具输出、公司记录和用户文件的权限、隐私、来源可信度和时效性没有在页面细讲；这些是实际企业 grounding 中的重要边界候选。
- 页面只写 `review important claims`，没有定义所有输出都必须人工审核。因此 human review、human approval、human-in-the-loop 和 domain expert review 在 raw 阶段分别保留并在 Do Not Confuse 中区分。
- 页面视频区域的直接标记包括 `Independent explainer`、`visual explainer`、`visual explainer video`、`poster` 和 `captions`；这些是低优先级呈现候选，不应误当成 grounding 机制。
- HTML 的导航词如 `What is it?`、`Think of it like...`、`How it works`、`Real-world examples`、`What it is NOT`、`Related concepts`、`Remember this` 和 `Video` 被保留为页面结构候选，便于追溯每个术语来自哪个正文区域。
- 本 raw 文件有意保留单数、复数、大小写形式和相近短语（如 evidence / evidences 不在页面出现时不额外伪造；documents / databases / web results / tool outputs / company records / user-provided files 则按页面原文保留）。
- 后续整理阶段可以再决定哪些候选合并为规范词条、哪些归入模块 08 其他主题、哪些仅作为 cross-reference；本文件不提前做这些取舍。
