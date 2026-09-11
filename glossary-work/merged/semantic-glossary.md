# Semantic AI Glossary

> 470 retained concepts from 24,356 all-raw rows across 108 raw files. Header artifacts were excluded before semantic review.

The glossary keeps one canonical concept per row. Case, hyphenation, plurals, abbreviations, and true aliases are consolidated, while distinct engineering concepts such as Search vs Retrieval vs Reranking, Training vs Fine-Tuning vs Inference, and Latency vs Throughput vs TTFT vs Tokens per Second remain separate.

## 01 / Artificial Intelligence

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| AI Product | AI 产品 | A product built using one or more AI systems. | 把 AI 能力包装给用户使用的产品。 |
| Artificial Intelligence (AI) | 人工智能(AI) | Technology that lets computers perform tasks that normally need human intelligence. | 让计算机完成通常需要人类理解、判断或创造力的事情。 |
| Pattern Recognition | 模式识别 | Finding meaningful regularities in data. | 从数据里找出重复或有意义的规律。 |
| Responsible AI | 负责任人工智能 | Designing and using AI with safety, fairness, and accountability. | 兼顾安全、公平、隐私和责任的 AI 实践。 |
| Search Engine | 搜索引擎 | A system that retrieves existing pages or records. | 帮你查找已经存在的网页或资料的系统。 |

## 01 / Deep Learning

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Activation | 激活值 / 激活 | A value produced by a unit after its transformation. | 某个神经单元经过计算后输出的数值。 |
| Activation Function | 激活函数 | A function that transforms a unit's input into its output. | 决定神经网络单元如何把输入变成输出的函数。 |
| Backpropagation | 反向传播 | Sending error information backward through a network to update its parameters. | 把误差信息从后往前传,帮助各层调整参数。 |
| Batch | 批次 | A group of examples processed together. | 一次放进模型一起计算的一小组样本。 |
| Batch Size | 批大小 | The number of examples processed in one batch. | 每次一起计算多少个训练样本。 |
| Bias | 偏置 | A learned offset added to a model computation. | 模型计算中用来调整基础输出的内部数字。 |
| Cross-Entropy Loss | 交叉熵损失 | A loss used especially for comparing predicted probabilities with the correct class. | 比较模型给出的类别概率和正确类别的差距。 |
| Deep Learning (DL) | 深度学习(DL) | Machine learning that uses neural networks with many layers. | 用很多层神经网络学习复杂规律的方法。 |
| Epoch | 训练轮次 | One complete pass through the training dataset. | 把整份训练资料完整看一遍。 |
| Generalization | 泛化 | Performing well on new data that was not in the training examples. | 不只会背训练题,遇到新资料也能做好。 |
| Gradient | 梯度 | A direction and rate showing how a quantity changes. | 告诉模型往哪个方向调整能让损失变化的数学信息。 |
| Gradient Descent | 梯度下降 | An optimization method that updates parameters in the direction that reduces loss. | 沿着让错误变小的方向一点点调整模型参数。 |
| Hyperparameter | 超参数 | A setting chosen before or around training, such as learning rate or batch size. | 训练前或训练过程中由人设定的控制旋钮。 |
| Learning Rate | 学习率 | The size of each parameter update. | 每次调整模型时迈多大一步。 |
| Loss Function | 损失函数 | A function that measures how far a model output is from the desired answer. | 用一个数字表示模型答得有多偏,训练会努力把它变小。 |
| Mean Squared Error (MSE) | 均方误差 | The average squared difference between predictions and targets. | 把预测差距平方后取平均的误差指标。 |
| Mini-Batch | 小批次 | A small batch used for a training update. | 用于一次更新的小批样本。 |
| Optimizer | 优化器 | A method that changes model parameters during training. | 负责按照训练反馈更新参数的算法。 |
| Overfitting | 过拟合 | Learning the training examples too closely and performing poorly on new data. | 把练习题背得太熟,换题就不会了。 |
| Underfitting | 欠拟合 | Failing to learn enough of the useful pattern in the data. | 连训练资料里的主要规律都没有学好。 |
| Weight | 权重 | A learned number that controls how strongly one signal affects another. | 决定某个输入信号影响有多大的数字。 |

## 01 / Machine Learning

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Algorithm | 算法 | A procedure for solving a problem or learning from data. | 解决问题或从数据学习的一套步骤。 |
| Data Augmentation | 数据增强 | Creating varied training examples from existing data. | 对已有样本做合理变化,生成更多训练例子。 |
| Data Contamination | 数据污染;测试集污染 | Unintended overlap between training data and evaluation data. | 训练时提前见过测试内容,导致评估不真实。 |
| Data Leakage | 数据泄漏 | Training receives information it should not have. | 不该提前看到的答案偷偷进入了训练。 |
| Data Preprocessing | 数据预处理 | Cleaning and transforming data before learning. | 训练前清洗、转换和整理数据。 |
| Data Quality | 数据质量 | How accurate, complete, consistent, and useful data is. | 数据是否准确、完整、一致、适合使用。 |
| Dataset | 数据集 | An organized collection of examples used for analysis or model development. | 按一定方式整理好、供模型学习或测试的一批数据。 |
| Feature | 特征 | A measurable property or signal used to make a prediction. | 模型用来判断问题的一项数据特征。 |
| Machine Learning (ML) | 机器学习(ML) | A way for computers to learn patterns from data and use them to make predictions or decisions. | 不把规则一条条写死,而是让系统从数据中学规律。 |
| Prediction | 预测 | A result a model estimates from an input. | 模型根据输入猜出的结果。 |
| Recommendation System | 推荐系统 | A system that ranks or suggests items for a user. | 根据用户行为推荐商品、视频或文章的系统。 |
| Self-Supervised Learning | 自监督学习 | Creating training signals from the data itself. | 不靠人工逐条标答案,而是从数据自身生成学习目标。 |
| Semi-Supervised Learning | 半监督学习 | Learning from a mix of labeled and unlabeled data. | 一部分数据有答案,另一部分没有答案。 |
| Test Set | 测试集 | Data used for a final unbiased check. | 最后验收模型、尽量不参与训练的数据。 |
| Training Data | 训练数据 | Examples used to teach a model. | 用来教模型的样本集合。 |
| Training Set | 训练集 | The portion of data used to fit a model. | 真正拿来教模型的那部分数据。 |
| Transfer Learning | 迁移学习 | Reusing knowledge learned for one task in another. | 把一个任务学到的能力迁移到新任务。 |
| Validation Set | 验证集 | Data used to choose settings and compare versions. | 用来调设置、比较模型方案的数据。 |

## 01 / Reinforcement Learning

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Reinforcement Learning (RL) | 强化学习(RL) | Learning by trying actions and using rewards or penalties as feedback. | 模型不断尝试行动,根据奖励或惩罚学会怎么做。 |

## 01 / Supervised Learning

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Classification | 分类 | Assigning an input to one or more predefined categories. | 把内容放进一个或多个预先定义的类别。 |
| Label | 标签 | The expected category or answer attached to a training example. | 训练例子旁边标注的正确类别或答案。 |
| Regression | 回归 | Predicting a numeric value rather than a category. | 预测一个数值,例如价格或温度。 |
| Supervised Learning | 监督学习 | Learning from examples that include the expected answer or label. | 训练资料里已经给了正确答案,模型照着学习。 |
| Target Variable | 目标值 | The answer the model is supposed to predict | 模型要预测的目标答案 |

## 01 / Unsupervised Learning

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Clustering | 聚类 | Grouping similar data points without predefined labels. | 把相似的数据自动分成一组组。 |
| Dimensionality Reduction | 降维 | Represent data with fewer dimensions | 用更少的维度表示数据 |
| Unsupervised Learning | 无监督学习 | Learning patterns from data without provided answer labels. | 没有标准答案,模型自己寻找数据中的结构。 |

## 02 / Attention

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Attention | 注意力机制 | A mechanism that gives more computation to the parts of an input that matter most. | 让模型在处理一句话或一张图时重点看更有用的部分。 |
| Attention Head | 注意力头 | One parallel attention subspace or computation | 多头注意力中的一个关系视角 |
| Attention Mask | 注意力掩码 | A mask controlling which positions can interact | 控制哪些位置可以互相关注的标记 |
| Attention Weight | 注意力权重 | A weight assigned to a relationship or input part | 表示模型重点参考哪部分信息的数值 |
| Cross-Attention | 交叉注意力 | Attention that connects one sequence or modality to another. | 让一类输入去关注另一类输入中的相关信息。 |
| Multi-Head Attention | 多头注意力 | Several attention operations that can focus on different relationships in parallel. | 同时用几组注意力去看不同类型的关系。 |
| Scaled Dot-Product Attention | 缩放点积注意力 | Attention based on scaled query-key dot products | 先缩放 query-key 点积再计算注意力 |
| Self-Attention | 自注意力 | Attention in which elements of a sequence compare with other elements in the same sequence. | 一句话中的每个词都可以参考同一句话里的其他词。 |

## 02 / CNN

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Convolution | 卷积 | A local operation that combines nearby input values. | 对相邻像素或信号做组合计算以发现局部模式。 |
| Convolution Kernel | 卷积滤波器 | A filter used in the convolution step. | 在卷积计算中扫描局部区域的滤波器。 |
| Convolutional Neural Network (CNN) | 卷积神经网络(CNN) | A neural network that is effective at learning local spatial patterns such as image features. | 擅长从图像局部区域学习边缘、纹理等模式的网络。 |
| Edge Detection | 边缘检测 | Detecting boundaries in visual input. | 找出图片中轮廓边界的处理。 |
| Image Classification | 图像分类 | Identify whether an image contains a cat, vehicle, or another category. | 判断图片是猫、车辆还是其他类别。 |
| Pooling | 池化 | A way to summarize nearby values and reduce spatial size. | 汇总相邻区域信息、减少表示大小的操作。 |

## 02 / Diffusion Models

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Autoencoder | 自编码器 | A model that learns to encode and reconstruct data. | 先压缩表达、再还原数据以学习表征的模型。 |
| Denoising | 去噪 | Turning noisy data into more organized data. | 把模糊、嘈杂的数据逐步变清楚。 |
| Diffusion Model | 扩散模型 | A generative model that learns to reverse a gradual noising process. | 学习把逐步加噪的数据还原成图像、声音等内容的生成模型。 |
| Generative Adversarial Network (GAN) | 生成对抗网络缩写 | Short for Generative Adversarial Network. | Generative Adversarial Network 的英文缩写。 |
| Variational Autoencoder (VAE) | 变分自编码器缩写 | Short for Variational Autoencoder. | Variational Autoencoder 的英文缩写。 |
| Vision Transformer (ViT) | 视觉 Transformer | A Transformer that processes image patches | 用 Transformer 处理图像块的架构 |

## 02 / Layers

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Hidden Layer | 隐藏层 | An internal layer between input and output. | 位于输入层和输出层之间、用户通常看不到的内部层。 |
| Layer | 层 | One stage of computation inside a neural network. | 神经网络里负责完成一段计算的一个"站点"。 |

## 02 / Neural Networks

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Computational Unit | 计算单元 | A basic unit that performs part of a computation. | 完成一小部分计算的基本单位。 |
| Deep Neural Network (DNN) | 深度神经网络 | A neural network with many processing layers. | 有很多处理层的神经网络。 |
| Feature Representation | 特征表示 | A representation of useful properties in model-ready form. | 把有用特征整理成模型可处理的形式。 |
| Feature Vector | 特征向量 | A numeric representation of multiple features. | 把多个特征排成一组数字给模型使用。 |
| Neural Network | 神经网络 | A model made of connected computational units that transform inputs into outputs. | 由许多相连计算单元组成、能从数据学习的模型。 |
| Neural Network Architecture | 神经网络架构 | A structured design for a neural network. | 神经网络内部各层和计算步骤如何组织的设计。 |
| Representation | 表示;表征 | An internal form used to represent useful information. | 模型内部用来表达信息的形式。 |

## 02 / RNN / LSTM

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Hidden State | 隐藏状态 | Internal information carried from earlier steps into later steps. | 网络内部保存的、不会直接展示给用户的上下文记忆。 |
| Long Short-Term Memory (LSTM) | 长短期记忆网络(LSTM) | A recurrent architecture designed to keep useful information over longer sequences. | 一种更擅长在较长序列中保留重要信息的循环网络。 |
| Recurrent Neural Network (RNN) | 循环神经网络(RNN) | A neural network that processes sequences while carrying information from earlier steps. | 处理序列时把前面步骤的信息带到后面的网络。 |
| Sequence Model | 序列模型 | A model designed to use order and context in data. | 会利用数据顺序和前后关系的模型。 |

## 02 / Transformer

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Decoder | 解码器 | A component that turns an internal representation into an output. | 把内部表征转换成输出的模型部分。 |
| Decoder-Only Model | 仅解码器模型 | A model that generates tokens from preceding context. | 根据前文逐步生成 token 的模型,现代 GPT 类模型常用。 |
| Encoder | 编码器 | A component that converts input into an internal representation. | 把输入转换成内部表征的模型部分。 |
| Encoder-Decoder Model | 编码器-解码器模型 | A model that encodes input and then generates output. | 先理解输入、再生成输出的模型结构。 |
| Encoder-Only Model | 仅编码器模型 | A model focused on representing or understanding input. | 主要把输入编码成表示、用于理解任务的模型。 |
| Feed-Forward Network | 前馈网络 | A network that further transforms each representation | 进一步变换每个表示的网络模块 |
| Layer Normalization | 层归一化 | Normalize activations within a layer | 对一层中的激活值进行归一化 |
| Positional Encoding | 位置编码 | Information indicating where a token occurs | 告诉模型 token 在序列中位置的信息 |
| Residual Connection | 残差连接 | A shortcut that adds an earlier representation to a later one | 把早期表示直接加回后续层的捷径 |
| Transformer | Transformer 架构 | A neural-network architecture built around attention and stacked processing blocks. | 以注意力为核心、把多个处理模块堆叠起来的网络架构。 |
| Transformer Architecture | Transformer 架构 | The Transformer design used to build models | 用来构建模型的 Transformer 设计 |
| Transformer Block | Transformer 模块 | A complete repeated unit containing attention and feed-forward processing. | 通常包含注意力和前馈处理的一组网络结构。 |
| Transformer Layer | Transformer 层 | One repeated processing block in a Transformer | Transformer 中重复堆叠的一个处理模块 |

## 03 / Foundation Models

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Base Model | 基础模型 / 底座模型 | The broadly trained model before task-specific adaptation. | 还没针对具体任务改造的通用模型底座。 |
| Checkpoint | 检查点 | A saved model state during training. | 训练过程中保存下来、可恢复的模型版本。 |
| Foundation Model | 基础模型 | A broadly trained model that can be adapted to many downstream tasks. | 先用大量通用数据训练,再拿去适配不同任务的模型。 |
| Model API | 模型 API | An API endpoint that accepts model requests. | 接收输入、返回模型结果的接口。 |
| Pre-Trained Model | 预训练模型 | A model that has completed broad initial training. | 已经完成基础训练、可以继续使用或适配的模型。 |
| Specialized Model | 专门化模型 | A model adapted for a narrower behavior or task. | 针对某项任务表现更稳定的模型。 |

## 03 / Large Language Models

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Language Model | 语言模型 | A model that estimates likely sequences of language. | 根据上下文判断哪些词或 token 更可能出现的模型。 |
| Large Language Model (LLM) | 大语言模型(LLM) | A language model trained at large scale to understand and generate text. | 用大量文字训练、能理解和生成语言的模型。 |
| Small Language Model (SLM) | 小型语言模型 | A language model with fewer parameters or lower resource needs. | 规模较小、运行资源需求较低的语言模型。 |

## 03 / Multimodal Models

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Image Captioning | 图像描述生成 | Generate a text description of an image. | 根据图片生成文字描述。 |
| Image-Text Alignment | 图文对齐 | How well an image and text correspond. | 图片和文字表达的意思是否对应。 |
| Image-Text Contrastive Learning | 图文对比学习 | Train on matching and non-matching image-text pairs. | 用匹配和不匹配的图片文字对训练。 |
| Image-to-Text | 图像转文本 | Produce text from an image. | 根据图片生成文字。 |
| Input Modality | 输入模态 | A data type accepted by a model. | 模型能够接收的一种信息形式。 |
| Modality | 模态;信息类型 | A kind of data such as text, image, audio, or video. | 一类信息形式,如文字、图片、声音或视频。 |
| Modality Fusion | 模态融合 | Combining signals from multiple modalities. | 把多个模态的信号合在一起。 |
| Multimodal Model | 多模态模型 | A model that works with more than one type of input or output, such as text, images, audio, or video. | 能同时处理文字、图片、声音或视频等不同信息类型的模型。 |
| Output Modality | 输出模态 | A data type generated by a model. | 模型能够生成的一种信息形式。 |
| Vision-Language Model (VLM) | 视觉语言模型 | A model combining visual and language understanding. | 同时理解图片和语言的模型。 |
| Visual Question Answering (VQA) | 视觉问答 | Answer questions using visual input. | 根据图片内容回答问题。 |

## 03 / Parameters

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Model Capacity | 模型容量 | How much complexity a model can represent | 模型能表示多复杂规律的能力 |
| Model Parameter | 模型参数 | A learned numeric value that determines part of a model's behavior. | 模型通过训练学出来、决定行为的一组数字。 |
| Model Size | 模型规模 | The overall size of a model, often related to parameters | 通常和参数数量相关的模型大小 |
| Parameter Count | 参数量 | The number of parameters in a model | 模型里参数的数量 |

## 03 / Scientific Models

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Scientific Foundation Model | 科学基础模型 | A broadly trained AI model for scientific data and tasks. | 在科学数据上广泛训练、可以支持多种科学任务的 AI 模型。 |
| Scientific Model | 科学模型 | A model that learns or represents patterns in scientific data. | 从科学数据中学习规律、用于表示或预测的模型。 |

## 03 / Speech Audio Models

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Audio-Language Model | 音频语言模型 | A model that connects audio and language. | 同时处理声音和文字的模型。 |
| Automatic Speech Recognition (ASR) | 语音识别 | Turning spoken audio into text. | 把人说的话听出来并写成文字。 |
| Speech Model | 语音模型 | A model for tasks involving speech. | 处理语音任务的模型。 |
| Text-to-Speech (TTS) | 文本转语音 | Turning text into spoken audio. | 把文字读成声音。 |

## 03 / Vision Foundation Models

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Optical Character Recognition (OCR) | 光学字符识别 | Read text from an image. | 从图片里识别出文字。 |
| Vision Foundation Model | 视觉基础模型 | A broadly trained model that learns reusable visual representations from large amounts of image or visual data. | 先用大量图像或视觉数据训练,再适配多个视觉任务的模型。 |

## 04 / Fine Tuning

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Fine-Tuning | 微调 | Additional training that adapts an existing model to a task, style, or domain. | 在已有模型上继续训练,让它更适合某个任务或领域。 |
| Low-Rank Adaptation (LoRA) | 低秩适配(LoRA) | A parameter-efficient fine-tuning method that learns a small low-rank update. | 不改动全部大参数,只训练一小组低秩更新来适配模型。 |
| Parameter-Efficient Fine-Tuning (PEFT) | 参数高效微调 | Adapting a model while changing only a small part of its parameters. | 只改很少一部分参数来适配模型。 |
| Supervised Fine-Tuning (SFT) | 监督微调(SFT) | Fine-tuning on examples that include desired answers or behaviors. | 用带有理想答案的例子继续训练模型。 |

## 04 / Instruction Tuning

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Instruction Tuning | 指令微调 | Training a model to follow natural-language instructions reliably. | 专门训练模型更好地理解并执行人类指令。 |

## 04 / Pre Training

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Autoregressive Modeling | 自回归模型 | A generative model that produces outputs step by step from prior outputs. | 依赖前面已经生成的内容,一步步生成后续内容的模型。 |
| Causal Language Modeling | 因果语言建模 | Training a language model to predict later tokens from earlier ones. | 只能根据前文预测后文的语言训练方式。 |
| Masked Language Modeling | 掩码语言建模 | Training by hiding tokens and predicting the hidden content. | 把句子中的词遮住,让模型猜回来。 |
| Missing-Token Prediction | 缺失词元预测 | Predicting a token hidden inside an example. | 猜出被遮住的词元。 |
| Next-Token Prediction | 下一个词元预测 | Predicting the next token in a sequence. | 预测一句话接下来最可能出现的词元。 |
| Pre-Training | 预训练 | Broad initial training on a large dataset before task-specific adaptation. | 先用大量通用资料打基础,再针对具体任务调整。 |
| Pre-Training Objective | 训练目标 | The prediction or optimization goal used during training. | 训练时规定模型要尽量做到的事情。 |
| Training | 训练 | The process of optimizing a model's learned parameters from data. | 让模型从数据中调整内部参数、逐步学会任务规律的过程。 |

## 04 / Preference Learning Rlhf

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Alignment | 对齐 | Making model behavior better match desired behavior. | 让模型做事更符合人们期望。 |
| Alignment Training | 对齐训练 | Training intended to match desired behavior. | 专门让模型行为符合目标的训练。 |
| Human Feedback | 人类反馈 | Feedback supplied by people. | 人来评价模型回答并提供意见。 |
| Preference Learning | 偏好学习 | Training a model using feedback about which outputs are more desirable. | 用"哪个结果更好"的反馈来训练模型。 |
| Preference Model | 偏好模型 | A model that predicts which output people would prefer. | 预测人们会更喜欢哪个回答的模型。 |
| Reinforcement Learning from Human Feedback (RLHF) | 基于人类反馈的强化学习(RLHF) | Using human preferences as feedback to improve a model's behavior. | 让人评价模型答案,再用这些偏好反馈改进模型。 |
| Reward Model | 奖励模型 | A model that predicts how desirable an output is. | 学习判断回答好坏的模型。 |
| Reward Signal | 奖励信号 | A signal used to reinforce some behaviors. | 用来鼓励某些行为的信号。 |
| Specification Gaming | 规范投机 | Satisfying a formal rule while missing its intended purpose. | 表面满足规则,但偏离真正意图。 |

## 04 / Training Data

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Data Curation | 数据整理与筛选 | Selecting and preparing useful data | 挑选、整理适合训练的数据 |
| Data Filtering | 数据筛选 | Selecting training examples according to quality or safety rules. | 按质量和安全要求挑选哪些数据能进入训练。 |
| Data Provenance | 数据溯源 | Information about where data came from and how it changed. | 记录数据来源以及经过哪些处理。 |
| Deduplication | 去重 | Removing repeated or near-repeated training examples. | 删除重复或几乎一样的训练材料。 |
| Label Quality | 标签质量 | How accurate and consistent labels are | 标签是否准确、统一、可靠 |
| Training Example | 训练示例 | An example used during training | 训练时给模型看的一个例子 |
| Training Pipeline | 训练流水线 | A repeatable sequence for preparing data and training | 可重复执行的数据准备和训练流程 |

## 05 / Context Window

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Context Budget | 上下文预算 | The total token space available for the operation. | 输入和输出可以共同使用的总空间。 |
| Context Length | 上下文长度 | The length of the context measured in tokens or content units. | 当前上下文包含多少 token 或内容长度。 |
| Context Overflow | 上下文溢出 | A situation where needed content exceeds available context capacity. | 要放的内容超过窗口能容纳的范围。 |
| Context Window | 上下文窗口 | The maximum amount of input and output context a model can handle at once. | 模型一次能看到和处理的文字容量上限。 |

## 05 / Inference

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Inference | 推理 | Running a trained model on an input to produce an output. | 把训练好的模型真正拿来回答问题或生成结果。 |
| Inference Pipeline | 推理管线 | The connected stages from input preparation to output. | 从准备输入、运行模型到返回结果的一串处理环节。 |
| Inference Request | 推理请求 | A request to run a trained model on supplied input. | 要求模型处理一份输入的请求。 |

## 05 / KV Cache

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Decode Phase | 解码阶段 | The phase that generates output tokens after prefill. | 缓存准备好后逐个生成输出词元的阶段。 |
| Key-Value Cache (KV Cache) | 键值缓存(KV Cache) | Cached attention information reused while generating a sequence. | 生成长回答时把已经算过的注意力信息存起来,减少重复计算。 |
| Prefill | 预填充 | The initial pass that processes the prompt and populates the cache. | 先一次性读入提示词并把缓存准备好的阶段。 |

## 05 / Next Token Prediction

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Autoregressive Generation | 自回归生成 | Generate the next token using previous tokens | 根据前面已有词元生成下一个词元 |
| Logit | logit;未归一化分数 | A raw model score before conversion to probabilities. | 转成概率前模型输出的原始分数。 |
| Softmax | softmax 函数 | A function that turns scores into normalized weights | 把分数转成总和通常为 1 的权重 |

## 05 / Sampling Temperature

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Decoding | 解码 | The process of selecting output tokens from model scores or probabilities. | 根据模型分数或概率逐步选出输出词元。 |
| Greedy Decoding | 贪心解码 | Always selecting the highest-scoring next token. | 每一步都选分数最高的 token。 |
| Sampling | 采样 | A method for choosing the next token from possible choices. | 从模型认为可能的选项里选出下一个词元的办法。 |
| Temperature | 温度参数 | A sampling setting that controls how varied or conservative model outputs are. | 调节模型回答更稳定还是更多样的参数。 |
| Top-k Sampling | Top-k 采样 | Sampling only from the k highest-scoring candidates. | 只在分数最高的 k 个候选中选择。 |
| Top-p Sampling | Top-p 采样 | Sampling from the smallest candidate set reaching probability p. | 从累计概率达到 p 的最小候选集合中采样。 |

## 05 / Token

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| End-of-Sequence Token (EOS) | 序列结束 token | A special token indicating that a sequence can end. | 表示一段 token 序列可以结束的特殊 token。 |
| Input Token | 输入 token;输入词元 | A token supplied to a model as input. | 用户输入被切分后的 token。 |
| Output Token | 输出 token;输出词元 | A token produced by a model. | 模型生成的一小段文字或符号。 |
| Token | 词元 | A small unit of text or other data that a model processes. | 模型处理文字时使用的小片段,不一定刚好等于一个汉字或单词。 |
| Token Sequence | token 序列 | An ordered sequence of tokens representing text. | 按原文顺序排列的一串 token。 |

## 05 / Tokenization

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Special Token | 特殊词元 | A reserved token with a control or structural role. | 不是普通文字、而是用于控制流程的词元。 |
| Subword Token | 子词 token | A token representing a whole word or part of a word. | 可以是完整单词,也可以只是单词的一部分。 |
| Tokenization | 词元化 | Splitting input text into the tokens a model can process. | 把文字切成模型能识别的小单位。 |
| Tokenizer | 分词器;词元分析器 | A component that divides text into token pieces. | 负责把文字切成词元的工具或组件。 |

## 06 / Context Engineering

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Context Assembly | 上下文组装 | Putting the selected context sources together before a model run. | 在模型运行前把需要的各种信息拼在一起。 |
| Context Engineering | 上下文工程 | Designing and assembling the information a model receives at runtime. | 设计模型在运行时到底看到哪些资料、以什么顺序看到。 |
| Context Grounding | 上下文依据化 | Using supplied context to anchor a model response. | 用给定上下文约束和支撑模型回答。 |

## 06 / Prompt Design

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Chain-of-Thought | 思维链 | Intermediate reasoning steps used to solve a problem. | 解决问题时中间的一连串推理步骤。 |
| In-Context Learning | 上下文学习 | Adapting behavior from examples or context in the prompt. | 不改参数,只根据当前上下文里的示例临时学习。 |
| Prompt | 提示词 | The instructions and input given to a model. | 发给模型的问题、要求和补充资料。 |
| Prompt Engineering | 提示词工程 | Designing prompts so a model is more likely to produce the desired result. | 通过设计提示词让模型更稳定地完成任务。 |
| Prompt Template | 提示模板 | A reusable structure for constructing prompts. | 可以反复套用来生成提示词的结构。 |
| User Prompt | 用户提示;用户请求 | The user's request for the current interaction. | 用户这一次发给模型的问题或要求。 |

## 06 / Structured Outputs

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| JSON | JSON 数据格式 | A text format for representing structured data with objects, arrays, and values. | 一种用文字表达字段、列表和数据值的常见格式。 |
| Output Parser | 解析器 | A component that converts formatted data into usable values. | 把格式化数据读成可使用值的程序。 |
| Output Schema | 模式;架构;结构定义 | A formal description of the fields and rules a result should follow. | 描述结果有哪些字段、什么类型、有什么规则的说明。 |
| Schema Validation | 模式验证 | Checking a result against a schema. | 按结构定义检查结果。 |
| Structured Output | 结构化输出 | Model output constrained to a predictable format such as JSON fields. | 要求模型按固定字段和格式返回结果。 |

## 06 / System Prompts

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Instruction Hierarchy | 指令层级 | An ordering of instruction sources by authority. | 不同来源指令之间的优先级关系。 |
| System Prompt | 系统提示词 | Instructions supplied by the application to set a model's role, rules, or behavior. | 应用预先给模型的身份、规则和行为要求。 |

## 07 / Audio Generation

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Audio Generation | 音频生成 | Using AI models to create new sound, speech, music, or other audio. | 用 AI 产生新的声音、语音、音乐或其他音频。 |

## 07 / Code Generation

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Code Completion | 代码补全 | Generating code that continues a partial snippet. | 接着已有代码把后面的部分补出来。 |
| Code Generation | 代码生成 | Producing source code with an AI model. | 用 AI 模型生成源代码。 |
| Code Review | 代码审查 | Human examination of code quality and risks. | 人工查看代码质量和风险。 |

## 07 / Generative Ai

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Generative AI | 生成式人工智能 | AI that creates new text, images, audio, video, code, or other content. | 能够生成新内容,而不只是分类或检索已有内容的 AI。 |
| Generative Model | 生成模型 | A model that produces new content from input. | 根据输入生成新内容的模型。 |

## 07 / Image Generation

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Image Generation | 图像生成;图片生成 | Using AI to create or transform visual content. | 用 AI 生成新图片,或修改已有图片。 |
| Image Generator | 图像生成器 | A system that creates new images. | 根据输入生成新图片的系统。 |
| Image-to-Image Generation | 图生图;图像到图像 | Generating or editing an image from an image input. | 参考一张图片生成或修改另一张图片。 |
| Inpainting | 图像修复;局部重绘 | Filling or replacing a selected area of an image. | 只修改图片中指定的一块区域。 |
| Outpainting | 外扩绘制;画面扩展 | Extending an image beyond its original boundaries. | 把图片边界向外扩展并补出新画面。 |
| Text-to-Image Generation | 文本生成图像;文生图(T2I) | A system maps text conditions to an image. | 输入文字、输出图片的生成方式。 |

## 07 / Multimodal Ai

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Multimodal AI | 多模态人工智能 | AI that works with more than one type of information. | 能处理不止一种信息形式的人工智能。 |

## 07 / Text Generation

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Conditional Generation | 条件生成 | Generation constrained or guided by an input condition. | 按给定条件生成内容。 |
| Text Generation | 文本生成 | Using an AI model to create new text | 用 AI 模型生成新的文字 |

## 07 / Video Generation

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Text-to-Video Generation | 文本到视频生成 | Video generation conditioned on text. | 由文字条件引导的视频生成。 |
| Video Generation | 视频生成 | The use of AI models to create or transform moving visual content. | 用 AI 模型生成或变换会动的视觉内容。 |

## 08 / Chunking

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Chunk | 块;分块内容 | A smaller piece of content used as a retrieval unit. | 从大资料中切出来、以后可以被找回的一小段内容。 |
| Chunking | 分块 | Splitting documents into smaller pieces for storage or retrieval. | 把长文档切成适合保存和检索的小段。 |

## 08 / Embeddings

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Embedding | 嵌入向量 | A learned numeric representation that captures useful relationships between items. | 把文字、图片等内容变成一串能比较相似度的数字。 |
| Embedding Model | 嵌入模型 | A model that converts an item into a vector. | 专门把文字、图片等变成向量的模型。 |
| Vector | 向量 | A list of numbers representing an item. | 一串按顺序排列、用来表示对象的数字。 |
| Vector Representation | 向量表示 | A representation stored as a vector. | 用一串数字表示文字、图片或其他对象。 |

## 08 / Grounding

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Citation | 引用 | A reference that points to the source supporting a claim. | 在答案旁边标出这句话依据的资料来源。 |
| Faithfulness | 忠实性 | Whether an explanation reflects the actual computation | 解释是否真实反映模型计算过程 |
| Groundedness | 依据一致性 | How well an answer is supported by its context. | 答案和给定资料是否一致、有依据。 |
| Grounding | 事实接地 | Connecting a model answer to supplied external evidence. | 让回答有外部资料依据,而不是完全凭模型记忆生成。 |
| Source Attribution | 来源归因 | Identifying which source contributed to an answer. | 说明回答中哪些内容来自哪个来源。 |

## 08 / Rag

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Context Retrieval | 上下文检索 | Retrieving information to place into the context. | 为当前窗口寻找并加入相关资料。 |
| Document Corpus | 来源集合;资料集合 | A collection searched for useful information. | 系统用来查找资料的一大批来源。 |
| Knowledge Base | 知识库 | An organized collection of information for retrieval. | 集中保存、供系统查找的知识资料。 |
| Retrieval-Augmented Generation (RAG) | 检索增强生成(RAG) | A system that retrieves information and gives it to a model before the model answers. | 先查资料,再把资料交给模型回答。 |

## 08 / Reranking

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Bi-Encoder | 双编码器 | A model that encodes query and items separately for efficient retrieval. | 分别编码问题和内容、适合快速检索的模型。 |
| Cross-Encoder | 交叉编码器 | A model that reads a query and candidate together to score relevance. | 把问题和候选内容一起读后再打相关性分的模型。 |
| Reranker | 重排序器;重排模型 | A component that examines candidates and orders them again. | 专门检查候选结果并重新排序的组件或模型。 |
| Reranking | 重排序 | Reordering retrieved results with a stronger relevance model. | 先找出候选资料,再用更精细的模型重新排顺序。 |

## 08 / Retrieval

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Keyword Search | 关键词搜索 | Search based mainly on literal terms. | 主要按词面是否出现来查找。 |
| Query Rewriting | 查询改写 | Rephrase a query to improve retrieval. | 换一种说法让搜索更容易找到资料。 |
| Retrieval | 检索 | Finding and returning information relevant to a query. | 从资料库里找出并取回和问题有关的资料。 |
| Retrieval Pipeline | 检索管线 | A sequence of retrieval operations. | 把查询、搜索、排序、过滤串起来的处理管线。 |
| Retriever | 检索器 | A component that retrieves candidate information. | 工作流中负责找回候选资料的组件。 |
| Search | 搜索 | Looking through a collection to find possible matches. | 在资料集合里找可能相关的内容。 |
| Search Query | 搜索查询 | The request used to find relevant information. | 用来查资料的问题或搜索内容。 |
| Similarity Search | 相似度搜索 | Finding items most similar to a query representation. | 找和当前问题最相似的内容。 |
| Top-k Retrieval | Top-k 检索 | Returning the highest-ranked k candidates. | 只返回排序最靠前的 k 个候选。 |

## 08 / Semantic Search

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Hybrid Search | 混合搜索 | Search combining lexical and vector retrieval. | 把关键词搜索和向量搜索结合起来。 |
| Semantic Search | 语义搜索 | Search that matches meaning rather than only exact words. | 理解问题意思后寻找相关内容,不只看字面是否相同。 |

## 08 / Vector Database

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Vector Database | 向量数据库 | A database designed to store and search vector representations. | 专门保存和查找嵌入向量的数据库。 |
| Vector Index | 向量索引 | An index organized to search vectors. | 专门帮助查找向量的索引。 |

## 08 / Vector Search

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Approximate Nearest Neighbor (ANN) | 近似最近邻 | A fast method for finding nearly closest vectors. | 用近似方式快速找最接近的向量。 |
| Vector Search | 向量搜索 | Searching for items whose vectors are close to a query vector. | 按内容的数字表示寻找相似资料。 |

## 09 / AI Agent

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Agent Goal | 用户目标 | What the user wants the workflow to accomplish. | 用户希望流程完成的事情。 |
| Agent System | 智能体系统 | A system combining an agent, model, tools, and a workflow. | 把智能体、模型、工具和工作流组合起来的系统。 |
| AI Agent | AI 智能体 | A system that uses a model, tools, and a control loop to pursue a goal. | 能理解目标、调用工具并多步行动的 AI 系统。 |

## 09 / Agent Loop

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Action | 行动;动作 | A step the system takes after deciding. | 系统做出决定后真正执行的一步。 |
| Agent Loop | 智能体循环 | A repeated cycle in which an agent observes, reasons, acts, and checks the result. | 智能体反复观察、思考、行动,再检查结果的循环。 |
| Agent-Environment Interaction | 智能体-环境交互 | The two-way process between the learner and its world. | 智能体行动、环境回应的来回过程。 |
| Observation | 观察结果;观测 | Information about the result or current state after an action. | 行动后得到的结果或状态信息。 |
| Workflow Orchestration | 编排 | Coordinate models, tools, steps, and state into a workflow. | 把模型、工具、步骤和状态组织起来协同工作。 |

## 09 / Human in the Loop

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Approval Gate | 审批闸门 | A gate that requires approval before an action continues. | 必须获得批准后才能继续的流程关口。 |
| Human Oversight | 人工监督 | Ongoing human attention to an AI system or its actions. | 人持续关注 AI 的行为和结果。 |
| Human-in-the-Loop (HITL) | 人在回路(HITL) | A workflow in which a person reviews, approves, corrects, or completes AI work. | 关键步骤保留人工检查、批准或接管。 |

## 09 / Memory State

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Agent Memory | 智能体记忆 | Information retained so an agent can use it later in a task or across sessions. | 智能体保存下来、之后还能使用的资料。 |
| Agent State | 智能体状态 | The current task information an agent needs to continue its work. | 记录智能体目前做到哪一步、掌握什么信息。 |
| Long-Term Memory | 长期记忆 | Information retained across interactions or over time. | 跨对话、跨时间保留下来的信息。 |
| Short-Term Memory | 短期记忆 | Context retained within a current interaction or task. | 当前对话或任务中暂时保留的信息。 |

## 09 / Model Context Protocol (MCP)

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| MCP Client | MCP 客户端 | A client inside the host that communicates with an MCP server. | 位于主机应用内部、负责和 MCP 服务器通信的客户端。 |
| MCP Server | MCP 服务器 | A server that exposes approved tools, resources, or prompts through MCP. | 按 MCP 提供获准工具、资源或提示的服务器。 |
| Model Context Protocol (MCP) | 模型上下文协议(MCP) | A protocol for connecting models or agents with tools and external context. | 让模型或智能体按统一方式连接工具和外部资料的协议。 |

## 09 / Multi-Agent Systems

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Agent Collaboration | 智能体协作 | Several agents working together on a task. | 多个智能体一起完成一个任务。 |
| Multi-Agent System | 多智能体系统 | A system in which multiple agents coordinate or divide work. | 多个智能体分工、协作或互相检查的系统。 |

## 09 / Planning

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Plan | 计划 | A proposed sequence of steps for reaching a goal. | 为达到目标而安排的一串步骤。 |
| Planning | 规划 | Breaking a goal into steps and deciding how to reach it. | 把大目标拆成步骤并安排完成顺序。 |
| Reasoning | 推理 | Work through information to reach a conclusion. | 处理信息并得出结论。 |
| Task Decomposition | 任务分解 | Break a task into manageable steps. | 把任务拆成容易处理的步骤。 |

## 09 / Skills / Plugins

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Plugin | 插件 | An installed or connected package that adds capability to a system. | 安装或接入后给系统增加能力的小组件。 |
| Skill | 技能 | A reusable packaged capability an AI system can use. | AI 可以反复使用的一套打包能力。 |

## 09 / Tool Calling

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Function Calling | 函数调用 | A structured request from a model to run a named function with arguments. | 模型按约定的函数名和参数请求程序执行动作。 |
| Tool | 工具 | A defined function or service that an application can invoke. | 应用可以调用的、事先定义好的功能或服务。 |
| Tool Calling | 工具调用 | Letting a model request an external function, API, or tool. | 让模型请求外部程序、接口或工具帮它做事。 |
| Tool Result | 工具结果 | The output returned after a tool executes. | 工具执行后返回的输出。 |
| Tool Schema | 工具模式 | The formal description of a tool's inputs and outputs. | 说明工具需要什么输入、会返回什么结果的结构。 |
| Tool Use | 工具使用 | Letting a model call external capabilities. | 让模型调用搜索、计算或其他外部工具。 |

## 10 / Api

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| API Endpoint | API 端点;接口地址 | A network-accessible location for a particular API operation. | 程序实际发送请求的接口地址。 |
| API Request | API 请求 | A request sent through an API to another system. | 按接口规则发给另一个系统的请求。 |
| API Response | API 响应 | A result returned through an API. | 通过 API 返回给应用的结果。 |
| Application Programming Interface (API) | 应用程序编程接口(API) | A defined way for software systems to request data or actions from one another. | 不同软件按约定方式互相请求数据或动作的入口。 |
| Software Development Kit (SDK) | 软件开发工具包 | A set of tools and libraries for building with a platform. | 帮助开发者接入平台的一组工具和代码库。 |

## 10 / GPU, VRAM & Unified Memory

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Compute | 计算资源 / 算力 | Processing capacity used for training or inference. | 训练和推理所需的计算能力。 |
| CPU | 中央处理器(CPU) | General-purpose hardware that can also run model computation. | 通用计算处理器,也可以运行模型。 |
| GPU | 图形处理器(GPU) | A processor designed for highly parallel numerical computation, often used for AI. | 能同时做大量数字计算、常用于训练和推理的处理器。 |
| Memory Footprint | 内存占用 | The amount of memory needed to load and run a model. | 加载和运行模型需要占用的内存大小。 |
| Unified Memory | 统一内存 | A shared memory pool that can be used by the CPU and GPU instead of separate system RAM and VRAM. | CPU 和 GPU 可以共同使用的一块内存,不必完全分成两套。 |
| VRAM | 显存(VRAM) | Memory on a GPU used to hold model weights, activations, and data. | GPU 上用来放模型和计算数据的内存。 |

## 10 / Latency

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Cost per Token | 每 token 成本 | The cost associated with processing or generating tokens. | 处理或生成 token 时产生的费用。 |
| Latency | 延迟 | The time a system takes to respond to a request. | 从发出请求到得到响应要等多久。 |
| Latency Breakdown | 延迟分解 | Splitting total latency into contributing parts. | 把总延迟拆成网络、上下文、模型等部分。 |
| Throughput | 吞吐量 | The amount of work a system completes in a given period of time. | 系统在一段时间内能处理多少请求或数据。 |
| Time to First Token (TTFT) | 首词元时间(TTFT) | The time from sending a request until the first generated token arrives. | 发出请求后,看到模型第一个字词需要等多久。 |

## 10 / Local AI vs Cloud AI

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Cloud AI | 云端 AI;云人工智能 | AI whose model inference runs on remote provider infrastructure. | 模型在远程服务商基础设施上运行的 AI。 |
| Local AI | 本地 AI;本地人工智能 | AI whose model inference runs on hardware the user controls. | 模型在自己控制的设备或硬件上运行的 AI。 |
| Self-Hosted Model | 自托管模型 | A model operated on infrastructure controlled by the user or organization. | 在自己控制的环境中运行和管理的模型。 |

## 10 / Model Serving

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Batch Inference | 批量推理 | Run inference on multiple inputs together. | 一次把多条输入交给模型处理。 |
| Dynamic Batching | 动态批处理 | Forming batches from requests that arrive at runtime so the serving system can process them together. | 请求陆续到来时,运行中把它们临时凑成一批一起处理。 |
| Inference Optimization | 推理优化 | A technique that makes model inference more efficient | 让模型生成结果时更快或更省资源的技术 |
| Inference Server | 推理服务器 | A server process that performs inference for callers. | 为调用方执行推理的服务器程序。 |
| Model Runtime | 模型运行时 | Software that loads and executes a model. | 负责加载模型并执行推理的软件环境。 |
| Model Serving | 模型服务 | Making a model available to applications through a running service. | 把模型放进持续运行的服务,供应用调用。 |

## 10 / Ollama

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Ollama | Ollama 本地运行工具 | A tool that makes it convenient to run language models locally. | 方便在本地电脑运行语言模型的工具。 |

## 10 / Quantization

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Mixed Precision | 混合精度 | Using different numerical precisions in different parts. | 模型不同部分使用不同精度。 |
| Numerical Precision | 数值精度 | How finely a number can be represented. | 一个数字能被表示得多细、多准确。 |
| Quantization | 量化 | Reducing the numeric precision of model values to lower memory or compute cost. | 用更少的数字精度保存模型,以减少内存和计算开销。 |

## 10 / Runtime Constraints

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Runtime Constraints | 运行时约束 | Limits that shape how an AI system can run in practice. | AI 系统真正运行时受到的各种限制。 |

## 10 / Tokens per Second

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Tokens per Second (TPS) | 每秒词元数(TPS) | The number of output tokens a system generates per second. | 模型每秒能生成多少个词元。 |

## 10 / Vllm

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Continuous Batching | 连续批处理 | Dynamically adding requests to active batches. | 在运行中动态把新请求加入批次。 |
| vLLM | vLLM 推理引擎 | An inference and serving engine optimized for running large language models. | 用于高效运行和提供大语言模型服务的推理引擎。 |

## 11 / Benchmarks

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Benchmark | 基准测试 | A standard task or dataset used to compare models. | 用统一题目或数据比较不同模型的测试。 |

## 11 / Deployment Readiness

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Deployment Readiness | 部署准备度 | Whether a model is ready for safe and reliable use. | 模型是否已经具备安全上线的条件。 |
| Release Gate | 就绪门;准备关卡 | A decision point that determines whether release may proceed. | 决定能不能继续发布的关卡。 |

## 11 / Evaluation

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Accuracy | 准确率 | The fraction of predictions that are correct. | 所有判断中答对的比例。 |
| Calibration | 校准 | How well a model's confidence matches its actual success frequency. | 模型说自己有多确定,长期看是否和实际正确率相符。 |
| Confusion Matrix | 混淆矩阵 | A table of classification outcome counts. | 把正确、误报、漏报等分类结果列成表。 |
| Evaluation | 评测 | Measuring a model or system against defined tasks, examples, or criteria. | 用规定的任务和标准检查模型或系统表现。 |
| Evaluation Metric | 评估指标 | A measurable quantity used to judge performance. | 用来量化模型表现的数字。 |
| F1 Score | F1 分数 | A combined measure of precision and recall. | 综合衡量精确率和召回率的指标。 |
| Human Evaluation | 人工评估 | People judge the quality, helpfulness, or safety of outputs. | 由人来判断回答是否有用、准确或安全。 |
| Offline Evaluation | 离线评估 | Testing on stored data before or outside live use. | 不接真实用户,先用保存的数据检查模型。 |
| Online Evaluation | 在线评估 | Measuring behavior in a live environment. | 模型实际运行时观察真实表现。 |
| Precision | 精确率 | Among predicted positive cases, the fraction that is actually positive. | 模型说"是"的结果里,真正是"是"的比例。 |
| Recall | 召回率 | Among actual positive cases, the fraction the model finds. | 所有真正的目标里,模型找出来的比例。 |

## 11 / Failure Handling

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Error Handling | 错误处理 | Detecting and responding to failures in a model workflow. | 发现模型或工具出错并采取处理措施。 |
| Failure Handling | 失败处理 | The practice of responding to unsuccessful operations. | 系统出错或失败时如何应对。 |
| Fallback | 备用方案 | A safer or simpler path used when the model cannot proceed. | 模型做不到或出错时采用的备用处理方式。 |
| Retry | 重试 | Running a request again after a transient failure. | 临时出错时再次发起请求。 |
| Timeout | 超时 | A request taking longer than an allowed limit. | 请求等待太久、超过规定时间。 |

## 11 / Failure Modes

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Failure Mode | 失败模式 | A recurring way the system can fail | 模型反复出现的一种失败方式 |

## 11 / Functional Tests

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Functional Test | 功能测试 | A test that checks whether a system behaves as intended. | 检查系统功能是否按预期工作的测试。 |
| Test Case | 测试案例 | A chosen input and expected behavior for checking a system. | 用来检查系统表现的一条具体案例。 |

## 11 / Guardrails

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Content Filter | 内容过滤器 | A component that detects or blocks certain content. | 检测并拦截特定内容的组件。 |
| Content Moderation | 内容审核 | Reviewing content for policy or safety compliance. | 检查内容是否符合规则和安全要求。 |
| Guardrail | 安全护栏 | A rule or control that limits unsafe, invalid, or unauthorized model behavior. | 限制模型不能做危险、违规或未经允许事情的控制。 |
| Red Teaming | 红队测试 | Deliberately probing a model for failures or unsafe behavior. | 有意攻击和试探模型,找出风险和漏洞。 |
| Safety Filter | 安全过滤器 | A mechanism that blocks or flags unsafe content. | 拦截或标记不安全生成内容的机制。 |

## 11 / Hallucination

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Fabricated Content | 编造内容 | Invented content presented as though it were retrieved, observed, or known. | 模型把没有依据的内容写出来,还让人以为它是真实资料。 |
| Factuality | 事实准确性 | Whether an output matches verifiable facts. | 回答是否与可验证事实一致。 |
| Hallucination | 幻觉 | Fluent model output that is unsupported, fabricated, or incorrect. | 回答听起来很像真的,但其实没有依据或内容是编出来的。 |
| Unsupported Claim | 无证据支持的主张 | A claim with no adequate supporting evidence. | 回答中没有资料依据的一句话。 |

## 11 / Permissions Safety

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Access Control | 访问控制 | Rules determining who or what may use a model or context. | 规定哪些人或系统可以使用模型和资料。 |
| Audit Log | 审计日志 | A record used to review system actions and changes. | 事后检查系统操作和修改的记录。 |
| Explainability | 可说明性 | The ability to communicate reasons for outputs. | 能否说明模型为何给出这个结果。 |
| Fairness | 公平性 | Whether a model behaves acceptably across groups. | 模型对不同人群是否不会产生不合理差别。 |
| Human Review | 人工审核 | A person verifies an important or uncertain result. | 由人检查重要或不确定的 AI 结果。 |
| Least Privilege | 最小权限 | Giving an identity only the access needed for its task. | 只给用户或程序完成工作所必需的最少权限。 |
| Permission | 权限 | Authorization to access or perform an action. | 被允许查看资料或执行操作的资格。 |
| Personally Identifiable Information (PII) | 个人可识别信息(PII) | Information that can identify a specific person directly or when combined with other data. | 能够直接或组合识别某个人的资料。 |
| Privacy | 隐私 | Protecting personal or sensitive information from improper use or disclosure. | 避免个人或敏感资料被不当使用或泄露。 |

## 11 / Prompt Injection

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Jailbreak | 越狱 | An attempt to bypass a model's safety or behavior restrictions. | 试图绕过模型安全限制,让它做本来不该做的事。 |
| Prompt Injection | 提示词注入 | An attack that puts instructions in input content to manipulate a model or agent. | 把恶意指令藏进输入资料,诱导模型违反原本规则。 |
| Prompt Leakage | 提示泄露 | Unwanted disclosure of hidden instructions or context. | 模型不该公开却泄露了系统提示或内部资料。 |

## 12 / Adoption

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| AI Adoption | AI 采用;AI 应用落地 | The sustained use of an AI system in real work. | 人们把 AI 真正、持续地用到工作里。 |
| AI Opportunity Assessment | AI 机会评估 | Reviewing a possible AI use based on work, value, risk, and fit. | 综合流程、收益、风险和适配性判断是否值得做 AI。 |
| User Feedback | 用户反馈 | Comments, signals, or observations supplied by users. | 用户对工具体验和结果的意见。 |
| Workflow Fit | 工作流适配 | How well a system fits the way work is actually done. | 工具是否贴合真实工作方式。 |

## 12 / Continuous Improvement

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Continuous Improvement | 持续改进 | Ongoing work that uses evidence to make a system better over time. | 根据真实使用情况不断把系统做得更好。 |

## 12 / Deployment

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| A/B Test | A/B 测试 | Comparing two system versions with different users or traffic. | 让两种版本分别服务一部分用户,比较谁更好。 |
| Availability | 可用性 | Whether users or applications can access the service. | 系统在需要时是否能正常使用。 |
| Canary Deployment | 金丝雀部署 | Releasing a model to a small portion of traffic first. | 先让少量用户试用新模型,再逐步扩大范围。 |
| Deployment | 部署 | Making a model or application available for real use. | 把模型或应用放到真实环境中运行。 |
| Production AI | 生产环境 AI | An AI system being used in real work by real users. | 已经上线、正在真实业务里工作的 AI。 |
| Reliability | 可靠性 | The ability to operate dependably across uses and time. | 系统能否稳定、持续、少出错地工作。 |
| Rollback | 回滚 | Return to a previous release or system state. | 新版本出问题时退回旧版本。 |

## 12 / Integration

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| API Integration | API 集成 | Integration that uses one or more APIs to connect systems. | 使用 API 把系统接到一起。 |
| Integration | 集成;整合 | The act of making separate capabilities work together as one usable system. | 把原本分开的东西接起来一起工作。 |

## 12 / Monitoring

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Concept Drift | 概念漂移 | A change in the relationship between inputs and outcomes over time. | 同样的输入和结果之间的规律随时间变了。 |
| Data Drift | 数据漂移 | A change over time in the characteristics of input data. | 线上收到的数据和过去训练或观察到的数据变了。 |
| Error Rate | 错误率 | The fraction of predictions that are wrong. | 预测错误的比例。 |
| Monitoring | 监控 | Continuously watching system behavior, quality, and operational signals. | 持续观察系统运行、质量和风险信号。 |
| Observability | 可观测性 | The ability to understand system behavior from logs, metrics, traces, and events. | 通过日志、指标和追踪信息看懂系统发生了什么。 |
| Production Monitoring | 生产监控 | Monitoring a model in live use | 模型上线后持续观察 |
| Schema Drift | 模式漂移 | An unexpected change in the fields or structure of data. | 数据字段或结构发生了程序没有预期的变化。 |

## 12 / Technical Scoping

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Technical Scoping | 技术范围界定 | Defining the data, interfaces, controls, and system boundaries for a solution. | 明确要用哪些数据、接口、控制和系统边界。 |

## 12 / Workflow Discovery

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Workflow Discovery | 工作流发现 | Finding and understanding a real workflow before deciding where AI fits. | 先弄清楚真实工作怎么做,再判断 AI 应该放在哪一步。 |
| Workflow Map | 工作流图;工作流程图 | A representation of steps, systems, decisions, and handoffs. | 把步骤、系统、判断和交接画在一起的图。 |

## 13 / Major AI Providers

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| AI Provider | AI 提供商 | A company that develops and makes models or AI services available. | 开发模型并提供 AI 产品或接口的公司。 |
| Anthropic | Anthropic 人工智能公司 | An AI company and provider associated with Claude models. | 一家开发 Claude 等模型的 AI 公司。 |
| Claude | Claude 大语言模型 | A large language model family developed by Anthropic. | Anthropic 开发的大语言模型家族。 |
| DeepSeek | DeepSeek AI 模型与提供商 | An AI model family and provider name used in the model landscape. | AI 模型家族和提供商名称之一。 |
| Gemini | Gemini 多模态模型 | A multimodal model family developed by Google. | Google 开发的多模态模型家族。 |
| GPT | GPT 生成式预训练模型 | A family of generative pre-trained transformer language models. | 一类以 Transformer 为基础、经过预训练并能生成内容的语言模型。 |
| Llama | Llama 大语言模型 | A large language model family developed by Meta. | Meta 开发的大语言模型家族。 |
| Meta AI | Meta AI 人工智能组织 | Meta's AI organization and model ecosystem, including Llama. | Meta 旗下负责 AI 模型和相关产品的组织与生态。 |
| Mistral AI | Mistral AI 人工智能公司 | An AI company and provider associated with the Mistral model family. | 一家开发 Mistral 模型家族的 AI 公司。 |
| Model Family | 模型家族 | A related group of models released under one model line or brand. | 同一条产品线或品牌下的一组相关模型。 |
| OpenAI | OpenAI 人工智能公司 | An AI company and provider associated with GPT models and AI products. | 一家开发 GPT 等模型并提供 AI 产品和接口的公司。 |
| Provider Strategy | 提供商策略 | Strategy labels might look mutually exclusive. | 与 Provider Strategy 相关的专业概念,用于理解 AI 系统或其工程实现。 |
| Qwen | 通义千问(Qwen) | An AI model family associated with Alibaba Cloud. | 阿里云旗下的 AI 模型家族。 |

## 13 / Model Types & Families

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Model Type | 模型类型 | A category based on a model's capability or purpose. | 根据模型能力或用途划分的一类模型。 |

## 13 / Open vs Closed / Local Models

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Cloud Model | 云端模型 | A model whose inference runs on remote infrastructure. | 推理主要在远程服务器上完成的模型。 |
| Local Model | 本地模型 | A model whose inference runs on user-controlled hardware. | 在自己的电脑、工作站或本地服务器上运行推理的模型。 |
| Open-Source Model | 开源模型 | A model release with broader source and licensing openness. | 在权重之外,通常还开放更多源代码和使用权利的模型。 |
| Open-Weight Model | 开放权重模型 | A model whose trained weights are made available for others to use or run. | 把训练后的模型权重公开出来、允许别人使用或运行的模型。 |
| Proprietary Model | 专有模型 | A model controlled by an organization whose weights or implementation are not broadly open. | 由某家公司控制、权重或实现没有完全公开的模型。 |

## 14 / AI Assistants & Coding Tools

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Agentic Coding | 智能体式编码 | Coding in which an AI can plan and take multiple actions. | AI 能规划并连续采取多个动作的编码方式。 |
| AI Assistant | AI 助手 | A user-facing AI system that helps with questions, content, or tasks. | 帮助用户回答问题、生成内容或完成任务的 AI 产品。 |
| AI IDE | AI 集成开发环境 | A development environment that integrates AI into coding and software work. | 把 AI 深度放进写代码环境里的开发工具。 |
| Autocomplete | 自动补全 | A feature that predicts and inserts likely code or text. | 预测并插入可能代码或文字的功能。 |
| Chatbot | 聊天机器人 | A system mainly designed to exchange messages with a user. | 主要和用户来回聊天的系统。 |
| Codebase | 代码库 | The complete set of source code for an application. | 一个应用的全部源代码。 |
| Coding Agent | 编程智能体 | An agent that can inspect code and take software-development actions. | 能查看代码并执行开发操作的智能体。 |
| Coding Assistant | 编码助手 | A tool that helps a developer write or understand code. | 帮助开发者编写或理解代码的工具。 |
| Computer Use | 计算机操作 | An AI capability that interacts with a graphical interface, browser, or desktop. | 让 AI 像用户一样操作界面、浏览器或桌面。 |
| Repository Context | 代码仓库上下文 | Information about the repository that guides an AI coding task. | 帮助 AI 完成编码任务的代码仓库信息。 |

## 14 / General Agents & Computer Use

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Browser Agent | 浏览器智能体 | An agent that mainly works in websites and browser interfaces. | 主要操作网页和浏览器界面的智能体。 |

## 15 / Agent Frameworks

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Agent Framework | 智能体框架 | Software components that help developers build, orchestrate, and run agents. | 帮助开发者组装、编排和运行智能体的软件框架。 |
| Agents SDK | 智能体 SDK | A software development kit for building applications with AI agents. | 帮助开发者构建 AI 智能体应用的一组软件工具。 |
| LangGraph | LangGraph 智能体框架 | A framework for building stateful agent workflows as graphs. | 把智能体步骤和状态连接成图来编排工作流的框架。 |

## 15 / How AI Agents Are Built

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Agent Architecture | 智能体架构 | The design of components and steps supporting an agent. | 支撑智能体运行的组件和流程设计。 |
| Middleware | 中间件 | Software between an application and a lower-level system. | 位于应用和底层系统之间的软件。 |
| Multi-Agent Orchestration | 多智能体编排 | Coordinating several agents and their interactions. | 协调多个智能体及其交互过程。 |

## 16 / AI Workflow Platforms

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| AI Step | AI 步骤 | A workflow step that uses an AI capability. | 工作流中调用 AI 能力的一步。 |
| AI Workflow Platform | AI 工作流平台 | A platform for assembling repeatable flows that combine models, tools, data, and human steps. | 把模型、工具、数据和人工步骤连成可重复流程的平台。 |
| API Orchestration | API 编排 | Coordinating multiple API calls into a workflow. | 把多个 API 调用组织成一个完整流程。 |
| Connector | 连接器 | A connection that lets a product work with another service or source. | 让产品接入其他服务或资料来源的连接。 |
| LLM Chain | LLM 链 | A connected sequence of large language model operations or components. | 把多个大语言模型处理步骤按顺序连接起来。 |
| RAG Pipeline | RAG 流水线 | A pipeline that retrieves knowledge and uses it to generate an answer. | 把检索资料和回答生成连起来的一组处理步骤。 |
| Trigger | 触发器;触发条件 | An event or signal that starts a workflow. | 让工作流开始运行的事件或信号。 |

## 16 / Automation Platforms

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Automation Platform | 自动化平台 | A platform that coordinates business workflow steps. | 负责协调业务流程各步骤的软件平台。 |
| Workflow Automation | 工作流自动化 | Using software to run repeatable workflow steps with limited manual effort. | 用软件自动执行重复的工作步骤。 |

## 17 / Data, APIs & Authentication

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Authentication | 身份认证 | Checking who a user or system is. | 确认"你是谁"。 |
| Authorization | 授权 | Deciding what an identified user or system is allowed to do. | 确认"你能做什么"。 |
| Backend | 后端 | Server-side software that handles data, business logic, and APIs. | 在服务器上处理数据、业务和接口的部分。 |
| Content Delivery Network (CDN) | 内容分发网络(CDN) | A distributed network that serves content from locations closer to users. | 把内容放到离用户更近的节点来加快访问。 |
| Database | 数据库 | A system that stores and retrieves structured application data. | 专门保存、查询和更新结构化数据的系统。 |
| Document Database | 文档数据库 | A database that stores records as documents. | 把数据以文档形式保存的数据库。 |
| File Storage | 文件存储 | Storage intended for files and media. | 专门保存文件和媒体的存储。 |
| HTTP | HTTP 网络协议 | The protocol commonly used to exchange requests and responses on the web. | 网页和服务之间传递请求与响应的基础协议。 |
| Relational Database | 关系型数据库 | A database that organizes data into related tables. | 把数据放在相互关联的表里的数据库。 |
| REST API | REST API 接口 | An API style that exposes resources and actions through standard web conventions. | 按常见 Web 规则通过接口访问资源和操作。 |

## 17 / Deployment & Operations

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Cloud Deployment | 云部署 | Release an application to cloud infrastructure. | 把应用发布到云平台运行。 |
| Continuous Deployment | 持续部署 | Automatically release a change after it passes the pipeline. | 代码通过自动检查后,自动发布到线上。 |

## 17 / Frontend & Backend

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Client | 客户端 | The side of a connection that requests or consumes a service. | 连接中发起请求或使用服务的一方。 |
| Frontend | 前端 | The user-facing part of an application that runs in a browser or client. | 用户看到并操作的界面部分。 |
| Server | 服务器 | A computer or service that performs backend work. | 承担后台处理工作的计算机或软件服务。 |
| Service | 服务 | A software capability that performs work for an application. | 为应用提供某种功能的软件能力。 |

## 18 / Backend & Data Platforms

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Backend Platform | 后端平台 | A platform that provides services behind an application's interface. | 在应用界面背后负责数据、登录、文件和接口等工作的平台。 |
| Edge Function | 边缘函数 | A function deployed to an edge execution environment. | 部署到边缘节点执行的一段服务端代码。 |
| Managed Database | 托管数据库 | A database operated and maintained by a provider. | 由服务商负责运行维护的数据库。 |
| PostgreSQL | PostgreSQL 关系型数据库 | An open-source relational database system. | 一种常用的开源关系型数据库。 |
| RLS | 行级安全(RLS) | Short name for Row-Level Security. | Row-Level Security 的英文缩写。 |

## 18 / Developer Platforms

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Deploy Preview | 部署预览 | A preview version generated by a deployment workflow. | 由部署流程生成的预览版本。 |
| Developer Platform | 开发者平台 | A service built around repositories for teamwork and delivery. | 围绕代码仓库提供团队协作和交付能力的服务。 |

## 18 / Web & Cloud Platforms

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Cloud Platform | 云平台 | Internet-hosted infrastructure and services used to run software. | 通过互联网提供、用来运行软件的基础设施和服务。 |
| Edge Compute | 边缘计算 | Running computation at distributed edge locations instead of one central server. | 不只在中心服务器,而是在分布式边缘位置执行计算。 |
| Edge Network | 边缘网络 | A distributed network of locations that serves traffic close to users. | 由许多靠近用户的节点组成、用于处理流量的分布式网络。 |
| Serverless | 无服务器架构 | A deployment model where the platform runs servers for application code on demand. | 开发者不用自己管理服务器,平台按需运行代码。 |

## 19 / Backend Technologies

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Cache | 缓存 | Temporarily stored data used to avoid repeating expensive work. | 把常用或已计算过的内容暂存起来,减少重复工作。 |
| Express | Express Node.js 框架 | A lightweight Node.js framework for building web servers and APIs. | 用 Node.js 构建网页服务器和接口的轻量框架。 |
| FastAPI | FastAPI Python 接口框架 | A modern Python framework for building APIs. | 用 Python 快速构建 Web 接口的框架。 |
| JavaScript | JavaScript 编程语言 | A programming language widely used for web interfaces and Node.js services. | 网页交互和 Node.js 服务常用的编程语言。 |
| Node.js | Node.js 运行环境 | A runtime for executing JavaScript outside the browser. | 让 JavaScript 能在浏览器之外运行的环境。 |
| Python | Python 编程语言 | A general-purpose programming language widely used for AI and backend work. | 常用于 AI、数据处理和后端开发的编程语言。 |
| TypeScript | TypeScript 编程语言 | A typed programming language that extends JavaScript. | 给 JavaScript 增加类型系统的编程语言。 |

## 19 / Data Technologies

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Data Pipeline | 数据管道 | A sequence for moving and processing data. | 移动和处理数据的一系列步骤。 |

## 19 / Frontend Technologies

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Next.js | Next.js Web 框架 | A React-based framework for building web applications. | 基于 React、用于构建 Web 应用的框架。 |
| React | React 前端库 | A JavaScript library for building user interfaces from reusable components. | 用可复用组件构建网页界面的 JavaScript 库。 |

## 19 / Product Services

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| SaaS | 软件即服务 | Software provided and operated as an online service. | 不必自己安装和维护、通过网络使用的软件服务。 |
