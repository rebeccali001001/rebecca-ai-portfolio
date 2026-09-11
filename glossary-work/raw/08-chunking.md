# Topic

Chunking

## Topic Metadata

- Requested Module: 08
- Page Module: 08 · Embeddings, Search & RAG
- Page Topic: Topic 01 · Chunking
- Topic Title: What is Chunking?
- Source File: `chunking.html`
- Source Page Description: Chunking splits large documents or data into smaller pieces that are easier to search and retrieve.
- Collection Mode: Raw, maximum candidate collection; candidates are intentionally not deduplicated, merged, or reduced.

## Glossary Candidates

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Chunking | 分块；切块 | Splitting large content into smaller pieces for search and retrieval. | 把大段内容切成较小的部分，方便搜索和取回。 |
| chunk | 块；分块内容 | A smaller piece of content used as a retrieval unit. | 从大资料中切出来、以后可以被找回的一小段内容。 |
| chunks | 多个块；多个分块 | Multiple smaller pieces created from larger content. | 从大资料切出来的多个小部分。 |
| document | 文档；文件 | A source of content that can be prepared and split. | 一份可以交给系统处理和切分的资料。 |
| documents | 文档；文件 | Multiple sources of content. | 多份可以被处理的资料。 |
| data | 数据 | Information that can be divided into smaller pieces. | 可以被系统处理、搜索或取回的信息。 |
| large document | 大型文档 | A document that may be too large to handle as one retrieval unit. | 内容很多、不适合整份拿来检索的文档。 |
| large documents | 大型文档 | Documents containing a large amount of content. | 内容量较大的多份文档。 |
| large data | 大量数据 | Data that may be easier to handle after splitting. | 数据很多、切开后更容易处理的数据。 |
| large content | 大量内容 | Content that may need to be divided into smaller pieces. | 内容很多、可能需要先分块的资料。 |
| content | 内容 | Text or other information being prepared for retrieval. | 文档或资料中真正要处理的信息。 |
| source | 来源；源资料 | The original material from which chunks are made. | 分块之前的原始资料。 |
| source content | 来源内容；原始内容 | The original content preserved through chunking. | 被切分但仍作为依据保留的原始内容。 |
| source material | 原始资料 | The material that supplies the content for a chunk. | 提供分块内容的原始文件或资料。 |
| smaller piece | 更小的部分 | A piece smaller than the original document or data. | 比原始大资料更小的一部分。 |
| smaller pieces | 更小的部分；小片段 | Pieces created by dividing a larger source. | 把大资料切开后得到的多个小片段。 |
| smaller unit | 更小的单元 | A smaller unit into which content is divided. | 大内容被拆成的较小单位。 |
| smaller units | 更小的单元 | Multiple smaller units made from content. | 从大资料中拆出的多个小单位。 |
| unit | 单元；单位 | One piece treated as a unit for a task. | 系统把一部分资料当作一个整体处理。 |
| retrieval unit | 检索单元 | A content unit that can be searched for and returned. | 搜索系统可以找到并返回的一段内容。 |
| retrievable piece | 可检索片段 | A piece that can be retrieved by a search system. | 可以被搜索系统取回的内容片段。 |
| retrievable pieces | 可检索片段 | Pieces prepared so a system can retrieve them. | 已准备好、可以被系统找回的多个片段。 |
| manageable | 易管理的；易处理的 | Easy enough for a system to handle. | 对系统来说大小合适、容易处理。 |
| relevant | 相关的 | Closely connected to a question or task. | 和当前问题或任务关系密切。 |
| search | 搜索 | Looking for useful content. | 在资料中寻找有用内容。 |
| retrieve | 检索；取回 | Find and return useful content. | 找到并把相关内容取回来。 |
| retrieval | 检索；取回 | The process of finding and returning relevant content. | 从资料中找出并返回相关内容的过程。 |
| search and retrieve | 搜索并检索 | Search for content and return the useful pieces. | 先搜索，再取回有用的内容片段。 |
| retrieval system | 检索系统 | A system that searches for and returns relevant pieces. | 负责查找和返回相关资料片段的系统。 |
| search system | 搜索系统 | A system that finds content related to a question. | 根据问题寻找相关内容的系统。 |
| search index | 搜索索引 | An index prepared so content can be searched. | 为了快速查资料而建立的内容目录。 |
| index | 索引；建立索引 | A searchable structure containing prepared content. | 让系统可以快速查找资料的结构或目录。 |
| indexing | 建立索引；索引化 | Preparing content for search by adding it to an index. | 把内容放进可搜索目录的过程。 |
| before search | 搜索之前 | The stage before a search is performed. | 系统真正开始查找之前的阶段。 |
| before indexing | 建立索引之前 | The stage before content is added to an index. | 内容放进索引之前的阶段。 |
| before search or indexing | 搜索或建立索引之前 | The preparation stage before search or indexing. | 搜索或建立目录前先准备资料的阶段。 |
| paragraph | 段落 | A possible unit used for a chunk. | 可以直接作为一个分块的文字段落。 |
| paragraphs | 段落 | Multiple possible text units used as chunks. | 可以被当作分块的多个文字段落。 |
| section | 章节；部分 | A structural part of a document that can be a chunk. | 文档中有结构意义的一部分，也可以作为分块。 |
| sections | 章节；部分 | Multiple structural parts of a document. | 文档中的多个章节或结构部分。 |
| fixed token range | 固定 token 范围 | A chunk boundary based on a fixed number or range of tokens. | 按固定数量的 token 来划分内容的范围。 |
| token | token；词元 | A model-readable unit of text. | 模型读取文字时使用的基本文字单位。 |
| tokens | tokens；词元 | Multiple model-readable text units. | 模型读取文字时使用的多个基本单位。 |
| token range | token 范围 | A range of tokens selected as a content unit. | 从文字中选出的一段 token 范围。 |
| model-readable text unit | 模型可读文字单位 | A text unit that a model can process. | 模型能够读取和处理的文字单位。 |
| semantic block | 语义块 | A content block formed around a coherent meaning. | 围绕完整含义划出的内容块。 |
| semantic blocks | 语义块 | Multiple meaning-based content blocks. | 按含义划出的多个内容块。 |
| semantic | 语义的 | Related to meaning rather than only surface form. | 关注内容含义的，而不只是表面文字的。 |
| structural | 结构性的 | Based on the organization of a document. | 根据文档的章节、标题等组织结构来划分的。 |
| fixed | 固定的 | Set according to a predetermined size or rule. | 按预先规定的大小或规则进行的。 |
| boundary | 边界；分界线 | A point that determines where one piece ends and another begins. | 决定一块内容在哪里结束、下一块在哪里开始的位置。 |
| boundaries | 边界；分界线 | Multiple points used to divide content. | 用来切分内容的多个分界位置。 |
| choose boundaries | 选择边界 | Decide where content should be split. | 决定资料应该从哪里切开。 |
| fixed boundaries | 固定边界 | Boundaries selected using a fixed rule or size. | 按固定规则或大小决定的分界线。 |
| structural boundaries | 结构边界 | Boundaries based on document structure. | 按标题、章节等文档结构决定的分界线。 |
| semantic boundaries | 语义边界 | Boundaries based on changes in meaning. | 根据内容含义是否完整来决定的分界线。 |
| chunking strategy | 分块策略 | The method used to decide how content is split. | 决定资料如何切开的方法。 |
| strategy | 策略 | A chosen method for preparing content. | 系统处理资料时采用的办法。 |
| choose a strategy | 选择策略 | Select a method for splitting content. | 选择一种切分资料的方式。 |
| fixed strategy | 固定策略 | A strategy based on predetermined sizes or rules. | 按预先规定大小或规则切分的办法。 |
| structural strategy | 结构策略 | A strategy that follows document organization. | 跟着文档章节、标题等结构切分的办法。 |
| semantic strategy | 语义策略 | A strategy that follows coherent meaning. | 按内容含义和主题完整性切分的办法。 |
| split | 分割；切分 | Divide content into smaller pieces. | 把一份大资料拆成小部分。 |
| splits | 切分；分割 | Divides content into smaller pieces. | 把内容切成更小的部分。 |
| splitting | 切分；分割 | The act of dividing content. | 把大内容拆开的动作或过程。 |
| divide | 划分；分开 | Separate a source into smaller units. | 把原始资料分成几个更小的单位。 |
| divides | 划分；分开 | Separates content into units. | 把内容分成不同单位。 |
| divided content | 已划分内容 | Content that has been separated into smaller units. | 已经被拆成多个小部分的内容。 |
| create chunks | 创建分块 | Make smaller retrievable pieces from content. | 从资料中生成可以检索的小片段。 |
| create a chunk | 创建一个分块 | Make one smaller retrieval unit. | 生成一个可以检索的内容块。 |
| chunk creation | 分块创建 | The process of making chunks. | 生成多个内容分块的过程。 |
| split content | 切分内容 | Divide the source content into pieces. | 把原始内容拆成多个部分。 |
| split large content | 切分大内容 | Divide a large source into smaller units. | 把大量内容拆成较小单位。 |
| content division | 内容划分 | Separation of content into smaller units. | 将内容分成多个小部分。 |
| prepare content | 准备内容 | Process content so it can be searched or indexed. | 先处理内容，让它之后能被搜索或建立索引。 |
| content preparation | 内容准备 | The preparation stage before search or indexing. | 搜索或建立索引前处理资料的阶段。 |
| prepare for search | 为搜索做准备 | Organize content so a search system can use it. | 整理内容，让搜索系统能够使用。 |
| prepare for indexing | 为建立索引做准备 | Organize content before adding it to an index. | 把内容整理好，准备放入索引。 |
| document preparation | 文档准备 | Preparing a document for retrieval. | 为了检索而先处理文档。 |
| start with content | 从内容开始 | Begin the workflow with a document or source. | 流程先从一份文档或其他资料开始。 |
| start with a document | 从文档开始 | Use a document as the initial input. | 把文档作为流程的起点。 |
| source is ready to prepare | 来源已准备好处理 | The source is available for preparation. | 原始资料已经可以交给系统处理。 |
| ready to prepare | 准备处理 | Available to be processed by the workflow. | 已经可以开始处理。 |
| process | 处理；流程 | An ordered set of steps for preparing and retrieving content. | 按顺序处理资料的一连串步骤。 |
| workflow | 工作流程 | The sequence from source content to retrieved pieces. | 从原始资料到取回结果的完整步骤。 |
| process flow | 流程 | The ordered sequence of processing stages. | 按顺序排列的处理步骤。 |
| process step | 流程步骤 | One stage in the workflow. | 工作流程中的一个环节。 |
| step | 步骤 | One action in an ordered process. | 一连串操作中的一个动作。 |
| Document | 文档 | Step 1: begin with a document or other source. | 第一步，准备一份文档或其他原始资料。 |
| document step | 文档步骤 | The first process step that supplies the content. | 流程中提供原始内容的第一步。 |
| Strategy | 策略 | Step 2: choose how boundaries will be selected. | 第二步，选择怎样划分内容边界。 |
| strategy step | 策略步骤 | The process step for choosing a chunking method. | 选择分块方法的流程步骤。 |
| Split | 切分 | Step 3: divide the content into chunks. | 第三步，把内容切成多个分块。 |
| split step | 切分步骤 | The process step that creates smaller pieces. | 生成更小内容片段的流程步骤。 |
| Metadata | 元数据 | Step 4: attach useful context to chunks. | 第四步，为分块附上有用的背景信息。 |
| metadata | 元数据 | Information attached to a chunk to describe or locate it. | 附在分块旁边、用来说明或定位它的信息。 |
| metadata step | 元数据步骤 | The process step for keeping useful context. | 保留分块背景信息的流程步骤。 |
| Index | 索引 | Step 5: prepare chunks for search. | 第五步，把分块准备成可搜索的索引内容。 |
| index step | 索引步骤 | The process step that prepares chunks for search. | 为搜索准备分块的流程步骤。 |
| Retrieve | 检索；取回 | Step 6: find pieces related to a question. | 第六步，找出和问题相关的内容片段。 |
| retrieve step | 检索步骤 | The process step that returns relevant chunks. | 返回相关分块的流程步骤。 |
| choose boundaries | 选择边界 | Select the points that separate chunks. | 选定不同分块之间的分界位置。 |
| create chunks | 创建分块 | Produce smaller units from a document. | 从文档中生成较小的内容单位。 |
| keep useful context | 保留有用上下文 | Preserve information that helps interpret a chunk. | 保留能帮助理解分块的信息。 |
| useful context | 有用上下文 | Context that makes a chunk easier to understand or use. | 让分块更容易被理解和使用的背景信息。 |
| context | 上下文；背景信息 | Information surrounding or describing a piece of content. | 帮助理解一段内容的周边信息。 |
| title | 标题 | A label that names a document or section. | 用来说明文档或章节主题的名称。 |
| titles | 标题 | Multiple labels naming documents or sections. | 多个文档或章节的名称。 |
| source name | 来源名称 | The name of the source document or material. | 原始文档或资料的名字。 |
| source names | 来源名称 | Names identifying source materials. | 用来标识原始资料的多个名称。 |
| position | 位置 | The location of a chunk within its source. | 分块在原文档中的位置。 |
| positions | 位置 | Locations of chunks within their sources. | 分块在原始资料中的多个位置。 |
| other metadata | 其他元数据 | Additional information attached to a chunk. | 除标题、来源和位置外附加的其他信息。 |
| attach metadata | 附加元数据 | Add descriptive information to a chunk. | 给分块加上说明它的信息。 |
| attach useful context | 附加有用上下文 | Add context that helps interpret a chunk. | 给分块补充有助于理解的背景信息。 |
| embed | 生成嵌入 | Convert a chunk into a numerical representation. | 把分块转换成可以比较的数字表示。 |
| embedded | 已生成嵌入 | Represented as numbers for comparison or search. | 已经被转换成数字表示、可以比较或搜索。 |
| embedding | 嵌入；向量表示 | A numerical representation used for comparison. | 把内容变成一串可比较数字的表示。 |
| embeddings | 嵌入表示；向量表示 | Numerical representations of content. | 多段内容对应的数字表示。 |
| embedding process | 嵌入过程 | The process of converting content into numerical representations. | 把内容转成数字表示的过程。 |
| add to an index | 加入索引 | Put prepared chunks into a searchable index. | 把处理好的分块放进搜索目录。 |
| added to a search index | 加入搜索索引 | Included in an index so a system can search it. | 已放入搜索目录，系统可以查找它。 |
| prepare for search | 为搜索做准备 | Make chunks available to a search system. | 让分块能够被搜索系统使用。 |
| return chunks | 返回分块 | Give relevant chunks back to the user or next system. | 把相关分块交还给用户或后续系统。 |
| related to the question | 与问题相关 | Connected to what the user asks. | 和用户提出的问题有关系。 |
| relevant piece | 相关片段 | A chunk useful for answering a question. | 对回答问题有帮助的一段内容。 |
| relevant pieces | 相关片段 | Chunks useful for the current question. | 对当前问题有帮助的多个内容片段。 |
| useful section | 有用章节；有用部分 | A section containing information needed for an answer. | 包含回答所需信息的章节或部分。 |
| answer | 答案 | The response produced using relevant retrieved content. | 系统根据相关资料给出的回应。 |
| answer a question | 回答问题 | Use relevant content to respond to a question. | 用相关资料回应用户的问题。 |
| user's question | 用户的问题 | The question used to request information. | 用户希望系统解答的提问。 |
| question | 问题 | A request for information used to retrieve content. | 用来查找资料的信息请求。 |
| query | 查询 | A request used to search for relevant content. | 交给搜索系统、用来找资料的请求。 |
| search query | 搜索查询 | A query sent to a search system. | 发给搜索系统的查找请求。 |
| retrieval query | 检索查询 | A query used to retrieve relevant chunks. | 用来找回相关分块的查询。 |
| useful section for a question | 对问题有用的部分 | A section that contains information relevant to a question. | 对某个问题有帮助的章节或内容。 |
| carry the whole textbook | 搬着整本教科书 | A metaphor for using an entire large source at once. | 比喻把整本大资料都带进回答，而不是只取相关部分。 |
| textbook | 教科书 | A long source that can be split into sections or cards. | 可以被切成多个部分来查找的长篇资料。 |
| large textbook | 大型教科书 | A large document used in the chunking analogy. | 用来比喻大文档的厚重资料。 |
| index card | 索引卡片 | A small card representing one useful piece of a larger source. | 把大资料的一小段写在卡片上的比喻。 |
| index cards | 索引卡片 | Multiple small cards made from a larger textbook. | 把大资料切成多个小片段的比喻。 |
| cut a large textbook into index cards | 把大教科书切成索引卡片 | An analogy for splitting a large source into retrievable pieces. | 用卡片比喻把大文档切成能单独找回的小块。 |
| analogy | 类比；比喻 | An explanation that compares chunking with cutting a textbook into cards. | 用熟悉的切卡片来帮助理解分块。 |
| useful card | 有用卡片 | A card containing the section needed for a question. | 恰好包含问题所需信息的小卡片。 |
| whole textbook | 整本教科书 | The complete large source before selecting relevant pieces. | 还没有挑出相关片段的完整大资料。 |
| instead of | 而不是 | Used to contrast retrieving a piece with using the whole source. | 表示选择一种做法，而不采用另一种做法。 |
| real-world example | 现实世界例子 | An example showing chunking in a practical setting. | 展示分块在真实场景中怎么用的例子。 |
| everyday example | 日常例子 | The textbook example used to explain chunking simply. | 用日常熟悉的教科书来说明分块。 |
| business example | 商业例子 | The company policy-search example. | 用企业资料搜索来说明分块。 |
| input | 输入 | The document or data given to the system. | 送进系统、准备被处理的资料。 |
| Input | 输入 | A label for the material entering an example workflow. | 示例流程中进入系统的原始资料。 |
| output | 输出 | The content returned by the system. | 系统处理后返回的结果。 |
| Output | 输出 | A label for the result returned in an example. | 示例中系统最后给出的结果。 |
| system | 系统 | The software that splits, indexes, or retrieves content. | 负责处理、搜索和返回资料的软件系统。 |
| System | 系统 | A label for the software action in an example. | 示例中执行切分或检索动作的软件。 |
| long textbook | 长篇教科书 | The input in the everyday chunking example. | 日常示例中需要被切分的长资料。 |
| splits it by useful sections | 按有用章节切分它 | The system divides a textbook according to useful sections. | 系统按照有意义的章节把教科书切开。 |
| relevant sections | 相关章节；相关部分 | Sections selected because they help answer a question. | 因为和问题有关而被选出的部分。 |
| few relevant sections | 少量相关部分 | Only a small number of useful sections returned from a long source. | 从长资料中只取出少数有用部分。 |
| company handbook | 公司手册 | A business document used as chunking input. | 企业内部用来查政策的员工手册。 |
| handbook | 手册 | A structured document containing policies or guidance. | 集中记录规则、政策或说明的资料。 |
| policy search | 政策搜索 | Searching company policies to answer an employee question. | 在公司政策资料中查找员工需要的规则。 |
| policy | 政策；规定 | A rule or guidance passage in a company handbook. | 公司规定或指导员工行为的一段内容。 |
| policies | 政策；规定 | Multiple rules or guidance passages. | 多条公司规则或政策内容。 |
| chunk policies | 将政策分块 | Divide policy content into searchable pieces. | 把政策资料切成方便搜索的小段。 |
| policy passage | 政策段落 | The policy text relevant to an employee question. | 和员工问题有关的一段政策文字。 |
| relevant policy passage | 相关政策段落 | The policy passage returned for a question. | 搜索后返回、能回答问题的政策段落。 |
| page metadata | 页码元数据 | Metadata recording page information for a chunk. | 记录分块来自哪一页的信息。 |
| page | 页；页面 | A location within a document used as metadata. | 文档中可以标记来源位置的一页。 |
| employee question | 员工问题 | A question answered using a company policy passage. | 员工希望根据公司政策得到回答的问题。 |
| handbook search | 手册搜索 | Finding a relevant passage in a company handbook. | 在公司手册中查找相关规定。 |
| title metadata | 标题元数据 | Metadata that keeps the title associated with a chunk. | 和分块一起保留的标题信息。 |
| source metadata | 来源元数据 | Metadata that identifies where a chunk came from. | 说明分块来自哪份原始资料的信息。 |
| position metadata | 位置元数据 | Metadata that records where a chunk occurs in its source. | 记录分块在原文档中位置的信息。 |
| Chunk ≠ Token | 分块不等于 token | A chunk is a larger retrieval unit, while a token is model-readable text. | 分块是较大的检索单位，token 是模型读取文字的小单位。 |
| chunk versus token | 分块与 token 的区别 | The distinction between a retrieval unit and a model text unit. | 区分检索用的分块和模型用的文字单位。 |
| larger retrieval unit | 较大的检索单位 | A paragraph or section used as a searchable piece. | 例如段落或章节这种较大的可检索内容。 |
| model-readable unit | 模型可读单位 | A text unit that a model reads and processes. | 模型理解文字时采用的单位。 |
| Chunking ≠ Embedding | 分块不等于嵌入 | Chunking divides content; embedding represents it as numbers. | 分块是切资料，嵌入是把资料变成数字。 |
| embedding as numbers | 以数字形式表示的嵌入 | Representing content numerically for comparison. | 把内容变成数字，以便比较。 |
| represent content as numbers | 把内容表示成数字 | Convert content into numerical form. | 把一段内容转换成数字表示。 |
| numbers for comparison | 用于比较的数字 | Numerical values used to compare represented content. | 用来判断内容是否相近的一串数字。 |
| compare content | 比较内容 | Examine represented content for similarity or difference. | 看不同内容之间是否相似或有差别。 |
| Chunking ≠ Summarization | 分块不等于摘要 | Chunking keeps source pieces; summarization rewrites them shorter. | 分块保留原文片段，摘要则重新写成更短内容。 |
| summarization | 摘要；总结 | Rewriting content in a shorter form. | 把原内容重新概括成更短的文字。 |
| rewrite content | 重写内容 | Express content again in a changed form. | 用新的说法重新表达原内容。 |
| shorter form | 更短形式 | A condensed form of the original content. | 比原文更短的表达方式。 |
| preserve source pieces | 保留来源片段 | Keep pieces of the original source rather than rewriting them. | 保留原资料切出来的片段，不把它改写掉。 |
| original source | 原始来源 | The source content from which chunks are made. | 产生分块的原始资料。 |
| source piece | 来源片段 | A piece retained from the original source. | 从原始资料保留下来的一个片段。 |
| preserve | 保留 | Keep content available in its source form. | 不删掉或改写，继续保留原内容。 |
| rewrite | 重写 | Write content again in a shorter or changed form. | 用另一种、更短或不同的说法再写一次。 |
| summarization versus chunking | 摘要与分块的区别 | The distinction between rewriting and preserving source pieces. | 区分“改写成摘要”和“切出原文片段”。 |
| related concepts | 相关概念 | Concepts connected to chunking in the retrieval workflow. | 和分块一起构成检索流程的相关知识。 |
| concept tree | 概念链；概念树 | The sequence Document → Chunking → Embeddings → Index → Retrieval → Answer. | 从文档到答案的一条相关概念流程。 |
| Document → Chunking | 文档到分块 | The first relationship in the concept flow. | 先有文档，再把文档切成分块。 |
| Chunking → Embeddings | 分块到嵌入 | Chunks can be converted into embeddings. | 分块之后可以把内容变成嵌入表示。 |
| Embeddings → Index | 嵌入到索引 | Embeddings can be prepared in an index for search. | 嵌入表示可以被放入索引中以便搜索。 |
| Index → Retrieval | 索引到检索 | A search index supports retrieval. | 系统从索引中检索相关内容。 |
| Retrieval → Answer | 检索到答案 | Retrieved pieces can support an answer. | 取回的内容可以用来生成答案。 |
| vector database | 向量数据库 | A database commonly used to store searchable vector representations. | 常用来保存和搜索向量表示的数据库。 |
| semantic search | 语义搜索 | Search based on meaning rather than only exact words. | 按含义查找，而不只是查找完全相同的词。 |
| RAG | 检索增强生成 | A workflow that retrieves source content before generating an answer. | 先检索资料，再用资料生成答案的方法。 |
| retrieval-augmented generation | 检索增强生成 | Generating an answer using retrieved source pieces. | 先找相关资料片段，再据此生成回答。 |
| answer generation | 答案生成 | Producing a response from relevant retrieved content. | 根据检索到的内容生成回应。 |
| search preparation | 搜索准备 | Preparing chunks, metadata, and indexes for search. | 为搜索整理分块、元数据和索引。 |
| retrieval preparation | 检索准备 | Preparing content so relevant pieces can be returned. | 把资料整理成之后能取回相关片段的形式。 |
| relevant retrieval | 相关检索 | Retrieval that returns pieces related to the question. | 找回和问题真正相关的内容。 |
| answer context | 答案上下文 | Retrieved content used to support an answer. | 用来帮助回答问题的检索内容背景。 |
| What is it? | 它是什么？ | A section introducing the definition of chunking. | 用来介绍分块定义的页面部分。 |
| Think of it like... | 可以把它想成…… | A section explaining chunking through an analogy. | 用比喻帮助理解分块的页面部分。 |
| How it works | 它如何工作 | A section describing the chunking workflow. | 介绍分块流程怎样进行的页面部分。 |
| Real-world examples | 现实世界例子 | A section showing everyday and business uses. | 展示日常和商业用法的页面部分。 |
| What it is NOT | 它不是什么 | A section distinguishing chunking from related concepts. | 专门说明分块不等于哪些概念的页面部分。 |
| Remember this | 记住这一点 | A concise takeaway about chunking. | 页面最后帮助读者记住的核心结论。 |
| definition | 定义 | A concise explanation of what chunking is. | 用简单话说明分块是什么。 |
| takeaway | 核心结论 | The main point the reader should remember. | 读者最后应该记住的重点。 |
| visual explainer | 可视化讲解 | A visual explanation of the topic. | 用图像或视频辅助解释主题。 |
| video | 视频 | A media explanation for the topic. | 用来讲解主题的影像内容。 |
| video unavailable | 视频暂不可用 | The page states that a video is not available yet. | 页面说明目前还没有该主题的视频。 |

## Potential Missing Concepts

- Chunk size / chunk length: The page names several chunk forms but does not specify how large a chunk should be.
- Chunk overlap / overlap window: The page does not discuss repeating boundary context between adjacent chunks.
- Recursive character splitting: A common implementation strategy not named in the source page.
- Sentence boundary and paragraph boundary: Paragraphs are named, but sentence-level boundary rules are not explained.
- Heading-aware splitting: Titles and sections appear as metadata/structure, but heading-aware splitting is not explicitly described.
- Document loader / parser: The page starts with a ready document and does not describe how source files are loaded or parsed.
- Page-level versus section-level chunking: Sections and page metadata appear, but the trade-off between granularities is not discussed.
- Token budget: Fixed token ranges are named, but model context limits and token budgets are not explained.
- Context window: The page does not connect chunk size to a model's context window.
- Chunk quality evaluation: No method or metric is given for checking whether chunks are coherent or useful.
- Retrieval quality metrics: Precision, recall, hit rate, and nDCG are not mentioned.
- Top-k retrieval: The page says a search system returns relevant chunks but does not specify how many.
- Reranking: A second-stage ordering of retrieved chunks is not discussed.
- Hybrid retrieval: Combining lexical and semantic search is not described.
- Vector database implementation: Vector Database is linked as a related concept but not explained in the body.
- Embedding model choice: Embeddings are linked in the workflow, but model selection is not covered.
- Parent-child chunks: Hierarchical retrieval units are not covered.
- Document hierarchy: Headings and sections are implied, but nested structure is not discussed.
- Deduplication: The page does not explain how repeated or overlapping chunks are handled.
- Boundary artifacts: The page does not discuss meaning being cut across chunk boundaries.
- Metadata filtering: Metadata is attached, but filtering search results by metadata is not explained.

## Aliases / Synonyms

- Chunking / splitting / dividing content / content division / creating chunks
- Chunk / smaller piece / smaller unit / retrieval unit / retrievable piece
- Document / source / source material / source content
- Large document / large content / long textbook
- Search / search query / policy search / handbook search
- Retrieve / retrieval / search and retrieve / relevant retrieval
- Search system / retrieval system
- Index / search index / indexing / add to an index
- Paragraph / section / semantic block / retrieval unit
- Fixed token range / token range / fixed boundary
- Structural boundary / section boundary / heading-related boundary
- Semantic boundary / meaning boundary / semantic split
- Metadata / source metadata / page metadata / title metadata / position metadata
- Context / useful context / answer context
- Embed / embedding / embeddings / embedding process
- Relevant piece / relevant section / relevant policy passage
- Input / Input / source input / document input
- Output / Output / retrieved result / answer context
- Chunking strategy / strategy / fixed strategy / structural strategy / semantic strategy
- Summarization / rewrite content / shorter form
- Semantic search / search by meaning
- RAG / retrieval-augmented generation

## Do Not Confuse Candidates

- Chunk vs token: A chunk is a larger retrieval unit such as a paragraph or section; a token is a model-readable text unit.
- Chunking vs embedding: Chunking divides content; embedding represents content as numbers for comparison.
- Chunking vs summarization: Chunking preserves pieces of the source; summarization rewrites content in a shorter form.
- Chunk vs document: A document is the larger source; a chunk is one smaller piece made from it.
- Chunk vs section: A section is a structural part of a document; a chunk is any chosen retrieval unit and may or may not align with a section.
- Metadata vs content: Metadata describes or locates a chunk; content is the source passage itself.
- Index vs retrieval: An index is the prepared searchable structure; retrieval is the act of finding and returning relevant pieces.
- Search vs retrieval: Search finds candidates; retrieval emphasizes returning useful content for the current question.
- Embeddings vs vector database: An embedding is a numerical representation; a vector database is a storage/search system that may hold such representations.
- Semantic boundary vs fixed boundary: A semantic boundary follows meaning; a fixed boundary follows a predetermined size or rule.
- Structural boundary vs semantic boundary: A structural boundary follows document organization; a semantic boundary follows the coherence of meaning.
- Input vs output: Input enters the workflow; output is the result returned by the workflow.
- Source vs metadata: The source is the original material; metadata is descriptive context attached to it.
- Relevant section vs whole textbook: A relevant section is a selected useful piece; the whole textbook is the complete large source.
- Chunking vs carrying the whole textbook: Chunking retrieves only useful pieces instead of using the entire large source at once.
- RAG vs chunking: RAG is a broader retrieve-then-generate workflow; chunking is the preparation step that creates retrievable pieces.
- Summarization vs preservation: Summarization rewrites and shortens; chunking preserves source pieces.

## Notes

- The source page is beginner-oriented and intentionally defines chunking through short definitions, an index-card analogy, a six-step process, two examples, explicit misconception cards, a related-concept chain, and a takeaway.
- Candidate collection is intentionally expansive and phrase-level. Repeated terms such as `chunk`, `content`, `system`, `input`, `output`, `index`, and `retrieve` are retained in context-specific rows rather than deduplicated.
- The page explicitly names three chunk forms: paragraphs, sections, and fixed token ranges; it also names semantic blocks and fixed, structural, and semantic boundaries/strategies.
- The page explicitly names titles, source names, positions, and other metadata as context that may be attached to chunks.
- The process shown on the page is: Document → Strategy → Split → Metadata → Index → Retrieve.
- The related-concept chain shown on the page is: Document → Chunking → Embeddings → Index → Retrieval → Answer.
- The page links Embeddings, Vector Database, Semantic Search, and RAG as related concepts.
- The page says a topic video is not available yet; `video`, `visual explainer`, and `video unavailable` are retained as source-visible candidates/notes.
- No explicit quantitative metric appears in the source text; `RAG` is the only prominent abbreviation on the page and is expanded in the candidate list.
