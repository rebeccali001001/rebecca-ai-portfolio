# Topic

Prompting vs RAG vs Fine-tuning

## Module/Topic/Source File

- Module: 04 · Training & Model Adaptation
- Topic: Prompting vs RAG vs Fine-tuning
- Source File: `prompting-vs-rag-vs-fine-tuning.html`
- Collection mode: Raw maximum-candidate collection; duplicates, aliases, repeated contextual uses, and potentially overlapping concepts are intentionally retained.

## Glossary Candidates

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Prompting | 提示；提示设计 | Guiding a model by giving it instructions or source material at runtime. | 在模型工作时告诉它要做什么、怎么做。 |
| prompting | 提示；提示设计 | Guiding a model through instructions or supplied material. | 用提示词引导模型完成任务的方法。 |
| prompt | 提示词；提示 | Text or other input that tells a generative system what to do. | 交给生成式 AI 的任务说明或输入。 |
| system prompt | 系统提示 | Instructions that define rules or behavior for the model. | 给模型规定身份、规则和工作方式的提示。 |
| user prompt | 用户提示 | The user-provided request or instruction. | 用户直接交给模型的问题或要求。 |
| SYSTEM / USER PROMPT | 系统／用户提示 | The combined instruction layer supplied at runtime. | 系统规则和用户要求组成的运行时指令。 |
| instructions | 指令；说明 | Guidance that tells a model what to do. | 告诉模型行动方向的文字要求。 |
| clear instructions | 清晰指令 | Instructions that make the requested behavior easier to follow. | 写得明确、让模型不容易误解的要求。 |
| task rules | 任务规则 | Rules that constrain how a task should be performed. | 完成任务时必须遵守的规则。 |
| runtime | 运行时 | The period when an application is actively handling a request. | 用户发来请求、系统正在处理的时间。 |
| runtime instruction | 运行时指令 | An instruction supplied while the model is being used. | 模型已经上线工作时临时给它的说明。 |
| runtime guidance | 运行时引导 | Guidance provided during inference rather than training. | 不重新训练模型、在使用时给的引导。 |
| RAG | 检索增强生成 | Generation guided by information retrieved at runtime. | 先查资料，再让模型结合资料生成答案。 |
| Retrieval-Augmented Generation | 检索增强生成 | A method that retrieves relevant information and adds it to generation context. | 先从资料库找相关内容，再把内容交给模型回答。 |
| retrieval | 检索 | Finding and bringing relevant external information into a task. | 从外部资料中找出相关信息。 |
| retrieve | 检索；取回 | Find and return relevant information. | 找到并取回有用的资料。 |
| retrieved information | 检索到的信息 | External information found for the current request. | 针对当前问题查到的资料。 |
| retrieved context | 检索上下文 | Retrieved material supplied to the model as context. | 查到后放进请求里的参考资料。 |
| external context | 外部上下文 | Information outside the model’s original request or parameters. | 模型原本看不到、由外部补充进来的信息。 |
| context | 上下文 | Information available to the model while producing a response. | 模型当前可以看到并参考的内容。 |
| available context | 可用上下文 | The information exposed to the model for a request. | 这次回答时模型能看到的资料范围。 |
| RAG context | RAG 上下文 | Retrieved information added to a model request. | RAG 查到并交给模型参考的内容。 |
| current context | 当前上下文 | Information relevant to the present request and time. | 这一次回答所依据的最新相关信息。 |
| current information | 当前信息 | Information that reflects the present state or latest facts. | 现在有效、不是旧版本的资料。 |
| changing facts | 变化中的事实 | Facts that may change after a model was trained. | 会随时间更新的政策、价格或数据。 |
| external knowledge | 外部知识 | Knowledge supplied from outside the model. | 从模型外部资料库或文件提供的知识。 |
| private information | 私有信息 | Information restricted to an organization or permitted users. | 不是公开资料、只有特定人能看的信息。 |
| frequently changing information | 经常变化的信息 | Information that is updated often. | 经常修改、需要不断获取最新版本的内容。 |
| knowledge retrieval | 知识检索 | Retrieving relevant knowledge for a task. | 为了回答问题去知识库里找资料。 |
| knowledge base | 知识库 | A collection of information used as a retrieval source. | 专门存放可查询资料的地方。 |
| document retrieval | 文档检索 | Finding relevant documents for a request. | 从很多文件中找到和问题有关的文件。 |
| source document | 来源文档 | A document used to supply facts or evidence. | 作为回答依据的原始文件。 |
| source material | 来源材料 | Material supplied to guide a task or generation. | 给模型参考的原始资料。 |
| latest HR policy | 最新 HR 政策 | The current version of a human-resources policy. | 公司人事政策的最新版本。 |
| current product policies | 当前产品政策 | Product rules and policies that are valid now. | 现在仍然有效的产品规定。 |
| policy information | 政策信息 | Information describing an organization’s rules. | 说明公司规定或政策的资料。 |
| employee leave-policy question | 员工休假政策问题 | A question about rules for employee leave. | 员工询问请假规定的问题。 |
| employee leave policy | 员工休假政策 | Rules governing employee leave. | 公司规定员工如何请假、休假的规则。 |
| fine-tuning | 微调 | Additional training that changes a model for narrower behavior or tasks. | 在基础模型上继续训练，让它更适合特定用途。 |
| fine-tuned model | 微调模型 | A model adapted by additional training. | 经过额外训练、行为更专门的模型。 |
| additional training | 额外训练 | Training performed after an initial model has been created. | 基础训练之后再进行的一轮训练。 |
| training | 训练 | The process of changing model parameters using examples. | 用很多例子调整模型内部数值的过程。 |
| training examples | 训练示例 | Examples used to teach a desired model behavior. | 用来教模型应该怎样回答或行动的例子。 |
| desired behavior | 期望行为 | The response behavior a system is intended to produce. | 希望模型稳定表现出来的方式。 |
| learned behavior | 学习到的行为 | Behavior encoded through training. | 模型训练后学会并保留下来的表现方式。 |
| specialized behavior | 专门化行为 | Behavior suited to a particular domain or task. | 针对某个行业或任务特别适配的行为。 |
| task-specific behavior | 任务特定行为 | Behavior adapted for one particular use. | 为某一个具体用途设计的表现。 |
| model adaptation | 模型适配 | Changing or guiding a model to fit a task. | 让通用模型更适合某个实际任务。 |
| task adaptation | 任务适配 | Adjusting a model or application for a specific task. | 根据任务需要调整模型或应用。 |
| model parameters | 模型参数 | Numerical values changed during training and used by the model. | 模型内部保存规律的一大批数字。 |
| parameters | 参数 | Internal numerical values that determine model behavior. | 决定模型如何处理输入的内部数值。 |
| learned parameters | 学习得到的参数 | Parameters obtained through training. | 模型从训练例子中学出来的数值。 |
| parameter change | 参数变化 | A change to the model’s learned numerical values. | 模型内部学到的数字被重新调整。 |
| learned model behavior | 学到的模型行为 | Behavior represented in the trained model. | 训练后模型比较固定的回答或行动倾向。 |
| base model | 基础模型；底座模型 | A general model used as the starting point for adaptation. | 后续提示、检索或微调所基于的通用模型。 |
| foundation model | 基础模型 | A broadly trained model reusable across many tasks. | 先广泛训练、可以再适配多种任务的模型。 |
| model | 模型 | A learned mechanism that maps inputs to outputs. | 学过规律、能把输入变成输出的程序。 |
| AI model | AI 模型 | A model used to perform an artificial-intelligence task. | 用来完成 AI 任务的模型。 |
| generative model | 生成模型 | A model that creates new outputs. | 能根据输入产出新内容的模型。 |
| capability | 能力 | What a model is able to do. | 模型能完成哪些事情。 |
| model capability | 模型能力 | The abilities already available in a model. | 模型本身已经具备的处理能力。 |
| response behavior | 回答行为 | The way a model produces and structures responses. | 模型回答问题时表现出的方式。 |
| task performance | 任务表现 | How well a system performs a task. | 系统把任务做得好不好的程度。 |
| instructions layer | 指令层 | The runtime layer that tells a model how to act. | 在运行时给模型规定做法的那一层。 |
| context layer | 上下文层 | The information layer made available to the model. | 在运行时给模型提供资料的那一层。 |
| training layer | 训练层 | The adaptation layer where model parameters are changed. | 通过训练改变模型内部参数的那一层。 |
| application layer | 应用层 | The product or workflow that combines model capabilities. | 把模型、规则和资料组合成实际功能的那一层。 |
| application | 应用 | A concrete use of a model in a product or workflow. | 把模型用于真实场景的具体功能。 |
| AI application | AI 应用 | An application that uses one or more AI capabilities. | 把 AI 能力做成可使用功能的应用。 |
| AI system | AI 系统 | The model, instructions, data, retrieval, and application around a task. | 为完成 AI 任务而组合起来的完整系统。 |
| support system | 支持系统 | A system that helps answer or handle support requests. | 帮助客服处理问题的系统。 |
| employee leave-policy answering | 员工休假政策问答 | Answering employee questions about leave rules. | 回答员工请假政策问题的功能。 |
| answer employee leave-policy questions accurately | 准确回答员工休假政策问题 | A target task requiring accurate policy answers. | 目标是把员工关于休假的问题答准确。 |
| accurate answer | 准确回答 | A response that correctly reflects the relevant facts. | 内容与正确政策一致的回答。 |
| answer clearly | 清晰回答 | Produce an answer that is easy to understand. | 用容易看懂的方式回答。 |
| supplied policy information | 已提供的政策信息 | Policy information supplied as the allowed answer source. | 已经给模型、允许它参考的政策资料。 |
| answer only from supplied information | 只依据已提供信息回答 | Restrict answers to the supplied material. | 不凭空补充，只用给定资料回答。 |
| behavior example | 行为示例 | An example showing how a model should respond. | 展示模型应该怎样回答的例子。 |
| model behavior | 模型行为 | The model’s observable way of responding. | 从回答中看到的模型表现方式。 |
| model adaptation through training | 通过训练进行模型适配 | Using more training to change learned behavior. | 再训练模型，使它学会新的稳定表现。 |
| runtime retrieval | 运行时检索 | Retrieving information while handling a request. | 用户提问时即时去资料库查内容。 |
| runtime context change | 运行时上下文变化 | Changing the information visible to the model for a request. | 不改模型本身，只改变这次它能参考的内容。 |
| parameter update | 参数更新 | Changing learned model values through training. | 训练时重新调整模型内部数字。 |
| model update | 模型更新 | A change to the model itself. | 模型内部能力或参数发生改变。 |
| request | 请求 | The input task sent to an AI system. | 用户交给系统要完成的事情。 |
| user request | 用户请求 | A request supplied by the user. | 用户提出的问题或任务。 |
| task | 任务 | Work the AI system is asked to perform. | 希望系统完成的一件事。 |
| input | 输入 | Information or instructions provided to a system. | 送进系统的信息或要求。 |
| output | 输出 | The result returned by a system. | 系统处理后返回的结果。 |
| response | 回答；响应 | An output produced in response to a request. | 系统针对请求给出的回答。 |
| generated answer | 生成的答案 | An answer produced by the model. | 模型生成出来的回答。 |
| generated response | 生成的响应 | A response created by the model. | 模型生成的回复内容。 |
| generation | 生成 | Producing an answer or other new content. | 根据输入产生新的内容。 |
| inference | 推理；推断 | Using a model at runtime to produce an output. | 用已经训练好的模型处理当前请求。 |
| serving | 服务推理 | Running a model so applications can send it requests. | 让模型上线、可以接收请求并返回结果。 |
| inference time | 推理时间 | The time when the model handles a request. | 模型正在处理问题并生成结果的阶段。 |
| training time | 训练时间 | The time when model parameters are learned or updated. | 模型通过例子学习和调整参数的阶段。 |
| retrieval step | 检索步骤 | The step that finds relevant external material. | 先从资料来源找相关内容的步骤。 |
| generation step | 生成步骤 | The step that produces the final response. | 模型根据请求和资料写出答案的步骤。 |
| training step | 训练步骤 | A step in which examples are used to update a model. | 用训练例子调整模型的步骤。 |
| decision flow | 决策流 | An ordered process for choosing an adaptation method. | 按问题一步步决定用哪种方法。 |
| decision rule | 决策规则 | A condition used to choose among prompting, RAG, and fine-tuning. | 根据需求判断该选提示、检索还是微调的规则。 |
| better instruction | 更好的指令 | A clearer instruction that may solve the task without adaptation. | 只把要求说清楚就能解决问题的情况。 |
| external / current information | 外部／当前信息 | Information not already available in the model and possibly changing. | 模型外部、而且可能更新的资料。 |
| learned behavior adaptation | 学习行为适配 | Changing learned behavior when prompting or context is insufficient. | 提示和资料都不够时，再改变模型学到的行为。 |
| combine | 组合 | Use multiple methods in the same system. | 把两种或多种方法一起使用。 |
| combined approach | 组合方法 | A system that uses prompting, RAG, and/or fine-tuning together. | 同时用提示、检索和微调来完成任务。 |
| hybrid system | 混合系统 | A system combining multiple adaptation mechanisms. | 把不同机制组合在一起的系统。 |
| fine-tuned model + system/user prompt + RAG context | 微调模型＋系统／用户提示＋RAG 上下文 | A combined stack for behavior, task rules, and current facts. | 模型负责行为，提示负责规则，RAG 负责最新资料。 |
| response behavior | 回答行为 | The model behavior supplied by a fine-tuned model. | 微调模型提供的回答风格和行为。 |
| task rules | 任务规则 | The rules supplied by a system or user prompt. | 系统提示或用户提示规定的任务要求。 |
| current product policies | 当前产品政策 | The current facts supplied by RAG context. | RAG 提供的现行产品规定。 |
| AI support application | AI 支持应用 | A support product combining model behavior, instructions, and retrieved policy. | 用 AI 帮用户或客服回答问题的实际产品。 |
| side-by-side comparison | 并列对比 | Comparing methods across the same set of questions. | 把几种方法放在一起逐项比较。 |
| comparison criterion | 对比标准 | A question used to compare methods. | 用来判断不同方法差异的一个标准。 |
| changes instructions | 改变指令 | Whether a method changes the instructions sent to the model. | 看这种方法会不会修改给模型的要求。 |
| adds external knowledge | 添加外部知识 | Whether a method supplies knowledge from outside the model. | 看这种方法会不会补充模型外部的资料。 |
| changes model parameters | 改变模型参数 | Whether a method updates internal learned values. | 看这种方法会不会改模型内部数字。 |
| works at runtime | 在运行时工作 | Whether a method operates while handling a request. | 看它是不是用户提问时即时起作用。 |
| requires training | 需要训练 | Whether additional model training is needed. | 看是不是要重新用例子训练模型。 |
| good for changing facts | 适合变化中的事实 | Useful when information changes frequently. | 资料经常更新时是否适合这种方法。 |
| good for behavior / style | 适合行为／风格 | Useful for consistent response behavior or style. | 需要稳定回答方式或风格时是否适合。 |
| behavior | 行为 | The way a model responds or acts. | 模型遇到事情时表现出来的方式。 |
| style | 风格 | The characteristic way a response is written or presented. | 回答呈现出来的语气和写法。 |
| consistency | 一致性 | The degree to which a model behaves similarly across cases. | 面对类似问题时能不能稳定地表现一致。 |
| specialization | 专门化 | Adaptation toward a narrower domain or task. | 从通用能力变成更专门的能力。 |
| facts | 事实 | Information that should be correctly represented. | 应该与现实或正式资料一致的信息。 |
| knowledge | 知识 | Information used to answer or perform a task. | 系统回答问题时需要用到的内容。 |
| model knowledge | 模型知识 | Information encoded in or available to a model. | 模型内部已经学到或能使用的知识。 |
| learned knowledge | 学到的知识 | Information acquired during training. | 模型通过训练学会并保留下来的内容。 |
| document upload | 文档上传 | Providing a document to an application. | 把文件交给应用读取或参考。 |
| uploading documents | 上传文档 | Sending documents into an application or workflow. | 把文件上传给系统。 |
| file | 文件 | A stored unit of information that may be supplied to a system. | 保存资料的一份文件。 |
| training document | 训练文档 | A document whose contents may be used to create training examples. | 可以整理成训练例子的文件。 |
| training example from a document | 从文档生成的训练示例 | An example created from document content for training. | 从文件内容整理出来、用于训练模型的例子。 |
| more context | 更多上下文 | Supplying more information in the current request. | 这次提问时给模型更多参考内容。 |
| context window | 上下文窗口 | The amount of input context a model can process at once. | 模型一次能看到的输入内容容量。 |
| learned behavior vs visible context | 学到的行为与可见上下文 | The difference between changing the model and changing what it can see. | 一个改模型本身，一个只改这次给模型看的资料。 |
| information availability | 信息可用性 | What information is available to the model for a request. | 模型在这次回答时到底拿得到哪些资料。 |
| model parameters vs context | 模型参数与上下文 | Internal learned values versus runtime supplied information. | 参数是模型内部学到的数字，上下文是临时给它看的内容。 |
| current policy retrieval | 当前政策检索 | Retrieving the latest policy for a response. | 回答前先查最新政策。 |
| policy-grounded answer | 基于政策的回答 | An answer grounded in supplied policy information. | 有政策资料作为依据的回答。 |
| grounding | 基于依据；接地 | Constraining a response with relevant external information. | 让回答有明确资料依据，不只靠模型猜。 |
| factual grounding | 事实依据约束 | Using factual source material to guide an answer. | 用事实资料约束回答内容。 |
| hallucination risk | 幻觉风险 | The risk that a generated answer invents or distorts facts. | 模型把不存在的内容说成真的风险。 |
| stale information | 过时信息 | Information that is no longer current. | 已经更新过、现在不再准确的资料。 |
| source freshness | 来源新鲜度 | How current the retrieved source is. | 被检索资料有多新。 |
| retrieval quality | 检索质量 | How well retrieval finds useful and relevant information. | 查到的资料是否真的相关、完整。 |
| answer quality | 回答质量 | How correct, useful, and clear an answer is. | 回答是否正确、有用、容易理解。 |
| accuracy | 准确性 | How often an answer matches the correct information. | 回答和正确事实相符的程度。 |
| relevance | 相关性 | How closely retrieved information or an answer matches the task. | 资料或回答和问题有多相关。 |
| consistency | 一致性 | How reliably similar inputs receive suitable behavior. | 类似问题能不能稳定得到合适回答。 |
| latency | 延迟 | The time between a request and a response. | 从提问到收到回答要等多久。 |
| cost | 成本 | The resources or money needed to run or train a method. | 使用、训练或维护这种方案要花多少资源。 |
| compute | 计算资源 | Hardware computation needed for training or inference. | 训练和运行模型所需要的计算能力。 |
| maintainability | 可维护性 | How easily information, prompts, or models can be updated. | 以后修改和维护方案是否方便。 |
| evaluation | 评估 | Testing how well a method performs. | 用测试判断方法效果好不好。 |
| test set | 测试集 | A set of cases used to measure final performance. | 专门用来检查模型效果的一批题目。 |
| evaluation example | 评估示例 | A case used to compare method performance. | 用来比较提示、RAG、微调效果的例子。 |
| failure case | 失败案例 | A case where the system gives an inadequate result. | 系统没有正确完成任务的例子。 |
| limitation | 局限 | A condition where a method may not work well. | 某种方法不适合或效果有限的地方。 |
| trade-off | 权衡 | A choice where improving one aspect may affect another. | 得到某个好处时可能要牺牲另一个方面。 |
| primary method | 主要方法 | The main method chosen to solve a problem. | 当前最主要、最先采用的方案。 |
| direct method | 直接方法 | A method that addresses the task without an intermediate mechanism. | 不额外增加复杂机制、直接解决问题的方法。 |
| adaptation method | 适配方法 | A method used to make a model fit a task. | 让模型适应任务的办法。 |
| training-and-runtime distinction | 训练与运行时区分 | The difference between changing a model during training and guiding it during use. | 一个发生在训练阶段，一个发生在实际使用时。 |
| Prompting vs RAG | 提示与 RAG 的区别 | Prompting gives instructions; RAG supplies information. | 提示是告诉模型怎么做，RAG 是给模型资料。 |
| RAG vs Fine-tuning | RAG 与微调的区别 | RAG changes runtime context; fine-tuning changes parameters through training. | RAG 临时补资料，微调改变模型内部能力。 |
| Prompting vs Fine-tuning | 提示与微调的区别 | Prompting is runtime instruction; fine-tuning is training-based adaptation. | 提示只改这次要求，微调会训练模型本身。 |
| external knowledge vs learned behavior | 外部知识与学习行为 | Retrieved facts are different from behavior learned in parameters. | 查到的事实和模型训练出来的行为不是一回事。 |
| context vs parameters | 上下文与参数 | Runtime-visible information is different from internal learned values. | 当前看到的资料和模型内部数字不同。 |
| retrieval vs training | 检索与训练 | Retrieval finds information; training changes model parameters. | 检索是查资料，训练是改模型。 |
| prompt vs fine-tuning | 提示与微调 | A prompt changes the request; fine-tuning changes learned behavior. | 提示改问题，微调改模型学到的行为。 |
| RAG is not training | RAG 不是训练 | RAG retrieves information without updating model parameters. | RAG 查资料，不会因此重新训练模型。 |
| prompting is not fine-tuning | 提示不是微调 | Prompting changes a request, not the trained parameters. | 写提示词不会自动改变模型内部参数。 |
| fine-tuning is not document upload | 微调不是上传文档 | Uploading a file alone does not perform additional training. | 把文件传上去不等于已经微调模型。 |
| more context is not fine-tuning | 更多上下文不是微调 | More visible input does not change what the model has learned. | 给更多资料只改变当前输入，不会改模型所学内容。 |
| runtime knowledge injection | 运行时知识注入 | Adding external knowledge while a request is processed. | 用户提问时把外部知识临时放进请求。 |
| parameter-level adaptation | 参数级适配 | Adapting the model by changing internal parameters. | 通过改模型内部参数来适配任务。 |
| instruction following | 指令遵循 | The ability to carry out supplied instructions. | 模型按照要求做事的能力。 |
| instruction hierarchy | 指令层级 | The ordering of system and user instructions. | 系统规则和用户要求之间的优先顺序。 |
| prompt design | 提示设计 | Designing instructions to obtain useful model behavior. | 设计更有效的提示词。 |
| prompt engineering | 提示工程 | Systematic design and testing of prompts. | 有方法地设计、测试和改进提示词。 |
| retrieval pipeline | 检索流水线 | The sequence that searches, selects, and supplies context. | 从查资料到把资料交给模型的一整套流程。 |
| fine-tuning pipeline | 微调流水线 | The sequence that prepares examples, trains, and evaluates a model. | 准备训练数据、训练模型、再检查效果的一整套流程。 |
| application pipeline | 应用流水线 | The end-to-end flow from request to answer in an application. | 用户提问到系统回答的完整处理流程。 |
| source selection | 来源选择 | Choosing which external source should provide context. | 决定从哪个文件或资料库找依据。 |
| context assembly | 上下文组装 | Combining retrieved material into the model request. | 把查到的几段资料整理进模型输入。 |
| answer generation | 答案生成 | Producing the final answer from instructions and context. | 模型根据要求和资料写出最终回答。 |
| response validation | 响应校验 | Checking whether a response is correct and appropriate. | 检查回答是否正确、合适、能使用。 |
| policy compliance | 政策合规 | Following the applicable policy rules. | 回答符合公司或产品规定。 |
| source citation | 来源引用 | Pointing to the source supporting an answer. | 在回答中说明依据来自哪里。 |
| grounded generation | 有依据的生成 | Generating content with relevant supplied evidence. | 根据相关资料生成，而不是完全凭模型记忆。 |
| factual update | 事实更新 | Updating the information used for current answers. | 换成最新事实，让回答跟上变化。 |
| behavior update | 行为更新 | Updating how the model responds or acts. | 改变模型回答问题的方式。 |
| request-time change | 请求时变化 | A change applied only while processing one request. | 只对当前这次请求生效的变化。 |
| persistent change | 持久变化 | A change that remains in the model or system after the request. | 这次使用后仍然保留下来的改变。 |
| ephemeral context | 临时上下文 | Context supplied for a limited request or session. | 只在当前请求或会话里暂时可见的资料。 |
| durable model behavior | 持久模型行为 | Behavior that remains after model adaptation. | 微调后能在后续请求中持续表现的行为。 |
| model memory | 模型记忆 | Information or behavior represented inside model parameters. | 模型内部保存的知识或行为倾向。 |
| external memory | 外部记忆 | Information stored outside the model and retrieved when needed. | 放在模型外部、需要时再查的资料。 |
| factual knowledge update | 事实知识更新 | Updating current facts through external sources. | 用外部资料更新模型回答所需的事实。 |
| behavior specialization | 行为专门化 | Making responses more consistent for a specialized use. | 让模型在特定用途上表现得更稳定。 |
| application context | 应用上下文 | The business or product information surrounding a request. | 当前业务或产品场景提供的背景资料。 |
| domain-specific behavior | 领域特定行为 | Behavior adapted for a specialized domain. | 针对某个行业表现出的专门行为。 |
| policy-grounded generation | 基于政策的生成 | Generating answers using policy material as grounding context. | 依据政策资料生成答案。 |
| model parameter training | 模型参数训练 | Learning parameter values from training examples. | 用例子把模型内部参数训练出来。 |
| task-specific training | 任务特定训练 | Additional training for a particular task. | 针对某个具体任务继续训练模型。 |
| adaptation stack | 适配栈 | The combined layers used to adapt a model. | 提示、RAG、微调等共同组成的适配层次。 |
| system design | 系统设计 | Deciding how model, instructions, context, and training fit together. | 设计这些组件怎样组合完成任务。 |
| operational choice | 运营选择 | A practical choice of method for a running system. | 在真实系统里选择哪种方案来落地。 |
| use case | 使用场景 | A concrete situation where a method is applied. | 某种方法实际被使用的场景。 |
| decision guide | 决策指南 | Guidance for choosing among methods. | 帮助判断该用哪种方法的说明。 |
| decision point | 决策点 | A question in a flow where the next method is chosen. | 决策流程中需要做选择的地方。 |
| if better instruction is enough | 如果更好指令就足够 | A condition that points to prompting. | 只需把要求说清楚就选提示。 |
| if external/current information is needed | 如果需要外部／当前信息 | A condition that points to RAG. | 需要最新或私有资料就考虑 RAG。 |
| if learned behavior needs adaptation | 如果需要适配学习行为 | A condition that points to fine-tuning. | 需要改变模型稳定行为就考虑微调。 |
| still not enough | 仍然不够 | A condition where an earlier method did not solve the task. | 前一种办法用了以后效果还不够。 |
| model behavior, task rules, current facts | 模型行为、任务规则、当前事实 | Three different concerns handled by fine-tuning, prompting, and RAG. | 分别对应模型怎么答、这次怎么做、现在事实是什么。 |
| what changes | 改变了什么 | The part of the system affected by a method. | 判断一种方法到底改了系统哪一部分。 |
| instructions / context / parameters | 指令／上下文／参数 | The three main targets changed by prompting, RAG, and fine-tuning. | 三种方法分别改要求、资料可见范围和模型内部数字。 |
| training versus runtime | 训练阶段与运行阶段 | A distinction between adaptation before use and guidance during use. | 训练是使用前改变模型，运行时是使用中临时引导。 |
| latest | 最新的 | Most up-to-date among available versions. | 目前时间点上最新的版本。 |
| private | 私有的 | Restricted rather than publicly available. | 只有组织或授权用户可以访问的。 |
| specialized | 专门的 | Designed for a narrower area or task. | 针对某个范围，而不是通用所有事情。 |
| current | 当前的 | Valid at the present time. | 现在仍然有效的。 |
| learned | 学到的 | Acquired through training or examples. | 模型通过训练例子得到的。 |
| supplied | 已提供的 | Made available as part of the request or system. | 已经交给模型、可以被它使用的。 |
| external | 外部的 | Coming from outside the model itself. | 来源在模型之外的。 |
| additional | 额外的 | Added after the initial setup or training. | 在原有基础上另外增加的。 |
| accurate | 准确的 | Correct and matching the relevant facts. | 和正确事实一致的。 |
| latest policy | 最新政策 | The most recently valid policy version. | 最新一版正式政策。 |
| current product information | 当前产品信息 | Product facts that are valid now. | 现在产品实际采用的信息。 |
| learned behavior | 学习行为 | Behavior acquired through model training. | 模型训练后形成的行为。 |
| model parameters | 模型参数 | Internal learned values that define model behavior. | 影响模型表现的一大批内部数字。 |
| context available to the model | 模型可用上下文 | Information the model can see for the current request. | 当前问题中模型能看到的资料。 |
| answer source | 回答来源 | The material from which answer facts are taken. | 回答内容依据的资料来源。 |
| response rule | 回答规则 | A rule constraining how a response should be produced. | 规定回答应该怎样写、哪些内容能说的规则。 |
| policy source | 政策来源 | The authoritative policy material used for an answer. | 提供正式政策内容的来源。 |
| model training examples | 模型训练例子 | Examples used to teach model behavior. | 用来训练模型回答方式的一组例子。 |

## Potential Missing Concepts

- **prompt template（提示模板）**：正文讲 system/user prompt，但没有说明如何把固定结构做成可复用模板。
- **prompt engineering（提示工程）**：正文使用 prompting 和 instructions，但没有单独解释系统化设计、测试和迭代提示的方法。
- **system prompt hierarchy（系统提示层级）**：正文把 system/user prompt 并列展示，但没有说明不同指令来源的优先级。
- **retriever（检索器）**：正文写 retrieve / retrieval，但没有说明负责查找候选资料的组件。
- **retrieval index（检索索引）**：正文说 RAG retrieves information，但没有解释资料如何被索引以便查找。
- **chunking（分块）**：正文提到文档和外部信息，但没有说明长文档通常要先切成片段。
- **reranking（重排序）**：正文没有解释如何从检索候选中再次挑选最相关内容。
- **vector search（向量搜索）**：正文没有说明 RAG 可能用向量相似度寻找相关内容。
- **keyword search（关键词搜索）**：正文没有区分关键词检索与语义检索。
- **semantic search（语义搜索）**：正文讲相关信息，但没有定义按含义而非只按字面查找。
- **embedding（嵌入）**：正文没有解释文字或文档如何转换成可比较的向量表示。
- **vector database（向量数据库）**：正文提到外部资料，但没有讲保存可检索向量的数据库。
- **retrieval precision / recall（检索精确率／召回率）**：正文有“相关信息”概念，但没有具体检索质量指标。
- **context recall（上下文召回）**：没有说明回答所需信息是否被检索到。
- **context precision（上下文精确度）**：没有说明加入的上下文中有多少真正相关。
- **groundedness（有据程度）**：正文暗示只能使用政策信息，但没有定义回答与来源的对应程度。
- **citation correctness（引用正确性）**：正文没有说明引用是否真的支持回答。
- **source attribution（来源归因）**：没有解释如何把回答中的主张归因到具体来源。
- **fine-tuning dataset（微调数据集）**：正文说 many examples，但没有说明数据集的组织和质量要求。
- **instruction tuning（指令微调）**：正文讲 desired behavior，但没有区分用指令—回答样本进行的微调。
- **supervised fine-tuning / SFT（监督微调）**：正文没有说明带有目标回答的微调形式。
- **pre-training（预训练）**：正文未展开基础模型在适配前如何获得通用能力。
- **preference optimization（偏好优化）**：正文提到行为和风格，但没有介绍偏好数据如何改变模型。
- **RLHF（基于人类反馈的强化学习）**：正文没有涉及用人类偏好优化回答行为。
- **DPO（直接偏好优化）**：正文没有介绍另一种偏好对齐方法。
- **adapter / LoRA（适配器／低秩适配）**：正文说改变参数，但没有说明低成本参数高效微调方法。
- **parameter-efficient fine-tuning / PEFT（参数高效微调）**：没有区分更新全部参数和只更新一小部分参数。
- **catastrophic forgetting（灾难性遗忘）**：没有讨论微调可能损害原有通用能力。
- **overfitting（过拟合）**：没有讨论模型过度记住训练示例的问题。
- **generalization（泛化）**：正文讲许多示例和新请求，但没有定义对未见场景的适应能力。
- **data leakage（数据泄漏）**：没有讨论训练或检索资料意外泄漏到不应看到的地方。
- **privacy（隐私）**：正文提到 private information，但没有展开数据保护和访问控制。
- **security（安全）**：正文的 safety 不是完整的系统安全定义。
- **prompt injection（提示注入）**：RAG 外部内容可能包含恶意指令，但正文没有讨论这个风险。
- **indirect prompt injection（间接提示注入）**：没有讨论被检索文档中的指令影响模型的情况。
- **access control（访问控制）**：正文说 private information，但没有说明谁可以检索什么。
- **authorization（授权）**：没有解释系统如何判断用户是否有权读取政策或文件。
- **freshness（新鲜度）**：正文使用 latest / current，但没有定义资料更新速度或过期规则。
- **versioning（版本管理）**：没有说明如何区分不同版本的政策和模型。
- **source of truth（事实源）**：没有指出哪一个政策来源具有最终权威性。
- **conflict resolution（冲突解决）**：没有讨论多个检索来源互相矛盾时怎么处理。
- **abstention（拒答／弃答）**：没有解释资料不足时模型应如何说“无法确定”。
- **uncertainty（不确定性）**：正文只有准确性和“still not enough”语境，没有具体不确定性机制。
- **confidence score（置信度分数）**：没有说明系统如何表达对答案的信心。
- **hallucination（幻觉）**：正文没有直接命名模型编造事实的风险。
- **factuality（事实性）**：没有把“准确回答政策”转成可测量的事实性指标。
- **faithfulness（忠实性）**：没有定义回答是否忠实于检索到的上下文。
- **answer quality metric（回答质量指标）**：正文没有列出准确率、相关性、完整性等具体指标。
- **latency（延迟）**：正文未讨论检索和生成带来的等待时间。
- **throughput（吞吐量）**：正文未讨论系统单位时间可处理多少请求。
- **token budget（Token 预算）**：正文未讨论提示和 RAG 上下文的长度限制。
- **context window（上下文窗口）**：正文说 context，但没有讲模型一次可处理的上下文容量。
- **cost（成本）**：正文没有比较提示、检索与微调的运行和训练成本。
- **compute（计算资源）**：正文没有讨论训练与推理需要的硬件资源。
- **deployment（部署）**：正文讲 AI application，但没有说明模型和检索流程如何上线。
- **monitoring（监控）**：正文没有说明上线后如何观察质量、延迟和检索失败。
- **observability（可观测性）**：没有定义如何记录提示、检索、模型输出和失败原因。
- **feedback loop（反馈闭环）**：正文没有说明错误回答如何反馈到提示、知识库或训练数据。
- **human-in-the-loop（人在回路中）**：正文未展开人工审核或升级机制。
- **human approval（人工批准）**：没有说明哪些政策回答或动作必须由人确认。
- **evaluation set（评估集）**：正文只有 comparison / good for，没有介绍标准化评估集。
- **A/B test（A/B 测试）**：没有说明如何比较不同 prompt、RAG 配置或微调模型。
- **baseline（基线）**：没有说明与未适配基础模型进行对比。
- **regression test（回归测试）**：没有讨论更新提示、资料或模型后如何确保旧能力不退化。
- **production quality（生产质量）**：没有说明从演示效果到上线可靠性的差异。
- **guardrail（护栏）**：正文提到 task rules，但没有展开限制模型行为的安全规则。
- **structured output（结构化输出）**：正文讲回答格式，但没有定义 schema 或可解析输出。
- **tool calling（工具调用）**：正文没有讨论模型调用检索器或其他外部工具的机制。
- **agent workflow（智能体工作流）**：正文把方法放在 AI application 中，但没有展开多步骤循环。
- **prompt caching（提示缓存）**：没有讨论重复提示内容的缓存和成本优化。
- **knowledge cutoff（知识截止时间）**：正文讲 current information，但没有说明基础模型知识的时间边界。
- **model version（模型版本）**：没有说明不同基础模型或微调版本的差异。
- **policy version（政策版本）**：没有说明 RAG 应该检索哪个生效版本。

## Aliases / Synonyms

- Prompting ↔ prompting ↔ prompt-based guidance ↔ instruction-based guidance ↔ runtime instruction
- Prompt ↔ prompt text ↔ user prompt ↔ task instruction ↔ request（prompt 是 input 的一种形式，不是所有 input 都是 prompt）
- System prompt ↔ system instruction ↔ system-level guidance
- User prompt ↔ user instruction ↔ user request
- RAG ↔ Retrieval-Augmented Generation ↔ retrieval-augmented generation ↔ retrieval-grounded generation
- Retrieval ↔ retrieve ↔ information retrieval ↔ knowledge retrieval ↔ lookup
- Retrieved information ↔ retrieved context ↔ external context ↔ RAG context
- Context ↔ available context ↔ runtime context ↔ model-visible information
- External knowledge ↔ external information ↔ supplied knowledge ↔ retrieved knowledge
- Current information ↔ current facts ↔ latest information ↔ up-to-date information
- Private information ↔ private knowledge ↔ organization-specific information
- Fine-tuning ↔ fine-tune ↔ additional training ↔ task-specific training ↔ model adaptation（adaptation 还可能包括 prompting 或 retrieval）
- Fine-tuned model ↔ adapted model ↔ task-adapted model
- Training ↔ model training ↔ additional training ↔ training phase
- Training examples ↔ fine-tuning examples ↔ behavior examples ↔ instruction examples
- Desired behavior ↔ target behavior ↔ intended behavior ↔ response behavior
- Learned behavior ↔ trained behavior ↔ model behavior encoded by training
- Specialized behavior ↔ task-specific behavior ↔ domain-specific behavior
- Model parameters ↔ parameters ↔ learned parameters ↔ learned values（learned values 可能比 parameters 更宽泛）
- Parameter update ↔ parameter change ↔ model update（model update 也可能包括非参数变化）
- Base model ↔ foundation model ↔ pretrained model ↔ general-purpose model（foundation model 与 base model 在不同语境下不完全等价）
- Model capability ↔ model ability ↔ capability
- Application ↔ AI application ↔ AI product feature ↔ product workflow
- AI system ↔ model-plus-application system ↔ AI application system
- Response ↔ answer ↔ generated answer ↔ generated response ↔ output（response 是 output 的一种形式）
- Generation ↔ answer generation ↔ response generation ↔ content generation
- Inference ↔ runtime computation ↔ serving-time computation ↔ prediction time
- Decision flow ↔ decision guide ↔ selection flow ↔ decision process
- Combination ↔ combined approach ↔ hybrid approach ↔ adaptation stack
- Prompt engineering ↔ prompt design ↔ systematic prompt design
- Retrieval pipeline ↔ retrieval workflow ↔ search-and-context pipeline
- Fine-tuning pipeline ↔ training pipeline ↔ adaptation pipeline
- Grounding ↔ factual grounding ↔ grounded generation ↔ policy-grounded generation
- Answer quality ↔ response quality ↔ output quality
- Accuracy ↔ factual accuracy ↔ correctness
- Relevance ↔ task relevance ↔ contextual relevance
- Current product policies ↔ current policy information ↔ latest product rules
- Employee leave policy ↔ HR leave policy ↔ employee leave-policy information
- Document upload ↔ uploading documents ↔ file upload（上传文件不等于 fine-tuning）
- More context ↔ additional context ↔ expanded input context（more context 不等于 fine-tuning）
- Model parameters vs context ↔ learned values vs runtime information
- Prompting vs RAG ↔ instructions vs context
- RAG vs Fine-tuning ↔ runtime context change vs parameter change
- Prompting vs Fine-tuning ↔ runtime instruction vs training-based adaptation
- RAG is not training ↔ retrieval is not parameter update
- Prompting is not fine-tuning ↔ prompt change is not model change
- Fine-tuning is not document upload ↔ uploading a file is not additional training

## Do Not Confuse Candidates

- **Prompting vs RAG**：Prompting changes instructions; RAG supplies additional external context. 提示主要告诉模型怎么做，RAG 主要给模型资料。
- **RAG vs fine-tuning**：RAG changes the context available at runtime; fine-tuning changes model parameters through training. RAG 是临时补上下文，微调是训练改变模型。
- **Prompting vs fine-tuning**：Prompting changes the request; fine-tuning changes learned behavior. 写提示词不会自动改模型内部参数。
- **RAG vs training**：RAG retrieves information while a request is handled; it does not update model parameters. 查资料不等于训练模型。
- **Prompting vs input**：A prompt is one kind of input, but input can also be a document, policy, image, or other material. 提示只是输入的一种形式。
- **Prompting vs source material**：Prompting is the instruction method; source material is information supplied for reference. 指令和参考资料不是一回事。
- **Context vs parameters**：Context is visible for a request; parameters are learned values inside the model. 当前可见资料和模型内部数字不同。
- **More context vs fine-tuning**：More context changes what the model can see now; fine-tuning changes what it has learned. 给更多资料不会让模型重新学习。
- **External knowledge vs learned behavior**：RAG can add current facts without changing learned behavior; fine-tuning changes learned behavior without being a direct live knowledge lookup. 外部事实和行为适配是两条不同路径。
- **Current facts vs specialized behavior**：Current facts are often a RAG problem; specialized stable behavior may be a fine-tuning problem. 最新政策和固定回答方式不一定用同一方案。
- **Latest policy vs model parameters**：A latest policy document can be retrieved at runtime; it does not need to be stored in model parameters. 最新政策不必靠重新训练写进模型。
- **Document upload vs fine-tuning**：Uploading a document alone is not additional training. 上传文件可能只是临时上下文，也可能供检索使用。
- **Training examples vs retrieved documents**：Training examples change model behavior during training; retrieved documents supply information during runtime. 训练样例和检索文件作用不同。
- **System prompt vs user prompt**：Both are prompts, but they can represent different instruction sources and priorities. 系统提示和用户提示都叫 prompt，但来源和优先级可能不同。
- **System prompt vs fine-tuning**：A system prompt can guide each request without updating parameters; fine-tuning persists behavior in the adapted model. 系统提示是运行时指导，微调是模型本身的持久适配。
- **RAG context vs source of truth**：RAG context is the material retrieved for a request; source of truth is the authoritative origin that should be trusted. 检索到的上下文不自动等于权威来源。
- **Retrieval vs generation**：Retrieval finds existing information; generation produces a response. 检索是找已有资料，生成是写出回答。
- **Retrieval quality vs answer quality**：A system can retrieve relevant documents but still generate a poor answer, or generate a fluent answer from poor retrieval. 查得准不等于答得好。
- **Accuracy vs consistency**：Accuracy is correctness; consistency is stable behavior across cases. 每次写法一致不代表内容一定正确。
- **Current information vs accurate information**：Information can be current but wrong, or accurate historically but stale now. 最新不自动等于正确，正确也不一定仍然适用。
- **Private information vs secure system**：Private data is restricted information; security includes controls that protect it. 有私有资料不代表系统已经安全。
- **Specialized behavior vs specialized knowledge**：Fine-tuning can shape behavior or style; it is not automatically the best way to inject frequently changing knowledge. 专门的回答方式和专门的事实资料不是一回事。
- **Base model vs finished product**：A base model is a starting point; a product also includes prompts, data, retrieval, interface, rules, and operations. 基础模型不是完整产品。
- **Foundation model vs fine-tuned model**：A foundation model is broadly trained; a fine-tuned model has received task-specific additional training. 基础模型可以是起点，微调模型是适配后的版本。
- **Model vs AI application**：A model produces or transforms outputs; an application combines the model with workflows and user-facing behavior. 模型和用户真正使用的应用不是同一个层次。
- **Model behavior vs application behavior**：The model may have learned response tendencies, while the application can add prompts, retrieval, validation, and policy rules. 应用整体表现不只由模型决定。
- **Runtime vs training time**：Runtime is when requests are handled; training time is when parameters are learned or updated. 运行时是实际回答，训练时是学习和调整模型。
- **Persistent change vs request-time change**：Fine-tuning is generally persistent; a prompt or retrieved context may only affect one request or session. 微调改变能保留，提示和上下文可能只临时生效。
- **Policy information vs policy compliance**：Having policy text in context does not guarantee the answer follows it. 给了政策资料不代表回答一定合规。
- **Prompting vs prompt engineering**：Prompting is the broad act of using instructions; prompt engineering emphasizes systematic design and testing. 使用提示和系统化设计提示的范围不同。
- **RAG vs search engine**：RAG is an application pattern that uses retrieval to ground generation; a search engine primarily returns or ranks existing results. RAG 往往还包含生成回答，不只是列搜索结果。
- **Fine-tuning vs pre-training**：Fine-tuning is additional narrower training after a base capability exists; pre-training creates broad initial capability. 微调不是从零开始的广泛预训练。
- **Fine-tuning vs instruction tuning**：Fine-tuning is the broad category; instruction tuning is one kind using instruction-response examples. 指令微调是微调的一种。
- **Parameters vs hyperparameters**：Parameters are learned by training; hyperparameters are usually chosen before or around training. 参数和超参数不是同一类数字。
- **Model update vs knowledge update**：A model update changes the model; a knowledge update may only change the external documents retrieved by RAG. 更新模型和更新知识库不一定是同一件事。
- **Current product policies vs task rules**：Product policies are external facts or rules; task rules are runtime instructions about what to do. 产品政策和本次任务要求可同时存在。
- **Response behavior vs response content**：Behavior concerns how the model responds; content concerns the facts or words in a particular response. 回答方式和某次回答具体说了什么不同。
- **Good for changing facts vs good for behavior/style**：RAG is presented as strong for changing facts; prompting and fine-tuning are stronger for behavior or style. 事实变化和行为风格适合的方案不同。
- **No training vs no model change**：Prompting and RAG do not require additional training, but RAG can still change the model’s current output by changing context. 不训练不代表输出不会变化。
- **No parameter change vs no effect**：Prompting and RAG do not change parameters, but they can materially change a response. 不改参数也能明显改变当前回答。
- **Current context vs learned knowledge**：Current context is supplied now; learned knowledge is represented in the trained model. 临时资料和模型长期学到的内容不同。
- **RAG context vs prompt**：RAG context is retrieved information; a prompt is instruction or input framing. 实际系统中二者可一起放进同一个请求，但作用不同。
- **Prompting vs application logic**：A prompt is one control mechanism; application code may separately enforce retrieval, validation, routing, and permissions. 提示不是整个应用的逻辑。
- **Fine-tuning vs guardrails**：Fine-tuning shapes tendencies; guardrails can enforce external constraints at the application layer. 微调不能替代所有安全规则。
- **Fine-tuning vs evaluation**：Fine-tuning changes the model; evaluation measures the result. 训练和评估分别是改变和检查。
- **RAG vs evaluation**：RAG is a solution mechanism; retrieval and answer evaluation are checks of whether it works. RAG 不是评估指标。
- **Accurate answer vs cited answer**：A citation can support an answer, but citation presence alone does not guarantee correctness. 有引用不代表一定答对。
- **Supplied policy information vs authoritative policy**：Supplied material may be incomplete or stale; authoritative policy is the approved source. 被提供的资料不一定就是最终权威版本。
- **Employee leave-policy question vs general question**：The shared example is a domain-specific use case, not a definition of RAG or fine-tuning. 休假政策只是示例场景，不是方法本身。

## Notes

- 本文件是 Module 04 的 raw glossary 收集稿，目标是最大化保留页面正文中的候选术语、机制、流程节点、对比标准、缩写、别名和易混淆概念；不做去重、归并或最终取舍。
- 已完整覆盖页面的导语、On this page 导航、The Big Idea、One shared example、Side-by-side comparison、When to use each、Decision flow、How they work together、Key distinctions、What it is NOT 和 Remember this。
- 页面核心三分法是：Prompting changes instructions；RAG adds external context；fine-tuning changes model parameters through additional training。
- 页面明确区分了两个维度：Prompting 和 RAG 在 runtime 工作，fine-tuning 发生在 training；Prompting/RAG 不需要额外 training，fine-tuning 需要 training。
- 页面共享示例是“Answer employee leave-policy questions accurately.”，对应的三种方法分别是清晰指令、检索最新 HR policy、用许多期望行为示例训练。
- 页面正文使用了“latest HR policy”“external / current information”“private or frequently changing information”等表达，因此 current、latest、private、changing facts、external knowledge 都被单独保留。
- 页面把 fine-tuning 的改变写成“model parameters / learned behavior”，raw 阶段同时保留 parameters、learned behavior、specialized behavior、response behavior 等可能重叠但语义角度不同的候选。
- 页面把 RAG 的改变写成“available context”，raw 阶段同时保留 context、available context、external context、retrieved context、RAG context。
- 页面“可组合”示例是：fine-tuned model 提供 response behavior；system/user prompt 提供 task rules；RAG context 提供 current product policies；三者共同组成 AI application。
- 页面决策流顺序是：如果 better instruction 足够，选 Prompting；如果需要 external/current information，选 RAG；如果 learned behavior 仍需 adaptation，选 Fine-tuning；页面同时说明真实系统 may combine all three。
- 页面比较维度包括 changes instructions、adds external knowledge、changes model parameters、works at runtime、requires training、good for changing facts、good for behavior/style；这些比较短语也作为候选保留。
- 页面四个 “What it is NOT” 边界是：RAG ≠ Training；Prompting ≠ Fine-tuning；Fine-tuning ≠ Uploading documents；More context ≠ Fine-tuning。
- 页面没有列出具体数值指标；accuracy、relevance、consistency、latency、cost 等条目是从正文任务目标和方法选择维度延伸出的潜在后续词表候选，已与正文直接术语一起保留。
- 页面没有展开 retriever、chunking、embedding、vector database、reranking、SFT、LoRA、prompt injection 等实现或风险概念；它们已放入 Potential Missing Concepts，避免把相邻概念误当成页面明确定义。
- raw 阶段保留重复词条，例如 response behavior、task rules、current product policies、model parameters、learned behavior，因为同一词在不同模块位置承担不同上下文角色。
- “RAG”是正文明确出现的缩写；“AI”来自 AI application；system/user prompt 是页面明确的组合表达。其他缩写如 SFT、PEFT、RLHF、DPO、LLM 属于潜在缺失或相邻概念，不伪装成页面直接定义。
- 页面没有把 RAG 限定为某一种数据库或搜索实现，因此 raw 术语只把 retrieval、context、external information 作为直接候选；vector search、keyword search 等具体实现放在 Potential Missing Concepts。
- 中文翻译在 raw 阶段以便于小白理解为主；例如 prompt 同时保留“提示词／提示”，fine-tuning 同时保留“微调”，context 同时保留“上下文”，后续整理阶段再统一术语规范。
