# Topic

Quantization

## Topic Metadata

- Module: 10 · Model Serving & Local AI
- Topic: Quantization
- Source File: `quantization.html`
- Source page title: `What is Quantization? · Model Serving & Local AI`
- Source page eyebrow: `07 · Model Serving & Local AI · Topic 02`
- Collection mode: raw candidate collection; terms are intentionally retained without deduplication or final pruning.

## Glossary Candidates

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Quantization | 量化 | Reducing the numerical precision used to represent a model. | 把模型内部数字用更少的精度表示，让模型更省空间和内存。 |
| model quantization | 模型量化 | Applying quantization to a machine-learning model. | 对模型做量化处理。 |
| numerical precision | 数值精度 | How finely a number can be represented. | 一个数字能被表示得多细、多准确。 |
| precision | 精度 | The amount of numerical detail retained. | 数字表示中保留了多少细节。 |
| numerical representation | 数值表示 | The format used to store a numerical value. | 用什么数字格式保存一个数。 |
| lower-precision representation | 低精度表示 | A representation that stores numbers with less numerical detail. | 用更少的数字细节保存模型数值。 |
| high precision | 高精度 | A representation that retains more numerical detail. | 能保存更多数字细节的表示方式。 |
| full precision | 全精度 | The original or relatively high-precision numerical format. | 模型原本使用的较高精度格式。 |
| full-precision model | 全精度模型 | A model stored in its original high-precision form. | 还没有降低数字精度的模型。 |
| quantized model | 量化模型 | A model whose numerical values use a reduced precision. | 已经把内部数字精度降低的模型。 |
| original model | 原始模型 | The model before its numerical representation is changed. | 做量化前的模型。 |
| model parameters | 模型参数 | Learned numerical values stored inside a model. | 模型内部保存学习结果的一大批数字。 |
| parameters | 参数 | Numerical values that control a model's behavior. | 决定模型如何计算和输出的数字。 |
| learned values | 学到的数值 | Values adjusted during model training. | 模型训练时学出来并保存下来的数字。 |
| internal values | 内部数值 | Numerical values used inside a model. | 模型内部计算时使用的数字。 |
| model knowledge | 模型知识 | Information encoded in the model's learned values. | 被保存进模型参数里的信息和规律。 |
| encoded knowledge | 编码后的知识 | Knowledge represented by model parameters. | 被转换成内部数字保存的知识。 |
| model file | 模型文件 | A file containing a model and its numerical values. | 保存模型的文件。 |
| model size | 模型大小 | The amount of storage space a model file needs. | 模型文件占用多少空间。 |
| storage | 存储空间 | Space used to keep files or model data. | 用来保存文件和模型的地方或容量。 |
| memory | 内存 | Working space used while a model runs. | 模型运行时需要占用的临时工作空间。 |
| memory usage | 内存使用量 | How much memory a model consumes. | 模型运行时用了多少内存。 |
| working footprint | 工作占用量 | The amount of working memory a model needs. | 模型运行时在设备上占用的空间。 |
| memory footprint | 内存占用 | The memory required by a model or process. | 程序或模型占用的内存大小。 |
| storage footprint | 存储占用 | The storage space required by a model file. | 模型文件占用的硬盘或存储空间。 |
| compute | 计算资源 | Processing capacity used to perform calculations. | 运行模型所需要的计算能力。 |
| compute usage | 计算资源使用量 | The amount of processing work required. | 模型运行时需要做多少计算。 |
| speed | 速度 | How quickly a model completes work. | 模型完成计算或给出结果有多快。 |
| runtime performance | 运行时性能 | How well a model performs while running. | 模型实际运行时的快慢和效率。 |
| quality | 质量 | How useful and accurate the model's results remain. | 模型结果有多准确、有用。 |
| model quality | 模型质量 | The quality of outputs produced by a model. | 模型输出结果整体好不好。 |
| quality trade-off | 质量权衡 | A possible quality cost of using a smaller representation. | 为了省内存或空间，可能要接受一点质量损失。 |
| trade-off | 权衡 | A situation where improving one property can affect another. | 得到一种好处时，可能要牺牲另一种好处。 |
| memory trade-off | 内存权衡 | Balancing memory savings against other requirements. | 在省内存和保持效果之间做取舍。 |
| storage trade-off | 存储权衡 | Balancing a smaller file against quality or compatibility. | 在文件大小和效果、兼容性之间取舍。 |
| speed trade-off | 速度权衡 | Balancing faster execution against quality or support. | 在运行速度和其他要求之间做取舍。 |
| compatibility trade-off | 兼容性权衡 | Balancing a format's benefits against runtime support. | 更省空间的格式不一定被所有设备支持。 |
| detail | 细节 | Information retained in a numerical or visual representation. | 表示中保留下来的细微信息。 |
| compact representation | 紧凑表示 | A representation that stores information in less space. | 用更少空间保存相同类型信息的方式。 |
| compactly | 紧凑地 | Using relatively little storage for information. | 用比较小的空间保存信息。 |
| fewer bits | 更少的比特位 | Using fewer binary digits to represent a value. | 用更少个二进制位表示数字。 |
| bit | 比特；位 | A binary digit with a value of zero or one. | 只能是 0 或 1 的最小数字单位。 |
| bit width | 位宽 | The number of bits used to represent a value. | 表示一个数字用了多少位。 |
| bit-depth | 位深 | The number of bits available for numerical values. | 数字格式能使用的位数。 |
| FP16 | 16 位浮点数 | A 16-bit floating-point numerical format. | 用 16 位表示的浮点数格式。 |
| float16 | 16 位浮点格式 | Another name for a 16-bit floating-point format. | FP16 的另一种写法。 |
| half precision | 半精度 | A common name for 16-bit floating-point precision. | 通常指 FP16 这种较高但不是全精度的格式。 |
| INT8 | 8 位整数 | An 8-bit integer numerical format. | 用 8 位整数保存数值的格式。 |
| int8 | 8 位整数格式 | A lower-case spelling of the INT8 format. | INT8 的另一种写法。 |
| Q8 | 8 位量化格式 | An 8-bit quantized representation, depending on the model format. | 常见的 8 位量化表示；具体行为要看实现。 |
| Q6 | 6 位量化格式 | A quantized representation commonly described with six bits. | 常见的 6 位量化表示。 |
| Q5 | 5 位量化格式 | A quantized representation commonly described with five bits. | 常见的 5 位量化表示。 |
| Q4 | 4 位量化格式 | A quantized representation commonly described with four bits. | 常见的 4 位量化表示。 |
| Q3 | 3 位量化格式 | A quantized representation commonly described with three bits. | 常见的 3 位量化表示。 |
| quantization level | 量化级别 | A chosen amount of numerical precision in a quantized model. | 量化后保留多少数字精度的档位。 |
| quantization quality | 量化质量 | The quality level associated with a quantized representation. | 某个量化版本保留效果的程度。 |
| quantization format | 量化格式 | A specific scheme for storing quantized values. | 量化数字具体采用的保存格式。 |
| quantization method | 量化方法 | The procedure used to convert values to lower precision. | 把数字转成低精度表示的具体方法。 |
| quantization scheme | 量化方案 | A complete choice of format, scaling, and conversion rules. | 一整套量化格式、缩放和转换规则。 |
| numerical precision ladder | 数值精度梯度 | An ordered range from higher to lower precision. | 从高精度到低精度的一串档位。 |
| original representation | 原始表示 | The representation used before quantization. | 量化前使用的数字表示。 |
| new representation | 新表示 | The numerical representation created after quantization. | 量化后生成的新数字表示。 |
| conversion | 转换 | Changing values from one numerical representation to another. | 把数字从一种格式变成另一种格式。 |
| quantize | 量化转换 | Convert values into a lower-precision representation. | 把数值转换成低精度格式。 |
| dequantize | 反量化 | Convert quantized values back to an approximate higher-precision form. | 把量化后的数值还原成近似的高精度数值。 |
| quantization error | 量化误差 | The difference introduced when values are represented approximately. | 数字变粗略后和原值之间产生的差距。 |
| approximation | 近似 | A representation that is close to, but not exactly, the original. | 和原来接近但不完全相同的表示。 |
| information loss | 信息损失 | Detail that is no longer retained after conversion. | 精度降低后丢失的部分细节。 |
| accuracy loss | 准确性损失 | A reduction in output correctness after quantization. | 量化后模型答得没原来准。 |
| quality degradation | 质量下降 | A reduction in output quality. | 模型效果变差。 |
| preservation of quality | 质量保持 | Keeping model results close to the original. | 尽量让量化模型和原模型效果接近。 |
| calibration | 校准 | Measuring value ranges to choose quantization parameters. | 先观察数值范围，再决定怎么量化。 |
| scale | 缩放因子 | A value used to map original numbers to quantized numbers. | 把原数字范围映射到量化范围的比例。 |
| zero-point | 零点 | An offset used when mapping real values to integer values. | 把实际数字映射到整数时使用的偏移量。 |
| clipping | 截断 | Limiting values outside a chosen numerical range. | 超出范围的数字被压到边界以内。 |
| outlier | 异常值 | A value much larger or smaller than most values. | 和大多数数字差别特别大的数。 |
| dynamic quantization | 动态量化 | Choosing some quantization information while the model runs. | 模型运行时动态决定部分量化参数。 |
| static quantization | 静态量化 | Choosing quantization information before runtime. | 模型运行前就确定量化参数。 |
| post-training quantization | 训练后量化 | Quantizing a trained model without retraining it fully. | 模型训练好后再降低它的数字精度。 |
| PTQ | 训练后量化（PTQ） | Short name for post-training quantization. | post-training quantization 的缩写。 |
| quantization-aware training | 量化感知训练 | Training while simulating the effects of quantization. | 训练时就让模型适应未来的低精度表示。 |
| QAT | 量化感知训练（QAT） | Short name for quantization-aware training. | quantization-aware training 的缩写。 |
| weight quantization | 权重量化 | Reducing the precision of learned model weights. | 把模型权重数字变成低精度格式。 |
| weight-only quantization | 仅权重量化 | Quantizing weights while leaving other values at higher precision. | 只压低权重精度，其他数值可能保持较高精度。 |
| activation quantization | 激活量化 | Reducing the precision of intermediate activations. | 把模型运行中间产生的激活值也变成低精度。 |
| mixed precision | 混合精度 | Using different numerical precisions in different parts. | 模型不同部分使用不同精度。 |
| per-tensor quantization | 逐张量量化 | Using one quantization range for a whole tensor. | 整个数值块共用一套量化范围。 |
| per-channel quantization | 逐通道量化 | Using separate quantization information for each channel. | 每个通道分别使用量化范围。 |
| tensor | 张量 | A multi-dimensional array of numerical values. | 按多个维度组织的一组数字。 |
| channel | 通道 | One slice or feature dimension in a tensor. | 张量中代表一组特征或数据的一条维度。 |
| integer representation | 整数表示 | Representing values with integers. | 只用整数形式保存数值。 |
| floating-point representation | 浮点表示 | Representing values with floating-point numbers. | 用能表示小数的浮点数格式保存数值。 |
| floating-point number | 浮点数 | A number that can represent fractional values. | 可以表示小数的数字。 |
| integer | 整数 | A number without a fractional part. | 没有小数部分的数字。 |
| range | 数值范围 | The lowest to highest values a format can represent. | 一个格式能表示的数字上下限。 |
| dynamic range | 动态范围 | The span between small and large representable values. | 格式能覆盖的数字大小范围。 |
| model architecture | 模型架构 | The structural design of a model. | 模型由哪些层和组件组成的结构。 |
| core architecture | 核心架构 | The main structure of a model. | 模型最主要的结构；量化通常不改变它。 |
| smaller architecture | 更小的架构 | A model structure with fewer components or parameters. | 通过减少结构本身来变小的模型。 |
| parameter count | 参数量 | The number of learned values in a model. | 模型内部有多少个参数数字。 |
| fewer parameters | 更少参数 | Having a smaller number of learned values. | 模型本身保存的数字更少。 |
| same model family | 同一模型系列 | Models sharing a common design or lineage. | 属于同一套模型家族的不同版本。 |
| model family | 模型家族 | A group of related model versions. | 结构或训练来源相近的一组模型。 |
| model version | 模型版本 | A particular release or numerical variant of a model. | 某个具体发布或量化版本的模型。 |
| runtime | 运行时 | The software environment that executes a model. | 真正负责运行模型的软件环境。 |
| inference runtime | 推理运行时 | Runtime software that performs model inference. | 负责让模型实际计算和生成结果的软件。 |
| hardware | 硬件 | The physical device executing the model. | 电脑、显卡、手机等实际设备。 |
| device | 设备 | A computer or embedded system where a model runs. | 承载并运行模型的电脑、手机或其他机器。 |
| accelerator | 加速器 | Hardware designed to perform certain computations efficiently. | 专门帮助模型更快计算的硬件。 |
| CPU | 中央处理器（CPU） | A general-purpose processor. | 电脑里负责通用计算的处理器。 |
| GPU | 图形处理器（GPU） | A processor suited to parallel numerical computation. | 擅长同时做大量数字计算的处理器。 |
| NPU | 神经网络处理器（NPU） | Hardware optimized for neural-network operations. | 专门加速神经网络计算的芯片。 |
| hardware support | 硬件支持 | The ability of hardware to efficiently run a format. | 设备是否能很好地运行某种格式。 |
| runtime support | 运行时支持 | The ability of runtime software to understand and execute a format. | 运行软件是否认识并支持某种量化格式。 |
| compatibility | 兼容性 | Whether a model format works with a given runtime or device. | 某模型能不能在某软件或设备上运行。 |
| limited hardware | 受限硬件 | Hardware with restricted memory or compute capacity. | 内存或计算能力比较有限的设备。 |
| lower-resource device | 低资源设备 | A device with less memory or compute capability. | 资源较少的电脑、手机或边缘设备。 |
| laptop | 笔记本电脑 | A portable computer that may run a local model. | 可以在本地运行模型的便携电脑。 |
| edge device | 边缘设备 | A device that processes data near where it is collected. | 在数据产生现场附近直接运行模型的设备。 |
| local AI | 本地 AI | AI running on a user's own device. | 模型直接在自己的电脑或设备上运行。 |
| local inference | 本地推理 | Running model inference on a local device. | 不依赖远程服务器，在本机算结果。 |
| cloud inference | 云端推理 | Running model inference on remote servers. | 把输入发到远程服务器，由云端算结果。 |
| deployment | 部署 | Making a model available to run in a target environment. | 把模型放到实际设备或系统中运行。 |
| model deployment | 模型部署 | Deploying a model for real-world use. | 让模型进入真实应用环境。 |
| deploy locally | 本地部署 | Put a model on a local computer or device. | 把模型装在自己的设备上运行。 |
| deployment target | 部署目标 | The device or environment where the model will run. | 准备运行模型的具体设备或环境。 |
| deployment constraint | 部署约束 | A limit imposed by the target environment. | 部署时受到的内存、速度、格式等限制。 |
| runtime constraint | 运行时约束 | A limit affecting model execution. | 模型运行时受到的资源或兼容性限制。 |
| memory constraint | 内存约束 | A limit on available working memory. | 可用内存不够或不能超出的限制。 |
| resource constraint | 资源约束 | A limit on available compute, memory, or storage. | 设备能提供的资源有限。 |
| operational constraint | 运行约束 | A practical limit in production use. | 实际使用中对模型大小、速度等的限制。 |
| serving | 服务化运行 | Running a model so applications can request outputs. | 让其他程序可以调用模型获得结果。 |
| model serving | 模型服务 | Operating a model for inference requests. | 把模型作为服务持续提供推理能力。 |
| inference | 推理 | Using a trained model to produce a result. | 用已经训练好的模型处理输入。 |
| inference computation | 推理计算 | The computation performed to generate a model output. | 模型从输入算出结果的过程。 |
| generated output | 生成输出 | Output produced by a model after processing input. | 模型处理输入后生成的结果。 |
| output | 输出 | The result returned by a model or system. | 模型给出来的结果。 |
| result | 结果 | What the model produces after computation. | 模型计算结束后得到的东西。 |
| input | 输入 | Information given to a model. | 送进模型让它处理的信息。 |
| process | 处理 | Computation applied to an input. | 模型对输入进行计算的过程。 |
| model execution | 模型执行 | Running the model's computations. | 让模型真正开始计算。 |
| model loading | 模型加载 | Reading a model into a runtime or device. | 把模型文件读进运行环境。 |
| loading time | 加载时间 | Time needed to load a model. | 模型从文件读进内存需要多久。 |
| inference time | 推理时间 | Time needed to produce an output. | 从收到输入到产生结果所需的时间。 |
| latency | 延迟 | Time between a request and its response. | 发出请求后等结果的时间。 |
| throughput | 吞吐量 | Amount of work completed per unit of time. | 一段时间内能处理多少请求或数据。 |
| tokens per second | 每秒词元数 | The number of text tokens generated per second. | 模型每秒生成多少个文字单位。 |
| tokens/s | 每秒词元数（tokens/s） | An abbreviation for tokens per second. | tokens per second 的缩写。 |
| speedup | 加速 | An increase in execution speed. | 运行得比原来更快。 |
| performance | 性能 | How efficiently and quickly a system operates. | 系统运行得快不快、稳不稳、效率高不高。 |
| practical | 实用的 | Suitable for actual use under given constraints. | 在现实条件下真正能用。 |
| impractical | 不切实际的 | Too demanding or unsuitable for the target use. | 资源要求太高，现实中不好用。 |
| laptop use case | 笔记本场景 | Running a model on a laptop. | 在笔记本上运行模型的情况。 |
| edge-device use case | 边缘设备场景 | Running a model on a nearby low-resource device. | 在现场附近的小型设备上运行模型。 |
| model choice | 模型选择 | Choosing among model sizes or quantization versions. | 根据需求挑选模型或量化版本。 |
| available memory | 可用内存 | Memory currently available to the model. | 设备现在能分给模型使用的内存。 |
| memory fit | 内存适配 | Whether a model fits within available memory. | 模型能不能装进现有内存。 |
| file size | 文件大小 | The amount of storage occupied by a file. | 文件占多少存储空间。 |
| smaller file | 更小的文件 | A file requiring less storage. | 占空间更少的文件。 |
| compressed image | 压缩图像 | An image stored in a smaller representation. | 经过压缩、文件更小的图片。 |
| high-resolution image | 高分辨率图像 | An image containing more visual detail. | 细节更多、清晰度更高的图片。 |
| image compression | 图像压缩 | Reducing image file size, often with possible detail loss. | 让图片文件变小，可能牺牲一些细节。 |
| analogy | 类比 | An example used to make an unfamiliar idea easier to understand. | 用熟悉的东西帮助理解新概念。 |
| ZIP compression | ZIP 压缩 | Compressing file bytes into a ZIP archive. | 把文件字节打包压缩成 ZIP 文件。 |
| file bytes | 文件字节 | The raw binary units that make up a file. | 文件底层由 0 和 1 组成的字节数据。 |
| ordinary compression | 普通压缩 | General file-size reduction that does not redefine model values. | 像 ZIP 一样缩小文件，不改变模型数字的含义。 |
| learned behavior | 学到的行为 | Behavior produced by patterns learned during training. | 模型训练后学会表现出来的方式。 |
| training | 训练 | The process through which a model learns from data. | 用数据让模型学会规律的过程。 |
| fine-tuning | 微调 | Additional training that changes a model for a narrower task. | 在原模型上继续训练，让它更适合某个任务。 |
| model architecture change | 模型架构改变 | Changing the structural design of a model. | 改变模型本身由哪些层和组件组成。 |
| quantization vs fine-tuning | 量化与微调的区别 | Quantization changes representation; fine-tuning changes learned behavior. | 量化改数字表示，微调改模型学到的行为。 |
| quantization vs architecture reduction | 量化与架构缩小的区别 | Quantization usually keeps structure; architecture reduction removes structure or parameters. | 量化通常保留结构，缩小架构则直接减少结构或参数。 |
| quantization vs ZIP compression | 量化与 ZIP 压缩的区别 | Quantization changes numerical precision; ZIP compresses file bytes. | 量化改变数字精度，ZIP 只是压缩文件字节。 |
| lower precision | 更低精度 | A representation retaining less numerical detail. | 牺牲部分数字细节来换取更省资源。 |
| higher precision | 更高精度 | A representation retaining more numerical detail. | 保存更多数字细节、通常更占资源。 |
| resource efficiency | 资源效率 | How much useful work is obtained from available resources. | 同样资源下能完成多少有用工作。 |
| memory efficiency | 内存效率 | How effectively a model uses memory. | 模型使用内存是否节省。 |
| storage efficiency | 存储效率 | How much model information fits into storage. | 用多小的文件保存模型信息。 |
| local model | 本地模型 | A model stored and run on a local device. | 存在自己设备上并由本机运行的模型。 |
| model format | 模型格式 | The file and numerical conventions used to store a model. | 模型文件组织和保存数字的方式。 |
| format label | 格式标签 | A shorthand name such as FP16, INT8, or Q4. | 用来快速表示数字格式的名字。 |
| shorthand | 简写；速记 | A short label standing for a longer technical description. | 用简短名字代替完整技术说明。 |
| Ollama | Ollama | A local model-running tool linked from the topic. | 一个帮助用户在本地运行模型的工具。 |
| captions | 字幕 | Text accompanying spoken video content. | 视频里同步显示的文字。 |
| independent explainer | 独立讲解视频 | A separate visual explanation accompanying the topic. | 页面附带的、独立制作的解释视频。 |
| visual explainer | 可视化讲解 | An explanation using visuals to show a concept. | 用图像或动画帮助解释概念。 |

## Potential Missing Concepts

- **calibration（校准）**：量化通常需要先估计权重或激活值的范围；正文只说 quantization method，没有展开校准流程。
- **scale（缩放因子）** 与 **zero-point（零点）**：正文没有解释连续数值如何映射到整数范围。
- **quantization error（量化误差）**：正文提到 quality may be lost，但没有单独说明由近似表示产生的误差。
- **post-training quantization / PTQ（训练后量化）**：正文描述量化流程，但没有区分训练后量化。
- **quantization-aware training / QAT（量化感知训练）**：正文没有说明让模型在训练阶段适应低精度的办法。
- **dynamic quantization / static quantization（动态量化／静态量化）**：正文没有说明量化参数是在运行时还是运行前确定。
- **weight quantization（权重量化）**：正文谈 model parameters，但没有明确区分权重和其他张量。
- **activation quantization（激活量化）**：正文没有介绍模型运行中间值的精度。
- **weight-only quantization（仅权重量化）**：正文没有说明只降低权重精度的常见方案。
- **mixed precision（混合精度）**：正文把 FP16、INT8、Q8、Q6、Q5、Q4、Q3作为档位，但没有说明同一模型可混用不同精度。
- **per-tensor quantization / per-channel quantization（逐张量／逐通道量化）**：正文没有介绍量化范围的粒度。
- **symmetric quantization / asymmetric quantization（对称／非对称量化）**：正文没有介绍零点是否为固定中心的两类映射。
- **tensor（张量）**：正文讲 model parameters，但没有解释参数在工程中常以多维张量保存。
- **dynamic range（动态范围）**：正文没有解释格式可以覆盖的数值范围。
- **clipping（截断）** 与 **outlier（异常值）**：极端数值会影响量化范围，但页面没有展开处理方法。
- **dequantization（反量化）**：页面提到 new representation 和运行时，但没有说明需要还原或近似还原的场景。
- **quantization kernel（量化计算内核）**：实际速度不仅取决于位数，还取决于运行时使用的底层计算实现。
- **hardware accelerator（硬件加速器）**：硬件支持会影响某个量化格式是否真的更快。
- **latency（延迟）**、**throughput（吞吐量）**：页面提到 speed，但没有拆成单请求等待时间和单位时间处理量。
- **tokens per second（每秒词元数）**：这是页面链接的相关性能指标，但正文没有定义如何测量。
- **benchmark（基准测试）**：正文说 behavior depends on runtime and hardware，但没有说明如何对不同版本进行可比测试。
- **perplexity（困惑度）**：语言模型量化质量常用的指标，正文没有列出。
- **accuracy（准确率）**、**exact match（精确匹配）**、**BLEU / ROUGE**：不同任务需要不同质量指标，正文只笼统说 quality。
- **calibration dataset（校准数据集）**：没有说明静态量化通常用什么样的数据估计范围。
- **representative dataset（代表性数据集）**：校准数据应接近真实输入分布，正文没有展开。
- **activation range（激活范围）**：正文没有解释中间激活值的上下界。
- **weight range（权重范围）**：正文没有解释模型权重的数值分布。
- **rounding（舍入）**：低精度转换需要把数值舍入到可表示的离散值，正文未提及。
- **clamp（钳位）**：超出格式范围的值需要被限制在边界内，正文未提及。
- **stochastic rounding（随机舍入）**：另一种舍入策略，正文未提及。
- **integer-only inference（纯整数推理）**：INT8 等格式不一定代表整个推理流程都是整数计算。
- **dequantization overhead（反量化开销）**：低位表示可能伴随转换成本，正文只说 speed sometimes increases。
- **memory bandwidth（内存带宽）**：量化的速度收益可能来自更少的数据搬运，正文没有解释。
- **cache behavior（缓存行为）**：更小的模型可能更容易放进缓存，正文没有展开。
- **model loading（模型加载）**：文件更小可能影响加载速度，但正文没有把它单独列为指标。
- **saturation（饱和）**：数值超出可表示范围时可能被压到边界，正文未提及。
- **accuracy recovery（准确率恢复）**：QAT、校准或重新训练可能用于恢复量化造成的质量损失，正文未提及。
- **task-specific evaluation（任务特定评估）**：量化质量应在目标任务上验证，正文没有给出评估流程。
- **format interoperability（格式互操作性）**：不同运行时对 FP16、INT8、Q 系列标签的解释可能不同。
- **quantized checkpoint（量化检查点）**：量化模型文件常以检查点形式保存，正文未提及。
- **model conversion（模型转换）**：从一种模型格式导出为另一种量化格式的过程，正文未提及。
- **fallback（回退）**：硬件或运行时不支持某算子时，可能回退到其他实现，正文未提及。
- **operator support（算子支持）**：量化格式是否覆盖模型中的所有计算算子，正文未提及。
- **accuracy–memory frontier（准确率—内存前沿）**：不同精度版本体现的选择边界，正文只用 trade-off 概括。

## Aliases / Synonyms

- Quantization ↔ model quantization ↔ numerical precision reduction ↔ precision reduction
- Quantized model ↔ quantized version ↔ lower-precision model ↔ compressed-precision model
- Full precision ↔ full-precision representation ↔ original precision ↔ high precision（语境中不一定完全相同）
- Numerical precision ↔ precision ↔ numerical detail ↔ number representation detail
- Lower precision ↔ lower numerical precision ↔ reduced precision ↔ fewer-bit representation
- Model parameters ↔ parameters ↔ learned values ↔ internal learned numbers
- Model size ↔ model file size ↔ storage size ↔ storage footprint
- Memory usage ↔ memory footprint ↔ working footprint ↔ working memory requirement
- Runtime performance ↔ inference performance ↔ execution performance ↔ model speed
- Runtime ↔ inference runtime ↔ execution environment ↔ model-running software
- Hardware ↔ target hardware ↔ execution device ↔ compute device
- Deployment ↔ model deployment ↔ serving setup ↔ putting a model into use
- Local AI ↔ local inference ↔ on-device AI ↔ local model execution
- Edge device ↔ edge-computing device ↔ lower-resource device ↔ nearby device
- Quantization method ↔ quantization scheme ↔ quantization procedure ↔ numerical conversion method
- Quantization format ↔ precision format ↔ model format ↔ format label
- Fewer bits ↔ lower bit width ↔ lower-bit representation ↔ smaller numerical representation
- FP16 ↔ float16 ↔ half precision ↔ 16-bit floating point
- INT8 ↔ int8 ↔ 8-bit integer ↔ 8-bit integer quantization（具体实现可能不同）
- Q8 ↔ 8-bit quantization ↔ eight-bit quantized format
- Q6 ↔ 6-bit quantization ↔ six-bit quantized format
- Q5 ↔ 5-bit quantization ↔ five-bit quantized format
- Q4 ↔ 4-bit quantization ↔ four-bit quantized format
- Q3 ↔ 3-bit quantization ↔ three-bit quantized format
- Quantization error ↔ rounding error from quantization ↔ approximation error ↔ precision loss
- Dequantization ↔ dequantizing ↔ approximate reconstruction ↔ conversion back to higher precision
- Calibration ↔ range calibration ↔ quantization calibration ↔ calibration pass
- Post-training quantization ↔ PTQ ↔ after-training quantization
- Quantization-aware training ↔ QAT ↔ training with simulated quantization
- Weight quantization ↔ parameter quantization ↔ quantizing model weights
- Weight-only quantization ↔ weights-only quantization ↔ W-only quantization
- Activation quantization ↔ quantizing activations ↔ activation precision reduction
- Mixed precision ↔ mixed-precision inference ↔ heterogeneous precision
- Memory constraint ↔ memory limit ↔ available-memory constraint ↔ fit-in-memory requirement
- Compatibility ↔ runtime compatibility ↔ hardware compatibility ↔ format support
- Quality trade-off ↔ accuracy–size trade-off ↔ precision–memory trade-off ↔ quality–resource trade-off
- Speed ↔ runtime speed ↔ execution speed ↔ inference speed
- Inference ↔ model execution ↔ serving-time computation ↔ prediction-time computation
- Output ↔ result ↔ response ↔ generated output
- Image compression ↔ compressed-image analogy ↔ file compression analogy
- ZIP compression ↔ ordinary file compression ↔ byte compression ↔ archive compression
- Tokens per second ↔ tokens/s ↔ tok/s ↔ generation throughput（不一定完全等价）
- Ollama ↔ local model runner ↔ local model-serving tool（页面仅以链接形式出现）

## Do Not Confuse Candidates

- **Quantization vs ZIP compression**：量化改变模型数值的表示精度；ZIP 主要压缩文件字节，概念上不改变数值精度。
- **Quantization vs fine-tuning**：量化改变表示方式；微调通过继续训练改变模型学到的行为。
- **Quantization vs smaller architecture**：量化通常保留核心架构和参数数量；更小架构可能减少层数、参数或改变结构。
- **Lower precision vs lower quality**：低精度可能带来质量损失，但质量损失不是低精度的同义词，也不一定严重。
- **FP16 vs INT8**：FP16 是浮点格式；INT8 是整数格式，二者不是简单的“同一格式不同写法”。
- **INT8 vs Q8**：两者都可能使用 8 位，但具体数值范围、缩放方式、布局和运行时支持可能不同。
- **Q4 / Q5 / Q6 / Q8**：Q 标签通常表示量化档位，不应仅凭数字断定所有实现都使用完全相同的位宽或质量。
- **Bit width vs model size**：位宽会影响模型大小，但模型大小还取决于参数量、元数据、格式和存储布局。
- **Memory vs storage**：存储用于保存模型文件；内存是模型运行时的工作空间。
- **Model size vs parameter count**：模型文件大小受参数量和每个参数的表示方式影响；参数量少不必然代表文件最小。
- **Speed vs runtime performance**：speed 是直观快慢；runtime performance 还可能包含延迟、吞吐量、加载时间和硬件效率。
- **Speed vs throughput**：速度可指单次完成快慢；吞吐量是单位时间完成多少工作。
- **Latency vs tokens per second**：延迟是等待一次响应的时间；每秒词元数是生成阶段的速率。
- **Quantization method vs quantization format**：方法是如何转换的流程；格式是转换后如何保存和计算的约定。
- **Full precision vs high precision**：full precision 常指原始或完整格式；high precision 只是相对更高，二者在不同上下文中不一定相同。
- **Numerical precision vs prediction precision**：数值精度描述数字表示；预测准确性描述输出是否正确。
- **Quantization error vs model error**：量化误差来自数值近似；模型误差可能来自训练、数据或任务本身。
- **Parameters vs hyperparameters**：参数通常由训练学出；超参数通常由人或训练流程提前设定。
- **Weights vs activations**：权重是模型保存的学习值；激活值是模型运行中间产生的数值。
- **Weight quantization vs activation quantization**：前者压低保存的权重精度；后者压低运行中间值的精度。
- **PTQ vs QAT**：PTQ 在训练完成后量化；QAT 在训练期间模拟量化影响并适应它。
- **Static vs dynamic quantization**：静态量化在运行前确定关键范围；动态量化可能在运行时确定部分范围。
- **Calibration vs training**：校准通常是估计量化范围；训练是更新模型学习参数的过程。
- **Rounding vs clipping**：舍入把数值映射到离散值；截断把超范围数值限制在边界。
- **Scale vs zero-point**：scale 改变数值跨度；zero-point 提供整数映射中的偏移。
- **Model architecture vs model format**：架构是模型结构；格式是模型如何存储和执行。
- **Model family vs model version**：模型家族是相关模型的集合；版本是其中一个具体变体。
- **Runtime vs hardware**：runtime 是执行模型的软件环境；hardware 是承载计算的物理设备。
- **Local AI vs cloud inference**：本地 AI 在用户设备运行；云端推理在远程服务器运行。
- **Deployment vs inference**：部署是把模型准备并放到目标环境；推理是模型在环境中处理一次输入。
- **Serving vs training**：服务化运行面向推理请求；训练用于学习或更新模型。
- **Hardware support vs runtime support**：硬件可能具备计算能力，但运行时仍可能不支持某个格式；反过来也一样。
- **Lower-resource device vs limited hardware**：二者都表示资源受限，但 lower-resource device 强调设备，limited hardware 可指设备能力本身。
- **Image compression vs quantization**：图像压缩只是帮助理解量化的类比；量化专门改变模型数值精度。
- **Compressed image vs quantized model**：图片的压缩方式和模型量化方式不同，不能把两者当成同一技术。
- **Quality trade-off vs compatibility trade-off**：前者关注效果损失，后者关注能否在目标软件或硬件上运行。
- **Quantized model vs smaller model**：量化模型可能保留同样的架构和参数，只改变数字表示；更小模型可能真的减少参数。
- **Model parameters vs model file**：参数是模型内部数字；模型文件是承载这些数字及其他信息的文件。
- **Ollama vs quantization format**：Ollama 是本地运行工具；Q4、Q8 等是量化或精度标签。
- **Tokens per second vs model size**：每秒词元数是运行指标；模型大小是存储指标，二者没有固定一一对应关系。

## Notes

- 本文件是 Module 10 Topic「Quantization」的 raw glossary 收集稿，目标是最大化保留候选；表格中的相近词、缩写、层级关系和可能重叠项有意不去重、不删减。
- 直接来源页面的定义主线是：model parameters are stored as numbers；quantization converts those values into lower-precision representations。
- 页面明确给出的主要收益和代价是：Memory ↓、Storage ↓、Speed ↑ sometimes，以及可能损失部分 model quality。
- 页面使用 image compression 作为 mental model，但明确说明这是 analogy，不是 ordinary ZIP compression；因此 image compression、compressed image、ZIP compression 和 file bytes 需同时保留并放入易混淆候选。
- 页面精度展示顺序为 FP16、INT8、Q8、Q6、Q5、Q4、Q3；页面同时提醒这些 labels 是 shorthand，formats are not automatically identical。
- 页面流程明确展示四个节点：Original model → Quantization → New representation → Deployment；对应的描述是 High precision → Fewer bits → Lower precision → More limited hardware。
- 页面明确指出实际行为取决于 quantization method、runtime 和 hardware；因此这三个词及其兼容性、支持度和性能相关扩展均保留。
- 页面案例包括 laptop、model choice 和 edge device，均围绕 available memory、local running、model family、quantization quality、lower-resource device 和 impractical 展开。
- 页面“不是”部分明确对照了 ZIP compression、fine-tuning、smaller architecture，以及“lower precision is not always better”；这些对照已在 Do Not Confuse Candidates 中保留。
- 页面相关概念链为 Model Parameters → Numerical Precision → Quantization → Model Size → Memory Usage → Runtime Performance；这些流程关系应保留，不应在后续整理中误合并为一个词。
- 页面相关链接包括 Ollama、Runtime Constraints、Parameters 和 Tokens per Second；它们不是正文主体定义，但属于正文导航明确指向的相关候选。
- 页面视频标记为 independent explainer、visual explainer、captions included；这些是页面呈现和学习辅助词，不是量化核心机制，但作为低优先级候选保留。
- `Topic Metadata` 同时保留了文件路径、页面 title 和页面内 eyebrow；页面内 eyebrow 写作 `07 · Model Serving & Local AI · Topic 02`，本收集任务的工作编号按要求记为 Module 10。
- Potential Missing Concepts 是基于正文范围推断的补充候选，不表示这些概念已经在页面中明确定义；它们用于后续 glossary 覆盖检查。
