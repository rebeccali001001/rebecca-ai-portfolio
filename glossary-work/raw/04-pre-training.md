# Topic

Pre-training

Module/Topic/Source File

- Module: 02 · LLMs & Transformers
- Topic: Pre-training
- Source File: `pre-training.html`

## Glossary Candidates

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Pre-training | 预训练 | The broad initial training stage that teaches general patterns from large amounts of data. | 先用大量数据让模型学会通用规律的阶段。 |
| pre-training stage | 预训练阶段 | The initial, broad part of a model-training lifecycle. | 模型训练一开始、范围很广的那一段。 |
| initial training | 初始训练 | Training performed before later adaptation or specialization. | 在专门训练之前进行的第一轮训练。 |
| broad initial training | 广泛初始训练 | Initial training over varied data and general capabilities. | 用很多不同类型的数据先学通用能力。 |
| general pattern | 通用模式；一般规律 | A reusable relationship learned from broad examples. | 从大量例子中学到、以后很多任务都能用的规律。 |
| large amounts of data | 大量数据 | A large collection of examples used for learning. | 数量很大的学习材料。 |
| model | 模型 | A learned system that maps input information to predictions or outputs. | 学会规律后可以反复处理新输入的程序。 |
| language model | 语言模型 | A model that learns patterns in language and predicts text units. | 学习文字规律并预测文字单位的模型。 |
| base model | 基础模型 | The broadly trained model produced before task-specific adaptation. | 还没有针对具体任务调整过的通用模型。 |
| foundation model | 基础模型；基座模型 | A broadly trained model that can support many downstream applications. | 先学通用能力、再支持很多应用的模型底座。 |
| LLM | 大型语言模型 | A large language model trained on extensive text or multimodal data. | 用海量数据训练、擅长处理语言的大模型。 |
| large language model | 大型语言模型 | A language model with many learned parameters and broad training data. | 参数很多、训练材料很广的语言模型。 |
| AI model | 人工智能模型 | A learned computational system that produces predictions or outputs. | 用数据学会规律并产出结果的 AI 系统。 |
| model capability | 模型能力 | What a model can do after learning from data. | 模型经过学习后能够完成的事情。 |
| capability | 能力 | A useful behavior or task a model can perform. | 模型实际能做到的一种事情。 |
| reusable starting point | 可复用起点 | A trained model that can be adapted for multiple later uses. | 训练好后可以拿去做很多后续工作的起点。 |
| general education | 通识教育 | Analogy for broad learning before specialist training. | 类比先学很多基础知识、再选择专业。 |
| specialist training | 专项训练 | Later learning focused on a specific job or task. | 针对某个具体任务继续学习。 |
| broad data | 广泛数据 | Varied data covering many subjects, formats, or use cases. | 覆盖很多主题或形式的数据。 |
| dataset | 数据集 | An organized collection of data used for training or evaluation. | 按一定方式收集整理的一批数据。 |
| large dataset | 大型数据集 | A dataset containing a very large number of examples. | 包含大量例子的一整套数据。 |
| mixed dataset | 混合数据集 | A dataset combining different kinds of data or subjects. | 把不同来源、主题或类型的数据放在一起。 |
| training data | 训练数据 | Examples used to teach a model. | 用来教模型的例子集合。 |
| training example | 训练示例 | One piece of data used in the learning process. | 训练时给模型看的一个例子。 |
| example | 示例；例子 | An input and target or expected continuation used for learning. | 给模型学习或参考的一条材料。 |
| text | 文本 | Written language used as training input or output. | 文字形式的信息。 |
| code | 代码 | Programming language text that can be included in training data. | 写给计算机执行的程序文字。 |
| image | 图像；图片 | Visual data that can be used as a training example. | 可以交给模型学习或分析的图片。 |
| other data | 其他数据 | Data modalities beyond the examples named in the page. | 除文字、代码、图片之外的其他材料。 |
| data modality | 数据模态 | A kind or format of information, such as text, image, or audio. | 信息的类型，例如文字、图片或声音。 |
| broad material | 广泛材料 | Diverse source material collected for general learning. | 为了学通用能力收集的各种材料。 |
| training corpus | 训练语料；训练语料库 | A large body of text or other examples used for training. | 用来训练模型的大批文字或数据材料。 |
| corpus | 语料库 | A collection of language or other data for study or training. | 收集起来供分析或训练使用的数据集合。 |
| data source | 数据来源 | The origin of examples used in a dataset. | 数据是从哪里收集来的。 |
| data mixture | 数据混合配比 | The composition of different sources or categories in training data. | 训练数据中各类材料所占的组合和比例。 |
| training example construction | 训练样本构造 | Turning raw data into examples the model can learn from. | 把原始材料整理成模型可以学习的例子。 |
| input | 输入 | Information given to a model for prediction. | 送进模型的信息。 |
| output | 输出 | The result produced by a model. | 模型处理后给出的结果。 |
| target | 目标；目标答案 | The expected token or answer used to compare with a prediction. | 训练时拿来对照模型预测的正确目标。 |
| expected answer | 预期答案 | The answer a training example is meant to represent. | 例子中希望模型学会给出的答案。 |
| missing token | 缺失词元 | A token hidden or omitted so the model must predict it. | 被遮住、需要模型猜出来的文字单位。 |
| next token | 下一个词元 | The text unit that comes immediately after the current context. | 当前文字后面最可能接着出现的单位。 |
| token | 词元；标记 | A small unit of text processed by a language model. | 语言模型处理文字时切分出的单位。 |
| text unit | 文本单位 | A piece of text treated as one processing unit. | 模型一次处理的一小段文字。 |
| token sequence | 词元序列 | An ordered series of tokens representing text. | 按顺序排成的一串词元。 |
| context | 上下文 | The preceding information used to predict a token. | 模型用来猜下一部分的前文信息。 |
| context window | 上下文窗口 | The amount of preceding input available to a model at once. | 模型一次能看到的前文范围。 |
| tokenization | 词元化；分词 | Converting language into tokens a model can process. | 把文字切成模型能处理的小单位。 |
| tokenizer | 词元分析器；分词器 | A tool or component that converts text into tokens. | 负责把文字切成词元的工具。 |
| tokenization process | 词元化过程 | The process of splitting or encoding text into tokens. | 文字变成词元的一连串步骤。 |
| prediction | 预测 | Estimating a missing or next token from context. | 根据前文猜接下来会出现什么。 |
| next-token prediction | 下一个词元预测 | Predicting the next token in a sequence. | 预测一句话接下来最可能出现的词元。 |
| missing-token prediction | 缺失词元预测 | Predicting a token hidden inside an example. | 猜出被遮住的词元。 |
| token prediction | 词元预测 | Predicting which token should be produced. | 判断哪个词元最可能是正确答案。 |
| language prediction | 语言预测 | Predicting language units based on previous language. | 根据前面的文字预测后面的文字。 |
| autoregressive prediction | 自回归预测 | Predicting each next token from previously available tokens. | 一边看已经有的文字，一边逐个预测后面的文字。 |
| causal language modeling | 因果语言建模 | Training a language model to predict later tokens from earlier ones. | 只能根据前文预测后文的语言训练方式。 |
| masked language modeling | 掩码语言建模 | Training by hiding tokens and predicting the hidden content. | 把句子中的词遮住，让模型猜回来。 |
| self-supervised learning | 自监督学习 | Creating training targets from the data itself. | 不一定人工标答案，而是从原始数据自己生成学习目标。 |
| unsupervised learning | 无监督学习 | Learning patterns from data without manually supplied labels. | 没有人工逐条标注答案、主要自己找规律。 |
| training objective | 训练目标 | The prediction or optimization goal used during training. | 训练时规定模型要尽量做到的事情。 |
| learning objective | 学习目标 | The objective that defines what the model should learn. | 告诉训练过程“什么算学得好”。 |
| objective function | 目标函数 | A mathematical function describing the desired training result. | 用数学方式表示训练想达到的目标。 |
| loss | 损失 | A numerical measure of how far a prediction is from the target. | 用数字表示模型猜得离正确答案有多远。 |
| loss function | 损失函数 | A formula that converts prediction error into a training signal. | 把预测错误计算成一个数字的公式。 |
| prediction error | 预测误差 | The difference between a model prediction and the target. | 模型预测与正确目标之间的差距。 |
| error | 错误；误差 | The mismatch between a prediction and the expected result. | 模型猜错或没猜准的程度。 |
| error signal | 误差信号 | Information indicating how the model should change after an error. | 告诉模型下一步该往哪个方向改的信号。 |
| cross-entropy loss | 交叉熵损失 | A common loss for comparing predicted token probabilities with the target token. | 常用于衡量模型给正确词元分配概率是否合适。 |
| perplexity | 困惑度 | A language-model metric related to how well it predicts token sequences. | 衡量语言模型预测文字顺不顺、准不准的指标。 |
| metric | 指标 | A numerical measure used to evaluate training or model behavior. | 用数字衡量模型表现的标准。 |
| evaluation metric | 评估指标 | A metric used to judge model quality or performance. | 用来判断模型效果好不好的数字。 |
| training metric | 训练指标 | A metric monitored during training. | 训练过程中持续观察的数字。 |
| parameter | 参数 | A learned numerical value inside a model. | 模型内部会在训练中不断调整的数字。 |
| model parameter | 模型参数 | A numerical value that influences a model's predictions. | 会影响模型输出、训练时会变化的内部数字。 |
| learned parameter | 学到的参数 | A parameter adjusted from data during training. | 模型通过数据训练后得到的内部数值。 |
| parameter value | 参数值 | The current numerical setting of a model parameter. | 某个模型参数此刻具体是多少。 |
| internal value | 内部数值 | A learned number used inside a model. | 模型内部用来表示规律的一大批数字。 |
| learned value | 学到的数值 | A numerical value retained after training updates. | 训练调整后保留下来的数字。 |
| model weights | 模型权重 | Learned values that determine how strongly internal signals affect outputs. | 决定不同信息影响大小的一组内部数字。 |
| weights | 权重 | Numerical strengths assigned to learned relationships. | 表示某种关系重要程度的数字。 |
| update | 更新 | Changing model parameters in response to prediction error. | 根据错误把模型内部数字改一改。 |
| parameter update | 参数更新 | One adjustment of model parameters during training. | 训练中对参数进行的一次修改。 |
| gradient | 梯度 | A direction and magnitude indicating how parameters affect loss. | 指示参数应该往哪个方向调整、调整多少的信号。 |
| gradient descent | 梯度下降 | An optimization method that adjusts parameters to reduce loss. | 沿着让错误变小的方向逐步改参数。 |
| backpropagation | 反向传播 | Computing how prediction error should affect earlier parameters. | 把错误从结果倒着传回前面各层、帮助调整参数。 |
| optimizer | 优化器 | The algorithm that applies parameter updates during training. | 按规则决定参数如何更新的算法。 |
| learning rate | 学习率 | The step size used when updating parameters. | 每次改参数时步子迈多大的设置。 |
| batch | 批次 | A group of training examples processed together. | 一次拿来训练的一小组例子。 |
| batch size | 批次大小 | The number of examples processed in one batch. | 每一批里包含多少个训练例子。 |
| minibatch | 小批次 | A small batch used for an individual training update. | 每次更新参数时使用的一小批数据。 |
| epoch | 训练轮次 | One complete pass through the training dataset. | 把整个训练数据集完整看一遍。 |
| training step | 训练步 | One iteration that processes data and updates parameters. | 处理一批数据并更新一次参数的动作。 |
| iteration | 迭代 | One repetition of a training operation or loop. | 把同一类训练动作重复一次。 |
| training loop | 训练循环 | The repeated sequence of prediction, error measurement, and update. | 预测、比较错误、更新参数不断重复的循环。 |
| prediction-error-update loop | 预测—误差—更新循环 | A training loop that predicts, compares with a target, and adjusts parameters. | 先猜、再看错多少、然后改参数并重复。 |
| compare with target | 与目标比较 | Measure a prediction against the expected target. | 把模型答案和正确答案放在一起比较。 |
| adjust parameters | 调整参数 | Change learned internal values to improve predictions. | 改变模型内部数字，让下次预测更好。 |
| reduce errors | 减少错误 | Make predictions closer to their targets. | 让模型猜得越来越接近正确答案。 |
| optimization | 优化 | Searching for parameter values that improve the training objective. | 找到更合适的参数，让训练结果更好。 |
| convergence | 收敛 | Training behavior in which improvements become small or stable. | 训练到后面，模型表现趋于稳定、不再大幅变化。 |
| checkpoint | 检查点；模型检查点 | A saved snapshot of model parameters during or after training. | 把模型当前状态保存下来，方便继续或使用。 |
| saved checkpoint | 已保存检查点 | A stored model state containing learned parameter values. | 已经保存好的模型参数快照。 |
| checkpointing | 检查点保存 | Saving model states during training for recovery or selection. | 训练过程中定期保存模型状态。 |
| learned parameter values | 学到的参数值 | The parameter settings retained from training. | 训练结束后模型保留下来的内部数字。 |
| model state | 模型状态 | The parameters and related information representing a model at one point. | 模型在某个时刻的完整保存状态。 |
| save a model | 保存模型 | Store learned parameters for later use or adaptation. | 把训练好的模型记下来，之后继续使用。 |
| base-model checkpoint | 基础模型检查点 | A saved checkpoint representing a broadly pretrained model. | 预训练完成后的基础模型保存版本。 |
| model initialization | 模型初始化 | Setting the starting parameter values before training. | 训练开始前给模型内部数字设定初始值。 |
| random initialization | 随机初始化 | Starting training with randomly chosen parameter values. | 一开始用随机数字作为模型起点。 |
| compute | 计算资源；算力 | Hardware and processing capacity used to train a model. | 训练模型需要的计算能力和机器资源。 |
| accelerator | 加速器 | Specialized hardware used to speed up model training. | 专门帮助模型更快计算的硬件。 |
| GPU | 图形处理器；GPU | Parallel processor commonly used for neural-network training. | 很适合同时做大量相似计算的训练芯片。 |
| TPU | 张量处理器；TPU | Specialized processor designed for machine-learning workloads. | 专门为机器学习计算设计的处理器。 |
| compute budget | 计算预算 | The amount of compute available for a training run. | 这次训练最多能使用多少算力。 |
| data scale | 数据规模 | The size and breadth of data used for training. | 训练数据有多少、覆盖多广。 |
| model scale | 模型规模 | The size of a model, often described by parameter count. | 模型有多大，通常看参数数量。 |
| parameter count | 参数量 | The number of learned parameters in a model. | 模型内部可学习数字的总数。 |
| scaling | 扩展；规模化 | Increasing data, model, or compute to improve capability. | 同时扩大数据、模型或算力来提升能力。 |
| scaling law | 扩展定律；规模规律 | An observed relationship between scale and model performance. | 数据、参数、算力变大时效果如何变化的经验规律。 |
| data quality | 数据质量 | How accurate, relevant, diverse, and usable training data is. | 数据是否准确、相关、丰富、适合训练。 |
| data cleaning | 数据清洗 | Removing or correcting problematic training data. | 去掉或修正错误、重复、危险的数据。 |
| deduplication | 去重 | Removing repeated or near-repeated training examples. | 删除重复或几乎一样的训练材料。 |
| data filtering | 数据筛选 | Selecting training examples according to quality or safety rules. | 按质量和安全要求挑选哪些数据能进入训练。 |
| data contamination | 数据污染；测试集污染 | Unintended overlap between training data and evaluation data. | 训练时提前见过测试内容，导致评估不真实。 |
| memorization | 记忆化 | Retaining specific training examples rather than only general patterns. | 模型记住了原文细节，而不只是学会规律。 |
| generalization | 泛化 | Applying learned patterns to new, unseen examples. | 遇到没见过的新题也能用学到的规律处理。 |
| overfitting | 过拟合 | Performing well on training data but poorly on new data. | 只会背训练材料，换新例子就表现不好。 |
| underfitting | 欠拟合 | Failing to learn enough structure from the training data. | 连训练材料里的基本规律都没学好。 |
| unseen data | 未见数据 | Data not used during training. | 训练时模型没有看过的新数据。 |
| held-out data | 留出数据 | Data reserved for validation or testing rather than training. | 特意留着不训练、用来检查效果的数据。 |
| validation set | 验证集 | Data used to monitor and tune training choices. | 用来检查训练过程、调整设置的数据。 |
| test set | 测试集 | Data used to measure final performance. | 最后用来检验模型效果的数据。 |
| downstream task | 下游任务 | A later task performed with or supported by a pretrained model. | 基础模型训练完成后拿去做的具体任务。 |
| downstream application | 下游应用 | An application built on top of a pretrained model. | 建立在基础模型能力之上的实际应用。 |
| adaptation | 适配；改造 | Later changes that make a base model fit a task or use case. | 把通用模型调整到某个具体用途。 |
| model adaptation | 模型适配 | Adapting a base model for a particular domain or task. | 让基础模型适合某个领域或任务。 |
| task-specific adaptation | 面向任务的适配 | Adaptation targeted at a particular task. | 专门针对一个具体任务进行的调整。 |
| task-specific training | 任务专用训练 | Later training focused on a particular task or domain. | 针对特定任务继续训练。 |
| specialization | 专门化 | Making a general model better for a narrower use. | 把通用能力变成某个方向的专长。 |
| fine-tuning | 微调 | Later targeted training that changes a pretrained model for a task. | 在预训练后用较专门的数据继续调整模型。 |
| instruction tuning | 指令微调 | Fine-tuning on examples of instructions and desired responses. | 用“指令—回答”例子训练模型更会听话。 |
| preference learning | 偏好学习 | Learning which outputs people or a preference model favor. | 学习哪些回答更符合人的偏好。 |
| RLHF | 基于人类反馈的强化学习 | Reinforcement learning from human feedback used for later alignment. | 根据人类反馈继续训练模型的方式。 |
| prompting | 提示；提示工程 | Giving runtime instructions or context without changing model parameters. | 使用时写提示让模型按要求回答，不改模型本身。 |
| prompt | 提示词；提示 | Instructions or context given to a model at runtime. | 运行时告诉模型要做什么的输入。 |
| runtime instruction | 运行时指令 | An instruction supplied when the model is being used. | 模型已经训练好后，使用时临时给的要求。 |
| inference | 推理；推断 | Using a trained model to produce an output for new input. | 用训练好的模型处理新问题并给出结果。 |
| deployment | 部署 | Making a trained model available for real use. | 把训练好的模型放到真实系统里使用。 |
| application | 应用 | A product or workflow that uses a model. | 把模型能力放进实际产品或流程。 |
| query time | 查询时；请求时 | The time when a user request is processed. | 用户真正发出问题、系统正在回答的时刻。 |
| retrieval | 检索；召回 | Finding external information relevant to a query. | 用户提问时从外部资料里找相关内容。 |
| RAG | 检索增强生成 | Retrieval-augmented generation that brings outside information into a response. | 回答时先查外部资料，再根据资料生成答案。 |
| retrieval-augmented generation | 检索增强生成 | A method that retrieves information at query time to support generation. | 在提问时临时检索资料来辅助生成。 |
| outside information | 外部信息 | Information supplied from outside the model's learned parameters. | 模型本身之外、运行时接入的资料。 |
| learned capability | 学到的能力 | Capability encoded in model parameters through training. | 训练后存在模型内部、无需每次另查的能力。 |
| runtime knowledge | 运行时知识 | Information provided while the model is being used. | 使用模型时临时提供给它的资料。 |
| parameter change | 参数变化 | A change to learned model values during training. | 训练时模型内部数字发生改变。 |
| parameter update vs runtime instruction | 参数更新与运行时指令 | Training changes parameters; prompting changes only the current input. | 训练会改模型本身，提示只改这一次的要求。 |
| pre-training vs fine-tuning | 预训练与微调 | Broad initial training differs from later targeted training. | 预训练先学通用规律，微调再学具体任务。 |
| pre-training vs prompting | 预训练与提示 | Pre-training changes parameters; prompting supplies runtime instructions. | 预训练改模型内部，提示只是在使用时发指令。 |
| pre-training vs RAG | 预训练与 RAG | Pre-training builds learned capability; RAG retrieves outside information at query time. | 预训练把能力学进模型，RAG 是提问时临时查资料。 |
| base model vs every AI model | 基础模型与所有 AI 模型 | A base model is a result or stage of pre-training, not a synonym for every AI model. | 基础模型不是所有 AI 模型的统称。 |
| broad data → pre-training → base model → adaptation | 广泛数据→预训练→基础模型→适配 | A high-level lifecycle from data to later use. | 从广泛数据训练出基础模型，再把它调整到具体用途。 |
| model building | 模型构建 | The process of creating and training a model. | 从数据、训练到保存模型的完整建造过程。 |
| training process | 训练流程 | The ordered operations used to turn data into a model. | 把数据变成模型的一连串步骤。 |
| training run | 训练运行 | One configured execution of a training process. | 按一套设置实际跑完的一次训练。 |
| pretraining corpus | 预训练语料 | The broad corpus used for initial model training. | 用来做初始通用训练的大批材料。 |
| pretraining objective | 预训练目标 | The objective used to learn general representations or token prediction. | 预训练阶段要求模型尽量完成的学习任务。 |
| representation | 表示；表征 | An internal form that encodes useful information. | 模型内部表达文字或其他信息的方式。 |
| learned representation | 学到的表征 | An internal representation formed from training data. | 模型从数据中学会、保存在内部的表达方式。 |
| latent representation | 潜在表示 | An internal representation not directly visible in the raw input. | 不是原始文字本身、但藏在模型内部的表示。 |
| feature | 特征 | An informative property used to represent an input. | 数据里对判断有用的某种属性。 |
| pattern learning | 模式学习 | Learning recurring relationships from examples. | 从例子里找出反复出现的关系。 |
| statistical pattern | 统计模式 | A regular relationship reflected in data frequencies or probabilities. | 数据中通过频率和概率体现出来的规律。 |
| probability | 概率 | A numerical estimate of how likely an outcome is. | 某个结果出现可能性的数字。 |
| token probability | 词元概率 | The model's estimated likelihood for a token. | 模型认为某个词元接下来出现的可能性。 |
| probability distribution | 概率分布 | Probabilities assigned across possible next tokens or outcomes. | 把可能结果及其可能性整体列出来。 |
| softmax | Softmax；归一化指数函数 | A function commonly used to turn scores into probabilities. | 把多个分数变成总和为一的可能性。 |
| vocabulary | 词表 | The set of tokens a language model can represent. | 模型认识和处理的词元全集。 |
| vocabulary size | 词表大小 | The number of tokens in a model's vocabulary. | 模型词表里一共有多少个词元。 |
| sequence | 序列 | An ordered set of tokens or data units. | 按顺序排列的一串数据单位。 |
| sequence modeling | 序列建模 | Learning patterns in ordered data such as text. | 学习文字等有先后顺序的数据规律。 |
| neural network | 神经网络 | A layered learned function used to transform inputs. | 由多层可学习计算单元组成的模型。 |
| transformer | Transformer | A neural-network architecture commonly used for modern language models. | 现代语言模型常用的一种神经网络结构。 |
| attention | 注意力机制 | A mechanism that weighs relevant parts of the input. | 模型判断前文哪些部分更值得重点参考的机制。 |
| self-attention | 自注意力 | Attention in which tokens compare with other tokens in the same sequence. | 句子里的词元互相参考、判断彼此关系。 |
| embedding | 嵌入；向量表示 | A numerical vector representation of a token or input. | 把词元变成一串数字，方便模型计算。 |
| positional encoding | 位置编码 | Information that represents token order in a sequence. | 告诉模型每个词元在句子里的位置。 |
| layer | 层 | One stage of a neural network transformation. | 神经网络逐步处理信息的一层。 |
| forward pass | 前向传播 | Computing a prediction by passing data through the model. | 把数据从模型前面传到后面得到预测。 |
| backward pass | 反向传播过程 | Computing updates from the prediction error back through the model. | 从错误结果倒着计算各层该怎么改。 |
| training objective vs evaluation metric | 训练目标与评估指标 | The optimized objective may differ from the metrics used to judge usefulness. | 训练时优化的数字，不一定等于最后评价模型的数字。 |
| training data scale | 训练数据规模 | The amount of data used during pre-training. | 预训练时到底用了多少资料。 |
| training duration | 训练时长 | How long a training run continues. | 这次训练持续了多久。 |
| throughput | 吞吐量 | The amount of data or tokens processed per unit time. | 每秒或每分钟能处理多少数据。 |
| tokens per second | 每秒词元数 | The number of tokens processed in one second. | 一秒钟训练或处理多少词元。 |
| sample efficiency | 样本效率 | How much useful learning is obtained from a given amount of data. | 用同样多的数据能学到多少有效能力。 |
| compute efficiency | 计算效率 | How much capability or progress is obtained per unit of compute. | 用同样算力能取得多少训练效果。 |
| training stability | 训练稳定性 | Whether training progresses without diverging or becoming erratic. | 训练是否平稳，不突然发散或失控。 |
| reproducibility | 可复现性 | The ability to obtain comparable results by repeating training conditions. | 条件相近时能否重新得到类似结果。 |
| data leakage | 数据泄漏 | Evaluation or future information unintentionally entering training. | 不该提前看到的资料意外进入训练。 |
| copyright risk | 版权风险 | The risk that training or outputs involve protected content improperly. | 训练材料或生成结果可能带来的版权问题。 |
| privacy risk | 隐私风险 | The risk of exposing sensitive information through data or memorization. | 训练数据或模型可能泄露个人敏感信息。 |
| safety filtering | 安全筛选 | Removing or controlling harmful training material. | 把有害内容筛掉或限制进入训练。 |
| alignment | 对齐 | Shaping a model's behavior to match human goals or constraints. | 让模型的行为更符合人的目标和安全要求。 |
| post-training | 后训练 | Training performed after pre-training, such as fine-tuning or alignment. | 预训练之后继续进行的各种训练。 |
| pretrained model | 预训练模型 | A model that has already undergone broad initial training. | 已经做过通用初始训练的模型。 |
| pretrained weights | 预训练权重 | Parameters learned during pre-training. | 预训练阶段学到并保存下来的权重。 |
| pretrained checkpoint | 预训练检查点 | A saved state of a pretrained model. | 保存好的预训练模型版本。 |
| model ready for adaptation | 可适配模型 | A base model prepared for later task-specific use. | 已经学好通用规律、可以继续适配具体任务的模型。 |
| model ready for deployment | 可部署模型 | A model prepared for use in an application. | 已经达到可以放进实际系统使用的状态。 |
| general capability before specialization | 专业化前的通用能力 | Broad ability learned before narrower task training. | 在专门做某件事前先拥有的通用本领。 |
| learned capability before deployment | 部署前学到的能力 | Capability encoded before the model is used in production. | 模型上线前已经学进内部的能力。 |
| application readiness | 应用就绪度 | Whether a model is ready to support a real application. | 模型是否已经准备好放进实际应用。 |

## Potential Missing Concepts

- `pre-training.html` explains the high-level prediction–error–parameter-update loop but does not name the usual mathematical loss functions, gradients, backpropagation, optimizers, learning rate, batches, epochs, or convergence.
- It mentions text, code, images, and “other data” but does not specify multimodal pre-training, audio, video, speech, vision encoders, or modality-specific tokenizers.
- It describes missing or next-token prediction but does not explicitly distinguish autoregressive/causal language modeling from masked language modeling.
- It says “large datasets” and “broad patterns” but does not define corpus construction, quality filtering, deduplication, data mixture, contamination, privacy, copyright, or safety filtering.
- It says prediction is “measured against the training example” but does not name cross-entropy, perplexity, token accuracy, calibration, or other training/evaluation metrics.
- It mentions a saved checkpoint but does not explain checkpoint selection, resuming, distributed training, sharding, parallelism, or fault recovery.
- It says “adjust parameters” but does not explain weights, gradients, optimizer state, initialization, numerical precision, or parameter counts.
- It describes a base model that can later be “prompted or adapted” but does not define post-training, instruction tuning, preference learning, RLHF, alignment, or safety tuning in detail.
- It contrasts pre-training with RAG but does not describe retrieval indexes, embeddings, vector search, reranking, grounding, or context assembly.
- It uses “language model” and “LLM” as related concepts but does not explain Transformer layers, attention, self-attention, embeddings, positional information, or context windows.
- It does not state train/validation/test splits, held-out evaluation, generalization, overfitting, memorization, or data leakage, although these are important for judging whether broad learning is real.
- It does not give concrete scale, compute, throughput, training-duration, energy, cost, or hardware details.
- It does not discuss preprocessing details such as normalization, filtering, document boundaries, sequence packing, or sample weighting.

## Aliases / Synonyms

- Pre-training / pretraining / initial training / broad initial training
- Base model / pretrained base model / pretrained model / foundation model / model foundation
- Training data / pretraining data / training corpus / pretraining corpus / dataset
- Next-token prediction / next token prediction / autoregressive prediction / causal language modeling
- Missing-token prediction / masked-token prediction / masked language modeling
- Token / text unit / subword unit / wordpiece (related tokenizer unit)
- Parameter / learned parameter / parameter value / weight / model weight
- Error / prediction error / loss signal / training loss (related, not always identical)
- Checkpoint / saved checkpoint / model snapshot / pretrained checkpoint
- Adaptation / model adaptation / downstream adaptation / task-specific adaptation
- Fine-tuning / targeted training / task-specific training (related but not identical)
- Prompting / runtime instruction / in-context instruction (related use-time concepts)
- RAG / retrieval-augmented generation / retrieval-enhanced generation
- Generalization / performance on unseen data / transfer to downstream tasks
- Large language model / LLM / language model (not all language models are large)
- Self-supervised learning / label-free pretraining (often used as a practical description)
- Loss / objective value / training error (related terms with different technical meanings)

## Do Not Confuse Candidates

- Pre-training ≠ fine-tuning: pre-training learns broad patterns first; fine-tuning is later, narrower training.
- Pre-training ≠ prompting: pre-training changes model parameters; prompting changes the runtime input or instructions.
- Pre-training ≠ RAG: pre-training builds capability into parameters; RAG retrieves outside information at query time.
- Base model ≠ every AI model: a base model is a broadly pretrained result intended for later use or adaptation.
- Training data ≠ inference input: training data teaches the model; inference input is supplied when the model is being used.
- Training example ≠ target: an example may contain input and target; the target is the expected answer or continuation used for comparison.
- Token ≠ word: one word can be split into multiple tokens, and a token can be smaller or larger than a word.
- Tokenization ≠ training: tokenization prepares units; training changes parameters from examples.
- Prediction ≠ generation: prediction estimates a missing or next unit; generation repeatedly predicts units to produce a sequence.
- Parameter ≠ hyperparameter: a parameter is learned during training; a hyperparameter such as learning rate is selected to control training.
- Parameter update ≠ model output: an update changes the model internally; an output is the result returned for an input.
- Loss ≠ accuracy: loss is an optimization signal; accuracy is one possible evaluation measure.
- Loss ≠ error in every sense: loss is a chosen formula, while “error” is the broader mismatch concept.
- Checkpoint ≠ final model: a checkpoint is any saved state and may be intermediate or selected later.
- Pretrained model ≠ deployed model: a model can be pretrained but not yet packaged, evaluated, or served in production.
- Generalization ≠ memorization: generalization transfers patterns to new data; memorization retains specific examples.
- Broad data ≠ high-quality data: more varied data can help, but quality, duplication, contamination, and safety still matter.
- Self-supervised learning ≠ no objective: it uses targets derived from the data itself and still optimizes a defined objective.
- Unsupervised learning ≠ next-token prediction in every case: next-token prediction is one self-supervised objective, not the definition of all unsupervised learning.
- Foundation model ≠ language model: foundation models may be trained for language, vision, audio, or multiple modalities.
- LLM ≠ every Transformer: LLMs are large language models; Transformer is an architecture that can be used for more than language.
- Query-time retrieval ≠ new pre-training: retrieving a document at runtime does not update the model's parameters.
- Adaptation ≠ deployment: adaptation changes or configures a model for a use; deployment makes it available to users or systems.
- Training metric ≠ product metric: a low training loss does not by itself prove usefulness, safety, or business value.

## Notes

- This is intentionally an expansive raw candidate inventory, not a deduplicated final glossary. Repeated ideas are retained where the page presents them as distinct wording or contrast.
- The source page directly covers the definition, broad data, tokenization, missing/next-token prediction, error comparison, parameter updates, base models, checkpoints, and contrasts with fine-tuning, prompting, and RAG.
- Technical candidates such as gradient descent, backpropagation, Transformer, attention, cross-entropy, perplexity, data quality, and evaluation splits are included because they are standard concepts strongly implied by the training workflow or useful for a complete Pre-training glossary; they are flagged as missing when not explicitly named by the page.
- The page's analogy terms (“general education,” “specialist training,” “student,” “subjects,” and “job”) are retained as explanatory candidates where they clarify the broad-training-versus-specialization distinction.
- The page's examples include “The trader closed the position because it was risky,” a mixed dataset, and a saved checkpoint; these examples motivate the candidate terms next token, continuation, broad patterns, learned parameter values, and model ready for adaptation.
- “Pre-training” and “pretraining” are orthographic variants. “Loss,” “error,” “objective,” and “metric” are related but should remain separate in a final glossary unless the final editorial pass intentionally merges them.
