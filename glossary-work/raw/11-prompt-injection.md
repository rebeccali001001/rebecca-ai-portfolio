# Topic

Prompt Injection

Module/Topic/Source File

- Module: 11 · Evaluation, Safety & Reliability
- Topic: Prompt Injection
- Source File: `prompt-injection.html`

## Glossary Candidates

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Prompt Injection | 提示词注入；提示注入 | Untrusted content tries to manipulate an AI system into following conflicting instructions. | 不可信内容试图“带偏”AI，让它执行与原本规则冲突的指令。 |
| injection | 注入 | Inserting content that changes how a system behaves. | 把特定内容塞进输入里，试图改变系统行为。 |
| untrusted content | 不可信内容 | Content that must not automatically control the AI system. | 不能默认拿来控制 AI 的外部内容。 |
| trusted instruction | 可信指令 | An instruction the system is authorized to follow. | 系统有权遵循的指令。 |
| intended rules | 预期规则 | The rules the AI system is supposed to follow. | AI 原本应该遵守的规则。 |
| intended instructions | 预期指令 | The instructions that define the system's intended behavior. | 规定系统应该怎样工作的指令。 |
| intended behavior | 预期行为 | The behavior the system is designed and authorized to produce. | 系统设计上应该表现出的行为。 |
| authorized action | 已授权操作 | An action the system has permission to perform. | 系统被允许执行的动作。 |
| manipulation attempt | 操纵尝试 | An attempt to steer a system away from its intended behavior. | 试图把系统引向原定任务之外的做法。 |
| change instructions | 改变指令 | Alter what the system is instructed or authorized to do. | 改变系统被要求或被允许做的事情。 |
| change system behavior | 改变系统行为 | Make the AI respond or act differently from its intended rules. | 让 AI 偏离原本规则而回答或行动。 |
| change authorized actions | 改变授权动作 | Try to make the system perform actions it was not meant to perform. | 试图让系统做原本没有授权的事情。 |
| AI system | AI 系统 | A system that receives input and produces responses or actions. | 接收信息并生成回答或执行动作的系统。 |
| system | 系统 | The complete mechanism that interprets inputs and produces outputs or actions. | 从接收信息到回答或行动的一整套机制。 |
| input | 输入 | Information given to an AI system. | 送进 AI 的信息。 |
| instruction | 指令 | A request or rule that tells a system what to do. | 告诉系统应该做什么的请求或规则。 |
| data | 数据 | Information that can be processed by the system. | 系统可以读取和处理的信息。 |
| user | 用户 | The person who supplies a request or content. | 提出请求或提供内容的人。 |
| webpage | 网页 | An external web resource that an AI or agent may read. | AI 或智能体可能读取的外部网页。 |
| document | 文档 | External written material that may be supplied to or retrieved by the system. | 交给系统或被系统检索到的外部文字材料。 |
| email | 电子邮件 | External message content that an AI system may process. | AI 可能读取的外部邮件内容。 |
| tool result | 工具结果 | Content returned by a tool after a system calls it. | 系统调用工具后返回的内容。 |
| external content | 外部内容 | Content coming from outside the system's trusted rules. | 来自系统可信规则之外的内容。 |
| external instruction | 外部指令 | An instruction appearing in content supplied by an outside source. | 出现在外部材料中的指令。 |
| trust boundary | 信任边界 | The boundary between instructions the system may trust and data it must treat as untrusted. | 区分“可以控制系统的指令”和“只能当资料看的内容”的界线。 |
| trusted boundary | 可信边界 | A boundary used to separate trusted control from untrusted input. | 把可信控制信息与不可信输入隔开的边界。 |
| trusted system rule | 可信系统规则 | A system-level rule that the AI is authorized to follow. | AI 可以信任并遵守的系统层规则。 |
| untrusted document | 不可信文档 | A document whose text should be treated as data, not as system control. | 只能当资料读取、不能自动当命令执行的文档。 |
| instruction versus data | 指令与数据的区分 | Deciding whether text controls the system or is merely content to process. | 判断一段文字是“命令”还是“资料”。 |
| instruction-like text | 看起来像指令的文本 | Text that looks like a command but may come from an untrusted source. | 虽然像命令，但来源不可信的文字。 |
| external content can contain instructions | 外部内容也可能包含指令 | A reminder that webpages and documents can include command-like text. | 网页、文档等外部内容里也可能藏着命令。 |
| direct injection | 直接注入 | A user directly supplies a manipulation attempt in the conversation. | 用户直接在对话中输入试图操纵系统的内容。 |
| indirect injection | 间接注入 | Manipulation appears inside a webpage, document, email, retrieved content, or tool result. | 操纵内容藏在网页、文档、邮件、检索结果或工具结果里。 |
| direct manipulation | 直接操纵 | Manipulation supplied directly in the conversation. | 直接在聊天输入中操纵 AI。 |
| indirect manipulation | 间接操纵 | Manipulation delivered through external content the system reads. | 通过 AI 读取的外部材料间接操纵 AI。 |
| conversation | 对话 | The interaction in which a user supplies messages to an AI system. | 用户与 AI 交流的消息过程。 |
| retrieved content | 检索内容 | Content fetched from an external source for the system to read. | 系统从外部来源取回的内容。 |
| agent | 智能体；代理 | An AI system that can read content and potentially use tools or take actions. | 能读取资料、调用工具甚至执行动作的 AI 系统。 |
| agent that reads external content | 读取外部内容的智能体 | An agent exposed to instructions embedded in content it processes. | 会读取外部网页、文档等材料、因此可能遇到注入的智能体。 |
| agent task | 智能体任务 | The task an agent is instructed to perform. | 交给智能体要完成的工作。 |
| webpage text | 网页文本 | Text from a webpage that an agent may process as data. | 智能体读取到的网页文字。 |
| webpage instruction | 网页指令 | An instruction-like statement embedded in webpage content. | 藏在网页文字中的、看起来像命令的话。 |
| document instruction | 文档指令 | An instruction-like statement embedded in a document. | 藏在文档中的、试图影响系统行为的文字。 |
| email instruction | 邮件指令 | An instruction-like statement embedded in an email. | 藏在邮件里的、试图让 AI 做某事的文字。 |
| bad system | 不安全系统；错误系统 | A system that treats untrusted webpage text as a trusted instruction. | 把网页等不可信文字直接当成系统命令的系统。 |
| better system | 更安全的系统 | A system that separates trusted instructions from untrusted content and requires approval for sensitive actions. | 能区分可信指令和外部资料，并对敏感动作要求审批的系统。 |
| system instruction | 系统指令 | A trusted instruction defining the system's role or constraints. | 规定 AI 角色和限制的可信系统层指令。 |
| web content | 网页内容 | Content read from the web and treated as untrusted data. | 从网页读取、应先当作不可信资料处理的内容。 |
| sensitive action | 敏感动作 | An action that can expose data, change records, or cause meaningful impact. | 可能泄露数据、修改记录或造成较大影响的动作。 |
| permission | 权限；许可 | Authorization required before an action is performed. | 执行动作前需要具备的许可。 |
| approval | 审批；批准 | Explicit permission to proceed with a sensitive action. | 对敏感动作明确说“可以执行”。 |
| permission / approval required | 需要权限或审批 | A control requiring authorization before a sensitive action. | 做重要动作前必须先有授权或人工批准。 |
| tool | 工具 | A capability an AI system can call to read data or perform an action. | AI 可以调用来读数据或做事情的能力。 |
| tool use | 工具使用 | Calling a tool as part of completing a task. | AI 在任务过程中调用外部工具。 |
| tool calling | 工具调用 | The mechanism of asking an external tool to perform an operation. | 让 AI 调用外部功能执行操作的机制。 |
| tool result | 工具返回结果 | Data or text returned after a tool call. | 工具执行后返回的数据或文字。 |
| capability | 能力 | What the system is technically able to read or do. | 系统在技术上能够读取或执行的事情。 |
| no tools | 没有工具 | A setting where the AI can only produce an output. | AI 只能生成回答、不能调用外部工具的状态。 |
| with tools | 配备工具 | A setting where the AI can read files or affect external systems. | AI 可以读文件或影响外部系统的状态。 |
| bad instruction | 不安全指令 | An instruction that conflicts with the intended task or rules. | 与原本任务或规则冲突的指令。 |
| bad output | 错误输出 | An output that is wrong, unsafe, or not useful. | 错误、不安全或没有帮助的回答。 |
| read files | 读取文件 | Access files as an action available to the system. | 系统打开并读取文件的动作。 |
| file access | 文件访问 | The capability to read or interact with files. | 系统读取或接触文件的能力。 |
| external action | 外部动作 | An action that affects something outside the model's text response. | 会影响系统外部对象的动作。 |
| change the world | 改变现实世界 | Cause an external effect beyond generating text. | 不只是回答文字，而是真正改变外部系统或现实状态。 |
| send email | 发送邮件 | An external action that sends a message to other people or systems. | 代表用户把邮件发出去的动作。 |
| change records | 修改记录 | An external action that alters stored data or business records. | 改动数据库、业务记录或其他保存信息。 |
| perform a transaction | 执行交易 | Carry out an operation involving a transaction or transfer. | 真正执行支付、转账或其他交易操作。 |
| transaction | 交易 | An operation that changes financial or business state. | 会改变财务或业务状态的一次操作。 |
| high impact | 高影响 | Having consequences that matter significantly if performed incorrectly. | 做错后会造成较大后果的特征。 |
| risk | 风险 | The possibility that manipulation causes unsafe behavior or impact. | 注入导致不安全行为或外部损害的可能性。 |
| control | 控制措施 | A mechanism that limits what a system can do or requires checks. | 限制系统行为或要求检查的机制。 |
| stronger controls | 更强的控制措施 | More restrictive safeguards needed when a system has more capability. | 系统能力越强，越需要严格的限制和检查。 |
| security problem | 安全问题 | A problem involving manipulation of system control or protected actions. | 涉及系统控制权或受保护动作被操纵的问题。 |
| control problem | 控制问题 | A failure to preserve the intended authority boundary. | 没有守住谁有权控制系统的边界。 |
| normal prompt | 普通提示词；正常提示 | A legitimate instruction for the intended task. | 为完成原本任务而提出的正常、合法指令。 |
| normal prompting | 正常提示 | Giving an AI a legitimate request for its intended task. | 正常告诉 AI 要完成什么工作。 |
| legitimate instruction | 合法指令 | An instruction appropriate for the intended task and authority. | 符合任务和权限范围的指令。 |
| intended task | 原定任务 | The task the system is supposed to complete. | 系统本来应该完成的工作。 |
| prompt injection versus normal prompt | 提示注入与普通提示的区别 | A normal prompt supports the intended task; an injection attempts to alter system behavior. | 正常提示帮助完成任务，注入则试图改变系统原本的行为。 |
| system behavior | 系统行为 | The responses and actions produced by the AI system. | AI 系统实际回答和执行的动作。 |
| hallucination | 幻觉 | Unsupported or incorrect content generated by an AI. | AI 生成没有依据或不正确的内容。 |
| unsupported content | 无依据内容 | Content not supported by the available information. | 现有信息无法支持的内容。 |
| incorrect generated content | 错误生成内容 | Generated content that is factually or logically wrong. | AI 生成的事实或逻辑错误内容。 |
| output reliability problem | 输出可靠性问题 | A problem with whether generated content is accurate or supported. | 关注回答是否准确、有依据的问题。 |
| prompt injection versus hallucination | 提示注入与幻觉的区别 | Injection is instruction manipulation; hallucination is unsupported or incorrect output. | 注入是控制问题，幻觉是输出可靠性问题。 |
| trust boundaries | 信任边界措施 | Separating trusted control instructions from untrusted data. | 把能控制 AI 的内容与只能读取的资料分开。 |
| permissions | 权限控制 | Limiting which actions the system is allowed to take. | 限制系统能够执行哪些动作。 |
| tool restrictions | 工具限制 | Constraints on which tools can be called and what they can do. | 限制 AI 能调用哪些工具、工具能做什么。 |
| validation | 验证 | Checking content or an intended action before accepting or executing it. | 在接受内容或执行动作前进行检查。 |
| human approval | 人工批准 | A person explicitly approves a potentially sensitive action. | 重要动作执行前由人明确同意。 |
| risk reduction | 风险降低 | Measures that make unsafe behavior less likely. | 让不安全行为更不容易发生的措施。 |
| risk is not guaranteed to disappear | 风险不会保证消失 | Safeguards reduce risk but cannot promise zero risk. | 防护能降低风险，但不能保证风险完全为零。 |
| guardrails | 防护栏；安全护栏 | Rules and controls that constrain unsafe system behavior. | 限制 AI 不要做危险事情的规则和控制。 |
| permissions and safety | 权限与安全 | The area covering authorization and safe system operation. | 讨论谁能做什么以及怎样安全执行。 |
| human in the loop | 人在回路中；人工参与 | A human reviews or approves an important step in the process. | 关键步骤由人检查或批准，而不是完全自动执行。 |
| failure handling | 失败处理 | Handling unsafe, invalid, or unsuccessful system behavior. | 系统出现不安全、无效或失败情况时如何处理。 |
| related concept | 相关概念 | A concept connected to prompt injection but not identical to it. | 与提示注入有关、但不一定等同的概念。 |
| every bad output | 每一种错误输出 | Any incorrect or unsafe answer, which is not automatically prompt injection. | 所有错误回答的总称，不是每个都属于提示注入。 |
| Prompt Injection is not normal prompting | 提示注入不等于正常提示 | Injection is not just any request; it attempts to alter intended behavior. | 不是所有请求都是注入，关键是是否试图改变原定行为。 |
| Prompt Injection is not hallucination | 提示注入不等于幻觉 | Injection concerns manipulated instructions, not merely incorrect content. | 注入关注指令被操纵，不只是回答是否错误。 |
| Prompt Injection is not tool calling | 提示注入不等于工具调用 | Tool calling is a capability or mechanism; injection is an attack or manipulation attempt. | 调用工具是功能机制，注入是试图操纵系统的行为。 |
| Prompt Injection is not every bad output | 提示注入不等于所有错误输出 | A bad answer can have other causes besides an injection. | 错误回答可能有很多原因，不一定是注入。 |
| evaluation | 评估 | Checking whether a system behaves correctly and safely. | 检查系统是否正确、安全地工作。 |
| safety | 安全性 | The property of avoiding harmful or unauthorized behavior. | 避免有害或未授权行为的性质。 |
| reliability | 可靠性 | The degree to which a system produces dependable results. | 系统持续产生可信结果的程度。 |
| security and reliability | 安全与可靠性 | The combined concern of protecting control and producing dependable outputs. | 同时关注系统不被操纵、输出也可信。 |
| sensitive data | 敏感数据 | Data whose exposure or misuse could cause harm. | 泄露或滥用后可能造成损害的数据。 |
| private data | 私人数据；私密数据 | Data that should not be exposed to an unauthorized party. | 不应被无权人员看到或发送的数据。 |
| protected action | 受保护动作 | An action that needs extra authorization or safeguards. | 必须经过额外授权或防护才能执行的动作。 |
| permission boundary | 权限边界 | The limit separating allowed actions from forbidden actions. | 区分“可以做”和“不可以做”的边界。 |
| authority boundary | 权威边界；权限归属边界 | The boundary that determines which source has authority to direct the system. | 决定谁有权指挥系统的界线。 |
| source authority | 来源权威 | The authority assigned to the source of an instruction. | 系统认为某个来源是否有权发出指令。 |
| content provenance | 内容来源 | Where a piece of content came from. | 一段内容是从哪里来的。 |
| source separation | 来源隔离 | Keeping content from different trust levels distinct. | 不把不同信任等级的内容混在一起。 |
| least privilege | 最小权限 | Give the system only the access needed for the task. | 只给系统完成任务所需的最少权限。 |
| confirmation step | 确认步骤 | A check that asks for explicit confirmation before proceeding. | 执行重要动作前再确认一次。 |
| action approval gate | 动作审批闸门 | A control point that blocks an action until approval is given. | 没有批准就不允许继续的控制点。 |
| untrusted instruction handling | 不可信指令处理 | Treating instruction-like text from external content as data to inspect, not commands to obey. | 外部材料里的命令样文字先当资料分析，而不是直接执行。 |
| instruction hierarchy | 指令层级 | An ordering that determines which instructions have priority. | 决定不同指令谁优先的层级关系。 |
| system-level control | 系统层控制 | Control supplied by trusted system instructions or policy. | 由可信系统指令或策略提供的控制。 |
| external side effect | 外部副作用 | A change caused outside the model's generated text. | AI 回答之外，对文件、账户或现实系统造成的变化。 |
| sensitive operation | 敏感操作 | An operation requiring additional checks because of its impact. | 因为影响较大而需要额外检查的操作。 |
| action validation | 动作验证 | Checking that an action is permitted and appropriate before execution. | 执行动作前确认它有权限且符合任务。 |
| content validation | 内容验证 | Checking external content before relying on it or acting on it. | 采用外部内容或依据它行动前先检查。 |

## Potential Missing Concepts

- The page introduces trust boundaries, permissions, tool restrictions, validation, and human approval, but does not name a detailed policy-enforcement architecture.
- It does not provide formal attack taxonomies beyond direct injection and indirect injection.
- It does not define a quantitative prompt-injection rate, attack-success rate, false-positive rate, or other numeric evaluation metric.
- It does not describe a concrete detector, classifier, sanitizer, parser, or content-isolation implementation.
- It does not specify a formal instruction-priority algorithm, policy language, sandbox design, or capability-token mechanism.
- It does not give a concrete incident-response workflow, logging standard, red-team protocol, or benchmark dataset.
- It mentions agents and external content but does not separately define retrieval-augmented generation, browsing, connectors, plugins, or memory systems.
- It mentions human approval and sensitive actions but does not define approval UX, escalation rules, or an explicit risk-scoring model.
- It mentions stronger controls as capability increases but does not define a capability-level scale or a mapping from capability to control strength.
- No standalone glossary entry on the page gives a formal definition of a metric; the source is primarily a conceptual explainer.

## Aliases / Synonyms

- Prompt Injection / prompt injection / 提示词注入 / 提示注入
- Direct Injection / direct prompt injection / 直接注入 / 直接提示注入
- Indirect Injection / indirect prompt injection / 间接注入 / 间接提示注入
- Untrusted Content / external content / 不可信内容 / 外部内容
- Trusted Instruction / trusted system rule / system instruction / 可信指令 / 可信系统规则 / 系统指令
- Trust Boundary / trusted boundary / authority boundary / permission boundary / 信任边界 / 权威边界 / 权限边界
- Tool Calling / tool use / tool invocation / 工具调用 / 工具使用
- Human Approval / human-in-the-loop approval / 人工批准 / 人在回路中的批准
- Guardrails / safety controls / stronger controls / 防护栏 / 安全控制 / 更强的控制措施
- Hallucination / unsupported or incorrect generated content / 幻觉 / 无依据或错误的生成内容
- Sensitive Action / sensitive operation / protected action / 敏感动作 / 敏感操作 / 受保护动作
- Bad Output / unsafe output / incorrect output / 错误输出 / 不安全输出 / 不正确输出
- External Side Effect / change the world / external action / 外部副作用 / 改变现实世界 / 外部动作

## Do Not Confuse Candidates

| Candidate | Do not confuse it with | Distinction |
|---|---|---|
| Prompt Injection | Normal Prompt | A normal prompt is a legitimate request for the intended task; injection attempts to alter intended behavior or authority. |
| Prompt Injection | Hallucination | Injection is a manipulation-of-instructions and security/control problem; hallucination is unsupported or incorrect generated content and an output-reliability problem. |
| Prompt Injection | Tool Calling | Tool calling is a capability or mechanism. It can increase the impact of injection, but tool calling itself is not an injection. |
| Prompt Injection | Every Bad Output | A bad output may result from misunderstanding, missing information, or other failures; not every bad output is caused by injection. |
| Direct Injection | Indirect Injection | Direct injection is supplied by a user in the conversation; indirect injection is embedded in external content the system reads. |
| Untrusted Content | Trusted Instruction | Untrusted content may contain instruction-like text, but it is data to inspect rather than authority to obey. |
| System Instruction | Web Content | A system instruction is trusted control; web content is external data unless separately authorized. |
| Permission | Capability | Capability is what the system can technically do; permission is what it is authorized to do. |
| Approval | Permission | Permission may be a standing authorization or policy; approval is an explicit confirmation for a particular action. |
| Tool Restriction | No Tools | Tool restrictions constrain available tools or operations; no tools means the system has no tool capability in that setting. |
| Guardrails | Trust Boundary | Guardrails are controls; a trust boundary is the separation that identifies which sources may control the system. |
| Validation | Human Approval | Validation can be automated or procedural checking; human approval specifically requires a person to authorize the action. |
| Sensitive Action | Bad Output | A sensitive action changes an external state; a bad output can be only an incorrect or unsafe piece of text. |
| Risk Reduction | Risk Elimination | The page says safeguards can reduce risk, not guarantee that risk disappears. |

## Notes

- Extraction scope: full visible explanatory text of `prompt-injection.html`, including headings, examples, comparison blocks, related concepts, and the closing reminder.
- The source repeatedly emphasizes the question “Is this trusted to control the system?” rather than whether text merely looks like an instruction.
- The source's core flow is: external content contains instruction-like text → system classifies its trust level → trusted instructions remain in control → sensitive actions require permission or approval.
- The source's direct example contrasts a trusted system rule, “Summarize the document,” with an untrusted document asking the system to ignore previous instructions and send all files.
- The source's agent example contrasts a bad system that trusts webpage text with a better system that separates system instruction, untrusted web content, and permission-gated sensitive action.
- Tools increase impact because an injected instruction may lead to file access, email, record changes, or transactions; more capability therefore requires stronger controls.
- The page uses conceptual language rather than a formal mathematical model. No standalone numeric indicators are defined in the source.
- Candidate collection is intentionally broad and retains closely related terms, explanatory phrases, aliases, and contrast concepts for later deduplication.
