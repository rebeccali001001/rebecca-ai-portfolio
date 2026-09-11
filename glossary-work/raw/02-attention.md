# Attention

- Module: 02 · Neural Networks & Model Architectures
- Topic: Attention
- Source File: `attention.html`

## Glossary Candidates

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Attention | 注意力机制 | A mechanism that weighs which pieces of information matter to one another | 一种给不同信息关系分配重要程度的机制 |
| attention mechanism | 注意力机制 | A neural-network mechanism for selecting relevant information | 神经网络中挑选相关信息的数学机制 |
| neural network | 神经网络 | A model made of connected computational units | 由许多相连计算单元组成的模型 |
| model | 模型 | A learned system that processes input and produces output | 学会处理数据的系统 |
| mechanism | 机制 | A way a system performs an operation | 系统完成某件事的工作方式 |
| weigh information | 给信息加权 | Assign different importance to information | 给不同信息分配不同重要程度 |
| mathematical weight | 数学权重 | A number representing how strongly information should count | 表示某条信息应该占多大比重的数字 |
| attention weight | 注意力权重 | A weight assigned to a relationship or input part | 表示模型重点参考哪部分信息的数值 |
| relevance | 相关性 | How useful one piece of information is to another | 一条信息对另一条信息有多相关 |
| relevant information | 相关信息 | Information useful for the current interpretation or task | 对当前理解或任务有帮助的信息 |
| piece of information | 信息片段 | One part of the available information | 可用信息中的一小部分 |
| information relationship | 信息关系 | A connection between pieces of information | 不同信息片段之间的联系 |
| input | 输入 | Information given to a model | 交给模型处理的信息 |
| input tokens | 输入 token | Tokens supplied as the model input | 作为模型输入的一串 token |
| token | token / 词元 | A piece of text or data processed by a model | 模型可以处理的一小段文字或数据 |
| tokenization | 分词 / token 化 | Breaking input into processable pieces | 把输入切成模型能处理的小片段 |
| input piece | 输入片段 | A portion of input that can be processed | 输入中可以单独处理的一部分 |
| representation | 表示 / 表征 | A numerical or structured form of information | 用数字或结构表达信息的形式 |
| token representation | token 表示 | The representation assigned to a token | 一个 token 对应的数字表达 |
| create representations | 创建表示 | Turn tokens into numerical representations | 把 token 转成数字形式 |
| numerical representation | 数字表示 | A representation expressed with numbers | 用数字表达数据或 token |
| vector representation | 向量表示 | A representation as an ordered list of numbers | 用一串有顺序的数字表示信息 |
| contextual representation | 上下文表示 / 上下文表征 | A representation that includes relevant surrounding context | 融合了相关上下文的信息表示 |
| context-aware representation | 上下文感知表示 | A representation that reflects relationships in context | 能体现上下文关系的表示 |
| contextualized token representation | 上下文化 token 表示 | A token representation updated using context | 根据上下文更新过的 token 表示 |
| context | 上下文 | Surrounding information that helps interpretation | 帮助理解当前信息的周围内容 |
| context processing | 上下文处理 | Using available context to interpret or generate output | 利用已有上下文理解或生成结果 |
| context-aware | 上下文感知的 | Able to use surrounding information | 能结合周围信息进行处理 |
| relationship | 关系 | A connection between two or more pieces of information | 两个或多个信息片段之间的联系 |
| token relationship | token 关系 | A relationship between tokens | token 之间的联系 |
| compare relationships | 比较关系 | Measure how relevant items are to one another | 衡量不同项目彼此有多相关 |
| relationship relevance | 关系相关性 | The degree to which one item matters to another | 一个项目对另一个项目的重要程度 |
| dependency | 依赖关系 | A relationship in which one element uses another | 一个元素依赖另一个元素的信息 |
| long-range dependency | 长距离依赖 | A relationship between far-apart sequence elements | 序列中相距很远的元素之间的关系 |
| local relationship | 局部关系 | A relationship among nearby elements | 相邻或附近元素之间的关系 |
| current task | 当前任务 | The task for which the model is processing information | 模型此时要完成的任务 |
| task | 任务 | A goal the model is asked to perform | 要求模型完成的目标 |
| mathematical operation | 数学运算 | A calculation applied to representations | 对表示进行的计算 |
| operation over representations | 对表示的运算 | A mathematical operation applied to representations | 在数字表示上执行的数学计算 |
| human attention | 人类注意力 | Human awareness or focus | 人类主动关注某件事的能力 |
| awareness | 意识 / 察觉 | Human awareness of something | 人对某事的意识或察觉 |
| human focus | 人类关注 | Human concentration on selected information | 人类把注意力放在某些信息上 |
| mathematical focus | 数学上的重点分配 | Numerical weighting that resembles focus | 用数字模拟“重点关注” |
| attention score | 注意力分数 | A score measuring relevance between representations | 衡量两个表示相关程度的分数 |
| attention scores | 注意力分数（复数） | Relevance scores computed among input elements | 输入元素之间算出的相关性分数 |
| attention matrix | 注意力矩阵 | A matrix of relationships or attention scores | 记录各 token 彼此关注程度的矩阵 |
| attention map | 注意力图 | A visual or structured map of attention weights | 展示关注权重分布的图或结构 |
| attention distribution | 注意力分布 | The distribution of weights across available information | 权重在各信息片段上的分布 |
| weight distribution | 权重分布 | How numerical importance is spread across items | 重要程度在各项目之间如何分配 |
| weighted combination | 加权组合 | A combination in which items contribute by weight | 按不同权重把信息混合起来 |
| weighted sum | 加权和 | A sum in which each value has a multiplier | 每个值先乘权重再相加 |
| combine information | 组合信息 | Mix information from multiple sources or tokens | 把多个来源或 token 的信息混合起来 |
| relevant information mixing | 相关信息混合 | Combine information judged relevant | 把模型认为相关的信息融合起来 |
| information aggregation | 信息聚合 | Gather information from multiple elements | 从多个元素汇总信息 |
| feature aggregation | 特征聚合 | Combine features from related elements | 融合相关元素的特征 |
| query | 查询向量 | The representation asking what information is useful | 用来询问“需要什么信息”的向量 |
| key | 键向量 | The representation used to match a query | 用来和 query 匹配的向量 |
| value | 值向量 | The information retrieved after matching | 匹配后真正被取用的信息向量 |
| query-key compatibility | query-key 兼容度 | A measure of how well a query matches a key | query 与 key 有多匹配 |
| query-key-value | 查询-键-值结构 | The three representations used by attention | 注意力计算中的查询、键和值三种表示 |
| scaled dot-product attention | 缩放点积注意力 | Attention based on scaled query-key dot products | 先缩放 query-key 点积再计算注意力 |
| dot product | 点积 | A multiplication-and-sum operation between vectors | 两个向量对应相乘后相加 |
| scaling factor | 缩放因子 | A factor used to keep scores numerically stable | 防止分数过大、让计算更稳定的因子 |
| softmax | softmax 函数 | A function that turns scores into normalized weights | 把分数转成总和通常为 1 的权重 |
| normalized weights | 归一化权重 | Weights put onto a comparable scale | 调整到可比较范围的权重 |
| self-attention | 自注意力 | Attention among elements within the same input | 输入内部各 token 互相计算关系 |
| cross-attention | 交叉注意力 | Attention from one sequence to another sequence | 一个序列关注另一个序列的信息 |
| multi-head attention | 多头注意力 | Several attention calculations performed in parallel | 同时从多个关系角度计算注意力 |
| attention head | 注意力头 | One parallel attention subspace or computation | 多头注意力中的一个关系视角 |
| causal attention | 因果注意力 | Attention restricted to information allowed by generation order | 生成时只能看允许看到的前文信息 |
| masked attention | 掩码注意力 | Attention with selected positions blocked | 用掩码禁止关注某些位置 |
| attention mask | 注意力掩码 | A mask controlling which positions can interact | 控制哪些位置可以互相关注的标记 |
| bidirectional attention | 双向注意力 | Attention that can use information from both directions | 可以同时利用前后方向信息的注意力 |
| encoder attention | 编码器注意力 | Attention used while encoding an input | 编码输入时使用的注意力 |
| decoder attention | 解码器注意力 | Attention used while generating or decoding output | 生成或解码输出时使用的注意力 |
| encoder-decoder attention | 编码器-解码器注意力 | Attention connecting encoded input with generated output | 把输入编码结果和输出生成过程连接起来 |
| Transformer | Transformer 架构 | An architecture that uses attention and other components | 使用注意力及其他组件的模型架构 |
| Transformer architecture | Transformer 架构 | A neural-network architecture built around attention layers | 以注意力层为核心的神经网络架构 |
| Transformer layer | Transformer 层 | One repeated processing block in a Transformer | Transformer 中重复堆叠的一个处理模块 |
| Transformer layers | Transformer 层（复数） | Multiple Transformer processing blocks | 多个 Transformer 处理模块 |
| attention layer | 注意力层 | A layer that computes relationships and mixes information | 计算关系并融合信息的网络层 |
| neural-network layer | 神经网络层 | A stage of computation in a neural network | 神经网络中的一个计算阶段 |
| feed-forward network | 前馈网络 | A network that further transforms each representation | 进一步变换每个表示的网络模块 |
| residual connection | 残差连接 | A shortcut that adds an earlier representation to a later one | 把早期表示直接加回后续层的捷径 |
| layer normalization | 层归一化 | Normalize activations within a layer | 对一层中的激活值进行归一化 |
| positional encoding | 位置编码 | Information indicating where a token occurs | 告诉模型 token 在序列中位置的信息 |
| positional information | 位置信息 | Information about sequence order or location | 表示顺序和位置的信息 |
| sequence | 序列 | An ordered set of tokens or elements | 按顺序排列的 token 或元素集合 |
| sequence position | 序列位置 | A token's location in an ordered sequence | token 在序列中的位置 |
| token order | token 顺序 | The order in which tokens appear | token 出现的先后顺序 |
| autoregressive generation | 自回归生成 | Generate one next token at a time from prior tokens | 根据前面 token 逐个生成下一个 token |
| next-token generation | 下一个 token 生成 | Predict and produce the next token | 预测并生成后续的一个 token |
| next token | 下一个 token | The token generated after the current context | 根据当前上下文生成的下一个 token |
| earlier tokens | 更早的 token | Tokens that appear earlier in the input or context | 输入或上下文中更早出现的 token |
| language model | 语言模型 | A model that processes or generates language | 处理或生成语言的模型 |
| large language model | 大语言模型 | A large model trained to process and generate language | 规模较大的语言处理与生成模型 |
| LLM | 大语言模型缩写 | Abbreviation for large language model | Large Language Model 的缩写 |
| LLM context processing | LLM 上下文处理 | Using relevant earlier tokens in language generation | 生成语言时利用前面相关 token |
| translation | 翻译 | Convert content from one language to another | 把一种语言转换成另一种语言 |
| machine translation | 机器翻译 | Automated translation by a model | 模型自动完成的翻译 |
| source sentence | 源句子 | The sentence being translated from | 被翻译的原始句子 |
| target sentence | 目标句子 | The translated sentence being produced | 模型生成的译文句子 |
| cross-lingual relationship | 跨语言关系 | A relationship between words in different languages | 不同语言词语之间的对应关系 |
| pronoun relationship | 代词关系 | A relationship connecting a pronoun to what it refers to | 把代词和它所指对象联系起来 |
| pronoun resolution | 代词消解 | Determine what a pronoun refers to | 判断代词具体指什么 |
| antecedent | 先行词 | The earlier expression referred to by a pronoun | 代词前面所指的对象 |
| “it” | “it” 代词 | A pronoun whose meaning depends on context | 需要结合上下文才能确定含义的代词 |
| “the trader” | “the trader” | The person or entity in the example sentence | 示例句中的交易者 |
| trader | 交易者 | A person or entity that trades | 进行交易的人或机构 |
| position | 头寸 / 持仓 | An investment held in a market | 市场中持有的一项投资 |
| risky position | 有风险的头寸 | A position described as risky | 被认为有风险的持仓 |
| vision transformer | 视觉 Transformer | A Transformer that processes image patches | 用 Transformer 处理图像块的架构 |
| Vision Transformer | Vision Transformer / 视觉 Transformer | A model that relates image patches to understand an image | 通过关联图像块来理解整幅图像的模型 |
| ViT | ViT / 视觉 Transformer 缩写 | Abbreviation for Vision Transformer | Vision Transformer 的常用缩写 |
| computer vision | 计算机视觉 | Machine processing and understanding of images | 让机器处理和理解图像的领域 |
| image | 图像 | A visual input made of pixels or patches | 由像素或图像块组成的视觉输入 |
| image patch | 图像块 | A small region of an image treated as an input unit | 把图像切成的小块 |
| image patch relationship | 图像块关系 | A relationship between regions of an image | 图像不同区域之间的联系 |
| whole image | 整幅图像 | The complete visual input | 完整的一张图像 |
| visual representation | 视觉表示 | A numerical representation of visual content | 图像内容的数字表示 |
| image understanding | 图像理解 | Extract meaning or structure from an image | 理解图像中的内容和关系 |
| context window | 上下文窗口 | The amount of input a model can process | 模型一次能处理的输入总量 |
| available tokens | 可用 token | Tokens present and available to attention | 当前可被注意力使用的 token |
| input length | 输入长度 | The amount of input measured in tokens or elements | 输入包含多少 token 或元素 |
| context-window size | 上下文窗口大小 | The maximum amount of context available | 模型最多能看到的上下文规模 |
| attention scope | 注意力范围 | The set of positions an attention operation can access | 一次注意力计算可以访问的范围 |
| token budget | token 预算 | A limit on the number of processed tokens | 可处理 token 数量的限制 |
| process input | 处理输入 | Use a model to compute over supplied information | 用模型计算输入信息 |
| generate output | 生成输出 | Produce a result from processed information | 根据处理结果产出内容 |
| inference | 推理 / 推断 | Applying a trained model to new input | 用训练好的模型处理新输入 |
| training | 训练 | Learning parameters from examples | 从数据中学习模型参数 |
| training data | 训练数据 | Data used to learn model behavior | 用来训练模型的数据 |
| model parameters | 模型参数 | Learned numerical values inside a model | 模型内部通过训练学到的数值 |
| learned representation | 学习到的表示 | A representation acquired through training | 模型训练过程中学到的表示 |
| attention computation | 注意力计算 | The calculations that produce attention weights and outputs | 计算注意力权重和结果的过程 |
| attention output | 注意力输出 | The context-aware representation produced by attention | 注意力计算后得到的上下文表示 |
| attention pattern | 注意力模式 | A pattern showing which elements interact | 展示哪些元素互相联系的模式 |
| attention flow | 注意力流 | The movement or combination of information through attention | 信息通过注意力传播和融合的过程 |
| compute relevance | 计算相关性 | Calculate how relevant one item is to another | 计算一个信息对另一个信息有多重要 |
| assign weights | 分配权重 | Give numerical importance to relationships | 给关系分配数字重要程度 |
| mix information | 混合信息 | Combine information from selected inputs | 把选中的输入信息融合起来 |
| preserve relevant context | 保留相关上下文 | Keep the context useful for the task | 保留对任务有帮助的上下文 |
| dependency modeling | 依赖关系建模 | Represent relationships among elements | 对元素之间的依赖进行建模 |
| representation update | 表示更新 | Modify a representation using related information | 用相关信息更新原有表示 |
| attention complexity | 注意力复杂度 | The computational cost of attention | 注意力计算需要多少计算资源 |
| quadratic attention | 二次复杂度注意力 | Attention whose pairwise cost grows quadratically with sequence length | token 两两比较导致成本按长度平方增长 |
| efficient attention | 高效注意力 | Attention designed to reduce time or memory cost | 设法减少时间或内存成本的注意力 |
| memory cost | 内存成本 | Memory required to run a computation | 执行计算所需的内存量 |
| computational cost | 计算成本 | Time or resources required for computation | 计算所需的时间和资源 |
| inference latency | 推理延迟 | Time needed to produce an output | 模型生成结果所需的时间 |
| attention visualization | 注意力可视化 | Display attention weights or patterns | 把注意力权重或模式画出来 |
| interpretability | 可解释性 | How understandable a model's behavior is | 人能否理解模型为何关注某些信息 |
| attention explanation | 注意力解释 | An explanation based on attention behavior | 根据注意力行为给出的解释 |
| attribution | 归因 | Assign output influence to input elements | 判断哪些输入对输出有贡献 |
| faithfulness | 忠实性 | Whether an explanation reflects the actual computation | 解释是否真实反映模型计算过程 |
| attention sink | 注意力汇 | A position that attracts disproportionate attention | 吸收大量注意力的特殊位置 |
| sparse attention | 稀疏注意力 | Attention that connects only selected positions | 只连接部分位置的注意力 |
| global attention | 全局注意力 | Attention that can connect across the whole input | 能在整个输入范围建立联系的注意力 |
| local attention | 局部注意力 | Attention limited to a nearby region | 只关注附近信息的注意力 |
| sliding-window attention | 滑动窗口注意力 | Local attention over a moving range of tokens | 在移动的小窗口内计算注意力 |
| retrieval-augmented generation | 检索增强生成 | Generate using retrieved external information | 先检索资料再结合资料生成内容 |
| retrieval | 检索 | Find relevant information from a collection | 从资料库找出相关信息 |
| retrieved context | 检索上下文 | Context supplied from retrieved information | 从检索结果中提供给模型的上下文 |
| external information | 外部信息 | Information outside the original input | 原始输入之外的补充信息 |
| key-value cache | 键值缓存 | Cached keys and values reused during generation | 生成时重复利用的 key 和 value 缓存 |
| KV cache | KV 缓存缩写 | Short name for key-value cache | Key-Value Cache 的缩写 |
| serving | 模型服务 | Running a model to answer requests | 让模型在线处理请求 |
| deployment | 部署 | Put a model into a real system | 把模型放进真实系统运行 |
| production inference | 生产推理 | Inference performed in a live product or service | 在线上产品中执行模型推理 |
| throughput | 吞吐量 | Amount of input or output processed per unit time | 单位时间处理的数据量 |
| scalability | 可扩展性 | Ability to handle increasing workload | 负载增加时仍能运行的能力 |
| privacy | 隐私 | Protection of information about people or organizations | 防止信息被不当暴露 |
| sensitive context | 敏感上下文 | Context containing information requiring protection | 含有需要保护内容的上下文 |
| data leakage | 数据泄露 | Unintended exposure of information | 信息意外暴露给不该看到的人或系统 |
| prompt injection | 提示注入 | Input that tries to manipulate model instructions | 通过输入内容干扰模型指令的攻击 |
| adversarial input | 对抗性输入 | Input crafted to cause an unwanted model behavior | 专门设计来误导模型的输入 |
| attention head redundancy | 注意力头冗余 | Multiple heads learning overlapping patterns | 多个注意力头学到相似关系 |
| gradient | 梯度 | A signal used to update model parameters | 用来调整模型参数的方向和大小信息 |
| backpropagation | 反向传播 | Compute gradients through the model during training | 训练时把误差信号反向传回模型 |
| attention parameter | 注意力参数 | Learned parameters used in attention projections | 注意力投影中通过训练学到的参数 |
| projection matrix | 投影矩阵 | A matrix that transforms representations | 把一种向量表示变成另一种表示的矩阵 |
| query projection | 查询投影 | Transform an input representation into a query | 把输入表示转换成 query 的过程 |
| key projection | 键投影 | Transform an input representation into a key | 把输入表示转换成 key 的过程 |
| value projection | 值投影 | Transform an input representation into a value | 把输入表示转换成 value 的过程 |
| output projection | 输出投影 | Transform combined attention output into the next representation | 把注意力结果变换成下一层表示 |
| attention dropout | 注意力 dropout | Randomly drop some attention connections during training | 训练时随机关闭部分注意力连接 |
| temperature | 温度参数 | A factor controlling how concentrated a distribution is | 控制权重分布尖锐或平滑程度的参数 |
| calibration | 校准 | Make scores or probabilities better reflect confidence | 让分数或概率更符合真实可信度 |
| attention failure | 注意力失效 | A case where attention uses unhelpful relationships | 注意力关注了不该关注的信息 |
| distraction | 注意力分散 | Attention assigned to irrelevant information | 模型把权重分给无关信息 |
| over-attention | 过度注意 | Excessive weight placed on one position or pattern | 对某个位置或模式分配过多权重 |

## Potential Missing Concepts

- Query, key, and value (Q/K/V): the standard representations used to compute relevance and retrieve information.
- Scaled dot-product attention, dot product, scaling factor, and softmax: the canonical mathematical recipe behind attention weights.
- Self-attention, cross-attention, encoder attention, decoder attention, and encoder-decoder attention: major attention patterns not explicitly named in the source page.
- Multi-head attention and attention heads: parallel relationship views used in Transformer layers.
- Causal attention, masked attention, bidirectional attention, and attention masks: ways to control which tokens may interact during training or generation.
- Positional encoding, positional embeddings, sequence order, and position information: attention needs an explicit way to represent order because it compares token representations.
- Attention scores, attention matrix, attention map, attention distribution, weighted sum, and weighted combination: intermediate and output structures that make the five-step process concrete.
- Feed-forward networks, residual connections, and layer normalization: common non-attention components inside a Transformer layer.
- Encoder, decoder, autoregressive generation, next-token prediction, and language-model head: surrounding architecture and inference concepts for translation and LLM examples.
- Cross-lingual alignment, source tokens, target tokens, and alignment matrix: translation-specific attention concepts.
- Pronoun resolution, coreference resolution, antecedent, and anaphora: linguistic concepts behind the “it” example.
- Vision Transformer (ViT), patch embedding, image patches, class token, and positional embeddings for images: common details behind relating image patches.
- Attention complexity, quadratic complexity, memory cost, inference latency, efficient attention, sparse attention, local attention, and sliding-window attention.
- FlashAttention, block-sparse attention, linear attention, kernelized attention, and recurrent or state-space alternatives: approaches for reducing attention cost.
- Long-context attention, context extension, token budget, truncation, and lost-in-the-middle effect: practical context-window limitations.
- Key-value cache (KV cache), prefill, decode, batching, throughput, and serving: production inference concepts for LLM attention.
- Attention visualization, attribution, faithfulness, saliency, and explanation: concepts needed to interpret attention without assuming that attention automatically explains a decision.
- Attention head specialization, head pruning, head redundancy, and layer-wise attention patterns: analysis and optimization concepts.
- Attention dropout, temperature, normalization, gradient, backpropagation, projection matrices, and learned attention parameters: training and implementation concepts.
- Attention sink, BOS token, padding token, special token, padding mask, and causal mask: token-level edge cases in real implementations.
- Privacy, sensitive context, data leakage, prompt injection, adversarial input, and access control: security concepts for attention over user-provided context.

## Aliases / Synonyms

- Attention / attention mechanism / neural attention / attention operation
- Attention weight / attention score weight / relevance weight / learned focus weight
- Attention score / compatibility score / relevance score / query-key score
- Attention matrix / attention map / attention pattern matrix / weight matrix
- Context-aware representation / contextual representation / contextualized representation / context-sensitive representation
- Token / input token / subword token / sequence element
- Representation / vector representation / numerical representation / embedding
- Context / surrounding context / available context / input context
- Self-attention / intra-sequence attention / self-attention mechanism
- Cross-attention / encoder-decoder attention / inter-sequence attention
- Multi-head attention / multiheaded attention / parallel attention heads
- Attention head / head / attention subspace
- Causal attention / autoregressive attention / left-to-right attention
- Masked attention / attention with a mask / restricted attention
- Attention mask / causal mask / padding mask / visibility mask
- Query / query vector / Q
- Key / key vector / K
- Value / value vector / V
- Query-key-value / QKV / Q-K-V
- Transformer / Transformer architecture / attention-based architecture
- Transformer layer / Transformer block / attention block
- Vision Transformer / ViT / image Transformer
- Large language model / LLM / language model at scale
- Context window / context length / maximum context / token context limit
- Image patch / visual patch / patch token
- Weighted sum / weighted combination / attention aggregation
- Attention complexity / computational complexity of attention / attention cost
- Key-value cache / KV cache / key-value memory
- Attention visualization / attention map visualization / attention inspection

## Do Not Confuse Candidates

- Attention vs human attention: model attention is a mathematical operation over representations, not awareness, consciousness, or human focus.
- Attention vs Transformer: attention is a mechanism; a Transformer is an architecture that uses attention together with other components.
- Attention vs context window: attention weighs relationships among available tokens; a context window is the amount of input a model can process.
- Attention vs context: attention is the computation that uses relationships; context is the surrounding information available to that computation.
- Attention weight vs attention score: a score is often an unnormalized relevance value, while a weight is the normalized or applied contribution after further processing.
- Attention score vs probability: an attention score need not be a probability; softmax may convert scores into normalized weights.
- Attention weight vs model parameter: attention weights are usually input-dependent values, while parameters are learned and stored in the model.
- Attention map vs geographic map: an attention map records model interaction strengths; it is not a physical map.
- Attention vs embedding: attention computes relationships and combines information; an embedding is a numerical representation.
- Attention vs tokenization: tokenization breaks input into units; attention relates and combines the resulting units.
- Attention vs positional encoding: attention compares content representations; positional encoding supplies information about order or location.
- Self-attention vs cross-attention: self-attention relates elements within one sequence; cross-attention connects one sequence or representation source to another.
- Causal attention vs bidirectional attention: causal attention blocks unavailable future positions; bidirectional attention can use information from both directions when allowed.
- Masked attention vs attention mask: masked attention is the operation with restrictions; the mask is the control structure that imposes them.
- Multi-head attention vs multiple models: heads are parallel projections within one attention module, not necessarily separate complete models.
- Attention head vs Transformer layer: a head is one sub-computation; a layer is a larger block that may contain many heads and other components.
- Transformer layer vs neural-network layer: a Transformer layer is a specific architecture block, while neural-network layer is the broader category.
- Query vs search query: an attention query is a learned vector, not necessarily a text search string typed by a user.
- Key vs database key: an attention key is a vector for matching; a database key identifies a stored record.
- Value vs scalar value: an attention value is a representation retrieved and combined, not merely one numeric scalar.
- Attention output vs model output: attention output is an intermediate representation; the model output may be a translation, token, class, or other final result.
- Relevant token vs important token in general: relevance is relative to the current query or task, not an absolute property of a token.
- Context window vs attention scope: a context window limits available input, while an attention mask or architecture may restrict which available positions interact.
- Context length vs model quality: a larger context window does not guarantee that every token will be used correctly or equally.
- LLM context processing vs human reading: an LLM uses numerical operations over token representations, not human comprehension or awareness.
- Translation vs attention: translation is a task; attention is one mechanism that can help a model perform it.
- Pronoun resolution vs attention: pronoun resolution is a linguistic task; attention may provide relationship information but does not by itself guarantee correct resolution.
- Vision Transformer vs computer vision: Vision Transformer is one model architecture; computer vision is the broader field.
- Image patch vs pixel: an image patch is a group or region of pixels treated as a unit, not necessarily one pixel.
- Attention mechanism vs memory: attention retrieves and combines information from representations for a computation; it is not automatically a persistent database or long-term memory.
- Attention visualization vs explanation: a visualization shows attention values, but those values are not automatically a faithful causal explanation of the model decision.
- Attention vs attribution: attention describes one internal weighting operation; attribution asks how inputs contributed to an output and may use other methods.
- Attention weight vs causal influence: a high attention weight does not by itself prove that the token caused the output.
- Softmax vs attention: softmax is a normalization function often used inside attention; it is not the entire attention mechanism.
- Query-key matching vs semantic understanding: numerical compatibility can help retrieve relevant representations, but it is not human-like understanding.
- Attention complexity vs context-window size: computational cost describes resource growth, while context-window size describes the allowed input amount.
- Training vs inference: training learns parameters; inference applies learned parameters to new input.
- Inference latency vs throughput: latency is time for a result; throughput is amount processed per unit time.
- Key-value cache vs context window: KV cache stores reusable intermediate states; the context window defines available input capacity.
- Sparse attention vs missing data: sparse attention intentionally limits connections; missing data means information is absent or unavailable.
- Privacy vs attention mask: privacy protects information; an attention mask controls computational visibility and is not a complete privacy control.
- Prompt injection vs ordinary context: prompt injection is adversarial or instruction-manipulating input; ordinary context is input used for the task.

## Notes

- The source page defines Attention as a mechanism that lets a neural network weigh which pieces of information are most relevant to one another.
- The source explicitly says that, for each part of the input, attention calculates how strongly it should use information from other parts.
- The source describes the result as a context-aware representation in which each token carries information about relationships that matter for the current task.
- The source’s analogy uses “The trader closed the position because it was risky,” where the model relates “it” to the risky position; it explicitly states that this is mathematical weighting, not human awareness.
- The source’s five-step process is: Input Tokens → Create Representations → Compare Relationships → Assign Attention Weights → Combine Relevant Information.
- The source’s real-world examples are pronoun relationships, translation, LLM context processing, and Vision Transformers relating image patches.
- The source explicitly distinguishes Attention from Human Attention, Transformer, and Context Window.
- The source related-concepts chain is Tokens → Attention → Transformer Layers → Contextual Representations, with links to Tokens, Transformer, and Context Window.
- The page’s takeaway is that Attention mathematically weighs relationships between pieces of information.
- The page contains a “Video coming soon” placeholder and states that no verified video asset is available; this is page metadata rather than a glossary concept.
- Raw collection intentionally preserves broad candidate coverage, repeated wording, aliases, and concepts that are strongly implied by the topic. No deduplication or pruning was performed.
