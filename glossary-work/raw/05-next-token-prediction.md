# Topic

Next-token Prediction

- Module: 05 · Tokens, Context & Inference
- Topic: Next-token Prediction
- Source File: `next-token-prediction.html`
- Module/Topic/Source File: `05 · Tokens, Context & Inference / Next-token Prediction / next-token-prediction.html`
- Page title: `What Is Next-token Prediction? · Tokens, Context & Inference`
- Source description: `Next-token prediction is the repeated process a language model uses to generate text one token at a time.`

## Glossary Candidates

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Next-token Prediction | 下一个词元预测 | Repeatedly estimating what token could come next | 模型一次次猜接下来最可能出现的词元 |
| next token prediction | 下一个词元预测 | Predicting the next token in a sequence | 预测序列中的下一个词元 |
| next-token prediction | 下一个词元预测 | The model’s repeated estimate of a possible next token | 模型反复估计下一个可能词元的过程 |
| next token | 下一个词元 | The token that may be added next | 下一步可能被加进去的词元 |
| token | 词元 | A unit of text processed by a language model | 模型处理的一小段文字单位 |
| tokens | 词元 | Text units available to or produced by the model | 模型读到或生成的文字单位 |
| generated token | 生成的词元 | A token selected and added during generation | 生成过程中被选中并加入文本的词元 |
| selected token | 被选中的词元 | The one token chosen from possible options | 从多个可能选项里选出的一个词元 |
| language model | 语言模型 | A model that works with language and text patterns | 学习文字规律并处理语言的模型 |
| model | 模型 | A learned system that estimates and selects tokens | 能估计并选择词元的学习系统 |
| text | 文本 | Written content generated or read by a model | 模型读取或生成的文字内容 |
| generate | 生成 | To produce text by selecting tokens | 通过选择词元产生文字 |
| generation | 生成 | The process of producing a sequence of tokens | 逐步产生一串词元的过程 |
| text generation | 文本生成 | Producing text from repeated token choices | 通过反复选择词元来生成文本 |
| repeated generation | 重复生成 | Generation that runs the prediction loop again and again | 不断重复预测循环来生成内容 |
| generate text one token at a time | 一次一个词元生成文本 | Build text by adding one token in each step | 每一步只加一个词元，慢慢形成文本 |
| repeated estimate | 反复估计 | An estimate made again after each new token | 每加入一个新词元后重新做一次估计 |
| estimate | 估计 | A model’s calculated belief about a possible continuation | 模型对可能后续内容的计算判断 |
| repeated prediction | 反复预测 | Predicting a next token at every generation step | 每个生成步骤都再预测一次 |
| prediction | 预测 | Estimating which tokens are plausible next | 估计哪些词元可能出现在下一步 |
| prediction step | 预测步骤 | One round of estimating possible next tokens | 进行一次下一个词元估计的步骤 |
| prediction-and-selection step | 预测与选择步骤 | A round that scores possibilities and selects one | 先评估可能性再选一个的步骤 |
| small prediction-and-selection steps | 小型预测与选择步骤 | Many small rounds that together make a response | 许多小步骤合起来形成最终回答 |
| final response | 最终回答 | The complete response that emerges from generation | 多次生成后形成的完整回答 |
| full answer | 完整答案 | A whole answer rather than one generated step | 整个回答，不只是一个生成步骤 |
| response | 响应 / 回答 | Text returned after generation | 模型生成并返回的内容 |
| available context | 可用上下文 | Information currently visible to the model | 模型此刻能看到的信息 |
| context | 上下文 | Tokens and information available for the next prediction | 用来做下一次预测的已有信息 |
| full available context | 完整可用上下文 | All context currently available to the model | 模型当前能参考的全部上下文 |
| new context | 新上下文 | Context after the selected token is added | 加入新词元后的上下文 |
| current context | 当前上下文 | The context at the present generation step | 当前这一步模型正在看的上下文 |
| context for the next step | 下一步上下文 | The sequence used for the following prediction | 下一次预测要读取的序列 |
| context window | 上下文窗口 | The amount of context a model can use | 模型一次能参考的上下文范围 |
| available tokens | 可用词元 | Tokens currently supplied to the model | 当前提供给模型的词元 |
| current tokens | 当前词元 | Tokens already present in the sequence | 已经在当前序列里的词元 |
| sequence | 序列 | An ordered collection of tokens | 按顺序排列的一串词元 |
| new sequence | 新序列 | The sequence after a new token is added | 加入新词元后更新的一串文本 |
| sequence grows | 序列增长 | The sequence becomes longer after each selection | 每次选词后序列都会变长 |
| continuation | 延续内容 | Text that could follow the existing context | 接在已有文字后面的内容 |
| possible continuation | 可能的延续 | One candidate for what may come next | 可能接在后面的一个候选内容 |
| possible continuations | 可能的后续内容 | Multiple candidate continuations | 多种可能接续下去的内容 |
| plausible next token | 合理的下一个词元 | A token that could sensibly follow the context | 在当前上下文后看起来合理的词元 |
| possible next token | 可能的下一个词元 | A candidate token considered for the next position | 模型考虑放在下一位置的候选词元 |
| possible next tokens | 可能的下一个词元集合 | Candidate tokens considered together | 一起被考虑的多个候选词元 |
| next-token distribution | 下一个词元分布 | Probabilities assigned across candidate next tokens | 给不同候选下一个词元分配可能性的整体结果 |
| token distribution | 词元分布 | A distribution over possible token choices | 各个可能词元的概率分配 |
| probability distribution | 概率分布 | A set of possible outcomes and their probabilities | 把可能结果和各自可能性放在一起 |
| token-selection distribution | 词元选择分布 | The distribution used when choosing a token | 用来选择下一个词元的概率分布 |
| distribution | 分布 | How probability is spread across options | 可能性在各个选项之间怎样分配 |
| probability | 概率 | A numerical estimate of how likely an option is | 某个选项出现可能性的数字 |
| probabilities | 概率 | Numerical likelihoods for several options | 多个选项各自的可能性数字 |
| score | 分数 | A value expressing how strongly a token is favored | 表示模型多偏向某个词元的数值 |
| scores | 分数 | Values assigned to possible continuations | 给不同后续选项打出的数值 |
| score possibilities | 为可能性打分 | Evaluate candidate tokens with scores | 给候选词元评估和打分 |
| calculate scores | 计算分数 | Evaluate possible next tokens numerically | 用数值评估可能的下一个词元 |
| output scores | 输出分数 | Return scores for many possible tokens | 输出多个候选词元的分数 |
| scores or probabilities | 分数或概率 | Two forms of information about candidate tokens | 表达候选可能性的两种结果形式 |
| score a continuation | 为延续内容打分 | Give a candidate continuation a numerical value | 给可能的后续内容一个数值评价 |
| probability list | 概率列表 | A displayed list of options and probabilities | 列出选项及其可能性的清单 |
| percentage | 百分比 | A percentage used to illustrate probability | 用百分数表示示例概率 |
| illustrative probability | 示意性概率 | A probability shown only for explanation | 为了说明而展示的概率，不是真实输出 |
| illustrative probabilities only | 仅为示意的概率 | Probabilities included as an illustration | 页面示例中的说明性概率 |
| model output | 模型输出 | The result produced by the model | 模型产生的结果 |
| real model output | 真实模型输出 | Output actually produced by a model run | 模型实际运行得到的结果 |
| model outputs | 模型输出结果 | Results returned by model computation | 模型计算后返回的结果 |
| selected output | 选定输出 | The single token selected from candidates | 从候选项中选出的单个词元 |
| output: scores or probabilities for many possible tokens | 输出：多个可能词元的分数或概率 | Prediction can expose many candidate values | 预测阶段可能给出很多候选的数值 |
| output: one chosen token | 输出：一个选中的词元 | Sampling produces one selected token | 采样阶段产出一个被选词元 |
| input | 输入 | Tokens supplied to the model before prediction | 预测前交给模型的词元或文字 |
| read context | 读取上下文 | Inspect the tokens currently available | 读取当前可用的词元信息 |
| the model reads the available context | 模型读取可用上下文 | The model uses current context as prediction input | 模型把当前上下文作为预测依据 |
| tokens currently available | 当前可用词元 | Tokens present at the current step | 这一步已经能提供给模型的词元 |
| model reads the tokens currently available | 模型读取当前可用词元 | Read the sequence before calculating candidates | 在计算候选前读取当前序列 |
| evaluate possible next tokens | 评估可能的下一个词元 | Assess candidate tokens for the next position | 判断哪些词元适合放在下一位置 |
| form probabilities | 形成概率 | Turn evaluations into a distribution | 把评估结果形成概率分布 |
| form a next-token distribution | 形成下一个词元分布 | Create a distribution over next-token choices | 建立下一个词元的整体可能性分配 |
| select one token | 选择一个词元 | Pick one token from the candidates | 从候选词元中选出一个 |
| select one | 选出一个 | Choose a single option for this step | 这一步只选一个结果 |
| add and repeat | 加入并重复 | Add the token and run the process again | 把词元加进去，再次运行流程 |
| add the selected token | 加入选中的词元 | Put the selected token into the sequence | 把选中的词元放进序列 |
| token becomes part of the context | 词元成为上下文的一部分 | A new token is available for the next step | 新词元会成为下一步可参考的信息 |
| new token becomes part of the context | 新词元加入上下文 | The selected token changes the next input | 选中的词元会改变下一次输入 |
| predict again | 再次预测 | Run another next-token prediction | 再做一次下一个词元预测 |
| repeat the loop | 重复循环 | Continue the generation cycle | 继续重复生成循环 |
| generation loop | 生成循环 | The repeated cycle from context to selection | 从读取上下文到选词、再回到上下文的循环 |
| loop | 循环 | A process that repeats after each token | 每个词元后再次开始的流程 |
| generation process | 生成过程 | The ordered process that builds a response | 逐步构建回答的有序过程 |
| generation step | 生成步骤 | One iteration of producing a token | 产生一个词元的一轮操作 |
| one token at a time | 一次一个词元 | Produce only one token in each step | 每一步只产生一个词元 |
| five steps | 五个步骤 | The page’s five-part summary of generation | 页面总结的五步生成流程 |
| one step | 一步 | A single next-token operation | 一次下一个词元操作 |
| read context | 读取上下文 | Step 01: read the tokens currently available | 第一步读取当前已有的词元 |
| calculate scores | 计算分数 | Step 02: evaluate possible next tokens | 第二步给可能词元计算数值 |
| form probabilities | 形成概率 | Step 03: turn scores into a distribution | 第三步把分数变成分布 |
| select one token | 选择一个词元 | Step 04: use a rule to choose one token | 第四步用规则选出一个词元 |
| add and repeat | 加入并重复 | Step 05: grow the sequence and restart | 第五步扩展序列并重新开始 |
| decoding rule | 解码规则 | A rule that chooses one token from model scores | 根据模型分数选择一个词元的规则 |
| decoding | 解码 | The process of turning token scores into a chosen token | 把词元分数转成具体选择的过程 |
| sampling | 采样 | Selecting one token from a probability distribution | 从概率分布中抽取一个词元 |
| sampling / decoding | 采样 / 解码 | The selection stage after prediction | 预测之后进行选择的阶段 |
| prediction vs sampling | 预测与采样的区别 | Prediction scores possibilities; sampling chooses one | 预测负责评估可能性，采样负责选一个 |
| Prediction | 预测 | Ask which tokens are plausible next | 问哪些词元可能是下一个 |
| Sampling | 采样 | Ask which token is selected this time | 问这一次具体选哪一个 |
| which tokens are plausible next? | 哪些词元可能是下一个？ | The question answered by prediction | 预测阶段要回答的问题 |
| which token is selected this time? | 这次选择哪个词元？ | The question answered by sampling | 采样阶段要回答的问题 |
| core difference | 核心区别 | Prediction scores; sampling selects | 预测打分，采样选择 |
| prediction scores possibilities | 预测给可能性打分 | Prediction evaluates many candidate tokens | 预测会评估多个候选词元 |
| sampling chooses one | 采样选择一个 | Sampling returns one chosen token | 采样只返回一个被选词元 |
| possible choice | 可能选项 | A token that could be selected | 可能被选中的词元 |
| chosen token | 被选词元 | The candidate selected for the sequence | 最后加入序列的候选词元 |
| one chosen token | 一个选中的词元 | The single result of a selection step | 一次选择产生的唯一结果 |
| temperature | 温度 | A setting that changes the token-selection distribution | 改变词元选择分布的设置 |
| token-selection temperature | 词元选择温度 | Temperature applied to token selection | 用于选择词元的温度参数 |
| temperature changes the token-selection distribution | 温度改变词元选择分布 | Temperature changes how choices are distributed | 温度会改变各候选词元的可能性分配 |
| lower temperature | 较低温度 | A setting that makes choices more conservative | 让选择更保守的温度设置 |
| higher temperature | 较高温度 | A setting that allows more variation | 让选择更有变化的温度设置 |
| lower-temperature distribution | 低温分布 | A more concentrated, conservative distribution | 更集中、更保守的概率分布 |
| higher-temperature distribution | 高温分布 | A distribution where less-likely options compete more | 低概率选项更有竞争力的分布 |
| more conservative distribution | 更保守的分布 | A distribution favoring predictable choices | 更偏向可预测选择的分布 |
| predictable token choices | 可预测的词元选择 | Choices that are more expected and stable | 更容易预料、较稳定的选词 |
| lower-probability choices | 较低概率的选择 | Options with smaller initial probability | 原本可能性较小的选项 |
| become more competitive | 变得更有竞争力 | Less-likely options gain a greater chance of selection | 低概率选项获得更大的竞争机会 |
| more variation in selection | 选择上的更多变化 | A wider variety of selected tokens | 选出的词元更加多样 |
| variation | 变化性 | Difference across choices or generations | 不同生成结果之间的差异 |
| conservative token selection | 保守的词元选择 | Prefer high-probability, predictable tokens | 更偏向高概率、可预期的词元 |
| token choice | 词元选择 | The decision of which token to add | 决定要加入哪个词元 |
| selection | 选择 | Choosing one candidate from a distribution | 从分布中挑出一个候选项 |
| selection rule | 选择规则 | The method used to choose a token | 决定如何选词元的方法 |
| decoding setting | 解码设置 | A control that affects token selection | 会影响选词的配置 |
| autocomplete | 自动补全 | A system that suggests what may come next | 会建议接下来文字的系统 |
| autocomplete repeated many times | 反复进行的自动补全 | Autocomplete used once per generation step | 每一步都运行一次的自动补全 |
| autocomplete analogy | 自动补全类比 | A simplified analogy for next-token generation | 用自动补全帮助理解逐词元生成 |
| analogy | 类比 | A simpler comparison used to explain a process | 用熟悉的事物解释复杂流程的方法 |
| simplified analogy | 简化类比 | An intentionally simplified explanation | 为了易懂而简化的解释 |
| learned probability patterns | 学到的概率模式 | Probability relationships learned from data | 模型从数据中学到的可能性规律 |
| probability pattern | 概率模式 | A learned relationship among possible continuations | 不同后续内容之间的可能性规律 |
| full available context | 完整可用上下文 | Context across which learned patterns are considered | 模型综合参考的全部当前信息 |
| coffee | 咖啡 | An example continuation after “a cup of” | “一杯……”后的示例接续词 |
| tea | 茶 | An example continuation after “a cup of” | “一杯……”后的另一个示例接续词 |
| water | 水 | An example continuation after “a cup of” | “一杯……”后的另一个示例接续词 |
| “I would like a cup of ...” | “我想要一杯……” | The autocomplete analogy prompt | 页面用于说明自动补全的例句 |
| “The sky is” | “天空是” | The input in the generation-loop illustration | 生成循环示意图中的输入 |
| blue | 蓝色 / 蓝 | The selected token in the sky example | 天空示例中被选中的词元 |
| clear | 晴朗 / 清澈 | A possible next token in the sky example | 天空示例中的候选词元 |
| dark | 黑暗 / 暗 | A possible next token in the sky example | 天空示例中的候选词元 |
| sky example | 天空示例 | The illustrative “The sky is blue” sequence | “The sky is blue”这个说明例子 |
| 52% | 52% | The illustrative probability assigned to “blue” | 示例中分配给 blue 的概率数字 |
| 18% | 18% | The illustrative probability assigned to “clear” | 示例中分配给 clear 的概率数字 |
| 11% | 11% | The illustrative probability assigned to “dark” | 示例中分配给 dark 的概率数字 |
| “Paris is the capital of” | “巴黎是……的首都” | The mini-example prompt | 页面小示例中的提示句 |
| Paris | 巴黎 | The subject in the mini-example prompt | 小示例中的城市名称 |
| capital | 首都 | The relation being completed in the mini-example | 小示例要补全的概念 |
| France | 法国 | The selected continuation in the mini-example | 小示例中被选出的正确接续 |
| Europe | 欧洲 | A lower-probability candidate in the mini-example | 小示例中的较低概率候选 |
| Italy | 意大利 | A lower-probability candidate in the mini-example | 小示例中的较低概率候选 |
| 87% | 87% | The illustrative probability for “France” | 示例中 France 的说明性概率 |
| 4% | 4% | The illustrative probability for “Europe” | 示例中 Europe 的说明性概率 |
| 2% | 2% | The illustrative probability for “Italy” | 示例中 Italy 的说明性概率 |
| mini example | 小示例 | A compact demonstration of selecting a next token | 用很短例子展示如何选下一个词元 |
| prompt | 提示 / 提示词 | Text supplied before a generation step | 生成前交给模型的文字输入 |
| prompt example | 提示示例 | An example input used to demonstrate generation | 用来展示生成过程的输入例子 |
| new sequence: Paris is the capital of France | 新序列：Paris is the capital of France | The sequence after the selected token is added | 加入 France 后形成的新序列 |
| training | 训练 | Updating a model’s parameters using data | 用数据更新模型内部参数的过程 |
| inference | 推理 | Using a trained model to produce output | 用训练好的模型处理输入并产生输出 |
| prediction during inference | 推理期间的预测 | Next-token prediction used while answering | 模型回答时进行的下一个词元预测 |
| model parameters | 模型参数 | Internal values updated during training | 训练时会更新的模型内部数值 |
| parameter update | 参数更新 | A change made to model parameters during training | 训练中改变模型内部参数的一次操作 |
| update model parameters | 更新模型参数 | Adjust the model’s learned internal values | 调整模型学到的内部数值 |
| prediction used during inference | 推理时使用的预测 | Prediction used to generate a response | 生成回答时使用的预测过程 |
| training updates parameters | 训练更新参数 | Training changes the internal model values | 训练会改变模型内部的参数 |
| prediction vs training | 预测与训练的区别 | Prediction generates with a model; training updates it | 预测使用模型，训练改变模型 |
| prediction is not training | 预测不是训练 | Generating a token does not itself update parameters | 生成词元本身不会自动训练模型 |
| one step is not a full answer | 一步不等于完整答案 | One token step is only part of a response | 一个词元步骤只是回答的一小部分 |
| final response emerges from repeated generation | 最终回答由反复生成形成 | The complete answer comes from many generation rounds | 完整回答由许多轮生成逐渐形成 |
| tokenization | 词元化 / 分词 | Turning text into model-readable tokens | 把文字切成模型能处理的词元 |
| tokens and context | 词元与上下文 | Tokens form the context used for prediction | 词元组成预测时使用的上下文 |
| Tokens, Context & Inference | 词元、上下文与推理 | The module topic grouping this page | 这个页面所属的模块主题 |
| inference context | 推理上下文 | Context supplied while the model is answering | 模型推理时提供给它的信息 |
| sampling / temperature | 采样 / 温度 | Selection and its variability control | 选择词元以及控制变化程度的设置 |
| KV Cache | KV 缓存 | Efficiency support for repeated generation | 让反复生成时计算更高效的缓存机制 |
| key-value cache | 键值缓存 | Cached attention information reused across steps | 在连续步骤中重复利用的注意力信息缓存 |
| side efficiency support | 辅助效率支持 | A supporting optimization rather than the prediction rule | 帮助提高效率但不是预测规则本身的机制 |
| repeated generation efficiency | 重复生成效率 | How efficiently the loop can run across many steps | 生成很多词元时循环运行的效率 |
| related concepts | 相关概念 | Concepts connected in the page’s concept tree | 页面认为与主题相连的概念 |
| concept tree | 概念链 / 概念树 | An ordered map of related concepts | 把相关概念按顺序连起来的图示 |
| generated text | 生成文本 | Text built from selected tokens | 由选中词元组成的文字 |
| visual explainer | 视觉解释器 | A visual explanation of a topic | 用图像或视频帮助解释主题的内容 |
| video | 视频 | A possible visual explanation format | 页面预留的视觉解释形式 |
| video unavailable | 视频不可用 | The page states that no video is available yet | 页面说明目前还没有视频 |
| illustrative example | 说明性示例 | An example intended to explain rather than report real output | 为解释概念而设的示例 |
| not real model outputs | 非真实模型输出 | The displayed values are not from a real run | 页面数字不是模型真实运行结果 |
| model probability | 模型概率 | The probability estimated by a model | 模型计算出的可能性 |
| candidate token | 候选词元 | A token considered before selection | 在最终选择前被考虑的词元 |
| candidate continuation | 候选后续 | A possible text continuation under consideration | 正在考虑的可能后续文本 |
| token candidate | 词元候选项 | A possible token in the candidate set | 候选集合中的一个词元 |
| candidate set | 候选集合 | The set of possible next tokens | 所有可能下一个词元组成的集合 |
| token sequence | 词元序列 | An ordered sequence made of tokens | 由词元按顺序组成的序列 |
| context update | 上下文更新 | Adding the selected token to current context | 把选中的词元加入当前上下文 |
| iterative generation | 迭代生成 | Generation that repeats the same loop step by step | 一步步重复同一循环来生成 |
| autoregressive generation | 自回归生成 | Generate the next token using previous tokens | 根据前面已有词元生成下一个词元 |
| causal generation | 因果生成 | Generation constrained to prior context | 只能依据前文生成后续内容 |
| language generation loop | 语言生成循环 | The recurring model-selection-context cycle | 模型、选择、更新上下文的重复循环 |
| next-token generation | 下一个词元生成 | Producing text through next-token choices | 通过逐个选择下一个词元生成文本 |
| token-level generation | 词元级生成 | Generation performed at token granularity | 以词元为最小步骤的生成 |
| token-level decision | 词元级决策 | One decision about the next token | 关于下一个词元的一次决定 |
| probability-based selection | 基于概率的选择 | Choosing with reference to token probabilities | 根据词元概率进行选择 |
| score-to-probability conversion | 分数到概率的转换 | Turning model scores into probabilities | 把分数转换成概率的过程 |
| probability-to-token selection | 从概率到词元选择 | Use the distribution to choose one token | 用概率分布选出一个词元 |
| selection distribution | 选择分布 | Distribution governing token choice | 决定词元选择的分布 |
| inference-time decoding | 推理时解码 | Decoding used during model inference | 模型回答时执行的解码 |
| decoding strategy | 解码策略 | A strategy for turning scores into output | 把模型分数转成输出的策略 |
| generation control | 生成控制 | A setting that shapes token selection | 调整词元选择方式的控制项 |
| output variability | 输出变化性 | How much generated choices can vary | 不同生成结果可能有多大差异 |
| predictability | 可预测性 | How expected the selected token is | 生成结果有多容易被预料 |
| probability ranking | 概率排序 | Ordering candidate tokens by likelihood | 按可能性给候选词元排序 |
| highest-probability token | 最高概率词元 | The candidate with the greatest estimated probability | 模型认为最可能的候选词元 |
| lower-probability token | 低概率词元 | A candidate with a smaller estimated probability | 模型认为可能性较小的候选词元 |
| model confidence | 模型置信度 | How strongly the model favors an option | 模型对某个选项有多确定 |
| next-token score | 下一个词元分数 | A score assigned to a possible next token | 给候选下一个词元的分数 |
| token probability table | 词元概率表 | A table of candidates and their probabilities | 列出候选词元和概率的表格 |
| probability mass | 概率质量 | The total probability distributed over outcomes | 分配给所有可能结果的总概率 |
| distribution shift from temperature | 温度造成的分布变化 | Change in choices caused by temperature | 温度设置导致的可能性分配变化 |
| stochastic selection | 随机性选择 | Selection that can vary among plausible tokens | 在合理候选中可能每次不同的选择 |
| deterministic selection | 确定性选择 | Selection that consistently favors one rule or option | 按固定规则稳定选择的方式 |
| greedy choice | 贪心选择 | Always select the currently highest-scoring token | 总是选择当前分数最高的词元 |
| top candidate | 首选候选项 | The candidate ranked most favorably | 排名最靠前的候选项 |
| next-position prediction | 下一位置预测 | Predict the token for the next position in a sequence | 预测序列下一个位置的词元 |
| sequence completion | 序列补全 | Extend an existing sequence with more tokens | 给已有序列接上更多词元 |
| continuation probability | 后续概率 | Likelihood assigned to a continuation | 某种后续内容被赋予的可能性 |
| context-dependent prediction | 依赖上下文的预测 | Prediction changes with the available context | 上下文不同，预测也会不同 |
| context-sensitive generation | 上下文敏感生成 | Generation that uses the current sequence | 会参考当前序列的生成方式 |
| model reads, scores, selects, and repeats | 模型读取、打分、选择并重复 | A compact description of the generation cycle | 对生成循环的简短总结 |
| read → score → distribute → select → add → repeat | 读取→打分→分布→选择→加入→重复 | The page’s process in compact notation | 页面生成流程的压缩表示 |
| input → model → next-token distribution → sampling / decoding → new context | 输入→模型→下一个词元分布→采样/解码→新上下文 | The illustrated generation pipeline | 页面图示的生成流水线 |

## Potential Missing Concepts

- The page names scores and probabilities but does not explain logits, log-probabilities, softmax, normalization, or how raw model scores become a probability distribution.
- It distinguishes prediction from sampling but does not name common decoding algorithms such as greedy decoding, temperature sampling, top-k sampling, top-p / nucleus sampling, beam search, typical sampling, or constrained decoding.
- It introduces temperature qualitatively but does not give the usual mathematical temperature transformation, numeric ranges, calibration implications, or the behavior at very low or very high values.
- It does not define stop conditions such as an end-of-sequence (EOS) token, stop sequence, maximum output tokens, length limit, or user cancellation.
- It does not discuss repetition penalty, frequency penalty, presence penalty, no-repeat constraints, or other controls that modify token selection.
- It describes one-token-at-a-time generation but does not explicitly name autoregressive modeling, causal language modeling, causal mask, teacher forcing, or the difference from masked language modeling.
- It does not define tokenization variants such as subword tokens, byte-pair encoding (BPE), WordPiece, SentencePiece, byte-level tokenization, special tokens, or token boundaries.
- It does not explain vocabulary, vocabulary size, token IDs, embeddings, positional information, attention, Transformer layers, or how the model computes candidate scores.
- It mentions context and context window but does not describe maximum context length, truncation, sliding windows, prompt tokens versus generated tokens, or context-window overflow.
- It mentions KV Cache as efficiency support but does not explain key/value tensors, prefill, decode, cache reuse, cache memory, or the difference between prefill and decode phases.
- It does not state the distinction between prefill computation over the prompt and decode computation for each generated token, nor how batching changes the workflow.
- It does not discuss latency, throughput, tokens per second, time to first token (TTFT), inter-token latency, or the cost of repeated generation.
- It does not define evaluation metrics such as token accuracy, negative log-likelihood, cross-entropy loss, perplexity, calibration, exact match, or sequence-level quality.
- It does not explain that the most probable token is not necessarily the best full-sequence continuation, or how local token choices can affect global coherence.
- It does not discuss exposure bias, compounding errors, error propagation, degeneration, blandness, incoherence, or hallucination during autoregressive generation.
- It does not distinguish random sampling from deterministic decoding, reproducibility from variability, random seeds, or provider-specific sampling behavior.
- It does not explain that tokenization can split a word into multiple tokens or that a token is not necessarily a word, character, or semantic unit.
- It does not define prompt, completion, input tokens, output tokens, total tokens, token budget, or billing / usage accounting.
- It does not explain batch generation, parallel requests, speculative decoding, assisted decoding, speculative tokens, or other inference acceleration methods.
- It does not cover beam scores, length normalization, diverse beam search, or why beam search is less common for open-ended chat generation.
- It does not explain structured or constrained generation, grammar-constrained decoding, JSON mode, function/tool-call token sequences, or stop-token handling.
- It does not discuss safety filters, refusal tokens, content moderation, prompt injection, or policy constraints that can intervene in generation.
- It does not discuss uncertainty estimation, entropy, top-1 probability, cumulative probability mass, confidence, or calibration of next-token distributions.
- It does not explain how temperature interacts with top-k, top-p, penalties, or other decoding settings when multiple controls are enabled.
- It does not state that generation may use a chat template, system message, role markers, special delimiters, or hidden control tokens before predicting the next token.
- It does not describe streaming output, partial responses, buffering, retries, or how a user interface exposes one-token-at-a-time generation.
- It does not cover multimodal next-token or next-unit prediction for image, audio, video, or other non-text modalities.
- It does not discuss training objectives for next-token prediction, target shifting, labels, cross-entropy, teacher-forced targets, or the relationship between training and inference distributions.
- It does not define causal attention masks, future-token masking, or why a causal model cannot use later tokens when predicting the current next token.
- It does not discuss sequence likelihood, joint probability, conditional probability, chain rule, or how token probabilities compose into sequence probabilities.
- It does not explain the difference between a probability distribution over vocabulary tokens and a distribution over words, sentences, or full responses.
- It does not cover stop criteria based on EOS, stop strings, special tokens, maximum length, minimum length, or application-level completion rules.
- It does not provide production examples involving API parameters, model-specific defaults, server-side decoding, or reproducible inference configuration.

## Aliases / Synonyms

- Next-token prediction / next token prediction / next-token forecasting / next-token modeling
- Next-token generation / next-token completion / token-by-token generation / one-token-at-a-time generation
- Prediction / next-token estimation / candidate scoring / probability estimation
- Generate text one token at a time / autoregressive generation / causal generation / iterative text generation
- Generation / text generation / sequence generation / response generation / completion generation
- Language model / text model / generative language model / autoregressive language model
- Token / text unit / model-readable text unit / token ID unit (related, not identical)
- Generated token / selected token / chosen token / output token / completion token
- Context / available context / current context / input sequence / prior sequence / prefix
- Context window / maximum context / context length / model context / available context range
- New context / updated context / extended context / context after selection
- Continuation / possible continuation / candidate continuation / completion / suffix (related, not identical)
- Candidate token / possible next token / plausible next token / next-token candidate
- Token distribution / next-token distribution / probability distribution / selection distribution
- Probability / token probability / next-token probability / likelihood (related, not identical)
- Score / token score / next-token score / candidate score / model score
- Probability list / token probability table / candidate probability table / score list
- Select one token / choose one token / sample one token / decode one token
- Sampling / token sampling / probability sampling / stochastic decoding
- Decoding / token decoding / inference-time decoding / output selection
- Sampling / decoding (closely related selection-stage terms, not always identical)
- Prediction versus sampling / scoring versus selection / probability estimation versus token choice
- Temperature / sampling temperature / decoding temperature / temperature parameter
- Lower temperature / conservative sampling / concentrated distribution / more predictable sampling
- Higher temperature / diverse sampling / more variable sampling / flatter distribution (related description)
- Variation / diversity / output variability / sampling variability
- Autocomplete / auto-completion / predictive text / completion suggestion
- Generation loop / autoregressive loop / decode loop / predict-select-add loop
- Add and repeat / append and predict again / update context and continue / iterate generation
- Tokenization / tokenisation / text splitting / text-to-token conversion
- Tokens, Context & Inference / tokens and context / token-context-inference workflow
- Inference / model inference / runtime generation / query-time generation
- Model parameters / learned parameters / weights / model weights (related, not all exact synonyms)
- Training / model training / parameter learning / parameter updating
- Prediction during inference / inference-time prediction / runtime prediction
- KV Cache / key-value cache / attention KV cache / key-value memory
- Generated text / model response / completion / final response / output sequence
- Illustrative probability / example probability / demonstration probability / non-production probability
- Selected continuation / completed sequence / extended sequence / new sequence
- Probability distribution / categorical distribution over vocabulary / vocabulary distribution
- High-probability choice / top candidate / most likely token / highest-scoring token
- Low-probability choice / less-likely token / lower-ranked candidate / tail candidate
- Context-dependent prediction / context-sensitive prediction / conditional next-token prediction
- Sequence completion / text completion / prompt completion / continuation generation
- Autoregressive model / causal language model / decoder-only language model (related architecture family)
- Greedy decoding / argmax decoding / maximum-probability decoding
- Top-k sampling / truncated sampling / k-best sampling
- Top-p sampling / nucleus sampling / cumulative-probability sampling
- EOS / end-of-sequence token / stop token / completion terminator

## Do Not Confuse Candidates

- Prediction ≠ sampling: prediction scores or assigns probabilities to many possibilities; sampling or decoding selects one token for the current step.
- Sampling ≠ randomness without structure: sampling uses the model’s probability distribution, even when the selected result can vary.
- Prediction ≠ generation: prediction is one estimation step; generation repeatedly predicts and selects tokens to build a sequence.
- One token ≠ one word: a token may be a word, a subword, punctuation, whitespace, or another text fragment.
- One step ≠ a full answer: one next-token decision is only one small part of a final response.
- Next-token prediction ≠ whole-response prediction: the model does not select the entire response in one undivided operation.
- Context ≠ model parameters: context is information available during this run; parameters are learned internal values.
- Context ≠ memory in every sense: current context is supplied or accumulated at runtime, while long-term memory may be a separate system.
- Context window ≠ output length: the context window covers available input and generated context; output length is only one part of it.
- Tokenization ≠ next-token prediction: tokenization creates the units; next-token prediction estimates the next unit.
- Token ≠ character: one token can contain multiple characters, and a character may be part of a larger token.
- Token ≠ word: words can split into several tokens, and a token can contain punctuation or part of a word.
- Score ≠ probability: scores may be raw model values; probabilities are normalized likelihood values or an interpretation of them.
- Probability ≠ certainty: a high probability is a model estimate, not a guarantee that the token is correct.
- Probability distribution ≠ chosen token: the distribution contains many possibilities; the selected token is one outcome.
- Highest probability ≠ guaranteed choice: a sampling or decoding rule may choose a lower-probability token.
- Temperature ≠ model retraining: temperature changes runtime selection behavior; it does not update model parameters.
- Temperature ≠ creativity switch: temperature changes the distribution and variation, but does not directly create knowledge or reasoning ability.
- Lower temperature ≠ always better: it can improve predictability while reducing variation and sometimes making outputs repetitive.
- Higher temperature ≠ always random: higher temperature can make lower-probability options more competitive, but selection remains distribution-guided.
- Sampling ≠ training: sampling chooses an output token during use; training updates parameters from data.
- Inference ≠ training: inference applies a trained model; training changes the model through parameter updates.
- Prediction during inference ≠ parameter update: producing a token normally does not change the model’s learned parameters.
- Model output ≠ model parameter: output is returned for an input; a parameter is internal learned state.
- Generated token ≠ selected distribution: the token is one selected result, while the distribution describes all candidate probabilities.
- KV Cache ≠ prediction rule: KV Cache supports repeated-generation efficiency but does not decide which token is correct.
- KV Cache ≠ long-term memory: it stores computation-related attention states for a current sequence, not necessarily durable user memory.
- Autocomplete analogy ≠ literal implementation: autocomplete helps explain the loop; language models use learned patterns over the full available context.
- Illustrative probabilities ≠ real model output: the 52%, 18%, 11%, 87%, 4%, and 2% values are explanatory examples.
- “Blue” ≠ guaranteed next token: it is the selected token in the page’s sky illustration, not a universal model result.
- “France” ≠ a general decoding rule: it is the selected answer in the page’s Paris example.
- Prompt ≠ training data: a prompt supplies runtime input; training data is used to teach or update a model.
- Prompt ≠ context window: a prompt can become part of the context, but the context can also include generated tokens and system-provided information.
- Context ≠ continuation: context is what is already available; continuation is what may be added next.
- Candidate continuation ≠ final response: a candidate is one possibility; the final response is built from many selected tokens.
- Decoding ≠ tokenization: decoding selects or reconstructs output from model representations; tokenization divides text into tokens.
- Greedy decoding ≠ all sampling: greedy decoding deterministically chooses the top candidate; sampling can choose among multiple candidates.
- Temperature sampling ≠ top-k or top-p sampling: temperature rescales preferences, while top-k/top-p restrict the candidate set; they can be combined.
- Sequence probability ≠ individual token probability: a sequence probability depends on the conditional probabilities of its tokens together.
- Per-token probability ≠ semantic quality: a likely token is not automatically the most useful, truthful, or safe continuation.
- Local token score ≠ whole-answer quality: token-level scores do not by themselves prove coherence, factuality, or usefulness of the final answer.
- Final response ≠ one prediction: the complete response emerges from repeated generation and many local decisions.
- Generation loop ≠ infinite loop: production generation normally has stopping conditions such as EOS, a stop sequence, or a maximum output length.
- Inference-time configuration ≠ learned capability: temperature and decoding settings shape use-time behavior but do not add knowledge to the model.

## Notes

- This is intentionally an expansive raw candidate inventory, not a deduplicated final glossary. Repeated wording, capitalization variants, page labels, process phrases, example terms, and closely related concepts are retained.
- The source page directly covers the definition of next-token prediction, reading context, scoring possible continuations, forming a probability distribution, selecting one token, adding it to new context, and repeating the loop.
- The source page explicitly separates prediction from sampling: prediction produces scores or probabilities for many possible tokens, while sampling produces one chosen token.
- The source page treats decoding as the rule or stage that chooses one token; “sampling / decoding” is therefore preserved as a paired phrase, while decoding and sampling remain separate candidates because they are not technically identical in every system.
- The page introduces temperature qualitatively: lower temperature is associated with more conservative and predictable choices; higher temperature makes lower-probability choices more competitive and increases variation.
- The examples “I would like a cup of ...”, “The sky is”, and “Paris is the capital of” are retained because they are part of the page’s explanatory vocabulary and make candidate meanings traceable to the source.
- The example probabilities are explicitly illustrative and not real model outputs. They are retained as raw candidates because the task calls for indicators, values, and source wording without early deletion.
- The page’s “What it is NOT” section explicitly contrasts prediction with sampling, prediction with training, and one step with a full answer; these contrasts are repeated in the Do Not Confuse section.
- The related-concepts chain is preserved as a source relationship: Tokenization → Tokens → Context Window → Inference → Next-token Prediction → Sampling / Temperature → Generated Token. KV Cache is described as side efficiency support during repeated generation.
- The HTML contains no explicit model name, API parameter name, benchmark, loss function, perplexity figure, token-accuracy metric, or production latency metric. These are therefore listed as potential missing concepts rather than presented as page facts.
- Important standard extensions such as autoregressive generation, causal language modeling, logits, softmax, top-k, top-p, EOS, perplexity, and TTFT are included as missing or related candidates for later editorial review, not as claims that the page defines them.
- “Prediction,” “score,” “probability,” “sampling,” “decoding,” “temperature,” and “KV Cache” should remain distinct in a final glossary unless a later editorial pass deliberately merges them with cross-references.
- The page is explanatory and introductory. It emphasizes the conceptual loop and does not expose the underlying neural-network computation, vocabulary logits, attention computation, or mathematical training objective.
- The final response is presented as an emergent result of many small prediction-and-selection steps; the page does not claim that every implementation must use the exact same decoding rule or runtime configuration.
