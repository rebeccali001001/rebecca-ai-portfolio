# Topic

Layers

Module: 02 · Neural Networks & Model Architectures

Topic: Layers

Source File: `layers.html`

## Glossary Candidates

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Layer | 层 | One stage of computation inside a neural network. | 神经网络里负责完成一段计算的一个“站点”。 |
| Neural Network | 神经网络 | A model made of connected computational stages that transform information. | 由许多相连计算步骤组成、把输入变成输出的模型。 |
| Neural Network Layer | 神经网络层 | A layer that transforms information inside a neural network. | 神经网络内部负责转换信息的一层。 |
| Stage | 阶段 / 环节 | One step in a larger computation. | 更大计算过程中的一个步骤。 |
| Computation | 计算 | An operation that processes values to produce a result. | 对数值做处理并产生结果。 |
| Information | 信息 | Data or signals handled by a system. | 系统接收、处理或传递的内容。 |
| Transform | 转换 | To change an input into a new form. | 把输入变成另一种形式。 |
| Transformation | 转换 / 变换 | The process of changing an input into a new representation. | 把输入处理成新表示的过程。 |
| Learned Transformation | 学到的变换 | A transformation whose behavior is learned during training. | 模型在训练中学会如何进行的变换。 |
| Input Layer | 输入层 | The layer that receives the original data. | 接收原始数据的第一层。 |
| Hidden Layer | 隐藏层 | An internal layer between input and output. | 位于输入层和输出层之间、用户通常看不到的内部层。 |
| Hidden Layers | 隐藏层（复数） | Internal layers that transform information before the final output. | 在最终输出前反复处理信息的内部层。 |
| Output Layer | 输出层 | The final layer that produces the task result. | 负责给出任务结果的最后一层。 |
| Input | 输入 | Data supplied to a layer or model. | 送进某层或模型处理的内容。 |
| Output | 输出 | The result produced by a layer or model. | 某层或模型处理后产生的结果。 |
| Raw Data | 原始数据 | Data before the network has transformed it. | 还没有经过模型处理的原始内容。 |
| Earlier Representation | 前一层表示 | A representation produced by an earlier layer. | 前面一层处理后传来的信息形式。 |
| Representation | 表示 / 表征 | A form in which information is encoded for further computation. | 把信息编码成模型更容易继续处理的形式。 |
| New Representation | 新表示 / 新表征 | The representation produced after a transformation. | 信息经过一层处理后得到的新形式。 |
| Learned Representation | 学到的表示 / 学到的表征 | A useful representation discovered during training. | 模型训练时自己学会的一种有用表达。 |
| Higher-Level Representation | 更高层次表示 | A representation that captures more abstract structure. | 更抽象、更接近整体含义的表达。 |
| Contextual Representation | 上下文表示 | A representation whose meaning reflects surrounding context. | 会结合前后文来表达信息的表示。 |
| Token Representation | Token 表示 / 词元表示 | A numeric or internal representation of a token. | 模型内部表示一个词元或片段的方式。 |
| Signal | 信号 | Information passed through a computation. | 在网络中从一层传到下一层的信息。 |
| Forward Pass | 前向传播 | Passing an input through layers to compute an output. | 让信息从前往后经过各层并得到结果。 |
| Pass Forward | 向前传递 | Sending a transformed representation to the next stage. | 把处理后的表示交给下一层。 |
| Next Layer | 下一层 | The layer that receives the current layer's output. | 接收当前层结果的后续一层。 |
| Previous Layer | 前一层 | The layer that supplies input to the current layer. | 为当前层提供输入的前面一层。 |
| Layer Sequence | 层序列 | An ordered series of layers applied one after another. | 按顺序连接、依次处理信息的一组层。 |
| Repeated Structure | 重复结构 | A structure used multiple times in an architecture. | 在网络中反复出现的结构模块。 |
| Specialized Structure | 专用结构 | A structure designed for a particular kind of computation. | 针对某类数据或计算专门设计的结构。 |
| Traditional Three-Layer Diagram | 传统三层图 | A simple diagram showing input, hidden, and output layers. | 用输入层、隐藏层、输出层表示网络的简化图。 |
| Three-Layer Network | 三层网络 | A network described with input, hidden, and output stages. | 按输入、隐藏、输出三部分来看的网络。 |
| Modern Architecture | 现代架构 | A current model design that may use many specialized layers. | 可能含有许多专用层和重复模块的现代模型设计。 |
| Neural Network Architecture | 神经网络架构 | The overall arrangement and connectivity of a neural network. | 神经网络各层如何排列、连接和协作的整体设计。 |
| Model Architecture | 模型架构 | The structural design of a model. | 模型内部结构的设计。 |
| Assembly Line Analogy | 装配线类比 | An analogy in which each layer is one station on an assembly line. | 把每一层想成流水线上的一个工作站。 |
| Assembly Line Station | 装配线工作站 | A station that receives, changes, and passes on something. | 接收材料、进行加工再传给下一站的环节。 |
| Receive Information | 接收信息 | Taking in data from outside or an earlier representation. | 从外部或前一层拿到要处理的内容。 |
| Apply Learned Computation | 应用学到的计算 | Using learned parameters and operations to transform input. | 用训练出来的参数和操作来处理输入。 |
| Learned Computation | 学到的计算 | A computation whose behavior is controlled by learned values. | 由训练所得数值控制的计算。 |
| Send a Representation | 发送表示 | Passing a transformed representation to the next layer. | 把处理后的信息表示传给下一层。 |
| Build More Structure | 构建更多结构 | Using additional layers to refine or reorganize information. | 用更多层把信息变得更有结构。 |
| Refine a Representation | 细化表示 | Make a representation more useful or informative. | 让信息表达得更清楚、更有用。 |
| Reorganize a Representation | 重组表示 | Rearrange information into a more useful form. | 把信息重新组织成更适合任务的形式。 |
| Prediction | 预测 | A result produced for an input. | 模型针对输入给出的判断或结果。 |
| Task-Specific Output | 任务特定输出 | An output shaped for the task the model performs. | 针对具体任务生成的最终结果。 |
| Final Stage | 最终阶段 | The last computation stage before the result is returned. | 输出结果前的最后一个计算环节。 |
| Image Recognition | 图像识别 | Identifying or classifying content in an image. | 让模型识别图片里是什么或属于哪一类。 |
| Image Processing | 图像处理 | Transforming visual data for analysis or prediction. | 对图片信息进行处理以便分析或预测。 |
| Early Processing | 早期处理 | Initial transformations that detect simple visual signals. | 网络前面几层先找简单视觉信息的处理。 |
| Later Layers | 后面层 / 后续层 | Layers that operate after early processing. | 在前面层之后继续处理信息的层。 |
| Edge | 边缘 | A boundary or abrupt change in an image. | 图片中物体轮廓或明暗突变的位置。 |
| Edge Detection | 边缘检测 | Detecting boundaries in visual input. | 找出图片中轮廓边界的处理。 |
| Simple Signal | 简单信号 | A basic pattern or feature detected from input. | 从输入中发现的基础变化或简单信息。 |
| Shape | 形状 | A geometric form represented in visual data. | 图片中物体的几何外形。 |
| Pattern | 模式 / 规律 | A recurring or recognizable structure in data. | 数据中反复出现、可以识别的结构。 |
| Higher-Level Pattern | 高层次模式 | A more abstract pattern assembled from simpler patterns. | 由简单模式组合出的更抽象规律。 |
| Cat | 猫 | An example image-recognition prediction class. | 图像分类中“猫”这一可能的类别。 |
| Car | 汽车 | An example image-recognition prediction class. | 图像分类中“汽车”这一可能的类别。 |
| Text Processing | 文本处理 | Transforming text information for prediction or classification. | 对文字信息进行处理以便预测或分类。 |
| Token | 词元 / Token | A unit of text processed by a language model. | 模型处理的一个文字片段，可以是词、字或符号。 |
| Token Sequence | Token 序列 | An ordered sequence of tokens. | 按顺序排列的一串词元。 |
| Repeated Transformation | 重复变换 | Applying multiple transformations in sequence. | 让信息连续经过多次处理。 |
| Combine Context | 结合上下文 | Integrate surrounding information into a representation. | 把前后相关信息合在一起理解。 |
| Context | 上下文 | Surrounding information that helps determine meaning. | 帮助理解当前内容的前后相关信息。 |
| Contextual Information | 上下文信息 | Information from surrounding tokens or inputs. | 来自附近文字或相关输入的信息。 |
| Classification | 分类 | Predicting a category or label. | 判断输入属于哪个类别。 |
| Neural Network Classification | 神经网络分类 | Using a neural network to assign an input to a category. | 用神经网络把输入分到某个类别。 |
| Computational Unit | 计算单元 | A basic unit that performs part of a computation. | 完成一小部分计算的基本单位。 |
| Neuron | 神经元 | One computational unit within a neural network layer. | 层里面的一个计算小单元。 |
| Node | 节点 | A computational point in a network graph. | 网络连接图中的一个计算点。 |
| Unit | 单元 | A generic name for one computational element. | 对单个计算元素的泛称。 |
| Layer Structure | 层结构 | The computation and organization associated with a layer. | 一层包含的计算方式和组织形式。 |
| Model Structure | 模型结构 | The components and connections that make up a model. | 组成模型的部件及其连接方式。 |
| Parameter | 参数 | A learned value used by a computation. | 模型训练后留下、会影响计算结果的数值。 |
| Learned Parameter | 学到的参数 | A parameter adjusted during training. | 模型训练时自动调出来的参数。 |
| Weights | 权重 | Learned values controlling the influence of signals. | 决定不同信息影响大小的数值。 |
| Weight | 权重值 | One learned value controlling signal influence. | 控制某个输入影响程度的一个数值。 |
| Biases | 偏置 / 偏置项 | Learned offsets used in a layer's computation. | 在计算中帮助调整基准位置的学到的数值。 |
| Bias | 偏置值 | One learned offset in a computation. | 计算里用于整体平移结果的一个数值。 |
| Operations | 操作 / 运算 | Procedures applied to an input within a layer. | 一层内部对输入执行的具体运算。 |
| Activation Function | 激活函数 | A function that transforms a unit's computed value. | 对神经元计算结果再处理、帮助网络学习复杂关系的函数。 |
| Nonlinearity | 非线性 | Behavior that cannot be described by a simple straight-line relationship. | 不是简单直线关系、能表达复杂模式的特性。 |
| Depth | 深度 | The number or extent of layers in a network. | 网络有多少层、信息要经过多深。 |
| Deep Network | 深层网络 | A network with many layers. | 含有较多层的神经网络。 |
| Deep Learning | 深度学习 | Machine learning using neural networks with many layers. | 使用多层神经网络学习的机器学习方法。 |
| Complex Pattern | 复杂模式 | A pattern that requires multiple transformations to represent. | 需要多步处理才能表达的复杂规律。 |
| Optimization Challenge | 优化挑战 | A difficulty in training a model to learn useful parameters. | 训练时让参数学好可能遇到的困难。 |
| Computational Cost | 计算成本 | The compute, time, or energy required by a model. | 运行模型所需要的算力、时间或能源。 |
| Inference Cost | 推理成本 | The resources needed to produce outputs after training. | 模型学会后每次给出结果所需的资源。 |
| Training Cost | 训练成本 | The resources needed to learn parameters. | 训练模型、调整参数所需的资源。 |
| Model Capacity | 模型容量 | The amount of structure or complexity a model can represent. | 模型能够记住和表达多复杂规律的能力。 |
| Generalization | 泛化 | Performing well on new inputs beyond training examples. | 遇到没见过的新数据也能处理得好的能力。 |
| Convolutional Neural Network | 卷积神经网络 | A neural network architecture designed especially for spatial data. | 特别适合处理图片等有空间结构数据的网络。 |
| CNN | 卷积神经网络缩写 | Short for Convolutional Neural Network. | Convolutional Neural Network 的缩写。 |
| Recurrent Neural Network | 循环神经网络 | A neural network architecture that processes sequences recurrently. | 通过循环处理序列信息的网络。 |
| RNN | 循环神经网络缩写 | Short for Recurrent Neural Network. | Recurrent Neural Network 的缩写。 |
| Transformer | Transformer 架构 | A neural network architecture widely used for contextual sequence processing. | 擅长结合上下文处理序列、文本等信息的网络架构。 |
| Transformer Architecture | Transformer 架构 | The layer-based architecture built around Transformer blocks and attention. | 由 Transformer 模块和注意力机制等层组成的架构。 |
| Attention | 注意力机制 | A mechanism for weighting relevant parts of an input. | 让模型重点关注输入中更相关部分的机制。 |
| Attention Layer | 注意力层 | A layer that computes relationships or relevance across inputs. | 计算不同输入之间关联程度的一层。 |
| Convolutional Layer | 卷积层 | A layer that applies local filters, often to images. | 用局部滤波器处理图片等空间数据的一层。 |
| Recurrent Layer | 循环层 | A layer that carries information across sequence steps. | 在序列各步之间传递信息的一层。 |
| Feedforward Layer | 前馈层 | A layer that passes information from input toward output without recurrence. | 信息只向前流动、不循环返回的一层。 |
| Embedding Layer | 嵌入层 | A layer that maps discrete items to learned vectors. | 把词或类别等离散项目变成向量的一层。 |
| Normalization Layer | 归一化层 | A layer that rescales activations to stabilize computation. | 调整数值范围、让训练和计算更稳定的一层。 |
| Pooling Layer | 池化层 | A layer that summarizes local information, often reducing size. | 汇总局部信息、常常同时缩小数据尺寸的一层。 |
| Residual Connection | 残差连接 | A shortcut that adds an earlier representation to a later computation. | 把较早的信息直接加到后面计算中的捷径连接。 |
| Skip Connection | 跳跃连接 | A connection that bypasses one or more layers. | 跳过一层或多层、直接传递信息的连接。 |
| Layer Normalization | 层归一化 | Normalization applied across the features of a layer representation. | 对一层表示中的特征进行归一化的方式。 |
| Feed-Forward Network | 前馈网络 | A network component that transforms information through feedforward layers. | 通过前馈层对信息做变换的网络组件。 |
| Representation Learning | 表征学习 | Learning useful representations automatically from data. | 让模型自己学出有用的信息表达。 |
| Feature Extraction | 特征提取 | Producing useful features from raw input. | 从原始输入中找出有用特征。 |
| Feature Hierarchy | 特征层次 | A progression from simple features to more abstract features. | 从简单特征逐步组合成抽象特征的层次。 |
| Hierarchical Representation | 分层表示 | A representation built through multiple levels of abstraction. | 经过多层抽象逐步形成的表示。 |
| Layer-wise Processing | 逐层处理 | Processing information one layer at a time. | 让信息一层一层地被处理。 |
| Layer Stack | 层堆叠 | Multiple layers placed sequentially in a model. | 在模型中按顺序堆起来的多层结构。 |
| Layer Composition | 层组合 | Combining layers to create a larger computation. | 把多层组合成更大的计算过程。 |
| Layer Width | 层宽度 | The number of units or features in a layer. | 一层里包含多少个单元或特征。 |
| Layer Type | 层类型 | The kind of computation a layer performs. | 一层采用的计算类型。 |
| Layer Configuration | 层配置 | The selected arrangement and settings of layers. | 层的排列方式及相关设置。 |
| Layer Output | 层输出 | The representation produced by a layer. | 某一层处理后输出的表示。 |
| Layer Input | 层输入 | The data or representation received by a layer. | 某一层接收到的数据或表示。 |
| Intermediate Representation | 中间表示 | A representation produced between input and final output. | 输入和最终结果之间产生的中间信息形式。 |
| Intermediate Layer | 中间层 | A layer between the first input and final output stages. | 位于输入与最终输出之间的一层。 |
| Final Prediction | 最终预测 | The prediction returned after all required transformations. | 所有必要层处理完成后给出的最终判断。 |
| Layer Count | 层数 | The number of layers in a network. | 一个网络一共有多少层。 |
| More Layers | 更多层 | Additional transformation stages in a network. | 网络中增加的额外处理层。 |
| Layer Depth | 层深度 | The extent of sequential layer processing. | 信息连续经过多少层的深度。 |
| Model Complexity | 模型复杂度 | How structurally or computationally complicated a model is. | 模型结构和计算有多复杂。 |
| Optimization | 优化 | Adjusting learned values to improve model behavior. | 调整参数，让模型结果变得更好的过程。 |
| Representation Refinement | 表示细化 | Improving a representation through additional transformations. | 通过继续处理，让表示越来越适合任务。 |
| Information Flow | 信息流 | The movement of data or representations through a network. | 数据或表示在网络各层之间流动的过程。 |
| Signal Flow | 信号流 | The movement of signals through computational stages. | 信号经过各个计算环节的路径。 |
| Layer-by-Layer Computation | 逐层计算 | Computation performed sequentially across layers. | 按层次依次执行计算。 |
| Task | 任务 | The prediction, classification, or other job a model performs. | 模型要完成的具体工作。 |

## Potential Missing Concepts

- Activation function and nonlinearity are implied by the idea of layer operations but are not named in the source page.
- Common concrete layer types such as convolutional, pooling, recurrent, embedding, normalization, and attention layers are not explained in the source page; they are included as expansion candidates because CNN, RNN, and Transformer are named.
- Forward propagation, backpropagation, gradients, and loss are natural training concepts related to learned layer parameters but are not present in the page text.
- Tensor, vector, matrix, dimensionality, feature map, and hidden state are common technical data structures associated with layer inputs and outputs but are not named in the source.
- Residual connections, skip connections, layer normalization, and feed-forward blocks are common modern architecture concepts that may be needed for a fuller Layers glossary.
- Layer width, layer count, depth, model capacity, computational cost, and inference cost are useful architecture and deployment terms suggested by the page's discussion of more layers and cost.
- Backpropagation, gradient descent, vanishing gradients, exploding gradients, and initialization are relevant optimization and deep-network concepts but are outside the page's beginner-level explanation.

## Aliases / Synonyms

- Layer / neural network layer / computation stage / processing stage / transformation stage
- Input layer / input stage / input side of the network
- Hidden layer / internal layer / intermediate layer
- Output layer / final layer / prediction layer / output stage
- Representation / data representation / feature representation / internal representation
- Learned representation / learned feature / learned feature representation
- Higher-level representation / abstract representation / high-level feature
- Contextual representation / context-aware representation
- Transform / process / map / convert / encode
- Transformation / computation / processing step / mapping
- Learned parameters / model parameters / trainable parameters / learned values
- Weights / weight values / connection weights
- Biases / bias values / offset terms
- Computational unit / neuron / node / unit
- More layers / greater depth / deeper network / increased depth
- Pass forward / forward flow / forward propagation / feedforward processing
- Image recognition / visual recognition / image classification
- Text processing / language processing / sequence processing
- Pattern / feature / structure / regularity
- Later layers / deeper layers / downstream layers
- CNN / Convolutional Neural Network / convolution network
- RNN / Recurrent Neural Network / recurrent network
- Transformer / Transformer architecture / Transformer model
- Classification / category prediction / label prediction
- Computational cost / compute cost / resource cost
- Optimization challenge / training difficulty / optimization difficulty

## Do Not Confuse Candidates

- Layer vs neuron: a layer is a stage containing or applying many computational units; a neuron is one unit within a layer.
- Layer vs parameter: a layer is a computation and structural component; a parameter is a learned value used by that computation.
- Layer vs model: a layer is one component or stage; a model is the complete system made from layers and other components.
- Layer vs architecture: a layer is one building block; an architecture is the overall arrangement and connectivity of many blocks.
- Input layer vs input: the input layer is a network component; input is the data received by that component.
- Output layer vs output: the output layer performs the final computation; output is the result it produces.
- Hidden layer vs hidden state: a hidden layer is a structural stage; a hidden state is a changing representation carried through sequence processing.
- Representation vs raw data: raw data is the original input; a representation is an encoded or transformed form used by the model.
- Representation vs prediction: a representation is an internal information form; a prediction is a task result returned by the model.
- Weight vs bias: a weight controls the influence of an input signal; a bias shifts the computation's baseline.
- Parameter vs hyperparameter: a parameter is learned during training; a hyperparameter is selected to control training or architecture.
- Computation vs operation: computation is the overall act of calculating; an operation is one specific procedure inside it.
- Depth vs width: depth counts sequential layers; width describes the number of units or features within a layer.
- More layers vs always better: adding depth may represent more complex patterns, but can increase cost and optimization challenges.
- CNN vs RNN: CNNs are commonly associated with local spatial patterns; RNNs are designed to carry information across sequence steps.
- RNN vs Transformer: both can process sequences, but they organize sequence computation differently and should not be treated as the same architecture.
- Layer vs layer type: a layer is an individual stage; layer type describes what kind of computation that stage performs.
- Early processing vs later layers: early processing often detects simple signals; later layers can combine them into shapes, patterns, and higher-level representations.
- Context vs contextual representation: context is surrounding information; a contextual representation is the encoded result after using that context.
- Classification vs prediction: classification is a type of prediction that returns a category or label.
- Image recognition vs text processing: both use layered transformations, but their input structures and useful representations differ.
- Learned computation vs hand-written rule: a learned computation gets behavior from training parameters; a hand-written rule is explicitly specified by a person.

## Notes

- The candidate set was extracted from the complete visible正文 of `layers.html`, including the page title, definition, analogy, process flow, concept tree, image and text examples, misconceptions, related-concepts map, and reminder text.
- The source is beginner-friendly and uses many plain-language phrases. Those phrases are retained when they carry a glossary-relevant meaning.
- Candidate rows intentionally preserve overlapping terms, abbreviations, variants, examples, and near-synonyms rather than deduplicating them.
- The source explicitly names input layer, hidden layers, output layer, learned parameters, representations, weights, biases, operations, signal, prediction, image recognition, text processing, token representations, context, classification, CNN, RNN, and Transformer.
- The source does not define a specific activation function, tensor shape, gradient, backpropagation procedure, or concrete layer implementation; those items are marked as potential missing concepts or expansion candidates rather than presented as source-defined facts.
