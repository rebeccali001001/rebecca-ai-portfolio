# Topic

KV Cache

## Module/Topic/Source File

- Module: 03 · Tokens, Context & Inference
- Topic: 05 · KV Cache
- Source File: `kv-cache.html`

## Glossary Candidates

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| KV Cache | KV 缓存；键值缓存 | Temporary memory that stores attention states for reuse during generation. | 生成文字时暂时保存注意力信息、避免反复重算的记忆区。 |
| key-value cache | 键值缓存 | Another name for a cache of key and value states. | 保存 key 和 value 状态的缓存。 |
| KV | K/V；键和值 | Short form referring to attention keys and values. | key（键）和 value（值）的缩写。 |
| K | K；键 | Short form for the key state used by attention. | 注意力机制里用来匹配相关信息的“键”状态。 |
| V | V；值 | Short form for the value state used by attention. | 注意力机制里真正被取用、汇总的信息“值”状态。 |
| cache | 缓存 | Stored information kept so later computation can reuse it. | 先存起来、以后直接重复使用的信息。 |
| temporary memory | 临时内存 | Memory used for a limited runtime period rather than permanent storage. | 只在一段运行期间使用、不会永久保存的内存。 |
| runtime memory | 运行时内存 | Memory allocated while a model or program is running. | 模型运行时临时占用的内存。 |
| runtime data | 运行时数据 | Data created or held while an inference request is active. | 一次推理请求运行期间产生或保存的数据。 |
| temporary runtime data | 临时运行时数据 | Runtime data retained only for an active computation. | 只为当前运行过程暂时保留的数据。 |
| request-specific state | 请求特定状态 | State belonging to one particular request or generation. | 只属于某一个请求或生成过程的内部信息。 |
| active generation | 当前生成过程 | The ongoing process of producing output tokens. | 模型正在逐步生成答案的过程。 |
| generation | 生成 | Producing a sequence of output tokens from a model. | 模型一个词元一个词元地产生输出。 |
| text generation | 文本生成 | Producing text by repeatedly predicting tokens. | 模型连续预测并写出文字。 |
| inference | 推理 | Using a trained model to compute outputs for an input. | 使用已经训练好的模型得到结果。 |
| inference runtime | 推理运行时 | The software environment that executes model inference. | 负责让模型进行推理计算的软件运行环境。 |
| attention information | 注意力信息 | Information produced by attention about how tokens relate. | 注意力机制计算出的词元之间的关联信息。 |
| attention state | 注意力状态 | An internal representation used by attention computation. | 注意力计算过程中保存下来的内部表示。 |
| attention states | 注意力状态（复数） | The collection of attention representations for tokens in a sequence. | 一串词元对应的一组注意力内部信息。 |
| earlier token | 较早的词元；前面词元 | A token that appeared earlier in the sequence. | 已经出现在前文里的词元。 |
| earlier tokens | 较早的词元（复数） | Previously processed tokens that precede the newest token. | 新词元之前已经处理过的那些词元。 |
| previous token | 前一个词元 | A token available before the current generation step. | 当前生成步骤之前已经出现的词元。 |
| new token | 新词元 | The token added at the current generation step. | 模型这一步刚生成或刚加入序列的词元。 |
| next token | 下一个词元 | The token generated immediately after the current context. | 接在当前上下文后面生成的下一个小文字单位。 |
| token | 词元；标记 | A small unit of text processed by a language model. | 语言模型处理文字时使用的小单位。 |
| text token | 文本词元 | A token representing part of written text. | 文字被切分后形成的一小段。 |
| token sequence | 词元序列 | An ordered series of tokens. | 按前后顺序排列的一串词元。 |
| sequence | 序列 | An ordered collection of tokens or states. | 按顺序排列的数据集合。 |
| context | 上下文 | Information available to the model when producing the next token. | 模型生成下一部分时可以参考的前文信息。 |
| earlier context | 先前上下文 | Context that has already been processed before the current step. | 当前生成步骤之前已经看过的上下文。 |
| prompt | 提示词；输入提示 | The input text or instruction given to the model. | 用户交给模型的输入文字或指令。 |
| prompt context | 提示上下文 | The context supplied by the prompt before generation begins. | 开始生成前由提示词提供的前文。 |
| long context | 长上下文 | A context containing many tokens or a large amount of information. | 包含很多文字、很长的前文范围。 |
| long document | 长文档 | A document whose many tokens create substantial context. | 文字很多、模型需要处理很长前文的文档。 |
| one generation | 一次生成 | One continuous model output process. | 从一次请求开始到答案生成完的一段过程。 |
| one active generation | 一次当前生成 | The single generation whose intermediate states are being reused. | 当前这一条答案生成过程中反复使用的状态。 |
| separate request | 独立请求 | A different inference request outside the current generation. | 与当前生成分开的另一条请求。 |
| reuse | 重用；复用 | Using already computed information again. | 已经算过的信息再拿来使用。 |
| reuse attention information | 复用注意力信息 | Reusing earlier attention results instead of calculating them again. | 以前算出的注意力结果直接再用。 |
| reuse earlier context | 复用先前上下文 | Using processed prior context for a later generation step. | 后面生成时继续使用已经处理过的前文。 |
| computation reuse | 计算复用 | Avoiding repeated computation by reusing prior results. | 不重复计算，直接使用已有结果。 |
| avoid recomputation | 避免重新计算 | Not calculating the same earlier information again. | 不把相同的前文重新算一遍。 |
| repeated computation | 重复计算 | Recalculating information that was already computed. | 同一份信息被反复计算。 |
| repeated work | 重复工作 | Extra computation caused by doing prior work again. | 因为重做以前的计算而增加的工作量。 |
| same earlier context | 相同的先前上下文 | The prior context that would otherwise be processed repeatedly. | 每一步都可能重复处理的那部分旧前文。 |
| attention computation | 注意力计算 | Computing how tokens use information from one another. | 计算每个词元应该参考哪些其他词元。 |
| Transformer | Transformer；变换器 | A neural-network architecture that uses attention for sequence processing. | 现代语言模型常用、包含注意力机制的神经网络结构。 |
| Transformer model | Transformer 模型 | A model built with the Transformer architecture. | 使用 Transformer 结构搭建的模型。 |
| Transformer attention | Transformer 注意力 | The attention mechanism inside a Transformer. | Transformer 中负责关联前文信息的机制。 |
| attention | 注意力机制 | A mechanism that weighs relevant parts of the input. | 模型判断哪些前文更重要、应重点参考的机制。 |
| self-attention | 自注意力 | Attention in which tokens relate to other tokens in the same sequence. | 同一句子中的词元互相参考的注意力机制。 |
| key state | 键状态 | An attention representation used to match a query with relevant token information. | 帮模型寻找哪些前文相关的内部信息。 |
| key states | 键状态（复数） | Key representations computed for the sequence. | 一串词元对应的 key 内部表示。 |
| value state | 值状态 | An attention representation containing information that can be retrieved. | 注意力找到相关内容后实际取用的信息表示。 |
| value states | 值状态（复数） | Value representations computed for the sequence. | 一串词元对应的 value 内部表示。 |
| key and value states | 键和值状态 | The pair of attention states stored for reuse. | KV cache 中一起保存的两类注意力状态。 |
| key/value states | 键/值状态 | Alternate notation for key and value states. | key 状态和 value 状态的另一种写法。 |
| computed attention information | 已计算的注意力信息 | Attention results already produced for a sequence. | 模型之前已经算好的注意力内部信息。 |
| attention representation | 注意力表示 | An internal numerical representation used by attention. | 注意力用数字形式表达的一类内部信息。 |
| internal representation | 内部表示 | A numerical form used inside the model to encode information. | 模型内部用来表示信息的数字结构。 |
| state | 状态 | Information describing the model's intermediate computation. | 模型计算到某一步时保留下来的内部信息。 |
| intermediate state | 中间状态 | A state produced between input processing and final output. | 从输入到输出之间某一步产生的内部信息。 |
| stored state | 已存状态 | A computed state retained for later use. | 已经计算并暂时保存、稍后还会用的信息。 |
| cached state | 缓存状态 | A state held in a cache for reuse. | 放在缓存里、以后直接复用的状态。 |
| state reuse | 状态复用 | Reusing an intermediate state in later computation. | 后续计算继续使用之前保存的内部状态。 |
| store | 存储 | To keep computed information for later computation. | 把算好的信息保留下来。 |
| storing key and value states | 存储键和值状态 | Keeping key and value representations in the KV cache. | 把 key、value 两种状态放进缓存。 |
| keep the states | 保留状态 | Retain computed attention states rather than discarding them. | 算好后不丢掉这些内部信息。 |
| stored attention information | 已存注意力信息 | Attention information kept for future generation steps. | 为后续生成保留的注意力信息。 |
| cache entry | 缓存条目 | One stored item or group of stored states in a cache. | 缓存中保存的一项信息。 |
| cache contents | 缓存内容 | The states currently held in the KV cache. | KV cache 当前装着的内部状态。 |
| cache growth | 缓存增长 | The increase in cached state as more tokens are processed. | 处理的词元越多，缓存里的状态越多。 |
| grows as the sequence grows | 随序列增长而增长 | The cache becomes larger when the token sequence becomes longer. | 前文变长时，缓存也跟着变大。 |
| sequence length | 序列长度 | The number of tokens in a sequence. | 一串文字里包含多少个词元。 |
| growing sequence | 增长中的序列 | A token sequence that receives additional tokens over time. | 不断加入新词元、越来越长的序列。 |
| memory use | 内存使用量 | The amount of memory occupied by a computation or cache. | 运行时占用了多少内存。 |
| memory consumption | 内存消耗 | Memory required to hold data during computation. | 为保存和计算数据所需要的内存。 |
| memory overhead | 内存开销 | Additional memory required by a mechanism such as a cache. | 为了使用缓存额外付出的内存成本。 |
| memory trade-off | 内存权衡 | A trade-off between lower repeated computation and higher memory use. | 用更多内存换取更少重复计算的取舍。 |
| efficiency | 效率 | Doing useful computation with less unnecessary work or resources. | 用较少资源完成更多有效工作。 |
| generation efficiency | 生成效率 | How efficiently a model produces output tokens. | 模型生成答案时做事有多快、多省资源。 |
| computational efficiency | 计算效率 | How much useful computation is obtained for the resources used. | 同样算力下完成有效计算的能力。 |
| faster generation | 更快生成 | Producing output with less repeated computation. | 因为少重算而更快地产生文字。 |
| faster next-token generation | 更快的下一个词元生成 | Producing each next token more efficiently during decoding. | 每一步更省计算地生成下一个词元。 |
| lower repeated work | 更低的重复工作量 | Less work spent repeating earlier computation. | 重新做旧计算的工作更少。 |
| lower repeated computation | 更低的重复计算量 | Less recomputation of prior attention information. | 不必反复计算以前的注意力信息。 |
| computational saving | 计算节省 | Computation avoided through reuse. | 因为复用已有结果而省下的计算。 |
| resource efficiency | 资源效率 | Using compute and memory effectively during runtime. | 更合理地使用计算资源和内存。 |
| latency | 延迟 | The time between a request and a generated result or token. | 从发出请求到看到结果所等待的时间。 |
| generation latency | 生成延迟 | The time needed to produce output during generation. | 模型生成答案时花费的等待时间。 |
| time per token | 每词元耗时 | The time required to generate or process one token. | 生成一个词元平均要花多少时间。 |
| throughput | 吞吐量 | The amount of processing completed per unit of time. | 单位时间能处理多少工作或词元。 |
| tokens per second | 每秒词元数 | The number of tokens generated or processed each second. | 一秒钟生成或处理多少个词元。 |
| performance | 性能 | How quickly and efficiently the system performs its work. | 系统完成任务的速度和资源表现。 |
| runtime performance | 运行时性能 | Performance while the model is serving an active request. | 模型实际运行、处理请求时的表现。 |
| decode | 解码；生成解码 | The autoregressive stage that produces output tokens one by one. | 模型逐个生成答案词元的阶段。 |
| decoding | 解码过程 | Repeatedly selecting and producing the next token. | 反复选择并生成下一个词元的过程。 |
| autoregressive generation | 自回归生成 | Generating each token from tokens already available. | 生成一个词元后，把它加入前文再生成下一个。 |
| generation step | 生成步骤 | One iteration that produces or adds a token. | 生成一个新词元的一轮计算。 |
| inference step | 推理步骤 | One stage of computation during inference. | 模型推理过程中进行的一步计算。 |
| decode step | 解码步骤 | One token-generation iteration during decoding. | 解码时生成一个词元的一步。 |
| process the prompt | 处理提示词 | Run the input prompt through the model. | 先让模型读入并计算用户给的提示词。 |
| process earlier tokens | 处理较早词元 | Compute representations for tokens already in the context. | 计算前文中已经存在的那些词元。 |
| receive the context | 接收上下文 | Take in the prompt and earlier tokens as model input. | 模型读入提示词和已有前文。 |
| read | 读取；读入 | The first process stage in which the model receives context. | 流程中先把上下文读进模型。 |
| build | 构建 | Compute the states needed for caching. | 算出并准备好要放入缓存的状态。 |
| create key and value states | 创建键和值状态 | Compute key and value representations for the sequence. | 为序列计算出 key 和 value 两种状态。 |
| compute | 计算 | Produce a numerical result from the model's operations. | 通过模型运算得到数字结果。 |
| attention information is computed | 计算注意力信息 | The model calculates attention-related states for the sequence. | 模型为整段序列算出注意力信息。 |
| store | 存储 | Put the computed states into the KV cache. | 把计算结果放到 KV cache 中。 |
| keep the states | 保留状态 | Retain the computed key and value states. | 把算好的状态留下来备用。 |
| runtime stores them | 运行时保存它们 | The inference runtime keeps the attention states. | 推理程序负责暂时保存这些状态。 |
| generate | 生成 | Produce the next token using available context and states. | 利用上下文和已有状态生成下一个词元。 |
| add the next token | 加入下一个词元 | Append the newly generated token to the sequence. | 把刚生成的词元接到序列末尾。 |
| use cached earlier states | 使用缓存的早期状态 | Use stored states for earlier tokens in a later step. | 后续计算直接用前面已经缓存的状态。 |
| update | 更新 | Change the cache to include newly computed information. | 把新产生的信息加入并刷新缓存。 |
| extend the cache | 扩展缓存 | Add new states to an existing KV cache. | 让缓存随着新词元加入而变长。 |
| new key and value states | 新的键和值状态 | Key and value states computed for the newly added token. | 新词元产生的两种新注意力状态。 |
| join the cache | 加入缓存 | Become part of the existing cached state sequence. | 新状态接到原来的缓存后面。 |
| cache update | 缓存更新 | The operation of adding new states to the cache. | 把新状态加入缓存的动作。 |
| incremental generation | 增量生成 | Generation that extends an existing sequence step by step. | 在已有前文上一次次追加新词元。 |
| incremental decoding | 增量解码 | Decoding that reuses prior states while adding one token at a time. | 每次加一个词元、同时复用旧状态的解码。 |
| prefill | 预填充 | The initial pass that processes the prompt and populates the cache. | 先一次性读入提示词并把缓存准备好的阶段。 |
| prefill phase | 预填充阶段 | The initial context-processing phase before token-by-token decoding. | 逐词元生成前先处理整段输入的阶段。 |
| decode phase | 解码阶段 | The phase that generates output tokens after prefill. | 缓存准备好后逐个生成输出词元的阶段。 |
| prompt processing | 提示词处理 | The initial computation over the input context. | 对用户输入的整段提示词做初始计算。 |
| token-by-token generation | 逐词元生成 | Producing output one token at a time. | 每次生成一个小文字单位。 |
| one token at a time | 一次一个词元 | A generation pattern that adds tokens sequentially. | 不一次写完整答案，而是逐个加入词元。 |
| continuation | 续写；延续 | Output generated after the existing context. | 接着已有前文继续生成的内容。 |
| ongoing generation | 持续生成 | Generation that continues across multiple output steps. | 模型不断生成后续词元的过程。 |
| streaming answer | 流式答案 | An answer delivered progressively as it is generated. | 答案一边生成一边逐段显示出来。 |
| streaming generation | 流式生成 | Generating and delivering output progressively. | 模型生成一点就逐步发送一点。 |
| long response | 长回答 | A response containing many generated tokens. | 包含很多词元、需要持续生成的答案。 |
| long chat | 长对话 | A conversation whose accumulated context contains many tokens. | 来回消息很多、前文越来越长的对话。 |
| conversation | 对话 | A sequence of user and model messages used as context. | 用户和模型连续交流形成的消息记录。 |
| growing conversation | 不断增长的对话 | A chat whose context expands with each new message. | 随着消息增加而变长的聊天记录。 |
| input | 输入 | Information supplied to a model. | 送进模型的信息。 |
| output | 输出 | Information produced by a model. | 模型计算后返回的结果。 |
| system | 系统 | The model-serving runtime or system carrying out the operation. | 负责运行模型并处理请求的系统。 |
| runtime | 运行时 | The software environment executing the model. | 模型实际运行的程序环境。 |
| model processes the prompt | 模型处理提示词 | The model computes representations for the supplied prompt. | 模型先读懂并计算输入的提示词。 |
| system reuses earlier attention states | 系统复用较早注意力状态 | The serving system uses cached attention states from prior steps. | 系统继续使用之前保存的注意力信息。 |
| system updates the cache | 系统更新缓存 | The runtime adds new states as tokens are generated. | 每生成新词元，系统就把新状态加进缓存。 |
| less repeated computation | 更少重复计算 | A reduction in recomputing earlier context at each step. | 每生成一步都少重新计算一些旧前文。 |
| continued generation | 持续生成 | Generation that proceeds using the updated cache. | 依靠不断更新的缓存继续写答案。 |
| model | 模型 | A learned system that transforms input into output. | 从数据中学会规律并处理输入的系统。 |
| model parameters | 模型参数 | Learned values that are part of the model itself. | 训练后固定在模型里的学习结果。 |
| parameter | 参数 | A learned numerical value used by the model. | 模型内部影响计算结果的数字。 |
| learned value | 学到的值 | A value adjusted during model training. | 训练过程中学出来的数字。 |
| model weights | 模型权重 | Learned numerical parameters controlling model behavior. | 模型通过训练学到、决定行为的数字。 |
| context window | 上下文窗口 | The maximum amount of information a model can work with at once. | 模型一次最多能看到和处理的前文范围。 |
| long-term memory | 长期记忆 | Information stored for later use across interactions or sessions. | 能跨请求、跨交流长期保存的信息。 |
| permanent memory | 永久记忆 | Memory intended to persist beyond one runtime or request. | 不会随着当前请求结束而消失的存储。 |
| cross-request memory | 跨请求记忆 | Information reused by separate requests. | 不同请求之间也可以继续使用的记忆。 |
| persistent storage | 持久化存储 | Storage that survives after the current computation ends. | 当前运行结束后仍然保留的数据存储。 |
| faster next-token generation | 更快的下一个词元生成 | Faster production of the next token because prior states are reused. | 通过复用旧状态更快生成下一词元。 |
| generation cost | 生成成本 | Compute, memory, time, or money required to generate output. | 生成答案需要付出的算力、内存和时间。 |
| memory cost | 内存成本 | The memory required to maintain cached states. | 为了保存缓存状态而占用的内存代价。 |
| compute cost | 计算成本 | The amount of computation needed for generation. | 生成过程中需要消耗的计算量。 |
| scalability | 可扩展性 | The ability to handle longer sequences or more requests as demand grows. | 规模变大时系统还能否继续稳定工作。 |
| batch | 批次 | A group of requests processed together by a runtime. | 系统一次成组处理的多条请求。 |
| batch size | 批大小 | The number of requests or sequences processed together. | 一批同时处理多少条请求或序列。 |
| concurrent request | 并发请求 | A request processed at the same time as others. | 和其他请求同时运行的一条请求。 |
| serving | 服务；在线推理服务 | Running a model so applications can send requests and receive outputs. | 把模型放在系统里供应用调用。 |
| model serving | 模型服务 | The infrastructure and process for serving model inference. | 负责接收请求、运行模型、返回结果的系统。 |
| inference request | 推理请求 | A request asking a model to produce an output. | 请模型根据输入生成结果的一次调用。 |
| active request | 当前请求 | A request that is currently being processed. | 系统此刻正在处理的请求。 |
| request lifetime | 请求生命周期 | The period from request start until its generation ends. | 一条请求从开始到完成的整个时间段。 |
| attention reuse | 注意力复用 | Reusing previously calculated attention-related states. | 不重算而重复使用旧的注意力状态。 |
| key-value state reuse | 键值状态复用 | Reusing cached key and value states in later decoding steps. | 后续解码时继续使用缓存的 key/value。 |
| cache mechanism | 缓存机制 | The method of storing and reusing intermediate states. | 保存中间结果并在后续计算中复用的方法。 |
| caching mechanism | 缓存机制；缓存方法 | A mechanism that trades memory for less recomputation. | 用额外内存换取少重复计算的办法。 |
| reuse during one generation | 单次生成中的复用 | Reuse of states within one continuous generation. | 只在同一条答案生成期间复用状态。 |
| generation-local reuse | 生成内复用 | Reuse limited to one generation sequence. | 复用范围只限当前这一条生成序列。 |
| context reuse | 上下文复用 | Reusing processed context information in later steps. | 后面继续利用已经处理过的上下文。 |
| prefix reuse | 前缀复用 | Reusing states for a shared initial context or prefix. | 多次计算中复用相同开头前文的状态。 |
| prefix cache | 前缀缓存 | A cache holding reusable states for a shared prefix. | 专门保存共同前缀计算结果的缓存。 |
| cache eviction | 缓存驱逐；缓存淘汰 | Removing cached states to manage limited memory. | 内存不够时删掉一部分缓存内容。 |
| cache management | 缓存管理 | Allocating, updating, sharing, or removing cached states. | 负责安排、更新和清理缓存的工作。 |
| cache capacity | 缓存容量 | The amount of cached state that can be held. | 缓存最多能装多少状态。 |
| cache size | 缓存大小 | The amount of memory or state currently occupied by the cache. | 当前缓存占了多少空间。 |
| memory bandwidth | 内存带宽 | The rate at which data can be read from or written to memory. | 内存每秒能搬运多少数据。 |
| GPU memory | GPU 内存 | Memory on the accelerator used for model computation and cache. | 显卡或加速器上保存模型与缓存的内存。 |
| VRAM | 显存 | Video random-access memory used by a GPU. | GPU 用来存模型和运行数据的内存。 |
| accelerator memory | 加速器内存 | Memory on a device such as a GPU used during inference. | GPU 等计算加速设备上的运行内存。 |
| memory-bound | 受内存限制的 | Limited mainly by memory capacity or data movement rather than arithmetic. | 速度主要卡在内存容量或搬运数据上。 |
| compute-bound | 受计算限制的 | Limited mainly by arithmetic computation capacity. | 速度主要卡在计算能力上。 |
| attention layer | 注意力层 | A neural-network layer that computes attention. | 神经网络中进行注意力计算的一层。 |
| Transformer layer | Transformer 层 | One repeated transformation block in a Transformer. | Transformer 中反复堆叠的一层处理模块。 |
| layer-wise cache | 分层缓存 | Cached key and value states maintained for each model layer. | 为模型每一层分别保存的 KV 状态。 |
| hidden state | 隐藏状态 | An internal numerical representation produced by a neural model. | 模型内部不会直接显示的数字表示。 |
| query | 查询；Q | The attention vector used to look for relevant keys. | 用来查询哪些前文相关的注意力向量。 |
| QKV | QKV；查询、键和值 | The query, key, and value components used in attention. | 注意力里的 query、key、value 三类向量。 |
| query-key matching | 查询键匹配 | Comparing a query with keys to determine relevance. | 把当前查询和前文 key 比较来找相关内容。 |
| attention score | 注意力分数 | A numerical relevance score between tokens in attention. | 表示某个前文有多值得参考的分数。 |
| attention weights | 注意力权重 | Weights assigned to values after attention scoring. | 决定不同前文信息被取用多少的权重。 |
| causal attention | 因果注意力 | Attention that lets a token use earlier positions but not future ones. | 生成时只能看前文、不能偷看后文的注意力。 |
| causal mask | 因果掩码 | A mask that prevents attention to future tokens. | 防止模型看到未来词元的限制。 |
| token position | 词元位置 | The place of a token within a sequence. | 一个词元在整串文字中的位置。 |
| positional information | 位置信息 | Information indicating the order of tokens. | 告诉模型词元先后顺序的信息。 |
| sequence representation | 序列表征 | Internal representations for the tokens in a sequence. | 模型内部对一整串词元的数字表达。 |
| matrix | 矩阵 | A rectangular arrangement of numbers used in model computation. | 按行列排列、供模型计算的数字表。 |
| key matrix | 键矩阵 | A matrix containing key representations for sequence positions. | 把各位置 key 状态排在一起的数字矩阵。 |
| value matrix | 值矩阵 | A matrix containing value representations for sequence positions. | 把各位置 value 状态排在一起的数字矩阵。 |
| tensor | 张量 | A multidimensional array used to store model data. | 可以有多维的数字数组，模型常用来存状态。 |
| cache tensor | 缓存张量 | A tensor storing cached key or value states. | 用来保存 KV 状态的多维数字数组。 |
| key/value tensor | 键/值张量 | Tensor data containing key or value representations. | 保存 key 或 value 数字表示的张量。 |
| memory footprint | 内存占用 | The total amount of memory used by a model or data structure. | 模型或缓存总共占用的内存大小。 |
| context-length scaling | 随上下文长度扩展 | The way memory or compute changes as context length grows. | 前文变长时内存和计算量如何跟着变化。 |
| quadratic attention cost | 二次注意力成本 | Attention work that can grow roughly with the square of sequence length. | 序列变长时，某些注意力计算会增长得很快。 |
| decoding cost | 解码成本 | Runtime work needed to generate output tokens. | 逐个生成输出词元所需的计算和内存代价。 |
| prefill cost | 预填充成本 | Work needed to process the prompt and build the initial cache. | 初次读入提示词并建立缓存所需的代价。 |
| time to first token | 首词元时间 | Time from request start until the first output token appears. | 从请求发出到第一个输出词元出现要等多久。 |
| inter-token latency | 词元间延迟 | Time between successive generated tokens. | 连续两个输出词元之间的等待时间。 |
| first-token latency | 首词元延迟 | Latency before the first generated token. | 看到第一个生成词元前的等待时间。 |
| token generation rate | 词元生成速率 | The rate at which output tokens are produced. | 模型每秒或每单位时间生成多少词元。 |
| request latency | 请求延迟 | Time taken to complete or begin serving an inference request. | 一条请求从发出到得到服务结果的耗时。 |
| memory utilization | 内存利用率 | The fraction of available memory occupied by runtime data. | 可用内存中已经被使用了多少。 |
| cache hit | 缓存命中 | Finding the needed prior state in the cache. | 需要的信息刚好已经在缓存里。 |
| cache miss | 缓存未命中 | The needed state is not available in the cache. | 需要的信息不在缓存里，只能重新计算或读取。 |
| recomputation | 重新计算 | Computing a result again because it was not reused. | 没有复用旧结果，只好再算一次。 |
| precomputed state | 预先计算状态 | A state computed before it is later needed. | 提前算好、后面可以直接使用的状态。 |
| intermediate result | 中间结果 | A result produced during a multi-stage model computation. | 模型多步计算中间产生的结果。 |
| model state | 模型状态 | Internal information describing the model at a computation point. | 模型运行到某个时刻时的内部信息。 |
| saved state | 保存的状态 | A state retained for later computation. | 暂时保存、之后还会继续用的状态。 |
| memory state | 内存状态 | State held in runtime memory. | 放在运行内存中的内部状态。 |
| attention output | 注意力输出 | The result produced after attention combines value information. | 注意力加权汇总相关信息后得到的结果。 |
| attention input | 注意力输入 | The token representations supplied to attention. | 送进注意力机制处理的词元表示。 |
| context representation | 上下文表示 | Internal representation of the available context. | 模型内部对前文上下文的数字表达。 |
| model computation | 模型计算 | Numerical operations performed by the model. | 模型内部进行的一系列数字运算。 |
| neural-network computation | 神经网络计算 | Computation performed through neural-network layers. | 数据经过神经网络各层的计算过程。 |
| operation | 操作；运算 | One computational action performed by the runtime or model. | 系统或模型完成的一项运算动作。 |
| generation pipeline | 生成流程 | The sequence of stages from receiving context to producing output. | 从读入前文、建缓存到持续生成的整条流程。 |
| inference pipeline | 推理流程 | The stages used to turn an input into model output. | 从输入到模型返回结果的完整处理流程。 |
| read-build-store-generate-update | 读取—构建—存储—生成—更新 | The five-step process shown for KV cache operation. | KV cache 页面展示的五步工作链路。 |
| process flow | 流程 | An ordered set of operations in the system. | 各步骤按顺序连接起来的工作过程。 |
| step | 步骤 | One stage in the KV-cache process. | 流程中的一个环节。 |
| process the prompt and earlier tokens | 处理提示词和较早词元 | Compute the input context before generating a new token. | 生成新词元前先计算提示词和已有前文。 |
| computed for the sequence | 为序列计算 | Produced for all currently available sequence positions. | 针对当前这串词元算出相应结果。 |
| new states join the cache | 新状态加入缓存 | Newly computed states become part of the cache. | 新算出的状态接到原来的缓存里。 |
| reuse within a request | 请求内复用 | Reuse limited to the current request. | 只在当前请求内部重复使用状态。 |
| cross-generation reuse | 跨生成复用 | Reuse across separate generation runs. | 在不同生成过程之间复用缓存状态。 |
| cross-request cache reuse | 跨请求缓存复用 | Sharing cached states between distinct requests. | 不同请求也共享同一批缓存状态。 |
| permanent model knowledge | 模型永久知识 | Knowledge encoded in learned parameters rather than runtime cache. | 训练后留在参数里的、不会因请求结束消失的知识。 |
| learned knowledge | 学到的知识 | Information encoded during model training. | 模型训练时从数据中学会的规律。 |
| request context | 请求上下文 | Context belonging to one inference request. | 某条请求自带的前文信息。 |
| conversation context | 对话上下文 | Prior messages included for a chat generation. | 为当前对话生成而提供的历史消息。 |
| active context | 当前上下文 | Context currently available during generation. | 当前这一步模型正在使用的前文。 |
| context reuse within generation | 生成内上下文复用 | Reusing context states during one generation. | 同一次生成里反复使用前文状态。 |

## Potential Missing Concepts

- The page explains key and value states but does not explicitly name the query (`Q`), the full `QKV` projection, attention-score calculation, softmax, attention weights, or the matrix multiplications that produce attention outputs.
- It says the cache grows as the sequence grows but does not give the cache-size formula or explain its dependence on batch size, sequence length, number of layers, number of attention heads, head dimension, and datatype/precision.
- It does not explicitly distinguish the prefill phase, which processes the prompt, from the decode phase, which generates one token at a time; these are standard KV-cache workflow terms.
- It does not explain the distinction between multi-head attention (MHA), multi-query attention (MQA), grouped-query attention (GQA), and how head sharing changes KV-cache memory.
- It does not discuss paged attention, paged KV cache, block-based allocation, block tables, or memory fragmentation in high-throughput serving.
- It does not cover cache capacity planning, cache eviction, prefix caching, cache sharing, cache hits/misses, cache reuse across requests, or the safety implications of sharing request prefixes.
- It does not describe GPU memory/VRAM, host memory, accelerator memory, memory bandwidth, memory-bound decoding, or the trade-off between compute and memory movement.
- It does not provide quantitative latency or throughput metrics such as time to first token (TTFT), inter-token latency (ITL), tokens per second, request latency, or batch throughput.
- It does not explain the difference between prompt-processing cost and decoding cost, or why KV cache reduces repeated attention work during autoregressive decoding without removing all attention computation.
- It does not specify tensor shapes, layer-wise storage, data layout, contiguous versus paged storage, or precision choices such as FP32, FP16, BF16, INT8, or quantized KV cache.
- It does not discuss cache quantization, compression, offloading, swapping, recomputation, or other ways to fit KV cache into limited memory.
- It does not explain batching behavior, continuous batching, concurrent requests, variable-length sequences, padding, sequence slots, or scheduling around per-request caches.
- It does not cover distributed inference, tensor parallelism, pipeline parallelism, context parallelism, or how KV states are communicated across devices.
- It does not discuss sliding-window attention, limited attention windows, recurrent/state-space alternatives, or what happens when a sequence exceeds available cache or context capacity.
- It does not distinguish KV cache from a model's learned parameters, hidden states, activations, optimizer state, embeddings, or an external vector/database memory.
- It does not explain cache lifetime, request cancellation, end-of-sequence cleanup, prompt mutation, beam search cache branching, speculative decoding, or cache invalidation.
- It does not give product-level measurements, hardware examples, cost estimates, or a concrete comparison of generation latency with and without caching.

## Aliases / Synonyms

- KV Cache / KV cache / key-value cache / key value cache / attention KV cache
- KV / K-V / K/V / key-value / key and value
- Key state / key states / K state / key representation / key tensor
- Value state / value states / V state / value representation / value tensor
- Key and value states / key/value states / K/V states / KV states
- Attention state / attention states / attention representation / attention information
- Cached state / stored state / saved state / precomputed state / cached attention state
- Cache / runtime cache / inference cache / attention cache / generation cache
- Temporary memory / runtime memory / request memory / request-specific state
- Earlier token / previous token / prior token / existing token
- New token / next token / generated token / output token
- Context / request context / prompt context / conversation context / active context
- Reuse / reuse of computation / computation reuse / attention reuse / state reuse
- Recompute / recomputation / repeated computation / repeated work
- Generation / text generation / inference generation / decoding
- Decode / decoding / decode phase / autoregressive decoding
- Autoregressive generation / token-by-token generation / incremental generation / incremental decoding
- Read / receive the context / prompt processing / process the prompt
- Build / create key and value states / compute attention states / populate the cache
- Store / keep the states / cache the states / retain the states
- Generate / add the next token / produce the next token / continue generation
- Update / extend the cache / append states / join the cache / cache update
- Faster generation / faster next-token generation / lower repeated work / lower repeated computation
- Efficiency / generation efficiency / computational efficiency / runtime efficiency
- Latency / generation latency / request latency / time per token
- Throughput / token throughput / tokens per second / token generation rate
- Memory use / memory consumption / memory footprint / memory overhead
- Cache growth / growing cache / cache size increase / sequence-dependent cache growth
- Long chat / growing conversation / long-context conversation
- Streaming answer / streaming generation / incremental output
- Transformer attention / attention / self-attention / causal attention (related, not identical)
- Model parameters / learned parameters / weights / model weights / learned values
- Context window / context length / maximum context (related, not always identical)
- Long-term memory / persistent memory / permanent memory / cross-request memory
- Prefill / prefill phase / prompt-processing phase / initial context pass
- TTFT / time to first token / first-token latency
- ITL / inter-token latency / time between tokens
- MHA / multi-head attention
- MQA / multi-query attention
- GQA / grouped-query attention
- Paged attention / paged KV cache / block-based KV cache

## Do Not Confuse Candidates

- KV cache ≠ context window: KV cache is runtime state used to speed up generation; the context window is the maximum amount of information the model can work with.
- KV cache ≠ long-term memory: KV cache normally belongs to one active generation or request; long-term memory persists for later use across interactions.
- KV cache ≠ model parameters: cache contents are temporary request-specific states; parameters are learned values that are part of the model.
- KV cache ≠ model weights: weights encode learned behavior; KV states encode intermediate attention information for the current context.
- KV cache ≠ hidden state in general: hidden states are a broad class of internal representations; KV cache specifically retains key and value states used by attention.
- KV cache ≠ activation cache in every sense: the KV cache is a particular subset/arrangement of inference activations, not a name for every intermediate activation.
- KV cache ≠ prompt itself: the prompt is input text/tokens; the cache is numerical attention state computed from that input.
- KV cache ≠ token cache: tokens are text units, while the KV cache stores numerical key and value representations for positions.
- KV cache ≠ context window: a model may have room in its context window while the runtime lacks enough memory for the corresponding KV cache.
- KV cache ≠ permanent storage: cached states can be released after a request; persistent storage survives the request.
- KV cache ≠ external memory: an external database or retrieval system stores documents or records; KV cache stores intermediate model states.
- KV cache ≠ RAG memory: RAG retrieves outside documents at runtime; KV cache reuses attention states already computed for the current sequence.
- KV cache ≠ embedding cache: embeddings are vector representations often used for retrieval; KV cache contains attention key/value tensors for inference.
- KV cache ≠ prefix cache: a prefix cache is a specialized reuse strategy for shared prefixes; KV cache is the broader runtime state structure.
- key state ≠ value state: keys help attention find relevant positions; values carry the information that attention retrieves.
- key/value states ≠ query state: KV states are retained from prior positions; the current query is used to look them up during attention.
- QKV ≠ KV cache: QKV names all three attention projections; KV cache normally refers specifically to retained key and value states.
- attention ≠ KV cache: attention is the mechanism that relates tokens; KV cache is stored data used to make repeated attention computation more efficient.
- self-attention ≠ causal attention: self-attention is the general same-sequence mechanism; causal attention additionally prevents access to future tokens.
- prompt processing ≠ decoding: prompt processing reads the existing context and builds initial states; decoding adds generated tokens step by step.
- prefill ≠ decode: prefill handles the initial prompt pass; decode produces output tokens after or while using the populated cache.
- generation ≠ inference: generation is one kind of inference that produces a sequence; inference also includes tasks that return scores, labels, or embeddings.
- next-token prediction ≠ next-token generation: prediction computes likely next-token outcomes; generation selects and emits one token as output.
- token ≠ word: a token can be part of a word, several characters, punctuation, or another text unit.
- token sequence ≠ context window: a sequence is the actual ordered tokens; a context window is the allowed capacity or range.
- context ≠ context window: context is the information currently supplied; context window is the model's maximum supported amount.
- cache reuse within one generation ≠ cross-request reuse: the page describes reuse during one generation; sharing states between separate requests requires additional cache-management rules.
- cache update ≠ cache eviction: update adds newly computed states; eviction removes states to manage limited capacity.
- cache size ≠ sequence length: sequence length counts tokens; cache size measures stored tensor data and also depends on model architecture and precision.
- memory use ≠ compute use: caching generally spends more memory to avoid some repeated computation.
- memory-bound ≠ compute-bound: memory-bound work is limited by storage or data movement; compute-bound work is limited by arithmetic capacity.
- latency ≠ throughput: latency measures waiting time for a request or token; throughput measures work completed per unit time.
- time to first token ≠ inter-token latency: TTFT is the wait before the first output token; ITL is the interval between later tokens.
- tokens per second ≠ tokens in context: tokens per second is a rate; tokens in context is a count.
- faster generation ≠ free generation: KV cache reduces repeated work but still consumes memory and performs new computation for each step.
- lower repeated computation ≠ zero computation: new tokens still require attention and model-layer computation.
- cache hit ≠ model prediction: a cache hit finds stored intermediate states; prediction chooses or scores the next token.
- cache miss ≠ model failure: a miss means the needed state is unavailable and may require recomputation, not that the model has failed.
- prefix caching ≠ long-term memory: prefix caching reuses computed states for a repeated prefix; it does not create general persistent knowledge.
- MHA ≠ MQA ≠ GQA: these attention variants use different patterns for sharing key/value heads and therefore have different KV-cache footprints.
- paged attention ≠ paging an operating-system disk: paged attention is a serving/memory-layout technique for attention state blocks, not ordinary virtual-memory paging.
- model state ≠ model knowledge: state is an intermediate runtime representation; knowledge learned from training is encoded primarily in parameters.
- learned parameter ≠ cached state: parameters persist with the model; cached states are derived from a particular input and request.
- active request ≠ separate request: an active request owns the current request-specific context; a separate request should not automatically receive its states.
- streaming answer ≠ lower total work by itself: streaming changes delivery timing; KV cache changes how prior attention work is reused.

## Notes

- This is intentionally an expansive raw candidate inventory, not a deduplicated final glossary. Repeated and near-repeated wording is retained where the page, process, examples, or contrasts present it as a distinct candidate.
- The source directly covers the definition of KV cache, temporary memory, earlier tokens, attention information, Transformer key/value states, reuse, memory growth, and the five-step read–build–store–generate–update flow.
- The source directly includes the analogy of keeping notes while reading a long document; the analogy candidates are retained because they explain reuse without implying permanent memory.
- The source's long-chat and streaming-answer examples motivate candidates for long context, request context, incremental generation, lower repeated computation, output tokens, and cache updates.
- The source explicitly contrasts KV cache with context window, long-term memory, and model parameters; those contrasts are repeated in the Do Not Confuse section for downstream glossary review.
- The page names Latency, Tokens per Second, Parameters, Context Window, and Transformer as related concepts. Their broader technical terms are included as candidates even where the page only gives a short link or label.
- Prefill/decode, QKV, attention-head variants, paged cache, tensor shapes, precision, cache management, and serving metrics are standard adjacent concepts that are not fully explained on this page; they are retained and flagged as potential missing concepts.
- “KV cache,” “KV Cache,” “key-value cache,” and “key/value states” are spelling or scope variants and should not be merged during this raw collection pass.
- “Attention state,” “hidden state,” “activation,” “model state,” and “cached state” are related but not interchangeable; the final glossary should preserve their distinctions.
