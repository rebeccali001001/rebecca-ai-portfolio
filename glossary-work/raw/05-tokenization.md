# Topic

Tokenization

## Topic Metadata

- Module: 05 · Tokens, Context & Inference
- Topic: Tokenization
- Topic Number: Topic 02
- Source File: `tokenization.html`
- Page Title: What is Tokenization?
- Source Scope: Complete page body, including the definition, analogy, five-step process flow, real-world examples, misconception cards, related-concept map, takeaway, and video metadata.

## Glossary Candidates

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Tokenization | 词元化；分词；标记化 | The process of converting text into tokens. | 把文字转换成模型能处理的小单位。 |
| tokenize | 进行词元化；切分成词元 | To convert text into tokens. | 把一段文字切成词元。 |
| token | 词元；标记 | A unit of text processed by a language model. | 语言模型处理文字时使用的一个小单位。 |
| tokens | 词元；标记复数 | Multiple text units produced by tokenization. | 文字被切开后得到的一组小单位。 |
| token unit | 词元单位 | A text unit treated as one token. | 模型把它当作一个单位处理的文字片段。 |
| token piece | 词元片段 | A piece of text created by a tokenizer. | 分词器切出来的一小段文字。 |
| token pieces | 词元片段复数 | The pieces into which a tokenizer divides text. | 分词器把文字拆成的多个片段。 |
| text unit | 文本单位 | A piece of text treated as one processing unit. | 一次作为一个单位处理的文字片段。 |
| text | 文本；文字 | Written language given to or produced by a model. | 以文字形式存在的信息。 |
| raw text | 原始文本 | Text before it is converted into tokens. | 还没有切成词元的原始文字。 |
| written text | 书面文本 | Language represented as written characters. | 以写出来的文字表示的语言。 |
| sentence | 句子 | A group of words forming one statement. | 表达一个意思的一句话。 |
| document | 文档 | A larger piece of written text. | 由较多文字组成的一份材料。 |
| word | 单词；词 | A human-language unit made from letters or characters. | 人类语言里有完整意义的词。 |
| whole word | 完整单词 | A token that corresponds to an entire word. | 一个词元刚好等于一个完整单词。 |
| part of a word | 单词的一部分 | A token corresponding to only part of a word. | 一个词元只代表单词的一部分。 |
| punctuation | 标点符号 | Marks such as commas or periods that can be tokenized. | 逗号、句号等也可能被当成词元。 |
| another text unit | 其他文本单位 | A tokenizer-dependent unit that is not necessarily a word or punctuation mark. | 根据分词器规则产生的其他文字单位。 |
| language model | 语言模型 | A model that processes language and produces language-related outputs. | 能处理文字并生成文字结果的模型。 |
| model | 模型 | A learned system that processes input and produces output. | 学会规律后处理输入并给出结果的系统。 |
| tokenizer | 分词器；词元分析器 | A component that divides text into token pieces. | 负责把文字切成词元的工具或组件。 |
| tokenizer rules | 分词器规则 | Rules used by a tokenizer to create token units. | 决定文字如何被切开的规则。 |
| tokenizer vocabulary | 分词器词表 | The vocabulary from which token IDs are assigned. | 分词器知道并能编号的词元集合。 |
| vocabulary | 词表；词汇表 | A collection of token units known to a tokenizer. | 分词器可识别的词元清单。 |
| model-readable unit | 模型可读单位 | A unit in the format the model can process. | 模型可以直接处理的输入单位。 |
| model-readable units | 模型可读单位复数 | The token units used as model input. | 模型处理输入时使用的一串词元单位。 |
| processing unit | 处理单位 | A unit handled by a computational process. | 系统一次处理的一小块信息。 |
| language processing | 语言处理 | Processing written language in a computational system. | 让计算机系统处理文字语言。 |
| text processing | 文本处理 | Operations performed on written text. | 对文字进行切分、转换或分析。 |
| input text | 输入文本 | Text supplied to a tokenizer or model. | 交给分词器或模型的文字。 |
| model input | 模型输入 | Information sent into the model for processing. | 送进模型进行处理的信息。 |
| input | 输入 | Information supplied to a system. | 交给系统的内容。 |
| output | 输出 | The result produced by a system. | 系统处理后给出的结果。 |
| model output | 模型输出 | The result produced by a model. | 模型处理输入后生成的结果。 |
| user input | 用户输入 | Text entered by a user. | 用户自己输入给系统的文字。 |
| user enters text | 用户输入文字 | A user supplies a sentence or document. | 用户把一句话或一份文档交给系统。 |
| sentence input | 句子输入 | A sentence supplied as input. | 作为输入交给系统的一句话。 |
| document input | 文档输入 | A document supplied as input. | 作为输入交给系统的一份文档。 |
| chat message | 聊天消息 | A message sent in a chat interaction. | 聊天时发送的一条消息。 |
| message | 消息 | A piece of information sent between a user and system. | 用户和系统之间传递的一段内容。 |
| chat assistant | 聊天助手 | An AI system that processes messages and responds. | 能理解消息并回复用户的 AI 助手。 |
| AI product | AI 产品 | A product that uses artificial intelligence capabilities. | 使用人工智能能力的产品。 |
| AI | 人工智能；AI | Artificial intelligence technology or systems. | 让计算机完成智能任务的技术。 |
| ID | 标识符；编号 | An identifier used to represent something. | 用来代表某个对象的编号。 |
| token ID | 词元 ID；词元编号 | A number representing a token. | 用数字代表一个词元。 |
| token IDs | 词元 ID；词元编号复数 | Numbers representing the tokens in an input. | 代表输入中各个词元的一串数字。 |
| vocabulary ID | 词表编号 | An ID assigned to a token in the tokenizer vocabulary. | 词表给某个词元分配的编号。 |
| numeric representation | 数字表示 | Representing a text unit with a number. | 用数字来表示文字单位。 |
| map to numbers | 映射为数字 | Convert token units into numeric IDs. | 把词元对应到数字编号。 |
| mapping | 映射 | A correspondence between text units and IDs. | 文字单位和数字编号之间的对应关系。 |
| representation | 表示；表征 | A form used to represent information. | 用某种形式表达信息。 |
| sequence | 序列 | An ordered arrangement of units. | 按顺序排列的一组单位。 |
| token sequence | 词元序列 | An ordered series of tokens representing text. | 按原文顺序排列的一串词元。 |
| token-ID sequence | 词元 ID 序列 | An ordered series of numeric token IDs. | 按顺序排列的一串词元编号。 |
| process the sequence | 处理序列 | Process token IDs in their ordered arrangement. | 按顺序处理这串词元编号。 |
| model input sequence | 模型输入序列 | The ordered sequence sent into a model. | 送进模型的一串有顺序的输入单位。 |
| tokenization flow | 词元化流程 | The ordered path from text to model input. | 从文字到模型输入的完整流程。 |
| text-to-token flow | 文本到词元流程 | The transformation from text into token pieces. | 文字变成词元片段的过程。 |
| text-to-ID flow | 文本到 ID 流程 | The transformation from text into numeric token IDs. | 文字先切成词元、再变成数字编号的过程。 |
| receive text | 接收文本 | Accept text as the first processing step. | 系统先收到一段文字。 |
| split the text | 切分文本 | Divide text into token pieces. | 把文字拆成多个片段。 |
| divide text | 划分文本 | Separate text according to tokenizer rules. | 按分词器规则把文字分开。 |
| represent units | 表示单位 | Represent text pieces in a model-readable form. | 把文字片段表示成模型能处理的单位。 |
| model-readable representation | 模型可读表示 | A representation that the model can consume. | 模型能够接收和处理的表示形式。 |
| process the sequence | 处理序列 | Run the ordered token representation through the model. | 让模型处理按顺序排列的词元表示。 |
| user text processing | 用户文本处理 | Processing text entered by a user. | 系统对用户输入的文字进行处理。 |
| one token | 一个词元 | A complete piece represented as one token. | 某段内容只对应一个词元。 |
| several pieces | 多个片段 | A word or text string represented by multiple token pieces. | 一段内容被拆成多个词元片段。 |
| one or several pieces | 一个或多个片段 | A tokenizer may represent the same text with one or several pieces. | 同一段文字可能被切成一个或多个词元。 |
| tokenizer-dependent | 取决于分词器的 | Determined by the tokenizer being used. | 结果会因使用的分词器不同而不同。 |
| tokenizer vocabulary-dependent | 取决于分词器词表的 | Determined by the tokenizer's vocabulary and rules. | 结果由分词器词表和规则共同决定。 |
| “unbelievable” | “unbelievable” | The example word used to show variable token pieces. | 页面用来说明一个词可能被切成一个或多个词元的例子。 |
| text conversion | 文本转换 | Changing text into another representation. | 把文字变成另一种表示形式。 |
| conversion | 转换 | Changing one form into another. | 把一种形式变成另一种形式。 |
| smaller unit | 更小单位 | A smaller piece created from a larger text string. | 从整段文字中切出的较小部分。 |
| smaller units | 更小单位复数 | Multiple smaller pieces of text. | 一整段文字被拆成的多个小部分。 |
| puzzle pieces | 拼图块；拼图片 | An analogy for token pieces that make up text. | 把句子想成被切成许多小拼图块。 |
| analogy | 类比 | A comparison used to explain a concept. | 用熟悉的事物帮助理解抽象概念。 |
| puzzle-piece analogy | 拼图块类比 | Explaining tokenization as cutting a sentence into pieces. | 把分词理解成先把句子切成拼图块。 |
| cut a sentence | 切开句子 | Divide a sentence into smaller pieces. | 把一句话拆成多个小片段。 |
| understand the input | 理解输入 | Use the token pieces to process the supplied text. | 模型利用词元片段处理用户给的内容。 |
| produce an output | 产生输出 | Generate a result after processing input. | 处理输入后给出结果。 |
| input processing | 输入处理 | Processing the information supplied to a model. | 对送入模型的内容进行处理。 |
| output production | 输出产生 | Producing a result from processed input. | 根据处理后的输入生成结果。 |
| model processing | 模型处理 | The model's operation on token IDs. | 模型对词元编号进行计算和处理。 |
| text representation | 文本表示 | A representation of text as token pieces or IDs. | 用词元或编号来表达原始文字。 |
| language-model input | 语言模型输入 | Token IDs supplied to a language model. | 送给语言模型处理的词元编号。 |
| tokenizer component | 分词器组件 | The component responsible for text-to-token conversion. | 负责把文本变成词元的系统部件。 |
| model component | 模型组件 | A component involved in processing model input. | 参与模型输入处理的系统部件。 |
| model-readable | 模型可读的 | In a form that a model can process. | 格式适合模型读取和计算。 |
| processable text | 可处理文本 | Text that can be converted into model input. | 可以被分词器转换成模型输入的文字。 |
| text segmentation | 文本分段；文本切分 | Dividing text into smaller segments. | 把文字切成更小片段的过程。 |
| text splitting | 文本切分 | Separating text into parts. | 把文字拆开成多个部分。 |
| splitting by spaces | 按空格切分 | Separating text only where spaces occur. | 只按照空格把文字分开。 |
| space-based splitting | 基于空格的切分 | A simple split that uses spaces as boundaries. | 把空格当成唯一切分位置的方法。 |
| tokenizer-based splitting | 基于分词器的切分 | Splitting text according to tokenizer rules. | 按分词器自己的规则切分，而不只是看空格。 |
| tokenization rule | 词元化规则 | A rule used to decide token boundaries and units. | 决定哪里切开、每块算什么的规则。 |
| token boundary | 词元边界 | The boundary between two token pieces. | 两个词元片段之间的分界线。 |
| boundary | 边界 | A point where one unit ends and another begins. | 一个单位结束、另一个单位开始的位置。 |
| model-readable token | 模型可读词元 | A token in the form expected by the model. | 模型可以直接使用的词元。 |
| language unit | 语言单位 | A unit used to represent part of language. | 用来表示语言一部分的单位。 |
| whole-word tokenization | 整词词元化 | Tokenization where each token is a whole word. | 每个词元都刚好对应一个完整单词。 |
| subword tokenization | 子词词元化 | Tokenization where words may become smaller word pieces. | 一个词可以被拆成几个更小的词片段。 |
| character tokenization | 字符词元化 | Tokenization where individual characters are units. | 把一个个字符作为词元单位。 |
| punctuation tokenization | 标点词元化 | Treating punctuation as token units. | 把标点符号也作为词元处理。 |
| whitespace tokenization | 空白符词元化 | Tokenization based mainly on whitespace boundaries. | 主要按照空格等空白符来切分。 |
| byte-level tokenization | 字节级词元化 | Tokenization that represents text through byte-level pieces. | 在更底层按字节相关片段处理文字。 |
| subword piece | 子词片段 | A token representing part of a word. | 一个单词被拆出来的一部分。 |
| special token | 特殊词元 | A reserved token with a control or structural role. | 不是普通文字、而是用于控制流程的词元。 |
| reserved token | 保留词元 | A token reserved for a specific system purpose. | 系统预留给特定用途的词元。 |
| padding token | 填充词元 | A token used to make sequences the same length. | 为了补齐长度而加入的特殊词元。 |
| unknown token | 未知词元 | A token used when text cannot be represented directly. | 分词器无法直接表示某段文字时使用的占位词元。 |
| out-of-vocabulary token | 词表外词元 | A token for text not covered by the vocabulary. | 词表里没有对应表示的文字单位。 |
| end-of-sequence token | 序列结束词元 | A token marking the end of a sequence. | 告诉模型一串内容已经结束的特殊词元。 |
| beginning-of-sequence token | 序列开始词元 | A token marking the beginning of a sequence. | 告诉模型一串内容开始的特殊词元。 |
| token count | 词元数量 | The number of tokens representing text. | 一段文字被切成了多少个词元。 |
| token length | 词元长度 | The length of text measured in tokens. | 用词元数量表示文字有多长。 |
| context window | 上下文窗口 | The amount of tokenized input a model can process at once. | 模型一次能看到和处理的词元范围。 |
| context length | 上下文长度 | The maximum or available token sequence length. | 一次输入最多能包含多少词元。 |
| token budget | 词元预算 | A limit on the number of tokens used or generated. | 一次请求能使用或生成的词元数量限制。 |
| token cost | 词元成本 | A cost measured or charged per token. | 按词元数量计算的使用成本。 |
| token efficiency | 词元效率 | How compactly text is represented in tokens. | 同样意思需要多少词元来表示。 |
| language-dependent tokenization | 依语言而变的词元化 | Tokenization behavior that differs across languages. | 不同语言可能被切成不同数量和形式的词元。 |
| multilingual tokenization | 多语言词元化 | Tokenization across multiple languages. | 同一个分词器处理多种语言的方式。 |
| Unicode text | Unicode 文本 | Text represented using the Unicode character standard. | 用统一字符编码表示的多种语言文字。 |
| Unicode normalization | Unicode 规范化 | Standardizing equivalent Unicode representations. | 把看起来相同但编码不同的文字统一起来。 |
| encoding | 编码 | Representing information in a defined machine-readable form. | 按规则把信息表示成计算机能处理的形式。 |
| decoding | 解码 | Converting a machine representation back into text. | 把模型内部表示还原成人能读的文字。 |
| detokenization | 反词元化；词元还原 | Converting tokens back into readable text. | 把词元重新拼回文字。 |
| token-to-text conversion | 词元到文本转换 | Turning token pieces or IDs back into text. | 把词元或编号还原成文字。 |
| text-to-token conversion | 文本到词元转换 | Turning text into token pieces. | 把原始文字转换成词元。 |
| text-to-ID conversion | 文本到 ID 转换 | Turning text into numeric token IDs. | 把文字变成代表词元的数字编号。 |
| token vocabulary | 词元词表 | The set of tokens available to a tokenizer. | 分词器可以使用的全部词元集合。 |
| vocabulary size | 词表大小 | The number of entries in a tokenizer vocabulary. | 词表里一共有多少种词元。 |
| tokenizer implementation | 分词器实现 | The concrete software that applies tokenization rules. | 真正执行切分和编号的软件。 |
| tokenizer model | 分词器模型 | The algorithm or learned system that determines token pieces. | 决定如何切分文字的分词算法或模型。 |
| tokenization algorithm | 词元化算法 | A procedure for converting text into tokens. | 把文本转换成词元的一套计算方法。 |
| Byte Pair Encoding | 字节对编码；BPE | A common subword tokenization algorithm. | 通过合并常见片段来形成词元的算法。 |
| BPE | 字节对编码 | Short name for Byte Pair Encoding. | Byte Pair Encoding 的缩写。 |
| WordPiece | WordPiece 子词算法 | A subword tokenization method. | 一种把词拆成子词片段的分词方法。 |
| Unigram tokenizer | Unigram 分词器 | A tokenizer approach that selects token pieces from a vocabulary. | 从候选词元词表中选择合适片段的分词方法。 |
| model input preparation | 模型输入准备 | Preparing text as token IDs before model processing. | 在模型计算前把文字切分、编号并整理好。 |
| preprocessing | 预处理 | Preparation performed before the main model operation. | 在正式模型处理前先做的准备工作。 |
| input representation | 输入表示 | The representation of user text sent into a model. | 用户文字进入模型前的表示形式。 |
| machine representation | 机器表示 | A representation suitable for computational processing. | 适合计算机处理的形式。 |
| tokenization pipeline | 词元化管线 | The sequence of steps from text to token IDs. | 从文字到词元编号的一整套步骤。 |
| pipeline step | 管线步骤 | One stage in a multi-stage processing flow. | 整个处理流程中的一个阶段。 |
| process node | 流程节点 | A named stage in the tokenization flow. | 流程图中代表一个动作或状态的节点。 |
| input stage | 输入阶段 | The stage where the system receives text. | 系统接收原始文字的阶段。 |
| tokenization stage | 词元化阶段 | The stage where text is divided into token pieces. | 把文本切成词元片段的阶段。 |
| ID mapping stage | ID 映射阶段 | The stage where token pieces receive numeric IDs. | 给每个词元分配数字编号的阶段。 |
| model-processing stage | 模型处理阶段 | The stage where the model consumes token IDs. | 模型真正接收词元编号并计算的阶段。 |
| tokenized input | 已词元化输入 | Input text after conversion into tokens. | 已经切成词元的输入文字。 |
| numeric token input | 数字化词元输入 | Model input represented as token IDs. | 用数字编号表示的模型输入。 |
| input sequence | 输入序列 | An ordered set of input units. | 按顺序排列的输入单位。 |
| output text | 输出文本 | Readable text produced after processing. | 模型处理后给用户看到的文字。 |
| readable text | 可读文本 | Text that humans can read directly. | 人可以直接阅读的文字。 |
| model-generated text | 模型生成文本 | Text produced by a language model. | 语言模型生成出来的文字。 |
| related concept | 相关概念 | A concept connected to tokenization. | 与词元化直接相关、可以继续学习的概念。 |
| tokens, context and inference | 词元、上下文与推理 | A topic area connecting tokens with model processing. | 把词元、模型能看到的内容和推理过程放在一起理解的主题。 |
| inference | 推理 | Model processing that produces an output from input. | 模型用输入计算并给出结果的过程。 |
| model inference | 模型推理 | Running a trained model on tokenized input. | 把词元化输入交给模型计算结果。 |
| Large Language Models | 大型语言模型 | Language models that process tokenized text. | 能处理词元化文字的大型语言模型。 |
| LLM | 大型语言模型 | Abbreviation for Large Language Model. | Large Language Model 的缩写。 |
| context-window relationship | 与上下文窗口的关系 | The connection between token count and available model context. | 词元数量会影响模型一次能处理的上下文范围。 |
| tokenization misconception | 词元化误解 | An incorrect assumption about how tokenization works. | 对词元化工作方式的错误理解。 |
| misconception | 误解 | A belief that is not accurate. | 看起来合理但其实不准确的理解。 |
| direct space splitting | 直接按空格切分 | Splitting only at spaces rather than using tokenizer rules. | 只遇到空格才切开，不能代表真正的词元化。 |
| word-level assumption | 以单词为单位的假设 | The assumption that every token is a whole word. | 误以为一个词元一定就是一个完整单词。 |
| tokenizer-model distinction | 分词器与模型的区别 | The distinction between converting text and processing token IDs. | 分词器负责切分和编号，模型负责处理这些输入。 |
| component boundary | 组件边界 | The boundary between tokenizer work and model work. | 区分分词器做什么、语言模型做什么。 |
| tokenizer output | 分词器输出 | Token pieces or IDs produced by a tokenizer. | 分词器处理后得到的词元片段或编号。 |
| language-model input ID | 语言模型输入 ID | An ID passed from the tokenizer to the model. | 分词器交给语言模型的数字编号。 |
| video explainer | 视频讲解 | An explanatory video about tokenization. | 用视频解释词元化的内容。 |
| independent explainer | 独立讲解内容 | An explainer separate from the page's main text. | 页面正文之外的独立解释材料。 |
| video metadata | 视频元信息 | Information describing a video asset. | 描述视频是否可用等信息。 |
| unavailable video | 暂不可用视频 | A video that is not currently available. | 页面标明目前还没有的视频。 |

## Potential Missing Concepts

- Tokenizer internals, token boundaries, vocabulary lookup, and the difference between a tokenizer algorithm and a tokenizer implementation.
- Subword tokenization methods such as Byte Pair Encoding (BPE), WordPiece, and Unigram; the page does not name a specific algorithm.
- Character, byte-level, whitespace, and whole-word tokenization as alternative strategies.
- Special tokens: beginning-of-sequence, end-of-sequence, padding, unknown, separator, and mask tokens.
- Out-of-vocabulary handling, unknown-token behavior, vocabulary size, and tokenizer coverage.
- Encoding, decoding, detokenization, reverse mapping from token IDs to readable text, and Unicode normalization.
- Token count, token length, context length, context-window limits, truncation, token budgets, and cost per token.
- Tokenization differences across languages, multilingual text, whitespace, newline characters, emojis, punctuation, and non-Latin scripts.
- Model input preparation, batching and padding, attention masks, position information, and the interface between token IDs and embeddings.
- Token embeddings and the distinction between token IDs as discrete identifiers and embeddings as continuous vectors.
- Common tokenizer file artifacts such as vocabulary files, merge rules, special-token maps, and tokenizer configuration.
- Metrics that can be associated with tokenization work: token count, compression ratio, average characters per token, and unknown-token rate; none is defined on the page.
- The page does not explain how token IDs become embeddings, how a model consumes them, or how generated token IDs are decoded back into text.

## Aliases / Synonyms

- Tokenization / tokenisation / text tokenization / token splitting / text splitting
- Token / text token / language token / token unit / token piece
- Tokenizer / text tokenizer / tokenization component / tokenization tool
- Token ID / token identifier / token number / vocabulary ID
- Token IDs / token-ID sequence / numeric token representation / tokenized input
- Text unit / language unit / processing unit / model-readable unit
- Token sequence / input sequence / tokenized sequence / model input sequence
- Tokenizer vocabulary / token vocabulary / vocabulary / token list
- Split the text / divide text / segment text / break text into pieces
- Token pieces / subword pieces / text pieces / smaller units
- Model input / language-model input / tokenized input / numeric token input
- Model output / output text / generated text / readable output
- Text-to-token conversion / tokenization / text segmentation
- Text-to-ID conversion / token ID mapping / token encoding
- Token-to-text conversion / detokenization / decoding
- Whole word / full word / word-level unit
- Part of a word / subword / word fragment / subword piece
- Punctuation / punctuation mark / non-word text unit
- Splitting by spaces / space-based splitting / whitespace splitting
- Tokenization rules / tokenizer rules / token boundary rules
- Tokenization flow / tokenization pipeline / text-to-ID pipeline
- Context window / context length / available token context
- Language model / LM / large language model / LLM
- AI product / AI application / model-powered product
- ID / identifier / numeric label / index
- Puzzle pieces / puzzle-piece analogy / cut-up sentence analogy
- Inference / model inference / model processing
- Related concepts / connected concepts / next concepts to explore

## Do Not Confuse Candidates

| Candidate A | Candidate B | Difference to preserve |
|---|---|---|
| Tokenization | Splitting by Spaces | Tokenization follows a tokenizer's rules; splitting by spaces only separates text at spaces. |
| Token | Word | A token may be a whole word, part of a word, punctuation, or another text unit; a word is a human-language unit. |
| Token | Token ID | A token is a text unit; a token ID is the number used to represent that token. |
| Token | Token piece | In this page's usage they are closely related, but a token piece emphasizes the fragment produced by the tokenizer. |
| Tokenizer | Language Model | A tokenizer converts text into pieces and IDs; a language model processes those inputs. |
| Tokenizer | Tokenization | A tokenizer is the component or tool; tokenization is the process it performs. |
| Tokenizer vocabulary | Language-model vocabulary | A tokenizer vocabulary is the set of units it can map; a model's broader learned behavior is not identical to the vocabulary list. |
| Token ID | Vocabulary ID | In this page's flow, a token ID is the numeric representation assigned from the tokenizer vocabulary; vocabulary ID is a common near-synonym. |
| Token sequence | Token-ID sequence | A token sequence contains token units; a token-ID sequence contains their numeric representations. |
| Text | Token | Text is the original human-readable material; a token is one processing unit created from it. |
| Raw text | Tokenized input | Raw text has not been converted into token units; tokenized input has. |
| Whole word | Part of a word | A whole-word token covers an entire word; a part-of-word token covers only a fragment. |
| Punctuation | Word | Punctuation can be a token even though it is not a word. |
| Model input | User input | User input is what the person enters; model input is the representation actually passed to the model, such as token IDs. |
| Model input | Tokenizer output | Tokenizer output is produced before the model receives it; model input is the downstream input consumed by the model. |
| Output text | Token IDs | Output text is readable language; token IDs are numeric representations used inside the processing flow. |
| Encoding | Tokenization | Tokenization creates text units; encoding is a broader term for representing information in a machine-readable form. |
| Decoding | Detokenization | Decoding is a broader conversion from a machine representation; detokenization specifically reconstructs text from tokens. |
| Tokenization | Detokenization | Tokenization goes from text to tokens; detokenization goes from tokens back to text. |
| Tokenization | Embedding | Tokenization creates discrete token units or IDs; embedding maps tokens into learned numeric vectors. |
| Vocabulary | Context Window | A vocabulary is the set of possible token units; a context window is the amount of tokenized input processed at once. |
| Context Window | Token Budget | A context window is the model's available input capacity; a token budget is a configured usage limit and may cover input, output, or both. |
| Token Count | Token Length | Both concern the number of tokens, but token count emphasizes counting and token length emphasizes sequence size. |
| Token Cost | Token Count | Token count measures quantity; token cost measures the price or resource impact associated with that quantity. |
| Inference | Tokenization | Inference is the model's processing of input to produce output; tokenization is the preparation of text before that processing. |
| Chat Assistant | Language Model | A chat assistant is a user-facing system or product; a language model is the model component processing language. |
| AI Product | Language Model | An AI product can include a model plus interface and surrounding systems; a language model is one model type. |
| AI | LLM | AI is the broad field; an LLM is one language-focused model category. |
| Tokenizer Rules | Language Rules | Tokenizer rules define computational token boundaries; language rules describe how people use a language. |
| Token Boundary | Word Boundary | A token boundary is set by the tokenizer; a word boundary is a linguistic distinction and may not align with it. |
| Whole-word Tokenization | Subword Tokenization | Whole-word tokenization keeps words intact when possible; subword tokenization can split a word into smaller pieces. |
| Subword Tokenization | Character Tokenization | Subword tokenization uses larger learned or rule-based pieces; character tokenization uses individual characters. |
| Whitespace Tokenization | Tokenization | Whitespace tokenization uses spaces or other whitespace as boundaries; general tokenization may also split words, punctuation, and other units. |
| BPE | Tokenizer | BPE is one tokenization algorithm; a tokenizer is the broader component that applies an algorithm and configuration. |
| Special Token | Ordinary Text Token | A special token has a structural or control role; an ordinary text token represents user text. |
| Unknown Token | Tokenizer Vocabulary | An unknown token represents text that is not directly covered; the vocabulary is the set of covered entries. |
| Padding Token | Text Token | A padding token is inserted for structural alignment; a text token represents content from the input. |
| Token ID | Parameter | A token ID represents input text; a parameter is a learned value inside the model. |
| Token | Parameter | A token is input or output data; a parameter is part of the model's learned internal state. |
| Tokenizer | Embedding Layer | The tokenizer operates before the model and produces IDs; the embedding layer turns IDs into learned vectors inside the model. |
| Model-Readable Unit | Human-Readable Word | A model-readable unit is defined by processing rules; a human-readable word is a linguistic unit and may not match it. |
| Model Output | Verified Fact | Generated model output is not automatically a verified fact or a database record. |
| Video Explainer | Page Body | The page body is the source used for this extraction; the video is marked unavailable and was not used as a separate source. |

## Notes

- Primary extraction source: the complete body of `tokenization.html`, including the definition, puzzle-piece analogy, five process cards, tokenization flow diagram, real-world examples, misconception cards, related-concept map, takeaway, and video metadata.
- The page's central definition is that tokenization converts text into tokens.
- The page explicitly says a token can be a whole word, part of a word, punctuation, or another text unit, depending on the tokenizer.
- The page explicitly warns that a token is not always the same thing as a word.
- The page's process is: Text → Tokenizer → Token Pieces → Token IDs → Model Input.
- The page explicitly says token IDs are mapped from the tokenizer vocabulary and then sent into the model as input.
- The page uses “unbelievable” as an example and says a tokenizer may represent it as one token or several pieces, depending on the tokenizer.
- The page explicitly distinguishes tokenization from splitting by spaces, token from word, and tokenizer from language model.
- The page links tokenization to Tokens, Context Window, Inference, Large Language Models, and KV Cache; these are related concepts, not all fully defined on this page.
- The page does not define a specific tokenizer algorithm, tokenization metric, special-token scheme, encoding format, or embedding step. Those items are retained as raw candidates under Potential Missing Concepts and in the main table for later verification.
- No external source or unavailable video was used for this extraction.
- Candidates intentionally retain near-duplicates, aliases, process phrases, examples, abbreviations, and potentially overlapping concepts; downstream review may normalize them later.
