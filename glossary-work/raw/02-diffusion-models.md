# Topic

Diffusion Models

Module: 02 · Neural Networks & Model Architectures

Topic: Diffusion Models

Source File: `diffusion-models.html`

## Glossary Candidates

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Diffusion Model | 扩散模型 | A generative model that creates data by reversing a gradual noising process. | 先把数据逐渐变得嘈杂，再学会把噪声一步步还原成有结构的结果。 |
| Diffusion Models | 扩散模型（复数） | A family of models based on adding and removing noise. | 一类通过加噪和去噪来生成内容的模型。 |
| Diffusion | 扩散 | The model family built around a noising and denoising process. | 扩散模型这一整类方法的简称。 |
| Generative Model | 生成模型 | A model that learns to create new data. | 学会生成新数据或新内容的模型。 |
| Generative Modeling | 生成式建模 | Modeling that learns how to generate structured data. | 让模型学习怎样产生有结构的数据。 |
| Generative Model Family | 生成模型家族 | One category of approaches for generating data. | 生成内容的方法类别，例如扩散、GAN、VAE。 |
| Generative Model Families | 生成模型家族（复数） | Related categories of generative modeling approaches. | 各种生成模型方法组成的分类体系。 |
| Data | 数据 | Information that a model can learn from or produce. | 模型学习或生成的各种信息。 |
| Noising Process | 加噪过程 | Gradually adding noise to an example. | 一点一点给原始数据加入噪声。 |
| Noise Addition | 加噪 | The operation of adding noise to data. | 把随机干扰加入数据，让原来的结构变得不清楚。 |
| Noise | 噪声 | Random variation that hides useful structure. | 会遮住原本规律的随机干扰。 |
| Noisy Data | 带噪数据 | Data that has been made less clear by noise. | 被加入干扰、变得不清晰的数据。 |
| Gradual Noise | 逐渐增加的噪声 | Noise added in small steps over time. | 不是一次加完，而是分很多步增加的噪声。 |
| Structured Data | 结构化数据 | Data with useful organization or recognizable structure. | 具有规律、组织或可辨认结构的数据。 |
| Useful Data | 有用数据 | Data that contains a useful signal or pattern. | 含有可利用信息、不是纯随机干扰的数据。 |
| Structure | 结构 | The organized pattern that makes data meaningful. | 让图像、声音或视频能够被辨认的规律。 |
| Pattern | 模式 / 规律 | A regular relationship learned from examples. | 许多例子中反复出现的规律。 |
| Training | 训练 | Learning from examples to predict or remove noise. | 模型看很多例子并调整自己、学会去噪的过程。 |
| Training Data | 训练数据 | Examples used to teach the model. | 用来教模型学习的数据样本。 |
| Example | 示例 / 例子 | One item shown to the model during learning. | 给模型学习的一个具体数据案例。 |
| Learn | 学习 | To acquire useful patterns from examples. | 从例子中找出可以重复使用的规律。 |
| Learned Model | 学到规律的模型 | A model that has learned patterns from examples. | 已经从训练数据中学会规律的模型。 |
| Predict Noise | 预测噪声 | Estimate which noise should be removed. | 判断当前数据里哪些部分是应该去掉的干扰。 |
| Noise Prediction | 噪声预测 | The model's estimate of the noise in a sample. | 模型对数据中噪声成分的估计。 |
| Remove Noise | 去除噪声 | Take away estimated noise from data. | 根据模型判断，把干扰从数据里减掉。 |
| Noise Removal | 噪声移除 | The operation of subtracting or removing noise. | 去掉数据中随机干扰的动作。 |
| Denoising | 去噪 | Turning noisy data into more organized data. | 把模糊、嘈杂的数据逐步变清楚。 |
| Denoise | 去噪（动词） | To remove noise from a sample. | 对数据执行去噪。 |
| Denoising Process | 去噪过程 | Repeatedly removing noise to reveal structure. | 多次去除噪声、逐步显露结构的过程。 |
| Repeated Denoising | 反复去噪 | Many denoising steps applied one after another. | 连续做很多次小的去噪操作。 |
| Denoising Step | 去噪步骤 | One update that makes a noisy sample more organized. | 每次把结果往更清晰方向推进的一小步。 |
| Next Denoising Step | 下一次去噪步骤 | The denoising update that should happen next. | 模型接下来要执行的那一步去噪。 |
| Denoising Direction | 去噪方向 | The useful direction for making a sample less noisy. | 让结果从随机走向有结构的变化方向。 |
| Organized Data | 变得有组织的数据 | Data that has gained more recognizable structure. | 经过去噪后越来越容易辨认的数据。 |
| Hidden Structure | 被隐藏的结构 | Useful organization obscured by heavy noise. | 被大量噪声盖住、暂时看不出的规律。 |
| Mostly Hidden | 大部分被隐藏 | A state where noise has obscured most structure. | 噪声很大，原本的内容几乎看不出来。 |
| Generation | 生成 | The process of producing a new output. | 模型从起点逐步做出新内容的过程。 |
| Generate | 生成（动词） | To create an output from a model. | 用模型做出一个结果。 |
| Generated Output | 生成输出 | The data produced after denoising. | 多次去噪后模型产生的最终结果。 |
| Output | 输出 | The result produced by a model. | 模型处理完成后交出的结果。 |
| Start from Noise | 从噪声开始 | Begin generation with random noise. | 一开始不提供成品，而是从随机噪声起步。 |
| Random Noise | 随机噪声 | Noise sampled randomly as a starting point. | 随机产生、用作生成起点的干扰信号。 |
| Starting Noise | 起始噪声 | The initial random sample used for generation. | 生成流程最开始使用的随机噪声。 |
| Random Starting Point | 随机起点 | A random initial state for generation. | 生成时模型开始工作的随机状态。 |
| Repeated Generation Steps | 反复生成步骤 | A sequence of updates used to create an output. | 模型重复很多小步骤才得到最终内容。 |
| Learn to Predict / Remove Noise | 学会预测／去除噪声 | Learn the denoising action needed at each stage. | 模型学习每个阶段应该去掉什么噪声。 |
| Training Process | 训练过程 | The sequence in which a model learns from examples. | 从例子到学会规律的完整学习流程。 |
| Generation Process | 生成过程 | The sequence that turns noise into an output. | 从随机噪声到最终内容的一连串步骤。 |
| Process | 过程 | An ordered series of operations. | 按顺序完成的一组操作。 |
| Step | 步骤 | One operation in a larger process. | 流程中的一个小环节。 |
| Data Type | 数据类型 | A kind of data such as image, audio, or video. | 数据的类别，例如图片、声音或视频。 |
| Image | 图像 / 图片 | Visual data that can be learned or generated. | 模型可以学习和生成的视觉内容。 |
| Images | 图像（复数） | Multiple visual data examples. | 多张图片或图像数据。 |
| Audio | 音频 | Sound data that can be learned or generated. | 声音形式的数据。 |
| Video | 视频 | Time-ordered visual data, often made of frames. | 随时间变化、由连续画面组成的内容。 |
| Other Data | 其他数据 | Data types beyond image, audio, and video. | 不只是图片、声音和视频的其他数据。 |
| Image Generation | 图像生成 | Creating an image with a diffusion model. | 用模型生成一张新的图片。 |
| Image Editing | 图像编辑 | Changing part of an existing image with controlled denoising. | 在保留部分原图的同时修改图片内容。 |
| Existing Image | 现有图像 | An image supplied as input for editing. | 用户已经有、拿来修改的一张图片。 |
| Text Prompt | 文本提示词 | Text that guides what an image model should create. | 用文字告诉模型想生成什么内容。 |
| Prompt | 提示词 | An input instruction or description used to guide generation. | 指导模型生成结果的文字或输入说明。 |
| Conditioning Signal | 条件信号 | Extra information that guides generation. | 告诉模型生成方向的附加信息。 |
| Conditioned Generation | 条件生成 | Generation guided by a prompt or another signal. | 根据文字或其他条件来控制生成内容。 |
| Controlled Noise | 受控噪声 | Noise used in a way that helps control an edit or generation. | 按控制要求使用的噪声，而不是完全随意的噪声。 |
| Video Generation | 视频生成 | Producing a sequence of video frames. | 让模型生成连续的视频画面。 |
| Sequence | 序列 | An ordered set of items. | 按顺序排列的一组数据。 |
| Sequence of Frames | 帧序列 | Ordered video images over time. | 视频中按时间排列的一张张画面。 |
| Frame | 帧 | One still image in a video sequence. | 视频里的单张画面。 |
| Temporal Consistency | 时间一致性 | Keeping generated frames coherent across time. | 视频前后画面中的人物、物体和动作保持连贯。 |
| Real-World Example | 现实世界例子 | A practical use case for the model. | 模型在实际场景中的一种用法。 |
| Television Screen | 电视屏幕 | A screen used in the page's learning analogy. | 页面用来打比方的电视屏幕。 |
| Static | 电视雪花 / 静电噪点 | Random visual noise on a television screen. | 电视没信号时满屏的随机雪花点。 |
| Recognizable Image | 可辨认的图像 | An image whose content can be recognized. | 人能看出里面是什么的图片。 |
| Learning Analogy | 学习类比 | A simplified comparison used to explain an idea. | 为了帮助理解而使用的简化比喻。 |
| Not Literally Cleaning a Television Screen | 不是字面上的清理电视屏幕 | The television example is only an analogy. | 扩散模型并不是真的在擦电视屏幕。 |
| Transformer | Transformer 架构 | A neural-network architecture based on attention. | 依靠注意力机制处理信息的另一种神经网络架构。 |
| Neural-Network Architecture | 神经网络架构 | The structural design of a neural network. | 神经网络内部各部分如何组织的设计。 |
| Neural Network | 神经网络 | A model made of connected computational layers. | 由多层相互连接的计算单元组成的模型。 |
| Attention | 注意力机制 | A mechanism for weighting relevant parts of information. | 模型重点关注与当前任务更相关的信息部分。 |
| Deep Learning | 深度学习 | A machine-learning approach using neural networks with many layers. | 使用多层神经网络学习数据规律的方法。 |
| Generative AI | 生成式人工智能 | A broad category or capability for creating new content. | 能够创建新内容的一大类 AI 能力。 |
| Generative AI Capability | 生成式 AI 能力 | The ability to create new content from learned patterns. | 根据学到的规律做出新内容的能力。 |
| Generative AI Category | 生成式 AI 类别 | A broad category of content-creating AI systems. | 按“能生成新内容”划分的一类 AI 系统。 |
| Creating New Content | 创建新内容 | Producing new text, images, audio, video, or other data. | 产生以前没有的一份内容。 |
| Image Model | 图像模型 | A broad description of a model focused on image data or tasks. | 面向图像数据或图像任务的更宽泛说法。 |
| Autoregressive Model | 自回归模型 | A generative model that produces outputs step by step from prior outputs. | 依赖前面已经生成的内容，一步步生成后续内容的模型。 |
| Autoregressive | 自回归 | A model family that generates sequentially using previous values. | 根据之前的结果逐步产生后续结果的方法。 |
| GAN | 生成对抗网络缩写 | Short for Generative Adversarial Network. | Generative Adversarial Network 的英文缩写。 |
| Generative Adversarial Network | 生成对抗网络 | A generative model family based on adversarial training. | 通过两个模型互相对抗来训练生成能力的模型家族。 |
| VAE | 变分自编码器缩写 | Short for Variational Autoencoder. | Variational Autoencoder 的英文缩写。 |
| Variational Autoencoder | 变分自编码器 | A generative model family based on an encoder and decoder with a latent distribution. | 用编码器、解码器和潜在分布生成内容的一类模型。 |
| Model Type | 模型类型 | A category used to describe a model family or task. | 按方法、结构或用途给模型分的类别。 |
| Model Family | 模型家族 | A group of related model designs. | 结构或生成方式相近的一组模型。 |
| Generative Modeling Family | 生成式建模家族 | A related group of approaches for generating data. | 解决生成问题的一组相关方法。 |
| Generative Modeling Approach | 生成式建模方法 | A particular way to build a generative model. | 构建生成模型的一种具体路线。 |
| Category | 类别 | A broad grouping of related things. | 把相似事物归在一起的分类。 |
| Capability | 能力 | What a system can do. | 系统能够完成的事情。 |
| Task | 任务 | A purpose for which a model is used. | 使用模型要完成的具体事情。 |
| Data or Task | 数据或任务 | A basis for describing a model's scope. | 说明模型是按处理的数据还是按完成的任务来分类。 |
| Neural Networks & Model Architectures | 神经网络与模型架构 | The broader topic area containing this page. | 本页面所属的神经网络和模型结构主题。 |
| Reversing a Noising Process | 逆转加噪过程 | Generation reverses the gradual corruption of data. | 生成时沿着与加噪相反的方向，把数据还原出来。 |
| Corruption | 破坏 / 污染 | Making a data sample less informative through noise. | 噪声逐渐破坏原始数据中的可见信息。 |
| Signal | 信号 | The useful information mixed with noise. | 数据里真正有用、想保留下来的信息。 |
| Signal-to-Noise Intuition | 信噪直觉 | The idea that useful structure becomes clearer as noise is removed. | 噪声少了以后，真正内容会越来越明显。 |
| Sample | 样本 | One data instance used or produced by a model. | 一条输入数据或一份生成结果。 |
| Generated Sample | 生成样本 | One output produced by the model. | 模型生成出来的一份数据。 |
| Input | 输入 | Data supplied to a model or generation task. | 送进模型的内容，例如噪声、提示词或原图。 |
| Output Data | 输出数据 | Data returned by the generation process. | 生成流程最后得到的数据。 |
| Repeated Update | 重复更新 | Applying many small changes to a sample. | 反复对结果做小幅调整。 |
| Reveal Structure | 显露结构 | Make useful organization visible through denoising. | 通过去噪让原本隐藏的规律显现出来。 |
| Useful Direction | 有用方向 | The direction in which denoising improves the sample. | 能让结果逐渐变清晰、变有结构的方向。 |
| Model Output | 模型输出 | The result produced by the trained model. | 训练好的模型返回的结果。 |
| Text-to-Image | 文生图 | Generating an image from text. | 根据文字描述生成图片。 |
| Image-to-Image | 图生图 | Generating or editing an image from an image input. | 根据一张图片生成或修改另一张图片。 |
| Video Diffusion | 视频扩散 | Applying diffusion modeling to video data. | 把扩散模型用于视频生成的方向。 |
| Audio Diffusion | 音频扩散 | Applying diffusion modeling to audio data. | 把扩散模型用于音频生成的方向。 |
| Multimodal Data | 多模态数据 | Data involving more than one modality, such as text and image. | 同时涉及文字、图片、声音等不同形式的数据。 |
| Related Concept | 相关概念 | A concept connected to the topic. | 和扩散模型有关、可以继续学习的概念。 |
| Explore Next | 下一步探索 | A suggested related topic to read next. | 页面推荐继续了解的相关主题。 |
| Verified Video Explainer | 已验证的视频讲解 | A video explanation confirmed as a real asset. | 经过确认、确实存在的视频说明材料。 |
| Real Asset | 真实素材 | An actual media asset available for use. | 真实存在、可以使用的媒体文件。 |
| Video Not Available Yet | 视频暂不可用 | The page says no video is currently available. | 页面目前还没有可用的视频。 |
| Content Generation | 内容生成 | Creating new content with a model. | 用模型做出新的文字、图片、声音或视频。 |
| Data Generation | 数据生成 | Creating new data samples. | 让模型产生新的数据样本。 |
| Structured Output | 结构化输出 | An output whose useful organization has been generated. | 模型输出的内容具有可辨认的组织和结构。 |
| Denoising-Based Generation | 基于去噪的生成 | Generation that starts from noise and repeatedly denoises. | 先从噪声开始，再靠反复去噪生成内容。 |
| Noise-to-Data Generation | 从噪声到数据的生成 | Turning random noise into structured data. | 把随机噪声一步步变成有结构的数据。 |
| Model Architecture Comparison | 模型架构对比 | Comparing diffusion with architectures such as transformers. | 把扩散这种生成方法和 Transformer 这种架构区分开。 |
| Broader Description | 更宽泛的描述 | A label that covers multiple specific model approaches. | 范围更大、不只指某一种具体模型的方法。 |
| Not the Same as | 不等同于 | A boundary phrase used to separate related concepts. | 页面用来提醒读者两个相关词不是一回事。 |
| One Family | 一个家族 / 一类 | One model family among several alternatives. | 扩散只是生成模型家族中的一种。 |
| Currently Unavailable | 当前不可用 | Not available at the time of the page. | 页面说明某项内容现在还没有。 |

## Potential Missing Concepts

- **Forward diffusion / forward process（前向扩散／前向过程）**：页面描述“逐渐加噪”，但没有给出把干净样本变成噪声样本的正式过程名称。
- **Reverse diffusion / reverse process（反向扩散／反向过程）**：页面说 generation reverses noising，但没有把生成阶段正式命名为反向过程。
- **Diffusion timestep（扩散时间步）**：页面多次说 step，但没有定义噪声水平随时间步变化的索引。
- **Noise schedule / beta schedule（噪声调度／beta 调度）**：没有说明每个步骤加入多少噪声，以及噪声强度如何安排。
- **Gaussian noise（高斯噪声）**：页面只说 random noise，没有说明常见噪声分布。
- **Markov chain（马尔可夫链）**：没有解释扩散过程常以逐步、只依赖当前状态的链式过程表示。
- **Variance（方差）**：没有说明噪声强度或随机性的数学量化方式。
- **DDPM（去噪扩散概率模型）**：页面没有给出 Denoising Diffusion Probabilistic Models 这一经典算法名称。
- **DDIM（去噪扩散隐式模型）**：页面没有介绍常见的更快采样方法。
- **Score-based model（基于 score 的模型）**：没有讲 score function、score matching 或基于梯度的去噪视角。
- **Score function（得分函数）**：没有说明数据分布对数密度梯度这一核心概念。
- **Score matching（得分匹配）**：没有介绍训练 score function 的目标。
- **Denoising score matching（去噪得分匹配）**：没有介绍利用加噪样本学习 score 的方法。
- **SDE / stochastic differential equation（随机微分方程）**：没有介绍连续时间扩散的数学表达。
- **ODE / ordinary differential equation（常微分方程）**：没有介绍 probability flow ODE 或确定性采样视角。
- **Noise prediction / epsilon prediction（噪声预测／epsilon 预测）**：正文说 predict noise，但没有说明常见的 epsilon 参数化。
- **x0 prediction（x0 预测）**：没有区分直接预测干净样本与预测噪声。
- **v-prediction（v 预测）**：没有介绍另一种训练参数化。
- **Training objective（训练目标）**：没有给出预测噪声误差等具体优化目标。
- **ELBO / evidence lower bound（证据下界）**：没有解释概率扩散模型中的变分训练目标。
- **U-Net（U-Net 架构）**：页面没有说明图像扩散模型常用的去噪网络结构。
- **Diffusion Transformer / DiT（扩散 Transformer）**：页面提到 Transformer，但没有说明 Transformer 也可作为扩散去噪器。
- **Cross-attention（交叉注意力）**：text prompt 和 conditioning signal 出现了，但没有说明文字如何注入图像生成网络。
- **Text encoder（文本编码器）**：没有解释提示词如何先转换为模型可用表示。
- **CLIP（对比语言-图像预训练）**：没有提到常见的文本-图像条件或相似度模型。
- **Latent diffusion（潜空间扩散）**：没有区分在像素空间和潜空间中进行扩散。
- **Latent space（潜空间）**：没有解释压缩后的表示空间。
- **Pixel space（像素空间）**：没有解释直接在图像像素上进行扩散的方式。
- **VAE encoder / decoder（VAE 编码器／解码器）**：页面列出 VAE，但没有展开潜空间扩散中的编码与解码角色。
- **Sampler（采样器）**：页面说 many steps，但没有介绍如何从噪声轨迹采样输出。
- **Scheduler（调度器）**：没有说明推理时如何安排时间步和更新规则。
- **Sampling（采样）**：没有正式定义从随机分布取样并逐步生成的过程。
- **Inference（推理）**：页面讲 generation，但没有把训练后的生成阶段明确称为推理。
- **Sampling steps / inference steps（采样步数／推理步数）**：没有讨论步数对速度和质量的影响。
- **Guidance（引导）**：conditioning signal 出现了，但没有介绍引导强度和采样控制。
- **Classifier guidance（分类器引导）**：没有介绍用分类器梯度引导生成。
- **Classifier-free guidance / CFG（无分类器引导）**：没有介绍文本条件扩散中常用的 CFG。
- **Guidance scale（引导尺度）**：没有说明控制条件遵循程度的参数。
- **Random seed（随机种子）**：页面说 random noise，但没有介绍如何复现随机起点。
- **Inpainting（局部重绘）**：image editing 出现了，但没有命名只修改图像局部的任务。
- **Outpainting（扩图）**：没有介绍在原图边界外继续生成内容。
- **Super-resolution（超分辨率）**：没有列出以低分辨率内容生成高分辨率内容的任务。
- **Image restoration（图像修复）**：没有列出修复损坏或退化图像的任务。
- **ControlNet（控制网络）**：conditioning signal 出现了，但没有介绍结构化控制条件的常见架构。
- **Consistency model（一致性模型）**：没有介绍减少采样步数的相关模型路线。
- **Flow matching（流匹配）**：没有介绍与扩散相邻的连续生成训练方法。
- **Rectified flow（整流流）**：没有介绍另一类从噪声到数据的路径学习方法。
- **Diffusion distillation（扩散蒸馏）**：没有介绍将多步扩散压缩为更少步骤的蒸馏。
- **Model checkpoint（模型检查点）**：没有说明训练后保存和加载模型状态的文件。
- **FID / Fréchet Inception Distance（弗雷歇 Inception 距离）**：没有列出图像生成质量和分布相似度指标。
- **Inception Score（Inception 分数）**：没有列出另一种图像生成评估指标。
- **CLIP score（CLIP 分数）**：文本提示出现了，但没有介绍文本-图像一致性的评估。
- **Human evaluation（人工评估）**：页面没有讨论由人判断生成质量、相关性或真实感。
- **Prompt adherence（提示词遵循度）**：没有单独讨论输出是否符合文本条件。
- **Image quality（图像质量）**：页面说 recognizable image，但没有展开质量维度。
- **Temporal coherence（时间连贯性）**：页面提到 temporal consistency，但没有定义视频质量中的相关指标。
- **Compute（计算资源）**：没有讨论训练或推理的计算量。
- **VRAM / memory（显存／内存）**：没有讨论高分辨率、多帧生成的内存约束。
- **Latency（延迟）**：没有讨论多步去噪带来的响应时间。
- **Throughput（吞吐量）**：没有讨论单位时间可生成的样本数量。
- **Deployment（部署）**：没有说明如何把扩散模型提供给应用调用。
- **Model serving（模型服务）**：没有说明在线运行模型的服务形态。
- **Safety filter（安全过滤器）**：页面未展开生成内容筛选和安全策略。
- **NSFW detection（不适宜内容检测）**：没有讨论对图像生成结果进行不适宜内容检测。
- **Copyright / provenance（版权／来源追踪）**：没有讨论生成图像的版权、来源或内容溯源。
- **Watermarking（数字水印）**：没有讨论生成内容标记。
- **Model bias（模型偏差）**：没有讨论训练数据和生成结果中的偏见。
- **Privacy（隐私）**：没有讨论训练图像、音频、视频可能包含的敏感信息。

## Aliases / Synonyms

- Diffusion Model ↔ Diffusion ↔ diffusion model family ↔ noise-to-data generative model
- Diffusion Models ↔ diffusion modeling ↔ diffusion-based generation
- Generative Model ↔ generative modeling system ↔ content-generation model
- Generative AI ↔ GenAI ↔ generative artificial intelligence（Generative AI 是更宽的能力／类别，不是 Diffusion 的完全同义词）
- Noising Process ↔ forward noising ↔ noise addition ↔ gradual corruption
- Noise Removal ↔ remove noise ↔ denoising ↔ denoise
- Denoising Process ↔ reverse denoising ↔ repeated denoising
- Denoising Step ↔ denoise step ↔ iterative denoising update
- Random Noise ↔ starting noise ↔ initial noise ↔ random starting point
- Generated Output ↔ generated result ↔ model output ↔ generated sample
- Training Data ↔ training examples ↔ examples used for learning
- Conditioning Signal ↔ conditioning input ↔ generation condition ↔ control signal
- Text Prompt ↔ prompt ↔ text condition ↔ textual description
- Image Generation ↔ image synthesis ↔ text-to-image（text-to-image 是图像生成的一种特定形式）
- Image Editing ↔ image-to-image editing ↔ controlled image generation
- Video Generation ↔ video synthesis ↔ video diffusion
- Sequence of Frames ↔ frame sequence ↔ video sequence
- Temporal Consistency ↔ temporal coherence ↔ frame-to-frame consistency
- Structure ↔ recognizable structure ↔ organized pattern
- Signal ↔ useful information ↔ data structure（signal 不等于全部 data）
- Transformer ↔ Transformer architecture ↔ attention-based neural-network architecture
- Neural Network ↔ neural-network model ↔ artificial neural network
- Deep Learning ↔ deep neural-network learning
- GAN ↔ Generative Adversarial Network ↔ adversarial generative model
- VAE ↔ Variational Autoencoder ↔ variational generative model
- Autoregressive ↔ autoregressive model ↔ sequential generation
- Real-World Example ↔ practical use case ↔ application example
- Learning Analogy ↔ explanatory analogy ↔ teaching analogy
- Denoising-Based Generation ↔ noise-to-data generation ↔ iterative generation from noise
- Model Family ↔ model class ↔ model category
- Other Data ↔ non-image data ↔ additional data modalities
- Image Model ↔ vision model（image model 是按数据／任务的宽泛说法）

## Do Not Confuse Candidates

- **Diffusion Model vs Transformer**：Diffusion 是以加噪和去噪为核心的生成模型家族；Transformer 是以 attention 为核心的神经网络架构。两者属于不同分类维度，也可以组合使用。
- **Diffusion Model vs Generative AI**：Generative AI 是更宽的能力或类别；Diffusion 是其中一种生成模型家族。
- **Diffusion Model vs Image Model**：Diffusion 可以处理图像，也可以处理音频、视频或其他数据；Image Model 只是按数据或任务描述的更宽泛概念。
- **Diffusion vs Noising Process**：Diffusion 指完整的模型／方法家族；noising process 只是其中的加噪阶段。
- **Noising vs Denoising**：Noising 是逐渐加入噪声；denoising 是逐步移除噪声并恢复结构。
- **Noise vs Signal**：Noise 是随机干扰；signal 是希望保留的有用信息。
- **Random Noise vs Generated Output**：随机噪声是生成起点；generated output 是多次去噪后的结果。
- **Training vs Generation**：Training 学习如何预测或移除噪声；generation 使用学到的能力从噪声产生新输出。
- **Training Data vs Starting Noise**：训练数据是模型学习的例子；starting noise 是生成阶段的随机起点。
- **Predict Noise vs Generate Data**：predict noise 是模型在单个去噪阶段做的估计；generate data 是所有步骤共同完成的结果。
- **Denoising Step vs Denoising Process**：一个 denoising step 是一次更新；denoising process 是许多步骤组成的完整过程。
- **Denoising vs Image Editing**：去噪是底层操作；图像编辑是利用受控去噪完成的应用任务。
- **Image Generation vs Image Editing**：图像生成可以从随机噪声开始创建新图；图像编辑以现有图像为输入并修改其中一部分或整体。
- **Text Prompt vs Conditioning Signal**：text prompt 是条件信号的一种；conditioning signal 还可以是图像、类别或其他控制信息。
- **Image Generation vs Video Generation**：图像生成产出单张图；视频生成需要处理按时间排列的多帧并维持 temporal consistency。
- **Frame vs Video**：frame 是视频中的单张画面；video 是按时间组织的帧序列。
- **Temporal Consistency vs Image Quality**：temporal consistency 关注前后帧是否连贯；image quality 关注单张图像的视觉质量。
- **Generative Model vs Generative AI**：generative model 是模型或方法；generative AI 是更广的系统能力和类别。
- **Generative Model vs Autoregressive Model**：autoregressive 是生成模型家族之一，不是所有生成模型的同义词。
- **GAN vs VAE vs Diffusion**：三者都是生成模型家族，但训练机制和生成流程不同。
- **GAN vs Transformer**：GAN 是生成模型家族；Transformer 是网络架构，分类角度不同。
- **VAE vs Diffusion**：VAE 通常用编码器和解码器及潜在分布；Diffusion 以逐步加噪和去噪为核心。
- **Deep Learning vs Diffusion**：Deep Learning 是更广的学习方法领域；Diffusion 是一种生成建模家族。
- **Neural Network vs Neural-Network Architecture**：neural network 是模型；architecture 是描述模型内部结构的设计。
- **Transformer vs Attention**：Transformer 是使用 attention 的架构；attention 是其中的核心机制之一。
- **Structured Data vs Image Data**：图像数据也可以有结构；structured data 不是图像的同义词。
- **Recognizable Image vs Clean Image**：页面只用 recognizable 表达“能辨认”，不等于技术上完全无噪声或视觉质量最高。
- **Analogy vs Mechanism**：电视静电是帮助理解的 analogy；模型真实机制是数学化的加噪、预测和去噪过程。
- **Controlled Noise vs Random Noise**：controlled noise 强调被用于控制编辑或生成；random noise 只强调随机起点。
- **Conditioned Generation vs Unconditional Generation**：conditioned generation 使用 prompt 或其他条件；页面没有展开无条件生成，不能把两者混为一谈。
- **Model Family vs Model Architecture**：model family 按方法类别分组；architecture 描述网络内部结构，扩散模型可以使用不同架构。
- **Data Type vs Model Type**：data type 指图像、音频、视频等输入／输出类别；model type 指 Diffusion、GAN、VAE 等模型类别。
- **Content Generation vs Data Generation**：content generation 强调用户可见的新内容；data generation 是更宽的样本生成说法。
- **Output vs Input**：output 是模型产生的结果；input 是送入模型的噪声、prompt、原图或其他数据。
- **Noise Prediction vs Noise Schedule**：noise prediction 是模型估计噪声；noise schedule 是预先安排各步噪声强度的规则。
- **Sampling vs Training**：sampling 是从噪声轨迹生成样本；training 是让模型学会去噪规则。
- **Generation Steps vs Model Layers**：generation steps 是推理时反复更新的次数；model layers 是神经网络内部的层数。
- **Video Not Available Yet vs No Video Concept**：页面没有可用视频资产，不代表视频生成不是扩散模型的应用。

## Notes

- 本文件是 Module 02 的 raw glossary 收集稿，目标是最大化保留 `diffusion-models.html` 正文中的候选术语，不做最终去重、归并或取舍。
- 页面核心定义是：diffusion model 是一种 generative model，学习通过逆转 gradual noising process 来创建 data。
- 页面明确的训练主线是：从 examples 开始，逐渐 add noise，学习 predict / remove noise；页面明确的生成主线是：start from random noise，经过 repeated denoising，得到 generated output。
- 页面把学习类比成“电视屏幕满是 static，逐渐变成 recognizable image”，并明确指出这只是 learning analogy，不是模型真的在清理电视屏幕。
- 页面列出的训练数据类型包括 images、audio、video 和 other data；因此 raw 候选保留了跨模态数据和 data type 相关词。
- 页面列出的应用例子是 Image Generation、Image Editing 和 Video Generation；其中 image generation 可由 text prompt 或 other conditioning signal 指导，image editing 使用 controlled noise 和 denoising，video generation 关注 temporal consistency。
- 页面明确给出了三个边界对照：Diffusion Model ≠ Transformer、Diffusion Model ≠ Generative AI、Diffusion Model ≠ Image Model。这些对照已在 Do Not Confuse Candidates 中展开。
- 页面相关概念图将 Diffusion 放在 Deep Learning 与 Generative Model Families 之下，并列出 Diffusion、Autoregressive、GAN、VAE 四个生成模型家族候选。
- 页面只把 Transformer 解释为 attention-based neural-network architecture，没有展开 U-Net、latent diffusion、sampler、guidance、DDPM 等实现细节，因此这些内容列入 Potential Missing Concepts。
- 页面 related chips 链接到 Deep Learning、Transformer、Generative AI；GAN 和 VAE 在正文中出现但页面说明当前没有对应链接页面。
- 页面的 Video 区块标记为 not available yet，并说明真实视频资产可用后才会加入；这些是页面元信息候选，不应误认为扩散机制本身。
- 页面没有给出数学公式、具体算法名称、损失函数、噪声分布、采样器或评估指标；这些主题已作为 Potential Missing Concepts 保留，方便后续术语完整化。
- raw 阶段保留了 diffusion / denoising / generation 等词的名词、动词、短语形式，以及单数、复数和缩写，后续规范化阶段再决定最终显示形式。
