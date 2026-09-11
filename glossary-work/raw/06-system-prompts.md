# System Prompts

## Module/Topic/Source File

- Module: 06 · Prompting & System Design
- Topic: System Prompts
- Source File: `system-prompts.html`
- Source page label: `04 · Prompting & System Design · Topic 01`
- Raw-stage scope: maximum source-grounded candidate set; repeated surface forms, aliases, neighboring concepts, process nodes, and beginner-facing phrases are intentionally retained.

## Glossary Candidates

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| System Prompt | 系统提示；系统提示词 | Instructions that guide an AI model inside an application. | 应用交给 AI、用来规定回答方式的一组指令。 |
| system prompt | 系统提示；系统提示词 | A set of instructions sent by an application to guide model behavior. | 应用发送给模型、指导它怎么做事的说明。 |
| System Prompts | 系统提示（复数） | Multiple sets of runtime instructions for AI applications. | 多组在运行时指导 AI 的指令。 |
| system instruction | 系统指令 | An instruction prepared by an application for the model. | 应用预先准备给模型的要求。 |
| system instructions | 系统指令（复数） | The instructions that establish application-level behavior. | 规定应用级行为的一组指令。 |
| instructions | 指令；说明 | Directions telling a model what to do or how to behave. | 告诉模型做什么、怎么做的要求。 |
| set of instructions | 一组指令 | Several instructions that work together. | 一组共同起作用的要求。 |
| guidance | 指导；引导 | Information that steers likely behavior. | 帮模型朝某种行为方向走的信息。 |
| AI guidance | AI 指导 | Guidance given to an AI system. | 给人工智能系统的行为引导。 |
| model guidance | 模型指导 | Instructions or information that steer a model response. | 帮模型决定如何回答的指导。 |
| behavior guidance | 行为指导 | Guidance about how the model should act. | 规定模型应该怎样表现的说明。 |
| guide an AI model | 指导 AI 模型 | Give instructions that influence model behavior. | 用指令影响 AI 模型的行为。 |
| guide the model's behavior | 指导模型行为 | Steer how the model responds. | 引导模型用某种方式回答。 |
| guide an AI application's behavior | 指导 AI 应用行为 | Steer the behavior of the whole AI application at runtime. | 在运行时引导整个 AI 应用如何表现。 |
| behavior | 行为；表现 | The way a model or application responds and acts. | 模型或应用表现出来的回答方式。 |
| model behavior | 模型行为 | The patterns in how a model responds. | 模型通常如何回答、如何做事。 |
| AI behavior | AI 行为 | The way an AI system acts in response to input. | AI 收到输入后表现出的方式。 |
| application's behavior | 应用行为 | How the application behaves while handling requests. | 应用处理请求时表现出来的行为。 |
| runtime behavior | 运行时行为 | Behavior produced while the system is running. | 系统真正运行时出现的表现。 |
| runtime | 运行时 | The period when an application is executing. | 程序正在运行、处理请求的时间。 |
| at runtime | 在运行时 | During actual execution rather than training. | 真正运行和回答时，而不是训练时。 |
| runtime instructions | 运行时指令 | Instructions applied while the model is being used. | 使用模型时临时或持续生效的要求。 |
| runtime guidance | 运行时指导 | Guidance supplied during model use. | 模型工作时提供的引导。 |
| inside an application | 在应用内部 | Within a product or program that uses a model. | 在调用模型的产品或程序里面。 |
| application | 应用；应用程序 | A product or program that uses an AI model. | 把模型用于实际任务的软件。 |
| AI application | AI 应用 | An application that uses an AI model. | 使用 AI 模型提供功能的应用。 |
| model inside an application | 应用中的模型 | A model operating as part of a larger application. | 作为软件一部分运行的模型。 |
| application-level guidance | 应用级指导 | Guidance set by the application rather than the current user. | 由应用统一规定、不是当前用户临时提出的要求。 |
| application-level instruction | 应用级指令 | An instruction originating from the application layer. | 来自应用层的指令。 |
| application sends instructions | 应用发送指令 | The application supplies instructions to the model. | 应用把要求传给模型。 |
| sent by an application | 由应用发送 | Supplied by the surrounding application. | 由外层应用提供。 |
| current request | 当前请求 | The request being handled now. | 系统此刻正在处理的问题或要求。 |
| current task | 当前任务 | The task for the present interaction. | 当前这一轮要完成的事情。 |
| request | 请求；要求 | Something a user or system asks the model to handle. | 用户或系统要求模型处理的事。 |
| handle a request | 处理请求 | Respond to the current request. | 对当前要求作出处理和回答。 |
| request handling | 请求处理 | The process of dealing with an incoming request. | 接收并处理请求的过程。 |
| role | 角色 | The part or identity the model is asked to adopt. | 要求模型扮演或遵循的身份定位。 |
| define a role | 定义角色 | Specify what role the model should play. | 规定模型应该以什么身份工作。 |
| rules | 规则 | Requirements the model should follow. | 模型需要遵守的规定。 |
| define rules | 定义规则 | State requirements for model behavior. | 把模型必须遵守的要求写清楚。 |
| boundaries | 边界 | Limits on what the model should or should not do. | 规定模型能做什么、不能做什么的界线。 |
| policy boundary | 政策边界 | A limit established by a policy or rule. | 政策规定的行为界线。 |
| behavioral boundaries | 行为边界 | Limits placed on model behavior. | 对模型行为设置的限制。 |
| define boundaries | 定义边界 | Specify limits for acceptable behavior. | 明确哪些行为可以、哪些不可以。 |
| tone | 语气；风格 | The manner or emotional style of a response. | 回答听起来是什么语气和感觉。 |
| define tone | 定义语气 | Specify how the response should sound. | 规定回答应该用什么口吻。 |
| output format | 输出格式 | The required shape or organization of an answer. | 规定答案要以什么结构或格式出现。 |
| define output format | 定义输出格式 | Tell the model how to structure its output. | 告诉模型答案应该怎样排版或组织。 |
| output | 输出 | The response produced by a model. | 模型生成出来的回答或结果。 |
| model output | 模型输出 | A response generated by a model. | 模型给出的内容。 |
| generated output | 生成的输出 | Content produced by the model. | 模型生成的结果。 |
| response | 回答；响应 | The model's answer to a task or request. | 模型对任务或请求给出的内容。 |
| answer | 答案；回答 | A response to a question or request. | 对问题或要求的回应。 |
| output format requirement | 输出格式要求 | A requirement describing the form of the output. | 对结果外形、字段或组织方式的要求。 |
| guide a response | 指导回答 | Influence how a response is produced. | 影响模型怎样生成回答。 |
| guide likely behavior | 引导可能行为 | Make a desired behavior more likely. | 让某种行为更可能发生。 |
| likely behavior | 可能行为；倾向行为 | Behavior the model is more likely to produce. | 模型倾向于表现出的行为。 |
| response behavior | 回答行为 | The way the model forms and presents answers. | 模型生成和呈现答案的方式。 |
| does not guarantee every response | 不保证每个回答 | Instructions can guide behavior without ensuring perfection. | 写了规则也不能保证每一次都完全遵守。 |
| guarantee | 保证 | Certainty that an outcome will always occur. | 确保结果一定如此。 |
| guaranteed control | 保证性控制 | Certainty that every output follows every rule. | 确保每个输出都遵守每条规则的控制。 |
| control | 控制 | Ability to determine an outcome exactly. | 能完全决定结果会怎样。 |
| certainty | 确定性 | A guarantee that something will happen as expected. | 结果一定符合预期的程度。 |
| every output | 每个输出 | All responses produced by the model. | 模型生成的每一个结果。 |
| follow every rule | 遵守每条规则 | Obey all specified requirements. | 一条不漏地执行所有规定。 |
| rule following | 规则遵循 | Behavior that obeys stated instructions. | 按照写下来的规则做事。 |
| response reliability | 回答可靠性 | How consistently responses follow intended guidance. | 回答能否稳定符合要求。 |
| validation | 验证；校验 | Checking whether an important result is acceptable. | 检查结果是否可信、合格。 |
| validate the output | 验证输出 | Check whether the generated result is correct or usable. | 检查模型结果能不能使用。 |
| check the output | 检查输出 | Review a generated result. | 看一遍模型生成的结果。 |
| important results | 重要结果 | Outputs that matter enough to require checking. | 出错会有影响、值得复核的结果。 |
| review | 复核；审查 | Examine an output before relying on it. | 在采用结果前再检查一遍。 |
| human review | 人工复核 | A person checks the model's result. | 由人来检查模型结果。 |
| human reviewer | 人工复核者 | A person who reviews an output. | 负责检查结果的人。 |
| review the output | 复核输出 | Inspect the result after generation. | 生成后检查答案。 |
| model does not guarantee | 模型不保证 | A model can follow guidance imperfectly. | 模型有可能没有完全做到要求。 |
| does not retrain the model | 不会重新训练模型 | A system prompt changes the current guidance, not learned parameters. | 系统提示只改当前使用方式，不重新教模型。 |
| retrain | 重新训练 | Train a model again to change what it has learned. | 再训练一次，让模型学到的东西改变。 |
| model training | 模型训练 | The process that changes learned model parameters. | 通过数据学习并调整模型内部参数的过程。 |
| training | 训练 | Learning performed before or during model development. | 在模型开发阶段让模型学习。 |
| learned parameters | 已学习参数 | Internal values learned during training. | 模型训练后形成的内部数值。 |
| parameters | 参数 | Internal values adjusted during training. | 模型内部用来产生结果的一组数值。 |
| model parameters | 模型参数 | The learned internal values of a model. | 模型已经学到的内部数值。 |
| change learned parameters | 改变已学习参数 | Update what the model has learned. | 改变模型训练后形成的内部数值。 |
| parameter update | 参数更新 | An adjustment to model parameters during training. | 训练时修改模型内部数值。 |
| model adaptation | 模型适配 | Further changing a model for a purpose. | 让已有模型适应某个目标的过程。 |
| current input | 当前输入 | Information supplied for this run. | 这一轮送进模型的内容。 |
| prompt | 提示；提示词 | The input instruction or question given to a model. | 给模型的问题或指令。 |
| user prompt | 用户提示；用户提示词 | The user's request for the current turn. | 用户这一轮实际提出的要求。 |
| current-turn request | 当前轮请求 | The request in the present interaction turn. | 当前这一轮对话中的要求。 |
| user request | 用户请求 | A request supplied by the user. | 用户交给模型处理的事情。 |
| current turn | 当前轮次 | The present exchange between user and model. | 当前这一轮对话。 |
| system prompt vs user prompt | 系统提示与用户提示 | Application guidance and the user's current request are different inputs. | 应用规定和用户当下提问不是同一种输入。 |
| application-level guidance vs current request | 应用级指导与当前请求 | One sets general behavior; the other asks for a task now. | 一个规定总体做法，一个提出眼前任务。 |
| context | 上下文；语境 | Information included to help the model handle the request. | 为当前回答提供背景的信息。 |
| add context | 添加上下文 | Include relevant information with the request. | 把相关背景资料一起交给模型。 |
| relevant context | 相关上下文 | Context that helps with the current task. | 对当前任务有帮助的背景信息。 |
| supply information | 提供信息 | Put information into the model input. | 把资料送进模型。 |
| information | 信息 | Content available to guide or support a response. | 模型回答时可以参考的内容。 |
| relevant documents | 相关文档 | Documents included because they matter to the request. | 与当前问题有关、可以参考的文件。 |
| document | 文档 | A piece of written information supplied as context. | 作为资料交给模型的文字文件。 |
| tool results | 工具结果 | Information returned by a tool and included in context. | 工具调用后返回、可供模型参考的结果。 |
| tool result | 工具结果（单数） | The result returned by one tool call. | 一次工具调用返回的信息。 |
| context supplied at runtime | 运行时提供的上下文 | Information added while the application is handling a request. | 应用正在处理请求时加入的背景资料。 |
| system prompt + user prompt + context | 系统提示＋用户提示＋上下文 | The combined inputs used before model generation. | 生成回答前组合起来的三类输入。 |
| combined input | 组合输入 | System instructions, user request, and context together. | 系统要求、用户问题和背景资料合在一起。 |
| input | 输入 | Information sent into the model. | 送进模型的内容。 |
| input to the model | 模型输入 | The complete content supplied for generation. | 模型生成前收到的全部内容。 |
| add rules | 添加规则 | Put behavioral requirements into the system instructions. | 把行为要求写入系统指令。 |
| set behavior | 设定行为 | Establish how the application or model should respond. | 先规定应该怎样回答和做事。 |
| prepare system instructions | 准备系统指令 | Build the application's instructions before the request is handled. | 应用先准备好给模型的要求。 |
| receive the user prompt | 接收用户提示 | Take in the user's current request. | 收到用户这一轮的问题。 |
| supply information to the model | 向模型提供信息 | Include context that can help the task. | 把有用资料放进模型输入。 |
| run the model | 运行模型 | Execute the model on the combined input. | 让模型根据输入真正生成结果。 |
| generate | 生成 | Produce an output from the input. | 根据输入产生回答。 |
| generate an answer | 生成答案 | Produce a response to the task. | 生成对问题的回答。 |
| model generation | 模型生成 | The act of producing an output. | 模型形成答案的过程。 |
| generation step | 生成步骤 | The process step where the model produces output. | 流程中模型真正产生结果的环节。 |
| combined input to the model | 送入模型的组合输入 | The assembled instructions, request, and context. | 组装后一起送给模型的全部内容。 |
| process | 流程；过程 | An ordered sequence for handling a request. | 按顺序完成任务的一连串步骤。 |
| workflow | 工作流；工作流程 | The ordered application process from instructions to review. | 从准备指令到复核结果的工作路径。 |
| five-step process | 五步流程 | Add rules, add request, add context, generate, review. | 添加规则、请求、上下文、生成、复核这五步。 |
| process flow | 流程图；流程 | A sequence showing how the request is handled. | 用顺序表示请求如何被处理。 |
| step | 步骤 | One ordered part of a process. | 流程中的一个环节。 |
| step 1 | 第一步 | Add rules. | 先添加规则。 |
| Step 1: Add rules | 第一步：添加规则 | The application prepares system instructions. | 应用先准备系统要求。 |
| Step 2: Add request | 第二步：添加请求 | Receive the user prompt. | 接着收到用户的当前请求。 |
| Step 3: Add context | 第三步：添加上下文 | Supply relevant information. | 再提供相关背景资料。 |
| Step 4: Generate | 第四步：生成 | Run the model on the combined input. | 让模型根据组合输入生成结果。 |
| Step 5: Review | 第五步：复核 | Check the output. | 最后检查模型输出。 |
| Add rules → Add request → Add context → Generate → Review | 添加规则→添加请求→添加上下文→生成→复核 | The page's five-stage runtime flow. | 页面展示的五阶段运行流程。 |
| prepare | 准备 | Arrange instructions or information before execution. | 在运行前先把指令或资料准备好。 |
| enter the input | 进入输入 | Become part of the content supplied to the model. | 被放进模型要读取的内容里。 |
| information enters the input | 信息进入输入 | Context is included in the model input. | 背景资料被加入模型输入。 |
| current task enters the input | 当前任务进入输入 | The user's task becomes part of the input. | 用户要做的事被放进输入。 |
| use the combined input | 使用组合输入 | Process all included instructions and information together. | 把所有指令和资料一起处理。 |
| relevant | 相关的 | Useful for the current request. | 和当前问题有关、有帮助的。 |
| handle | 处理 | Work on a request or task. | 对要求进行处理。 |
| application prepares | 应用准备 | The application assembles instructions before generation. | 应用在生成前把指令组合好。 |
| request enters the input | 请求进入输入 | The current request is added to the model input. | 当前问题被加入送给模型的内容。 |
| output review | 输出复核 | Checking a model result after generation. | 模型生成后检查结果。 |
| workplace handbook | 工作场所手册；员工手册 | A handbook that sets rules before work begins. | 工作开始前规定做事方法的手册。 |
| workplace handbook analogy | 工作手册类比 | The page compares a system prompt to a workplace handbook. | 页面用工作手册来帮助理解系统提示。 |
| handbook | 手册 | A document that records rules and guidance. | 写着规则和说明的文件。 |
| sets rules before a customer arrives | 在客户到来前设定规则 | The handbook establishes behavior before a case starts. | 在具体请求来之前先定好做法。 |
| customer arrives | 客户到来 | A new customer interaction begins. | 一个客户请求开始进入系统。 |
| handles the current request | 处理当前请求 | The application responds to the present case. | 应用处理眼前这一次问题。 |
| model is not a person | 模型不是人 | The analogy does not mean the model is human. | 工作手册只是比喻，模型并不是人。 |
| analogy | 类比；比喻 | A comparison used to explain a technical idea. | 用熟悉的事物帮助理解技术概念。 |
| customer support | 客户支持；客服 | Help provided when a customer has a problem. | 客户遇到问题时提供帮助。 |
| support example | 客服示例 | The refund-handling example in the page. | 页面用退款问题说明系统提示的例子。 |
| refund | 退款 | Money returned to a customer under a policy. | 按规定把钱退还给客户。 |
| ask about a refund | 询问退款 | A customer request concerning a refund. | 客户来问能不能退款。 |
| customer asks about a refund | 客户询问退款 | The input in the everyday support example. | 客服实例中的用户问题。 |
| company policy | 公司政策 | Rules the company uses to decide how to respond. | 公司规定的处理标准。 |
| follow company policy | 遵循公司政策 | Give an answer consistent with company rules. | 按公司规定回答，不自行改变规则。 |
| avoid inventing rules | 避免编造规则 | Do not make up a policy that does not exist. | 不要凭空编一个公司没有的规定。 |
| invent rules | 编造规则 | Make up unsupported requirements or policies. | 把不存在的规定说成真的。 |
| policy-based answer | 基于政策的回答 | An answer grounded in company policy. | 依据公司规定给出的回答。 |
| human review in support | 客服中的人工复核 | Escalating a support case to a person. | 让人工检查或处理客服问题。 |
| human review outcome | 人工复核结果 | A support case resolved or checked by a person. | 人工检查后给出的处理结果。 |
| policy-compliant answer | 符合政策的回答 | A response that follows the relevant policy. | 遵守相关规定的回答。 |
| invoice data | 发票数据 | Information extracted from an invoice. | 从发票里整理出来的数据。 |
| invoice | 发票 | A document containing billing information. | 记录交易和金额的单据。 |
| invoice example | 发票示例 | The business example involving structured extraction. | 页面用发票抽取说明系统提示的例子。 |
| required schema | 要求的模式；规定的结构 | The required fields and structure for the output. | 结果必须包含的字段和结构。 |
| schema | 模式；数据结构 | A formal description of fields and their arrangement. | 规定数据有哪些字段、怎样排列的结构。 |
| input: an invoice and a required schema | 输入：发票和要求的模式 | The two inputs in the invoice example. | 发票实例中送给系统的两类输入。 |
| extract fields | 提取字段 | Find and return requested pieces of information. | 从发票中找出指定信息。 |
| field | 字段 | One named piece of structured data. | 结构化数据中的一项信息。 |
| data extraction | 数据提取 | Pull structured information from a document. | 从文件中抽出可用数据。 |
| mark uncertain values | 标记不确定值 | Identify values that may not be reliable. | 把模型不确定的数字或内容标出来。 |
| uncertain value | 不确定值 | A value the system is not confident enough to trust automatically. | 模型没有把握、需要留意的值。 |
| uncertainty | 不确定性 | Lack of certainty about a result or value. | 对结果或内容没有十足把握。 |
| structured invoice data | 结构化发票数据 | Invoice information returned in an organized schema. | 按固定字段整理好的发票信息。 |
| structured data | 结构化数据 | Data organized into defined fields or a schema. | 按固定格式、字段排列的数据。 |
| data extraction from an invoice | 从发票提取数据 | Extract fields from invoice content. | 从发票内容中找出字段。 |
| required output schema | 要求的输出模式 | The structure the generated result must follow. | 模型输出必须遵守的结构。 |
| uncertain field | 不确定字段 | A requested field whose value may be unreliable. | 找到了但不太确定是否正确的字段。 |
| structured output | 结构化输出 | Output arranged according to a specified schema. | 按规定字段和格式输出的结果。 |
| structured outputs | 结构化输出（复数） | Generated results that follow a defined structure. | 遵守固定结构的一类模型结果。 |
| system prompt ≠ user prompt | 系统提示不等于用户提示 | System guidance is different from the current user request. | 应用给的规则和用户当前提问不是一回事。 |
| system prompt ≠ model training | 系统提示不等于模型训练 | Runtime instructions are different from changing learned parameters. | 运行时指令不等于重新训练模型。 |
| system prompt ≠ guaranteed control | 系统提示不等于保证性控制 | Guidance does not guarantee every output. | 有指导不代表能百分之百控制结果。 |
| model training changes learned parameters | 模型训练会改变已学习参数 | Training updates internal model values. | 训练会改变模型内部学到的数值。 |
| runtime instruction | 运行时指令 | An instruction used while the model is serving a request. | 模型正在回答时使用的指令。 |
| current-turn instruction | 当前轮指令 | An instruction for the present turn. | 只针对当前这一轮的要求。 |
| instruction hierarchy | 指令层级 | An ordering of instruction sources by authority. | 不同来源指令之间的优先级关系。 |
| authority | 权限；优先级 | The degree to which an instruction controls behavior. | 哪条指令更有权要求模型这样做。 |
| instruction priority | 指令优先级 | Which instruction should take precedence. | 冲突时先听哪条要求。 |
| prompt hierarchy | 提示层级 | The ordering among system, user, and other prompts. | 系统提示、用户提示等之间的层次。 |
| LLM | 大语言模型 | A large language model that generates text responses. | 能理解和生成语言的大型模型。 |
| large language model | 大语言模型 | A model trained to process and generate language. | 用大量语言数据训练、能生成文字的模型。 |
| language model | 语言模型 | A model that works with language sequences. | 处理和预测语言内容的模型。 |
| application → system prompt + user prompt + context → LLM → output | 应用→系统提示＋用户提示＋上下文→LLM→输出 | A compact map from application inputs to model output. | 从应用提供输入到模型生成结果的关系图。 |
| model invocation | 模型调用 | Running a model with a prepared input. | 把准备好的内容交给模型运行一次。 |
| inference | 推理；模型推理 | Using a trained model to produce an output. | 用已经训练好的模型生成结果。 |
| inference-time instruction | 推理时指令 | Guidance supplied during inference. | 模型推理回答时加入的要求。 |
| prompt engineering | 提示工程 | Designing prompts to influence model behavior. | 设计提示词来影响模型表现的方法。 |
| prompt design | 提示设计 | Planning the content and structure of prompts. | 规划提示内容和结构。 |
| system design | 系统设计 | Designing the application around the model. | 设计包围和使用模型的整个应用系统。 |
| prompting and system design | 提示与系统设计 | The topic area containing system prompts. | 研究怎样写提示、怎样设计模型应用的领域。 |
| behavior specification | 行为规范 | A description of the behavior an application wants. | 把希望应用怎样表现写清楚。 |
| policy instruction | 政策指令 | An instruction based on a rule or policy. | 把政策要求传给模型的指令。 |
| format constraint | 格式约束 | A limit on the shape of generated output. | 对模型输出格式设置的限制。 |
| content constraint | 内容约束 | A limit on what the response may contain. | 对回答可以包含什么设置的限制。 |
| safety boundary | 安全边界 | A limit intended to prevent unsafe behavior. | 防止模型做危险事情的界线。 |
| domain rule | 领域规则 | A rule specific to an application domain. | 某个业务或行业中特有的规定。 |
| request-specific context | 请求特定上下文 | Context selected for the current request. | 专门为这一次问题准备的背景资料。 |
| source documents | 来源文档 | Documents supplied as supporting information. | 用来支持回答的原始文件。 |
| tool calling | 工具调用 | Using a tool and possibly adding its result to context. | 调用外部工具并把结果提供给模型。 |
| model output validation | 模型输出验证 | Checking whether output satisfies important requirements. | 检查结果是否满足关键要求。 |
| fallback to human review | 转人工复核 | Send an uncertain or important case to a person. | 不确定时交给人工处理。 |
| escalation | 升级处理 | Move a case to a higher level or human reviewer. | 把复杂、重要或不确定的问题交给更合适的人。 |
| operational policy | 运营政策；操作政策 | Rules for handling real application cases. | 实际业务处理中要遵守的规则。 |
| application behavior contract | 应用行为契约 | An informal description of expected application behavior. | 对应用应该怎样表现的约定。 |
| expected behavior | 预期行为 | Behavior the designer wants the system to produce. | 设计者希望系统表现出来的方式。 |
| desired response | 期望回答 | The kind of response the application wants. | 应用希望模型给出的回答类型。 |
| response format | 回答格式 | The structure and presentation of a response. | 回答怎样组织和呈现。 |
| response constraint | 回答约束 | A rule limiting response content or format. | 限制回答内容或格式的规则。 |
| application context | 应用上下文 | Information about the application and current task. | 应用场景和当前任务相关的背景。 |
| system context | 系统上下文 | System-provided information available to the model. | 系统提供给模型的背景信息。 |
| user context | 用户上下文 | User-provided information relevant to the request. | 用户提供、能帮助回答的背景。 |
| output checking | 输出检查 | Looking for errors or requirement violations. | 检查结果有没有错或违反要求。 |
| source-grounded answer | 有来源依据的回答 | An answer grounded in supplied policy or documents. | 根据给定规则或资料作答，而不是凭空猜。 |
| hallucinated policy | 幻觉式政策；编造政策 | A policy claim not supported by the actual rules. | 模型把不存在的规定说成真的。 |
| unsupported answer | 无依据回答 | An answer not supported by the available rules or context. | 现有规则和资料没有支持的回答。 |
| reliable output | 可靠输出 | Output that has been checked enough for its use. | 经过适当检查、可以较放心使用的结果。 |
| raw candidate | 原始候选 | A term retained before glossary normalization. | 还没合并、删减或规范化的候选词。 |
| terminology candidate | 术语候选 | A possible term to consider for the final glossary. | 将来可能进入正式词汇表的词。 |
| beginner-facing phrase | 面向初学者的表达 | A simple phrase used to explain a technical idea. | 页面为了小白理解而使用的简单说法。 |
| professional term | 专业术语 | A technical term used in AI or application design. | AI 或应用设计领域里的技术词。 |

## Potential Missing Concepts

- **Instruction hierarchy and precedence rules**: The page distinguishes system and user prompts but does not explain what happens when instructions conflict or which source has priority.
- **Developer messages and other message roles**: A real chat protocol may include developer, tool, assistant, and system roles beyond the two roles shown here.
- **Prompt serialization and message boundaries**: The page shows combined inputs but does not explain how messages are encoded, delimited, or represented to the model.
- **Tokenization, token budget, and context-window limits**: Long system prompts, documents, and tool results consume context and may be truncated.
- **Prompt injection and instruction-conflict attacks**: User content or retrieved documents may contain instructions that attempt to override the intended system behavior.
- **Data exfiltration and secret leakage**: A system prompt may contain sensitive policy or operational details that should not be revealed.
- **System-prompt leakage**: The page does not discuss attempts to make the model disclose hidden instructions.
- **Guardrails and policy enforcement**: A prompt is guidance; separate classifiers, filters, permissions, or deterministic checks may be needed for stronger enforcement.
- **Structured output validation**: A required schema is named, but the page does not explain JSON/schema validation, retries, repair, or rejection of invalid output.
- **Tool permissions and least privilege**: Tool results are mentioned, but tool authorization, scoped permissions, and confirmation before side effects are absent.
- **Grounding and retrieval**: Relevant documents are named, but retrieval, source selection, citation, and grounding quality are not described.
- **Prompt templates and variables**: Reusable templates, slots, escaping, and request-specific substitution are not explained.
- **Prompt versioning and change management**: The page does not cover tracking which system-prompt version produced an output.
- **Prompt evaluation and regression testing**: There are no test sets, golden answers, rubrics, or automated evaluations for prompt changes.
- **Observability and tracing**: Logging the prompt, context, tools, model version, latency, and output is not discussed.
- **Privacy and data minimization**: Supplying documents and tool results raises questions about sensitive data, retention, and access control.
- **Model selection and capability differences**: The page treats “the model” generically and does not explain that models may follow instructions differently.
- **Decoding and sampling controls**: Temperature, top-p, deterministic decoding, and other generation settings are not covered.
- **Latency, cost, and context trade-offs**: More instructions and context may increase cost and response time, but these operational metrics are absent.
- **Human-in-the-loop design**: Human review appears in the examples, but routing criteria, reviewer UX, and escalation ownership are not defined.
- **Confidence calibration**: “Uncertain values” are mentioned, but the page does not explain confidence scores, thresholds, or calibration.
- **Error taxonomy and failure handling**: The page says outputs may need validation but does not enumerate refusal, omission, fabrication, formatting, or policy failures.
- **Access control and tenant isolation**: Application-level instructions may differ across users or organizations; authorization boundaries are not described.
- **Prompt injection-resistant context design**: The page does not distinguish trusted system instructions from untrusted documents or tool output.
- **Policy updates and rollout**: It does not explain how to deploy, test, canary, roll back, or audit changes to a system prompt.
- **Prompt caching and reuse**: Reusing stable system instructions can affect latency and cost, but caching is not discussed.
- **Multilingual prompts and localization**: Tone, policy wording, and instruction following across languages are not addressed.
- **Model refusal and safe completion**: Safety boundaries are implied but refusal behavior and safe alternatives are not explained.
- **Evaluation metrics**: No explicit metrics such as task success, schema validity, policy compliance, factuality, refusal rate, or human-review rate are provided.

## Aliases / Synonyms

- System prompt / system instruction / system message / system-level prompt / application instruction / application-level guidance
- System prompts / system instructions / system messages / runtime instructions
- Prompt / prompt text / prompt input / model instruction / model input
- User prompt / user message / user request / current request / current-turn request / current task
- Application / app / AI application / model-powered application / surrounding application
- Guidance / instruction / direction / steering signal / behavior specification
- Behavior / model behavior / response behavior / application behavior / runtime behavior
- Rules / requirements / constraints / policy rules / operating rules / domain rules
- Boundaries / limits / constraints / guardrails / safety boundaries / policy boundaries
- Tone / voice / style / response style / writing manner
- Output / model output / generated output / response / answer / result
- Output format / response format / output schema / required schema / structured-output format
- Context / prompt context / request context / application context / supplied information / supporting information
- Document / source document / relevant document / reference document / retrieved document
- Tool result / tool output / returned information / external result / retrieved context
- Generate / produce / run the model / model invocation / inference / model generation
- Review / check / validate / inspect / verify / human review
- Validation / output validation / result checking / schema validation / quality check
- Human review / manual review / human verification / human oversight / human-in-the-loop
- Training / model training / learning / parameter learning / model fitting
- Retrain / retraining / additional training / further training / update the model
- Parameters / model parameters / learned parameters / internal values / learned weights
- LLM / large language model / language model / text-generation model
- Structured output / structured outputs / schema-constrained output / structured data response
- Uncertain value / uncertain field / low-confidence value / questionable value
- Policy-based answer / policy-compliant answer / rules-based answer / grounded answer
- Refund request / refund question / customer refund case / support refund case
- Invoice data / invoice fields / billing data / extracted invoice information
- Add rules / set behavior / define behavior / establish rules / prepare instructions
- Add request / receive request / receive user prompt / accept current task
- Add context / supply context / include information / provide relevant documents / attach tool results
- Generate / run / execute inference / produce a response / create output
- Review / check output / inspect result / validate response / escalate for review
- Application → system prompt + user prompt + context → LLM → output / application-to-model flow / prompt-processing flow / request-to-output flow
- System prompt vs user prompt / system prompt not user prompt / application guidance versus user request
- System prompt vs model training / runtime instruction versus training / prompt-time guidance versus parameter update
- System prompt vs guaranteed control / guidance versus guarantee / likely behavior versus certainty
- Prompt design / prompt engineering / prompting / prompt authoring
- System design / AI application design / model application architecture / prompt-and-system design

## Do Not Confuse Candidates

- **System prompt vs user prompt**: A system prompt is application-level guidance; a user prompt is the request for the current turn.
- **System prompt vs system message**: These may refer to similar concepts in different interfaces, but a product's exact message-role semantics should be checked.
- **System prompt vs developer message**: Some APIs distinguish developer-level instructions from system-level instructions; the page does not define that protocol distinction.
- **System prompt vs context**: A system prompt establishes guidance; context supplies information relevant to the current task.
- **System prompt vs retrieved document**: A system prompt is an instruction source; a retrieved document is usually content to consult and may be untrusted.
- **System prompt vs tool result**: A system prompt guides behavior; a tool result is returned information that may be added to the input.
- **System prompt vs user request**: The application sets general behavior; the user asks for a specific task now.
- **System prompt vs prompt engineering**: A system prompt is an artifact or message; prompt engineering is the practice of designing prompts.
- **System prompt vs model training**: A system prompt guides a runtime response; training changes learned parameters.
- **System prompt vs fine-tuning**: A prompt changes the current input; fine-tuning changes the model through additional training.
- **System prompt vs pre-training**: A prompt is used after a model exists; pre-training builds broad model capability.
- **System prompt vs instruction tuning**: Instruction tuning changes learned behavior during training; a system prompt provides runtime instructions.
- **System prompt vs reinforcement learning**: Runtime guidance is not a reward-based learning procedure.
- **Guidance vs control**: Guidance makes behavior more likely; control would imply certainty over every output.
- **Instruction vs guarantee**: An instruction states what should happen; it does not prove that it will happen every time.
- **Rules vs policies**: Rules are requirements in the prompt; a policy is the broader organizational or domain standard behind them.
- **Boundary vs prohibition**: A boundary describes a limit; a prohibition is one specific forbidden action.
- **Tone vs style**: Tone is the manner or emotional voice; style can also include format, length, and organization.
- **Output format vs output content**: Format describes shape and organization; content is what the answer says.
- **Schema vs format**: A schema specifies fields and structure; “format” can be a looser presentation requirement.
- **Structured output vs structured data**: Structured output is a generated response following a structure; structured data is the organized data itself.
- **Context vs input**: Context is supporting information; input is the full content sent to the model.
- **Current task vs current context**: The task is what must be done; context is information that helps do it.
- **Relevant document vs authoritative document**: Relevance helps answer a question; authority concerns whether the source should be trusted.
- **Tool result vs tool instruction**: A tool result is returned data; a tool instruction describes or requests an action.
- **Generate vs run the model**: Generation is producing output; running the model is the execution step that produces it.
- **Inference vs training**: Inference uses a trained model; training changes or fits the model.
- **Review vs validation**: Review may be human or qualitative; validation may be a formal or automated check.
- **Human review vs guaranteed correctness**: Human review is a safeguard, not proof that the result is correct.
- **Uncertain value vs incorrect value**: Uncertainty means the system lacks confidence; it does not prove the value is wrong.
- **Policy-based answer vs hallucinated policy**: A policy-based answer follows supplied policy; a hallucinated policy invents unsupported rules.
- **Company policy vs system prompt**: Company policy is the business rule; the system prompt is one mechanism for communicating it to a model.
- **Invoice field vs invoice schema**: A field is one item; a schema defines the set and arrangement of fields.
- **Application vs model**: The application is the surrounding product or program; the model is one component inside it.
- **AI application vs LLM**: An AI application can include prompts, tools, validation, and UI; an LLM is the model component.
- **LLM vs system prompt**: An LLM generates language; a system prompt provides runtime instructions to it.
- **Model behavior vs model parameters**: Behavior is what users observe; parameters are internal learned values.
- **Runtime vs training time**: Runtime is when the application handles requests; training time is when the model learns.
- **Runtime instruction vs learned behavior**: A runtime instruction is supplied now; learned behavior comes from training.
- **Prompt injection vs ordinary user prompt**: A user prompt asks for a task; prompt injection attempts to manipulate instruction priority or expose protected information.
- **Guardrail vs prompt wording**: A prompt can guide behavior; a guardrail may include independent enforcement mechanisms.
- **Schema requirement vs schema validation**: A requirement asks for a structure; validation checks whether the output actually matches it.
- **Response quality vs response compliance**: Quality concerns usefulness or correctness; compliance concerns following rules and format.
- **Response consistency vs response guarantee**: Consistency is a tendency across runs; a guarantee means no exceptions.
- **Source grounding vs model memory**: Grounding uses supplied sources for the current request; model memory refers to learned parameters or application state.
- **Application policy vs model capability**: A policy says what should be done; capability concerns what the model can do.
- **Human escalation vs model refusal**: Escalation sends a case to a person; refusal is the model declining to provide an answer or action.

## Notes

- The source file was read in full, including the title, lede, on-page navigation, definition, workplace-handbook analogy, five-step process, support refund example, invoice/schema example, three “What it is NOT” comparisons, related-concepts chain, takeaway, and video placeholder.
- Primary source wording emphasizes: system prompt, instructions, application, AI model, behavior, role, rules, boundaries, tone, output format, runtime, response, model training, learned parameters, user prompt, current turn, context, relevant documents, tool results, combined input, generation, output review, validation, company policy, refunds, human review, invoices, schemas, fields, uncertain values, structured data, LLM, and output.
- The page uses a workplace handbook as an analogy; the model is explicitly not a person, and the analogy does not guarantee that every response follows every rule.
- The five process nodes are retained both as individual candidates and as the full flow: Add rules → Add request → Add context → Generate → Review.
- The support example retains “customer asks about a refund,” “follows company policy,” “avoids inventing rules,” “policy-based answer,” and “human review” as separate raw candidates because each names a distinct process or failure boundary.
- The invoice example retains “invoice,” “required schema,” “extracts fields,” “marks uncertain values,” and “structured invoice data” separately; none is silently collapsed into “structured output.”
- The source explicitly contrasts system prompt with user prompt, model training, and guaranteed control. These comparison phrases are retained as candidates and repeated in Do Not Confuse Candidates.
- “System prompt,” “system instruction,” “system message,” “application-level guidance,” and “runtime instruction” are related but interface-dependent terms; normalization should happen later.
- “Context,” “relevant documents,” and “tool results” are retained because the page explicitly says they may be included in the combined input, even though it does not explain retrieval or trust boundaries.
- No explicit numeric metric appears in the source body. Metric-related follow-ups are listed under Potential Missing Concepts rather than being presented as source-defined facts.
- Raw-stage policy: preserve capitalization, singular/plural variants, exact source phrases, process labels, neighboring technical terms, aliases, and plausible easily-confused concepts. Do not deduplicate or prune at this stage.
- No website files, CSS, scripts, video assets, or GitHub state were modified.
