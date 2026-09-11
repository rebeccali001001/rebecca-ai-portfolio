# Fine-tuning

## Module/Topic/Source File

- Module: 04 · Fine-tuning (glossary work item)
- Page Module: 02 · LLMs & Transformers
- Topic: Fine-tuning
- Source File: `fine-tuning.html`

## Glossary Candidates

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Fine-tuning | 微调 | Additional training that adapts an existing model for a specific behavior or task. | 在已有模型上继续训练，让它更适合某个具体任务。 |
| fine-tuning | 微调 | A focused form of additional model training. | 针对性地继续训练模型。 |
| additional training | 额外训练；追加训练 | Training that happens after an earlier training stage. | 在原来的训练之后再训练一轮。 |
| adapt | 适配；调整 | Change a model so it works better for a target use. | 把模型调整得更适合某种用途。 |
| adapted model | 适配后的模型 | A model changed for a more specific use. | 已经针对某个用途调整过的模型。 |
| pre-trained model | 预训练模型 | A model that has already learned broad patterns before fine-tuning. | 已经先学过大量通用知识的模型。 |
| pre-trained | 预训练的 | Trained before the current task-specific training. | 在当前任务之前已经训练过。 |
| specific behavior | 特定行为 | The particular behavior a model is expected to produce. | 模型需要表现出来的特定做法。 |
| specific task | 特定任务 | A narrowly defined job or use case. | 范围比较明确的一项工作。 |
| behavior | 行为 | The way a model responds or acts. | 模型实际表现出来的反应方式。 |
| task | 任务 | The job the model is being adapted to perform. | 希望模型完成的事情。 |
| existing model | 现有模型 | A model that already exists before more training. | 已经有了、可以继续训练的模型。 |
| continue training | 继续训练 | Keep training a model from its current state. | 不从零开始，而是接着现在的模型继续学。 |
| focused examples | 针对性样例 | Examples selected for a target behavior or task. | 专门为目标任务准备的示例。 |
| example | 示例；样例 | A training case showing an input, output, or desired behavior. | 用来示范模型应该怎么做的一条样本。 |
| training example | 训练样例 | One example used during training. | 训练过程中使用的一条示例数据。 |
| target example | 目标样例 | An example designed around the intended target behavior. | 围绕目标行为准备的示例。 |
| method | 方法 | A way of carrying out adaptation or training. | 实现模型调整的一种做法。 |
| update model parameters directly | 直接更新模型参数 | Change the model's learned values during training. | 直接改动模型内部学到的数值。 |
| model parameters | 模型参数 | Learned numeric values that determine model behavior. | 决定模型行为的大量内部数值。 |
| parameter | 参数 | A learned value inside a model. | 模型内部会被训练调整的数值。 |
| train adapters | 训练适配器 | Train small additional components while leaving much of the base model unchanged. | 训练附加的小模块，不必大幅改动原模型。 |
| adapter | 适配器 | A trainable add-on used to specialize a base model. | 接在基础模型上的可训练小模块。 |
| adapter training | 适配器训练 | Training an adapter for a target behavior. | 专门训练附加模块来改变模型表现。 |
| specialist training | 专业化训练；专门训练 | Training after general education for a narrower skill. | 模型先学通用能力，再学专门技能。 |
| general education | 通识教育；通用学习 | Broad learning before specialist training. | 先学习广泛知识和能力。 |
| broad skills | 广泛能力；通用能力 | Capabilities that apply across many tasks. | 不只适用于一个任务的通用本领。 |
| start from zero | 从零开始 | Begin training without an existing model. | 没有基础模型，完全重新训练。 |
| build on broad skills | 建立在通用能力之上 | Use existing general abilities as the starting point. | 利用模型已经具备的通用能力继续学习。 |
| base model | 基础模型 | The existing model used as the starting point for adaptation. | 用来继续训练的原始模型。 |
| Base model | 基础模型 | The model loaded before target examples are used. | 流程第一步中被加载的基础模型。 |
| target behavior | 目标行为 | The behavior the adapted model should produce. | 微调后希望模型稳定表现出的行为。 |
| expose a model to examples | 让模型接触示例 | Present training examples to a model. | 把准备好的样例喂给模型学习。 |
| target examples | 目标示例 | Focused examples for the intended task. | 为目标任务准备的训练示例。 |
| training updates | 训练更新 | Changes made to learned values during training. | 训练时对模型内部数值所做的调整。 |
| selected values | 被选中的数值 | The values chosen to be updated. | 训练过程中被改动的那部分数值。 |
| evaluation | 评估 | Testing the adapted model to check its result. | 检查模型训练后效果好不好。 |
| Evaluation | 评估 | A check of quality, safety, and general behavior. | 对效果、安全性和整体表现进行检查。 |
| evaluate the result | 评估结果 | Check what the training produced. | 看训练之后得到了什么效果。 |
| specialized model | 专门化模型 | A model adapted for a narrower behavior or task. | 针对某项任务表现更稳定的模型。 |
| specialized behavior | 专门化行为 | Behavior focused on a particular target. | 模型针对某个方向形成的表现。 |
| consistency | 一致性；稳定性 | Producing similar desired behavior across similar cases. | 面对类似输入时表现更稳定。 |
| more consistent | 更一致；更稳定 | Less variable behavior on the target task. | 在同类任务上不容易忽好忽坏。 |
| target task | 目标任务 | The task for which the model is adapted. | 模型微调时瞄准的具体工作。 |
| use adapted behavior | 使用适配后的行为 | Apply the specialized response pattern in use. | 在实际使用中调用模型学到的新表现。 |
| desired behavior | 期望行为 | The behavior demonstrated by the training examples. | 示例告诉模型应该表现成什么样。 |
| input | 输入 | The information given to the model. | 提供给模型的内容。 |
| output | 输出 | The result produced by the model. | 模型生成或返回的结果。 |
| input and output examples | 输入输出示例 | Examples pairing inputs with desired outputs. | 把问题和理想答案配在一起的样例。 |
| support classification | 客服分类；支持分类 | Classifying customer support tickets into categories. | 把客服工单分到合适类别的任务。 |
| customer support | 客户支持；客服 | Help provided to customers. | 为客户处理问题的服务。 |
| customer ticket | 客户工单 | A customer request or issue submitted for support. | 客户提交的一条问题或请求记录。 |
| ticket | 工单 | A recorded support request. | 用来跟踪客户问题的一条记录。 |
| desired label | 期望标签 | The category label that an example should receive. | 一条样本应该被分到的标准类别。 |
| label | 标签；类别标记 | A category assigned to an input. | 给输入标上的分类名称。 |
| category | 类别 | A group used to organize examples or outputs. | 把相似内容归在一起的组。 |
| consistent category | 稳定类别；一致分类 | A repeatable classification result. | 类似工单能够稳定落到同一类。 |
| writing style | 写作风格 | The characteristic way text is written. | 文字呈现出来的语气和写法。 |
| draft request | 草稿请求 | A request containing a draft or asking for one. | 与文章草稿有关的输入请求。 |
| draft | 草稿 | An early version of a piece of writing. | 尚未最终定稿的文字版本。 |
| tone | 语气 | The emotional or professional manner of writing. | 文字给人的正式、友好等感觉。 |
| format | 格式 | The structure or presentation form of an output. | 输出内容的组织和呈现方式。 |
| structured output | 结构化输出 | Output organized according to a defined structure. | 按固定结构返回的结果。 |
| document | 文档 | A piece of text or file given to the model. | 提供给模型处理的一份文字材料。 |
| target schema | 目标模式；目标结构 | The required fields and structure for an output. | 输出必须遵守的字段和结构。 |
| schema | 模式；数据结构 | A formal description of expected fields and organization. | 规定结果应该有哪些字段、怎么组织。 |
| predictable fields | 可预测字段 | Fields that appear in a stable expected form. | 每次都能较稳定得到的字段。 |
| field | 字段 | One named piece of structured output. | 结构化结果中的一个信息项。 |
| more predictable | 更可预测 | Easier to anticipate the shape or content of outputs. | 更容易预料模型会返回什么样的结果。 |
| real-world example | 现实世界实例 | An example of applying fine-tuning to a practical task. | 把微调用在真实业务中的例子。 |
| practical use case | 实际用例 | A concrete situation where a system is used. | 系统真正落地使用的场景。 |
| What it is NOT | 它不是什么 | A section distinguishing fine-tuning from nearby concepts. | 用来说明微调和相似概念不同的部分。 |
| pre-training | 预训练 | Broad initial training before task-specific adaptation. | 模型先进行的大范围基础训练。 |
| broad initial training | 广泛初始训练 | The general training stage before specialization. | 在专门训练前进行的通用训练。 |
| prompting | 提示；提示词设计 | Giving instructions at runtime to influence a model. | 使用时通过提示告诉模型怎么回答。 |
| prompt | 提示词；输入指令 | Runtime instructions or input used to guide a model. | 每次调用模型时给它的指令或问题。 |
| runtime | 运行时 | The time when a model is being used. | 模型真正接收请求并作答的时候。 |
| instructions at runtime | 运行时指令 | Instructions supplied when the model is used. | 使用模型当下临时提供的要求。 |
| retrieval-augmented generation | 检索增强生成 | Generate responses using information retrieved at query time. | 先查外部资料，再根据资料生成答案。 |
| RAG | 检索增强生成缩写 | Short form for retrieval-augmented generation. | Retrieval-Augmented Generation 的缩写。 |
| retrieve external information | 检索外部信息 | Find information outside the model at use time. | 使用时从外部资料库查找信息。 |
| query time | 查询时；请求时 | The time when a user request is handled. | 用户提出问题、系统正在处理请求的时刻。 |
| external information | 外部信息 | Information supplied from outside the model's learned parameters. | 来自模型外部资料源的信息。 |
| adaptation choice | 适配选择 | A way of changing or guiding a model for a use case. | 为特定需求选择提示、RAG 或微调等方式。 |
| prompting, RAG, and fine-tuning | 提示、RAG 与微调 | Three different ways to adapt or guide model use. | 三种不同的模型适配路线。 |
| model behavior | 模型行为 | How the model responds to inputs. | 模型面对输入时的表现方式。 |
| behavior through training | 通过训练形成的行为 | Behavior changed by updating learned values. | 通过训练改动模型内部能力和反应方式。 |
| behavior at runtime | 运行时行为 | Behavior influenced by instructions during use. | 不改模型本身，只在调用时改变表现。 |
| quality | 质量；效果 | How good the model's outputs are. | 模型回答是否好用、准确、符合要求。 |
| safety | 安全性 | Whether model behavior avoids harmful or unsafe results. | 模型是否会产生危险或不合适的结果。 |
| general behavior | 通用行为；整体行为 | The model's behavior beyond the narrow target task. | 除目标任务外模型整体还会怎么表现。 |
| regression | 回归；能力退化 | A loss of quality in existing abilities after adaptation. | 微调后原来会的能力反而变差。 |
| check regressions | 检查回归问题 | Test whether previous capabilities became worse. | 检查微调有没有损害旧能力。 |
| model adaptation | 模型适配 | Adjusting a model to fit a target use. | 让模型适应新用途的总称。 |
| model specialization | 模型专门化 | Making a general model better at a narrower use. | 把通用模型变成更擅长某类任务的模型。 |
| learned behavior | 学到的行为 | Behavior encoded through model training. | 模型通过训练学会的反应方式。 |
| learned values | 学到的数值 | Internal values learned during training. | 模型训练中形成的内部数值。 |
| training process | 训练过程 | The sequence of preparing examples, updating values, and evaluating. | 准备样例、训练更新、检查结果的一整套过程。 |
| base-model stage | 基础模型阶段 | The first stage that loads a pre-trained model. | 流程中先拿到基础模型的阶段。 |
| target-example stage | 目标示例阶段 | The stage that prepares focused input-output examples. | 准备目标任务样例的阶段。 |
| additional-training stage | 额外训练阶段 | The stage that trains parameters or adapters. | 用样例更新参数或适配器的阶段。 |
| specialized-model stage | 专门化模型阶段 | The stage where adapted behavior is used. | 得到更专门模型并开始使用的阶段。 |
| evaluation stage | 评估阶段 | The stage that checks quality, safety, and general behavior. | 训练后检查效果和安全性的阶段。 |
| step | 步骤 | One part of the fine-tuning flow. | 整个流程中的一个环节。 |
| flow | 流程 | The ordered sequence from base model to evaluation. | 从基础模型到评估的先后步骤。 |
| base model → target examples → additional training → specialized model → evaluation | 基础模型→目标示例→额外训练→专门化模型→评估 | The page's five-step fine-tuning flow. | 页面展示的微调五步流程。 |
| target behavior consistency | 目标行为一致性 | Stable performance on the behavior being trained. | 在目标行为上反复表现稳定。 |
| target-task quality | 目标任务质量 | Quality measured on the task the model was adapted for. | 模型专门任务上的效果。 |
| safety check | 安全检查 | A test for unsafe or harmful behavior. | 检查输出是否安全合规。 |
| general-behavior check | 通用行为检查 | A test that checks abilities beyond the target task. | 检查微调后整体能力有没有异常。 |
| model values | 模型数值 | Internal learned values that can be updated. | 模型内部可以被调整的数值。 |
| adapter-based adaptation | 基于适配器的适配 | Specialization using trainable add-on modules. | 通过附加小模块来完成专门化。 |
| parameter-based adaptation | 基于参数的适配 | Specialization by changing model parameters. | 直接改变模型参数来完成专门化。 |
| target schema example | 目标结构示例 | An example demonstrating the required output schema. | 展示输出格式应该长什么样的样例。 |
| tone and format | 语气与格式 | The style and structure demonstrated by examples. | 示例中要求的说话方式和排版形式。 |
| input document | 输入文档 | A document supplied to a structured-output task. | 交给模型处理的文档。 |
| target label example | 目标标签示例 | A ticket example paired with the desired category. | 工单和标准分类配对的示例。 |
| more consistent draft | 更一致的草稿 | A draft whose tone and format are more repeatable. | 每次生成的草稿风格更统一。 |
| more predictable output | 更可预测的输出 | Output with a more stable expected shape. | 输出结构和内容更容易预料。 |
| model adaptation vs model training | 模型适配与模型训练 | Adaptation is a focused continuation of training. | 微调是训练的一种有明确目标的后续阶段。 |
| Fine-tuning ≠ Pre-training | 微调不等于预训练 | Fine-tuning is targeted additional training; pre-training is broad initial training. | 微调是专门追加训练，预训练是最初的大范围学习。 |
| Fine-tuning ≠ Prompting | 微调不等于提示 | Fine-tuning changes learned behavior through training; prompting changes runtime instructions. | 微调改模型学到的行为，提示只改使用时的指令。 |
| Fine-tuning ≠ RAG | 微调不等于 RAG | Fine-tuning adapts behavior; RAG retrieves external information at query time. | 微调改行为，RAG 在提问时查外部资料。 |
| target behavior vs broad skills | 目标行为与广泛能力 | A narrow target is built on top of broad existing skills. | 专项能力建立在通用能力之上。 |
| parameters vs adapters | 参数与适配器 | Adaptation may update model parameters or train adapters. | 可以直接改模型参数，也可以训练附加模块。 |
| training vs evaluation | 训练与评估 | Training updates the model; evaluation checks what happened. | 训练负责改变模型，评估负责检查结果。 |
| quality, safety, and general behavior | 质量、安全性与通用行为 | Three dimensions the page says evaluation should test. | 评估不能只看任务效果，还要看安全和整体能力。 |
| LLM | 大语言模型 | A language model that can be adapted to specialized behaviors. | 可以通过微调适应具体语言任务的模型。 |
| language model | 语言模型 | A model that processes or generates language. | 能理解或生成语言的模型。 |
| LLMs & Transformers | 大语言模型与 Transformer | The page's broader topic area. | 该页面所属的知识主题分类。 |
| foundation model | 基础模型；基础模型体系 | A broadly trained model that can support later adaptation. | 先具备通用能力、再用于不同任务的模型。 |
| Foundation Models | 基础模型 | The related concept linked from the page. | 页面“Related concepts”中的相关主题。 |
| Parameters | 参数 | The related concept linked from the page. | 页面“Related concepts”中的参数主题。 |
| Pre-training | 预训练 | The related concept linked from the page. | 页面“Related concepts”中的预训练主题。 |
| RAG | 检索增强生成 | The related concept linked from the page. | 页面“Related concepts”中的 RAG 主题。 |
| target examples | 目标示例 | The video metadata's phrase for focused examples. | 视频信息中强调的目标样例。 |
| evaluation | 评估 | The video metadata's phrase for checking the result. | 视频信息中强调的训练后检查。 |
| specialist training | 专门训练 | The video metadata's phrase for fine-tuning. | 视频信息中用来概括微调的短语。 |
| visual explainer | 视觉讲解 | A visual explanation supplied through the page's video section. | 用视频或图像帮助理解概念。 |
| independent video | 独立视频 | A separate explainer video associated with the topic. | 页面附带的独立讲解视频。 |
| Azure Neural voice | Azure Neural 语音 | The voice label shown in the video metadata. | 页面视频元信息中标出的语音来源标签。 |
| MP4 | MP4 | A video file format. | 视频文件的一种常见格式。 |
| H.264 | H.264 | A video compression format listed in the metadata. | 视频编码格式。 |
| AAC | AAC | An audio compression format listed in the metadata. | 音频编码格式。 |

## Potential Missing Concepts

以下概念是围绕页面主题的最大补充候选；它们没有在 `fine-tuning.html` 正文中展开定义，保留在“潜在缺失”区，不把它们误当成页面已讲内容：

- supervised fine-tuning (SFT)；监督式微调
- instruction tuning；指令微调
- task-specific fine-tuning；任务特定微调
- domain adaptation；领域适配
- domain-specific fine-tuning；领域特定微调
- continued pre-training；持续预训练
- transfer learning；迁移学习
- parameter-efficient fine-tuning (PEFT)；参数高效微调
- full fine-tuning；全量微调
- partial fine-tuning；部分微调
- layer freezing；冻结层
- frozen parameters；冻结参数
- trainable parameters；可训练参数
- trainable weights；可训练权重
- adapter layers；适配器层
- adapter tuning；适配器调优
- bottleneck adapter；瓶颈适配器
- LoRA (Low-Rank Adaptation)；低秩适配
- low-rank update；低秩更新
- QLoRA；量化低秩适配
- prefix tuning；前缀调优
- prompt tuning；提示调优
- P-tuning；P 调优
- soft prompt；软提示
- prompt encoder；提示编码器
- bias-only tuning；仅偏置调优
- BitFit；仅偏置微调方法
- IA3；IA³ 适配方法
- reparameterization；重参数化
- merge adapter；合并适配器
- adapter composition；适配器组合
- multi-task fine-tuning；多任务微调
- single-task fine-tuning；单任务微调
- few-shot fine-tuning；少样本微调
- multi-epoch fine-tuning；多轮次微调
- continual fine-tuning；持续微调
- catastrophic forgetting；灾难性遗忘
- negative transfer；负迁移
- overfitting；过拟合
- underfitting；欠拟合
- memorization；记忆化
- generalization；泛化
- domain shift；领域偏移
- distribution shift；分布偏移
- task interference；任务干扰
- instruction-following；指令遵循
- alignment；对齐
- preference optimization；偏好优化
- reinforcement learning from human feedback (RLHF)；基于人类反馈的强化学习
- direct preference optimization (DPO)；直接偏好优化
- reward model；奖励模型
- preference data；偏好数据
- synthetic data；合成数据
- human-written data；人工编写数据
- data curation；数据整理
- data filtering；数据过滤
- data deduplication；数据去重
- data contamination；数据污染
- data mixture；数据混合
- training corpus；训练语料
- fine-tuning dataset；微调数据集
- instruction dataset；指令数据集
- demonstration；示范样例
- input-output pair；输入输出对
- prompt-completion pair；提示补全对
- chat template；聊天模板
- conversation format；对话格式
- system message；系统消息
- user message；用户消息
- assistant message；助手消息
- completion；补全
- target response；目标回复
- ground truth；真实答案
- label quality；标签质量
- annotation；标注
- annotation guidelines；标注规范
- label noise；标签噪声
- data split；数据划分
- training set；训练集
- validation set；验证集
- development set；开发集
- test set；测试集
- holdout set；留出集
- evaluation set；评估集
- benchmark；基准测试
- baseline model；基线模型
- control model；对照模型
- ablation study；消融研究
- before-and-after comparison；前后对比
- regression test；回归测试
- capability retention；能力保留
- transfer evaluation；迁移评估
- task performance；任务表现
- task accuracy；任务准确率
- exact match；完全匹配率
- precision；精确率
- recall；召回率
- F1 score；F1 分数
- macro-F1；宏平均 F1
- micro-F1；微平均 F1
- pass rate；通过率
- pass@k；前 k 次通过率
- loss；损失
- training loss；训练损失
- validation loss；验证损失
- cross-entropy loss；交叉熵损失
- perplexity；困惑度
- calibration；校准
- consistency score；一致性分数
- format adherence；格式遵循度
- schema validity；模式有效性
- structured-output accuracy；结构化输出准确率
- toxicity；有害性
- refusal rate；拒答率
- safety evaluation；安全评估
- factuality；事实性
- hallucination rate；幻觉率
- BLEU；BLEU 指标
- ROUGE；ROUGE 指标
- BERTScore；BERTScore 指标
- human evaluation；人工评估
- pairwise preference；两两偏好比较
- judge model；评审模型
- evaluation harness；评测框架
- hyperparameter；超参数
- learning rate；学习率
- batch size；批大小
- micro-batch size；微批大小
- gradient accumulation；梯度累积
- number of epochs；训练轮数
- training steps；训练步数
- warmup steps；预热步数
- weight decay；权重衰减
- dropout；丢弃法
- optimizer；优化器
- Adam；Adam 优化器
- AdamW；AdamW 优化器
- gradient；梯度
- backpropagation；反向传播
- gradient clipping；梯度裁剪
- checkpoint；检查点
- early stopping；提前停止
- learning-rate schedule；学习率调度
- cosine schedule；余弦调度
- mixed precision；混合精度
- bfloat16；bfloat16 精度
- FP16；半精度浮点数
- GPU；图形处理器
- VRAM；显存
- compute budget；计算预算
- training cost；训练成本
- inference cost；推理成本
- latency；延迟
- throughput；吞吐量
- model size；模型大小
- parameter count；参数量
- memory footprint；内存占用
- quantization；量化
- quantized fine-tuning；量化微调
- quantization-aware training；量化感知训练
- 4-bit quantization；4 位量化
- 8-bit quantization；8 位量化
- model checkpoint format；模型检查点格式
- model card；模型卡
- adapter checkpoint；适配器检查点
- model version；模型版本
- reproducibility；可复现性
- random seed；随机种子
- experiment tracking；实验跟踪
- hyperparameter sweep；超参数搜索
- prompt baseline；提示基线
- RAG baseline；RAG 基线
- fine-tuning vs prompting；微调与提示比较
- fine-tuning vs RAG；微调与 RAG 比较
- knowledge update；知识更新
- behavior update；行为更新
- style transfer；风格迁移
- format control；格式控制
- domain knowledge injection；领域知识注入
- factual knowledge storage；事实知识存储
- retrieval freshness；检索新鲜度
- model editing；模型编辑
- knowledge editing；知识编辑
- serving a fine-tuned model；部署微调模型
- model registry；模型注册表
- deployment；部署
- rollout；发布
- shadow evaluation；影子评估
- online evaluation；在线评估
- monitoring；监控
- drift monitoring；漂移监控
- rollback；回滚
- safety guardrail；安全护栏
- access control；访问控制
- data privacy；数据隐私
- sensitive data；敏感数据
- personally identifiable information (PII)；个人可识别信息
- copyright risk；版权风险
- license compliance；许可证合规
- model ownership；模型所有权

## Aliases / Synonyms

- Fine-tuning / fine tuning / model fine-tuning / 微调／模型微调
- additional training / continued training / further training / 额外训练／继续训练／进一步训练
- pre-trained model / pretrained model / base model / 预训练模型／基础模型
- adapted model / specialized model / task-adapted model / 适配模型／专门化模型／任务适配模型
- target behavior / desired behavior / intended behavior / 目标行为／期望行为／预期行为
- specific task / target task / task-specific use case / 特定任务／目标任务／任务特定用例
- focused examples / target examples / task examples / 针对性示例／目标示例／任务示例
- model parameter / parameter / learned value / 模型参数／参数／学到的数值
- update parameters / update learned values / change model values / 更新参数／更新学到的数值／改变模型数值
- adapter / adaptation module / trainable add-on / 适配器／适配模块／可训练附加模块
- train adapters / adapter training / adapter tuning / 训练适配器／适配器训练／适配器调优
- specialist training / model specialization / specialized training / 专门训练／模型专门化／专业化训练
- broad skills / general skills / general capabilities / 广泛能力／通用能力／一般能力
- input-output examples / input-output pairs / prompt-completion pairs / 输入输出示例／输入输出对／提示补全对
- label / target label / desired label / 标签／目标标签／期望标签
- category / class / classification label / 类别／类／分类标签
- writing style / style / tone and format / 写作风格／风格／语气与格式
- structured output / schema-constrained output / structured response / 结构化输出／模式约束输出／结构化回复
- target schema / output schema / response schema / 目标模式／输出模式／回复模式
- predictable fields / stable fields / expected fields / 可预测字段／稳定字段／预期字段
- pre-training / initial training / broad training / 预训练／初始训练／广泛训练
- prompting / prompt-based adaptation / in-context instruction / 提示／基于提示的适配／上下文内指令
- prompt / instruction / runtime instruction / 提示词／指令／运行时指令
- RAG / retrieval-augmented generation / retrieval augmented generation / 检索增强生成
- retrieve external information / retrieve at query time / use external context / 检索外部信息／查询时检索／使用外部上下文
- query time / runtime / inference time / 查询时／运行时／推理时
- quality / output quality / task quality / 质量／输出质量／任务质量
- safety / model safety / safety behavior / 安全性／模型安全／安全行为
- general behavior / overall behavior / non-target behavior / 通用行为／整体行为／非目标行为
- regression / capability regression / performance regression / 回归／能力退化／性能回归
- fine-tuning flow / adaptation pipeline / training pipeline / 微调流程／适配流水线／训练流水线
- base-model stage / initialization stage / starting-model stage / 基础模型阶段／初始化阶段／起始模型阶段
- evaluation / model evaluation / post-training evaluation / 评估／模型评估／训练后评估
- fine-tuning / SFT / supervised fine-tuning / 微调／监督式微调
- parameter-efficient fine-tuning / PEFT / efficient adaptation / 参数高效微调／PEFT／高效适配
- low-rank adaptation / LoRA / low-rank fine-tuning / 低秩适配／LoRA／低秩微调
- quantized LoRA / QLoRA / quantization-aware adapter tuning / 量化 LoRA／QLoRA／量化适配器调优
- full fine-tuning / full-parameter fine-tuning / 全量微调／全参数微调
- freeze layers / freeze parameters / keep base weights fixed / 冻结层／冻结参数／保持基础权重不变
- catastrophic forgetting / capability forgetting / loss of prior abilities / 灾难性遗忘／能力遗忘／原有能力丢失
- overfitting / memorization / poor generalization / 过拟合／记忆化／泛化不佳
- training set / fine-tuning set / adaptation dataset / 训练集／微调集／适配数据集
- validation set / dev set / development set / 验证集／开发集
- test set / holdout set / evaluation set / 测试集／留出集／评估集
- accuracy / exact match / task success rate / 准确率／完全匹配率／任务成功率
- loss / objective loss / training loss / 损失／目标损失／训练损失
- perplexity / language-model perplexity / 困惑度／语言模型困惑度
- human evaluation / expert evaluation / manual review / 人工评估／专家评估／人工审查
- regression test / capability retention test / before-and-after test / 回归测试／能力保留测试／前后对比测试

## Do Not Confuse Candidates

- Fine-tuning vs Pre-training：微调是基于已有模型的针对性追加训练；预训练是模型最初进行的广泛训练。
- Fine-tuning vs Prompting：微调通过训练改变模型学到的行为；提示通过运行时指令影响模型当下的回答。
- Fine-tuning vs RAG：微调适配模型行为；RAG 在查询时检索外部信息。
- Fine-tuning vs Continued Pre-training：两者都可能是继续训练，但微调通常使用更明确的目标任务或行为示例，持续预训练更偏向继续学习领域语料。
- Fine-tuning vs Model Editing：微调通常通过数据和训练更新一组参数或适配器；模型编辑通常针对少数事实或行为做局部修改。
- Pre-trained Model vs Base Model：页面语境中二者都可指微调起点，但“预训练模型”强调先前训练历史，“基础模型”强调作为后续适配底座的角色。
- Base Model vs Specialized Model：基础模型提供广泛能力；专门化模型在特定任务或行为上经过适配。
- Broad Skills vs Target Behavior：广泛能力是已有通用基础；目标行为是微调后希望稳定加强的窄方向。
- Parameter vs Adapter：参数是模型内部的学习数值；适配器是可附加、可训练的小模块。
- Update Parameters Directly vs Train Adapters：前者直接修改模型本体的参数；后者主要训练附加模块。
- Adapter vs Full Model：适配器只是附加组件，不等于完整基础模型或完整微调后的模型。
- Training vs Evaluation：训练会更新模型；评估只检查训练结果，通常不应把评估本身当作训练。
- Evaluation vs Benchmark：评估是整体检查过程；基准测试是可重复比较的一类评估设置或数据集。
- Quality vs Consistency：质量表示输出好不好；一致性表示相似输入下是否稳定地产生相似的期望行为。
- Quality vs Accuracy：质量是更宽泛的判断；准确率是某类任务中特定的数值指标。
- Safety vs General Behavior：安全关注是否产生危险或不合适结果；通用行为关注目标任务以外的整体能力和反应。
- Regression vs Overfitting：回归是已有能力或指标变差；过拟合是训练数据表现好但泛化变差，二者可能相关但不等同。
- Target Examples vs Target Schema：目标示例是训练样本；目标模式是规定输出字段和结构的规范。
- Input vs Output：输入是给模型的内容；输出是模型生成或返回的结果。
- Label vs Target Behavior：标签通常是分类目标；目标行为是更宽泛的模型表现要求。
- Category vs Label：类别是概念上的分组；标签是附着在具体输入或样本上的标记。
- Tone vs Format：语气描述说话风格；格式描述结构、排列和呈现方式。
- Structured Output vs Predictable Output：结构化输出强调遵守规定结构；可预测输出强调结果更容易预料，未必一定是严格结构化。
- Schema vs Field：模式规定整体结构；字段是结构中的一个信息项。
- Prompting vs Prompt Tuning：页面中的 prompting 是运行时给指令；prompt tuning 是训练可学习提示参数的方法。
- RAG vs Fine-tuning for Knowledge：RAG 在请求时提供外部资料，便于更新知识；微调主要改变行为或任务表现，不等于实时知识库。
- RAG vs External Information：RAG 是完整的方法；外部信息只是该方法可能检索到的内容。
- Runtime vs Training Time：运行时是模型被调用回答请求；训练时是模型参数或适配器被更新。
- LLM vs Foundation Model：LLM 是语言模型类别；基础模型是更宽泛的可作为下游适配底座的模型概念。
- Foundation Model vs Base Model：基础模型有时是角色称呼，基础模型也可能是多模态或非语言模型；不要把两者机械当作完全同义。
- SFT vs RLHF：SFT 从示例答案学习；RLHF 通常使用人类偏好、奖励模型和强化学习等后续流程。
- PEFT vs Full Fine-tuning：PEFT 只更新较少参数或附加组件；全量微调更新更多或全部模型参数。
- LoRA vs Adapter：LoRA 是一种低秩参数更新方法；adapter 是更大的附加模块类别。
- LoRA vs QLoRA：QLoRA 在量化基础模型上使用 LoRA；LoRA 本身不必包含量化。
- Fine-tuning Dataset vs Evaluation Set：微调数据用于更新模型；评估集用于检查模型，不能默认混用。
- Training Set vs Validation Set vs Test Set：训练集用于学习，验证集用于调参或选择，测试集用于最终或独立检查。
- Training Loss vs Evaluation Metric：损失是训练优化目标的一种形式；评估指标用于解释任务效果，二者不一定同向或同尺度。
- Exact Match vs Semantic Similarity：完全匹配要求文本或结构精确相同；语义相似允许表达不同但意思接近。
- Catastrophic Forgetting vs Generalization：灾难性遗忘是旧能力丢失；泛化是对未见样本表现良好，方向不同。
- Fine-tuning vs Inference：微调发生在训练阶段；推理是模型训练完成后生成输出的阶段。
- Model Behavior vs Model Knowledge：行为是模型怎么响应；知识是模型可能掌握或调用的信息，微调改变行为不必等于注入可靠新知识。
- Adapter Checkpoint vs Model Checkpoint：适配器检查点保存附加组件；模型检查点通常保存更完整的模型状态。

## Notes

- 本 raw 文件按 `fine-tuning.html` 的完整正文、页面导航、相关链接文本和视频元信息做最大候选收集；不去重、不删减，保留大小写、单复数、重复出现和短语级候选。
- 页面核心定义是：Fine-tuning 是 additional training，用来把 pre-trained model 适配到更具体的 behavior 或 task。
- 页面明确给出两类适配方式：直接更新 model parameters，或训练 adapters；因此两套术语都保留在候选表中。
- 页面类比是“general education 之后的 specialist training”：模型基于 broad skills 继续学习，而不是从 zero 开始。
- 页面五步流程是：Base model → Target examples → Additional training → Specialized model → Evaluation。
- 页面明确要求评估 quality、safety 和 general behavior，并检查 regressions；这些词属于页面直接出现的评估语境。
- 页面三个现实例子是 Support classification、Writing style、Structured output，分别包含 customer ticket/label、draft/tone/format、document/target schema/predictable fields 等候选。
- 页面明确区分 Fine-tuning、Pre-training、Prompting 和 RAG；其中 Prompting 改变 runtime instructions，RAG 在 query time retrieves external information。
- 页面相关概念链接包括 Pre-training、Foundation Models、LLM、RAG、Parameters；链接文本和对应概念均保留，不能因为页面只展开了部分内容而删除。
- 页面标题上下文为 “Fine-tuning · LLMs & Transformers”；因此 LLM、language model、Transformers 相关上下文也保留为关系候选。
- 页面视频区域出现 specialist training、target examples、evaluation、visual explainer、independent video、Azure Neural voice、MP4、H.264、AAC 等元信息候选；它们不应被误解为微调算法。
- `Potential Missing Concepts` 只列出围绕页面主题但正文未展开的补充候选，包括 SFT、PEFT、LoRA、QLoRA、评估指标、超参数、数据集、部署和安全等；这些不代表页面已经定义。
- `Aliases / Synonyms` 用于保留可能的别名、大小写变体和后续清洗时需要判断的近义词；不应直接当作已经完成术语规范化。
- `Do Not Confuse Candidates` 用于保留页面中的显式对比和该主题中高风险混淆边界，后续最终词表仍需逐条核验。
- 该文件是 glossary-work/raw 的原始收集稿，不是最终去重、排序、翻译校准或外部事实核验后的术语表。
