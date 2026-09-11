# Topic

Transformer

## Module/Topic/Source File

- Module: 02 · Neural Networks & Model Architectures
- Topic: Transformer
- Source File: `transformer.html`

## Glossary Candidates

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Transformer | Transformer；变换器架构 | A neural-network architecture that processes relationships between tokens | 一种通过处理词或 token 之间关系来工作的神经网络架构 |
| transformer | Transformer；变换器架构 | The same architecture name written in lowercase | Transformer 这个架构名称的小写写法 |
| neural-network architecture | 神经网络架构 | A design for how a neural network is organized | 神经网络各部分如何组成和连接的设计 |
| neural network architecture | 神经网络架构 | A structure that specifies the components and flow of a neural network | 规定神经网络组件和数据流向的结构 |
| architecture | 架构 | The overall design of a system or model | 一个系统或模型的整体设计 |
| processes relationships | 处理关系 | Uses computation to model connections between items | 用计算方式处理不同项目之间的联系 |
| relationship | 关系 | A connection between two or more items | 两个或多个对象之间的联系 |
| relationships between tokens | token 之间的关系 | Connections modeled between tokens in a sequence | 模型要理解的词或 token 之间的联系 |
| token | token；词元 | A unit of text processed by a model | 模型处理的一小段文字单位，可能是词、词的一部分或符号 |
| tokens | token；词元 | Multiple text units processed as a sequence | 模型一次处理的一串文字单位 |
| Token | token；词元 | A capitalized form of the text unit term | token 这个术语的首字母大写写法 |
| token representations | token 表征 | Numeric representations of tokens used by the model | 把 token 变成模型能计算的数字表示 |
| token representation | token 表征 | A representation for one token | 一个 token 对应的数字化表示 |
| representations | 表示；表征 | Encoded forms used for computation | 为了让模型计算而编码出来的形式 |
| representation | 表示；表征 | A form that carries information about an item | 能携带对象信息的一种表达形式 |
| prediction | 预测 | An output produced by estimating a likely result | 模型估计并输出的可能结果 |
| output | 输出 | The result produced by a model | 模型处理后给出的结果 |
| output representation | 输出表征 | A representation produced at the end of processing | 模型处理结束后得到的表示 |
| output representations | 输出表征 | Representations produced as model outputs | 模型输出的一组表示 |
| scores | 分数；得分 | Numeric values supporting a prediction or task | 帮助模型作出预测或任务判断的数值 |
| score | 分数；得分 | A numeric value associated with an output or prediction | 与输出或预测相关的一个数值 |
| key idea | 核心思想 | The central concept needed to understand a topic | 理解这个主题最重要的要点 |
| attention | 注意力机制 | A mechanism that lets each token use information from relevant tokens | 让每个 token 参考其他相关 token 信息的机制 |
| Attention | 注意力机制 | The capitalized name of the attention mechanism | Attention 这个机制名称的首字母大写写法 |
| attention mechanism | 注意力机制 | A computation in which tokens weigh information from other tokens | token 给其他 token 的信息分配不同重要程度的计算 |
| attention mechanisms | 注意力机制 | Mechanisms that compare and weight token relationships | 比较 token 关系并分配权重的一类机制 |
| token weigh information | token 对信息加权 | A token assigns different importance to information | 一个 token 判断其他信息对自己有多重要 |
| weigh information | 对信息加权 | Assign different importance to pieces of information | 给不同信息分配不同的重要程度 |
| relevant tokens | 相关 token | Tokens whose information is useful for the current token | 对当前 token 的理解有帮助的其他 token |
| other relevant tokens | 其他相关 token | Other tokens selected as useful context | 被认为与当前内容相关、值得参考的 token |
| relevant positions | 相关位置 | Positions whose information may matter to a position being processed | 序列中可能对当前位置有帮助的位置 |
| attention result | 注意力结果 | The result of combining information according to attention weights | 按注意力权重汇总信息后的结果 |
| attention weights | 注意力权重 | Values that indicate how much each relationship matters | 表示每个关系有多重要的数值 |
| attention weight | 注意力权重 | One value expressing the importance of a relationship | 表示某一个关系重要程度的数值 |
| real attention weights | 真实注意力权重 | Attention weights from an actual model computation | 真实模型计算出来的注意力权重 |
| simplified illustration | 简化示意 | An intentionally simplified example for explanation | 为了讲清楚概念而简化过的例子 |
| visualization | 可视化 | A visual display of data or model behavior | 把数据或模型行为画出来帮助理解 |
| specific model | 特定模型 | One particular model implementation | 某一个具体实现的模型 |
| stacked neural network layers | 堆叠的神经网络层 | Neural-network layers placed one after another | 一层层叠起来、连续处理信息的神经网络层 |
| stacked neural-network layers | 堆叠的神经网络层 | A hyphenated form describing repeated neural-network layers | “堆叠神经网络层”的连字符写法 |
| neural-network layer | 神经网络层 | One processing block in a neural network | 神经网络中负责一部分计算的处理单元 |
| neural network layer | 神经网络层 | A layer that transforms a neural representation | 对神经网络表征进行转换的一层 |
| layer | 层 | One stage of computation in a model | 模型进行一次处理的阶段 |
| layers | 层 | Multiple stages of model computation | 模型中重复进行处理的多个阶段 |
| layer stack | 层堆栈；层叠 | A sequence of layers that repeatedly transforms representations | 按顺序反复改变表征的一串层 |
| Layer stack | 层堆栈；层叠 | The capitalized form used in the architecture map | 架构图中 Layer stack 的写法 |
| stacked layers | 堆叠层 | Layers arranged in a repeated sequence | 按顺序叠放、重复工作的多层结构 |
| repeated building blocks | 重复的构建模块 | Similar processing units used repeatedly | 反复使用的相似模型组件 |
| refine representations | 细化表征 | Improve or transform a representation through more processing | 通过继续计算让表示更精细、更有用 |
| progressively transform | 逐步转换 | Change a representation little by little through stages | 经过多层处理逐步改变表示 |
| final representation | 最终表征 | The representation after all model layers finish | 所有层处理完后得到的表示 |
| additional neural-network processing | 额外神经网络处理 | Neural-network computation performed beyond attention | 除了注意力之外继续进行的神经网络计算 |
| feed-forward processing | 前馈处理 | A forward computation that further transforms representations | 把信息向前传递并进一步转换表征的计算 |
| feed-forward | 前馈 | Computation that moves information through a network without feedback loops | 信息沿网络向前计算、不回头循环的处理方式 |
| model task | 模型任务 | A task performed using a model's representation or output | 利用模型表征或输出完成的任务 |
| attention + stacked neural network layers | 注意力 + 堆叠神经网络层 | The page's compact formula for a Transformer | 页面用来概括 Transformer 的“注意力加多层网络”公式 |
| architecture map | 架构图 | A visual map of model components and their order | 展示模型组件和先后顺序的图 |
| architecture first | 先理解架构 | A framing that explains the overall design before the mechanism | 先看整体结构，再看里面的具体机制 |
| mechanism | 机制 | The way a component produces its effect | 某个组件发挥作用的方式 |
| mechanism inside | 内部机制 | A mechanism contained within a larger architecture | 大架构里面包含的具体工作方式 |
| core idea | 核心思想 | The main idea of a concept | 一个概念最主要的意思 |
| input tokens | 输入 token | Tokens entering a model as input | 送进模型的一串 token |
| input token | 输入 token | One token supplied to a model | 送进模型的一个 token |
| input | 输入 | Information supplied to a model | 交给模型处理的信息 |
| tokens enter the model | token 进入模型 | The first processing step in the page's story | 处理流程中 token 被送入模型的步骤 |
| text | 文本 | Written language supplied to or processed by a model | 模型要处理的文字内容 |
| words | 单词；词语 | Word-level units used in the reading-group analogy | 页面类比中把文本看成的词语单位 |
| word | 单词；词语 | One word in the analogy or example sentence | 类比或例句中的一个词 |
| context | 上下文 | Surrounding information that helps interpret a token | 帮助理解当前词或内容的周围信息 |
| current context | 当前上下文 | Context available for understanding the current token | 解释当前 token 时能参考的背景内容 |
| context from | 来自上下文的信息 | Information drawn from surrounding tokens | 从附近 token 中获取的相关信息 |
| sequence | 序列 | An ordered collection of tokens | 按顺序排列的一串 token |
| position | 位置 | A location of a token in a sequence | token 在序列中的位置 |
| each position | 每个位置 | Every location in the processed sequence | 序列中的每一个位置 |
| current position | 当前位置 | The position currently being interpreted | 模型当前正在处理的那个位置 |
| other positions | 其他位置 | Positions besides the current one | 除当前位置外的序列位置 |
| compare relationships | 比较关系 | Examine how tokens relate to one another | 比较不同 token 之间的联系 |
| comparison | 比较 | Examining items against one another | 把不同对象放在一起看它们的差别和联系 |
| reading group | 阅读小组 | The human analogy used to explain token interaction | 页面用来类比 token 互相参考的阅读小组 |
| reading-group analogy | 阅读小组类比 | An analogy for how tokens can use one another's information | 用阅读小组帮助理解 token 互相参考的比喻 |
| understanding the current context | 理解当前上下文 | Interpreting a token using surrounding information | 结合周围内容理解当前文字 |
| useful information | 有用信息 | Information that helps the current interpretation or task | 对当前理解或任务有帮助的信息 |
| repeated discussion | 重复讨论 | The analogy for repeated layer processing | 用来类比多层重复处理的“反复讨论” |
| mathematical operations | 数学运算 | Formal computations used by the model | 模型真正执行的公式和数字计算 |
| human discussion | 人类讨论 | Human conversation in the explanatory analogy | 页面明确说 Transformer 不是进行真实人类讨论 |
| processing story | 处理流程 | A step-by-step account of how a model processes input | 按步骤讲解模型如何处理输入的过程 |
| processing | 处理 | Computing over input information | 对输入信息进行计算 |
| processing step | 处理步骤 | One stage in a processing sequence | 整个处理流程中的一个阶段 |
| step | 步骤 | A named stage in a process | 流程中先后排列的一个动作或阶段 |
| token representations are updated | token 表征被更新 | Token representations change after computation | 经过计算后 token 的表示被改写 |
| update representations | 更新表征 | Change representations using new computed information | 用新计算出的信息改变原有表示 |
| combined information | 合并信息 | Information brought together into one result | 把多个来源的信息组合起来 |
| transform the representation | 转换表征 | Change the encoded representation through a layer | 经过一层计算改变编码后的表示 |
| output scores are produced | 产生输出分数 | The model generates numeric scores at the end | 模型最后计算出用于判断的数字分数 |
| output score | 输出分数 | A score returned by a model | 模型返回的一个分数 |
| final output | 最终输出 | The result after the complete processing pipeline | 整个处理流程结束后得到的结果 |
| prediction task | 预测任务 | A task in which the model estimates an answer | 让模型估计答案或结果的任务 |
| representation task | 表征任务 | A task that uses or produces a useful representation | 使用或生成有用数据表示的任务 |
| Transformer at a Glance | Transformer 概览 | A compact summary of the architecture pipeline | 对 Transformer 架构流程的快速概览 |
| pipeline | 流水线；处理管线 | An ordered series of processing stages | 按固定顺序连接起来的一系列处理步骤 |
| token representations | token 表征 | The model's encoded form of input tokens | 输入 token 在模型中的编码表示 |
| repeat through layers | 经过多层重复 | Run the processing again across successive layers | 在后续层中反复执行类似处理 |
| output representation / scores | 输出表征 / 分数 | The final representation or numeric scores | 流程最后得到的表示或数字分数 |
| attention asks | 注意力所回答的问题 | The question of which tokens matter for a token | 注意力要判断“哪些其他 token 对这里重要” |
| layer stack asks | 层堆栈所回答的问题 | The question of how to refine a representation | 多层结构要继续判断“如何改进当前表示” |
| information flow | 信息流 | The movement of information through model stages | 信息在模型各处理阶段之间流动的过程 |
| Why attention matters | 注意力为何重要 | An explanation of the role of attention | 说明注意力机制为什么能帮助理解上下文 |
| focus token | 关注 token | The token currently used as the example of interpretation | 示例中当前重点分析的 token |
| pronoun | 代词 | A word that refers to another person, thing, or concept | 用来指代其他人、事物或概念的词 |
| pronouns and context | 代词与上下文 | Understanding pronouns using surrounding language | 结合前后文字判断代词指什么 |
| loan | 贷款 | The object referred to in the attention example | 注意力例句中与 bank 和 it 相关的贷款 |
| bank | 银行；河岸 | A word whose meaning can be clarified by context | 需要结合上下文理解含义的例句词语 |
| information | 信息 | Data or knowledge used to interpret or decide | 用来理解内容或作决定的资料 |
| English | 英语 | The source language in the translation example | 翻译示例中的输入语言 |
| another language | 另一种语言 | A target language different from the input language | 翻译后输出的不同语言 |
| language understanding | 语言理解 | Interpreting meaning and relationships in language | 理解文字含义及词语之间关系的能力 |
| translation | 翻译 | Converting content from one language to another | 把一种语言的内容转换成另一种语言 |
| classification | 分类 | Assigning an input to a category | 判断输入属于哪个类别 |
| category | 类别 | A label or group assigned to an input | 给输入归属的一个类别 |
| support ticket | 支持工单 | A customer-support request used as an example input | 示例中的客户支持请求 |
| input category | 输入类别 | The category predicted for an input | 模型为输入判断出的类别 |
| language model | 语言模型 | A model that processes or predicts language | 处理或预测语言的模型 |
| large language model | 大型语言模型 | A large model for language tasks | 用于语言任务、规模较大的模型 |
| LLM | 大型语言模型缩写 | Short for Large Language Model | Large Language Model 的缩写 |
| LLMs | 大型语言模型 | Plural form of LLM | 多个大型语言模型 |
| architecture versus language model | 架构与语言模型的区别 | The distinction between a design and a model using that design | 架构是设计，语言模型是利用架构完成语言任务的模型 |
| Transformer architecture | Transformer 架构 | The Transformer design used to build models | 用来构建模型的 Transformer 设计 |
| model built with Transformer architecture | 基于 Transformer 架构构建的模型 | A model whose design uses Transformer components | 使用 Transformer 结构搭建出来的模型 |
| product | 产品 | A user-facing system built from models and other systems | 面向用户的完整产品，不只是一个模型架构 |
| ChatGPT | ChatGPT | A product that uses models plus other systems | 一个结合模型和其他系统的产品 |
| architecture versus product | 架构与产品的区别 | The distinction between a technical design and a complete product | 架构不是完整产品，产品还包含模型之外的系统 |
| full architecture | 完整架构 | The whole model design, including its mechanisms | 包含多个机制的完整模型结构 |
| one mechanism | 单个机制 | One component or method inside a larger architecture | 大架构里面的一个工作机制 |
| full architecture versus one mechanism | 完整架构与单个机制的区别 | The distinction between the whole design and attention alone | Transformer 是完整架构，attention 只是其中一个机制 |
| broader family | 更广泛的类别 | A larger category that contains a concept | 包含当前概念的更大类别 |
| key mechanism | 关键机制 | An important mechanism inside a system | 系统中非常重要的工作机制 |
| common sequence units | 常见序列单位 | Units commonly used to form an ordered sequence | 组成文字序列的常见基本单位 |
| available context amount | 可用上下文量 | The amount of context available to a model | 模型一次能参考多少上下文信息 |
| context window | 上下文窗口 | The amount of input context a model can use at once | 模型一次能看到和参考的上下文范围 |
| inference optimization | 推理优化 | A technique that makes model inference more efficient | 让模型生成结果时更快或更省资源的技术 |
| inference | 推理 | Running a trained model to produce an output | 用训练好的模型实际计算结果 |
| KV Cache | KV 缓存 | A cache used to speed up Transformer inference | 推理时缓存已算过的信息以减少重复计算 |
| key-value cache | 键值缓存 | The expanded concept behind KV Cache | KV Cache 的完整概念名称 |
| key-value (KV) cache | 键值（KV）缓存 | Cached key and value representations for inference | 推理时保存 key 和 value 表示的缓存 |
| attention optimization | 注意力优化 | Improving the efficiency of attention computation | 让注意力计算更高效的优化 |
| model inference | 模型推理 | The process of using a model to generate or score output | 让模型运行并生成或评估输出的过程 |
| neural networks | 神经网络 | A broad family of layered computational models | 由多层计算单元组成的一大类模型 |
| Neural Networks | 神经网络 | The capitalized broader concept in the related-concepts map | 相关概念图中的 Neural Networks 写法 |
| related concept | 相关概念 | A connected idea that helps explain a topic | 与当前主题有联系、能帮助理解的概念 |
| connections | 连接关系 | Links between related concepts | 不同概念之间的联系 |
| architecture map | 架构图 | A map showing the Transformer components and flow | 展示 Transformer 组件和流程的图 |
| model architecture | 模型架构 | The organized design of a model | 模型各组件如何组织的设计 |
| model component | 模型组件 | A part of a model that performs a role | 模型中负责某项工作的部分 |
| building block | 构建模块 | A reusable unit used to build a larger model | 用来搭建更大模型的可复用单元 |
| stacked architecture | 堆叠式架构 | An architecture made of repeated layers or blocks | 由多层或多个模块重复堆叠而成的架构 |
| sequence processing | 序列处理 | Processing ordered tokens while considering their relationships | 按顺序处理 token 并考虑它们之间的关系 |
| token-level processing | token 级处理 | Processing information for individual tokens | 以单个 token 为单位进行处理 |
| contextual representation | 上下文表征 | A representation shaped by surrounding tokens | 融合周围 token 信息后的表示 |
| contextual information | 上下文信息 | Information from surrounding tokens or text | 来自前后文、帮助理解当前内容的信息 |
| semantic relationship | 语义关系 | A meaning-based relationship between tokens or words | 词语或 token 之间基于含义的联系 |
| dependency | 依赖关系 | A relationship in which one token's interpretation uses another | 一个词的理解需要参考另一个词的关系 |
| sequence unit | 序列单位 | One item in an ordered sequence | 有顺序排列的一串数据中的一个单位 |
| model representation | 模型表征 | The encoded information held inside a model | 模型内部保存的信息表示 |
| learned representation | 学到的表征 | A representation shaped by model learning | 模型学习过程中形成的表示 |
| transformation | 转换 | A change from one representation to another | 把一种表示变成另一种表示的过程 |
| neural computation | 神经网络计算 | Computation carried out by neural-network layers | 神经网络层执行的数字计算 |
| model output | 模型输出 | What the model returns after processing | 模型处理输入后返回的结果 |
| task output | 任务输出 | The result used to complete a specific task | 为完成某项任务而输出的结果 |
| output representation / scores | 输出表征 / 分数 | Two possible final products of the pipeline | 处理管线最后可能给出表示或分数 |
| independent explainer | 独立讲解视频 | A separate explanatory media resource | 独立制作、用于讲解概念的视频资料 |
| Azure Neural voice | Azure Neural voice；Azure 神经语音 | The voice style noted for the explainer | 页面视频说明中标注的 Azure 神经语音 |
| visual explanation | 可视化解释 | An explanation using visual structure or motion | 用图形或动画帮助说明概念 |
| video | 视频 | Moving media explaining the Transformer | 页面提供的 Transformer 讲解视频 |
| captions | 字幕 | Text synchronized with spoken video content | 与视频语音同步显示的文字 |
| English captions | 英文字幕 | Captions written in English | 用英语写的视频字幕 |
| video playback | 视频播放 | Playing the video resource in a browser | 在浏览器中播放视频资源 |
| browser | 浏览器 | Software that can display and play web content | 用来打开网页和播放视频的软件 |

## Potential Missing Concepts

- The page uses the high-level word `attention` but does not name the standard subcomponents Query, Key, and Value (Q, K, V).
- It does not explicitly name self-attention, multi-head attention, scaled dot-product attention, or causal/masked attention.
- It does not explicitly name positional encoding, positional embeddings, or how order is represented in a token sequence.
- It does not explicitly name encoder, decoder, encoder-only, decoder-only, or encoder-decoder Transformer variants.
- It does not explicitly name residual connection, skip connection, layer normalization, activation function, or the standard Transformer block.
- It does not explicitly name logits, softmax, probability distribution, next-token prediction, autoregressive generation, or loss function.
- It does not explicitly name training, pre-training, fine-tuning, parameters, weights, gradients, backpropagation, or optimization.
- It does not explicitly name sequence length, computational complexity, quadratic attention complexity, memory use, latency, throughput, or batching.
- It does not explicitly name bidirectional attention, unidirectional attention, cross-attention, or attention masking.
- It does not explicitly name BERT, GPT, T5, Vision Transformer (ViT), or other concrete Transformer model families.
- It does not explicitly name embeddings, input embeddings, output embeddings, or embedding dimension.
- It does not explicitly name tokenization, vocabulary, special tokens, padding, or unknown tokens.
- It does not explicitly name decoding, sampling, temperature, beam search, top-k, or top-p.

## Aliases / Synonyms

| Candidate | Alias / Synonym | Note |
|---|---|---|
| Transformer | transformer architecture | Same architecture name with an explicit architecture qualifier |
| Transformer | Transformer model architecture | Common expanded wording for the design |
| neural-network architecture | neural network architecture | Spelling variant without the hyphen |
| token | word-piece; text unit; sequence unit | Related ways to describe a unit of model input; not always exact synonyms |
| token representation | token representation(s) | Singular/plural grammatical variants |
| representation | representation(s); encoded representation | Related forms used for an internal encoded form |
| attention | attention mechanism | The page uses the short term and the expanded mechanism name |
| attention weights | attention weight | Plural and singular forms |
| layer stack | stacked layers | Closely related descriptions of repeated layers |
| layer stack | stacked neural-network layers | More explicit description of the same architecture idea |
| feed-forward processing | feed-forward | Short form of the forward-processing component |
| output representation | final representation | Both describe a representation at the end of processing, depending on context |
| scores | output scores | Expanded form for model-produced numeric scores |
| context window | available context amount | The page's plain-language explanation of a context window |
| KV Cache | key-value cache | Expanded name of the inference cache |
| KV Cache | key-value (KV) cache | Expanded name retaining the abbreviation |
| LLM | large language model | Abbreviation and full form |
| LLM | language model | Related but broader/less specific wording |
| neural networks | Neural Networks | Capitalization variant in the related-concepts map |
| words | word | Plural and singular forms in the analogy |
| translation | language translation | Common expanded phrase |
| classification | text classification | More specific form for a text input and category output |

## Do Not Confuse Candidates

| Candidate A | Candidate B | Distinction |
|---|---|---|
| Transformer | LLM | Transformer is an architecture; an LLM is a language model often built with that architecture |
| Transformer | language model | Transformer describes design; language model describes a model's language-processing or prediction role |
| Transformer | attention | A Transformer is a full architecture; attention is one important mechanism inside it |
| Transformer | attention mechanism | The architecture contains the mechanism but is not identical to it |
| Transformer | ChatGPT | Transformer is a technical architecture; ChatGPT is a product using models plus other systems |
| Transformer | product | An architecture is not a complete user-facing product |
| architecture | mechanism | Architecture is the overall design; mechanism is one way a component works |
| neural network | Transformer | A neural network is the broader model family; Transformer is one architecture in that family |
| token | word | A token is a model-processing unit and may be smaller or different from a human word |
| token | token representation | A token is the input unit; its representation is the encoded form used in computation |
| representation | output | A representation is an encoded information form; output is whatever the model returns |
| attention | attention weights | Attention is the mechanism; attention weights are numeric importance values produced or used by it |
| attention weights | model output scores | Attention weights describe internal token relationships; output scores support the final task result |
| context | context window | Context is surrounding information; context window is the amount the model can access |
| layer | layer stack | A layer is one processing stage; a layer stack is multiple layers arranged together |
| feed-forward processing | attention | Feed-forward processing is additional neural computation; attention compares and weights relationships |
| prediction | representation | A prediction is an estimated task result; a representation is an encoded intermediate or final form |
| score | probability | A score is a general numeric value and need not be a normalized probability |
| inference | training | Inference uses a trained model to produce outputs; training adjusts the model from data |
| KV Cache | context window | KV Cache is an inference optimization; context window is the available input context amount |
| translation | classification | Translation outputs another language; classification outputs a category |
| language understanding | translation | Understanding language is a capability/task area; translation converts between languages |
| reading group | Transformer layer | Reading group is an explanatory analogy; Transformer layer performs mathematical operations |
| human discussion | mathematical operations | The page explicitly distinguishes the analogy from the actual computation |
| simplified illustration | real attention weights | The illustration explains an idea and is not a display of a specific model's actual weights |
| output representation | output scores | A representation carries encoded information; scores are numeric values for prediction or another task |

## Notes

- Collection scope is the complete visible textual content of `transformer.html`, including headings, labels, explanatory paragraphs, examples, concept boundaries, related-concept map, and video accessibility/source text.
- Candidates intentionally retain capitalization, singular/plural forms, hyphenation variants, repeated appearances, page wording, aliases, and plain-language phrases; this is a raw candidate collection, not a normalized glossary.
- `bank`, `loan`, `it`, `information`, `English`, and `another language` are retained because they are part of the page's concrete examples of context, attention, and translation.
- `ChatGPT` is retained as a boundary example even though the page states that it is a product rather than a Transformer architecture.
- The attention example is explicitly simplified; its token relationships should not be read as actual attention weights from a particular model.
- The page describes a Transformer at a conceptual level and does not provide equations, implementation details, named sublayers, or model-specific benchmarks.
- The video source is referenced in the HTML as `vedio/transformer.mp4`, with `vedio/transformer.vtt` for English captions and `vedio/transformer.png` as the poster image.
