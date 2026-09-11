# Parameters

- Module: 02 · LLMs & Transformers
- Topic: Parameters
- Source File: `parameters.html`

## Glossary Candidates

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Parameters | 参数 | Learned numerical values inside an AI model | AI 模型内部通过学习得到的数字值 |
| parameters | 参数 | Numerical values learned during training | 训练时学出来的一组数字 |
| learned numerical values | 学习得到的数值 | Numbers adjusted by learning from data | 模型从数据中学会并不断调整的数字 |
| AI model | AI 模型 | A system that learns patterns and produces results | 能从数据中学规律并输出结果的系统 |
| model | 模型 | A learned system that processes inputs | 学会规律后处理输入的系统 |
| model parameters | 模型参数 | Learned values belonging to a model | 属于模型的学习所得数值 |
| parameter value | 参数值 | One learned numerical setting | 一个学到的数字设置 |
| numerical value | 数值 | A value represented by a number | 用数字表示的值 |
| numerical setting | 数字设置 | A number that influences model behavior | 会影响模型行为的数字设置 |
| inside an AI model | AI 模型内部 | Located within the model | 存在于模型内部 |
| training | 训练 | Adjusting a model by learning from examples | 让模型从示例中学习和调整的过程 |
| train | 训练模型 | Make a model learn from data | 用数据让模型学会规律 |
| training adjusts values | 训练调整数值 | Learning changes parameter values | 训练会改变参数值 |
| adjustment | 调整 | A change made to a value | 对数值进行改变 |
| task | 任务 | The job a model is expected to perform | 模型要完成的工作 |
| parameter count | 参数量 | The number of parameters in a model | 模型里参数的数量 |
| model capacity | 模型容量 | How much complexity a model can represent | 模型能表示多复杂规律的能力 |
| capacity | 容量 / 能力 | The amount of complexity a system can handle | 系统能承载和表达的复杂程度 |
| complete list of facts | 完整事实清单 | An explicit list of stored facts | 明确存放在里面的事实清单 |
| fact | 事实 | A piece of information considered true | 一条被认为正确的信息 |
| parameter count describes capacity | 参数量描述容量 | Count indicates potential scale, not every fact | 参数量说明模型规模潜力，不是事实目录 |
| learned settings | 学习得到的设置 | Settings learned from examples | 从示例中学出的设置 |
| tiny settings | 微小设置 | Many small values that jointly affect behavior | 大量一起起作用的小数字设置 |
| machine | 机器 | A system carrying out a process | 执行过程的系统 |
| final settings | 最终设置 | Parameter values after training | 训练完成后的参数值 |
| inference | 推理 | Using fixed trained values to produce an output | 用训练好的固定参数生成结果 |
| trained values | 训练后的数值 | Values obtained after learning | 学习完成后留下的数值 |
| output | 输出 | The result produced by a model | 模型产生的结果 |
| input | 输入 | Information given to a model | 交给模型处理的信息 |
| response | 响应 | A result returned for an input | 针对输入返回的结果 |
| model behavior | 模型行为 | How a model responds or acts | 模型面对输入时的表现 |
| shape a response | 影响响应 | Influence how the model responds | 影响模型怎样回答 |
| produce a result | 产生结果 | Generate an output from an input | 根据输入得到输出 |
| expected result | 预期结果 | The target output used for comparison | 用来比较的目标答案 |
| target | 目标 | The expected answer for an example | 示例中希望得到的答案 |
| training example | 训练示例 | An input-result pair used for learning | 用于学习的一组输入和结果 |
| example | 示例 | One case shown to the model | 展示给模型的一条例子 |
| prediction | 预测 | An output produced using current settings | 模型用当前参数给出的结果 |
| current settings | 当前设置 | Parameter values at the present training step | 当前训练阶段正在使用的参数值 |
| compare | 比较 | Check an output against a target | 把输出和目标答案放在一起检查 |
| error | 误差 | The difference between output and target | 输出和目标之间的差距 |
| measure error | 衡量误差 | Quantify how far a prediction is from the target | 计算预测离目标有多远 |
| error measurement | 误差度量 | A numerical assessment of prediction error | 用数字表示预测错误程度 |
| update | 更新 | Change values based on measured error | 根据误差改变参数 |
| parameter update | 参数更新 | A change to learned values during training | 训练中对参数值的一次改变 |
| adjust values | 调整数值 | Change numerical settings slightly | 小幅改变数字设置 |
| optimizer | 优化器 | A method that changes parameters during training | 训练时负责更新参数的方法 |
| optimization | 优化 | Improving settings based on error | 根据误差逐步改进参数 |
| optimizer changes parameters | 优化器改变参数 | The optimizer updates many values | 优化器一次更新许多参数 |
| slightly | 小幅地 | By a small amount | 每次只改变一点点 |
| many parameters | 大量参数 | A large collection of learned values | 很多一起工作的参数 |
| training loop | 训练循环 | Repeated example, prediction, comparison, and update steps | 反复示例、预测、比较、更新的过程 |
| process | 流程 | An ordered series of steps | 按顺序进行的一系列步骤 |
| show a target | 提供目标 | Give the model an expected result | 给模型一个应达到的答案 |
| try current settings | 尝试当前设置 | Produce an output with present values | 用当前参数试着输出结果 |
| adjust parameters | 调整参数 | Change learned values to reduce error | 改变参数以减少误差 |
| use the model | 使用模型 | Apply the trained system to a task | 把训练好的系统用于任务 |
| new input | 新输入 | Input not used in exactly the same form during training | 模型要处理的新数据 |
| learned model | 已学习模型 | A model whose values were learned from data | 已经从数据中学到参数的模型 |
| language model | 语言模型 | A model that processes or generates language | 处理或生成语言的模型 |
| next token | 下一个 token | The next text unit predicted in a sequence | 文本序列中模型要预测的下一个单位 |
| next-token prediction | 下一个 token 预测 | Predicting what text unit comes next | 预测接下来出现哪个文字单位 |
| The sky is | “天空是” | An example prompt fragment | 用来测试续写的输入片段 |
| possible continuations | 可能的续写 | Candidate text that could follow an input | 输入后可能接上的文字 |
| score possible continuations | 为可能续写打分 | Assign scores to candidate next tokens | 给不同续写候选计算分数 |
| likely next token | 可能性较高的下一个 token | The candidate with high predicted likelihood | 模型认为最可能接下来的文字单位 |
| blue | 蓝色 | An example predicted continuation | “天空是蓝色”的续写示例 |
| image model | 图像模型 | A model that processes or interprets images | 处理或理解图像的模型 |
| label | 标签 / 类别名 | A name assigned to an input such as an image | 给图片等输入起的类别名称 |
| photo | 照片 | An image used as model input | 作为模型输入的一张图片 |
| visual relationships | 视觉关系 | Learned relationships among visual patterns | 图像模式之间学到的关系 |
| learned visual relationships | 学到的视觉关系 | Visual patterns represented through training | 训练后模型掌握的视觉模式联系 |
| object label | 物体标签 | A label naming an object in an image | 说明图片里是什么物体的类别名 |
| fine-tuning | 微调 | Additional training that adapts a model | 在已有模型上继续训练以适应新目标 |
| style | 风格 | A consistent way of writing or responding | 写作或回答时保持的一种风格 |
| writing request | 写作请求 | An instruction asking for written output | 要求模型写东西的输入 |
| targeted training | 针对性训练 | Training aimed at selected behavior | 针对特定行为进行的训练 |
| selected values | 选定的数值 | A subset of values chosen for updating | 被挑出来更新的一部分参数 |
| adapter | 适配器 | A small trainable component used to adapt a model | 用来适配模型的小型可训练组件 |
| adapters | 适配器组件 | Added components that modify model behavior | 加到模型上的行为调整组件 |
| consistent style | 一致的风格 | Similar style across generated outputs | 多次输出保持相近的表达风格 |
| parameters are not tokens | 参数不等于 token | Parameters are learned values, tokens are processed units | 参数是学到的数值，token 是处理的文字单位 |
| token | token / 词元 | An input or output unit processed by a model | 模型处理的一小段文字或符号 |
| input unit | 输入单位 | One unit of model input | 输入内容被切分后的一小单位 |
| output unit | 输出单位 | One unit produced by a model | 模型生成的一小单位 |
| knowledge database | 知识数据库 | Explicit records stored for retrieval | 可以直接检索的明确记录集合 |
| database | 数据库 | A structured store of records | 存放记录的数据系统 |
| explicit records | 明确记录 | Information stored as identifiable entries | 一条条可以明确找到的记录 |
| retrieval | 检索 | Find stored information for use | 从存储中找出信息 |
| statistical relationships | 统计关系 | Patterns of association encoded in values | 参数中编码的统计关联模式 |
| encoded | 编码的 | Represented inside a system | 以某种形式存在于系统内部 |
| more parameters | 更多参数 | A model with a larger number of learned values | 参数数量更多的模型 |
| model quality | 模型质量 | How well a model performs its task | 模型完成任务的好坏 |
| data quality | 数据质量 | How useful and reliable the training data is | 训练数据是否可靠、合适 |
| architecture | 架构 | The design and arrangement of a model | 模型内部结构和组织方式 |
| task fit | 任务适配度 | How suitable a model is for a task | 模型是否适合要完成的任务 |
| context | 上下文 | Information surrounding the current input | 当前输入周围的相关信息 |
| model context | 模型上下文 | Context available to the model while responding | 模型回答时能看到的上下文 |
| external memory | 外部记忆 | Information kept outside the model parameters | 存在模型参数之外的信息 |
| parameter memory | 参数记忆 | Information-like patterns encoded in parameters | 以参数形式留下的模式信息 |
| trained model | 训练好的模型 | A model after its parameters have been learned | 参数学习完成后的模型 |
| training data | 训练数据 | Data used to learn parameters | 用来学习参数的数据 |
| parameter space | 参数空间 | The space of possible parameter settings | 所有可能参数组合组成的空间 |
| parameter initialization | 参数初始化 | Choosing starting parameter values | 训练开始前给参数设定初始值 |
| parameter update rule | 参数更新规则 | The rule used to change parameter values | 决定每次怎样改参数的规则 |
| learned relationship | 学到的关系 | A relationship inferred from training examples | 从训练示例中学出来的联系 |
| model capacity versus knowledge | 模型容量与知识 | Capacity is not the same as an explicit fact store | 模型能装多复杂规律不等于存着事实清单 |
| fixed during inference | 推理期间固定 | Values are not updated while producing an output | 生成回答时参数通常不再训练改变 |
| trainable values | 可训练数值 | Values allowed to change during training | 训练中可以被更新的参数 |
| frozen values | 冻结数值 | Values kept unchanged during adaptation | 微调时保持不变的参数 |
| weight | 权重 | A learned value that scales a signal | 控制信号影响大小的学习数值 |
| bias | 偏置 | A learned offset added to a calculation | 加到计算结果上的学习偏移量 |
| learned weight | 学习权重 | A weight adjusted from data | 从数据中学到的权重 |
| parameter count metric | 参数量指标 | A size measure based on number of parameters | 用参数数量衡量模型规模的指标 |
| model size | 模型规模 | The overall size of a model, often related to parameters | 通常和参数数量相关的模型大小 |
| capacity metric | 容量指标 | A measure used to describe representational capacity | 描述模型表达复杂规律能力的指标 |
| quality metric | 质量指标 | A measure of task performance | 衡量任务表现的数值 |
| statistical model | 统计模型 | A model representing learned statistical patterns | 表示学到的统计规律的模型 |
| parameterized system | 参数化系统 | A system whose behavior is controlled by numerical parameters | 行为由数字参数控制的系统 |
| model response | 模型响应 | The model's output for a prompt or input | 模型针对输入给出的回答 |
| prompt | 提示 / 输入 | Text or data given to a model | 交给模型的文字或数据 |
| input-output pair | 输入输出对 | An input together with its expected result | 输入和对应目标结果的一对数据 |
| target output | 目标输出 | The output used as the expected answer | 训练时作为标准的输出 |
| loss | 损失 | A value measuring how wrong an output is | 表示模型输出有多不准确的数值 |
| loss function | 损失函数 | A function that computes prediction error | 计算预测误差的函数 |
| gradient | 梯度 | A direction indicating how parameters should change | 指示参数往哪个方向调整的数学量 |
| gradient descent | 梯度下降 | An optimization method that reduces loss step by step | 一步步降低损失的优化方法 |
| backpropagation | 反向传播 | Computing how output error relates to parameters | 把输出误差传回各参数以便更新 |
| learning rate | 学习率 | The step size used for parameter updates | 每次参数改变幅度的大小 |
| optimization algorithm | 优化算法 | An algorithm for finding better parameter values | 寻找更好参数值的算法 |
| training step | 训练步 | One update cycle in training | 训练中进行一次计算和更新 |
| epoch | 训练轮次 | One pass through the training data | 把训练数据完整看一遍 |
| parameter-efficient fine-tuning | 参数高效微调 | Adaptation that updates only a small part of parameters | 只更新少量参数的微调方式 |
| LoRA | LoRA / 低秩适配 | A parameter-efficient adapter method | 一种用小型低秩组件适配模型的方法 |
| low-rank adapter | 低秩适配器 | A compact adapter using low-rank updates | 用低秩更新减少可训练参数的适配器 |
| full fine-tuning | 全量微调 | Updating most or all model parameters | 更新模型大部分或全部参数 |
| quantization | 量化 | Representing values with lower numerical precision | 用更少位数表示参数以节省空间 |
| checkpoint | 检查点 / 模型快照 | A saved set of model parameters | 保存下来的一组模型参数 |
| parameter file | 参数文件 | A file storing model values | 存储模型参数的文件 |
| parameter tensor | 参数张量 | A multidimensional array of learned values | 按多维数组存储的一组参数 |
| tensor | 张量 | A multidimensional numerical array | 多维数字数组 |
| parameter precision | 参数精度 | The numerical precision used to store values | 存储参数时使用的数值精细程度 |
| generalization | 泛化 | Performing well on new inputs | 面对新输入也能表现良好 |
| overfitting | 过拟合 | Learning training examples too specifically | 只记住训练数据，遇到新数据表现变差 |
| scaling law | 缩放定律 | A relationship between scale and performance | 模型规模与表现之间的经验关系 |
| compute | 计算量 | Computational resources used by training or inference | 训练或推理要消耗的计算资源 |
| memory footprint | 内存占用 | Storage needed for model parameters | 存放模型参数所需的内存空间 |
| parameter-efficient | 参数高效的 | Requiring fewer trainable parameters | 用较少可训练参数完成适配 |

## Potential Missing Concepts

- Weights, biases, trainable parameters, frozen parameters, parameter tensors, parameter matrices, and parameter vectors: the page says numerical values but does not name common parameter components or storage shapes.
- Loss function, objective function, loss value, error signal, gradient, backpropagation, gradient descent, learning rate, momentum, Adam, and stochastic gradient descent: the page names comparison, error, and optimizer but omits the usual optimization mechanics.
- Initialization, random initialization, seed, convergence, training step, batch, epoch, minibatch, and checkpoint: operational training concepts needed to explain how values are repeatedly updated and saved.
- Hyperparameters versus parameters: learning rate, batch size, number of layers, optimizer choice, and regularization settings are selected controls rather than learned values.
- Full fine-tuning, parameter-efficient fine-tuning, frozen layers, adapter layers, LoRA, low-rank update, and prefix tuning: the page mentions selected values or adapters without naming adaptation methods.
- Quantization, floating-point precision, FP32, FP16, BF16, INT8, memory footprint, and model file size: important ways parameter storage affects deployment.
- Parameter sharing, tied embeddings, sparse parameters, pruning, sparsity, and mixture-of-experts routing: architectural mechanisms that change how many distinct values are stored or used.
- Activation, hidden state, intermediate representation, logits, probability, and context window: runtime values and context that should not be confused with learned parameters.
- Architecture, layers, neurons, weights, biases, embeddings, attention matrices, and feed-forward matrices: structural parts that contain or use parameters.
- Model size, parameter count, compute, FLOPs, latency, throughput, and memory bandwidth: deployment and scaling metrics related to parameter count but not identical to it.
- Generalization, overfitting, underfitting, regularization, dropout, weight decay, validation set, and test set: concepts needed to explain why more parameters do not always improve quality.
- Scaling laws, emergent capabilities, model capacity, data quality, data quantity, and task fit: factors affecting the relationship between parameter count and model performance.
- Knowledge storage, memorization, factual recall, distributed representation, and catastrophic forgetting: deeper explanations of what parameters can encode and what fine-tuning can change.
- Training mode, evaluation mode, inference mode, frozen weights, and gradient tracking: distinctions needed to explain why inference keeps learned values fixed.
- Checkpoint loading, model serialization, state dictionary, versioning, reproducibility, and experiment tracking: practical management of learned parameter states.
- Parameter count notation such as K, M, B, and T, along with billion-parameter model naming: common abbreviations and scale conventions absent from the page.
- Next-token probability, logits, softmax, sampling, temperature, and decoding: language-model mechanisms related to how parameters score candidate continuations.
- Image features, convolution kernels, vision embeddings, classification head, and object recognition: model-specific parameter uses behind the image-label example.
- Adapter weights, base model, task head, instruction tuning, and style transfer: additional terminology for the fine-tuning and style example.
- Training loss, validation loss, accuracy, perplexity, F1, precision, recall, and calibration: metrics that assess learned behavior rather than parameter count itself.
- Parameter count versus effective capacity, active parameters, total parameters, and expert parameters: distinctions especially relevant to sparse or routed models.
- Model weights versus external memory, retrieval-augmented generation, context injection, and knowledge database: mechanisms that provide information without changing parameters.

## Aliases / Synonyms

- Parameters / model parameters / learned parameters / trainable values / learned numerical values
- Parameter value / learned value / numerical value / numerical setting / learned setting
- Parameter count / number of parameters / parameter total / model parameter size
- Model capacity / representational capacity / expressive capacity / capacity
- Weight / model weight / learned weight / weight parameter
- Bias / bias parameter / learned offset
- Training / model training / parameter learning / fitting / optimization
- Inference / model inference / prediction-time computation / serving-time computation
- Optimizer / optimization algorithm / parameter update method
- Parameter update / weight update / gradient update / learned-value update
- Error / prediction error / loss / loss value / error signal
- Target / expected result / expected output / ground-truth output / reference answer
- Input / prompt / example input / model input
- Output / prediction / response / generated result
- Language model / text model / generative language model
- Next token / next text unit / following token / predicted continuation
- Image model / vision model / visual model
- Label / class label / object label / category name
- Fine-tuning / model adaptation / additional training / task adaptation
- Adapter / adapter module / adaptation layer / parameter-efficient adapter
- Full fine-tuning / full-parameter tuning / updating all weights
- Parameter-efficient fine-tuning / PEFT / efficient adaptation / partial-parameter tuning
- Knowledge database / explicit knowledge store / retrieval database / external fact store
- Context / model context / prompt context / context window contents
- External memory / external knowledge / non-parameter memory
- Fixed parameters / frozen parameters / non-updated parameters
- Parameter tensor / tensor of parameters / parameter array / weight tensor
- Model size / parameter scale / parameter-count scale
- Trainable parameter / learnable parameter / updateable parameter

## Do Not Confuse Candidates

- Parameters vs tokens: parameters are learned numerical values inside a model; tokens are input or output units processed by the model.
- Parameters vs knowledge database: parameters encode statistical relationships in learned values; a knowledge database stores explicit records for retrieval.
- Parameters vs context: parameters are persistent learned values; context is information supplied around the current input.
- Parameters vs external memory: external memory is stored outside the model parameters and can be retrieved or injected at runtime.
- Parameter count vs knowledge amount: a larger count describes capacity or scale, not a complete list of facts the model knows.
- Parameter count vs model quality: more parameters can increase capacity, but quality also depends on data, training, architecture, and task fit.
- Parameters vs architecture: parameters are learned numerical values; architecture is the design that determines how those values are arranged and used.
- Parameters vs hyperparameters: parameters are learned during training; hyperparameters such as learning rate or layer count are selected controls.
- Parameters vs activations: parameters are persistent learned values; activations are temporary values computed for a particular input.
- Parameters vs hidden states: hidden states are input-dependent runtime representations, not the model's learned weights.
- Parameters vs embeddings: an embedding may be a learned parameter table or a runtime vector, so the term must be read in context.
- Weights vs biases: both can be parameters, but weights scale signals while biases provide learned offsets.
- Trainable parameters vs frozen parameters: trainable values can be updated; frozen values are held fixed during a training or adaptation stage.
- Full fine-tuning vs adapter tuning: full fine-tuning updates most or all base-model parameters; adapter tuning adds or updates a smaller component.
- Fine-tuning vs inference: fine-tuning changes learned values; inference uses the current values to produce outputs.
- Training vs inference: training compares predictions with targets and updates values; inference keeps the trained values fixed.
- Optimizer vs parameters: an optimizer is the update method; parameters are the values being updated.
- Error vs parameter: error measures a mismatch in output; a parameter is a learned value that influences the output.
- Target vs prediction: the target is the expected result; the prediction is what the current model produces.
- Parameter count vs parameter precision: count says how many values exist; precision says how finely each value is represented.
- Model size vs memory footprint: model size may refer to parameter scale or file size; memory footprint depends also on precision and runtime buffers.
- Capacity vs performance: capacity is potential representational complexity; performance is measured behavior on a task.
- Statistical relationship vs explicit record: a learned relationship is distributed in values and may not behave like a directly retrievable database row.
- Learned values vs random settings: trained parameters are adjusted from data; arbitrary random values do not generally encode useful task behavior.
- “More parameters” vs “always better”: larger models may be harder or more expensive to train and deploy and may not fit every task.
- Next-token score vs token itself: a score is a model-produced value for a candidate; the token is the candidate text unit.
- Object label vs visual relationship: a label is an output category; visual relationships are patterns represented by the image model.
- Parameter-efficient fine-tuning vs quantization: the former reduces which values are updated; the latter changes how values are represented or stored.
- Parameter count vs active parameters: sparse or routed models may have many total parameters but use only a subset for one input.
- Model parameters vs external retrieval: retrieving a current document does not necessarily update the model's learned values.

## Notes

- The source page defines Parameters as “learned numerical values inside an AI model.”
- The page explicitly says training adjusts parameter values and that parameter count describes capacity, not a complete list of facts.
- The analogy presents parameters as millions of tiny settings in a machine; training adjusts them gradually and inference uses the final settings.
- The process shown is: show a target → try current settings → compare output with target → measure error → update values with an optimizer → use the trained model for inference.
- The source uses the phrase “inference keeps them fixed,” so inference is represented as application of trained values rather than another parameter-learning phase.
- The language example is “The sky is” → parameters score possible continuations → a likely next token such as “blue.”
- The image example is a photo → learned visual relationships → an object label.
- The fine-tuning example says targeted training changes selected values or adapters to produce a more consistent style.
- The page explicitly contrasts Parameters with Tokens, Knowledge database, and the claim that more parameters are always better.
- The page states that parameters encode statistical relationships rather than explicit records in a knowledge database.
- The page links Parameters with LLM, Transformer, Pre-training, Fine-tuning, and Token; these related-topic names are retained as glossary candidates.
- The relationship map is training data → parameter updates → trained model → inference, and separately distinguishes parameters from model context and external memory.
- Raw collection intentionally preserves repeated wording, capitalization variants, source phrases, related professional terms, aliases, and potentially overlapping candidates. No deduplication or pruning was performed.
- The page includes a video section with learned values, training, and model capacity as metadata; the video itself is media context rather than a separate mechanism.
