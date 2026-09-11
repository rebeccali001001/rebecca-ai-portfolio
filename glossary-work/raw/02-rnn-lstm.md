# Topic

RNN / LSTM

Module: 02 · Neural Networks & Model Architectures

Topic: RNN / LSTM

Source File: `rnn-lstm.html`

## Glossary Candidates

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| RNN | 循环神经网络缩写 | Short for Recurrent Neural Network. | RNN 是 Recurrent Neural Network 的缩写。 |
| Recurrent Neural Network | 循环神经网络 | A neural network that carries information from earlier sequence steps into later processing. | 一边按顺序处理数据，一边把前面学到的信息带到后面。 |
| recurrent network | 循环网络 / 递归网络 | A network that processes sequence items recurrently and carries state forward. | 会反复按时间顺序处理数据、并把状态传下去的网络。 |
| recurrent neural network architecture | 循环神经网络架构 | A neural-network design built for step-by-step sequence processing. | 专门用来逐步处理序列数据的一种神经网络设计。 |
| recurrent-network architecture | 循环网络架构 | Another wording for a recurrent architecture. | recurrent network architecture 的另一种说法。 |
| LSTM | 长短期记忆网络缩写 | Short for Long Short-Term Memory. | LSTM 是 Long Short-Term Memory 的缩写。 |
| Long Short-Term Memory | 长短期记忆 | A recurrent architecture designed to retain useful information across longer sequences. | 一种更擅长在较长序列中保留有用信息的循环网络。 |
| neural-network architecture | 神经网络架构 | A structured design for how a neural network processes information. | 神经网络内部如何组织、传递和处理信息的设计。 |
| neural network | 神经网络 | A model made of connected computational units that transforms inputs into outputs. | 由许多相连计算单元组成、把输入变成输出的模型。 |
| architecture | 架构 | The overall design of a model or system. | 模型或系统整体是怎样搭起来的。 |
| sequence | 序列 | An ordered collection of items processed in a particular order. | 有先后顺序的一串数据。 |
| sequence data | 序列数据 | Data whose order carries meaning. | 顺序本身有意义的数据，例如一句话或一串时间测量值。 |
| sequence processing | 序列处理 | Processing ordered items one at a time while carrying context. | 按顺序逐个处理数据，同时保留前面的上下文。 |
| sequence task | 序列任务 | A task involving ordered inputs, outputs, or both. | 输入或输出带有顺序关系的任务。 |
| step-by-step processing | 逐步处理 | Processing one sequence item at a time. | 一次处理一个数据项，而不是一下子处理完全部。 |
| sequence step | 序列步骤 / 时间步 | One position or processing moment in a sequence. | 序列中的一个位置或一次处理时刻。 |
| earlier sequence step | 较早的序列步骤 | A sequence position processed before the current position. | 当前数据之前已经处理过的步骤。 |
| later processing | 后续处理 | Processing that happens after earlier sequence steps. | 在前面步骤之后进行的处理。 |
| ordered data | 有序数据 | Data items that arrive or are interpreted in order. | 按固定先后顺序到来的数据。 |
| current item | 当前数据项 | The item being processed at the present sequence step. | 网络此刻正在处理的那一项数据。 |
| item | 数据项 | One element of an ordered input. | 一串数据中的一个元素。 |
| information | 信息 | Content carried by an input or internal state. | 输入或内部状态里包含的内容。 |
| context | 上下文 | Earlier information that helps interpret the current item. | 前面发生过的内容，帮助理解现在的数据。 |
| sequence context | 序列上下文 | Context collected from previous items in a sequence. | 从序列前面内容中带到当前步骤的背景信息。 |
| hidden state | 隐藏状态 | Internal information carried from earlier steps into later steps. | 网络内部保存的、不会直接展示给用户的上下文记忆。 |
| state | 状态 | The internal information representing what the network has carried so far. | 网络到目前为止记住了什么的内部表示。 |
| state update | 状态更新 | Changing the hidden state after processing a new item. | 读入新数据后，重新调整内部记忆。 |
| carried context | 携带的上下文 | Context passed from earlier processing to the next step. | 从前面步骤带到下一步的上下文。 |
| carry information forward | 向前传递信息 | Passing useful information from earlier steps to later steps. | 把前面有用的信息继续传给后面。 |
| gating mechanism | 门控机制 | A mechanism that decides what information to keep or forget. | 像开关一样决定哪些信息保留、哪些信息丢掉。 |
| gate | 门 / 门控单元 | A learned control that regulates information flow. | 控制信息能不能通过的可学习“开关”。 |
| information gate | 信息门控 | A gate that controls the flow of information. | 控制信息进入、保留或离开的机制。 |
| retain information | 保留信息 | Keep useful information available for later steps. | 把有用的信息留下来供后面继续用。 |
| forget information | 忘记信息 | Remove or reduce information that is no longer useful. | 把不再有用的信息丢掉或减弱。 |
| keep information | 保留信息 | Choose to preserve a signal in the recurrent state. | 决定继续记住某个信号。 |
| keep-or-forget decision | 保留或遗忘决策 | The decision about which information should remain in state. | 决定哪些内容留下、哪些内容忘掉。 |
| useful information | 有用信息 | Information that helps later prediction or processing. | 对后续判断有帮助的内容。 |
| useful signal | 有用信号 | A meaningful part of the input that should be preserved. | 输入中值得保留、能帮助结果的信号。 |
| longer sequence | 更长序列 | A sequence with more ordered steps to remember across. | 需要跨越更多步骤才能处理完的一串数据。 |
| long-range information | 长距离信息 | Information whose source is many steps earlier in a sequence. | 来自很久以前步骤、但对现在仍可能有用的信息。 |
| longer-range information | 更长距离信息 | Information that must be carried over a larger sequence distance. | 需要在更长的范围内保持住的上下文。 |
| long-term information | 长期信息 | Information retained for later use across many steps. | 需要记住较久、以后还要用的信息。 |
| basic RNN | 基础 RNN | A simpler recurrent network without the LSTM-style gating design. | 比 LSTM 简单、没有这套门控机制的循环网络。 |
| vanilla RNN | 普通 RNN | A standard basic recurrent neural network. | 最基础、未特别改造的 RNN。 |
| standard RNN | 标准 RNN | Another name for a basic recurrent neural network. | basic RNN 的另一种说法。 |
| recurrent architecture | 循环架构 | An architecture that reuses a state while moving through a sequence. | 沿着序列前进时持续更新并复用状态的架构。 |
| LSTM architecture | LSTM 架构 | A recurrent architecture with gates for longer-range information. | 带门控、专门帮助处理较长上下文的循环架构。 |
| recurrent processing | 循环处理 | Processing that repeatedly updates state as sequence items arrive. | 每来一个数据就更新一次状态的处理方式。 |
| input | 输入 | Data supplied to a model or network. | 送进模型让它处理的内容。 |
| sequence input | 序列输入 | An input made of ordered items. | 由一项项有顺序的数据组成的输入。 |
| output | 输出 | The result produced by a model after processing input. | 模型处理输入后给出的结果。 |
| final output | 最终输出 | The result returned after the relevant sequence processing is complete. | 序列处理完成后最终返回的结果。 |
| prediction | 预测 | A result estimated from the current input and carried context. | 模型根据当前输入和上下文推测出的结果。 |
| predicted next word | 预测的下一个词 | A word selected as the likely continuation of earlier words. | 根据前面文字猜接下来最可能出现的词。 |
| next-word prediction | 下一词预测 | Predicting the next word in a word sequence. | 预测一句话下一个要出现的词。 |
| next token prediction | 下一个 token 预测 | Predicting the next token in a sequence. | 预测序列中下一个最小文本单位；这里是 next-word prediction 的相关说法。 |
| forecast | 预测 / 预报 | A prediction about a future value or event. | 根据过去数据估计未来会怎样。 |
| anomaly score | 异常分数 | A score indicating how unusual a sequence value or pattern is. | 表示某个数据或模式有多不寻常的分数。 |
| anomaly detection | 异常检测 | Finding unusual values or patterns in data. | 找出与平常规律明显不同的数据。 |
| label | 标签 / 类别标签 | A category or name assigned as an output. | 给输入判断出来的类别或名字。 |
| transcription | 转写结果 | Text produced from spoken or audio input. | 把声音内容转换成文字后的结果。 |
| signal estimate | 信号估计 | An estimated value or representation of a signal. | 对声音等信号的内容或数值作出的估计。 |
| model | 模型 | A learned system that turns inputs into outputs. | 学会一些规律、可以接收输入并给出结果的系统。 |
| network | 网络 | A connected computational model. | 由多个计算单元连接起来的模型。 |
| process | 处理 | Take input through computations to produce an updated state or output. | 对输入做计算并得到状态或结果。 |
| receive ordered data | 接收有序数据 | Take in sequence items in their defined order. | 按原本顺序接收一项项数据。 |
| read the first item | 读取第一项 | Process the first element of a sequence. | 先处理序列里的第一个数据。 |
| process the current item | 处理当前项 | Apply the network to the item at the current step. | 对当前这一步的数据做计算。 |
| carry context | 携带上下文 | Pass earlier information into the next step. | 把前面内容带到下一步。 |
| update the state | 更新状态 | Combine a new item with carried context to form a new state. | 把新数据和旧记忆合在一起，形成新的内部状态。 |
| continue | 继续处理 | Move to another sequence step after updating state. | 更新完状态后继续处理后面的数据。 |
| respond | 作出响应 | Produce a task result from the processed sequence. | 根据处理结果给出回应。 |
| first item | 第一项 | The first ordered element presented to the network. | 序列中最先到来的数据。 |
| next item | 下一项 | The item processed after the current item. | 当前数据之后要处理的那一项。 |
| earlier words | 前面的词 | Words that appeared before the current word. | 当前词之前已经读过的文字。 |
| whole sequence | 整个序列 | All ordered items considered together. | 一整串有顺序的数据。 |
| reread the whole sequence | 重新读取整个序列 | Read all earlier items again instead of carrying notes or state. | 每次都重新看完整段数据，而不是携带前面的记忆。 |
| notes from earlier words | 前面词语留下的笔记 | An analogy for context carried from earlier words. | 用“读句子时记笔记”来比喻隐藏状态和上下文。 |
| sentence | 句子 | An ordered sequence of words. | 由有顺序的词组成的一段话。 |
| word sequence | 词序列 | Words arranged in their original order. | 按原顺序排列的一串词。 |
| word | 词 / 单词 | One language item in a word sequence. | 句子里的一个词。 |
| time-series value | 时间序列值 | A measurement associated with a point in time. | 某个时间点上的测量数值。 |
| time series | 时间序列 | Measurements or observations arranged over time. | 按时间先后排列的一串测量数据。 |
| time-series processing | 时间序列处理 | Processing values as they arrive over time. | 按时间顺序逐个分析测量值。 |
| measurement over time | 随时间变化的测量值 | A value observed at successive times. | 在不同时间不断记录下来的数值。 |
| sound frame | 声音帧 | A short ordered slice of an audio signal. | 一小段按顺序切出来的声音数据。 |
| audio frame | 音频帧 | Another name for a short segment of audio processed in order. | 对声音进行分段后得到的一小块音频。 |
| audio sequence | 音频序列 | Ordered audio frames treated as a sequence. | 按时间排列的一串音频帧。 |
| speech | 语音 | Human spoken audio used in a sequence task. | 人说话产生的声音数据。 |
| speech task | 语音任务 | A task that processes spoken audio or its sequence. | 处理语音输入或语音序列的任务。 |
| sequence of sound frames | 声音帧序列 | Ordered sound frames arriving one after another. | 一帧接一帧按顺序到来的声音数据。 |
| earlier language model | 早期语言模型 | A language model from before Transformer-dominated large-scale systems. | Transformer 普及前常见的语言模型类型。 |
| language model | 语言模型 | A model that learns patterns in language sequences. | 学习文字顺序规律、用于理解或生成语言的模型。 |
| time-series model | 时间序列模型 | A model that learns or predicts patterns across time. | 专门分析随时间变化数据的模型。 |
| sequence model | 序列模型 | A model designed to use order and context in data. | 会利用数据顺序和前后关系的模型。 |
| real-world example | 现实世界示例 | A practical use case illustrating a model or process. | 用现实任务说明模型怎么用。 |
| speech and sequence task | 语音与序列任务 | A task using ordered audio or other sequential inputs. | 处理语音或其他有序数据的任务。 |
| pattern | 模式 / 规律 | A repeated or useful relationship in a sequence. | 数据里反复出现、能帮助预测的规律。 |
| track useful patterns | 跟踪有用模式 | Preserve patterns that matter across sequence frames. | 在连续数据中持续记住有用的变化规律。 |
| Transformer | Transformer 架构 / 变换器 | A sequence architecture that uses attention to relate positions. | 通过注意力机制联系序列不同位置的架构。 |
| Transformer architecture | Transformer 架构 | A model architecture based on attention rather than recurrent step-by-step state passing. | 主要用注意力关联各位置、不是靠循环传状态的架构。 |
| attention | 注意力机制 | A mechanism that relates or weighs positions in a sequence. | 让模型判断序列中哪些位置更值得关注。 |
| sequence position | 序列位置 | One location in an ordered sequence. | 一串数据中的某个位置。 |
| positions in a sequence | 序列中的各个位置 | The locations that attention can relate to one another. | 序列里每个数据项所在的位置。 |
| attention-based processing | 基于注意力的处理 | Processing that directly relates sequence positions using attention. | 用注意力把不同位置联系起来的处理方式。 |
| large-scale language task | 大规模语言任务 | A language task involving large datasets or models. | 数据量、模型规模都较大的语言处理任务。 |
| historical importance | 历史重要性 | Importance of a method as part of the development of a field. | 某种方法在技术发展历史中的价值。 |
| mathematical mechanism | 数学机制 | A formal computational mechanism rather than a human process. | 由数学计算实现的机制，不是人的真实记忆。 |
| human memory | 人类记忆 | Biological and cognitive memory in people. | 人的大脑通过生物和认知过程形成的记忆。 |
| biological process | 生物过程 | A process occurring in a living organism. | 生物体内发生的过程。 |
| cognitive process | 认知过程 | A mental process involved in human thought and memory. | 人进行思考、理解和记忆的心理过程。 |
| signal | 信号 | A meaningful changing value carried by data such as audio. | 数据中随时间变化、承载信息的内容。 |
| signal processing | 信号处理 | Working with signals such as audio over ordered frames. | 对声音等信号进行分析、变换或估计。 |
| final response | 最终响应 | A response produced after the model uses updated state. | 模型处理后给出的最后回答或结果。 |
| related concept | 相关概念 | A concept connected to the topic for further learning. | 和当前主题有关系、可以继续学习的概念。 |
| Deep Learning | 深度学习 | A machine-learning approach commonly built from neural networks. | 使用多层神经网络进行学习的一类机器学习方法。 |
| Neural Networks | 神经网络 | The broader family that includes recurrent networks. | RNN、LSTM 等都属于神经网络这个大类。 |
| model architecture family | 模型架构家族 | A group of related architectures such as RNNs, LSTMs, and Transformers. | 结构思路相近的一组模型架构。 |
| processing step | 处理步骤 | One unit of work in the sequence-processing flow. | 序列流程中的一步计算。 |
| flow | 流程 | The ordered path from input through state updates to output. | 从接收数据到更新状态、最后输出的过程。 |
| input-output mapping | 输入输出映射 | The relationship by which a model turns input into output. | 模型把什么输入变成什么结果的关系。 |
| current state | 当前状态 | The hidden state after the items processed so far. | 处理到当前为止形成的内部记忆。 |
| previous context | 先前上下文 | Context originating from earlier sequence steps. | 来自前面步骤的背景信息。 |
| later step | 后续步骤 | A sequence step that occurs after an earlier step. | 在前面步骤之后发生的处理时刻。 |
| sequence prediction | 序列预测 | Predicting an output using ordered inputs and context. | 根据一串有顺序的数据预测结果。 |
| recurrent model | 循环模型 | A model that reuses an evolving state across sequence steps. | 在序列步骤间反复传递和更新状态的模型。 |
| long-range dependency | 长距离依赖 | A relationship between items separated by many sequence steps. | 当前结果依赖很久以前数据的关系。 |
| temporal dependency | 时间依赖 | A relationship between values at different times. | 不同时间的数据之间存在的依赖关系。 |
| sequence memory | 序列记忆 | Internal retained information from earlier sequence items. | 网络对前面序列内容留下的内部记忆。 |

## Potential Missing Concepts

- Vanilla RNN / simple recurrent unit: the page says “basic RNN” but does not explain its recurrence equation or parameter sharing.
- GRU (Gated Recurrent Unit): a related gated recurrent architecture that is not covered.
- Cell state: the separate long-lived memory path commonly used to explain LSTM internals.
- Forget gate, input gate, and output gate: the page mentions gating and keep/forget decisions but does not name the usual LSTM gates individually.
- Candidate cell state / candidate memory: the temporary content considered for writing into an LSTM cell state.
- Recurrent update equation: the mathematical rule that combines the current input and previous hidden state.
- Backpropagation Through Time (BPTT): the usual training algorithm for recurrent networks.
- Vanishing gradient: a training difficulty in which gradients become too small across many steps.
- Exploding gradient: a training difficulty in which gradients become too large across many steps.
- Long-term dependency: the page discusses longer-range information but does not give the standard dependency term explicitly in the main explanation.
- Bidirectional RNN / bidirectional LSTM: recurrent processing that reads a sequence in both directions.
- Many-to-one, one-to-many, and many-to-many sequence mappings: common input-output shapes for recurrent models.
- Sequence-to-sequence model: an encoder-decoder sequence architecture not described on this page.
- Teacher forcing: a recurrent-model training technique not covered.
- Autoregressive generation: using previous outputs as later inputs, relevant to next-word prediction but not named.
- Padding and masking: practical handling of sequences with different lengths, not covered.
- Sequence length: the number of ordered steps in an input, not formally defined.
- Batch processing: grouping multiple sequences for training or inference, not discussed.
- Training: the page explains processing and prediction but does not describe how RNN/LSTM parameters are learned.
- Inference: applying a trained recurrent model to new sequence data is implied but not named.
- Hidden-to-hidden transition: the recurrent connection carrying state from one step to the next.
- Parameter sharing across time: the same recurrent parameters are reused at each sequence step, not explained.
- Attention over recurrent states: attention can be combined with RNN/LSTM models, but the page only contrasts Transformer attention with recurrence.
- CTC (Connectionist Temporal Classification): a common speech-sequence objective not covered.
- Perplexity: a common language-model metric not covered.
- Forecast horizon: how far ahead a time-series model predicts, not covered.
- Online / streaming inference: processing values as they arrive in real time, suggested by the examples but not named.
- Sequence truncation: limiting how many earlier steps are retained during training, not covered.
- Memory cell: another common name for the LSTM's persistent memory component.

## Aliases / Synonyms

- RNN = Recurrent Neural Network = recurrent neural network = recurrent network.
- LSTM = Long Short-Term Memory = LSTM network = LSTM architecture.
- Basic RNN = vanilla RNN = standard RNN = simple recurrent network.
- Recurrent architecture = recurrent-network architecture = recurrent neural network architecture.
- Hidden state = recurrent state = carried context = sequence memory (related usage, not always mathematically identical).
- Context = sequence context = previous context = notes from earlier words (analogy).
- State update = update the state = recurrent update.
- Gating mechanism = gate = information gate = keep-or-forget control.
- Retain information = keep information = carry useful information forward.
- Forget information = discard information = reduce stale information.
- Long-range information = longer-range information = long-term information = long-term dependency (related terms).
- Sequence = ordered data = sequence data = ordered input.
- Time series = time-series data = measurements over time.
- Sound frame = audio frame = short audio segment.
- Speech and sequence task = speech sequence task = ordered-audio task.
- Prediction = forecast = estimated output (forecast is especially used for future values).
- Anomaly score = anomaly-detection score = unusualness score.
- Signal estimate = signal prediction = estimated signal.
- Next-word prediction = predicted next word = next-token prediction (the latter is the broader token-level formulation).
- Transformer = Transformer architecture = attention-based sequence architecture.
- Neural Networks = neural network family = neural-network models.
- LSTM's mathematical mechanism ≠ human memory, even though both can be described with memory language.

## Do Not Confuse Candidates

- RNN vs. LSTM: RNN is the broader recurrent-network family; LSTM is one recurrent architecture with gating mechanisms for longer-range information.
- RNN vs. basic RNN: RNN can refer to the family in general; “basic RNN” means the simpler member without LSTM-style gates.
- LSTM vs. long-term human memory: LSTM is a mathematical mechanism for retaining signals; human memory is a biological and cognitive process.
- RNN vs. Transformer: RNN processes a sequence recurrently, step by step; Transformer uses attention to relate sequence positions.
- Hidden state vs. human memory: hidden state is a numerical internal representation, not conscious or biological memory.
- Hidden state vs. cell state: the page only names hidden state; in standard LSTM terminology, cell state is a distinct persistent memory path.
- Context vs. entire input: context is the useful carried information from earlier items, not necessarily a verbatim copy of the whole sequence.
- Retain vs. remember: retaining information is a learned numerical operation, not literal remembering.
- Forget vs. delete: an LSTM gate reduces or removes a signal from its internal state; it is not deleting a human memory or source record.
- Sequence vs. set: sequence order matters; a set does not normally carry the same ordered-step meaning.
- Time-series value vs. forecast: a time-series value is an observed input; a forecast is an estimated future output.
- Anomaly score vs. anomaly label: a score expresses how unusual something is; a label is a categorical output.
- Sound frame vs. complete recording: a frame is a short slice of audio, while a recording may contain many frames.
- Transcription vs. signal estimate: transcription is usually a language/text result; a signal estimate is a numerical or signal-level estimate.
- Prediction vs. final output: prediction is one kind of output; final output is the broader result returned by the system.
- Next-word prediction vs. speech transcription: next-word prediction continues text; transcription converts audio into text.
- Attention vs. gating: attention selects or weighs positions in a sequence; gating controls what recurrent information is kept or forgotten.
- Recurrent processing vs. rereading the whole sequence: recurrence carries state forward instead of reprocessing all previous items at every step.
- Earlier language model vs. current Transformer-dominated language model: RNNs were important in earlier language-model systems, while Transformers now dominate many large-scale language tasks.
- Sequence model vs. sequence data: a sequence model is the processing system; sequence data is the ordered information it receives.

## Notes

- The source is a beginner-friendly topic page titled “What are RNNs and LSTMs?” under Module 02, “Neural Networks & Model Architectures,” Topic 04.
- The core source definition is that RNNs and LSTMs process sequences step by step, carrying information from earlier steps into later processing.
- The process flow explicitly contains: receive ordered data → read the first item → carry context in a hidden state → update the state with the next item → continue or produce an output.
- The source's LSTM explanation centers on gating mechanisms that help decide what information to keep or forget; it does not name the standard individual gates.
- Examples explicitly cover earlier language models, time-series processing, and speech / sequence tasks.
- The page says Transformers now dominate many large-scale language tasks, while RNNs remain historically important and can still be useful for some sequence problems.
- The source includes links to Neural Networks, Deep Learning, and Transformer as related concepts.
- The page contains a “Video” section, but states that no video asset is available; no additional glossary terms were extracted from a video.
- Candidates are intentionally broad and may overlap or repeat through exact phrases, aliases, and related wording; this raw file is not a deduplicated final glossary.
