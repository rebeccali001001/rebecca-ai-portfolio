# Token

## Module/Topic/Source File

- Module: 05 · Tokens, Context & Inference
- Topic: Token
- Source File: `token.html`
- Page Title: What is a Token?
- Topic Position: 03 · Tokens, Context & Inference · Topic 01

## Glossary Candidates

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Token | 词元；token | A small unit of text processed by a language model. | 模型处理的一小段文字、符号或数字。 |
| token | 词元；token | The lowercase form of Token. | token 这个术语的小写写法。 |
| What is a Token? | 什么是 Token？ | The page's question about a model-readable text unit. | 这页要解释“模型怎样切分和处理文字”。 |
| small unit of text | 小文本单位 | A small piece of text used as a processing unit. | 把文字拆成模型能处理的小块。 |
| text unit | 文本单位 | A unit into which text can be divided. | 文本被切分后的一小单位。 |
| language model | 语言模型 | A model that processes and generates language. | 能处理和生成语言的模型。 |
| Language Model | 语言模型 | The capitalized form of language model. | 语言模型这个术语的首字母大写写法。 |
| processed by a language model | 由语言模型处理 | Handled as input or output by a language model. | 文字进入模型后按 token 来计算。 |
| input token | 输入 token；输入词元 | A token supplied to a model as input. | 用户输入被切分后的 token。 |
| output token | 输出 token；输出词元 | A token produced by a model. | 模型生成的一小段文字或符号。 |
| input or output unit | 输入或输出单位 | A unit that can enter or leave a model. | token 既可以是输入，也可以是输出。 |
| whole word | 整个单词 | A complete word that may be represented as one token. | 有些完整单词可能正好对应一个 token。 |
| part of a word | 单词的一部分 | A subword segment that may become a token. | 一个单词也可能被拆成几段 token。 |
| punctuation mark | 标点符号 | A written punctuation symbol that may be tokenized. | 逗号、句号等也可能各自成为 token。 |
| number | 数字 | A numeric text unit that may be tokenized. | 数字文本也会被切分并处理。 |
| another text unit | 其他文本单位 | Any other tokenizer-defined piece of text. | 不属于完整单词的其他文字片段。 |
| text | 文本；文字 | Written input that can be split into tokens. | 用户输入或模型输出的文字内容。 |
| Text | 文本 | The capitalized process-stage label for text. | 流程里的原始文字阶段。 |
| sentence | 句子 | A sequence of text that can be broken into pieces. | 模型处理前的一整句话。 |
| sentences | 句子（复数） | Multiple sequences of text. | 多个可被切分的句子。 |
| words | 单词（复数） | Human language units that do not always equal tokens. | 人看到的单词，不一定等于 token。 |
| word | 单词 | A human language unit. | 人类语言里的词；一个词可能对应多个 token。 |
| human language unit | 人类语言单位 | A word-like unit recognized by people. | 人理解的词，不是模型唯一的切分单位。 |
| text exactly the way humans see words and sentences | 人类看待词和句子的原样文本 | The human view of text that differs from model processing. | 模型并不是像人一样直接阅读单词和句子。 |
| model-readable unit | 模型可读单位 | A text piece represented in a form the model can process. | 模型能识别和计算的文字小块。 |
| model-readable units | 模型可读单位（复数） | Multiple tokenizer-produced processing pieces. | 文字切分后形成的一组模型处理单位。 |
| tokenizer | 分词器；tokenizer | A component that splits text into model-readable units. | 把文字拆成 token 的程序或算法。 |
| Tokenizer | 分词器；Tokenizer | The capitalized process-stage label for the tokenizer. | 流程里的分词器阶段。 |
| tokenization | 分词；词元化 | The process of splitting text into tokens. | 把文字切分成 token 的过程。 |
| tokenize | 进行分词；切成 token | Convert text into tokenizer-defined units. | 把一段文字拆成模型要处理的小块。 |
| token boundaries | token 边界 | The positions where token units begin and end. | token 在文字中从哪里开始、到哪里结束。 |
| tokenizer-dependent | 取决于分词器的 | Determined by the tokenizer being used. | 换一个分词器，切法可能不同。 |
| depending on the tokenizer | 取决于分词器 | Varying according to tokenizer rules. | 是否一个 token，要看具体分词规则。 |
| splitting text | 切分文本 | Dividing text into smaller processing units. | 把原文拆成多个小块。 |
| split the text into model-readable units | 将文本切分为模型可读单位 | The tokenizer operation described in the process. | 分词器把文本变成模型可以处理的单位。 |
| text becomes tokens | 文本变成 token | The result of tokenization. | 原始文字被表示成 token 序列。 |
| token sequence | token 序列 | An ordered sequence of tokens representing text. | 按原文顺序排列的一串 token。 |
| model processing | 模型处理 | Computation performed over token representations. | 模型对 token 表示进行计算。 |
| Model | 模型 | The stage that processes token representations. | 接收 token 并进行计算的 AI 模型。 |
| Model processing | 模型处理 | The capitalized process-stage label for model computation. | 流程图中的模型计算阶段。 |
| token representation | token 表示 | The model's numerical representation of a token. | token 进入模型后对应的内部表示。 |
| token representations | token 表示（复数） | Numerical representations for multiple tokens. | 一串 token 在模型内部的表示。 |
| token ID | token ID；词元编号 | A number assigned to represent a token. | 用数字代表某个 token。 |
| Token ID | token ID；词元编号 | The capitalized process-stage label for token IDs. | 流程中“每个 token 对应数字”的阶段。 |
| Token IDs | token IDs；词元编号（复数） | Numeric identifiers for tokens. | 多个 token 各自对应的编号。 |
| ID | 编号；标识符 | A numeric identifier for a token. | 用来标记 token 的数字。 |
| token identifier | token 标识符 | A number or code identifying a token. | token 在词表中的数字身份。 |
| each token is represented by a number | 每个 token 用一个数字表示 | The mapping from token units to numeric IDs. | 模型不直接拿文字计算，而是使用数字编号。 |
| token-to-ID mapping | token 到 ID 的映射 | The conversion from a token to its numeric identifier. | 把 token 查成对应编号。 |
| vocabulary | 词表 | A collection of token units and their IDs. | 模型认识的 token 及其编号清单。 |
| token vocabulary | token 词表 | The set of token units available to a tokenizer/model. | 分词器可以使用的 token 集合。 |
| vocabulary entry | 词表条目 | One token and its associated identifier. | 词表中的一个 token—编号项目。 |
| generated tokens | 生成的 token | Tokens produced by the model during generation. | 模型逐步生成的文字小块。 |
| Generated tokens | 生成的 token | The capitalized output-stage label for generated tokens. | 流程中模型输出 token 的阶段。 |
| generated text | 生成文本 | Text reconstructed from generated tokens. | 模型生成 token 后还原出的文字。 |
| output text | 输出文本 | Text returned after token generation and conversion. | 用户最后看到的模型文字结果。 |
| converted back to text | 转回文本 | Reconstructing readable text from token units. | 把生成 token 重新拼成文字。 |
| detokenization | 反分词；token 还原 | The process of converting tokens back to text. | 把 token 序列还原成人能读的文字。 |
| decode | 解码；还原文本 | Convert token IDs or generated tokens into text. | 把编号或 token 变回文字。 |
| decoding | 解码过程 | The output-side conversion from token representation to text. | 模型生成后把结果变成可读文字的过程。 |
| text reconstruction | 文本重建 | Reassembling text from token units. | 按顺序把 token 拼回原文或新文本。 |
| generated token sequence | 生成 token 序列 | An ordered sequence produced by the model. | 模型按顺序生成的一串 token。 |
| user enters text | 用户输入文本 | The first step in the page's process flow. | 用户把文字输入系统。 |
| user input | 用户输入 | Text supplied by a user. | 用户交给模型的问题、句子或指令。 |
| input | 输入 | Information supplied to a model. | 送进模型的文字内容。 |
| input text | 输入文本 | Text supplied as model input. | 作为输入的一段文字。 |
| output | 输出 | Information produced by a model. | 模型最后返回的结果。 |
| model output | 模型输出 | Result produced by model processing. | 模型计算后生成的内容。 |
| processing flow | 处理流程 | Ordered stages from text input to text output. | 文字进入、切分、计算、生成、还原的一连串步骤。 |
| token processing flow | token 处理流程 | The page's sequence from text through token IDs to output text. | 从原文到 token，再到生成文字的流程。 |
| Text → Tokenizer → Tokens → Token IDs → Model processing → Generated tokens → Text | 文本→分词器→Token→Token ID→模型处理→生成 Token→文本 | The complete flow shown on the page. | 文字先切分成 token，模型处理后再生成文字。 |
| process stage | 流程阶段 | One named step in a processing sequence. | 整个 token 流程中的一个步骤。 |
| stage 1 · Text | 阶段 1·文本 | The input-text stage. | 第一步：用户输入文本。 |
| stage 2 · Tokenizer | 阶段 2·Tokenizer | The tokenization stage. | 第二步：分词器进行切分。 |
| stage 3 · Tokens | 阶段 3·Tokens | The token sequence stage. | 第三步：文本变成 token。 |
| stage 4 · Token IDs | 阶段 4·Token IDs | The numeric encoding stage. | 第四步：token 变成数字编号。 |
| stage 5 · Model | 阶段 5·Model | The model computation stage. | 第五步：模型处理这些表示。 |
| stage 6 · Output | 阶段 6·Output | The generated-output stage. | 第六步：生成 token 并还原成文本。 |
| user enters text | 用户输入文本 | Text is entered before tokenization. | 用户先输入一句话或一段文字。 |
| tokenizer splits the text | 分词器切分文本 | The tokenizer divides the input. | 分词器负责把输入拆开。 |
| text becomes tokens | 文本变为 tokens | Tokenization produces token units. | 输入文字变成 token 序列。 |
| token IDs | token 编号 | Numeric codes representing tokens. | token 对应的数字表示。 |
| model processes token representations | 模型处理 token 表示 | The model computes over token representations. | 模型对 token 的内部数字表示做计算。 |
| generated tokens are converted back to text | 生成 token 被还原为文本 | Output tokens are decoded into readable text. | 模型生成的小块最后重新拼成句子。 |
| one token | 一个 token | A single token unit. | 一块 token。 |
| one or several tokens | 一个或多个 token | A word or text span represented by one or multiple units. | 一段文字可能占一个，也可能占多个 token。 |
| several tokens | 多个 token | Multiple token units. | 被拆开的多个小块。 |
| token count | token 数量 | The number of tokens in text. | 一段文字被切成了多少个 token。 |
| token length | token 长度 | The amount of tokenized text or number of token units. | 文本占用的 token 长度。 |
| token budget | token 预算 | A limit on how many tokens can be processed or generated. | 一次调用最多能处理或生成多少 token。 |
| context length | 上下文长度 | The amount of tokenized context available to a model. | 模型一次能看到的 token 数量范围。 |
| token usage | token 用量 | The number of tokens consumed by an interaction. | 一次请求输入和输出用了多少 token。 |
| token-based billing | 按 token 计费 | Charging based on processed token counts. | 服务按处理的 token 数量收费。 |
| token efficiency | token 效率 | How much useful content is represented per token. | 用更少 token 表达同样有用内容的程度。 |
| English | 英语 | The language used in the English tokenization example. | 页面用来举例说明 token 切分的语言。 |
| Artificial intelligence | 人工智能 | The text in the English example. | 示例短语“Artificial intelligence”。 |
| “Artificial intelligence” | “Artificial intelligence” | A two-word text example whose token split depends on the tokenizer. | 页面中的英文示例文本。 |
| English-style words | 英语式单词 | Word boundaries commonly used in English. | 以空格等方式划分的英语单词边界。 |
| long word | 长单词 | A word that may be split into several tokens. | 太长的词可能被拆成几块。 |
| uncommon word | 生僻词；不常见单词 | A rare word that may be split into several tokens. | 分词器不常见的词可能被拆开。 |
| long or uncommon word | 长或不常见的词 | A word likely to be represented by multiple tokens. | 长、少见的词更可能占多个 token。 |
| Chinese | 中文 | The language used in the Chinese tokenization example. | 页面用来说明非英语 token 边界的语言。 |
| Chinese text | 中文文本 | Text that is tokenized without necessarily using English word boundaries. | 中文也会切分，但边界不一定按英语单词来。 |
| Chinese tokenization | 中文分词；中文 token 化 | Tokenizing Chinese text into model units. | 把中文文字切成模型单位的过程。 |
| token boundaries do not necessarily match English-style words | token 边界不一定匹配英语式单词 | Token boundaries can differ across languages. | 中文 token 的边界不能简单套用英语单词概念。 |
| multilingual tokenization | 多语言分词 | Tokenization across multiple languages. | 不同语言使用统一模型时的切分过程。 |
| language-dependent tokenization | 依语言而异的分词 | Tokenization behavior that varies with language. | 不同语言可能有不同的 token 切分方式。 |
| tokenization rule | 分词规则 | A rule used to decide token boundaries. | 决定文字如何被拆分的规则。 |
| tokenization strategy | 分词策略 | A broader method for converting text into tokens. | 分词器采用的整体切分方法。 |
| byte-level tokenization | 字节级分词 | Tokenization based partly on byte sequences. | 按字节片段处理文字的一类方法。 |
| character-level tokenization | 字符级分词 | Tokenization using individual characters or character units. | 把单个字符作为主要处理单位。 |
| subword tokenization | 子词分词 | Tokenization into word pieces smaller than whole words. | 把一个词拆成可复用的词片段。 |
| word-level tokenization | 词级分词 | Tokenization where whole words are the main units. | 主要按完整单词切分。 |
| whole-word tokenization | 整词分词 | Tokenization that favors complete words. | 尽量让一个完整词作为一个单位。 |
| subword | 子词；词片段 | A reusable piece of a word. | 单词的一部分，可和其他片段组合。 |
| token piece | token 片段 | A token-sized fragment of text. | 被分词器选出的文字片段。 |
| text fragment | 文本片段 | A portion of a larger text. | 原文中的一小段。 |
| punctuation token | 标点 token | A token representing punctuation. | 代表标点符号的 token。 |
| numeric token | 数字 token | A token representing numeric text. | 代表数字文字的 token。 |
| special token | 特殊 token | A reserved token with a control or structural role. | 用于表示边界、角色或特殊控制信息的 token。 |
| whitespace token | 空白 token | A token that represents whitespace or spacing. | 代表空格等空白信息的 token。 |
| newline token | 换行 token | A token representing a line break. | 代表换行的 token。 |
| tokenization granularity | 分词粒度 | How fine or coarse the token units are. | token 切得大块还是小块。 |
| granularity | 粒度 | The size level of processing units. | 一次处理单位的粗细程度。 |
| text representation | 文本表示 | A representation of text used by the model. | 文字在模型内部采用的表示方式。 |
| numerical representation | 数字表示 | A numeric form used for computation. | 把文字变成数字后进行计算。 |
| encoded text | 编码后的文本 | Text converted into machine-usable codes. | 文字转换成模型能处理的编码。 |
| encoding | 编码 | Converting text units into IDs or representations. | 把 token 映射为数字和内部表示。 |
| token encoding | token 编码 | The encoding of tokens as numeric IDs. | 将 token 变成 token ID 的过程。 |
| vocabulary lookup | 词表查找 | Finding a token's ID in a vocabulary. | 从词表里查某个 token 对应的编号。 |
| token ID sequence | token ID 序列 | Ordered IDs representing an input sequence. | 按文字顺序排列的 token 编号列表。 |
| model-readable | 模型可读的 | Represented in a form the model can process. | 能被模型转换和计算的形式。 |
| human-readable text | 人类可读文本 | Text that people can read directly. | 用户能直接看到和理解的文字。 |
| machine-readable representation | 机器可读表示 | A structured numeric or symbolic representation for computation. | 给机器计算而不是直接给人阅读的表示。 |
| not a word | 不是单词 | A token is not necessarily a complete word. | token 和人类的单词不是一回事。 |
| not a character | 不是字符 | A token is not necessarily one written symbol. | token 可能包含一个或多个字符。 |
| not a parameter | 不是参数 | A token is not a learned numerical value inside a model. | token 是处理单位，参数是模型学到的内部数值。 |
| Token ≠ Word | Token 不等于 Word | A token chosen by a tokenizer differs from a human word. | 一个词可能对应一个或多个 token。 |
| token vs word | token 与单词的区别 | A comparison between model units and human language units. | 模型按 token 处理，人通常按词理解。 |
| Token ≠ Character | Token 不等于 Character | A token may contain one or more characters. | 一个 token 可能由多个字符组成。 |
| token vs character | token 与字符的区别 | A comparison between a tokenizer unit and one written symbol. | 字符是一个符号，token 不一定只有一个字符。 |
| Token ≠ Parameter | Token 不等于 Parameter | A token is an input/output unit; a parameter is a learned value. | token 是文字单位，参数是模型内部学到的数字。 |
| token vs parameter | token 与参数的区别 | A comparison between processed units and learned model values. | 不要把 token 数量和参数数量混为一谈。 |
| character | 字符 | A single written symbol. | 一个单独的文字、字母、数字或符号。 |
| single written symbol | 单个书写符号 | One individual visible symbol. | 一个字符级的最小书写单位。 |
| one or more characters | 一个或多个字符 | The possible character span contained in a token. | 一个 token 可以包含一个或多个字符。 |
| parameter | 参数 | A learned numerical value inside a model. | 训练中学到、存在模型内部的数值。 |
| learned numerical value | 学到的数值 | A numeric value adjusted during model training. | 模型通过训练学出来的内部数字。 |
| input/output unit | 输入/输出单位 | A unit used when text enters or leaves a model. | token 可以是模型接收或生成的单位。 |
| relationship between token and word | token 与单词的关系 | One word may map to one or several tokens. | 单词和 token 不是固定一对一。 |
| relationship between token and character | token 与字符的关系 | One token may contain one or more characters. | token 可以跨越多个字符。 |
| relationship between token and parameter | token 与参数的关系 | Tokens are processed; parameters are learned. | token 是输入输出，参数是内部设置。 |
| context | 上下文 | Surrounding information available to the model. | 当前文字周围、帮助模型理解的内容。 |
| context window | 上下文窗口 | The maximum tokenized context available to a model. | 模型一次能看到的 token 容量上限。 |
| Context Window | 上下文窗口 | The related-concept label for context window. | 相关概念链接中的上下文窗口。 |
| context-window limit | 上下文窗口限制 | A limit on the number of tokens in context. | 输入和输出不能无限占用 token。 |
| context length limit | 上下文长度限制 | A maximum length measured in tokens. | 模型一次处理的 token 数上限。 |
| LLM | 大型语言模型 | Large Language Model, a model that processes tokenized language. | 处理 token 的大型语言模型简称。 |
| Large Language Model | 大型语言模型 | The expanded form of LLM. | LLM 的英文全称。 |
| LLM inference | LLM 推理 | Running a language model to produce output from tokenized input. | 用模型根据输入 token 生成结果。 |
| LLM Inference | LLM 推理 | The related-concept label for inference with an LLM. | 相关概念流程中的 LLM 推理阶段。 |
| inference | 推理 | Using a trained model to process input and generate output. | 模型实际回答问题或生成内容的过程。 |
| Transformer | Transformer；变换器架构 | A neural-network architecture commonly used by language models. | 很多语言模型用来处理 token 的网络架构。 |
| transformer model | Transformer 模型 | A model architecture that processes token representations. | 以 Transformer 为基础处理 token 的模型。 |
| Parameters | 参数 | The related-concept label linked from the page. | 页面关联的模型内部学习数值概念。 |
| Pre-training | 预训练 | The related training stage linked from the token topic. | 模型先从数据中学习一般语言规律的阶段。 |
| tokenization topic | tokenization 主题 | The broader process topic related to Token. | 专门解释如何切分文本的主题。 |
| tokens-context-inference | Tokens、Context & Inference | The parent topic group containing this page. | 本页所属的 token、上下文和推理主题组。 |
| related concept | 相关概念 | A concept connected to token processing. | 与 token 学习路径相连的概念。 |
| concept map | 概念图 | A map linking text, tokenization, token, context window, inference, and output. | 展示这些概念前后关系的图。 |
| Text → Tokenization → Token → Context Window → LLM Inference → Output | 文本→分词→Token→上下文窗口→LLM 推理→输出 | The page's related-concept chain. | 从文字切分到模型生成结果的学习路径。 |
| output generation | 输出生成 | Producing output tokens from model computation. | 模型根据输入逐步生成结果。 |
| generation | 生成 | Creating new token units as model output. | 模型一个 token 一个 token 地产生文字。 |
| token generation | token 生成 | Producing tokens during inference. | 推理时生成输出 token 的过程。 |
| autoregressive generation | 自回归生成 | Generating a next token based on preceding tokens. | 根据已经生成的内容继续生成下一个 token。 |
| next token | 下一个 token | The next unit predicted or generated in a sequence. | 模型接下来要输出的那一小段文字。 |
| next-token prediction | 下一个 token 预测 | Predicting the next token in a sequence. | 模型根据前文猜下一个 token。 |
| token probability | token 概率 | A score or probability assigned to a possible token. | 模型认为某个 token 接下来出现的可能性。 |
| candidate token | 候选 token | One possible next token considered by a model. | 模型可以选择生成的一个候选小块。 |
| decoding strategy | 解码策略 | A rule for selecting generated tokens. | 决定每一步选哪个 token 的方法。 |
| sampling | 采样 | Selecting output tokens using a probability distribution. | 按概率从候选 token 中选择输出。 |
| greedy decoding | 贪心解码 | Choosing the highest-scoring next token. | 每一步都选当前分数最高的 token。 |
| temperature | 温度 | A decoding control that changes output randomness. | 调整生成 token 随机程度的参数。 |
| generated response | 生成回答 | Text formed from the model's generated tokens. | 模型生成 token 后得到的完整回答。 |
| token-level processing | token 级处理 | Computation performed one token unit at a time or over token units. | 模型把文字当作 token 单位进行计算。 |
| sequence modeling | 序列建模 | Modeling ordered token sequences. | 学习 token 前后顺序和关系。 |
| sequence position | 序列位置 | A token's location in a token sequence. | token 在一串 token 中的顺序位置。 |
| positional information | 位置信息 | Information about where a token occurs. | 模型知道 token 在句子中的位置。 |
| token order | token 顺序 | The order in which token units appear. | token 在文本中排列的先后次序。 |
| token context | token 上下文 | Surrounding tokens considered for a token. | 某个 token 周围的其他 token。 |
| token-level context | token 级上下文 | Context represented as neighboring or available tokens. | 以 token 形式提供给模型的上下文。 |
| semantic unit | 语义单位 | A unit carrying meaning in language. | 能表达部分意思的文字单位；不必等于 token。 |
| linguistic unit | 语言单位 | A unit defined by human language structure. | 按语言学理解的词、词素等单位。 |
| token boundary mismatch | token 边界不匹配 | The difference between token boundaries and word or character boundaries. | token 切分线可能和人理解的词边界不同。 |
| one-to-one mapping | 一对一映射 | A mapping where one item corresponds to one item. | 一个词固定对应一个 token；现实中不一定如此。 |
| many-to-one mapping | 多对一映射 | Multiple source units represented as one unit. | 多个字符可能合成一个 token。 |
| one-to-many mapping | 一对多映射 | One source unit represented as several units. | 一个单词可能拆成多个 token。 |
| model input capacity | 模型输入容量 | The amount of tokenized input a model can accept. | 模型一次能接收的 token 数量。 |
| prompt length | 提示长度 | The tokenized length of a prompt. | 提示词占用的 token 数。 |
| completion length | 补全长度 | The tokenized length of generated completion text. | 模型输出占用的 token 数。 |
| input tokens | 输入 token 数量 | Tokens counted in the input. | 用户输入部分的 token 数。 |
| output tokens | 输出 token 数量 | Tokens counted in the output. | 模型生成部分的 token 数。 |
| total tokens | 总 token 数 | Input tokens plus output tokens. | 输入和输出 token 加起来的数量。 |
| token limit | token 限制 | A maximum allowed token count. | 系统规定最多能处理多少 token。 |
| tokenization error | 分词错误 | An incorrect or undesirable tokenization result. | 分词器把文字切得不符合预期。 |
| unknown token | 未知 token | A fallback token used for unavailable text. | 词表不认识的内容可能被替代成的特殊 token。 |
| out-of-vocabulary | 超出词表 | Text not represented directly in a vocabulary. | 词表里没有直接对应项的文字。 |
| vocabulary coverage | 词表覆盖率 | How much input text the vocabulary can represent. | 词表能直接或间接表示多少种文字。 |
| tokenization cost | 分词成本 | Computation or operational cost of tokenizing text. | 把文字切分也需要时间和计算。 |
| tokenization latency | 分词延迟 | Time required to tokenize text. | 分词器完成切分所需的时间。 |
| tokens per second | 每秒 token 数 | A rate measuring token processing or generation. | 一秒钟处理或生成多少 token。 |
| throughput | 吞吐量 | Amount of token processing per unit time. | 单位时间能处理多少 token。 |
| latency | 延迟 | Time taken to produce or process tokens. | 从输入到结果需要等待多久。 |
| token metric | token 指标 | A measurement based on token counts or rates. | 用 token 数量、速度或长度衡量系统。 |
| token-based metric | 基于 token 的指标 | A metric calculated from tokenized text. | 以 token 为统计单位的指标。 |
| token cost | token 成本 | Resource or billing cost associated with tokens. | token 越多，可能越费时间、显存或费用。 |
| token budget utilization | token 预算利用率 | The share of an allowed token budget that is used. | 实际用了 token 上限的多少。 |

## Potential Missing Concepts

- Byte-pair encoding (BPE), WordPiece, Unigram, SentencePiece, byte-level BPE, and vocabulary construction are common tokenizer mechanisms not named in the source.
- Tokenizer training, merge rules, merge ranks, subword vocabulary, normalization, Unicode normalization, whitespace handling, lowercasing, and pre-tokenization are implementation concepts absent from the beginner explanation.
- Byte, Unicode code point, grapheme cluster, character, word, morpheme, and subword are finer-grained units that help explain why token boundaries differ from human language boundaries.
- Special tokens such as BOS, EOS, PAD, UNK, CLS, SEP, role tokens, chat-template tokens, and end-of-turn markers are not explicitly described.
- Token vocabulary, vocabulary size, token-to-ID lookup, unknown-token fallback, out-of-vocabulary handling, reserved IDs, and vocabulary coverage are implied by token IDs but not explained.
- Encoding and decoding, detokenization, normalization, byte fallback, reversible tokenization, and whitespace reconstruction are output/input mechanics not detailed on the page.
- Token count, context length, maximum sequence length, prompt length, completion length, total tokens, truncation, padding, and sliding-window chunking are practical length concepts not named.
- Token budget, input-token pricing, output-token pricing, billing units, rate limits, tokens per second, throughput, first-token latency, and time per output token are useful operational metrics absent from the page.
- Token probability, logits, softmax, next-token prediction, autoregressive generation, causal language modeling, candidate distribution, sampling, greedy decoding, temperature, top-k, and top-p are generation mechanisms not covered in detail.
- Attention, embeddings, positional encoding, hidden states, contextual representations, and Transformer layers explain how token IDs become model computations but are only linked or implied.
- Context-window truncation, lost context, recency effects, long-context degradation, attention complexity, and effective context are practical consequences of tokenized context not addressed.
- Different tokenizers can produce different token counts for the same text; tokenizer compatibility, tokenizer versioning, and model-specific vocabulary are not explicitly discussed.
- English, Chinese, Japanese, Korean, Arabic, emoji, code, URLs, whitespace, punctuation, and mixed-language text can have different tokenization behavior; only English and Chinese are exemplified.
- Unicode, accents, capitalization, contractions, apostrophes, hyphenation, line breaks, tabs, and invisible characters can affect token boundaries but are not shown.
- Tokenization of images, audio, video, multimodal patches, visual tokens, audio tokens, and discrete latent tokens is outside the page's text-only scope.
- Prompt injection, delimiter tokens, control tokens, role markers, system/user/assistant messages, and chat templates are adjacent token-usage concepts not covered.
- Compression ratio, characters-per-token, words-per-token, token-to-character ratio, and language efficiency are useful comparative metrics absent from the source.
- Token count is not the same as semantic complexity, word count, character count, parameter count, compute cost, or model quality; these distinctions could be expanded.
- Tokenization bugs, tokenizer mismatch, malformed UTF-8, invalid token IDs, sequence overflow, truncation, padding artifacts, and decoding artifacts are practical failure modes not discussed.
- Caching, KV cache, prefix caching, prompt caching, speculative decoding, batching, continuous batching, and streaming are serving mechanisms related to token processing but absent from the page.
- Perplexity, cross-entropy loss, token accuracy, next-token accuracy, and bits per byte are token-level evaluation concepts not named.
- Token attribution, token saliency, token masking, masked language modeling, span corruption, and token-level supervision are training or analysis concepts not included.
- Vocabulary expansion, tokenizer adaptation, token healing, token merging, token pruning, and token compression are advanced concepts beyond the page.

## Aliases / Synonyms

- Token ↔ token ↔ text token ↔ word piece ↔ text unit
- Token ↔ model-readable unit ↔ model processing unit ↔ input/output unit
- Tokenization ↔ tokenisation ↔ tokenization process ↔ text splitting ↔ text segmentation
- Tokenizer ↔ tokeniser ↔ text tokenizer ↔ tokenization component ↔ text splitter
- Token ID ↔ token identifier ↔ token index ↔ vocabulary index ↔ numeric token code
- Token IDs ↔ token identifiers ↔ token index sequence ↔ encoded token sequence
- Token sequence ↔ token string ↔ sequence of tokens ↔ tokenized text
- Token representation ↔ token embedding ↔ token vector ↔ numerical token representation (context-dependent)
- Input token ↔ prompt token ↔ source token ↔ user-input token
- Output token ↔ generated token ↔ completion token ↔ target token (context-dependent)
- Generated tokens ↔ output tokens ↔ generated text units ↔ decoded output units
- Text ↔ input text ↔ source text ↔ natural-language text
- Word ↔ whole word ↔ human language unit ↔ lexical item (context-dependent)
- Part of a word ↔ subword ↔ word piece ↔ word fragment
- Character ↔ written character ↔ single written symbol ↔ code point (not always identical)
- Punctuation mark ↔ punctuation symbol ↔ punctuation token (when tokenized separately)
- Number ↔ numeric text ↔ numeral ↔ numeric token (context-dependent)
- Token vocabulary ↔ vocabulary ↔ token set ↔ tokenizer vocabulary
- Vocabulary entry ↔ token record ↔ token-ID pair ↔ vocabulary item
- Text encoding ↔ token encoding ↔ token-to-ID conversion ↔ token lookup
- Decoding ↔ detokenization ↔ token-to-text conversion ↔ text reconstruction
- Encode ↔ tokenize and encode ↔ convert to token IDs ↔ map text to IDs
- Decode ↔ detokenize ↔ convert IDs to text ↔ reconstruct text
- Token boundary ↔ segmentation boundary ↔ split point ↔ tokenization boundary
- Token count ↔ number of tokens ↔ token length ↔ sequence length (context-dependent)
- Context window ↔ context length ↔ maximum context ↔ token capacity ↔ maximum sequence length (context-dependent)
- LLM ↔ Large Language Model ↔ large language model ↔ language model (LLM is a subset/context)
- LLM inference ↔ language-model inference ↔ model serving ↔ generation-time computation
- Inference ↔ prediction ↔ generation ↔ runtime model use
- Model output ↔ generated output ↔ completion ↔ response ↔ output text
- Next token ↔ following token ↔ predicted token ↔ candidate continuation
- Next-token prediction ↔ next-token modeling ↔ causal language modeling ↔ autoregressive prediction
- Token probability ↔ next-token probability ↔ candidate probability ↔ token likelihood
- Sampling ↔ probabilistic decoding ↔ random decoding ↔ distribution sampling
- Greedy decoding ↔ argmax decoding ↔ highest-score decoding
- Temperature ↔ sampling temperature ↔ randomness control ↔ decoding temperature
- Tokens per second ↔ token generation rate ↔ token throughput ↔ TPS
- Latency ↔ response delay ↔ generation delay ↔ time to output
- Throughput ↔ processing rate ↔ generation throughput ↔ tokens per second (not always identical)
- Parameter ↔ model parameter ↔ learned numerical value ↔ learned setting
- Token vs word ↔ token-word distinction ↔ model unit versus human word
- Token vs character ↔ token-character distinction ↔ model unit versus written symbol
- Token vs parameter ↔ token-parameter distinction ↔ processed unit versus learned value
- English tokenization ↔ English text segmentation ↔ English token splitting
- Chinese tokenization ↔ Chinese text segmentation ↔ Chinese token splitting
- Subword tokenization ↔ word-piece tokenization ↔ word-fragment tokenization
- Byte-level tokenization ↔ byte tokenization ↔ byte-based segmentation
- Word-level tokenization ↔ whole-word segmentation ↔ word tokenization

## Do Not Confuse Candidates

- Token vs word: a token is selected by a tokenizer; a word is a human language unit. One word may become one or several tokens.
- Token vs character: a token may contain one or more characters; a character is one written symbol.
- Token vs parameter: a token is an input/output processing unit; a parameter is a learned numerical value inside the model.
- Token vs embedding: a token is a text or vocabulary unit; an embedding is a numerical vector representation of a token or other input.
- Token vs token ID: the token is the text/symbol unit; the token ID is the number used to identify it.
- Token vs token representation: the token is the discrete unit; its representation is the numerical form used in computation.
- Tokenization vs encoding: tokenization chooses units; encoding commonly maps those units to IDs or numerical representations.
- Encoding vs decoding: encoding maps text toward token units/IDs; decoding reconstructs text from token units/IDs.
- Tokenizer vs vocabulary: the tokenizer is the component or algorithm; the vocabulary is the set of tokens and IDs it uses.
- Token vocabulary vs dictionary: a vocabulary is model-specific and may contain subwords, punctuation, numbers, and special tokens; it is not a normal human dictionary.
- Token boundary vs word boundary: token boundaries are tokenizer decisions and need not align with word boundaries.
- Token count vs word count: a sentence's token count can differ from its number of words.
- Token count vs character count: one token can include multiple characters, and characters can be split across tokens.
- Token count vs parameter count: tokens are processed units for an interaction; parameters are learned values in the model.
- Token count vs context-window size: token count measures a particular text; context-window size is a model capacity limit.
- Token length vs semantic length: more tokens do not necessarily mean more meaning or complexity.
- Input tokens vs output tokens: input tokens are supplied by the user/system; output tokens are generated by the model.
- Generated token vs generated text: a generated token is one unit; generated text is the reconstructed sequence.
- Token generation vs tokenization: generation creates output tokens; tokenization splits existing text.
- Tokenization vs inference: tokenization prepares text; inference runs the model over the prepared representation.
- Inference vs training: inference uses learned parameters; training updates learned parameters.
- Context window vs context: the context is available information; the context window is the maximum capacity for tokenized context.
- Context window vs memory: a context window is current input capacity, not necessarily persistent long-term memory.
- LLM vs tokenizer: an LLM performs model computation; a tokenizer prepares and reconstructs text.
- LLM inference vs tokenization: inference includes model computation, while tokenization is an input/output preprocessing step.
- Token ID vs parameter ID: a token ID indexes a vocabulary entry; it is not a model parameter identifier.
- Token ID vs character code: a token ID is model-vocabulary-specific; a character code identifies a character/code point.
- Token probability vs token: probability is a score for a candidate; the token is the candidate unit itself.
- Next token vs next word: a model predicts token units, which may be smaller or larger than human words.
- Sampling vs tokenization: sampling selects generated tokens; tokenization creates the units used by the model.
- Temperature vs model parameter: temperature controls decoding behavior; it is not a learned weight in the model.
- Throughput vs latency: throughput measures amount processed per time; latency measures time to a result.
- Tokens per second vs token count: tokens per second is a rate; token count is an amount.
- Token budget vs context window: a token budget may be an application or billing limit; the context window is a model capacity limit.
- Token budget vs parameter budget: token budget limits processed text; parameter budget describes model size or trainable values.
- Tokenization granularity vs model quality: finer or coarser tokenization alone does not determine quality.
- English word boundary vs Chinese token boundary: Chinese token boundaries do not necessarily follow English-style word assumptions.
- Subword vs morpheme: a subword is a tokenizer unit; a morpheme is a linguistic meaning-bearing unit and may not align with it.
- Character vs Unicode code point: a visible character can involve multiple code points; the two notions are not always identical.
- Byte vs character: bytes encode data; characters are written symbols; tokenizers may operate partly at byte level.
- Special token vs ordinary text token: special tokens may control structure or boundaries and need not represent ordinary text.
- Unknown token vs uncommon word: an uncommon word may be split into known subwords rather than becoming one unknown token.
- Vocabulary size vs context length: vocabulary size is the number of available token entries; context length is how many tokens can be processed together.
- Tokenizer version vs model version: changing a tokenizer can change token IDs and counts even if the model weights are unchanged.
- Tokenization compatibility vs text compatibility: a model expects the tokenizer and vocabulary it was trained with; arbitrary token IDs are not interchangeable.
- Detokenization vs summarization: detokenization reconstructs text; summarization creates a shorter meaning-preserving output.
- Tokenization vs translation: tokenization changes representation within a language; translation changes content into another language.
- Token processing vs human reading: model computation over token representations is not human-like reading or awareness.
- Token relevance vs token identity: a token's importance in a task is not the same as its vocabulary identity.
- Token unit vs semantic unit: token boundaries are computational; semantic boundaries are meaning-based.
- More tokens vs better answer: a longer token sequence does not guarantee a more accurate or useful output.
- More parameters vs more tokens: model parameter count and prompt/output token count are different scales and resources.
- Token cost vs model cost: token-related cost is one part of runtime or billing cost; architecture and hardware also matter.
- Context length vs context quality: allowing more tokens does not guarantee the model will use every token correctly.
- Output token limit vs answer completeness: truncating output tokens can cut off an answer; a high limit does not ensure quality.

## Notes

- The page defines a token as “a small unit of text processed by a language model.”
- The source explicitly says that a token may be a whole word, part of a word, punctuation mark, number, or another text unit depending on the tokenizer.
- The page's main takeaway is that AI models process tokens, not text exactly the way humans see words and sentences.
- The LEGO analogy treats a sentence as a LEGO model and tokens as the smaller LEGO pieces used by the model.
- The source explicitly states “Token ≠ Word” and explains that one word may be one token or multiple tokens.
- The process flow is: Text → Tokenizer → Tokens → Token IDs → Model processing → Generated tokens → Text.
- In the first process step, a user enters text.
- In the tokenizer step, the tokenizer splits text into model-readable units.
- In the token step, the text becomes tokens.
- In the token-ID step, each token is represented by a number.
- In the model step, the model processes token representations.
- In the output step, generated tokens are converted back to text.
- The English example is “Artificial intelligence”; the page says it may be split into one or several tokens depending on the tokenizer.
- The long-word example says a long or uncommon word may be split into several tokens.
- The Chinese example says Chinese text is tokenized, but token boundaries do not necessarily match English-style words.
- The comparison section explicitly distinguishes Token from Word, Character, and Parameter.
- The related-concepts chain is Text → Tokenization → Token → Context Window → LLM Inference → Output.
- The linked related concepts include Context Window, LLM, Transformer, and Parameters.
- The page's definition uses “language model,” while the related-concept section uses “LLM Inference”; both are retained as source-grounded candidates.
- The page includes an explainer image and video; media file names and captions are context, not independent token mechanisms.
- Media context retained from the page: `vedio/token-lego-analogy.png`, `vedio/token.png`, `vedio/token.mp4`, and `vedio/token.vtt`.
- The video caption is “A short visual explanation of tokens.”
- The page has a “Video” section labelled “Independent explainer” and “visual explainer.”
- Raw collection intentionally preserves repeated wording, capitalization variants, source phrases, process labels, linked concepts, aliases, and overlapping candidates.
- No deduplication, pruning, or ranking was performed in this raw candidate collection.
