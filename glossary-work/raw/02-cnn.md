# Topic

CNN

Module: 02 · Neural Networks & Model Architectures

Topic: CNN

Source File: `cnn.html`

## Glossary Candidates

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| CNN | 卷积神经网络缩写 | Short for Convolutional Neural Network. | Convolutional Neural Network 的常见英文缩写。 |
| Convolutional Neural Network | 卷积神经网络 | A neural-network architecture designed to detect spatial patterns, especially in images. | 一种特别擅长在图像中找空间规律的神经网络结构。 |
| Convolutional neural network | 卷积神经网络 | The same architecture written in ordinary sentence capitalization. | 卷积神经网络的小写写法，和 CNN 指同一种结构。 |
| Neural-network architecture | 神经网络架构 | A structured design for a neural network. | 神经网络内部各层和计算步骤如何组织的设计。 |
| Neural network architecture | 神经网络架构 | The arrangement of layers and operations in a neural network. | 神经网络由哪些层组成、怎样连接和处理信息。 |
| Architecture | 架构 | The structural design of a model. | 模型内部各部分如何组织的设计。 |
| Model architecture | 模型架构 | The structural plan of a model. | 模型的整体结构蓝图。 |
| Neural Network | 神经网络 | A broader family of learned architectures. | 通过多层计算学习规律的一大类模型。 |
| Neural network | 神经网络 | A model made from connected processing layers. | 由相互连接的计算层组成的模型总称。 |
| Deep Learning | 深度学习 | The broader learning area in which neural networks are commonly used. | 用多层神经网络学习的机器学习方向。 |
| Deep learning | 深度学习 | A related concept above neural networks and CNNs. | CNN 所属的更大技术领域之一。 |
| Model | 模型 | A learned system that turns inputs into useful outputs. | 学会规律后，接收输入并给出结果的系统。 |
| Spatial pattern | 空间模式 / 空间规律 | A pattern defined by how elements are arranged in space. | 关注图像中不同位置之间关系的规律。 |
| Spatial patterns | 空间模式 / 空间规律 | Patterns in the arrangement of visual elements. | 图像里像素、边缘和形状在位置上的组合规律。 |
| Local pattern | 局部模式 | A pattern found in a small nearby region. | 在图像一小块邻近区域里出现的规律。 |
| Local patterns | 局部模式 | Small-region patterns detected by a CNN. | CNN 先从局部小区域中发现的视觉规律。 |
| Local spatial pattern | 局部空间模式 | A spatial pattern occurring in a small local region. | 一小块图像区域中的位置关系和视觉特征。 |
| Visual pattern | 视觉模式 | A meaningful pattern in visual information. | 图像中看得见、能帮助判断内容的规律。 |
| Visual patterns | 视觉模式 | Visual structures such as edges, textures, and shapes. | 边缘、纹理、形状等图像结构。 |
| Image | 图像 / 图片 | Visual input processed by a CNN. | 送进 CNN 分析的图片。 |
| Images | 图像 / 图片 | A common input domain for CNNs. | CNN 特别常处理的一类视觉数据。 |
| Visual information | 视觉信息 | Information carried by images or other visual inputs. | 图片里包含的颜色、位置、纹理、形状等信息。 |
| Learned filter | 学习得到的滤波器 | A small pattern detector learned from data. | 模型通过训练学会的“小探测器”。 |
| Learned filters | 学习得到的滤波器 | Filters learned by the network during training. | CNN 训练后得到、用来寻找不同模式的一组滤波器。 |
| Filter | 滤波器 / 过滤器 | A small operation that scans input to detect a pattern. | 在图片上移动、寻找某种特征的小工具。 |
| Filters | 滤波器 / 过滤器 | Small learned detectors that move across an input. | 会在输入上移动并检测模式的一组小探测器。 |
| Convolution filter | 卷积滤波器 | A filter used in the convolution step. | 在卷积计算中扫描局部区域的滤波器。 |
| Convolution filters | 卷积滤波器 | Filters that scan local regions for visual patterns. | 用来在小区域里找边缘、纹理等规律的滤波器。 |
| Small filter | 小滤波器 | A filter operating on a small part of the input at a time. | 每次只看图片一小块的滤波器。 |
| Filter movement | 滤波器移动 | Moving a filter across an input. | 让小窗口从图片的一边扫到另一边。 |
| Move across an input | 在输入上移动 | Scan different positions of the input with a filter. | 把滤波器放到输入的不同位置逐处查看。 |
| Scan across an image | 扫描图像 | Move a small window across an image to inspect regions. | 用小窗口从头到尾扫描图片。 |
| Small window | 小窗口 | A small view of an image used during scanning. | 每次观察图片的一小块区域。 |
| Input | 输入 | Data supplied to the model. | 送进模型让它处理的内容。 |
| Image input | 图像输入 | An image supplied to the network. | 送入 CNN 的图片。 |
| Pixels | 像素 | Small numerical elements that make up an image. | 组成图片的一个个小点及其数值。 |
| Pixel | 像素 | One visual data element in an image. | 图片中的一个小点。 |
| Local region | 局部区域 | A small nearby part of an input. | 图像里当前滤波器正在看的小块。 |
| Feature | 特征 | A useful signal or visual property detected in the input. | 能帮助模型识别图片内容的特点。 |
| Feature signal | 特征信号 | Information indicating that a visual feature is present. | 表示某种特征是否出现以及出现在哪里的信息。 |
| Useful signal | 有用信号 | Information retained because it helps a prediction. | 对最终判断有帮助、需要保留下来的信息。 |
| Signal | 信号 | Information carried forward for later computation. | 网络中传递的、代表模式或特征的信息。 |
| Edge | 边缘 | A place where light and dark meet. | 图片中明暗交界的线。 |
| Edges | 边缘 | Basic visual patterns where light and dark meet. | 明暗变化形成的基础图像特征。 |
| Texture | 纹理 | Repeated visual detail in an image. | 图像里重复出现的细小视觉细节。 |
| Textures | 纹理 | Repeated visual details detected in an image. | 比如布料、草地、木头表面的重复细节。 |
| Shape | 形状 | A visual form made from simpler patterns. | 由边缘等基础特征组合成的轮廓或外形。 |
| Shapes | 形状 | Combinations of simpler visual patterns. | 多个基础视觉模式组合出的形状。 |
| Feature map | 特征图 | A map showing where a filter’s pattern appears. | 一张图，标出某种特征在原图哪些位置出现。 |
| Feature maps | 特征图 | Outputs showing the locations of detected patterns. | 每个滤波器扫描后留下的模式位置图。 |
| Pattern location | 模式位置 | The location where a detected pattern appears. | 某个边缘、纹理或其他特征在图片中的位置。 |
| Feature layer | 特征层 | A network layer that represents visual features. | 保存或加工视觉特征的一层网络。 |
| Feature layers | 特征层 | Layers that transform detected visual signals. | 逐层处理和表示图像特征的网络层。 |
| Deeper feature layer | 更深的特征层 | A later layer that combines earlier features into richer ones. | 越往后越能理解复杂视觉结构的层。 |
| Deeper feature layers | 更深的特征层 | Later layers building richer visual features. | CNN 后面的层把简单模式组合成更复杂的特征。 |
| Later layer | 后续层 / 更后面的层 | A layer appearing later in the network. | 网络流程中位于前面层之后的层。 |
| Layer | 层 | One processing stage in a neural network. | 神经网络中负责一次信息变换的一层。 |
| Rich visual feature | 丰富的视觉特征 | A more complex visual representation built from simpler patterns. | 由边缘、纹理等简单特征组合出的复杂特征。 |
| Richer visual features | 更丰富的视觉特征 | Higher-level visual features built by later layers. | 网络越往后形成的、更复杂、更有辨识力的视觉信息。 |
| Combine patterns | 组合模式 | Use simpler detected patterns to form richer features. | 把简单边缘、纹理等组合起来理解更复杂的东西。 |
| Combination of simpler patterns | 简单模式的组合 | A shape or richer feature made from basic patterns. | 多个基础模式合在一起形成新特征。 |
| Pattern detector | 模式检测器 | A component that detects whether a pattern is present. | 判断某种规律有没有出现的小组件。 |
| Detection | 检测 | Finding whether and where something appears. | 找出目标或模式是否存在、出现在哪里。 |
| Prediction | 预测 | A result returned by the model for an input. | 模型看完输入后给出的判断结果。 |
| Model prediction | 模型预测 | The answer produced from the processed visual signals. | CNN 根据图像特征做出的结果。 |
| Classify | 分类 | Assign an input to a category. | 判断图片属于哪一种类别。 |
| Classification | 分类 | Identifying which category an image belongs to. | 给整张图片贴上类别答案。 |
| Image classification | 图像分类 | Identify whether an image contains a cat, vehicle, or another category. | 判断图片是猫、车辆还是其他类别。 |
| Category | 类别 | A named group an image may belong to. | 图片可能被归入的类型，例如猫或车辆。 |
| Class | 类 / 类别 | One possible category in a classification task. | 分类任务中的一个选项。 |
| Locate | 定位 | Determine where an object or pattern is. | 找到目标在图片中的位置。 |
| Object detection | 目标检测 | Find objects in an image and mark where they are. | 找出图片里的物体并标记它们的位置。 |
| Object | 物体 / 目标 | A thing in an image that a model may detect. | 图片中要被找出来的东西。 |
| Mark where they are | 标出所在位置 | Indicate the locations of detected objects. | 在图片上指出物体在哪里。 |
| Medical imaging | 医学影像 | Use visual pattern analysis to help analyze medical scans. | 用模型辅助分析医学扫描图像。 |
| Medical scan | 医学扫描图 | A scan whose visual patterns may need clinical review. | 需要医生查看的医学图像。 |
| Clinical review | 临床复核 | Human clinical review of patterns found in a medical scan. | 医疗场景中由专业人员进一步检查模型发现的模式。 |
| Analyze scans | 分析扫描图 | Examine medical scans for relevant visual patterns. | 查看医学图像里有没有值得关注的特征。 |
| Visual task | 视觉任务 | A task involving interpretation of visual information. | 需要理解图片或其他视觉内容的任务。 |
| Computer Vision | 计算机视觉 | The broader field of interpreting visual information. | 让计算机理解图片和视觉信息的整个领域。 |
| Computer vision | 计算机视觉 | A broad field that includes many visual methods and tasks. | 比 CNN 更大的视觉技术领域。 |
| Image Generator | 图像生成器 | A system that creates new images. | 根据输入生成新图片的系统。 |
| Image generator | 图像生成器 | A model or system that creates images rather than only recognizing them. | 用来创作图片，而不是只识别图片内容的系统。 |
| Create new images | 创建新图像 | Generate images that were not directly supplied as input. | 生成原来不存在的新图片。 |
| Recognize patterns | 识别模式 | Detect and interpret patterns in an input. | 找出图片中已经存在的规律。 |
| Recognize visual content | 识别视觉内容 | Determine what visual information an image contains. | 判断图片里有什么。 |
| Locate visual content | 定位视觉内容 | Determine where relevant visual content appears. | 判断图片里的目标在什么位置。 |
| Vision model | 视觉模型 | A model designed to process visual information. | 专门处理图片或视觉信息的模型。 |
| Modern vision model | 现代视觉模型 | A current vision model that may use CNNs, Transformers, or both. | 现代视觉模型，可能使用 CNN，也可能使用 Transformer。 |
| Transformers | Transformer 模型 / 变换器 | A model architecture also widely used in modern vision models. | 现代视觉模型常用的另一种架构。 |
| Transformer | Transformer 模型 / 变换器 | A related neural-network architecture. | 与 CNN 并列的神经网络架构家族。 |
| RNN | 循环神经网络缩写 | Short for Recurrent Neural Network, shown as a related neural-network family. | 页面相关概念树中的另一类神经网络缩写。 |
| Recurrent Neural Network | 循环神经网络 | A related neural-network architecture shown beside CNN. | 页面把它作为 CNN 的相关架构对照项。 |
| Neural Networks & Model Architectures | 神经网络与模型架构 | The broader topic area containing CNN. | CNN 所属的上位主题。 |
| Related concept | 相关概念 | A concept connected to CNN. | 和 CNN 有关系、适合一起理解的术语。 |
| Concept tree | 概念树 | A hierarchy showing relationships among deep learning, neural networks, and architectures. | 用树状关系表示概念上下级和并列关系。 |
| Broader field | 更大的领域 | A field containing a narrower method or architecture. | 例如计算机视觉比 CNN 更宽泛。 |
| Specialized type | 专门类型 | A narrower type within a broader family. | CNN 是神经网络家族中的一种专门类型。 |
| Broader family | 更大的家族 | The larger group that contains a specialized architecture. | 神经网络是包含 CNN 的更大模型家族。 |
| Pattern recognition | 模式识别 | Finding meaningful patterns in input data. | 从数据中找出有意义的规律。 |
| Spatial pattern learning | 空间模式学习 | Learning local spatial patterns from an input. | CNN 通过训练学会识别图像不同位置的规律。 |
| Learned representation | 学到的表示 / 表征 | A useful visual representation discovered by the network. | 模型训练过程中自己学会的图像特征表达。 |
| Representation | 表示 / 表征 | A form in which visual information is encoded for later prediction. | 把图像信息变成网络更容易使用的形式。 |
| Training | 训练 | The process through which filters and representations are learned. | 让 CNN 看很多例子并调整内部滤波器的过程。 |
| Learning | 学习 | Discovering useful visual patterns from examples. | 从图片例子中学会哪些视觉特征有用。 |
| Inference | 推理 / 推断 | Applying a learned CNN to a new image. | CNN 学会后，用它处理新图片并返回结果。 |
| New image | 新图像 | An image presented after learning for classification or detection. | 训练后模型第一次看到的图片。 |
| Learned model | 学到规律的模型 | A model whose filters and representations were learned from data. | 已经通过训练学会图像规律的模型。 |
| Process | 过程 | The sequence from image input to prediction. | 从像素进入到模型返回答案的一连串步骤。 |
| Workflow | 工作流 / 流程 | The ordered stages a CNN uses to process an image. | CNN 处理图像时按顺序经过的步骤。 |
| Pipeline | 流水线 | A sequence of processing stages. | 输入、卷积、特征图、深层特征、预测串起来的流程。 |
| Input stage | 输入阶段 | The first stage where the image enters the network. | 图片进入 CNN 的第一步。 |
| Convolution stage | 卷积阶段 | The stage where learned filters scan local regions. | 滤波器在图片小区域上移动并找模式的阶段。 |
| Feature-map stage | 特征图阶段 | The stage where each filter records where its pattern appears. | 把每个滤波器找到的模式位置保留下来。 |
| Deeper-feature stage | 深层特征阶段 | The stage where later layers combine patterns. | 后续层把简单模式组合成更丰富视觉特征的阶段。 |
| Prediction stage | 预测阶段 | The final stage that returns an answer. | 模型输出分类或定位结果的最后一步。 |
| Receive an image | 接收图像 | Take an image as the network input. | CNN 收到一张要分析的图片。 |
| Pixels enter the network | 像素进入网络 | Image pixel values are passed into the model. | 图片像素数值被送进 CNN。 |
| Scan for patterns | 扫描模式 | Search the input for learned visual patterns. | 在图片上寻找模型学会的规律。 |
| Keep useful signals | 保留有用信号 | Preserve feature information that helps later prediction. | 留下对最终判断有帮助的特征信息。 |
| Build richer visual features | 构建更丰富的视觉特征 | Combine earlier signals into more complex features. | 用前面找到的简单特征组成更复杂的视觉理解。 |
| Return an answer | 返回答案 | Produce the model’s final output. | 模型把识别或定位结果交出来。 |
| Classify or locate | 分类或定位 | Either identify a category or find an object’s location. | CNN 可能回答“是什么”，也可能回答“在哪里”。 |
| What it is | 它是什么 | The definition section of the page. | 页面用来解释 CNN 定义的部分。 |
| How it works | 它如何工作 | The process section describing CNN stages. | 页面用来说明 CNN 工作流程的部分。 |
| Real-world examples | 现实世界示例 | Practical applications of CNNs. | CNN 在真实场景中的用法例子。 |
| What it is NOT | 它不是什么 | Comparisons preventing common category mistakes. | 用来避免把 CNN 和相关概念混为一谈。 |
| Remember this | 记住这一点 | The page’s concise takeaway. | 页面最后对 CNN 核心机制的简短总结。 |
| Local spatial patterns across an input | 输入上的局部空间模式 | The core pattern-learning behavior summarized by the page. | CNN 的核心：在输入各处找局部位置规律。 |
| Apply learned filters across an input | 在输入上应用学习得到的滤波器 | Use learned filters at many input positions. | 把学会的小探测器放到图片的不同位置使用。 |
| Detect spatial patterns | 检测空间模式 | Find meaningful arrangements of visual elements. | 找出图像中有意义的空间排列规律。 |
| Recognize or locate patterns | 识别或定位模式 | Use visual patterns to recognize content or its location. | 根据模式判断内容是什么或在哪里。 |
| Image recognition | 图像识别 | Recognizing the content or category of an image. | 判断一张图片里是什么。 |
| Visual pattern analysis | 视觉模式分析 | Analysis of image patterns for recognition or review. | 对图片中的边缘、纹理、形状等规律进行分析。 |
| Spatially local computation | 空间局部计算 | Computation focused on nearby input elements. | 每次重点计算相邻的小区域。 |
| Prediction output | 预测输出 | The answer returned after visual processing. | CNN 最后给出的分类或定位结果。 |
| Category prediction | 类别预测 | Predicting an image’s category. | 预测图片属于猫、车辆等哪一类。 |
| Object localization | 目标定位 | Predicting where an object appears in an image. | 预测物体在图片中的位置。 |

## Potential Missing Concepts

以下概念与 CNN 直接相关，但 `cnn.html` 没有展开定义；保留为后续词表或核验阶段的潜在缺失候选，不把它们当作页面已讲内容：

- convolution / 卷积运算
- kernel / filter kernel / 卷积核／滤波器核
- receptive field / 感受野
- kernel size / 卷积核大小
- stride / 步幅
- padding / 填充
- valid padding / valid 卷积
- same padding / same 卷积
- channel / 通道
- input channel / 输入通道
- output channel / 输出通道
- RGB channel / RGB 通道
- activation map / 激活图
- pooling / 池化
- max pooling / 最大池化
- average pooling / 平均池化
- global average pooling / 全局平均池化
- subsampling / 子采样
- downsampling / 下采样
- upsampling / 上采样
- flatten / 展平
- fully connected layer / 全连接层
- dense layer / 稠密层
- output layer / 输出层
- hidden layer / 隐藏层
- input tensor / 输入张量
- feature tensor / 特征张量
- tensor / 张量
- feature extraction / 特征提取
- hierarchical feature learning / 层次化特征学习
- translation equivariance / 平移等变性
- translation invariance / 平移不变性
- parameter sharing / 参数共享
- local connectivity / 局部连接
- weight / 权重
- bias term / 偏置项
- activation function / 激活函数
- ReLU / ReLU 激活函数
- sigmoid / Sigmoid 函数
- softmax / Softmax 函数
- logits / 逻辑值／未归一化得分
- class probability / 类别概率
- backpropagation / 反向传播
- gradient / 梯度
- gradient descent / 梯度下降
- loss function / 损失函数
- cross-entropy loss / 交叉熵损失
- optimizer / 优化器
- learning rate / 学习率
- batch / 批次
- epoch / 训练轮次
- data augmentation / 数据增强
- random crop / 随机裁剪
- horizontal flip / 水平翻转
- image normalization / 图像归一化
- train-validation-test split / 训练集-验证集-测试集划分
- overfitting / 过拟合
- regularization / 正则化
- dropout / Dropout
- batch normalization / 批归一化
- batch norm / 批归一化缩写
- transfer learning / 迁移学习
- pretrained CNN / 预训练 CNN
- fine-tuning / 微调
- frozen backbone / 冻结的骨干网络
- backbone / 骨干网络
- head / 任务头
- classifier head / 分类头
- detection head / 检测头
- segmentation head / 分割头
- semantic segmentation / 语义分割
- instance segmentation / 实例分割
- object proposal / 候选区域
- bounding box / 边界框
- intersection over union (IoU) / 交并比
- mean average precision (mAP) / 平均精度均值
- precision / 精确率
- recall / 召回率
- F1 score / F1 分数
- confusion matrix / 混淆矩阵
- top-1 accuracy / Top-1 准确率
- top-5 accuracy / Top-5 准确率
- receiver operating characteristic (ROC) / ROC 曲线
- area under the curve (AUC) / 曲线下面积
- sensitivity / 敏感度
- specificity / 特异度
- medical image segmentation / 医学图像分割
- clinical validation / 临床验证
- explainability / 可解释性
- saliency map / 显著性图
- class activation map (CAM) / 类激活图
- Grad-CAM / Grad-CAM 可视化
- adversarial example / 对抗样本
- robustness / 鲁棒性
- distribution shift / 分布变化
- data drift / 数据漂移
- model monitoring / 模型监控
- inference latency / 推理延迟
- throughput / 吞吐量
- GPU inference / GPU 推理
- edge deployment / 边缘部署
- model compression / 模型压缩
- quantization / 量化
- pruning / 剪枝
- ONNX / ONNX 模型格式
- TensorRT / TensorRT 推理优化
- residual connection / 残差连接
- residual network / 残差网络
- ResNet / 残差网络架构缩写
- AlexNet / AlexNet
- VGG / VGG 网络
- LeNet / LeNet
- Inception / Inception 架构
- EfficientNet / EfficientNet
- MobileNet / MobileNet
- U-Net / U-Net
- YOLO / YOLO 目标检测模型家族
- vision transformer (ViT) / 视觉 Transformer
- CNN vs Transformer / CNN 与 Transformer 对比
- receptive-field growth / 感受野增长
- multi-scale feature / 多尺度特征
- feature pyramid / 特征金字塔
- image-to-label mapping / 图像到标签映射
- image-to-box mapping / 图像到边界框映射
- training-time computation / 训练时计算
- inference-time computation / 推理时计算
- deployment / 部署
- safety review / 安全复核

## Aliases / Synonyms

- CNN / Convolutional Neural Network / Convolutional neural network / 卷积神经网络
- convolutional network / convolution network / 卷积网络
- neural-network architecture / neural network architecture / 模型架构
- learned filter / filter / convolution filter / convolutional filter / 学习得到的滤波器／滤波器／卷积滤波器
- filter / small window / pattern detector / 滤波器／小窗口／模式检测器（页面语境中的近似表达）
- spatial pattern / visual pattern / image pattern / 空间模式／视觉模式／图像模式
- local pattern / local spatial pattern / 局部模式／局部空间模式
- feature map / activation map / 特征图／激活图（activation map 未在页面展开）
- feature layer / feature map layer / 特征层／特征图层
- deeper feature layer / later layer / 深层特征层／后续层
- edge / edges / 边缘
- texture / textures / 纹理
- shape / shapes / 形状
- image classification / classification / category prediction / 图像分类／分类／类别预测
- object detection / object localization / locate objects / 目标检测／目标定位／定位物体
- prediction / model prediction / prediction output / 预测／模型预测／预测输出
- image / visual input / image input / 图像／视觉输入／图像输入
- pixels / pixel values / 像素／像素值
- computer vision / vision / visual information interpretation / 计算机视觉／视觉／视觉信息理解
- image generator / image generation system / image generator model / 图像生成器／图像生成系统／图像生成模型
- neural network / Neural Network / neural-network model / 神经网络／神经网络模型
- Transformer / Transformers / transformer architecture / Transformer 模型／Transformer 架构
- RNN / Recurrent Neural Network / 循环神经网络
- detect spatial patterns / recognize patterns / pattern recognition / 检测空间模式／识别模式／模式识别
- classify / classify an image / image classification / 分类／给图像分类／图像分类
- locate / mark where objects are / object localization / 定位／标出目标位置／目标定位
- input / image input / input image / 输入／图像输入／输入图像
- learned representation / visual representation / feature representation / 学到的表示／视觉表示／特征表示
- process / workflow / pipeline / 流程／工作流／流水线
- receive an image / pixels enter the network / image input stage / 接收图像／像素进入网络／图像输入阶段
- scan for patterns / scan across an image / filter movement / 扫描模式／扫描图像／滤波器移动
- keep useful signals / retain useful features / useful signal extraction / 保留有用信号／保留有用特征／有用信号提取
- combine patterns / build richer visual features / hierarchical feature building / 组合模式／构建更丰富视觉特征／层次化特征构建
- classify or locate / recognize or locate / recognition or localization / 分类或定位／识别或定位／识别或定位任务

## Do Not Confuse Candidates

- CNN vs Computer Vision：CNN 是用于视觉任务的一种具体架构；Computer Vision 是解释视觉信息的更大领域。
- CNN vs Neural Network：CNN 是神经网络的专门类型；Neural Network 是包含 CNN 在内的更广泛模型家族。
- CNN vs Image Generator：CNN 通常识别或定位输入中的模式；Image Generator 的核心任务是创建新图像。
- CNN vs Image Classification：CNN 是架构；Image Classification 是使用模型判断图像类别的任务。
- CNN vs Object Detection：CNN 是架构；Object Detection 是找出目标并标记其位置的任务。
- CNN vs Medical Imaging：CNN 是模型结构；Medical Imaging 是应用领域或数据场景。
- CNN vs Transformer：二者都是神经网络架构，但页面只说明现代视觉模型可以使用 CNN、Transformer 或二者的组合，不应视为同一个架构。
- CNN vs RNN：CNN 和 RNN 都属于神经网络架构，但页面仅将它们列为相关概念，不应把 RNN 当作 CNN 的别名。
- Convolutional Neural Network vs Computer Vision：前者是方法/架构，后者是领域；有计算机视觉系统不代表一定使用 CNN。
- Filter vs Feature Map：filter 是扫描并检测模式的组件；feature map 是该 filter 在各位置检测结果的图。
- Learned Filter vs Hand-written Rule：learned filter 是从数据训练得到的参数化模式检测器，不是人手写的固定规则。
- Small Window vs Whole Image：small window 每次只查看局部区域；CNN 通过移动它逐步覆盖整张输入图像。
- Local Pattern vs Rich Visual Feature：local pattern 通常是小区域里的基础规律；richer visual feature 是后续层组合出来的更复杂表示。
- Edge vs Shape：edge 是明暗交界等基础特征；shape 是多个简单模式组合成的整体外形。
- Texture vs Shape：texture 强调重复的视觉细节；shape 强调轮廓或组合出的外形。
- Pixel vs Feature：pixel 是原始图像元素；feature 是网络从像素中检测或组合出来的有用信息。
- Feature Map vs Image：feature map 是滤波器检测结果的表示，不等于原始输入图像。
- Feature Layer vs Feature Map：feature layer 是网络中的处理层；feature map 是层或滤波器产生的数据表示。
- Detect vs Classify：detect 关注模式/目标是否存在及其位置；classify 关注输入属于哪个类别。
- Classification vs Object Detection：分类通常回答“是什么”；目标检测还要回答“在哪里”。
- Locate vs Recognize：locate 找位置；recognize 判断内容或类别，二者可以同时出现在一个视觉任务中。
- Prediction vs Ground Truth：prediction 是模型给出的结果；ground truth 是用于比较的真实答案（页面未展开 ground truth）。
- Training vs Inference：training 是学习滤波器和表示；inference 是用学好的 CNN 处理新图像。
- Input vs Output：input 是进入网络的图像/像素；output 是分类或定位答案。
- Image Recognition vs Image Generation：recognition 识别已有图像内容；generation 创建新图像。
- Vision Model vs Computer Vision：vision model 是一个处理视觉数据的模型；computer vision 是更大的领域。
- Deep Learning vs CNN：Deep Learning 是领域/方法范围；CNN 是其中一种神经网络架构。
- Architecture vs Task：architecture 描述模型怎么构成；task 描述模型要完成什么，例如分类或检测。
- Model vs Filter：model 是完整的 CNN 系统；filter 是模型内部用于检测局部模式的组件。
- Filter vs Kernel：页面使用 filter，没有展开 kernel；在 CNN 文献中 kernel 常是 filter 的近似术语，但要保留两者的来源差异。
- Feature vs Signal：feature 是有意义的视觉属性；signal 是网络中承载这类信息的信号，不能简单视为原始像素。
- Shape vs Object：shape 是视觉形式；object 是图像中要识别或定位的实体，物体可以由多个形状特征表示。
- CNN vs All Vision Models：页面只说 CNN 是一种架构，不能把所有视觉模型都称为 CNN。
- Modern Vision Models vs CNN-only Systems：页面明确现代视觉模型也广泛使用 Transformers，因此不能假定现代视觉模型只使用 CNN。

## Notes

- 本 raw 文件按 `cnn.html` 的页面正文、导航、可见示例、流程卡片、对照卡片、概念树和结论做最大候选收集；不做最终去重或删减。
- 正文核心定义是：CNN 是一种用于检测空间模式、尤其是图像中空间模式的神经网络架构。
- 正文另一种定义表述是：CNN 使用会在输入上移动的小型学习得到的滤波器，检测局部模式。
- 页面给出的图像模式例子是 edges、textures、shapes；这些例子全部单独保留，并保留其组合关系。
- 页面给出的工作流是：Input → Convolution filters → Feature maps → Deeper feature layers → Prediction；五个节点及其动作短语均保留。
- 页面把 feature map 解释为“每个 filter 显示其模式出现在哪里”，把 deeper feature layers 解释为“后续层构建更丰富的视觉特征”。
- 页面给出的应用示例是 Image classification、Object detection、Medical imaging；应用描述也分别保留。
- 页面明确区分 CNN 与 Computer Vision、Neural Network、Image Generator；这些对照关系放入 Do Not Confuse Candidates。
- 页面相关概念树为 Deep Learning → Neural Networks → CNN / RNN / Transformer；相关概念、层级关系及链接主题全部纳入候选。
- 页面明确说现代视觉模型同时使用 CNNs 和 Transformers；这不是说二者相同，也不是说所有现代视觉模型都使用二者。
- 页面没有展开卷积核尺寸、步幅、填充、池化、激活函数、反向传播、损失、训练指标、安全、部署或具体 CNN 模型家族；相关词放在 Potential Missing Concepts，不冒充正文已定义内容。
- 页面视频区块只有“没有可用的真实视频资源”的状态说明，没有新增的视频专业术语或外部来源事实。
- 该文件仅是 `glossary-work/raw` 原始候选稿，供后续清洗、核验、合并和排序使用。
