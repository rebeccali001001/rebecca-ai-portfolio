# Instruction Tuning

## Module/Topic/Source File

- Module: 04 · Training & Model Adaptation
- Topic: Instruction Tuning
- Source File: `instruction-tuning.html`

## Glossary Candidates

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Instruction Tuning | 指令调优；指令微调 | Additional training that teaches a model to respond to instructions. | 用额外训练让模型更会按要求做事。 |
| instruction tuning | 指令调优；指令微调 | The same concept written in lowercase. | 指令调优这个术语的小写写法。 |
| Instruction-tuned model | 经过指令调优的模型 | A model trained to follow instructions more reliably. | 已经练过“按要求回答”的模型。 |
| instruction-tuned model | 经过指令调优的模型 | The lowercase form of the adapted model name. | 经过指令调优的模型的小写写法。 |
| model | 模型 | A learned system that produces outputs from inputs. | 根据输入生成结果的程序或系统。 |
| pre-trained model | 预训练模型 | A model that already learned language and general patterns. | 先学过语言和一般规律、再继续训练的模型。 |
| Pre-training | 预训练 | Broad initial learning before task-focused adaptation. | 让模型先广泛学习基础知识和语言能力。 |
| pre-training | 预训练 | The lowercase form of the initial training stage. | 预训练这个阶段的小写写法。 |
| additional training | 额外训练 | Training performed after an earlier training stage. | 在原有训练之后继续训练。 |
| training | 训练 | Adjusting a model using examples so it learns patterns. | 用例子调整模型，让它学会规律。 |
| additional training focused on following instructions | 以遵循指令为重点的额外训练 | Extra training aimed at instruction-following behavior. | 专门练习“听懂要求并照做”的后续训练。 |
| language | 语言 | A communication system and the patterns a language model learns. | 模型学习和处理的人类语言。 |
| broad ability | 广泛能力 | General capability learned before specialization. | 模型在专门训练前已有的综合能力。 |
| general patterns | 一般规律；通用模式 | Broad regularities learned from data. | 从大量数据里学到的普遍规律。 |
| knowledge | 知识 | Information or understanding represented by a model. | 模型掌握的事实和理解能力。 |
| knowledgeable employee | 有知识的员工 | The employee in the page's analogy for a capable model. | 用来比喻已经掌握很多知识的模型。 |
| workplace request | 工作场景请求 | A request an employee is expected to follow. | 比喻用户给模型的工作任务要求。 |
| request | 请求 | An input asking a model or person to do something. | 希望模型完成的事情。 |
| user request | 用户请求 | A task or instruction supplied by a user. | 用户交给模型的要求或问题。 |
| instruction | 指令；说明 | A request that tells the model what to do. | 告诉模型任务内容和做法的话。 |
| instructions | 指令；说明（复数） | Multiple requests or directions for a model. | 多个任务要求或操作说明。 |
| following instructions | 遵循指令 | Doing what an instruction asks. | 按照要求完成任务。 |
| instruction following | 指令遵循 | The capability to carry out requested tasks. | 模型理解要求并照做的能力。 |
| follows user requests | 遵循用户请求 | Responds in line with what the user asked. | 回答符合用户真正想要的内容。 |
| follow requests more reliably | 更可靠地遵循请求 | Follows requests with fewer failures. | 更稳定、更少偏离要求地完成任务。 |
| desired response | 期望回答；目标响应 | The response that an example says the model should produce. | 训练示例中被认为正确、理想的回答。 |
| useful response | 有用的回答 | A response that helps complete the requested task. | 对用户有帮助、能解决问题的回答。 |
| response | 回答；响应 | The output given after an instruction. | 模型对请求给出的结果。 |
| responses | 回答；响应（复数） | Multiple outputs produced for requests. | 模型给出的多个回答。 |
| output | 输出 | Information produced by a model. | 模型最后生成的结果。 |
| training example | 训练示例 | One example used to teach a model. | 用来教模型的一条样例。 |
| training examples | 训练示例（复数） | A collection of examples used for training. | 用来训练模型的一批样例。 |
| example | 示例；例子 | A concrete input-output teaching case. | 一个具体的训练或说明例子。 |
| examples of instructions and useful responses | 指令与有用回答的示例 | Examples pairing requests with helpful outputs. | 把要求和好回答放在一起给模型学习。 |
| pair a request with a desired response | 将请求与期望回答配对 | Put an instruction and target answer together. | 每条要求都配一条理想答案。 |
| request-and-response pair | 请求—回答对 | A paired input and target output. | 一条问题或指令加上对应答案。 |
| instruction-response pair | 指令—响应对 | A training pair consisting of an instruction and response. | 一条指令和应有回答组成的训练单位。 |
| input | 输入 | The request supplied to the model. | 送进模型的文字或任务要求。 |
| target response | 目标响应 | The answer used as the desired training output. | 训练时希望模型学会生成的答案。 |
| data example | 数据样例 | A single training record. | 数据集里的一条记录。 |
| dataset | 数据集 | A collection of training examples. | 集中存放训练样例的数据。 |
| supervised example | 监督样例 | An example containing an input and expected answer. | 同时给出问题和参考答案的例子。 |
| supervised learning | 监督学习 | Learning from examples with expected outputs. | 给模型看题目和正确答案来学习。 |
| fine-tuning | 微调 | Further training that adapts an existing model. | 在已有模型上继续训练，使它适应目标任务。 |
| task-focused adaptation | 面向任务的适配 | Adapting a general model toward particular tasks. | 把通用模型调整到更适合某些任务。 |
| model adaptation | 模型适配；模型调整 | Changing a model to work better for a use case. | 让模型更适合特定用途的调整过程。 |
| adaptation approach | 适配方法 | A way to adapt a model after pre-training. | 预训练后改变模型用途或行为的一种方法。 |
| model behavior | 模型行为 | The patterns in how a model responds. | 模型面对不同输入时表现出的反应方式。 |
| behavior through training | 通过训练形成的行为 | Response behavior changed by training. | 训练改变模型回答问题的方式。 |
| internal parameters | 内部参数 | Learned values inside a model. | 模型内部决定输出的许多数值。 |
| parameters | 参数 | Learned numerical settings of a model. | 模型通过训练调整的内部数字。 |
| adjust parameters | 调整参数 | Change learned model values during training. | 训练时修改模型内部数值。 |
| changes model parameters | 改变模型参数 | Updates the model's learned numerical state. | 让模型本身的内部数值发生变化。 |
| favor better responses | 偏向更好的回答 | Make desirable outputs more likely. | 让模型更倾向于给出理想回答。 |
| learned patterns | 学到的模式 | Regularities acquired during training. | 模型训练后记住的任务规律。 |
| task shapes | 任务形状；任务形式 | Recurring structures of tasks and requests. | 不同任务通常采用的输入和输出形式。 |
| recognize task shapes | 识别任务形式 | Identify what kind of task a request represents. | 看出用户要模型做总结、分类等哪类工作。 |
| format | 格式 | The expected structure of an answer. | 回答需要采用的排版或数据结构。 |
| formats | 格式（复数） | Different expected answer structures. | 多种可能的回答结构。 |
| role | 角色 | A function or perspective assigned to a model. | 要模型扮演或遵守的身份和职责。 |
| roles | 角色（复数） | Different assigned functions or perspectives. | 不同的身份、职责或回答视角。 |
| task-following behavior | 任务遵循行为 | Behavior that carries out a requested task. | 模型按任务要求行动和回答的表现。 |
| runtime | 运行时 | The stage when a trained model is being used. | 模型训练完成后真正接收请求的阶段。 |
| at runtime | 在运行时 | During actual model use after training. | 用户实际使用模型的时候。 |
| unfamiliar instruction | 不熟悉的指令 | A new instruction not seen exactly during training. | 训练时没见过原句、但形式相近的新要求。 |
| new request | 新请求 | A request supplied after training. | 模型训练结束后遇到的新任务。 |
| apply learned patterns | 应用学到的模式 | Use learned behavior on a new input. | 把训练得到的规律用到新问题上。 |
| task-following capability | 任务遵循能力 | Ability to execute requested tasks. | 模型按任务要求完成工作的能力。 |
| generalization | 泛化 | Applying learned patterns to new inputs. | 没见过完全相同的问题也能处理。 |
| summarization | 摘要；总结 | Producing a shorter version of content. | 把长文章压缩成重点内容。 |
| summary | 摘要；总结 | A short version of a longer text. | 用较少文字概括原文重点。 |
| article | 文章 | A piece of written content to summarize. | 需要被总结的长篇文字。 |
| translation | 翻译 | Converting content from one language to another. | 把一种语言的内容转换成另一种语言。 |
| translate | 翻译 | Convert text into another language. | 将文字改写成另一种语言。 |
| French | 法语 | The target language in the page's translation example. | 页面示例中要翻译成的语言。 |
| classification | 分类 | Assigning an input to a category. | 判断一段内容属于哪个类别。 |
| classify | 分类 | Assign an item to a class. | 给输入内容贴上合适类别。 |
| support ticket | 客服工单；支持工单 | A customer-support issue to categorize. | 用户提交给客服、需要归类的问题单。 |
| Billing | 账单；计费 | The category in the support-ticket example. | 页面分类示例中的“账单/计费”类别。 |
| structured response | 结构化回答 | An output following a specified structure. | 按规定字段和结构返回的答案。 |
| structured output | 结构化输出 | Output organized into a predictable schema. | 按固定格式组织的模型结果。 |
| JSON | JSON；JavaScript 对象表示法 | A structured text format for data. | 机器容易读取的键值对数据格式。 |
| name | 名称；姓名字段 | A requested field in the JSON example. | 结构化输出中的名称字段。 |
| date | 日期字段 | A requested field in the JSON example. | 结构化输出中的日期字段。 |
| field | 字段 | A named value in structured data. | JSON 等数据中的一个信息栏位。 |
| schema | 数据模式；结构规范 | The expected fields and structure of output. | 规定输出有哪些字段、如何排列的规则。 |
| answer in this format | 按此格式回答 | Follow a specified response format. | 不只回答内容，还要按指定样式返回。 |
| return JSON with name and date | 返回包含 name 和 date 的 JSON | Produce JSON containing named fields. | 按要求返回带名称和日期字段的数据。 |
| response format | 回答格式 | The structure in which a response is returned. | 模型回答应遵守的结构。 |
| correct translation | 正确翻译 | A translation that accurately preserves meaning. | 意思准确、语言正确的译文。 |
| short useful summary | 简短有用的摘要 | A concise summary that preserves useful points. | 短但保留重点、真正有帮助的总结。 |
| task example | 任务示例 | A sample task used to demonstrate or train behavior. | 用来展示或训练某项任务的例子。 |
| Pre-training vs Instruction Tuning | 预训练与指令调优的区别 | Broad initial learning differs from instruction-focused additional training. | 预训练学基础，指令调优练按要求做事。 |
| Instruction Tuning vs Prompting | 指令调优与提示的区别 | Tuning changes parameters; prompting changes supplied instructions. | 指令调优改模型本身，提示词只改这次输入。 |
| Instruction Tuning vs RAG | 指令调优与 RAG 的区别 | Tuning changes behavior through training; RAG supplies external context during use. | 指令调优靠训练改变行为，RAG 在使用时补充外部资料。 |
| Prompting | 提示；提示词设计 | Changing the instructions supplied at runtime. | 临时修改给模型的输入要求。 |
| prompt | 提示词；提示 | Text supplied to guide a model at runtime. | 每次使用时发给模型的指令或问题。 |
| supplied instructions | 提供的指令 | Instructions passed into a model during use. | 实际运行时输入给模型的要求。 |
| RAG | 检索增强生成 | Supplying external context during model use. | 使用时先找外部资料，再让模型参考资料回答。 |
| Retrieval-Augmented Generation | 检索增强生成 | The expanded form of RAG. | RAG 的英文全称。 |
| external context | 外部上下文 | Information supplied from outside the model during use. | 模型运行时临时补充的外部信息。 |
| external information | 外部信息 | Information retrieved or supplied at runtime. | 不一定存进模型参数、使用时才提供的资料。 |
| during use | 使用期间；运行时 | While a model is responding to a request. | 用户实际调用模型的过程。 |
| training-time change | 训练时变化 | A change made while training the model. | 训练阶段对模型能力或参数做的改变。 |
| runtime change | 运行时变化 | A change made by altering the input at use time. | 不重新训练，只在调用时改变输入。 |
| model parameters vs prompt | 模型参数与提示词 | The distinction between learned state and supplied input. | 参数是模型学到的内部状态，提示词是临时输入。 |
| model behavior vs external context | 模型行为与外部上下文 | The distinction between learned behavior and runtime information. | 一个是模型怎么回答，一个是这次提供什么资料。 |
| Foundation Model | 基础模型 | A broad pretrained model used as a starting point. | 具备通用能力、可继续适配的预训练模型。 |
| foundation model | 基础模型 | The lowercase form of foundation model. | 基础模型这个术语的小写写法。 |
| Pre-training → Foundation Model → Instruction Tuning | 预训练→基础模型→指令调优 | The relationship shown in the page's concept map. | 先预训练得到基础模型，再做指令调优。 |
| model adaptation approach | 模型适配方法 | One way of adapting a pretrained model. | 改造预训练模型用途的一条路线。 |
| SFT | 监督式微调 | Common abbreviation for supervised fine-tuning, closely related to instruction tuning. | 用带参考答案的样例进行监督式微调的简称。 |
| Supervised Fine-Tuning | 监督式微调 | Fine-tuning on input and desired-output examples. | 用“指令+正确答案”继续训练模型。 |
| instruction dataset | 指令数据集 | A dataset of instructions paired with target responses. | 收集了任务要求和参考回答的数据集。 |
| instruction-following evaluation | 指令遵循评估 | Evaluation of whether a model follows requests. | 检查模型是否按要求完成任务。 |
| response quality | 回答质量 | How useful, correct, and format-compliant a response is. | 看回答是否正确、有用、符合格式。 |
| correctness | 正确性 | Whether an output is accurate. | 回答内容是否对。 |
| helpfulness | 有用性 | Whether an output helps the user. | 回答是否真正解决用户问题。 |
| format adherence | 格式遵循度 | Whether an output follows the requested format. | 回答是否遵守指定结构或格式。 |
| reliability | 可靠性 | How consistently a model follows requests. | 多次使用时能否稳定按要求完成。 |
| evaluation metric | 评估指标 | A measure used to assess model behavior. | 用来衡量模型表现好坏的标准。 |

## Potential Missing Concepts

- Supervised fine-tuning (SFT) is a common implementation label for instruction tuning, but the source page does not explicitly name the abbreviation or training objective.
- Instruction-tuning dataset, data curation, train/validation split, and held-out evaluation set are natural implementation concepts implied by “training examples,” but are not described in detail.
- Teacher forcing, next-token prediction, cross-entropy loss, optimizer, learning rate, batch, epoch, checkpoint, and gradient update are common training mechanics that are absent from this beginner page.
- Base model, chat model, system message, user message, assistant message, and conversation template are common instruction-following model concepts not explicitly covered.
- Preference tuning, RLHF, reward model, DPO, and human feedback are related alignment concepts, but should not be assumed to be part of the page's instruction-tuning process.
- Benchmark, exact match, ROUGE, BLEU, accuracy, human evaluation, helpfulness, correctness, and format adherence are possible evaluation concepts; the source provides examples but no named metric.
- Catastrophic forgetting, overfitting, data contamination, instruction diversity, safety tuning, refusal behavior, and out-of-distribution generalization are practical concerns not covered in the source.

## Aliases / Synonyms

- Instruction Tuning ↔ instruction tuning ↔ instruction-tuned training
- Instruction Tuning ↔ instruction fine-tuning ↔ instruction-focused fine-tuning
- SFT ↔ Supervised Fine-Tuning ↔ supervised instruction tuning
- Instruction-following ↔ instruction following ↔ task following
- Desired response ↔ target response ↔ reference answer ↔ expected output
- Useful response ↔ helpful response ↔ helpful output
- Request ↔ user request ↔ task instruction ↔ prompt (context-dependent)
- Response ↔ answer ↔ output (context-dependent)
- Structured response ↔ structured output ↔ schema-constrained output
- Prompting ↔ prompt-based control ↔ runtime instruction
- RAG ↔ Retrieval-Augmented Generation ↔ retrieval-augmented generation
- Pre-training ↔ pretraining
- Foundation Model ↔ foundation model ↔ pretrained general model
- Parameters ↔ model parameters ↔ internal parameters
- Summarization ↔ summary generation
- Classification ↔ categorization
- JSON ↔ JavaScript Object Notation

## Do Not Confuse Candidates

- Instruction Tuning vs Pre-training: pre-training builds broad language and general-pattern ability; instruction tuning is additional training focused on following requests.
- Instruction Tuning vs Fine-tuning: fine-tuning is the broader adaptation term; instruction tuning is a task-following-oriented form of further training.
- Instruction Tuning vs Prompting: instruction tuning changes learned model parameters; prompting changes the instructions supplied at runtime.
- Instruction Tuning vs RAG: instruction tuning changes learned behavior through training; RAG supplies external context during use.
- Instruction Tuning vs Preference Tuning / RLHF / DPO: these are related alignment or post-training approaches, not automatically identical to instruction tuning.
- Instruction vs Prompt: an instruction is the requested task; a prompt is the complete runtime input, which may contain an instruction plus context, examples, or formatting constraints.
- Response vs Desired Response: a response is any produced output; a desired response is the target output used in an example.
- Output vs Structured Output: output is general model-produced content; structured output must follow a specified schema or format.
- Foundation Model vs Instruction-Tuned Model: a foundation model is broadly pretrained; an instruction-tuned model has additional training for reliable task following.
- Runtime vs Training Time: runtime is when the trained model is used; training time is when examples update the model.
- JSON vs Schema: JSON is a data representation format; a schema is the rule describing required fields and structure.
- Summarization vs Translation: summarization shortens content in a target-preserving way; translation changes the language while preserving meaning.
- Classification vs Generation: classification selects a category; generation produces free-form or structured content.
- Knowledge vs Behavior: pre-training can provide broad knowledge; instruction tuning primarily changes how the model uses its capability in response to requests.

## Notes

- The source is a beginner-friendly, single-page explanation. The candidate table intentionally retains capitalization variants, singular/plural variants, repeated phrases, example-specific words, relationship labels, and common terminology implied by the page so it can serve as a maximum raw collection before later deduplication.
- Explicit process sequence in the source: pre-trained model → examples → additional training → learned patterns → instruction-tuned model.
- Explicit examples in the source: summarization, translation into French, classification of a support ticket, Billing, and JSON containing name and date.
- Explicit runtime comparison in the source: instruction tuning changes model parameters; prompting changes supplied instructions; RAG supplies external context.
- No named algorithm, loss function, optimizer, training hyperparameter, benchmark, or numeric evaluation score appears in the source. Candidates for those areas are marked as potential missing concepts rather than presented as source-stated facts.
- The video section is a placeholder (“Video coming soon”) and contributes no additional instructional content.
