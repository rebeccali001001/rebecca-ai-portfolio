# Topic

Tokens, Context & Inference

## Module / Topic / Source File

- Module: 05 · Tokens, Context & Inference
- Topic: Inference
- Topic number: 05
- Source File: `inference.html`
- Extraction scope: Complete visible HTML正文，包括页面导航、定义、类比、流程、示例、反例、相关概念、记忆点和视频状态。
- Collection mode: Raw candidate collection; intentionally broad, with contextual variants, aliases, near-duplicates, abbreviations, process nodes, metrics, and potentially confusable concepts retained for later review.

## Glossary Candidates

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| inference | 推理；推断；推理执行 | Running a trained model on input to produce an output. | 把已经训练好的模型拿来处理输入并得到结果。 |
| inference process | 推理过程 | The process in which a model turns input into a result. | 模型从收到信息到给出结果的整个过程。 |
| model inference | 模型推理 | Using a model to calculate a prediction or generated result. | 让模型实际计算并产出结果。 |
| trained model | 训练好的模型 | A model that has learned from examples. | 已经从例子中学会规律、可以拿来使用的模型。 |
| trained | 训练好的 | Having learned patterns or parameters from data. | 已经经过训练、内部规律被调整好的状态。 |
| model | 模型 | A learned system that maps inputs to outputs. | 学会规律后，可以反复处理新信息的程序。 |
| run a model | 运行模型 | Execute the model on an input. | 让模型开始处理一条输入。 |
| use a model | 使用模型 | Apply a model to a task or input. | 把模型用于一个具体任务。 |
| input | 输入 | Information given to a model. | 送进模型的信息。 |
| new input | 新输入 | Data supplied for the current inference request. | 这一次刚交给模型、要它处理的信息。 |
| new data | 新数据 | Data the model receives after training. | 训练结束后模型要处理的新资料。 |
| unseen data | 未见数据 | Data not used as a training example. | 训练时没有给模型看过的数据。 |
| output | 输出 | The result returned by the model. | 模型处理后返回的结果。 |
| result | 结果 | What the model produces after processing input. | 模型算完后产生的东西。 |
| prediction | 预测 | A model-produced estimate or answer. | 模型根据输入估计出来的结果。 |
| make a prediction | 做出预测 | Use the model to estimate an answer or label. | 让模型判断可能的答案或类别。 |
| generate a result | 生成结果 | Produce a new result from input. | 根据输入产出一个结果。 |
| likely result | 可能的结果 | A result considered probable by the model. | 模型认为比较可能出现的结果。 |
| learned parameters | 学到的参数 | Numerical values learned during training. | 训练时调整、最后保存在模型里的数字。 |
| model parameters | 模型参数 | Internal numerical values that encode learned patterns. | 模型内部用来保存规律的一大批数字。 |
| parameters | 参数 | Values used by the model during computation. | 模型计算时会用到的内部数值。 |
| learned values | 学到的数值 | Values adjusted by training and used later. | 训练过程中不断调整并留下来的数字。 |
| training | 训练 | Learning patterns from examples. | 用许多例子让模型学会规律的过程。 |
| training phase | 训练阶段 | The stage when model parameters are learned. | 模型学习和调整内部数字的阶段。 |
| inference phase | 推理阶段 | The stage when learned parameters are applied to input. | 模型不再学习，而是用已学规律处理输入的阶段。 |
| training changes model parameters | 训练改变模型参数 | Training updates the model's learned numerical values. | 训练会改模型内部保存规律的数字。 |
| inference uses learned parameters | 推理使用学到的参数 | Inference applies existing parameters without learning them for each request. | 推理主要使用已经学好的数字，不是每次请求都重新训练。 |
| apply learned parameters | 应用学到的参数 | Use trained values in model computation. | 把训练留下的规律用于这次计算。 |
| prediction time | 预测时 | The time when a trained model makes a prediction. | 模型已经学完、现在要给出判断的时刻。 |
| serving-time computation | 服务时计算 | Computation performed while serving a model request. | 用户请求到来时，服务端实际进行的模型计算。 |
| model execution | 模型执行 | The act of carrying out a model's computation. | 把模型内部的计算步骤真正跑起来。 |
| execution process | 执行过程 | The ordered computation that produces a model result. | 模型按顺序计算并输出结果的过程。 |
| computation | 计算 | Numerical processing performed by the model. | 模型内部对数字进行的运算。 |
| compute | 计算；计算过程 | Carry out the operations needed for a result. | 执行产生结果所需的运算。 |
| apply | 应用 | Use learned values or a procedure on input. | 把已有的规律或方法用到输入上。 |
| process | 处理 | Transform input through model computation. | 模型把输入转换成结果的过程。 |
| receive new data | 接收新数据 | Take in data for the current request. | 收到这一次需要处理的信息。 |
| represent | 表示；表征 | Convert input into a form the model can use. | 把输入换成模型能读懂的形式。 |
| convert the input | 转换输入 | Change input into a model-readable representation. | 把原始输入变成可供模型计算的格式。 |
| model-readable | 模型可读的 | In a form that the model can process. | 模型能够接收和计算的形式。 |
| calculate | 计算 | Produce a numerical result from the input. | 通过运算得出结果。 |
| calculate a prediction | 计算预测 | Compute a likely label, value, or answer. | 算出模型认为可能的类别、数值或答案。 |
| predict | 预测 | Estimate an output from the input. | 根据输入猜测或判断结果。 |
| produce a result | 产生结果 | Create an output after computation. | 计算完成后给出结果。 |
| return | 返回 | Send a computed result back to the requester. | 把模型算出的内容交回去。 |
| generate output | 生成输出 | Produce and return model output. | 让模型产出并返回结果。 |
| prediction output | 预测输出 | An output representing a model prediction. | 表示模型判断结果的输出。 |
| generated output | 生成的输出 | New content produced by the model. | 模型新生成的内容。 |
| response | 回应；响应 | An output returned in response to a request. | 模型针对请求返回的回答。 |
| label | 标签；类别标签 | A category name assigned to an input. | 给输入贴上的类别名称。 |
| transcription | 转录；转写结果 | Text produced from spoken audio. | 把声音内容转换成的文字。 |
| next token | 下一个词元 | The next small text unit selected by a language model. | 语言模型下一步要输出的一个小文字单位。 |
| likely next token | 可能的下一个词元 | The next token the model considers most likely or samples. | 模型认为接下来可能出现的词元。 |
| next-token prediction | 下一个词元预测 | Predicting what text unit should come next. | 预测文字接下来应该出现什么。 |
| repeated next-token predictions | 反复的下一个词元预测 | Predict one token after another to form a response. | 一个词元接一个词元地预测，逐步组成回答。 |
| next-token prediction loop | 下一个词元预测循环 | Repeatedly predict and append tokens until generation ends. | 不断预测、追加文字，直到满足停止条件。 |
| generation | 生成 | Producing new content or output pieces. | 按规律创造新的内容或结果。 |
| generation step | 生成步骤 | One step that adds an output unit. | 每次新增一小段输出的步骤。 |
| output generation | 输出生成 | Creating the response returned to the user. | 逐步创造最后要返回的回答。 |
| stopping condition | 停止条件 | A condition that ends generation or execution. | 满足某个条件后停止继续生成或计算。 |
| prompt | 提示词；提示 | Text or other input that guides a model. | 告诉模型要做什么的输入。 |
| image | 图像；图片 | Visual data supplied to or processed by a model. | 可以交给模型分析的视觉信息。 |
| audio clip | 音频片段 | A short piece of audio input. | 一小段交给模型处理的声音。 |
| audio recording | 音频录音 | Recorded sound used as model input. | 录下来、可以交给语音模型处理的声音。 |
| other input | 其他输入 | Any supported input besides the examples listed. | 除文字、图片、音频外模型可以接收的其他信息。 |
| text input | 文本输入 | Written language supplied to the model. | 交给模型的一段文字。 |
| visual input | 视觉输入 | Image or other visual information supplied to the model. | 交给模型的图片等视觉信息。 |
| audio input | 音频输入 | Sound information supplied to the model. | 交给模型的声音信息。 |
| multimodal input | 多模态输入 | Input containing more than one kind of data. | 同时包含文字、图像、声音等不同类型的信息。 |
| input representation | 输入表示 | The model-usable form of an input. | 输入被转换后、模型内部使用的形式。 |
| representation | 表示；表征 | An internal form used to carry information. | 模型内部表达信息的形式。 |
| readable by the model | 模型可读取 | Encoded or formatted so model computation can use it. | 已经变成模型能处理的格式。 |
| classify | 分类 | Assign an input to a category. | 判断一个输入属于哪一类。 |
| classification | 分类任务 | Assigning a category label to an input. | 给输入分配一个类别的任务。 |
| image classification | 图像分类 | Predicting a category for an image. | 判断一张图片属于什么类别。 |
| category | 类别 | A group or class used for classification. | 把相似东西归在一起的一类。 |
| dog category | “狗”类别 | The dog label used as an example category. | 例子中代表狗的那个分类结果。 |
| category label | 类别标签 | A name representing a predicted class. | 表示模型分类结果的名称。 |
| speech recognition | 语音识别 | Turning spoken audio into recognized language. | 让模型识别人说了什么。 |
| transcription output | 转写输出 | Text returned from speech recognition. | 语音识别后返回的文字。 |
| language model | 语言模型 | A model that processes and generates language. | 学习文字规律、可以处理或生成文字的模型。 |
| language-model inference | 语言模型推理 | Running a language model on a prompt or context. | 让语言模型根据输入计算回答。 |
| language-model response | 语言模型回答 | Text produced by a language model. | 语言模型生成的一段回答。 |
| image model | 图像模型 | A model that processes or predicts from images. | 处理图片或从图片中判断结果的模型。 |
| audio model | 音频模型 | A model that processes sound. | 处理声音信息的模型。 |
| speech model | 语音模型 | A model designed for spoken audio tasks. | 专门处理人类语音的模型。 |
| model input | 模型输入 | The data supplied to the model. | 送进模型进行计算的数据。 |
| model output | 模型输出 | The result returned by the model. | 模型计算后返回的结果。 |
| input data | 输入数据 | Data supplied for processing. | 交给模型处理的资料。 |
| output data | 输出数据 | Data produced by processing. | 模型处理后产生的资料。 |
| prediction result | 预测结果 | The result of a model's prediction. | 模型对输入做出的预测。 |
| generated result | 生成结果 | New content produced during inference. | 推理过程中新生成的内容。 |
| label output | 标签输出 | A category label returned by the model. | 模型返回的类别名称。 |
| response output | 回应输出 | A response returned to a user or system. | 返回给人或另一个系统的回答。 |
| inference input | 推理输入 | Input used during inference rather than training. | 在推理阶段送给模型的数据。 |
| inference output | 推理输出 | Output produced during inference. | 推理阶段产生的结果。 |
| trained parameters | 训练所得参数 | Parameters learned during training and reused at inference. | 训练时学到、推理时继续使用的内部数字。 |
| parameter update | 参数更新 | Changing model parameters during training. | 训练时修改模型内部数字的动作。 |
| learned pattern | 学到的模式；规律 | A relationship learned from examples. | 模型从例子中总结出的规律。 |
| pattern | 模式；规律 | A repeated or useful relationship in data. | 数据中反复出现、可以利用的关系。 |
| model behavior | 模型行为 | How a model responds to different inputs. | 模型遇到不同输入时表现出来的反应。 |
| task behavior | 任务行为 | Model behavior for a particular task. | 模型在某个任务中表现出来的做法。 |
| execution | 执行 | Carrying out the model's learned computation. | 把模型的计算真正运行起来。 |
| inference-time | 推理时；推理阶段的 | Relating to the time a model is run on new input. | 模型处理新输入时发生的事情。 |
| training-time | 训练时；训练阶段的 | Relating to the time a model learns from data. | 模型从数据学习时发生的事情。 |
| runtime | 运行时 | The period when software or a model is executing. | 程序或模型正在运行的时间。 |
| serving | 服务；提供模型服务 | Making a model available to handle requests. | 把模型接到服务上，让请求可以调用它。 |
| model serving | 模型服务 | Hosting a model so it can receive inputs and return outputs. | 让模型在线接收请求并返回结果。 |
| request | 请求 | A call asking the model to process input. | 用户或系统要求模型处理信息的调用。 |
| model request | 模型请求 | A request sent to a model endpoint or runtime. | 发给模型服务的一次任务要求。 |
| request-response cycle | 请求—响应循环 | Send input, run inference, and receive output. | 发出请求、模型处理、收到回答的一轮过程。 |
| endpoint | 端点；接口地址 | A service location that accepts model requests. | 供程序发送模型请求的服务入口。 |
| API request | API 请求 | A programmatic request to run a model. | 程序通过 API 要求模型处理输入。 |
| batch inference | 批量推理 | Run inference on multiple inputs together. | 一次把多条输入交给模型处理。 |
| online inference | 在线推理 | Run inference as requests arrive. | 用户请求来了就即时处理。 |
| offline inference | 离线推理 | Run inference ahead of time on stored data. | 提前批量处理已经保存的数据。 |
| real-time inference | 实时推理 | Produce a result with little waiting after input. | 输入后很快返回结果的推理。 |
| latency | 延迟 | Time between receiving input and returning output. | 从交给模型到拿到结果要等多久。 |
| throughput | 吞吐量 | Amount of input or output handled in a period. | 一段时间内模型能处理多少请求或数据。 |
| tokens per second | 每秒词元数 | Number of tokens generated or processed per second. | 模型每秒生成或处理多少个词元。 |
| inference cost | 推理成本 | Resources or money needed to run a model. | 每次运行模型要消耗的计算资源或费用。 |
| compute cost | 计算成本 | Cost of the computation used for inference. | 为完成模型计算付出的资源和费用。 |
| memory use | 内存使用量 | Memory required while running the model. | 模型运行时占用多少内存。 |
| context window | 上下文窗口 | The input context available to a model for a request. | 一次推理时模型能看到的文字或信息范围。 |
| context | 上下文 | Information provided around the current input. | 帮助模型理解当前请求的相关信息。 |
| tokenization | 词元化；分词 | Splitting text into tokens before model computation. | 把文字切成模型处理的小单位。 |
| token | 词元；标记 | A small unit of text processed by a language model. | 语言模型处理文字时使用的小单位。 |
| token sequence | 词元序列 | An ordered list of tokens representing text. | 按顺序排列的一串词元。 |
| input tokens | 输入词元 | Tokens representing the input or prompt. | 输入文字被切分后的词元。 |
| output tokens | 输出词元 | Tokens generated as the response. | 模型生成回答时逐步产生的词元。 |
| token budget | 词元预算 | Maximum or planned number of tokens for a request. | 一次请求允许使用的词元数量。 |
| KV cache | KV 缓存 | Cached attention values reused during generation. | 生成回答时把已经算过的中间信息存起来，减少重复计算。 |
| key-value cache | 键值缓存 | The key and value states cached for attention. | 注意力计算中保存下来的 key 和 value 信息。 |
| attention state | 注意力状态 | Cached or computed information used to attend to context. | 模型判断上下文重点时使用的中间信息。 |
| context processing | 上下文处理 | Process the supplied context before or during generation. | 模型读取并计算当前上下文的过程。 |
| autoregressive generation | 自回归生成 | Generate each next token using previous tokens. | 每一步都参考前面已经生成的词元。 |
| decoding | 解码 | Select output tokens from model scores or probabilities. | 根据模型给出的可能性选择要输出的词元。 |
| sampling | 采样 | Select a possible output according to a probability distribution. | 按可能性随机挑选一个结果。 |
| greedy decoding | 贪心解码 | Always choose the highest-scoring next token. | 每一步都选当前分数最高的词元。 |
| temperature | 温度 | A setting that changes randomness in token selection. | 控制生成结果更保守还是更多样的参数。 |
| probability | 概率 | A numerical estimate of how likely an outcome is. | 用数字表示某个结果可能出现的程度。 |
| score | 分数；得分 | A numerical value used to compare possible outputs. | 用来比较不同结果可能性或优先级的数字。 |
| logit | 逻辑值；未归一化分数 | A raw model score before conversion to probabilities. | 模型先算出的、还没变成概率的原始分数。 |
| confidence | 置信度 | A measure of how strongly a model favors an output. | 模型对自己这个结果有多“确信”的数值。 |
| uncertainty | 不确定性 | Lack of certainty about whether an output is correct. | 模型结果可能不可靠、不能完全确定的程度。 |
| confidence score | 置信分数 | A score representing model confidence. | 表示模型对结果把握程度的数字。 |
| likely | 可能的 | Having a relatively high estimated probability. | 模型认为比较有可能发生或正确。 |
| most likely | 最可能的 | The option with the highest estimated probability. | 所有候选结果里模型认为最可能的那个。 |
| output selection | 输出选择 | Selecting which result or token to return. | 从多个可能结果中选出要输出的内容。 |
| prediction distribution | 预测分布 | Scores or probabilities across possible outputs. | 各种可能输出分别有多大可能性的整体情况。 |
| decision | 决定；判断 | Choosing an output or action from the computation. | 根据计算结果选定一个答案、类别或动作。 |
| decision boundary | 决策边界 | A boundary separating different predicted categories. | 把不同分类结果分开的界线。 |
| classification decision | 分类判断 | The model's choice of a category. | 模型把输入归到某个类别的决定。 |
| input-processing-output | 输入—处理—输出 | A simple view of turning input into output. | 信息进来、系统处理、结果出去的基本流程。 |
| input-process-output flow | 输入—处理—输出流程 | The end-to-end flow from data to result. | 从输入到处理再到输出的一整条路径。 |
| process flow | 处理流程 | Ordered steps that turn input into output. | 把信息变成结果时依次经过的步骤。 |
| workflow | 工作流程 | A sequence of steps for completing a task. | 完成任务时按顺序执行的一组步骤。 |
| step | 步骤 | One stage in a process. | 流程中的一个环节。 |
| process node | 流程节点 | A named stage in a processing flow. | 流程图中代表一个动作或阶段的节点。 |
| input step | 输入步骤 | The stage where new data is received. | 流程中接收新数据的环节。 |
| represent step | 表示步骤 | The stage where input is converted into a usable form. | 流程中把输入转换成模型可用形式的环节。 |
| compute step | 计算步骤 | The stage where the model is run. | 流程中真正执行模型运算的环节。 |
| predict step | 预测步骤 | The stage where a prediction or likely next token is calculated. | 流程中计算预测结果的环节。 |
| return step | 返回步骤 | The stage where output is sent back. | 流程中把标签、转录或回应交回去的环节。 |
| receive | 接收 | Take in data or a request. | 收到输入信息或请求。 |
| convert | 转换 | Change data into another usable form. | 把数据变成另一种可用格式。 |
| apply | 应用 | Use learned parameters in computation. | 使用模型已经学到的参数。 |
| calculate | 计算 | Work out a prediction or result. | 通过运算得出预测或结果。 |
| produce | 产生；生成 | Make an output or result. | 产出结果。 |
| return output | 返回输出 | Send the result to a user or another system. | 把结果交给用户或下一个系统。 |
| input source | 输入来源 | The source supplying data to the model. | 提供输入的地方或材料。 |
| user input | 用户输入 | Information supplied by a person. | 人交给模型的文字、图片或其他信息。 |
| system input | 系统输入 | Information supplied by another software system. | 另一个程序传给模型的信息。 |
| input modality | 输入模态 | The type of input, such as text, image, or audio. | 输入属于文字、图像、声音等哪一种形式。 |
| output modality | 输出模态 | The type of result, such as label, text, or audio. | 输出是标签、文字、音频等哪一种形式。 |
| label output | 标签输出 | A category returned by an inference request. | 推理后返回的类别名称。 |
| transcription output | 转录输出 | Text returned from audio inference. | 音频推理后返回的文字。 |
| response output | 回应输出 | A natural-language response returned by a model. | 模型返回的一段自然语言回答。 |
| input-output mapping | 输入—输出映射 | The relationship between a model input and its output. | 模型如何把某种输入对应到某种结果。 |
| mapping | 映射 | A rule or learned relationship from inputs to outputs. | 把输入对应到输出的关系。 |
| function | 函数 | A rule that maps an input to an output. | 输入进去后按某种关系得到输出的计算方式。 |
| learned function | 学到的函数 | A mapping learned from training data. | 模型通过训练学会的输入到输出关系。 |
| model prediction | 模型预测 | A result estimated by a model. | 模型对输入作出的估计。 |
| inference result | 推理结果 | The result of running the model on an input. | 模型完成一次推理后得到的结果。 |
| model result | 模型结果 | Any output produced by the model. | 模型返回的任何结果。 |
| correct result | 正确结果 | An output that matches the intended or expected answer. | 与正确答案或任务要求相符的结果。 |
| incorrect result | 错误结果 | An output that does not match the expected answer. | 与正确答案不相符的结果。 |
| quality | 质量 | How correct, useful, and suitable an output is. | 结果是否正确、有用、合适。 |
| safety | 安全性 | Whether output avoids harmful or unsafe behavior. | 结果是否会带来伤害或风险。 |
| fit | 适配度；适用性 | How well a result matches the task and context. | 结果是否真的符合当前任务和场景。 |
| quality of inference | 推理质量 | How well inference produces useful and correct results. | 模型推理结果的正确性、实用性和合适程度。 |
| reliability | 可靠性 | How consistently a model produces acceptable results. | 模型能不能稳定地产出可用结果。 |
| robustness | 稳健性 | Ability to remain useful across changing inputs or conditions. | 输入有变化时模型仍能正常工作的能力。 |
| evaluation | 评估 | Testing a model's quality and limits. | 用测试检查模型效果和适用范围。 |
| test | 测试 | An example or procedure used to check performance. | 用来检验模型表现的案例或过程。 |
| metric | 指标 | A measurable quantity used to assess a model. | 用数字衡量模型表现的标准。 |
| accuracy | 准确率 | The fraction of predictions that are correct. | 预测正确的比例。 |
| error rate | 错误率 | The fraction of predictions that are wrong. | 预测错误的比例。 |
| precision | 精确率 | Among predicted positives, the fraction that is correct. | 模型判为某类的结果中，真正正确的比例。 |
| recall | 召回率 | Among actual positives, the fraction found by the model. | 所有真正属于某类的情况中，模型找出来的比例。 |
| F1 score | F1 分数 | A combined measure of precision and recall. | 综合衡量精确率和召回率的指标。 |
| latency metric | 延迟指标 | A measure of how long inference takes. | 衡量推理要等多久的指标。 |
| throughput metric | 吞吐量指标 | A measure of how many requests inference handles. | 衡量单位时间能处理多少请求的指标。 |
| quality check | 质量检查 | A check that output meets expected standards. | 检查结果是否达到要求。 |
| safety check | 安全检查 | A check for harmful or unsafe output. | 检查结果有没有安全风险。 |
| fit check | 适用性检查 | A check that output matches its intended use. | 检查结果放在当前场景里是否合适。 |
| review | 审核；复核 | Checking whether an output is correct, safe, and suitable. | 人或系统检查结果能不能使用。 |
| human review | 人工审核 | A person checks an important or uncertain result. | 由人检查重要或不确定的模型结果。 |
| human-in-the-loop | 人在回路中 | A workflow where a person reviews or approves system results. | AI 做一部分，人保留检查和决定权。 |
| HITL | 人在回路中（HITL） | Abbreviation for human-in-the-loop. | human-in-the-loop 的英文缩写。 |
| human oversight | 人工监督 | Human monitoring or control over model behavior. | 人持续看着模型并在必要时介入。 |
| human approval | 人工批准 | A person explicitly approves an output or action. | 重要结果或动作必须得到人的同意。 |
| uncertain result | 不确定结果 | An output whose correctness or fit is unclear. | 看起来可能对，但不能放心直接使用的结果。 |
| review loop | 复核闭环 | A workflow in which review feeds future improvement. | 结果被检查，反馈再帮助后续改进的循环。 |
| feedback | 反馈 | Information used to improve later behavior. | 帮助模型或流程下次做得更好的信息。 |
| model limitation | 模型局限 | A condition under which a model may fail or be unsuitable. | 模型能力不够或不适用的地方。 |
| model boundary | 模型边界 | The limit of what model inference should be taken to mean. | 模型“能做到哪里”的范围界线。 |
| conceptual boundary | 概念边界 | The distinction between related ideas. | 容易混淆的概念之间的范围区别。 |
| reasoning | 推理；推理行为 | Possible problem-solving behavior described at a higher level. | 看起来像分步骤解决问题的行为描述。 |
| problem-solving behavior | 问题解决行为 | Behavior that appears to work through a problem. | 处理问题、寻找答案时表现出来的行为。 |
| model execution vs reasoning | 模型执行与推理行为 | Execution is running the model; reasoning describes possible behavior. | “模型跑起来”是执行，“像在解题”是对行为的描述。 |
| training vs inference | 训练与推理 | Training changes learned values; inference applies them. | 训练负责学习和改数字，推理负责使用这些数字。 |
| inference vs next-token prediction | 推理与下一个词元预测 | Inference is broader; next-token prediction may repeat inside it. | 推理是完整运行过程，预测下一个词元只是其中可能反复发生的一步。 |
| inference vs reasoning | 推理与推理行为 | Inference means execution; reasoning refers to possible problem-solving behavior. | inference 是技术执行，reasoning 是可能表现出的解题行为。 |
| real-world example | 真实世界示例 | An example of inference in practical use. | 模型推理在实际场景中的一个例子。 |
| dog | 狗 | The example image-classification category. | 页面用来说明分类结果的“狗”这个类别。 |
| image becomes a category | 图像变成类别 | Image classification maps a picture to a label. | 模型看图片后给它贴上类别标签。 |
| prompt produces a response | 提示产生回应 | A language model turns a prompt into text. | 语言模型根据提示生成一段回答。 |
| audio recording becomes a transcription | 音频录音变成转写 | Speech inference converts recorded sound into text. | 模型把录音里的话写成文字。 |
| output type | 输出类型 | The form of result returned by inference. | 推理最后返回的是标签、文字还是其他形式。 |
| classification output | 分类输出 | A category label returned for an input. | 模型返回的类别结果。 |
| language generation | 语言生成 | Producing text from a prompt or context. | 根据提示和上下文生成文字。 |
| speech-to-text | 语音转文字 | Convert spoken audio into written text. | 把人说的话变成文字。 |
| image-to-label | 图像到标签 | Map an image to a category label. | 把图片判断成某个类别。 |
| inference use case | 推理用例 | A practical task performed by running a model. | 使用模型推理来完成的具体任务。 |
| input modality: prompt | 输入模态：提示 | Textual instruction or material supplied to a model. | 以文字提示形式输入模型的信息。 |
| input modality: image | 输入模态：图像 | A visual input supplied to a vision model. | 交给视觉模型的一张图片。 |
| input modality: audio clip | 输入模态：音频片段 | A short sound input supplied to an audio model. | 交给音频模型的一段声音。 |
| output modality: label | 输出模态：标签 | A category name returned by classification. | 分类任务返回的类别名字。 |
| output modality: transcription | 输出模态：转录 | Text returned from speech recognition. | 语音识别返回的文字。 |
| output modality: response | 输出模态：回应 | Text returned as an answer to a prompt. | 根据提示返回的回答文字。 |
| related concept | 相关概念 | A concept connected to inference. | 和 inference 有关系、可以一起理解的概念。 |
| concept tree | 概念链；概念树 | An ordered relationship among related concepts. | 把相关概念按先后和关系串起来的图。 |
| context window | 上下文窗口 | The context available to the model during inference. | 模型一次能看到和参考的信息范围。 |
| input → context window → inference → next-token prediction → output | 输入 → 上下文窗口 → 推理 → 下一个词元预测 → 输出 | A conceptual chain from supplied information to generated result. | 从输入开始，经过上下文和模型计算，逐步得到输出的关系链。 |
| tokenization | 词元化；分词 | Converting text into tokens before inference. | 把文字切成模型能处理的小单位。 |
| KV cache | KV 缓存 | Reused key-value states that can speed up generation. | 把已经算过的上下文中间结果留下来，生成时少算一些。 |
| coming soon | 即将推出 | A related topic not yet available on the page. | 这个相关主题目前还没有页面，之后可能补上。 |
| unavailable | 不可用；暂未提供 | A link or resource that is not currently available. | 目前还不能打开或使用的内容。 |
| video | 视频 | A visual or spoken explainer resource. | 用视频解释主题的资源。 |
| independent explainer | 独立讲解 | An explainer not presented as the main page text. | 独立于正文之外的讲解内容。 |
| explainer video | 讲解视频 | A video that explains inference. | 专门解释 inference 的视频。 |
| not yet available | 尚未提供 | The resource does not exist or is not ready yet. | 现在还没有可用的资源。 |
| video caption | 视频说明 | Text describing the video resource. | 页面上对视频状态的文字说明。 |
| trained model on new input | 在新输入上运行训练好的模型 | The core definition of inference. | 用已学会规律的模型处理这次的新信息。 |
| output for a request | 请求对应的输出 | The result returned for one inference request. | 一次请求对应得到的模型结果。 |
| model-generated response | 模型生成的回应 | A response produced by model computation. | 模型计算后新生成的一段回答。 |
| model-produced label | 模型产生的标签 | A category label predicted by the model. | 模型判断出来的类别名称。 |
| model-produced transcription | 模型产生的转写 | Text produced by processing audio. | 模型把声音识别后生成的文字。 |
| model output form | 模型输出形式 | The kind of output a model returns. | 模型最后返回的是哪一种结果格式。 |
| output recipient | 输出接收方 | A user or another system receiving model output. | 接收模型结果的人或另一个程序。 |
| downstream system | 下游系统 | Another system that uses the model's output. | 接着使用模型结果的后续系统。 |
| inference pipeline | 推理管线 | The connected stages from input preparation to output. | 从准备输入、运行模型到返回结果的一串处理环节。 |
| input preparation | 输入准备 | Preparing data in the form required by the model. | 把原始资料整理成模型可以接收的格式。 |
| preprocessing | 预处理 | Transforming raw input before model computation. | 模型正式计算前先整理和转换输入。 |
| postprocessing | 后处理 | Transforming raw model output into a usable result. | 模型算完后把结果整理成用户能看懂或系统能用的形式。 |
| output formatting | 输出格式化 | Formatting the result for a user or another system. | 把模型结果整理成需要的显示或数据格式。 |
| inference pipeline stage | 推理管线阶段 | One named stage in the inference pipeline. | 推理管线中的一个明确环节。 |
| model call | 模型调用 | A request that executes a model. | 程序或用户触发模型运行的一次调用。 |
| inference request | 推理请求 | A request to run a trained model on supplied input. | 要求模型处理一份输入的请求。 |
| inference service | 推理服务 | A service that runs models for callers. | 专门接收请求并运行模型的服务。 |
| inference engine | 推理引擎 | Software that executes a model efficiently. | 负责高效运行模型计算的软件。 |
| hardware accelerator | 硬件加速器 | Hardware used to speed up model computation. | 帮模型更快完成运算的专用硬件。 |
| CPU inference | CPU 推理 | Run model inference on a CPU. | 用通用处理器运行模型。 |
| GPU inference | GPU 推理 | Run model inference on a GPU. | 用适合并行计算的显卡运行模型。 |
| inference optimization | 推理优化 | Changes that reduce inference cost or time. | 让模型运行更快、更省资源或更便宜的改进。 |
| quantization | 量化 | Use lower-precision numbers to reduce model cost. | 用更小的数字精度运行模型，以节省内存和计算。 |
| batching | 批处理 | Group multiple inputs into one computation. | 把多条输入凑成一批一起计算。 |
| caching | 缓存 | Store reusable computation for later requests. | 把可以重复使用的计算结果暂时保存起来。 |
| deterministic inference | 确定性推理 | Inference that gives the same result for the same input and settings. | 输入和设置相同时，通常得到同样结果的运行方式。 |
| stochastic inference | 随机性推理 | Inference where sampling can produce different outputs. | 因为随机选择，同样输入可能产生不同结果的运行方式。 |
| reproducibility | 可复现性 | Ability to reproduce an inference result. | 之后按同样条件能否得到相同或相近结果。 |
| failure | 失败 | A case where inference cannot produce a usable result. | 模型没有正常给出可用结果的情况。 |
| error handling | 错误处理 | Steps taken when inference fails or returns a problem. | 模型出错时系统如何回应和继续工作的机制。 |
| fallback | 备用方案；降级处理 | An alternative path when the main inference path fails. | 主模型不能用时改走的替代办法。 |
| timeout | 超时 | A request taking longer than the allowed time. | 模型太久没返回，系统停止等待。 |
| retry | 重试 | Run a failed request again. | 请求失败后再尝试一次。 |
| hallucination | 幻觉 | A plausible-looking but unsupported or incorrect model output. | 模型说得像真的一样，但内容可能是编造或错误的。 |
| unsafe output | 不安全输出 | Output that could cause harm or violate safety requirements. | 可能带来伤害或风险的模型结果。 |
| privacy | 隐私 | Protection of sensitive information in model inputs and outputs. | 防止输入和输出里的敏感信息被不当使用或泄露。 |
| security | 安全防护 | Protection of the model service and its data. | 防止模型、接口和数据被攻击或滥用。 |
| data quality | 数据质量 | Correctness and usefulness of input data. | 输入资料是否准确、完整、适合处理。 |
| distribution shift | 数据分布变化 | A change between training data and inference inputs. | 线上新数据和训练时见过的数据规律不一样。 |
| generalization | 泛化 | Applying learned patterns successfully to new inputs. | 模型不只会做训练例题，也能处理新情况。 |
| overfitting | 过拟合 | Memorizing training examples instead of learning general patterns. | 模型只记住练习题，遇到新题就不会。 |
| underfitting | 欠拟合 | Failing to learn enough useful patterns. | 模型连训练数据中的基本规律都没学好。 |
| bias | 偏差 | A systematic tendency that makes outputs inaccurate or unfair. | 模型结果持续向某个方向偏，可能导致不准或不公平。 |
| fairness | 公平性 | Whether model quality and treatment are acceptable across groups. | 模型对不同人群是否都尽量公平。 |
| explainability | 可解释性 | Ability to explain why a model produced an output. | 能不能说清楚模型为什么给出这个结果。 |
| interpretability | 可理解性 | How understandable the model's behavior or output is. | 人能不能理解模型的判断过程或结果。 |
| model monitoring | 模型监控 | Watching model quality, latency, and failures after deployment. | 模型上线后持续观察效果、速度和错误。 |
| deployment | 部署 | Put a model into a usable environment or service. | 把模型放到真实系统里供人或程序调用。 |
| production inference | 生产环境推理 | Inference performed in a live product or business system. | 正式上线的产品或业务系统中的模型运行。 |
| local inference | 本地推理 | Run inference on a local device or machine. | 在自己的电脑或设备上运行模型。 |
| cloud inference | 云端推理 | Run inference on remote cloud infrastructure. | 把请求发到云端服务器运行模型。 |
| inference platform | 推理平台 | Infrastructure for deploying and running model inference. | 用来部署、运行和管理模型推理的系统。 |
| user-facing output | 面向用户的输出 | Model output shown or delivered to a user. | 最终展示给人的模型结果。 |
| machine-readable output | 机器可读输出 | Output formatted for another program to consume. | 按程序能继续读取的格式返回的结果。 |

## Potential Missing Concepts

- **algorithm（算法）**：正文讲了模型如何计算，但没有单独解释完成计算的一套明确步骤。
- **dataset（数据集）**：正文出现 data、new data 和 examples，但没有定义数据集如何组织。
- **feature（特征）**：正文提到图像、音频和文本中的信息，但没有说明输入中可用于预测的属性。
- **target / target value（目标／目标值）**：prediction、label 和 expected result 出现了，但没有统一解释监督学习中的目标值。
- **loss function / objective function（损失函数／目标函数）**：正文说 training changes parameters，却没有说明训练如何量化错误。
- **parameter vs hyperparameter（参数与超参数）**：页面解释 learned parameters，但没有区分训练学出的参数与训练前设置的超参数。
- **generalization（泛化）**：页面强调 new input，但没有说明模型从训练例子推广到新情况的能力。
- **overfitting / underfitting（过拟合／欠拟合）**：没有讨论只记住训练例子或学习不足的情况。
- **training set / validation set / test set（训练集／验证集／测试集）**：出现 trained model、new input 和 evaluation，但没有介绍数据拆分。
- **accuracy / precision / recall / F1 score（准确率／精确率／召回率／F1 分数）**：页面说 prediction、classification 和 quality，但没有列出具体评估指标。
- **confidence / uncertainty calibration（置信度／不确定性校准）**：页面保留 uncertain result，但没有说明置信度是否可靠以及如何校准。
- **calibration（校准）**：没有解释预测概率与实际正确率是否一致。
- **confusion matrix（混淆矩阵）**：image classification 出现，但没有展示分类错误的分布。
- **precision-recall trade-off（精确率—召回率权衡）**：没有说明不同阈值会怎样改变分类指标。
- **threshold（阈值）**：classification decision 出现，但没有说明把分数变成类别时的界限。
- **bias（偏差）**：页面谈 safety 和 quality，但没有展开数据偏差或模型偏差。
- **fairness（公平性）**：没有说明不同群体上的表现差异。
- **explainability / interpretability（可解释性／可理解性）**：没有介绍如何理解模型为什么产生某个结果。
- **data quality（数据质量）**：页面有 image、audio、prompt 等输入，但没有讲输入错误如何影响推理。
- **data preprocessing（数据预处理）**：represent 和 convert the input 出现，但没有解释清洗、缩放、格式转换等工作。
- **postprocessing（后处理）**：页面说 return 和 generate output，但没有解释如何把原始模型结果整理给用户或下游系统。
- **embedding（嵌入）**：representation 出现，但没有解释文本、图像或音频如何变成向量。
- **vector（向量）**：内部数字表示出现，但没有讲向量作为数据结构的含义。
- **forward pass（前向传播）**：compute 和 apply learned parameters 出现，但没有介绍输入如何经过各层得到预测。
- **backpropagation（反向传播）**：training changes parameters 出现，但没有解释训练时误差如何用于更新参数。
- **neural network weights（神经网络权重）**：learned parameters 出现，但没有具体说明权重如何影响计算。
- **activation function（激活函数）**：模型内部计算未展开，未说明网络如何引入非线性。
- **attention / Transformer（注意力／Transformer）**：context window 和 language model 出现，但没有说明现代语言模型的核心架构。
- **large language model / LLM（大语言模型／LLM）**：language model 出现，但没有定义“大规模”以及 LLM 的范围。
- **multimodal AI（多模态 AI）**：页面同时列出 prompt、image、audio clip，但没有解释多种模态如何共同处理。
- **autoregressive generation（自回归生成）**：repeated next-token predictions 暗示了它，但没有使用该术语解释生成机制。
- **decoding（解码）**：next-token prediction 出现，但没有解释如何把分数或概率变成实际输出。
- **sampling（采样）**：likely next token 出现，但没有介绍概率采样与确定性选择的差别。
- **temperature（温度）**：生成过程没有讲控制随机性的设置。
- **top-k / top-p（Top-k／Top-p）**：没有介绍限制候选词元的常用解码策略。
- **logit（逻辑值／未归一化分数）**：没有解释模型输出概率前的原始分数。
- **softmax（Softmax）**：没有解释如何把分数转换成概率分布。
- **context window limit（上下文窗口限制）**：context window 作为相关概念出现，但没有说明输入长度限制。
- **KV cache（KV 缓存）**：被列为 related concept，但没有解释它如何减少生成时的重复计算。
- **prefill / decode（预填充／解码阶段）**：没有区分处理输入上下文和逐词元生成的阶段。
- **batch inference（批量推理）**：正文没有区分一次处理一条输入与批量处理。
- **online inference / offline inference（在线推理／离线推理）**：页面没有说明即时请求与预先批处理的差异。
- **real-time inference（实时推理）**：没有讨论实时系统的时延要求。
- **latency（延迟）**：没有讨论从输入到输出的等待时间。
- **throughput（吞吐量）**：没有讨论单位时间能处理多少请求。
- **tokens per second（每秒词元数）**：没有列出生成速度指标。
- **time to first token / TTFT（首词元时间／TTFT）**：没有说明用户看到第一段输出要等多久。
- **cost / compute（成本／计算资源）**：没有讨论推理所需的算力、内存和费用。
- **memory use（内存使用量）**：没有讨论模型运行时的内存占用。
- **inference engine（推理引擎）**：没有介绍实际执行模型的运行软件。
- **hardware accelerator（硬件加速器）**：没有讨论 CPU、GPU 或其他硬件对推理的影响。
- **CPU inference / GPU inference（CPU 推理／GPU 推理）**：页面没有比较不同计算硬件。
- **inference optimization（推理优化）**：没有说明如何降低推理时间或成本。
- **quantization（量化）**：没有说明降低数值精度如何节省资源。
- **batching（批处理）**：没有讲把多条输入合并计算的方式。
- **caching（缓存）**：KV cache 被提及，但一般缓存机制没有展开。
- **deterministic / stochastic inference（确定性／随机性推理）**：没有解释同样输入为何可能得到不同输出。
- **random seed（随机种子）**：没有说明如何控制采样结果的可复现性。
- **reproducibility（可复现性）**：页面没有讨论如何重复得到同样结果。
- **serving（服务）**：model execution 被说明，但没有展开模型如何被部署成服务。
- **model serving（模型服务）**：没有介绍接收请求并返回结果的线上组件。
- **endpoint / API request（端点／API 请求）**：正文没有说明程序如何调用推理。
- **request-response cycle（请求—响应循环）**：input 和 output 出现，但没有以服务交互方式说明一轮调用。
- **deployment（部署）**：页面没有介绍模型上线到真实环境的过程。
- **production inference（生产环境推理）**：没有区分教学示例和正式业务运行。
- **local inference / cloud inference（本地推理／云端推理）**：没有比较设备本地和远程服务器运行。
- **monitoring（监控）**：没有介绍上线后观察质量、时延和失败的方法。
- **failure handling（失败处理）**：页面没有讲模型失败、超时、重试或备用路径。
- **fallback（降级／备用方案）**：没有说明推理失败后的替代路径。
- **timeout / retry（超时／重试）**：没有介绍服务请求的错误处理。
- **hallucination（幻觉）**：页面要求 review，但没有具体说明生成式模型虚构内容的风险。
- **unsafe output（不安全输出）**：safety 出现，但没有列出有害内容、隐私等具体风险。
- **privacy / security（隐私／安全防护）**：输入可能包含敏感信息，但页面没有展开保护机制。
- **distribution shift（分布偏移）**：new input 出现，但没有说明线上输入与训练数据分布变化。
- **drift（漂移）**：没有讨论数据或模型表现随时间变化。
- **data leakage（数据泄漏）**：没有说明训练和推理之间可能发生的信息泄漏。
- **human approval（人工批准）**：human review 出现，但没有规定哪些输出或动作必须经人批准。
- **output schema（输出模式）**：return a label、transcription、response 出现，但没有说明固定输出结构。
- **structured output（结构化输出）**：没有解释如何保证模型返回机器可读格式。
- **machine-readable output（机器可读输出）**：页面没有区分给人看的回答与给下游系统消费的数据。

## Aliases / Synonyms

- inference ↔ model inference ↔ inference process ↔ model execution ↔ prediction time ↔ serving-time computation（工程语境中范围可能不同）
- run a trained model ↔ use a trained model ↔ apply learned parameters ↔ execute the model
- input ↔ model input ↔ inference input ↔ new input ↔ new data（new input 强调当前请求；不等同于所有输入）
- output ↔ model output ↔ inference output ↔ result ↔ response ↔ generated result（response、generated result 是输出的具体形式）
- prediction ↔ model prediction ↔ prediction result ↔ make a prediction
- prediction ↔ likely next token prediction（后者是语言生成中的一种具体预测）
- generate a result ↔ produce a result ↔ generate output ↔ output generation
- learned parameters ↔ trained parameters ↔ model parameters ↔ learned values（learned values 可能比 parameters 更宽泛）
- training ↔ training phase ↔ training-time ↔ learning phase
- inference phase ↔ inference-time ↔ prediction time ↔ serving time
- represent ↔ convert the input ↔ create an input representation ↔ make it readable by the model
- calculate ↔ compute ↔ perform computation ↔ run the model
- predict ↔ estimate ↔ calculate a likely result
- return ↔ return output ↔ send back the result
- label ↔ category label ↔ class label ↔ classification output
- transcription ↔ transcription output ↔ speech-to-text output ↔ transcribed text
- response ↔ language-model response ↔ model-generated response
- token ↔ text unit ↔ language-model token ↔ wordpiece（具体切分方式不一定相同）
- next-token prediction ↔ next token prediction ↔ likely next-token prediction ↔ autoregressive token prediction
- generation ↔ text generation ↔ language generation ↔ output generation
- prompt ↔ instruction input ↔ textual input（prompt 是 input 的一种，不是所有 input 都是 prompt）
- image ↔ picture ↔ visual input（image 是视觉输入的一种）
- audio clip ↔ audio recording ↔ sound input ↔ audio input
- image classification ↔ image-to-label ↔ visual classification
- speech recognition ↔ speech-to-text ↔ audio-to-transcription
- language model ↔ text model（language model 不一定是 large language model）
- context window ↔ available context ↔ model context（context window 是模型可见上下文的容量或范围）
- tokenization ↔ tokenization process ↔ text splitting into tokens
- KV cache ↔ key-value cache ↔ attention cache
- classification ↔ categorization ↔ labeling（labeling 也可指给训练数据加标签的动作）
- review ↔ human review ↔ manual review ↔ human verification
- human-in-the-loop ↔ HITL ↔ human oversight ↔ human review workflow
- evaluation ↔ testing ↔ assessment ↔ quality check（具体语境下不一定完全等价）
- quality ↔ output quality ↔ quality of inference
- safety ↔ output safety ↔ safety check（safety 是属性，safety check 是检查动作）
- uncertainty ↔ lack of confidence ↔ uncertain result（不确定性是程度，uncertain result 是结果状态）
- latency ↔ response time ↔ inference time（inference time 也可能泛指总计算时间）
- throughput ↔ request processing rate ↔ inference capacity
- batch inference ↔ offline inference（不完全同义；批量可在线发生，offline 强调非即时）
- online inference ↔ real-time inference（不完全同义；在线不必然满足严格实时）
- serving ↔ model serving ↔ inference service
- endpoint ↔ model endpoint ↔ inference endpoint
- preprocessing ↔ input preparation ↔ input conversion
- postprocessing ↔ output formatting ↔ result formatting
- hallucination ↔ fabricated output ↔ unsupported generation
- failure handling ↔ error handling ↔ fallback and retry flow

## Do Not Confuse Candidates

- **Inference vs Training**：training 改变或学习模型参数；inference 使用已经学到的参数处理新输入。
- **Inference vs Next-token Prediction**：inference 是完整的模型执行过程；next-token prediction 只是其中可能重复发生的一个预测步骤。
- **Inference vs Reasoning**：inference 是技术上的模型运行；reasoning 描述可能表现为解题或分步骤思考的行为，不是同义词。
- **Inference vs Generation**：inference 可以输出分类标签、预测值或转录；generation 是产生新内容的一类输出方式。
- **Inference vs Prediction**：prediction 是推理可能产生的结果或动作；inference 是产生它的整体过程。
- **Model Parameters vs Input**：parameters 是模型内部保存的数值；input 是这次请求送入模型的数据。
- **Learned Parameters vs Hyperparameters**：learned parameters 通常由训练学出；hyperparameters 通常由人或训练流程在训练前设置。
- **Training Data vs New Input**：training data 用来教模型；new input 是训练后当前请求要处理的案例。
- **Input vs Prompt**：prompt 是生成式场景中的一种输入形式；图片、音频片段和其他数据也可以是 input。
- **Output vs Result**：result 是广义的结果；output 强调该结果从模型或系统中被返回出来。
- **Output vs Response**：response 是面向请求者的一种输出形式；并非所有 output 都是自然语言 response。
- **Output vs Transcription**：transcription 是音频转换得到的文字；普通 response 或 classification label 不一定是 transcription。
- **Label vs Prediction**：label 是类别名称或目标答案；prediction 是模型针对当前输入算出来的结果。
- **Classification vs Generation**：classification 从预设类别中选择标签；generation 构造新的文字、图像、音频或其他内容。
- **Image Classification vs Speech Recognition**：前者把图像映射到类别；后者把语音映射到转写文字。
- **Language Model vs Image Model vs Audio Model**：它们分别主要处理文字、视觉输入和声音输入；具体多模态模型可能跨越这些边界。
- **Model vs Product**：model 是可复用的学习机制；product 还包括界面、数据、规则、工具和运营。
- **Context vs Context Window**：context 是提供给模型的相关信息；context window 是模型一次能够容纳或使用的上下文范围。
- **Token vs Word**：token 是模型处理的小单位，不一定等于一个完整单词，也可能是单词片段、标点或其他片段。
- **Tokenization vs Inference**：tokenization 是把输入拆成词元的准备步骤；inference 是使用模型完成计算的整体过程。
- **KV Cache vs Model Parameters**：KV cache 是某次上下文或生成过程中的临时中间状态；model parameters 是训练后长期保存的模型数值。
- **KV Cache vs Context Window**：context window 是可见信息容量；KV cache 是为了加速已处理信息而保存的计算状态。
- **Model Execution vs Reasoning Trace**：模型执行不等于产生了人类式思维过程；可见的 reasoning trace 也不一定反映真实内部计算。
- **Likely vs Correct**：likely 表示模型估计可能性较高；不保证结果一定正确。
- **Confidence vs Accuracy**：confidence 是模型对单次结果的确信程度；accuracy 是一批结果中实际正确的比例。
- **Uncertain Result vs Incorrect Result**：uncertain 表示暂时不能放心判断；incorrect 表示已经知道或评估为错误。
- **Quality vs Safety**：quality 关心正确、清楚和有用；safety 关心是否造成伤害或违反安全要求。
- **Evaluation vs Inference**：evaluation 是系统地测试和衡量表现；inference 是模型对具体输入实际运行。
- **Review vs Evaluation**：review 常是检查某个输出是否可用；evaluation 更常是对模型或一批结果进行系统测量。
- **Human Review vs Human-in-the-loop**：human review 是一次检查行为；human-in-the-loop 是把人检查或批准纳入工作流程的设计。
- **Online Inference vs Real-time Inference**：online 表示请求到来时处理；real-time 还暗示有严格的低延迟要求。
- **Batch Inference vs Offline Inference**：batch 强调一次处理多条输入；offline 强调不需要在用户请求到来时即时返回。
- **Latency vs Throughput**：latency 是单次请求等待多久；throughput 是一段时间内能处理多少请求。
- **Preprocessing vs Postprocessing**：preprocessing 在模型计算前整理输入；postprocessing 在模型计算后整理输出。
- **Serving vs Inference**：serving 是把模型作为可调用服务提供；inference 是服务内部实际执行模型的计算。
- **Inference Engine vs Model**：inference engine 是执行模型的软件运行环境；model 是被执行的参数和计算结构。
- **Deployment vs Serving**：deployment 是把模型放入目标环境；serving 是部署后持续接收请求并提供模型能力。
- **Hallucination vs Randomness**：随机性可能让输出不同；hallucination 是输出内容缺乏依据或不正确。
- **Safety vs Security**：safety 关注模型输出或行为是否有害；security 关注系统、接口和数据是否受到攻击或滥用。
- **Generalization vs Memorization**：generalization 是在新输入上仍有效；memorization 只记住训练样例，不代表真正泛化。
- **Model Output vs Human Understanding**：模型返回结果不等于模型像人一样理解输入的意义。
- **Generated Content vs Retrieved Content**：生成内容由模型构造；检索内容来自已有资料，二者可以在同一系统中结合。
- **Inference vs Search**：inference 是运行模型；search 是从已有索引或资料中查找内容，搜索结果也可以再作为模型输入。
- **New Input vs New Parameters**：推理通常收到新输入，但不意味着为每个请求学习或改变模型参数。

## Notes

- 页面标题为 **What is Inference? · Tokens, Context & Inference**，页面 eyebrow 标为 **05 · Tokens, Context & Inference · Topic 05**。
- 页面核心定义是：**Inference is the process of running a trained model on an input to produce an output.**
- 页面进一步定义 inference 为：**Inference happens when a trained model is used to make a prediction or generate a result.**
- 页面最重要的边界句是：training changes model parameters，而 inference uses learned parameters on new input。
- 页面用“Training is studying for an exam; inference is using what you learned to answer a new question”作类比；该类比保留了 studying、exam、answer、new question 等上下文候选。
- 页面明确列出的流程节点是五步：1 · Input、2 · Represent、3 · Compute、4 · Predict、5 · Return。
- 流程的直接文案分别是：Receive new data；Convert the input；Run the model；Produce a result；Generate output。
- 流程说明还明确列出：prompt、image、audio clip、other input、make it readable by the model、apply learned parameters、calculate a prediction、likely next token、label、transcription、response。
- 三个真实世界示例是 image classification、language model、speech recognition；对应结果分别是 category such as “dog”、response through repeated next-token predictions、transcription。
- “What it is NOT” 明确列出三个易混淆关系：Inference ≠ Training；Inference ≠ Next-token Prediction；Inference ≠ Reasoning。
- 页面给出的 next-token 边界是：inference is the broader execution process；next-token prediction can repeat within it。
- 页面给出的 reasoning 边界是：inference means model execution；reasoning describes possible problem-solving behavior。
- 相关概念链原文为：Input → Context Window → Inference → Next-token Prediction → Output。
- 相关概念 chips 明确列出 Tokenization、Context Window、Next-token Prediction（Coming soon）、KV Cache；raw 阶段保留其显示状态。
- 页面 takeaway 原文是：**Inference is what happens when a trained model is run on new input.**
- 视频区块标为 Independent explainer / Video，状态为 not yet available；它不是 inference 核心机制，但作为页面正文中的可见词保留。
- 页面没有提供具体数字指标，因此 accuracy、latency、throughput 等指标在本稿中作为 raw 候选或 Potential Missing Concepts 保留，不宣称页面已经解释它们。
- 页面没有展开解码、采样、Softmax、KV cache 内部细节；这些概念仅因 related concept 或 inference 机制邻接关系被保留，并在 Notes 中标明未展开。
- 本文件是 raw glossary 收集稿：不做最终去重、术语合并、优先级删减或同义词裁决；重复或近似条目应留给后续整理阶段处理。
