# Topic

Sampling / Temperature

## Module/Topic/Source File

- Module: 05 · Tokens, Context & Inference
- Topic: Topic 07 · Sampling / Temperature
- Page title: What are Sampling and Temperature?
- Source File: `sampling-temperature.html`
- Page language: English
- Source body sections: What is it?; Think of it like...; How it works; Real-world examples; What it is NOT; Related concepts; Remember this; Video

## Glossary Candidates

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| sampling | 采样 | A method for choosing the next token from possible choices. | 从模型认为可能的选项里选出下一个词元的办法。 |
| sample | 采样；抽取 | Select one outcome from a set of possible outcomes. | 从一组可能结果中抽取一个结果。 |
| sampling method | 采样方法 | A rule used to select an outcome from a distribution. | 按某种规则从概率分布中选结果。 |
| selection | 选择 | The act of choosing one available option. | 从可用选项里挑出一个。 |
| choose | 选择 | Pick one option from several possibilities. | 在多个可能性中选一个。 |
| next token | 下一个词元 | The token selected to come next in generated text. | 生成文字时接下来要放入的文字单位。 |
| token | 词元；标记 | A small unit of text processed by a language model. | 语言模型处理文字时使用的一小块文字单位。 |
| text token | 文本词元 | A token that represents part of written text. | 表示部分文字的词元。 |
| possible choice | 可能选项 | One outcome the model could select next. | 模型下一步可能选出的一个选项。 |
| possible next token | 可能的下一个词元 | A token that could follow the current context. | 在当前上下文后可能出现的词元。 |
| probability | 概率 | A number describing how likely an outcome is. | 用数字表示某个结果有多可能发生。 |
| probability distribution | 概率分布 | Probabilities assigned across possible outcomes. | 把不同可能结果各自的可能性列出来。 |
| token probability | 词元概率 | The probability assigned to a particular token. | 某个词元被选中的可能性数值。 |
| token probabilities | 词元概率（复数） | Probabilities assigned to possible tokens. | 不同可能词元各自的可能性。 |
| next-token probability | 下一个词元概率 | The probability of each candidate for the next position. | 对下一位置每个候选词元的可能性估计。 |
| relative probability | 相对概率 | A probability considered in relation to the other choices. | 和其他选项相比的可能性大小。 |
| updated relative probability | 更新后的相对概率 | A revised probability compared with the other choices. | 调整后、相对于其他选项的可能性。 |
| probability shape | 概率形状 | How probability is concentrated or spread across choices. | 概率在选项之间集中还是分散的状态。 |
| distribution shape | 分布形状 | The pattern of how probability is allocated. | 概率在各个选项上如何分配的样子。 |
| temperature | 温度 | A generation setting that changes how concentrated token probabilities are. | 一个会改变词元概率集中程度的生成设置。 |
| generation setting | 生成设置 | A configurable option that affects generation behavior. | 可以调节生成行为的设置项。 |
| temperature setting | 温度设置 | The chosen temperature value used during generation. | 生成时采用的温度数值。 |
| adjust | 调整 | Change a setting or distribution. | 改变设置或概率分布。 |
| adjust the distribution | 调整分布 | Change how probability is allocated among choices. | 改变概率在各个选项之间的分配方式。 |
| adjustment | 调整 | A change made before selection. | 在选择前做出的改变。 |
| before selection | 选择之前 | The stage before one token is chosen. | 真正选出词元之前的阶段。 |
| concentrated | 集中的 | Having most probability near a few choices. | 大部分概率集中在少数选项上。 |
| more concentrated | 更集中 | Having probability focused more strongly on top choices. | 概率更偏向排名靠前的选项。 |
| less concentrated | 不那么集中 | Having probability spread more across choices. | 概率在更多选项之间分散。 |
| higher-probability choice | 高概率选项 | An option assigned a relatively large probability. | 模型认为更可能出现的选项。 |
| top-ranked option | 排名最高的选项 | The option with the strongest rank among candidates. | 候选项中排名最靠前的选项。 |
| lower-ranked option | 排名较低的选项 | An option with a lower rank than the leading choices. | 排名低于前几个选项的选项。 |
| variation | 变化；多样性 | Differences that can appear between generated outputs. | 多次生成的结果之间可能出现的不同。 |
| increase variation | 增加变化 | Make different outcomes more likely across runs. | 让每次生成更可能出现不同结果。 |
| selection behavior | 选择行为 | How the system tends to choose among candidates. | 系统在候选项之间倾向怎样选择。 |
| randomness | 随机性 | Variation caused by choosing among multiple possible outcomes. | 结果不是每次完全一样的程度。 |
| generation | 生成 | Producing an output sequence one piece at a time. | 一次一小块地产出完整结果。 |
| generated output | 生成输出 | The content produced by the model. | 模型生成出来的内容。 |
| output | 输出 | The result returned by the system. | 系统处理后返回的结果。 |
| output sequence | 输出序列 | An ordered series of generated tokens. | 按顺序组成的生成词元序列。 |
| growing output | 不断增长的输出 | Output that becomes longer as tokens are added. | 随着新词元加入而逐渐变长的结果。 |
| continuation | 续写；延续内容 | Text that continues an existing input. | 接在已有输入后面的文字。 |
| selected continuation | 选出的续写 | One continuation chosen from possible continuations. | 从多种可能续写中选出的那一种。 |
| generated response | 生成的回答 | A response produced by a model. | 模型生成的一段回答。 |
| variation across runs | 多次运行之间的变化 | Differences in output from repeated generation attempts. | 同一个输入重复生成时结果可能不同。 |
| decoder | 解码器 | The component or procedure that turns probabilities into selected output tokens. | 把概率变成实际输出词元的部分或过程。 |
| decoding | 解码 | The process of selecting output tokens from model scores or probabilities. | 根据模型分数或概率逐步选出输出词元。 |
| selection rule | 选择规则 | The rule that determines which candidate is chosen. | 决定选哪个候选项的规则。 |
| another selection method | 另一种选择方法 | A method other than sampling for choosing a token. | 除采样以外的词元选择办法。 |
| choose by the rule | 按规则选择 | Select an outcome according to the active method. | 根据当前采用的方法选结果。 |
| model | 模型 | A learned system that assigns probabilities to possible next tokens. | 会根据上下文估计下一个词元可能性的系统。 |
| language model | 语言模型 | A model that learns patterns in language and generates text. | 学习语言规律并生成文字的模型。 |
| model prediction | 模型预测 | The model's estimate of possible next outcomes. | 模型对下一步可能结果的估计。 |
| prediction | 预测 | Estimating what may come next or what an input means. | 根据已有信息估计下一步结果。 |
| next-token prediction | 下一个词元预测 | Estimating probabilities for the next token. | 预测下一个词元可能是什么。 |
| predict | 预测 | Estimate the next possible result. | 估计接下来可能出现的结果。 |
| predict and select | 预测并选择 | First estimate candidates, then choose one. | 先列出可能性，再选出一个。 |
| token selection | 词元选择 | Choosing one token for the next output position. | 为输出的下一个位置挑一个词元。 |
| inference | 推理；推断 | Using a model to produce an output for an input. | 用已经有的模型处理输入并给出结果。 |
| inference loop | 推理循环 | Repeating prediction and selection until generation ends. | 不断预测、选择，直到生成停止的循环。 |
| loop | 循环 | A repeated sequence of operations. | 一组动作反复进行。 |
| repeat the loop | 重复循环 | Run the prediction-and-selection cycle again. | 再次执行预测和选择这套流程。 |
| continue generation | 继续生成 | Produce another token after the current token. | 在当前词元后继续生成下一个词元。 |
| generation process | 生成过程 | The sequence of steps used to create output. | 产生输出时经历的一连串步骤。 |
| process step | 流程步骤 | One stage in a larger process. | 一整套流程中的一个阶段。 |
| process flow | 流程图；流程 | An ordered path through generation stages. | 按顺序展示生成各阶段的流程。 |
| next-token probabilities step | 下一个词元概率步骤 | The stage where possible next tokens receive probabilities. | 给可能的下一个词元分配概率的阶段。 |
| apply generation settings step | 应用生成设置步骤 | The stage where generation settings alter the distribution. | 用生成设置改变概率分布的阶段。 |
| adjusted distribution step | 调整后分布步骤 | The stage with updated relative probabilities. | 已经得到更新后相对概率的阶段。 |
| sampling method step | 采样方法步骤 | The stage where the decoder applies a selection method. | 解码器按选择方法挑选词元的阶段。 |
| selected token step | 选定词元步骤 | The stage where one token is added to output. | 把一个选中的词元加入输出的阶段。 |
| continue generation step | 继续生成步骤 | The stage where the model begins the next cycle. | 进入下一轮预测和选择的阶段。 |
| list possible choices | 列出可能选项 | Enumerate candidate next tokens. | 列出下一步可能出现的词元。 |
| assign probabilities | 分配概率 | Give each candidate a likelihood value. | 给每个候选项一个可能性数值。 |
| adjust the distribution | 调整概率分布 | Reshape the relative likelihoods of candidates. | 改变候选项之间的相对可能性。 |
| rank the chances | 按可能性排序 | Order choices by their relative probabilities. | 按可能性大小排出选项顺序。 |
| updated probabilities | 更新后的概率 | Probabilities after a generation setting is applied. | 应用生成设置后的概率。 |
| add one token | 加入一个词元 | Append one selected token to the output. | 把选定的一个词元接到输出后面。 |
| possible token | 可能的词元 | A token available as a candidate at the next position. | 下一位置可以考虑的一个词元。 |
| ranked menu | 排名菜单 | An analogy in which choices are ordered from likely to less likely. | 把候选选项想成按排名排列的菜单。 |
| ranked option | 排名选项 | An option placed in an order relative to others. | 和其他选项比较后排了名的选项。 |
| low temperature | 低温 | A low setting that usually favors high-probability choices. | 较低设置，通常更偏向高概率选项。 |
| high temperature | 高温 | A high setting that usually spreads probability more broadly. | 较高设置，通常让概率分布得更广。 |
| top-ranked choices | 排名靠前的选择 | The leading candidates in a ranked set. | 一组候选项里排在前面的选项。 |
| lower-ranked choices | 排名靠后的选择 | Candidates below the leading options. | 排名低于前面选项的候选项。 |
| better chance | 更大的机会 | A relatively increased likelihood of being selected. | 被选中的可能性相对变大。 |
| selected outcome | 选定结果 | The one outcome produced after selection. | 选择步骤最终产出的那个结果。 |
| food menu analogy | 食物菜单类比 | An analogy comparing token choices with choosing food. | 用点餐来帮助理解词元选择。 |
| menu | 菜单 | A ranked set of choices in the page's analogy. | 页面类比中代表候选项列表的菜单。 |
| choose food | 选择食物 | Pick an item from a menu in the analogy. | 类比中从菜单里挑一种食物。 |
| everyday example | 日常示例 | A familiar example used to explain the mechanism. | 用日常场景解释机制的例子。 |
| real-world example | 真实世界示例 | An example showing how the concept appears in practice. | 说明这个概念在实际场景中如何出现的例子。 |
| completing a message | 补全消息 | Continuing a partially written message. | 把一条没写完的消息接着写下去。 |
| message | 消息 | A piece of text that can be completed. | 可以被续写的一段文字。 |
| input | 输入 | Information supplied to the model. | 交给模型处理的信息。 |
| system | 系统 | The model-and-generation process that compares or samples choices. | 负责比较候选项并生成结果的系统。 |
| likely next token | 可能的下一个词元 | A candidate the system considers likely to follow the input. | 系统认为接下来可能出现的词元。 |
| station | 车站 | One example of a likely continuation in the message example. | 页面消息例子中可能接在句子后的地点词。 |
| office | 办公室 | One example of a likely continuation in the message example. | 页面消息例子中可能接在句子后的另一个地点词。 |
| chat assistant | 聊天助手 | An AI product that generates responses to user messages. | 根据用户消息生成回答的 AI 助手。 |
| slogan idea | 标语创意 | A possible slogan proposed by the assistant. | 聊天助手可以生成的一种宣传语想法。 |
| slogan | 标语 | A short phrase used to express an idea or brand message. | 用短句表达想法或品牌信息的文字。 |
| several ideas | 多个想法 | More than one candidate idea requested by the user. | 用户要求系统提供的不止一个创意。 |
| user | 用户 | The person who supplies an input or request. | 向系统提出问题或要求的人。 |
| request | 请求 | An instruction or question given to the assistant. | 用户交给助手要完成的事情。 |
| temperature-selected generation | 按温度设置的生成 | Generation in which temperature changes the selection distribution. | 温度设置参与改变选词概率的生成。 |
| creativity | 创造力；创意性 | A broad description of how novel or varied an output seems. | 描述结果是否新颖、多样的宽泛说法。 |
| accuracy | 准确性 | How well an output matches what is correct or expected. | 结果与正确答案或预期是否相符。 |
| task | 任务 | The work the model is asked to perform. | 用户让模型完成的一件事。 |
| data | 数据 | Information used by a model or evaluation. | 模型处理或评估时使用的信息。 |
| evaluation | 评估 | Measuring the quality or suitability of a result. | 检查结果质量和适用性的过程。 |
| direct model setting | 直接模型设置 | A setting exposed as a control for model behavior. | 可以直接调节模型行为的配置项。 |
| output quality | 输出质量 | How correct, useful, and suitable the generated result is. | 生成结果是否正确、有用、合适。 |
| task performance | 任务表现 | How well the system performs a particular task. | 系统完成指定任务的效果。 |
| related concept | 相关概念 | A concept connected to the topic. | 和当前主题有关、需要一起理解的概念。 |
| context | 上下文 | Surrounding information used to interpret the next token. | 帮助模型判断下一词元的前后文字信息。 |
| context window | 上下文窗口 | The amount of context a model can process at once. | 模型一次能看到的上下文范围。 |
| output as a growing sequence | 逐渐增长的输出序列 | An output formed by adding tokens one by one. | 一个个加入词元、逐步变长的输出。 |
| generation setting versus selection method | 生成设置与选择方法 | A setting changes probabilities; a method chooses from them. | 设置改变可能性，方法负责从可能性中选结果。 |
| probability creation | 概率生成 | Producing probabilities for candidate next tokens. | 先算出各个候选词元可能性的过程。 |
| probability-based selection | 基于概率的选择 | Choosing an outcome using assigned probabilities. | 按候选项概率来选出结果。 |
| temperature-controlled variation | 温度控制的变化 | Output variation influenced by the temperature setting. | 温度设置影响下的输出多样性。 |
| explicit abbreviation | 明示缩写 | A shortened form such as an initialism shown in the source. | 页面正文中明确写出的英文缩写形式。 |
| topic | 主题 | The subject explained by the page. | 这一页面集中解释的知识主题。 |
| video | 视频 | A visual explainer associated with the topic. | 用画面解释主题的媒体内容。 |
| visual explainer | 可视化讲解 | A video or visual resource that explains an idea. | 用视觉方式帮助理解概念的讲解材料。 |
| video unavailable | 视频暂不可用 | A status meaning the topic video is not available yet. | 表示该主题的视频目前还没有。 |

## Potential Missing Concepts

- The source explains sampling and temperature conceptually but does not define logits, log-probabilities, softmax, or the mathematical temperature transformation.
- The source does not explain greedy decoding, argmax selection, deterministic decoding, multinomial sampling, beam search, or how these compare with sampling.
- The source does not name or explain top-k sampling, top-p sampling (nucleus sampling), typical sampling, min-p sampling, or other truncation rules.
- The source does not explain whether temperature changes logits before softmax, changes probabilities directly, or how an implementation handles temperature equal to zero.
- The source does not explain random seeds, pseudo-random number generators, reproducibility, or why repeated runs can differ.
- The source does not introduce entropy, perplexity, calibration, confidence, uncertainty, or diversity metrics for describing a distribution or output.
- The source does not explain repetition penalty, frequency penalty, presence penalty, stop sequences, maximum output tokens, or other generation controls that can interact with temperature.
- The source does not describe tokenization, vocabulary, token IDs, subword tokens, special tokens, end-of-sequence tokens, or how a token differs from a word.
- The source does not explain how a language model computes next-token probabilities from context, including neural-network layers, hidden states, embeddings, attention, or logits.
- The source does not distinguish model training from inference in detail, or explain why temperature is generally an inference-time generation setting.
- The source does not provide numerical examples, probability tables, plots, pseudocode, equations, or API parameter examples.
- The source does not define how temperature affects factuality, calibration, safety, refusal behavior, or task-specific accuracy in a particular model.
- The source does not establish a recommended temperature range or a rule for choosing temperature by task.
- The source does not define evaluation protocols for comparing runs, such as fixed prompts, multiple samples, human ratings, automated metrics, or statistical significance.
- The source does not cover production concerns such as latency, throughput, cost, streaming, caching, rate limits, or serving infrastructure.
- The source does not explain the difference between probability, likelihood, score, confidence, preference, and ranking.
- The source does not explain the interaction between temperature and the candidate set, including whether low-probability candidates are removed or merely down-weighted.
- The source does not explain that “higher temperature” is a metaphor borrowed from the transformation setting and is not physical heat.
- No explicit abbreviation is used in the source body for sampling, temperature, next-token prediction, or the decoding process.

## Aliases / Synonyms

- sampling / probabilistic sampling / stochastic sampling / probability-based selection / 采样 / 概率采样 / 随机采样（相关表达；不一定在所有实现中完全同义）
- sampling method / selection method / decoding method / 采样方法 / 选择方法 / 解码方法
- sample a token / select a token / choose a token / draw a token / 采样词元 / 选择词元 / 抽取词元
- next token / next text token / next output token / 下一个词元 / 下一个文本词元 / 下一个输出词元
- probability distribution / token probability distribution / next-token distribution / 概率分布 / 词元概率分布 / 下一个词元分布
- probability of a token / token likelihood / token probability / 词元概率 / 词元似然（相关术语）
- temperature / temperature parameter / temperature setting / 温度 / 温度参数 / 温度设置
- generation setting / decoding setting / generation parameter / 生成设置 / 解码设置 / 生成参数
- low temperature / lower temperature / low-temperature decoding / 低温 / 较低温度 / 低温解码
- high temperature / higher temperature / high-temperature decoding / 高温 / 较高温度 / 高温解码
- concentrated distribution / peaked distribution / sharp distribution / 集中的分布 / 尖锐分布 / 高峰分布
- broadly spread distribution / flatter distribution / diffuse distribution / 分散的分布 / 平坦分布 / 弥散分布
- variation / output diversity / generation diversity / 变化 / 输出多样性 / 生成多样性
- randomness / stochasticity / 随机性 / 随机程度
- decoder / decoding procedure / output selection procedure / 解码器 / 解码过程 / 输出选择过程
- decoding / token decoding / sequence decoding / 解码 / 词元解码 / 序列解码
- next-token prediction / next-token probability prediction / predicting the next token / 下一个词元预测 / 预测下一个词元
- prediction / model prediction / probability prediction / 预测 / 模型预测 / 概率预测
- inference / inference-time generation / generation-time inference / 推理 / 推理时生成 / 生成时推理
- output / generated output / model output / 生成结果 / 模型输出 / 输出
- continuation / text continuation / message completion / 续写 / 文本续写 / 消息补全
- chat assistant / conversational assistant / AI assistant / 聊天助手 / 对话助手 / AI 助手
- probability choice / candidate choice / possible choice / 概率选项 / 候选选项 / 可能选项
- top choice / top-ranked option / highest-probability option / 首选项 / 排名最高选项 / 最高概率选项
- lower-ranked option / less likely option / low-probability option / 低排名选项 / 较不可能选项 / 低概率选项
- selected token / chosen token / sampled token / 选定词元 / 选出的词元 / 采样出的词元
- growing output / generated sequence / output sequence / 增长中的输出 / 生成序列 / 输出序列
- repeat the loop / iterative generation / autoregressive generation / 重复循环 / 迭代生成 / 自回归生成（相关扩展术语）
- creativity / novelty / originality / 创造力 / 新颖性 / 原创性（相关描述，不是温度的直接同义词）
- accuracy / correctness / task accuracy / 准确性 / 正确性 / 任务准确率（相关描述，不是温度的直接同义词）
- context / prompt context / surrounding context / 上下文 / 提示上下文 / 周围上下文
- context window / maximum context / context length / 上下文窗口 / 最大上下文 / 上下文长度
- explicit abbreviation / acronym / initialism / 缩写 / 首字母缩写 / 初始字母缩写
- video / visual explainer / topic video / 视频 / 可视化讲解 / 主题视频

## Do Not Confuse Candidates

- Sampling vs Prediction: prediction produces probabilities for possible next tokens; sampling selects one token from those possibilities.
- Sampling vs Selection: sampling is one probability-based selection method; selection is the broader act of choosing an option.
- Sampling vs Decoding: decoding is the broader process of turning model scores or probabilities into output; sampling is one decoding strategy.
- Sampling vs Greedy Decoding: sampling can choose a non-top candidate; greedy decoding always selects the currently highest-probability candidate.
- Sampling vs Beam Search: sampling follows probabilistic choices; beam search keeps and compares multiple partial sequences.
- Temperature vs Creativity: temperature changes probability concentration; creativity is a broad description of how novel or varied an output seems.
- Temperature vs Randomness: temperature can influence variation and stochastic behavior, but it is not identical to every source of randomness in generation.
- Temperature vs Accuracy: temperature changes selection behavior; accuracy depends on the model, task, data, and evaluation method.
- Temperature vs Quality: temperature can affect output quality for a task, but it is not itself a quality score.
- Temperature vs Probability: temperature is a setting that changes a distribution; probability is the likelihood assigned to an outcome.
- Temperature vs Probability Distribution: temperature modifies how probabilities are concentrated; the distribution is the resulting allocation of probabilities.
- Temperature vs Top-k Sampling: temperature reshapes relative probabilities; top-k restricts candidates to a selected number of top options.
- Temperature vs Top-p Sampling: temperature changes concentration; top-p restricts candidates to a cumulative-probability nucleus.
- Temperature vs Seed: temperature is a generation setting; a seed controls the starting state of a pseudo-random process.
- Temperature vs Model Parameter: temperature is generally an inference-time generation control; learned model parameters are values learned during training.
- Temperature vs Hyperparameter: temperature may be called a generation hyperparameter in some systems, but it is distinct from training hyperparameters such as learning rate.
- Probability vs Likelihood: probability usually describes uncertainty over outcomes; likelihood evaluates data under a parameterized model, even though the terms are sometimes used loosely.
- Probability vs Score: a score may rank candidates without being a normalized probability; the page specifically describes a probability distribution.
- Probability vs Confidence: probability has a formal distribution meaning; confidence may be an informal or calibrated interpretation of certainty.
- Ranking vs Probability: ranking orders candidates; probability assigns quantities to them and can express relative chance.
- Next Token vs Word: a token may be a whole word, part of a word, punctuation, or another text unit.
- Token vs Character: a token is the model's processing unit and may contain one or more characters.
- Token vs Output: a token is one small unit; output is the complete result made from one or more tokens.
- Input vs Context: input is the supplied content; context is the surrounding information used to interpret the next choice.
- Context Window vs Output Length: context window describes what the model can use as context; output length describes how much it generates.
- Inference vs Training: inference applies an existing model to generate output; training updates model parameters from data.
- Generation vs Completion: generation is the broad production process; completion is generation that continues an existing partial input.
- Generated Response vs Slogan Idea: a generated response is the full assistant output; a slogan idea is one possible content type within it.
- Selected Continuation vs Entire Output: a continuation is the next portion added to an input; the entire output may contain many continuations.
- Low Temperature vs Deterministic Output: low temperature usually favors top choices but does not automatically guarantee identical outputs in every implementation.
- High Temperature vs Uniform Distribution: high temperature can spread probabilities more broadly but does not necessarily make all choices equally likely.
- Higher-probability Choice vs Guaranteed Choice: a larger probability means more chance, not certainty.
- Variation Across Runs vs Model Improvement: output differences across runs do not mean the model learned or improved.
- Sampling Method vs Generation Setting: the method determines how to choose; the setting changes the inputs to that choice.
- Decoder vs Language Model: the language model predicts probabilities; the decoder applies a method to turn them into output tokens.
- Output Quality vs Accuracy: quality can include usefulness, style, and suitability; accuracy is correctness relative to a target or expected answer.
- Accuracy vs Creativity: accuracy concerns correctness; creativity concerns novelty or variation and may not have a single ground truth.
- Evaluation vs Selection: evaluation measures a result; selection chooses a token during generation.
- System vs Model: the system may include the model, generation settings, selection process, and product behavior; the model is one component.
- Chat Assistant vs Language Model: a chat assistant is a user-facing product or role; a language model is the underlying model that can generate text.
- Real-world Example vs Mechanism: an example illustrates the idea; the mechanism explains the ordered computation.
- Video vs Text Explanation: the page lists a video as unavailable; the written sections are the available explanation.

## Notes

- Raw collection intentionally keeps a broad, overlapping candidate set. Repeated terms, grammatical variants, process labels, examples, aliases, and boundary concepts are retained rather than deduplicated.
- The primary evidence is the complete body of `sampling-temperature.html`, including the page title, lede, on-page navigation labels, definition, menu analogy, six-step process flow, two real-world examples, three “What it is NOT” comparisons, related-concept tree, takeaway, and video status.
- The core source distinction is: prediction creates a probability distribution for possible next tokens; sampling selects a next token from that distribution; temperature changes the distribution's concentration before selection.
- The source explicitly says lower temperature usually makes higher-probability choices more dominant, while higher temperature usually spreads probability more broadly and can increase variation.
- The word “usually” is retained conceptually: the page gives a general behavior, not an absolute guarantee for every implementation or task.
- “Temperature” is retained as both a plain-language metaphor in the ranked-menu analogy and a technical generation setting.
- “Creativity,” “accuracy,” “quality,” “randomness,” and “variation” are deliberately separate candidates because the “What it is NOT” section distinguishes them from temperature or from one another.
- The six process nodes are retained as candidates even where their labels overlap with the explanatory text: Next-token Probabilities, Apply Generation Settings, Adjusted Distribution, Sampling Method, Selected Token, and Continue Generation.
- The body uses “decoder” and “another selection method” without naming specific decoding algorithms; those unnamed algorithms are listed under Potential Missing Concepts rather than treated as explicit page content.
- The real-world examples deliberately retain “station,” “office,” “chat assistant,” and “slogan ideas” because the raw collection is meant to preserve source vocabulary, not only abstract technical terms.
- No explicit abbreviation such as “LLM,” “NTP,” “T,” “top-k,” or “top-p” appears in the source body. Abbreviation-related language is retained only as a metadata/candidate note and as a missing-concepts boundary.
- The source's links point to related concepts including Inference, Next-token Prediction, Token, and Context Window; these are retained even though the page's focus is sampling and temperature.
- The video card says “Video unavailable” and “A video for this topic is not available yet.” These are content/media-status candidates only; this task does not modify the website, CSS, JavaScript, video assets, or GitHub.
- This file is an unfiltered raw glossary-candidate collection for later review. It is not a final approved glossary and does not claim that every candidate has a full definition on the source page.
