# Topic

Embeddings

## Topic Metadata

- Requested Module: 08
- Page Module: 05 · Embeddings, RAG & Vector Search
- Page Topic: Topic 01 · Embeddings
- Topic Title: What are Embeddings?
- Source File: `embeddings.html`
- Source Page Description: Embeddings represent text or other data as numbers so a system can compare meaning or features.
- Collection Mode: Raw, maximum candidate collection; candidates are intentionally not deduplicated, merged, or reduced.

## Glossary Candidates

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| embedding | 嵌入；向量表示 | A numerical representation of data that a computer can compare. | 把文字、图片等信息变成一串电脑能比较的数字。 |
| embeddings | 嵌入表示；向量表示 | Numerical representations of items used for comparison. | 多个对象对应的数字表示。 |
| numerical representation | 数值表示 | Information represented with numbers. | 用数字表达一个东西的方式。 |
| representation | 表示；表征 | A form used to represent useful information. | 用某种形式表达信息。 |
| data representation | 数据表示 | A numerical or structured form of data. | 把原始数据换成方便计算的形式。 |
| text embedding | 文本嵌入 | An embedding of text. | 把文字转换成数字表示。 |
| image embedding | 图像嵌入 | An embedding of an image. | 把图片转换成数字表示。 |
| product embedding | 产品嵌入 | An embedding of a product or product description. | 把商品或商品描述转换成可比较的数字。 |
| vector | 向量 | A list of numbers representing an item. | 一串按顺序排列、用来表示对象的数字。 |
| vector representation | 向量表示 | A representation stored as a vector. | 用一串数字表示文字、图片或其他对象。 |
| vector space | 向量空间 | The space in which vectors are represented and compared. | 放置这些数字向量、方便比较它们关系的数学空间。 |
| representation space | 表示空间 | The chosen space where items are mapped as vectors. | 模型把对象放进去并比较位置的“数字地图”。 |
| map items into a vector | 将对象映射为向量 | Convert each item into a vector in a representation space. | 把每个对象变成一串数字并放到数字空间里。 |
| map | 映射 | Convert or place an item into another representation. | 按模型规则把东西转换到另一种形式。 |
| item | 对象；项目 | A piece of data being represented or compared. | 被转换、存储或比较的一个东西。 |
| data object | 数据对象 | A unit of data treated as one item. | 系统当作一个整体来处理的一份数据。 |
| meaning | 含义；意义 | What an item expresses or refers to. | 一段文字、图片或商品表达的内容。 |
| useful meaning | 有用含义 | Meaning that helps a system compare or use items. | 对比较和完成任务有帮助的含义。 |
| feature | 特征 | A useful property or signal of an item. | 一个对象中能帮助系统识别或比较的属性。 |
| useful feature | 有用特征 | A feature that supports a task or comparison. | 对当前任务有用的特点。 |
| pattern | 模式；规律 | A relationship or regularity captured in data. | 数据中反复出现、可以利用的规律。 |
| relationship | 关系 | How items or features relate to one another. | 不同对象之间的联系。 |
| semantic relationship | 语义关系 | A relationship based on meaning. | 根据含义而不是只看字面判断的联系。 |
| similar item | 相似对象 | An item with a similar meaning or feature pattern. | 和另一个对象含义或特征相近的东西。 |
| similar meaning | 相似含义 | Meaning that is close between two items. | 两段文字或两个对象表达的意思接近。 |
| nearby vector | 邻近向量 | A vector located close to another vector in the chosen space. | 在数字空间中位置靠近的向量。 |
| vector proximity | 向量邻近性 | How close two vectors are. | 两串数字在空间里离得近不近。 |
| compare | 比较 | Examine items or vectors to find similarity or difference. | 把两个或多个东西放在一起看是否相近。 |
| compare meaning | 比较含义 | Compare items based on represented meaning. | 看两个对象表达的意思是否接近。 |
| compare features | 比较特征 | Compare useful properties represented in items. | 看两个对象的重要特点是否相似。 |
| similarity | 相似度 | A measure of how alike two vectors or items are. | 用一个数表示两个对象有多像。 |
| similarity measure | 相似度度量 | A method for measuring similarity. | 计算两个对象相似程度的方法。 |
| similarity score | 相似度分数 | A numerical score expressing similarity. | 表示两个对象有多相似的数字分数。 |
| distance | 距离 | A measure of how far apart vectors are. | 用数字表示两个向量相差多远。 |
| compare a query vector | 比较查询向量 | Compare a query representation with stored representations. | 拿当前问题对应的向量去和已保存的向量比较。 |
| query | 查询；查询内容 | The current request used to find related items. | 用户现在想查找的内容或问题。 |
| query vector | 查询向量 | The vector representing a current query. | 把当前问题转换成的一串数字。 |
| stored vector | 已存向量 | A vector saved for later comparison. | 提前保存、以后拿来匹配的数字向量。 |
| source vector | 来源向量 | A vector associated with a source item. | 对应某份原始资料的向量。 |
| candidate vector | 候选向量 | A stored vector considered as a possible match. | 可能与查询相似、正在被比较的向量。 |
| nearest item | 最近对象 | An item whose vector is closest to the query vector. | 数字位置最靠近当前查询的对象。 |
| nearby item | 邻近对象 | An item with a nearby vector. | 在向量空间中靠近的对象。 |
| chosen representation space | 选定的表示空间 | The space selected for representing and comparing vectors. | 模型用来放置和比较向量的数字空间。 |
| literal map | 字面地图 | A physical or literal map, unlike an embedding space. | 真正表示地理位置的地图；嵌入的“地图”不是这种地图。 |
| map of human meaning | 人类含义地图 | A literal, complete map of human meaning. | 能完整表示人类所有含义的地图，向量并不能保证做到。 |
| analogy | 类比 | An explanation that compares embeddings to placing ideas on a map. | 用熟悉的事物帮助理解抽象概念。 |
| idea map | 想法地图 | A metaphor for a space where related ideas are near each other. | 把相近想法放在一起的比喻。 |
| place ideas near each other | 将相近想法放在一起 | Represent similar ideas with nearby vectors. | 让意思相近的内容在数字空间里靠近。 |
| Input | 输入 | The item received by the embedding workflow. | 送进系统、准备被转换的数据。 |
| receive the item | 接收对象 | Take in text, an image, or another data object. | 系统先收到文字、图片或其他数据。 |
| encode | 编码 | Convert an input into a representation. | 把输入转换成另一种可计算的形式。 |
| encoding | 编码 | The act of converting data into a representation. | 把数据转成数字表示的过程。 |
| embedding model | 嵌入模型 | A model that converts an item into a vector. | 专门把文字、图片等变成向量的模型。 |
| apply an embedding model | 应用嵌入模型 | Use an embedding model on an input item. | 用嵌入模型处理一个输入。 |
| convert the item into a vector | 将对象转换成向量 | Turn an item into a numerical vector. | 把对象变成一串数字。 |
| Store | 存储 | Save the vector for later use. | 把转换后的向量保存起来。 |
| save the vector | 保存向量 | Persist a vector after encoding. | 把向量留下，以便以后查询。 |
| ID | 标识符；ID | An identifier associated with a stored vector. | 给向量或原始对象用来区分身份的编号。 |
| identifier | 标识符 | A value that identifies an item or record. | 用来说明“这是哪一个对象”的编号或名称。 |
| source metadata | 来源元数据 | Metadata describing where a vector came from. | 说明向量来自哪份资料的信息。 |
| metadata | 元数据 | Information describing or accompanying an item. | 描述数据来源、类型、时间等的附加信息。 |
| store with an ID | 与 ID 一起存储 | Save a vector together with its identifier. | 向量保存时同时记录它对应谁。 |
| store with source metadata | 与来源元数据一起存储 | Save a vector with information about its source. | 向量保存时同时记录原始资料信息。 |
| Compare | 比较 | Measure the relationship between a query vector and stored vectors. | 把当前向量和已保存向量放在一起计算。 |
| measure similarity | 衡量相似度 | Calculate how similar two vectors are. | 算出两个向量有多像。 |
| Use | 使用 | Apply nearby items in a downstream task. | 把找到的相似内容交给后续任务使用。 |
| retrieve | 检索；取回 | Find and return relevant stored items. | 从已保存资料中找出相关内容。 |
| recommend | 推荐 | Suggest useful similar items. | 找出可能对用户有用的相似内容。 |
| retrieve or recommend | 检索或推荐 | Use nearby items either for lookup or suggestions. | 找资料，或推荐相似对象。 |
| downstream task | 下游任务 | A later task that uses retrieved or matched items. | 使用前一步结果继续完成的任务。 |
| process flow | 流程 | The ordered sequence from input to downstream use. | 从接收数据到拿结果使用的一连串步骤。 |
| process step | 流程步骤 | One stage in the embedding workflow. | 流程中的一个环节。 |
| input step | 输入步骤 | The first stage that receives the item. | 流程中先把资料交给系统。 |
| encode step | 编码步骤 | The stage that applies the embedding model. | 流程中把资料转换成向量。 |
| store step | 存储步骤 | The stage that saves the vector and context. | 流程中保存向量、ID 和来源信息。 |
| compare step | 比较步骤 | The stage that measures similarity. | 流程中计算查询与已存向量的关系。 |
| use step | 使用步骤 | The stage that retrieves or recommends items. | 流程中把匹配结果用于后续任务。 |
| item ID | 对象 ID | An identifier for the represented item. | 代表某个文字、图片或商品的编号。 |
| source | 来源 | The original material from which an item came. | 向量对应的原始文章、图片或商品资料。 |
| source metadata | 来源信息；来源元数据 | Context that identifies an item's source. | 说明内容来自哪里、属于什么资料的信息。 |
| text | 文本 | Written language that can be embedded. | 可以被转换成向量的文字。 |
| image | 图像；图片 | Visual data that can be embedded. | 可以被转换成向量的图片。 |
| product | 产品；商品 | An item that can be represented and matched. | 可以拿来比较或推荐的商品。 |
| product description | 产品描述 | Text describing a product. | 介绍商品特点、用途等的文字。 |
| question | 问题 | A user request that can be embedded as a query. | 用户想让系统查找答案的提问。 |
| help article | 帮助文章 | An article that may answer a user question. | 帮助用户解决问题的资料文章。 |
| relevant article | 相关文章 | An article whose content matches a question. | 和用户问题最有关的文章。 |
| product matching | 产品匹配 | Finding products with similar descriptions or features. | 找出特点相近的商品。 |
| similar product | 相似产品 | A product with a similar embedding. | 向量表示相近、可能相似的商品。 |
| product review | 产品审核；商品复核 | Human or system review of matched products. | 对匹配出来的商品再检查。 |
| recommendation | 推荐 | A suggested item selected as useful or similar. | 系统认为可能有用、值得查看的内容。 |
| relevant | 相关的 | Closely connected to the current query or task. | 和当前问题或任务关系密切。 |
| password change | 密码更改 | The everyday search scenario used in the page. | 用户要修改密码这一类问题。 |
| search | 搜索 | Finding relevant content for a query. | 根据问题寻找相关资料。 |
| search question | 搜索问题 | A question used to search a collection. | 用来查资料的用户问题。 |
| help article matching | 帮助文章匹配 | Comparing a question embedding with help-article embeddings. | 把问题和帮助文章的向量进行比较。 |
| business example | 商业示例 | The product-matching use case on the page. | 企业里用向量匹配商品的例子。 |
| real-world example | 现实世界例子 | An example showing how embeddings can be used. | 说明技术在真实场景怎么用的例子。 |
| keyword | 关键词 | A literal word or phrase used for matching. | 直接查找文字里是否出现某个词。 |
| keyword match | 关键词匹配 | Matching literal words or phrases. | 只看词语是否相同或出现。 |
| literal word | 字面词语 | The exact word appearing in text. | 文字中原样出现的词。 |
| literal phrase | 字面短语 | An exact phrase appearing in text. | 文字中原样出现的一串词。 |
| pattern and relationship | 模式与关系 | Information represented by an embedding as numbers. | 向量试图用数字保留内容中的规律和联系。 |
| database | 数据库 | A system that stores vectors, metadata, or records. | 专门保存数据、方便之后查询的系统。 |
| vector database | 向量数据库 | A database designed to store and search vectors. | 专门保存并查找向量的数据库。 |
| database record | 数据库记录 | A stored entry containing data or metadata. | 数据库中保存的一条资料。 |
| vector storage | 向量存储 | The act or system of saving vectors. | 把向量保存起来的功能或过程。 |
| metadata record | 元数据记录 | Stored descriptive information associated with a vector. | 和向量一起保存的来源、ID 等说明信息。 |
| meaning itself | 含义本身 | The full human meaning, not merely a model-generated representation. | 真正完整的人类理解，不等于一串模型生成的数字。 |
| model-generated representation | 模型生成的表示 | A representation produced by an embedding model. | 模型计算出来的数字表达，不是意义本身。 |
| guarantee | 保证 | Make something certain or assured. | 确保事情一定成立。 |
| cannot be guaranteed by a vector alone | 不能仅靠向量保证 | A vector by itself does not guarantee complete human meaning. | 只有向量不一定就代表真正、完整的理解。 |
| vector search | 向量搜索 | Search based on vector similarity or distance. | 按向量相似程度查找内容。 |
| retrieval | 检索 | Finding relevant items from stored data. | 从已保存内容中找出相关资料。 |
| RAG | 检索增强生成（RAG） | Generation supported by retrieved information. | 先检索资料，再用资料帮助生成回答。 |
| token | 词元；标记 | A text unit used by a language model. | 语言模型处理文字时切分出的单位。 |
| related concept | 相关概念 | A concept connected to embeddings. | 和嵌入主题有直接联系的概念。 |
| concept tree | 概念链 | An ordered relationship from data to retrieved items. | 从原始数据一路到检索结果的概念流程。 |
| data → embedding model → vector | 数据→嵌入模型→向量 | Data is transformed into a vector by an embedding model. | 数据经过嵌入模型，变成向量。 |
| vector → vector search | 向量→向量搜索 | A vector can be used in vector search. | 有了向量后，可以按相似性搜索。 |
| retrieved items | 检索出的对象 | Items returned after vector comparison. | 比较后找出来的资料或商品。 |
| retrieval result | 检索结果 | The item or list returned by a search. | 搜索后系统返回的内容。 |
| recommended item | 推荐对象 | An item suggested because it appears similar or useful. | 因为相似或有用而被推荐的内容。 |
| downstream use | 下游使用 | Applying retrieved or recommended items later. | 把找到的结果交给后续功能使用。 |
| numerical feature | 数值特征 | A feature represented with numbers. | 用数字表示的对象特点。 |
| dimension | 维度 | The number of coordinates or values in a vector. | 一串向量里有多少个数字位置。 |
| coordinate | 坐标 | One numerical position in a vector space. | 向量中表示某个方向或属性的一个数字位置。 |
| embedding dimension | 嵌入维度 | The number of values in an embedding vector. | 一个嵌入向量包含多少个数字。 |
| similarity geometry | 相似性几何关系 | The spatial relationship used to compare vectors. | 用空间位置来判断对象相似不相似。 |
| cosine similarity | 余弦相似度 | A common measure comparing vector directions. | 看两串数字指向的方向有多接近。 |
| dot product | 点积 | A calculation combining corresponding vector values. | 把两串数字对应相乘再相加的一种比较方法。 |
| Euclidean distance | 欧氏距离 | Straight-line distance between vectors. | 在数字空间里两点之间的直线距离。 |
| nearest-neighbor search | 最近邻搜索 | Search for vectors closest to a query vector. | 找出离当前查询向量最近的对象。 |
| top-k results | Top-k 结果 | The best k matches returned by a search. | 只返回最相似的前几项。 |
| ranking | 排序 | Ordering candidate items by similarity or relevance. | 按相似程度或相关程度排先后。 |
| relevance | 相关性 | How useful an item is for the query. | 一个结果对当前问题有多有用。 |
| semantic search | 语义搜索 | Search based on meaning rather than exact words. | 不要求词完全一样，而是按意思找资料。 |
| lexical search | 词法搜索 | Search based mainly on literal words. | 主要根据字面词语查找。 |
| dense vector | 稠密向量 | A vector in which many coordinates carry values. | 大多数位置都有数字的向量。 |
| sparse vector | 稀疏向量 | A vector in which many coordinates are zero or empty. | 很多位置没有值、只有少数位置有数字的向量。 |
| embedding model output | 嵌入模型输出 | The vector produced by an embedding model. | 嵌入模型处理完输入后吐出的数字向量。 |
| embedding input | 嵌入输入 | The data supplied to an embedding model. | 交给嵌入模型处理的文字、图片或其他数据。 |
| model inference | 模型推理 | Running an embedding model on new data. | 用已经训练好的嵌入模型处理新内容。 |
| batch embedding | 批量嵌入 | Creating embeddings for many items together. | 一次把很多资料都转换成向量。 |
| online embedding | 在线嵌入 | Creating an embedding during a live request. | 用户查询时即时把内容转成向量。 |
| offline embedding | 离线嵌入 | Creating and storing embeddings before a query. | 提前批量生成并保存向量。 |
| embedding pipeline | 嵌入流水线 | The complete sequence for encoding and using embeddings. | 从输入、编码、保存到查询使用的完整流程。 |
| corpus | 语料库；资料集合 | A collection of documents or items to embed and search. | 用来生成向量并供搜索的资料总集合。 |
| document | 文档 | A text item that can be embedded or retrieved. | 可以转换成向量、也可以被检索的文字资料。 |
| document collection | 文档集合 | Multiple documents stored for comparison or search. | 放在一起、等待被搜索的多份文档。 |
| source document | 源文档 | The original document represented by an embedding. | 产生某个向量的原始文档。 |
| metadata filter | 元数据过滤 | Restrict search using metadata in addition to similarity. | 先按来源、类别等附加信息筛选。 |
| chunk | 文档片段；分块 | A smaller piece of a document used for embedding. | 把长文档切成的一小段。 |
| chunking | 文档切分 | Splitting a document into smaller pieces. | 把长资料拆成更适合搜索的小块。 |
| chunk embedding | 文档片段嵌入 | An embedding created for one document chunk. | 为文档中的一小段文字生成的向量。 |
| context | 上下文 | Surrounding information that helps interpret an item. | 帮助理解某句话或资料的前后信息。 |
| retrieved context | 检索上下文 | Context brought back for a downstream task. | 搜索后找回、交给后续系统参考的资料。 |
| reranking | 重排序 | Reorder retrieved candidates using a later relevance step. | 初步找出结果后，再按更精细的相关性重新排序。 |
| bi-encoder | 双编码器 | A setup that encodes query and item separately. | 查询和资料各自先变成向量，再比较。 |
| cross-encoder | 交叉编码器 | A model that evaluates a query and candidate together. | 把问题和候选资料放在一起做更细的判断。 |
| embedding quality | 嵌入质量 | How well embeddings preserve useful similarity and relationships. | 向量是否真的把重要相似关系保留下来。 |
| retrieval quality | 检索质量 | How useful and relevant returned items are. | 搜出来的内容是否相关、是否有用。 |
| recall@k | Recall@k；前 k 项召回率 | The share of relevant items found in the top k results. | 最相关的资料有多少被前几项结果找出来。 |
| precision@k | Precision@k；前 k 项精确率 | The share of top k results that are relevant. | 返回的前几项里有多少真正相关。 |
| mean reciprocal rank | 平均倒数排名；MRR | A metric rewarding relevant results appearing early. | 相关结果越靠前，评分越高的一种指标。 |
| NDCG | 归一化折损累计增益（NDCG） | A ranking metric that accounts for relevance and position. | 同时看相关程度和结果排位的排序指标。 |
| latency | 延迟 | Time between a query and returned results. | 用户发起查询后要等多久才有结果。 |
| throughput | 吞吐量 | How many embedding or search requests a system handles. | 系统一段时间能处理多少请求。 |
| storage cost | 存储成本 | Resources needed to save vectors and metadata. | 保存大量向量和附加信息所需的空间和费用。 |
| embedding drift | 嵌入漂移 | A change in embedding behavior over time or model versions. | 数据或模型变了之后，向量关系也发生变化。 |
| model version | 模型版本 | A particular release of an embedding model. | 嵌入模型的某一个版本。 |
| compatibility | 兼容性 | Whether vectors from different components or versions work together. | 不同模型、索引或系统生成的向量能不能一起使用。 |
| modality | 模态；数据类型 | The type of data, such as text or image. | 信息是文字、图片、音频等哪一种形式。 |
| multimodal embedding | 多模态嵌入 | A representation involving more than one data modality. | 让文字、图片等不同类型的信息能放在可比较的表示里。 |
| cross-modal comparison | 跨模态比较 | Comparing items from different modalities. | 比较文字和图片等不同类型的信息。 |
| audio | 音频 | Sound data that could be represented as an embedding. | 可以交给系统处理的声音信息。 |
| video | 视频 | Moving visual and/or audio data. | 连续的画面和声音信息。 |
| feature space | 特征空间 | A space organized by represented features. | 按对象特征安排位置的数字空间。 |
| semantic space | 语义空间 | A space where meaningful similarity is represented geometrically. | 让意思相近内容位置接近的数字空间。 |
| representation learning | 表示学习 | Learning useful representations from data. | 让模型自己学会怎样用数字表示数据。 |
| contrastive learning | 对比学习 | Learning representations by bringing similar items closer and separating dissimilar ones. | 让相似内容靠近、不相似内容分开的学习方法。 |
| training objective | 训练目标 | The goal used to shape an embedding model during training. | 训练时希望模型学到什么效果。 |
| similarity objective | 相似度目标 | A training objective focused on preserving similarity relationships. | 训练模型时要求相似对象保持相近的目标。 |
| semantic equivalence | 语义等价 | Different wording with essentially the same meaning. | 说法不同但意思基本相同。 |
| paraphrase | 改写；释义 | A different wording of similar meaning. | 用另一种说法表达同样意思。 |
| synonym | 同义词 | A word with the same or similar meaning. | 意思相同或接近的词。 |
| alias | 别名 | Another name used for the same or related concept. | 同一个概念的另一种叫法。 |
| terminology | 术语 | A specialized word used in a field. | 某个专业领域里有特定含义的词。 |
| abbreviation | 缩写 | A shortened form of a term. | 把较长术语缩短后的写法。 |
| label | 标签 | A name or category attached to an item. | 给内容标上的类别或名称。 |
| title | 标题 | A short name for a document or item. | 资料最上方概括内容的名字。 |
| output | 输出 | The result returned by a system. | 系统处理后给出来的结果。 |
| input | 输入 | Information supplied to a system. | 交给系统处理的信息。 |
| system | 系统 | Software and data components working together. | 一起接收、处理和返回信息的一整套东西。 |
| computer | 计算机 | A machine that processes numerical representations. | 能按规则处理数字和数据的机器。 |
| compare meaning or features | 比较含义或特征 | Use embeddings to compare what items mean or what they contain. | 用数字表示来判断两个对象的意思或特点是否相近。 |
| useful downstream task | 有用的下游任务 | A later application that benefits from matched items. | 能利用检索或推荐结果完成的后续工作。 |
| page definition | 页面定义 | The concise definition given by the topic page. | 页面直接给出的概念解释。 |
| independent explainer | 独立讲解视频 | A separate visual explanation accompanying the page. | 页面附带的额外视频说明。 |
| visual explainer | 可视化讲解 | An explanation using visuals. | 用画面帮助理解概念的讲解。 |
| captions | 字幕 | Text displayed for spoken video content. | 视频里同步显示的文字。 |
| poster | 视频封面图 | The preview image shown before video playback. | 视频播放前显示的预览图片。 |

## Potential Missing Concepts

- **vector dimension（向量维度）**：页面说 vector 和 numerical representation，但没有解释一个向量包含多少个数字。
- **cosine similarity（余弦相似度）**：页面只说 measure similarity，没有列出最常用的具体比较公式。
- **dot product（点积）**：页面没有说明向量如何通过数字运算比较。
- **Euclidean distance（欧氏距离）**：页面用 nearby vectors 作类比，但没有定义距离计算。
- **normalization（归一化）**：没有说明比较向量前是否需要调整长度或尺度。
- **nearest-neighbor search（最近邻搜索）**：nearby items 出现了，但没有给出正式搜索术语。
- **top-k（前 k 项）**：页面说 retrieve or recommend，但没有说明通常返回最相似的前 k 个结果。
- **ranking（排序）**：similarity comparison 出现了，但没有展开如何把候选按相关性排序。
- **semantic search（语义搜索）**：向量搜索相关内容出现了，但没有解释按含义搜索和按关键词搜索的区别。
- **lexical / keyword search（词法／关键词搜索）**：keyword 对照出现了，但没有介绍传统字面检索的整体机制。
- **dense vector / sparse vector（稠密向量／稀疏向量）**：页面没有区分向量中多数维度是否有值。
- **vector database（向量数据库）**：页面只说 database stores vectors，没有解释专门用于向量检索的数据库。
- **index（索引）**：没有说明如何让大规模向量搜索不必逐一比较所有向量。
- **approximate nearest neighbor / ANN（近似最近邻）**：没有介绍大规模向量搜索常用的近似算法。
- **HNSW（分层可导航小世界图）**：没有介绍常见的向量索引结构。
- **FAISS（Facebook AI Similarity Search）**：没有提及常用的向量相似性搜索库。
- **chunking（文档切分）**：页面提到 text 和 source metadata，但没有说明长文档通常先切成片段。
- **chunk（文档片段）**：没有解释检索通常针对文档片段，而不是整本长文档。
- **metadata filtering（元数据过滤）**：页面强调保存 metadata，但没有说明查询时如何按来源、类别或时间筛选。
- **reranking（重排序）**：页面只说 compare similarity，没有说明初步召回后的二次排序。
- **bi-encoder（双编码器）**：没有区分查询和文档分别编码的架构。
- **cross-encoder（交叉编码器）**：没有介绍将查询和候选一起判断相关性的架构。
- **embedding model training（嵌入模型训练）**：页面讲如何使用 embedding model，没有说明模型如何学会这种表示。
- **representation learning（表示学习）**：页面讲 representation，但没有定义让模型学出表示的学习范式。
- **contrastive learning（对比学习）**：没有说明如何通过相似和不相似样本塑造向量空间。
- **positive pair / negative pair（正样本对／负样本对）**：没有说明对比学习中哪些对象应靠近或远离。
- **multimodal embedding（多模态嵌入）**：页面提到 text、image 和 other data，但没有讲不同模态能否共享空间。
- **cross-modal retrieval（跨模态检索）**：没有展开用文字找图片或用图片找文字的情况。
- **embedding dimension trade-off（嵌入维度权衡）**：没有讨论维度、表达能力、存储和检索成本之间的关系。
- **embedding quality（嵌入质量）**：页面说 useful meaning or features，但没有定义如何评价表示是否好。
- **recall@k（前 k 项召回率）**：页面没有给出检索覆盖率指标。
- **precision@k（前 k 项精确率）**：页面没有给出返回结果相关程度的指标。
- **MRR（平均倒数排名）**：页面没有给出强调相关结果排位的指标。
- **NDCG（归一化折损累计增益）**：页面没有给出同时考虑相关性和顺序的排序指标。
- **latency（延迟）**：页面没有讨论从查询到结果返回的时间。
- **throughput（吞吐量）**：页面没有讨论系统单位时间能处理多少嵌入或搜索请求。
- **storage cost（存储成本）**：页面没有展开保存大量高维向量的空间和费用。
- **model version compatibility（模型版本兼容性）**：没有说明不同 embedding model 版本生成的向量通常不能直接混用。
- **embedding drift（嵌入漂移）**：没有讨论模型更新或数据分布变化后向量关系改变的问题。
- **out-of-domain data（域外数据）**：没有说明输入超出模型训练或适用范围时可能失真。
- **polysemy（多义词）**：页面说 meaning，但没有讨论同一个词在不同上下文有不同含义。
- **context sensitivity（上下文敏感性）**：没有解释上下文如何改变同一文本的嵌入表示。
- **semantic equivalence（语义等价）**：没有单独定义不同措辞表达相同含义的情况。
- **paraphrase（释义／改写）**：没有展开同义改写在语义搜索中的作用。
- **data leakage（数据泄漏）**：没有说明来源或训练数据泄漏对检索和评估的影响。
- **privacy（隐私）**：页面说可嵌入文本、图片和产品数据，但没有讨论敏感内容保护。
- **access control（访问控制）**：没有说明向量和源文档的权限是否需要保持一致。
- **data deletion（数据删除）**：没有说明删除原始资料时如何同步删除对应向量。
- **security（安全）**：没有讨论向量数据库、元数据和检索接口的系统安全。
- **evaluation set（评估集）**：没有说明怎样准备查询、相关文档和人工判断来评估检索。
- **ground truth（真实答案／标注真值）**：没有说明如何判断某个检索结果是否确实相关。
- **human relevance judgment（人工相关性判断）**：页面说 product review，但没有说明人工如何标注搜索结果。
- **query expansion（查询扩展）**：没有介绍如何改写或扩充查询以找回更多相关内容。
- **hybrid search（混合搜索）**：没有说明如何结合关键词搜索和向量搜索。
- **RAG context window（RAG 上下文窗口）**：页面列出 RAG，但没有说明检索结果还要适配生成模型的上下文限制。
- **retrieval-augmented generation（检索增强生成全称）**：只给出缩写 RAG，没有给出完整英文展开。
- **embedding API（嵌入 API）**：页面没有说明应用如何调用服务生成向量。
- **batching（批处理）**：没有说明批量生成向量如何影响吞吐和成本。
- **online versus offline embedding（在线与离线嵌入）**：没有区分实时生成和预先生成。
- **re-embedding（重新嵌入）**：没有说明模型升级或数据修订后如何重建向量。
- **index rebuild（索引重建）**：没有说明向量更新后如何维护搜索索引。

## Aliases / Synonyms

- embedding ↔ embeddings ↔ vector representation ↔ numerical representation
- text embedding ↔ text vector ↔ vectorized text representation
- image embedding ↔ image vector ↔ visual embedding
- product embedding ↔ product vector ↔ product representation
- embedding model ↔ embedding encoder ↔ representation model
- encode ↔ embed ↔ vectorize ↔ convert into a vector
- vector ↔ embedding vector ↔ numerical vector
- vector space ↔ representation space ↔ feature space ↔ semantic space
- similarity ↔ similarity score ↔ similarity measure ↔ closeness
- distance ↔ vector distance ↔ geometric distance
- nearby vector ↔ close vector ↔ similar vector
- query ↔ query item ↔ search input ↔ current request
- query vector ↔ query embedding ↔ embedded query
- stored vector ↔ indexed vector ↔ document vector ↔ candidate vector
- source metadata ↔ metadata ↔ source information ↔ provenance metadata
- ID ↔ identifier ↔ item ID ↔ record ID
- retrieve ↔ retrieve items ↔ search and return ↔ find relevant items
- retrieval ↔ information retrieval ↔ lookup ↔ vector search（相关但不完全同义）
- recommend ↔ suggest ↔ make a recommendation
- recommendation ↔ suggested item ↔ recommended result
- relevant ↔ related ↔ useful for the query
- embedding pipeline ↔ embedding workflow ↔ encode-store-search flow
- semantic search ↔ meaning-based search ↔ vector search（常见实现方式相关，但不完全同义）
- keyword search ↔ lexical search ↔ literal matching
- keyword match ↔ exact word match ↔ literal phrase match
- vector database ↔ vector store ↔ similarity-search database
- chunk ↔ document chunk ↔ text segment ↔ passage
- chunking ↔ document splitting ↔ text segmentation
- reranking ↔ re-ranking ↔ second-stage ranking
- nearest-neighbor search ↔ NN search ↔ closest-vector search
- top-k ↔ top k results ↔ k nearest items
- cosine similarity ↔ cosine score ↔ angular similarity
- dense vector ↔ dense embedding
- sparse vector ↔ sparse representation
- multimodal embedding ↔ cross-modal embedding ↔ shared embedding space
- RAG ↔ retrieval-augmented generation ↔ retrieval-enhanced generation
- metadata filter ↔ attribute filter ↔ structured filter
- product matching ↔ item matching ↔ similar-product retrieval
- source document ↔ original document ↔ source material
- downstream task ↔ downstream use ↔ later application
- embedding quality ↔ representation quality ↔ semantic preservation
- recall@k ↔ top-k recall
- precision@k ↔ top-k precision
- MRR ↔ mean reciprocal rank
- NDCG ↔ normalized discounted cumulative gain
- alias ↔ alternate name ↔ another name
- synonym ↔ near-synonym ↔ same-meaning term

## Do Not Confuse Candidates

- **Embedding vs vector**：embedding 是语义或特征表示这一概念；vector 是承载该表示的一串数字。页面把 embedding 表达为 vector，但二者在抽象层级上不完全相同。
- **Embedding vs embedding model**：embedding 是模型产生的结果；embedding model 是把输入转换成 embedding 的模型。
- **Embedding model vs vector database**：嵌入模型负责编码；向量数据库负责保存、索引和搜索向量。
- **Embedding vs meaning itself**：embedding 是模型生成的近似表示，不保证等于完整的人类含义。
- **Embedding vs keyword**：embedding 比较表示出的模式和关系；keyword 主要做字面词语或短语匹配。
- **Semantic similarity vs literal overlap**：两个文本可以用不同词表达相近含义；字面重叠少不代表语义一定不相似。
- **Similarity vs distance**：similarity 越高通常代表越相近；distance 越小通常代表越相近，方向相反但都可用于比较。
- **Query vector vs stored vector**：query vector 表示当前查询；stored vector 表示已保存的候选资料或对象。
- **Source metadata vs source content**：metadata 描述来源、ID、类别等；source content 是实际被表示或检索的原始内容。
- **Vector space vs literal map**：向量空间是数学表示空间；页面的“地图”只是帮助理解的类比，不是地理地图。
- **Vector search vs keyword search**：向量搜索主要按表示的相似性查找；关键词搜索主要按字面词语查找。
- **Vector search vs retrieval**：vector search 是一种搜索方法；retrieval 是找回相关资料这一更宽泛的任务。
- **Retrieval vs recommendation**：retrieval 通常强调找回已有相关资料；recommendation 强调判断并建议可能有用的对象。
- **Recommendation vs product matching**：recommendation 是面向用户的建议；product matching 是把商品与商品或描述匹配起来，可能还要人工复核。
- **Embedding vs generation**：embedding 把输入转换成表示；generation 产生新的文字、图片或其他内容。
- **Embedding vs token**：token 是语言模型处理文本时的单位；embedding 是对 token、文本或其他对象的数值表示。
- **Embedding vs tokenization**：tokenization 是切分文字；embedding 是把对象编码成向量，两个步骤可能连续但不是一回事。
- **Embedding vs classification label**：embedding 是连续的数值表示；label 是离散的类别名称或答案。
- **Embedding vs output**：embedding 可以是模型输出的一种形式，但不是所有系统输出都是 embedding。
- **Embedding vs database record**：embedding 是向量表示；database record 是保存向量、ID、metadata 或其他字段的记录。
- **Embedding database vs ordinary database**：普通数据库可以保存记录；向量数据库还需要高效支持向量相似度搜索。
- **Similarity score vs relevance judgment**：相似度分数是模型或算法计算的数值；相关性判断可能还需要任务标准或人工审核。
- **Nearest item vs best answer**：向量最近的对象通常是最相似候选，不保证就是最终正确答案。
- **Nearby vectors vs identical meaning**：位置接近只表示模型认为相似，不代表两个对象含义完全相同。
- **Model-generated representation vs human understanding**：数字表示能帮助比较，不等于系统像人一样理解。
- **Metadata vs embedding**：metadata 是附加描述信息；embedding 是内容本身的数值表示。
- **ID vs vector**：ID 用来识别对象；vector 用来表示对象并参与比较。
- **Source document vs retrieved context**：source document 是原始资料；retrieved context 是查询后被选回、用于下游任务的资料片段。
- **RAG vs embeddings**：embeddings 是一种表示技术；RAG 是利用检索资料辅助生成的完整工作流，通常可以使用 embeddings。
- **RAG vs vector search**：vector search 负责找相似内容；RAG 还包括把找回的内容交给生成模型使用。
- **Chunk vs document**：chunk 是文档的一部分；document 是完整或较大的原始资料。
- **Chunking vs encoding**：chunking 是切分资料；encoding 是把切分后的对象转成向量。
- **Dense vector vs sparse vector**：dense vector 多数维度有值；sparse vector 很多维度为零或没有值。
- **Cosine similarity vs Euclidean distance**：前者通常比较方向；后者比较空间直线距离，不能把名称和数值方向混为一谈。
- **Bi-encoder vs cross-encoder**：bi-encoder 分别编码查询和候选，适合高效召回；cross-encoder 把两者放在一起评分，通常更精细但更慢。
- **Recall@k vs precision@k**：recall@k 看相关内容找回了多少；precision@k 看返回的前 k 项中有多少相关。
- **Embedding quality vs retrieval quality**：表示本身可能有质量问题；检索质量还会受到索引、排序、过滤和数据覆盖的影响。
- **Online embedding vs offline embedding**：online 是请求到来时实时生成；offline 是提前生成并保存。
- **Model version vs vector compatibility**：模型版本改变可能使新旧向量空间不兼容，不能默认直接混搜。
- **Similarity vs causality**：向量相似只表示表示空间中的接近，不说明一个对象导致另一个对象。
- **Similarity vs truth**：相似度高不保证内容真实、正确或适合业务使用。
- **Search relevance vs business suitability**：搜索结果相关不一定符合权限、库存、价格或其他业务条件。
- **Product matching vs duplicate detection**：商品匹配寻找相似商品；重复检测要判断是否其实是同一个记录或商品。
- **Semantic equivalence vs factual equivalence**：意思相近不代表两个陈述包含完全相同的事实。
- **Visual explainer vs glossary concept**：页面的 video、poster、captions 是呈现资源相关词，不是 embedding 机制本身。

## Notes

- 本文件是 `embeddings.html` 的 raw glossary 收集稿，按要求尽可能保留正文中出现或由正文直接触发的术语、流程节点、例子词、对照词和相关工程词，不做最终去重、归并或删减。
- 页面元信息为 `05 · Embeddings, RAG & Vector Search · Topic 01`；本任务指定的输出命名和模块编号为 `08-embeddings.md`，因此两套信息都保留在 Topic Metadata 中。
- 页面核心定义是：embedding 把 text 或 other data 表示成 numbers，使 computer 能比较 meaning 或 features。
- 页面定义段进一步说明 embedding 是 numerical representation，能够捕捉 useful meaning or features；model 将 text、images 或 products 映射到 vector；similar items 往往在 chosen representation space 中拥有 nearby vectors。
- 页面类比是“placing ideas on a map”：相似含义的对象彼此靠近；同时明确提醒该 map 只是帮助比较 relationships，不是 literal map of human meaning。
- 页面明确给出五步流程：1. Input / Receive the item；2. Encode / Apply an embedding model；3. Store / Save the vector with an ID and source metadata；4. Compare / Measure similarity；5. Use / Retrieve or recommend。
- 页面 everyday example 是 search：输入是 changing a password 的问题；系统比较其 embedding 与 help articles；输出是 most relevant articles。
- 页面 business example 是 product matching：输入是 product description；系统比较 product embeddings；输出是 similar products for review or recommendation。
- 页面 “What it is NOT” 直接对照三组：Embedding ≠ Keyword、Embedding ≠ Database、Embedding ≠ Meaning Itself。对照中的关键词、数据库、意义本身都应保留为易混淆候选。
- 页面 related concept tree 是 `Data → Embedding Model → Vector → Vector Search → Retrieved Items`；页面还列出 Vector Search、Retrieval、RAG、Token 作为 Explore next。
- 页面 Remember this 的核心句是：An embedding turns data into numbers that a system can compare。
- 页面出现的原始数据类型包括 text、images、products 和 another data object；候选集合因此保留 text embedding、image embedding、product embedding 及 multimodal 相关扩展。
- 页面正文没有明确给出 cosine similarity、dot product、vector dimension、index、ANN 等公式或工程实现；这些被放入 Potential Missing Concepts，不能当作页面明示定义。
- 页面正文没有给出具体 retrieval metrics；recall@k、precision@k、MRR、NDCG 等属于向量检索的常见缺口候选。
- 页面中的 `ID`、`source metadata`、`query vector`、`stored vectors` 是流程和数据关系的重要词，不应在后续整理时仅因为常见而删除。
- 页面使用 retrieve or recommend，说明 embedding 结果既可以支持资料找回，也可以支持相似对象推荐；两者在用途上相关但不完全同义。
- 页面将 embedding 与 literal keyword match 区分开；因此 semantic search、lexical search、keyword matching 和 exact match 可作为相关扩展，但应标为候选而非页面的完整定义。
- 页面将 database 定义为保存 vectors、metadata 或 other records 的东西；它没有把 database 等同于 embedding，也没有具体展开 vector database 的索引实现。
- 页面将 embedding 与 meaning itself 区分开，强调 model-generated representation 不能仅凭一个 vector 保证完整的人类含义；这是本主题最重要的边界说明之一。
- 页面视频区域只标记 `Independent explainer`、`visual explainer`、`captions`、`poster` 和视频源文件；这些是低优先级呈现相关候选，不是 embedding 核心术语。
- 英文大小写形式（Embedding、embedding、Vector、vector、Input、Encode、Store、Compare、Use）和复数形式（embeddings、vectors、items、features）在 raw 阶段保留为可追踪候选，不在本阶段强制统一。
