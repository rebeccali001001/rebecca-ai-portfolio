# Topic

Vector Search

## Topic Metadata

- Requested Module: 08
- Page Module: 05 · Embeddings, RAG & Vector Search
- Page Topic: Topic 03 · Vector Search
- Topic Title: What is Vector Search?
- Source File: `vector-search.html`
- Source Page Description: Vector search finds items whose vector representations are close to a query vector.
- Collection Mode: Raw, maximum candidate collection; candidates are intentionally not deduplicated, merged, or reduced.

## Glossary Candidates

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Vector Search | 向量搜索 | A search method that finds similar stored vectors. | 按数字向量的相似程度找内容。 |
| vector search | 向量搜索 | Search based on vector similarity or distance. | 根据向量接近程度进行搜索。 |
| vector representation | 向量表示 | A numerical representation of an item as a vector. | 用一串数字表示一个对象。 |
| vector representations | 向量表示 | Numerical representations used for comparison. | 用来比较的多组数字表示。 |
| item | 对象；项目 | A stored thing that can be searched for. | 系统里可以被查找的一条内容或对象。 |
| stored item | 已存对象 | An item saved before a search request. | 提前保存、等待查询的对象。 |
| query | 查询；查询内容 | The request used to find matching items. | 用户这次想查找的内容或问题。 |
| query vector | 查询向量 | A vector representing the current query. | 把当前问题变成的一串数字。 |
| stored vector | 已存向量 | A vector saved for later comparison. | 预先保存、以后拿来比较的向量。 |
| stored vectors | 已存向量 | Vectors stored in a search system. | 搜索系统中保存的多组向量。 |
| most similar | 最相似的 | Having the closest representation to the query. | 和查询表示最接近的。 |
| similarity | 相似度 | How alike two vectors or items are. | 两个对象有多像。 |
| similar | 相似的 | Close in representation or meaning. | 在表示或含义上接近。 |
| close | 接近的 | Near another vector in the comparison space. | 在比较空间里离得近。 |
| proximity | 邻近性 | The condition of being near another item. | 两个对象彼此靠近的程度。 |
| distance | 距离 | A measure of how far two vectors are apart. | 用数字表示两个向量相差多远。 |
| similarity measure | 相似度度量 | A method for comparing how alike vectors are. | 计算两个向量有多像的方法。 |
| distance measure | 距离度量 | A method for calculating vector separation. | 计算两个向量相隔多远的方法。 |
| query comparison | 查询比较 | Comparing a query with stored vectors. | 把当前查询和已保存向量比较。 |
| matching record | 匹配记录 | A stored record selected as a match. | 被系统认为匹配的一条已存资料。 |
| record | 记录 | A stored data entry returned by search. | 数据系统里保存的一条资料。 |
| metadata | 元数据 | Descriptive information accompanying a record. | 描述资料来源、权限或属性的信息。 |
| source text | 来源文本 | Text associated with a returned record. | 记录对应的原始文字。 |
| source | 来源 | The original material behind a record. | 一条资料原本来自哪里。 |
| embedding model | 嵌入模型 | A model that converts data into vectors. | 把数据转换成向量的模型。 |
| embedding | 嵌入；嵌入表示 | A vector representation produced by an embedding model. | 模型生成的数字向量表示。 |
| embeddings | 嵌入表示 | Multiple vector representations of data. | 多个对象对应的向量表示。 |
| vector | 向量 | An ordered list of numbers. | 按顺序排列的一串数字。 |
| numerical representation | 数值表示 | Information expressed with numbers. | 用数字表达信息的方式。 |
| representation | 表示；表征 | A form used to encode useful information. | 用某种形式表达一个对象。 |
| learned representation | 学习得到的表示 | A representation learned by a model. | 模型从数据中学出来的数字表达。 |
| semantic representation | 语义表示 | A representation intended to preserve meaning. | 尽量保留含义的数字表达。 |
| feature representation | 特征表示 | A representation of useful properties. | 表示对象重要特点的形式。 |
| query representation | 查询表示 | The representation of a search query. | 对当前查询内容的数字表达。 |
| stored representation | 已存表示 | A representation kept for future search. | 为之后搜索保存的数字表达。 |
| same map | 同一张地图 | The shared comparison space for a query and stored items. | 查询和已存对象共同放入的数字空间。 |
| map | 地图；映射空间 | A metaphor for a space containing comparable points. | 这里是理解向量位置的比喻，不是真实地图。 |
| nearby point | 邻近点 | A point close to the query point in the analogy. | 比喻中离查询位置近的点。 |
| point | 点 | A vector viewed as a position in a space. | 把向量想成空间里的一个位置。 |
| geographic distance | 地理距离 | Physical distance on a real-world map. | 真实地理位置之间的距离。 |
| literal geographic distance | 字面地理距离 | Actual physical distance, not vector similarity. | 真正的地理远近，不是向量相似度。 |
| analogy | 类比 | An explanation using a familiar comparison. | 用熟悉事物帮助理解抽象技术。 |
| nearby places | 附近地点 | Places close to one another on a map. | 地图上彼此靠近的地方。 |
| map analogy | 地图类比 | Explaining vector proximity as nearby places. | 用地图上找附近地点来解释向量接近。 |
| proximity analogy | 邻近类比 | The comparison between vector closeness and map closeness. | 把数字空间的接近比作地图上的靠近。 |
| encode | 编码 | Convert a query into a vector representation. | 把查询转换成可计算的向量。 |
| encoding | 编码 | The act of converting data into a representation. | 把数据转换成数字表示的过程。 |
| encode step | 编码步骤 | The first search stage that creates a query vector. | 搜索流程中生成查询向量的一步。 |
| create a query vector | 创建查询向量 | Convert the user's query into a vector. | 把用户问题转成一串数字。 |
| user's query | 用户查询 | The text or request supplied by a user. | 用户输入的问题或请求。 |
| convert | 转换 | Change data into another usable form. | 把一种形式改成另一种形式。 |
| convert the user's query | 转换用户查询 | Encode the user's request as a vector. | 把用户问题编码成向量。 |
| compare | 比较 | Examine a query vector against stored vectors. | 将查询向量与已存向量放在一起计算。 |
| compare step | 比较步骤 | The stage that measures query-to-vector relationships. | 搜索流程中计算相似关系的一步。 |
| compare with stored vectors | 与已存向量比较 | Evaluate a query against saved vectors. | 将查询和保存好的向量逐一或批量比较。 |
| measure distance | 衡量距离 | Calculate how far vectors are from each other. | 算出向量之间相差多远。 |
| measure similarity | 衡量相似度 | Calculate how alike vectors are. | 算出向量之间有多像。 |
| rank | 排名；排序 | Put candidates in order of closeness. | 按接近程度给候选结果排先后。 |
| ranking | 排名；排序 | The ordered list of search candidates. | 按分数或相似程度排列结果。 |
| rank candidates | 给候选排序 | Order possible matches from best to worse. | 把可能匹配的对象按优先级排列。 |
| candidate | 候选对象 | A possible matching item. | 可能符合查询的对象。 |
| candidate set | 候选集合 | The items considered for ranking. | 等待比较和排序的一组对象。 |
| order candidates | 排列候选 | Arrange possible matches by similarity. | 按相似程度安排候选对象顺序。 |
| closest match | 最接近的匹配 | The candidate closest to the query representation. | 和当前查询最接近的匹配项。 |
| closest matches | 最接近的匹配项 | The candidates with the smallest distance or highest similarity. | 与查询最接近的几项结果。 |
| top match | 最佳匹配 | The highest-ranked match. | 排名最前的匹配对象。 |
| top-k results | Top-k 结果 | The best k matches returned by search. | 只返回最相似的前几项。 |
| k nearest neighbors | k 个最近邻 | The k stored vectors nearest to a query. | 离查询最近的 k 个对象。 |
| filter | 过滤 | Remove candidates that violate constraints. | 把不符合条件的候选结果排除。 |
| filter step | 过滤步骤 | The stage that applies search constraints. | 搜索流程中按条件筛选的一步。 |
| apply constraints | 应用约束 | Restrict results using rules. | 根据规定限制可返回的结果。 |
| constraint | 约束；限制条件 | A rule that a result must satisfy. | 结果必须满足的条件。 |
| metadata filter | 元数据过滤器 | A filter based on fields attached to records. | 根据资料附带信息筛选结果。 |
| metadata filtering | 元数据过滤 | Filtering by attributes stored with a record. | 按记录的属性或说明信息过滤。 |
| permission | 权限 | A rule describing who may access a result. | 谁可以查看或使用结果的规定。 |
| permissions | 权限控制 | Access rules applied to search results. | 对搜索结果可见范围的控制。 |
| permissions rule | 权限规则 | A rule used to restrict accessible records. | 限制用户能看到哪些记录的规则。 |
| freshness | 新鲜度；时效性 | How current or recently updated a record is. | 资料是不是最新、是否刚更新。 |
| freshness rule | 新鲜度规则 | A rule preferring or requiring recent data. | 按资料更新时间筛选的规则。 |
| return | 返回 | Send matching records back to the requester. | 把找到的结果交回给用户或系统。 |
| return step | 返回步骤 | The stage that sends selected results onward. | 搜索流程中输出结果的一步。 |
| send results | 发送结果 | Pass search results to a downstream component. | 把搜索结果交给后续功能。 |
| search result | 搜索结果 | A record returned for a query. | 搜索后返回的一条或多条资料。 |
| retrieved record | 检索记录 | A record returned by the search process. | 检索流程找回的一条记录。 |
| retrieved records | 检索出的记录 | Records selected and returned by search. | 搜索后找回的一组资料。 |
| retrieval | 检索；取回 | Finding and returning relevant stored items. | 从已存资料中找出并返回相关内容。 |
| retrieve | 检索；取回 | Find stored records relevant to a query. | 从资料库中找到相关记录。 |
| retrieval result | 检索结果 | The record or list returned after retrieval. | 检索后系统给出的内容。 |
| retrieval system | 检索系统 | A system that finds relevant stored records. | 负责找回相关资料的系统。 |
| downstream task | 下游任务 | A later task that uses search results. | 使用搜索结果继续完成的后续任务。 |
| downstream use | 下游使用 | Applying returned records in a later step. | 把检索结果交给后续功能使用。 |
| generation | 生成 | Producing a final response or other new output. | 系统根据输入生成新的内容。 |
| retrieval or generation | 检索或生成 | Search results may support lookup or generation. | 结果可以用来查资料，也可以帮助生成回答。 |
| return records for retrieval | 返回记录供检索 | Send matching records to a retrieval workflow. | 把匹配记录交给后续检索流程。 |
| return records for generation | 返回记录供生成 | Send retrieved records as input to generation. | 把资料交给模型辅助生成答案。 |
| workflow | 工作流 | An ordered series of processing stages. | 按顺序执行的一串处理步骤。 |
| process | 流程；处理过程 | The sequence from query encoding to result return. | 从输入到返回结果的完整过程。 |
| process flow | 流程图；流程 | An ordered representation of the search stages. | 展示搜索各步骤先后关系的流程。 |
| process node | 流程节点 | One stage in a multi-step workflow. | 流程中的一个环节。 |
| five-step process | 五步流程 | Encode, compare, rank, filter, and return. | 编码、比较、排序、过滤、返回五个阶段。 |
| Encode | 编码 | Step 1 of the page's process. | 页面流程的第一步。 |
| Compare | 比较 | Step 2 of the page's process. | 页面流程的第二步。 |
| Rank | 排序 | Step 3 of the page's process. | 页面流程的第三步。 |
| Filter | 过滤 | Step 4 of the page's process. | 页面流程的第四步。 |
| Return | 返回 | Step 5 of the page's process. | 页面流程的第五步。 |
| help article | 帮助文章 | An article that may answer a user's question. | 帮助用户解决问题的资料文章。 |
| help articles | 帮助文章 | A collection of support articles. | 一组帮助和支持资料。 |
| password change | 密码更改 | The example task of changing a password. | 用户想修改密码的常见问题。 |
| change my password | 修改我的密码 | The example search query on the page. | 用户输入的“如何修改密码”问题。 |
| relevant help article | 相关帮助文章 | A support article matching a password question. | 与用户问题最有关的帮助资料。 |
| most relevant help articles | 最相关的帮助文章 | The best support articles returned for the query. | 搜索后最能回答问题的帮助文章。 |
| relevant | 相关的 | Connected or useful for the current query. | 和当前问题有关系、能帮上忙的。 |
| relevance | 相关性 | How useful a result is for the query. | 一个结果对当前问题有多有用。 |
| product catalog | 产品目录；商品目录 | A collection of product records. | 集中记录商品信息的目录。 |
| product catalog vector | 产品目录向量 | A vector representing a catalog item. | 表示目录中商品的一串数字。 |
| product description | 产品描述 | Text describing a product. | 介绍商品特点、用途等的文字。 |
| product descriptions | 产品描述 | Textual descriptions for multiple products. | 多个商品的说明文字。 |
| similar catalog vector | 相似目录向量 | A catalog vector close to the input vector. | 和输入向量接近的商品目录向量。 |
| similar catalog vectors | 相似目录向量 | Multiple catalog vectors close to the input. | 和输入内容相近的一组商品向量。 |
| matching product | 匹配产品；匹配商品 | A product whose vector is similar to the input. | 向量表示与输入相近的商品。 |
| matching products | 匹配产品 | Products returned as similar catalog items. | 搜索后找出的相似商品。 |
| similar product | 相似产品 | A product with a nearby vector representation. | 数字表示接近、可能相似的商品。 |
| product matching | 产品匹配 | Finding products similar to a description or item. | 根据描述或商品找相似商品。 |
| product review | 产品审核；商品复核 | Reviewing products found by a search. | 对匹配出来的商品再检查。 |
| review | 审核；复核 | Examine returned candidates for suitability. | 对搜索结果做进一步检查。 |
| real-world example | 现实世界例子 | An example showing a practical use. | 说明技术在真实场景如何使用的例子。 |
| everyday example | 日常例子 | The help-article search example. | 页面里的普通生活场景例子。 |
| business example | 商业例子 | The product-catalog matching example. | 页面里的企业商品匹配例子。 |
| input | 输入 | Data supplied to a system or process. | 送进系统、准备处理的内容。 |
| output | 输出 | The result produced by a system or process. | 系统处理后给出的结果。 |
| AI / System | AI／系统 | The component performing the search. | 负责执行向量搜索的 AI 或软件系统。 |
| keyword search | 关键词搜索 | Search that matches literal words or text patterns. | 按文字中是否出现关键词来查找。 |
| Keyword Search | 关键词搜索 | Literal term matching rather than vector comparison. | 看词面是否匹配的搜索方式。 |
| literal term | 字面术语 | An exact word or phrase in text. | 原文中实际出现的词或短语。 |
| text pattern | 文本模式 | A literal pattern matched in text. | 在文字中按固定形式匹配的模式。 |
| literal match | 字面匹配 | Matching exact words or text forms. | 词语或文字形式相同才算匹配。 |
| exact match | 精确匹配 | A match requiring the same term or value. | 要求词语或值完全相同的匹配。 |
| learned representation comparison | 学习表示比较 | Comparing model-created representations. | 比较模型学到的数字表示，而不是只看原词。 |
| representation-based search | 基于表示的搜索 | Search using encoded representations. | 按内容的数字表示来搜索。 |
| embedding creation | 嵌入创建 | Producing a vector from input data. | 把输入数据变成向量。 |
| embedding generation | 嵌入生成 | Generating an embedding for a query or item. | 为查询或对象生成向量表示。 |
| query encoding | 查询编码 | Encoding the query into a vector. | 把查询转成查询向量。 |
| vector comparison | 向量比较 | Comparing two or more vectors. | 计算多组数字向量之间的关系。 |
| vector ranking | 向量排序 | Ranking candidates by vector similarity. | 按向量相似程度排列候选。 |
| vector filtering | 向量过滤 | Combining vector matching with constraints. | 在向量匹配后再按条件筛选。 |
| vector retrieval | 向量检索 | Retrieving records using vector similarity. | 按向量相似度找回资料。 |
| semantic search | 语义搜索 | Search based on meaning rather than exact words. | 不要求词完全一样，而是按意思查找。 |
| meaning-based search | 基于含义的搜索 | Search using represented meaning. | 根据内容表达的含义来搜索。 |
| lexical search | 词法搜索 | Search based mainly on literal words. | 主要根据字面词语查找。 |
| full-text search | 全文搜索 | Search over text using words or patterns. | 在整段文字中查找词语或模式。 |
| keyword matching | 关键词匹配 | Matching query words against text words. | 把查询关键词和文字中的词进行匹配。 |
| record retrieval | 记录检索 | Finding records from a stored collection. | 从已保存的数据集合中找记录。 |
| information retrieval | 信息检索 | The broader task of finding relevant information. | 从大量资料中找出相关信息的任务。 |
| search index | 搜索索引 | A structure that supports efficient search. | 帮助系统更快找到结果的数据结构。 |
| vector index | 向量索引 | An index organized for vector similarity search. | 为快速查找相似向量建立的索引。 |
| indexed vector | 已索引向量 | A vector placed in a search index. | 已加入搜索索引、可被查询的向量。 |
| vector database | 向量数据库 | A database designed to store and search vectors. | 专门保存并查找向量的数据库。 |
| vector store | 向量存储 | A system that stores vectors and associated data. | 保存向量及其相关资料的系统。 |
| database record | 数据库记录 | A stored entry containing vector or metadata fields. | 数据库中保存的一条资料。 |
| collection | 数据集合 | A group of stored records or vectors. | 一组集中保存的记录或向量。 |
| corpus | 语料库；资料集合 | A collection of documents or items to search. | 用来搜索的一大批资料。 |
| document | 文档 | A text item that can be represented or retrieved. | 可以被编码和检索的文字资料。 |
| text | 文本 | Written language used as input or source content. | 可以作为查询或来源的文字。 |
| source text | 来源文本 | Original text associated with a record. | 记录背后对应的原始文字。 |
| image | 图像；图片 | Visual data that can be represented as a vector. | 可以转换成向量的图片资料。 |
| other data | 其他数据 | Data types beyond text or images. | 除文字和图片之外的其他资料。 |
| data item | 数据项 | One piece of data represented or searched. | 被处理或搜索的一份数据。 |
| source record | 来源记录 | The original stored record behind a result. | 搜索结果所对应的原始记录。 |
| attached metadata | 附带元数据 | Metadata stored alongside a vector or record. | 和向量或记录一起保存的说明信息。 |
| permissions metadata | 权限元数据 | Metadata describing access permissions. | 说明哪些人可以访问资料的信息。 |
| freshness metadata | 新鲜度元数据 | Metadata describing recency or update time. | 说明资料新旧或更新时间的信息。 |
| attribute | 属性 | A field used to describe or filter a record. | 描述记录、也可用于筛选的字段。 |
| filter condition | 过滤条件 | A condition a returned record must meet. | 结果必须符合的筛选要求。 |
| access control | 访问控制 | Rules controlling access to retrieved records. | 控制谁能查看或使用检索结果。 |
| freshness constraint | 新鲜度约束 | A restriction based on record recency. | 只允许较新或指定时间内的资料。 |
| similarity score | 相似度分数 | A number representing similarity. | 表示两个向量有多像的分数。 |
| distance score | 距离分数 | A value representing separation between vectors. | 表示两个向量相差多远的数值。 |
| score | 分数 | A numeric value used for ranking. | 帮助排序的数字。 |
| ordering | 顺序排列 | Arranging results from more to less suitable. | 把结果按优先级排好顺序。 |
| relevance score | 相关性分数 | A score estimating usefulness for the query. | 估计结果和问题有多相关的数字。 |
| retrieval quality | 检索质量 | How well a system returns useful records. | 系统找回相关资料的效果好不好。 |
| search quality | 搜索质量 | How well search results satisfy the query. | 搜索结果是否准确有用。 |
| recall | 召回率 | The share of relevant items that are found. | 相关资料中有多少被找回来。 |
| precision | 精确率 | The share of returned items that are relevant. | 返回的资料中有多少真正相关。 |
| recall@k | 前 k 项召回率 | Relevant items found among the top k results. | 前 k 个结果找回了多少相关内容。 |
| precision@k | 前 k 项精确率 | The relevant fraction among the top k results. | 前 k 个结果里有多少是相关的。 |
| MRR | 平均倒数排名 | Mean reciprocal rank of the first relevant result. | 看第一个相关结果平均排得多靠前。 |
| mean reciprocal rank | 平均倒数排名 | An evaluation metric for the rank of a relevant result. | 用相关结果排名的倒数评价搜索。 |
| NDCG | 归一化折损累计增益 | A metric for graded relevance and ranking order. | 同时考虑相关程度和排列顺序的指标。 |
| normalized discounted cumulative gain | 归一化折损累计增益 | A ranking metric that discounts lower positions. | 越靠后的结果权重越低的排序指标。 |
| latency | 延迟 | Time from query to returned results. | 从提出查询到收到结果所花的时间。 |
| throughput | 吞吐量 | The amount of search work handled per unit time. | 单位时间能处理多少查询或向量。 |
| scalability | 可扩展性 | Ability to keep working as data or traffic grows. | 数据量和请求量变大后还能否正常工作。 |
| approximate nearest neighbor | 近似最近邻 | A fast method for finding nearly closest vectors. | 用近似方式快速找最接近的向量。 |
| ANN | 近似最近邻（ANN） | Abbreviation for approximate nearest neighbor. | approximate nearest neighbor 的缩写。 |
| nearest-neighbor search | 最近邻搜索 | Search for vectors closest to a query vector. | 找离查询向量最近的对象。 |
| k-nearest-neighbor search | k 近邻搜索 | Search for the k closest vectors. | 找距离最近的 k 个向量。 |
| cosine similarity | 余弦相似度 | A measure comparing the direction of vectors. | 比较两串数字方向有多接近。 |
| dot product | 点积 | A calculation combining corresponding vector values. | 对应数字相乘再相加的计算。 |
| Euclidean distance | 欧氏距离 | Straight-line distance between vectors. | 数字空间中两点间的直线距离。 |
| Manhattan distance | 曼哈顿距离 | Distance measured by summing coordinate differences. | 把各维度差值相加得到的距离。 |
| similarity metric | 相似度指标 | A chosen mathematical measure of similarity. | 用来计算相似程度的数学方法。 |
| vector dimension | 向量维度 | The number of numeric coordinates in a vector. | 一串向量里有多少个数字位置。 |
| dimensionality | 维度数量 | The number of dimensions in a vector space. | 向量空间有多少个方向或位置。 |
| coordinate | 坐标 | One numeric position in a vector. | 向量中的一个数字位置。 |
| high-dimensional vector | 高维向量 | A vector with many coordinates. | 包含很多数字维度的向量。 |
| dense vector | 稠密向量 | A vector with values in most coordinates. | 大多数位置都有数字的向量。 |
| sparse vector | 稀疏向量 | A vector with many zero or empty coordinates. | 很多位置为零或没有值的向量。 |
| vector space | 向量空间 | A mathematical space where vectors are represented. | 放置和比较向量的数学空间。 |
| semantic space | 语义空间 | A vector space organized around meaning. | 让含义相近的内容位置接近的数字空间。 |
| feature space | 特征空间 | A space whose coordinates represent features. | 用特征维度表示对象的空间。 |
| embedding space | 嵌入空间 | The space containing embedding vectors. | 存放嵌入向量并比较它们的空间。 |
| representation space | 表示空间 | The selected space for vector representations. | 放置数字表示、比较对象关系的空间。 |
| neighborhood | 邻域 | The local area around a vector. | 某个向量周围的一小片相近区域。 |
| nearest neighbor | 最近邻 | An item whose vector is closest to another vector. | 向量位置最接近的对象。 |
| neighbor | 邻居；邻近对象 | A vector located near another vector. | 在数字空间中靠近另一个对象的向量。 |
| similarity neighborhood | 相似邻域 | The group of vectors near a query. | 查询向量周围的一组相似对象。 |
| RAG | 检索增强生成（RAG） | Generation that uses retrieved records as context. | 先找资料，再用资料帮助生成回答。 |
| retrieval-augmented generation | 检索增强生成 | A workflow that grounds generation in retrieved information. | 用检索到的资料增强模型生成。 |
| retrieved context | 检索上下文 | Retrieved text supplied to a generation model. | 搜索后交给生成模型参考的资料。 |
| model context | 模型上下文 | Information supplied to a model for generation. | 生成时提供给模型参考的信息。 |
| grounding | 基于依据；落地 | Supporting an answer with source information. | 让回答有检索到的资料作为依据。 |
| context | 上下文 | Information used to interpret or generate an answer. | 帮助模型理解和回答的背景资料。 |
| final answer | 最终答案 | The answer produced after retrieval or generation. | 用户最后看到的回答。 |
| answer generation | 答案生成 | Producing an answer after finding relevant records. | 找到资料后生成最终回答。 |
| recommendation | 推荐 | A suggested item chosen as useful or similar. | 系统认为值得查看的建议对象。 |
| recommend | 推荐 | Suggest an item or result to a user. | 向用户建议某个对象或结果。 |
| lookup | 查找 | Finding an existing item or record. | 在已有资料中查找内容。 |
| search | 搜索 | Find relevant items for a query. | 根据问题寻找相关资料。 |
| search system | 搜索系统 | Software that compares and returns records. | 负责比较并返回资料的软件系统。 |
| query input | 查询输入 | The data submitted for a search. | 送进搜索系统的查询内容。 |
| result set | 结果集 | The records returned for a query. | 一次搜索返回的一组结果。 |
| matching result | 匹配结果 | A returned item judged similar to the query. | 被认为与查询相似而返回的结果。 |
| possible match | 可能匹配 | An item that may be relevant after comparison. | 比较后可能符合要求的对象。 |
| relevant record | 相关记录 | A record useful for answering or completing the query. | 对当前问题或任务有帮助的记录。 |
| output record | 输出记录 | A record sent back by the search system. | 搜索系统输出的一条记录。 |
| search candidate | 搜索候选 | An item considered during search. | 搜索过程中被考虑的对象。 |
| candidate ranking | 候选排序 | Ordering possible matches by score. | 按分数排列候选结果。 |
| constraint-aware retrieval | 感知约束的检索 | Retrieval that respects metadata, permissions, or freshness. | 检索时同时遵守属性、权限和时效条件。 |
| filtered retrieval | 过滤后检索 | Retrieval after applying constraints. | 先按条件筛选，再返回相关资料。 |
| hybrid retrieval | 混合检索 | Retrieval combining vector and other search methods. | 把向量搜索和其他搜索方式结合。 |
| hybrid search | 混合搜索 | Search combining semantic and keyword matching. | 同时按含义和关键词查找。 |
| reranking | 重排序 | Reordering retrieved candidates with a second scorer. | 先找候选，再用另一套方法重新排列。 |
| second-stage ranking | 第二阶段排序 | A later, more detailed ranking step. | 在初步排序后再做一次更精细排序。 |
| bi-encoder | 双编码器 | An architecture encoding query and candidate separately. | 查询和候选分别编码、适合快速召回的架构。 |
| cross-encoder | 交叉编码器 | A model scoring a query and candidate together. | 把查询和候选一起输入、通常更精细但更慢的模型。 |
| query-document pair | 查询-文档对 | A query and document evaluated together. | 放在一起判断相关性的查询和文档。 |
| relevance judgment | 相关性判断 | A decision about whether a result is relevant. | 判断一个结果是否真的有用。 |
| ground truth | 真实答案；标注真值 | The reference relevance or answer used for evaluation. | 评估时用来对照的正确标注。 |
| evaluation set | 评估集 | Queries and references used to test retrieval. | 用来测试搜索效果的一组问题和标准答案。 |
| retrieval evaluation | 检索评估 | Measuring how well retrieval returns relevant items. | 用指标检查检索效果。 |
| vector search engine | 向量搜索引擎 | Software optimized for similarity search. | 专门快速查找相似向量的软件。 |
| index build | 索引构建 | Creating a search index from stored vectors. | 根据保存的向量建立可搜索索引。 |
| index rebuild | 索引重建 | Recreating an index after data or model changes. | 数据或模型变化后重新建立索引。 |
| re-embedding | 重新嵌入 | Generating vectors again with updated inputs or models. | 用新模型或新资料重新生成向量。 |
| embedding version | 嵌入版本 | The version of the model or representation scheme. | 生成向量所用模型或方案的版本。 |
| model version compatibility | 模型版本兼容性 | Whether vectors from different model versions can be compared. | 不同模型版本生成的向量能否直接混用。 |
| vector compatibility | 向量兼容性 | Whether vectors share a comparable representation space. | 不同向量是否能放在一起公平比较。 |
| embedding drift | 嵌入漂移 | Change in vector behavior after model or data shifts. | 模型或数据变化后向量关系发生改变。 |
| data drift | 数据漂移 | Change in the distribution of incoming data. | 新数据和原来数据的分布发生变化。 |
| domain shift | 领域变化 | A change between training and use domains. | 实际使用领域和模型原来接触的领域不同。 |
| out-of-domain data | 域外数据 | Data outside the model's expected domain. | 超出模型适用范围的数据。 |
| semantic equivalence | 语义等价 | Different wording expressing the same meaning. | 说法不同但意思相同。 |
| paraphrase | 改写；释义 | A restatement with similar meaning. | 用不同说法表达相近意思。 |
| polysemy | 多义性 | One word having multiple meanings. | 一个词在不同语境有多个意思。 |
| context sensitivity | 上下文敏感性 | Dependence of representation on surrounding context. | 同一个词因上下文不同而表示不同。 |
| hallucination | 幻觉 | An unsupported or incorrect generated claim. | 模型没有依据却生成了错误内容。 |
| factual correctness | 事实正确性 | Whether content is true, independent of similarity. | 内容是否真实，不等于它和查询相似。 |
| business suitability | 业务适用性 | Whether a result satisfies business requirements. | 结果是否符合权限、库存等实际业务要求。 |
| duplicate detection | 重复检测 | Finding records that may represent the same item. | 判断两个记录是不是其实是同一个对象。 |
| privacy | 隐私 | Protection of sensitive data used in search. | 防止敏感资料被不当搜索或暴露。 |
| security | 安全 | Protection of the search system and its data. | 保护向量、数据库和接口不被滥用。 |
| data deletion | 数据删除 | Removing source data and its associated vector. | 删除原始资料时也清掉对应向量。 |
| API | 应用程序接口（API） | An interface used to call an embedding or search service. | 程序调用模型或搜索服务的入口。 |
| embedding API | 嵌入接口 | An API that creates embeddings. | 用程序请求生成向量的接口。 |
| search API | 搜索接口 | An API that submits queries and returns results. | 用程序发起搜索并取得结果的接口。 |
| visual explainer | 可视化讲解 | A video or visual explanation of the topic. | 用视频或图像解释主题的内容。 |
| independent explainer | 独立讲解 | A supplementary explainer separate from the article. | 独立于正文的补充讲解。 |
| video | 视频 | The media resource attached to the topic. | 页面附带的视频资源。 |
| poster | 视频海报图 | The preview image for the video. | 视频播放前显示的预览图片。 |
| captions | 字幕 | Text displayed with a video. | 视频中同步显示的文字。 |
| subtitle | 字幕 | A text track for spoken video content. | 视频语音对应的文字轨道。 |
| visual explainer video | 可视化讲解视频 | A video explaining vector search visually. | 用画面解释向量搜索的视频。 |
| concept tree | 概念链 | An ordered chain of related concepts. | 把相关概念按流程串起来的链条。 |
| Query → Embedding → Vector Index → Similarity Search → Retrieved Records | 查询→嵌入→向量索引→相似搜索→检索记录 | The page's concept chain for vector search. | 从用户问题到最终找回记录的概念流程。 |
| Query | 查询 | The first node in the page's concept chain. | 概念链起点：用户想查找的内容。 |
| Embedding | 嵌入 | The representation node after the query. | 概念链中把查询变成向量的环节。 |
| Vector Index | 向量索引 | The indexed structure used for vector lookup. | 帮助快速查找向量的索引结构。 |
| Similarity Search | 相似搜索 | Searching by vector closeness. | 按向量相似程度查找。 |
| Retrieved Records | 检索记录 | Records returned after similarity search. | 相似搜索后找回的资料记录。 |
| Explore next | 继续探索 | A prompt to inspect related topics. | 页面建议继续学习的相关内容。 |
| related concept | 相关概念 | A concept connected to vector search. | 和向量搜索有联系的概念。 |

## Potential Missing Concepts

- **approximate nearest neighbor / ANN（近似最近邻）**：页面讲“closest matches”和向量距离，但没有说明大规模系统如何用近似算法加速最近邻搜索。
- **exact nearest neighbor（精确最近邻）**：页面没有区分精确找到最近向量与近似找到候选。
- **vector index（向量索引）**：概念链列出 Vector Index，但没有介绍索引结构、建立或更新方式。
- **inverted index（倒排索引）**：页面提到 keyword search，但没有解释关键词搜索常用的索引结构。
- **HNSW（分层可导航小世界图）**：没有介绍常见的近似最近邻图索引。
- **IVF（倒排文件索引）**：没有介绍按向量簇缩小搜索范围的索引方法。
- **product quantization / PQ（乘积量化）**：没有介绍压缩向量以降低存储和搜索成本的方法。
- **vector quantization（向量量化）**：没有说明把连续向量压缩或离散化的技术。
- **cosine similarity（余弦相似度）**：页面只说 distance or similarity measure，没有指定具体公式。
- **dot product（点积）**：页面没有展开常用的向量比较计算。
- **Euclidean distance（欧氏距离）**：页面没有指定“distance”采用哪一种距离。
- **Manhattan distance（曼哈顿距离）**：页面没有讨论按坐标差绝对值求和的距离。
- **distance metric（距离度量）**：页面没有说明度量是否满足数学距离的性质。
- **similarity score direction（相似度分数方向）**：没有解释分数越高越相似、距离越小越相似的方向差别。
- **embedding dimension（嵌入维度）**：页面没有说明向量包含多少维，以及维度对效果的影响。
- **curse of dimensionality（维度灾难）**：没有讨论高维空间中距离区分度和索引效率的问题。
- **normalization（归一化）**：没有解释向量长度归一化如何影响余弦相似度和点积。
- **dense retrieval（稠密检索）**：页面讲 learned representations，但没有给出 dense retrieval 这一检索范式名称。
- **sparse retrieval（稀疏检索）**：页面讲 keyword search，但没有以 sparse retrieval 的形式展开。
- **hybrid search（混合搜索）**：页面对照 vector search 和 keyword search，却没有介绍结合两者的检索策略。
- **query expansion（查询扩展）**：没有介绍改写或扩充查询以找回更多相关结果。
- **query rewriting（查询重写）**：没有说明在编码前如何清理、改写或补充查询。
- **metadata filtering（元数据过滤）**：页面列出 metadata constraints，但没有说明过滤是在向量召回前还是后执行。
- **pre-filtering（预过滤）**：没有讨论先按权限、类别或时间筛选候选再做向量搜索。
- **post-filtering（后过滤）**：没有讨论先召回相似结果再过滤可能导致结果不足的问题。
- **filter recall loss（过滤造成的召回损失）**：没有讨论严格过滤如何漏掉原本相关的结果。
- **reranking（重排序）**：页面只有 rank step，没有讲初步召回后的二次排序。
- **bi-encoder（双编码器）**：没有介绍查询和文档分别编码的高效架构。
- **cross-encoder（交叉编码器）**：没有介绍将查询和候选一起评分的精排架构。
- **retrieval-augmented generation（检索增强生成全称）**：页面给出 RAG，但没有完整展开英文名称。
- **RAG context window（RAG 上下文窗口）**：没有讨论检索结果如何适配生成模型的上下文限制。
- **context compression（上下文压缩）**：没有说明如何压缩过长的检索结果。
- **chunking（分块）**：页面讲 records and source text，但没有说明长文档如何切成可检索片段。
- **document chunk（文档块）**：没有说明返回完整文档还是其中的片段。
- **chunk overlap（分块重叠）**：没有讨论相邻片段之间是否保留重叠文本。
- **parent-child retrieval（父子文档检索）**：没有介绍用小片段召回、再返回较大上下文的设计。
- **multi-vector retrieval（多向量检索）**：没有讨论一个对象由多个向量表示的检索方法。
- **late interaction（延迟交互）**：没有介绍细粒度 token 向量交互式检索。
- **embedding model training（嵌入模型训练）**：页面使用 embedding model，但没有解释模型如何学会表示。
- **representation learning（表示学习）**：页面出现 representation，但没有定义表示学习过程。
- **contrastive learning（对比学习）**：没有说明用相似和不相似样本塑造向量空间的方法。
- **positive pair / negative pair（正样本对／负样本对）**：没有说明训练时哪些对象应该靠近或远离。
- **multimodal embedding（多模态嵌入）**：页面提到 other data，但没有讨论文本、图像等是否共享空间。
- **cross-modal retrieval（跨模态检索）**：没有展开用文本搜索图片或用图片搜索文本。
- **embedding quality（嵌入质量）**：页面描述相似表示，但没有给出评价表示质量的方法。
- **retrieval quality（检索质量）**：页面没有定义如何系统评估搜索质量。
- **recall@k（前 k 项召回率）**：页面没有给出召回覆盖率指标。
- **precision@k（前 k 项精确率）**：页面没有给出前 k 项相关程度指标。
- **MRR（平均倒数排名）**：页面没有给出强调首个相关结果排位的指标。
- **NDCG（归一化折损累计增益）**：页面没有给出同时考虑相关性和排序的指标。
- **latency（延迟）**：页面没有讨论查询到返回的时间。
- **throughput（吞吐量）**：页面没有讨论单位时间可处理的请求数。
- **storage cost（存储成本）**：没有讨论保存大量高维向量的空间和费用。
- **compute cost（计算成本）**：没有讨论编码、索引和搜索的计算资源。
- **model version compatibility（模型版本兼容性）**：没有说明不同 embedding model 版本的向量是否能混用。
- **embedding drift（嵌入漂移）**：没有讨论模型更新或数据变化导致向量关系改变。
- **out-of-domain data（域外数据）**：没有说明超出模型适用领域时相似度可能失真。
- **polysemy（多义词）**：页面说 meaning，但没有讨论一个词的多种含义。
- **context sensitivity（上下文敏感性）**：没有解释上下文如何改变同一文本的表示。
- **semantic equivalence（语义等价）**：没有单独定义不同措辞表达相同意思的情况。
- **paraphrase（释义／改写）**：没有展开同义改写在语义搜索中的作用。
- **data leakage（数据泄漏）**：没有说明训练或评估数据泄漏对检索结果的影响。
- **privacy（隐私）**：页面提到 source text and records，但没有讨论敏感内容保护。
- **access control（访问控制）**：页面提到 permissions constraints，但没有说明向量权限与原文权限如何同步。
- **data deletion（数据删除）**：没有说明删除原始记录时如何删除关联向量和索引项。
- **security（安全）**：没有讨论向量数据库、元数据和搜索接口的安全。
- **evaluation set（评估集）**：没有说明如何准备查询、相关记录和标注。
- **ground truth（真实答案／标注真值）**：没有说明如何判断结果是否确实相关。
- **human relevance judgment（人工相关性判断）**：页面有 product review，但没有说明人工如何评定结果。
- **business suitability（业务适用性）**：没有说明相关结果还要满足权限、库存、价格等业务条件。
- **similarity versus truth（相似度与真实性）**：没有明确提醒高相似度不保证内容真实或正确。
- **similarity versus causality（相似度与因果关系）**：没有说明向量接近不代表一个对象导致另一个对象。
- **exact match（精确匹配）**：页面对照 keyword search，但没有把 exact matching 单独定义。
- **lexical search（词法搜索）**：页面只用 keyword search 描述字面匹配，没有给出更宽的术语。
- **vector database（向量数据库）**：页面正文没有直接展开具体数据库实现。
- **embedding API（嵌入 API）**：页面没有说明应用如何调用服务生成查询向量。
- **batching（批处理）**：没有说明批量生成向量如何影响吞吐和成本。
- **online embedding（在线嵌入）**：没有区分请求到来时实时生成查询向量。
- **offline embedding（离线嵌入）**：没有区分提前生成并保存资料向量。
- **re-embedding（重新嵌入）**：没有说明模型升级或资料修订后的向量重建。
- **index rebuild（索引重建）**：没有说明向量更新后如何维护搜索索引。
- **deletion consistency（删除一致性）**：没有讨论原文、向量、元数据和索引同步删除。
- **freshness window（时效窗口）**：页面提到 freshness rules，但没有说明可接受的时间范围。
- **permission-aware search（权限感知搜索）**：页面列出 permissions，但没有说明如何避免越权召回。
- **source attribution（来源归因）**：页面说返回 metadata and source text，但没有说明如何展示引用来源。
- **result diversity（结果多样性）**：没有讨论避免 top-k 结果过度重复。
- **maximum marginal relevance / MMR（最大边际相关性）**：没有介绍同时平衡相关性和多样性的排序方法。
- **deduplication（去重）**：页面要求返回 matching records，但没有讨论重复记录如何处理。
- **false positive（假阳性）**：没有讨论返回看似相似但实际无关的结果。
- **false negative（假阴性）**：没有讨论漏掉真正相关结果的情况。
- **no-result handling（无结果处理）**：没有说明没有足够相似结果时系统如何响应。
- **similarity threshold（相似度阈值）**：没有说明低于某个分数是否应拒绝返回。
- **distance threshold（距离阈值）**：没有说明超过某个距离是否应视为不相关。
- **top-k selection（Top-k 选择）**：页面讲 closest matches，但没有说明 k 如何确定。
- **candidate generation（候选生成）**：没有把初步召回阶段作为独立工程概念展开。
- **retrieval pipeline（检索流水线）**：页面有五步流程，但没有给出完整工程管线名称。
- **online query serving（在线查询服务）**：没有讨论实时请求的服务化部署。
- **index update（索引更新）**：没有说明新增、修改和删除记录如何反映到索引。
- **sharding（分片）**：没有讨论大规模向量集合如何横向分布。
- **replication（复制）**：没有讨论搜索系统的副本和高可用。
- **filterable metadata（可过滤元数据）**：没有定义哪些元数据字段适合预过滤或后过滤。

## Aliases / Synonyms

- vector search ↔ Vector Search ↔ similarity search ↔ vector similarity search
- query ↔ search query ↔ query input ↔ user request ↔ current request
- query vector ↔ query embedding ↔ embedded query ↔ vectorized query
- stored vector ↔ indexed vector ↔ database vector ↔ candidate vector
- vector representation ↔ numerical representation ↔ embedding ↔ embedding vector
- vector space ↔ embedding space ↔ representation space ↔ semantic space
- similarity ↔ closeness ↔ proximity ↔ semantic similarity
- similarity measure ↔ similarity metric ↔ similarity function
- distance ↔ vector distance ↔ distance measure ↔ geometric distance
- most similar ↔ closest ↔ nearest ↔ highest-similarity
- nearest neighbor ↔ closest neighbor ↔ nearest item ↔ closest match
- nearest-neighbor search ↔ k-nearest-neighbor search ↔ closest-vector search
- retrieve ↔ find and return ↔ look up ↔ search and return
- retrieval ↔ information retrieval ↔ record retrieval ↔ vector retrieval
- result ↔ search result ↔ retrieved record ↔ returned record
- relevant ↔ related ↔ useful for the query ↔ pertinent
- rank ↔ order ↔ sort ↔ score and order
- ranking ↔ candidate ranking ↔ result ordering ↔ relevance ordering
- filter ↔ constrain ↔ restrict ↔ apply conditions
- metadata filter ↔ attribute filter ↔ structured filter ↔ filter condition
- permissions ↔ access control ↔ authorization constraints
- freshness ↔ recency ↔ currency ↔ up-to-dateness
- encode ↔ embed ↔ vectorize ↔ convert into a vector
- query encoding ↔ query embedding ↔ creating a query vector
- keyword search ↔ lexical search ↔ literal search ↔ full-text search
- keyword match ↔ literal match ↔ exact match ↔ term match
- semantic search ↔ meaning-based search ↔ representation-based search
- vector database ↔ vector store ↔ similarity-search database
- vector index ↔ similarity index ↔ approximate nearest-neighbor index
- RAG ↔ retrieval-augmented generation ↔ retrieval-enhanced generation
- retrieved context ↔ search context ↔ retrieval results supplied to generation
- product matching ↔ similar-product retrieval ↔ item matching
- product catalog ↔ catalog collection ↔ product database
- product description ↔ item description ↔ catalog description
- matching product ↔ similar product ↔ related product
- help article ↔ support article ↔ knowledge-base article
- source text ↔ original text ↔ source content
- source record ↔ original record ↔ database record
- top-k ↔ top k results ↔ k nearest items ↔ best k matches
- cosine similarity ↔ cosine score ↔ angular similarity
- dot product ↔ inner product
- Euclidean distance ↔ L2 distance
- ANN ↔ approximate nearest neighbor ↔ approximate nearest-neighbor search
- reranking ↔ re-ranking ↔ second-stage ranking
- bi-encoder ↔ dual encoder
- cross-encoder ↔ joint encoder
- recall@k ↔ top-k recall
- precision@k ↔ top-k precision
- MRR ↔ mean reciprocal rank
- NDCG ↔ normalized discounted cumulative gain
- dense vector ↔ dense embedding ↔ dense representation
- sparse vector ↔ sparse representation ↔ sparse embedding
- embedding quality ↔ representation quality
- retrieval quality ↔ search quality
- online embedding ↔ real-time embedding
- offline embedding ↔ precomputed embedding
- re-embedding ↔ embedding regeneration ↔ vector re-generation
- index rebuild ↔ index reconstruction
- freshness rule ↔ recency constraint ↔ freshness filter
- visual explainer ↔ visual explanation ↔ explainer video
- poster ↔ video poster ↔ preview image
- captions ↔ subtitles ↔ subtitle track

## Do Not Confuse Candidates

- **Vector search vs keyword search**：vector search 比较学习得到的向量表示；keyword search 主要匹配字面词语或文本模式。
- **Vector search vs embedding**：vector search 是查找相似已存向量的过程；embedding 是生成向量表示的结果或技术。
- **Vector search vs RAG**：vector search 返回相似记录；RAG 还要把检索结果作为上下文交给生成模型。
- **Vector search vs retrieval**：vector search 是一种搜索方法；retrieval 是找回相关资料这一更宽泛的任务。
- **Vector search vs generation**：vector search 选择已有记录；generation 产生新的回答或内容。
- **Vector search vs recommendation**：vector search 找到相似候选；recommendation 还包含向用户建议对象的产品或业务逻辑。
- **Embedding vs embedding model**：embedding 是模型产生的向量表示；embedding model 是负责生成它的模型。
- **Embedding vs vector**：embedding 强调表示概念或模型输出；vector 强调承载表示的一串数字。
- **Embedding vs query vector**：embedding 可以表示任何对象；query vector 特指当前查询的表示。
- **Query vector vs stored vector**：query vector 表示当前问题；stored vector 表示已保存、等待匹配的对象。
- **Vector vs vector space**：vector 是空间中的一个数字对象；vector space 是承载并比较许多向量的数学空间。
- **Vector space vs literal map**：向量空间是数字和数学关系的表示空间；地图类比不是实际地理地图。
- **Proximity vs geographic distance**：向量接近表示表示空间中的相似；不等于现实世界地点的地理距离。
- **Similarity vs distance**：相似度通常越高越接近；距离通常越小越接近，数值方向不能混淆。
- **Similarity vs truth**：高相似度不保证内容真实、正确或适合业务。
- **Similarity vs causality**：向量相似不说明一个对象导致另一个对象。
- **Similarity score vs relevance judgment**：分数是算法计算值；相关性判断还可能依赖任务标准或人工审核。
- **Nearest item vs best answer**：最近的对象只是最相似候选，不保证就是最终正确答案。
- **Retrieved record vs source record**：retrieved record 是本次搜索返回的记录；source record 强调原始来源记录。
- **Source text vs metadata**：source text 是实际原文；metadata 是描述来源、权限、时间等的附加信息。
- **Metadata vs vector**：metadata 描述对象；vector 用数字表示对象并参与相似度比较。
- **ID vs vector**：ID 负责识别记录；vector 负责表示内容并参与搜索。
- **Filter vs rank**：rank 按相似度排列结果；filter 按权限、属性或时效条件排除结果。
- **Filter vs rerank**：filter 删除不满足条件的候选；rerank 重新安排仍保留的候选顺序。
- **Keyword match vs semantic match**：keyword match 依赖词面重合；semantic match 可以识别不同措辞下的相近含义。
- **Exact match vs similarity match**：exact match 要求相同词或值；similarity match 允许表示接近但文字不同。
- **Semantic search vs keyword search**：semantic search 侧重含义；keyword search 侧重字面词语。
- **Vector database vs ordinary database**：普通数据库可以保存记录；向量数据库还需要高效支持向量相似度搜索。
- **Vector index vs vector database**：vector index 是用于查找的结构；vector database 是保存数据并提供查询能力的系统。
- **Vector index vs inverted index**：向量索引支持向量邻近搜索；倒排索引主要支持词项到文档的字面查找。
- **Nearest-neighbor search vs exact nearest-neighbor search**：前者可泛指最近邻搜索；exact 方法保证计算真实最近项，近似方法可能牺牲少量精度换速度。
- **ANN vs exact search**：ANN 追求快速找到近似最近项；exact search 追求严格的最近项结果。
- **Cosine similarity vs Euclidean distance**：余弦相似度通常比较方向；欧氏距离比较空间直线长度。
- **Cosine similarity vs dot product**：两者都可比较向量，但点积还受向量长度影响，不能直接当成同一指标。
- **Dense vector vs sparse vector**：dense vector 大多数维度有值；sparse vector 大量维度为零或空。
- **Dimension vs coordinate**：dimension 是空间或向量的维度数量；coordinate 是某一个具体位置的数值。
- **Embedding dimension vs vector count**：embedding dimension 是每个向量有多少数字；vector count 是集合里有多少个向量。
- **Recall@k vs precision@k**：recall@k 看相关项找回了多少；precision@k 看前 k 项中有多少相关。
- **MRR vs NDCG**：MRR 主要关注第一个相关结果排位；NDCG 可考虑多个结果及不同相关等级。
- **Latency vs throughput**：latency 是一次请求等待多久；throughput 是单位时间能处理多少请求。
- **Retrieval quality vs embedding quality**：embedding quality 关注表示本身；retrieval quality 还受索引、排序、过滤和数据覆盖影响。
- **Bi-encoder vs cross-encoder**：bi-encoder 分别编码查询和候选、适合快速召回；cross-encoder 联合评分、通常更精细但更慢。
- **Recall vs ranking quality**：召回关注是否找回来；排序质量关注找回后顺序是否合理。
- **Product matching vs recommendation**：product matching 是匹配商品；recommendation 是面向用户的建议行为。
- **Product matching vs duplicate detection**：商品匹配寻找相似商品；重复检测要判断是否是同一条记录或同一商品。
- **Help article vs final answer**：帮助文章是检索出的来源资料；最终答案是系统可能根据资料生成的回答。
- **Retrieved context vs source document**：retrieved context 是为当前查询选出的上下文；source document 是原始文档本身。
- **Chunk vs document**：chunk 是文档的一部分；document 是完整或更大的原始资料。
- **Embedding vs token**：token 是语言模型处理文本的单位；embedding 是对 token、文本或对象的数字表示。
- **Encoding vs retrieval**：encoding 生成向量；retrieval 使用向量找回记录。
- **Offline embedding vs online embedding**：offline embedding 提前生成并保存；online embedding 在请求到来时实时生成。
- **Index build vs index search**：index build 建立搜索结构；index search 使用该结构查找结果。
- **Model version vs vector compatibility**：模型版本变化可能改变向量空间，不能默认把新旧向量直接混搜。
- **Freshness vs relevance**：freshness 关注资料新旧；relevance 关注资料是否与查询相关。
- **Permissions vs relevance**：一个结果即使相关，也可能因权限不足不能返回。
- **Metadata filter vs semantic similarity**：元数据过滤按结构化字段限制；语义相似按向量表示比较。
- **RAG vs grounding**：RAG 是检索加生成的工作流；grounding 是让输出有外部资料依据的更宽概念。
- **Retrieval vs generation**：retrieval 找已有内容；generation 生成新内容。
- **Hallucination vs low similarity**：幻觉是生成内容缺乏依据或错误；低相似度只是检索匹配分数低。
- **Visual explainer vs glossary concept**：video、poster、captions 是页面呈现资源相关词，不是向量搜索机制本身。

## Notes

- 本文件是 `vector-search.html` 的 raw glossary 收集稿，按要求从正文、导航、流程卡片、示例、对照区、相关概念链和视频资源中尽可能保留候选，不做最终去重、归并或删减。
- 页面元信息为 `05 · Embeddings, RAG & Vector Search · Topic 03`；本任务指定的输出命名和模块编号为 `08-vector-search.md`，两套信息均保留在 Topic Metadata 中。
- 页面核心定义是：Vector search finds stored vectors that are most similar to a query vector；向量通常来自 embedding model，系统用 distance or similarity measure 比较它们。
- 页面进一步说明，搜索结果常以 matching records 返回，并可能同时带有 metadata 和 source text。
- 页面地图类比是：把 query 放到和 stored items 同一张“地图”上，附近 points 是可能匹配；该类比解释 proximity，不是 literal geographic distance。
- 页面明确给出五步流程：1. Encode / Create a query vector；2. Compare / Measure distance；3. Rank / Order candidates；4. Filter / Apply constraints；5. Return / Send results。
- Filter 阶段的约束候选包括 metadata、permissions 和 freshness rules；这些词应保留为机制、工程和边界候选。
- 日常例子是 help article：输入为 “How can I change my password?”；系统 searches nearby article vectors；输出为 most relevant help articles。
- 商业例子是 product catalog：输入为 a product description；系统 finds similar catalog vectors；输出为 matching products for review。
- 页面直接对照三组边界：Vector Search ≠ Keyword Search、Vector Search ≠ Embedding、Vector Search ≠ RAG。对照中的 keyword search、embedding、RAG 及各自定义均保留。
- 页面相关概念链是 `Query → Embedding → Vector Index → Similarity Search → Retrieved Records`；Explore next 列出 Embeddings、Retrieval、RAG、Grounding。
- 页面 Remember this 的核心边界是：Vector search finds nearby vector representations；it does not generate the final answer by itself。
- 页面正文出现 vector、query vector、stored vectors、embedding model、distance、similarity、metadata、source text、permissions、freshness、retrieval、generation 等重要专业词，不应因常见而删除。
- 页面没有给出具体距离或相似度公式；cosine similarity、dot product、Euclidean distance 等保留在 Potential Missing Concepts，同时作为可追踪的工程扩展候选。
- 页面没有给出具体指标；recall@k、precision@k、MRR、NDCG、latency、throughput 属于向量检索常见但页面未展开的指标候选。
- 页面没有讲索引实现；ANN、HNSW、IVF、PQ、vector index、reranking 等属于 Potential Missing Concepts，不应误写成页面已定义内容。
- 页面用 “nearby” 和 “closest” 表达相似位置；这不等于内容完全相同、事实正确、因果相关或业务上一定可用。
- 页面将 vector search 与 keyword search 区分：前者比较 learned representations，后者匹配 literal terms or text patterns；因此 semantic search、lexical search、exact match 作为相关候选保留。
- 页面将 vector search 与 RAG 区分：向量搜索返回 similar records；RAG uses retrieval results as model context for generation。
- 页面中的 `ID`、`metadata`、`source text`、`permission`、`freshness` 是结果可用性和访问边界的重要词，即使页面没有单独展开实现，也保留为 raw 候选。
- 页面两个实例分别覆盖 support search 和 product matching；help article、password change、product description、product review、recommendation 等例子词均保留。
- 页面视频区只标记 `Independent explainer`、`visual explainer`、`captions`、`poster` 和视频源文件；这些是低优先级呈现相关候选，不是向量搜索核心机制。
- 英文大小写形式（Vector Search、Keyword Search、Encode、Compare、Rank、Filter、Return、RAG）和复数形式（vectors、records、results、articles）在 raw 阶段保留为可追踪候选。
