# Topic

Reranking

## Topic Metadata

- Requested Module: 08
- Page Module: 08 · Embeddings, Search & RAG
- Page Topic: Topic 10 · Reranking
- Topic Title: What is Reranking?
- Source File: `reranking.html`
- Source Page Description: Reranking reorders retrieved results so the most useful candidates appear first.
- Collection Mode: Raw, maximum candidate collection; candidates are intentionally not deduplicated, merged, or reduced.

## Glossary Candidates

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Reranking | 重排序；重新排序 | Reordering results that have already been retrieved. | 把已经找到的结果重新排先后。 |
| reranking | 重排序；重新排序 | A second ordering of retrieved candidates. | 对检索出来的候选内容再排一次顺序。 |
| re-ranking | 重排序 | Another spelling of reranking. | reranking 的连字符写法。 |
| reranker | 重排序器；重排模型 | A component that examines candidates and orders them again. | 专门检查候选结果并重新排序的组件或模型。 |
| rerank | 重新排序 | Apply a second ranking operation. | 对结果进行第二次排序。 |
| rank | 排名；排序 | Put items in an order of relevance or value. | 按相关程度或价值排出名次。 |
| ranking | 排序；排名 | The process of assigning an order to items. | 给多个结果安排先后次序的过程。 |
| second-stage ranking | 第二阶段排序 | Ranking performed after an initial retrieval stage. | 初步检索后再进行的一轮排序。 |
| second-stage step | 第二阶段步骤 | A later step applied to the initial results. | 在第一轮结果之后进行的后续步骤。 |
| ranking step | 排序步骤 | One step that orders candidate items. | 把候选项排出先后的一个步骤。 |
| first-stage retrieval | 第一阶段检索 | The fast initial search that gathers possible matches. | 先快速找出可能相关内容的第一轮搜索。 |
| initial retrieval | 初始检索；初步检索 | The first search that finds possible candidates. | 先找出候选结果的初步检索。 |
| initial search | 初次搜索；初步搜索 | A quick first search for possible matches. | 先快速寻找可能匹配内容的搜索。 |
| retrieval | 检索 | Find and return potentially relevant information. | 从资料中找回可能相关的信息。 |
| retrieved results | 已检索结果 | Results returned by an earlier retrieval step. | 前面检索阶段已经找出来的结果。 |
| retrieved candidates | 已检索候选项 | Candidate items returned by retrieval. | 检索得到、等待进一步判断的候选内容。 |
| candidate | 候选项 | An item that may match the query. | 可能符合问题要求的一个选项。 |
| candidates | 候选项；候选结果 | Items being considered for final ordering. | 正在被比较和排序的一批可能结果。 |
| candidate result | 候选结果 | A result found before final selection. | 找到但还没有排定最终位置的结果。 |
| candidate results | 候选结果 | A set of possible results from search. | 搜索返回的一组可能答案或内容。 |
| candidate set | 候选集合 | The group of items passed to a reranker. | 交给重排序器处理的一批候选项。 |
| possible match | 可能匹配项 | An item that might satisfy the request. | 可能符合用户请求的内容。 |
| possible matches | 可能匹配项 | Multiple items that might be relevant. | 可能与请求相关的多个内容。 |
| relevant | 相关的 | Connected to what the user is asking for. | 和用户要找的东西有关。 |
| relevance | 相关性 | How well an item matches the query. | 一个结果和问题匹配得有多好。 |
| most relevant | 最相关的 | Matching the query better than the other candidates. | 在候选结果中最符合问题的。 |
| useful | 有用的 | Helpful for the user or downstream system. | 对用户或后续系统有帮助的。 |
| most useful candidates | 最有用的候选项 | Candidates expected to help the user most. | 预计最能解决用户问题的候选内容。 |
| relevance score | 相关性分数 | A score expressing how well a candidate matches a query. | 用数字表示候选内容和问题有多匹配。 |
| relevance scores | 相关性分数 | Scores used to order candidates by relevance. | 用来按相关程度排序的分数。 |
| score | 分数；评分 | A numerical value assigned to a candidate. | 给一个候选结果打出的数字分。 |
| scoring | 打分；评分 | Calculating values that support ranking. | 计算分数以帮助决定先后。 |
| score relevance | 对相关性打分 | Evaluate candidate relevance numerically. | 用数字判断候选结果的相关程度。 |
| order | 顺序；排序 | The position of items relative to one another. | 多个结果之间的先后位置。 |
| improved order | 改进后的顺序 | A better ordering after reranking. | 重新打分后更有用的结果顺序。 |
| new relevance scores | 新的相关性分数 | Scores produced by the reranking step. | 重排序阶段重新算出的相关性分数。 |
| reorder | 重新排列 | Change the existing order of items. | 改变原来结果的先后顺序。 |
| sort | 排序 | Arrange items according to a value or score. | 按某个标准或分数排列内容。 |
| put the best first | 把最好的放在前面 | Place the strongest matches at the top. | 把最符合需求的结果排在最前面。 |
| top result | 顶部结果；排名靠前的结果 | A result near the beginning of the ordered list. | 排在结果列表前面的内容。 |
| top results | 顶部结果；前列结果 | The highest-ranked results. | 排名最高、最值得先看的结果。 |
| top result set | 顶部结果集合 | The small set selected from the highest ranks. | 从前几名中选出的较小结果集合。 |
| top-k results | Top-k 结果；前 k 个结果 | The first k items after ranking. | 排名后最前面的 k 个结果。 |
| smaller set | 更小的集合 | A reduced set passed to the next component. | 从大量候选中缩小出来的一组结果。 |
| strongest results | 最强结果；最可靠候选 | The candidates with the best reranking scores. | 重排序后分数最高、最值得使用的内容。 |
| pass results | 传递结果 | Send selected results to another component. | 把选出的结果交给后续模块。 |
| pass the strongest results | 传递最强结果 | Forward the highest-quality candidates downstream. | 把最值得用的候选结果传给下一步。 |
| query | 查询；查询语句 | The question or request used to search. | 用户输入、用来查找内容的问题或文字。 |
| read the request | 读取请求 | Interpret the user request before searching. | 先看懂用户想要什么。 |
| request | 请求 | What the user asks the system to find or do. | 用户要求系统查找或完成的事情。 |
| user request | 用户请求 | A request made by the person using the system. | 使用者提出的问题或要求。 |
| identify what the user needs | 识别用户需求 | Determine the information the user is seeking. | 判断用户真正想找什么。 |
| user need | 用户需求 | The information or result that would help the user. | 用户希望得到的信息或结果。 |
| find candidates | 查找候选项 | Retrieve possible matches for the query. | 找出可能符合查询的内容。 |
| search returns possible matches | 搜索返回可能匹配项 | The first search produces items that might fit. | 搜索先返回一批可能合适的结果。 |
| compare candidates | 比较候选项 | Examine candidates against one another and the query. | 把候选内容相互比较，并和问题对照。 |
| compare candidates with the query | 将候选项与查询比较 | Judge each candidate in relation to the query. | 看每个候选结果和用户问题到底有多匹配。 |
| in more detail | 更详细地 | Use a more careful comparison than the first search. | 比第一轮搜索更仔细地分析。 |
| detailed comparison | 详细比较 | A close comparison of query and candidates. | 对问题和候选内容进行更细致的匹配。 |
| query understanding | 查询理解 | Understanding the intent and details of a query. | 理解用户问题的意图和具体要求。 |
| query intent | 查询意图 | What the user means to find or accomplish. | 用户提出查询时真正想完成的目标。 |
| result list | 结果列表 | An ordered list of returned items. | 搜索或检索返回的结果清单。 |
| search result | 搜索结果 | An item returned by a search. | 搜索系统找回的一项内容。 |
| retrieved item | 检索项 | An item returned from a retrieval system. | 检索系统找回的一条内容。 |
| information retrieval | 信息检索 | Finding relevant information from a collection. | 在资料集合中找相关信息的技术。 |
| retriever | 检索器 | A component that quickly gathers candidate results. | 负责先快速找候选结果的组件。 |
| ranking model | 排序模型 | A model that scores or orders search results. | 给搜索结果打分并排序的模型。 |
| reranking model | 重排序模型 | A model used to reorder an initial candidate list. | 专门把第一轮候选结果重新排序的模型。 |
| relevance model | 相关性模型 | A model that estimates query-result relevance. | 估计问题和结果相关程度的模型。 |
| learned ranker | 学习型排序器 | A ranker trained to order items effectively. | 通过数据学习如何排列结果的排序器。 |
| first-pass ranker | 首轮排序器 | A fast ranker used before a more careful reranker. | 在精细重排序前快速排一次的排序器。 |
| two-stage retrieval | 两阶段检索 | Retrieve candidates first and rerank them second. | 先找候选、再精排的两步检索流程。 |
| multi-stage retrieval | 多阶段检索 | A retrieval pipeline with several filtering or ranking stages. | 经过多个筛选和排序阶段的检索流程。 |
| candidate generation | 候选生成 | Produce a manageable set of possible items. | 先生成一批可供后续判断的候选项。 |
| candidate retrieval | 候选检索 | Retrieve items that may be relevant. | 检索可能相关的候选内容。 |
| candidate filtering | 候选过滤 | Remove candidates that do not meet requirements. | 去掉明显不符合要求的候选项。 |
| coarse-to-fine retrieval | 从粗到细的检索 | Start with fast broad retrieval and then apply detailed ranking. | 先粗略快速查找，再细致判断排序。 |
| precision stage | 精排阶段 | The stage that improves the ordering of retrieved items. | 提高已检索结果顺序质量的阶段。 |
| recall stage | 召回阶段 | The stage focused on finding enough possible matches. | 尽量找全可能相关内容的阶段。 |
| fast search | 快速搜索 | Search optimized for speed and broad candidate coverage. | 重点是速度和找出候选项的搜索。 |
| careful examination | 仔细检查；精细分析 | A more detailed assessment of each candidate. | 对候选结果进行更认真、更细的判断。 |
| semantic similarity | 语义相似度 | Similarity based on meaning rather than exact words. | 根据意思相近程度，而不只是看字面是否一样。 |
| semantically similar vectors | 语义相似的向量 | Vectors positioned near one another because their meanings are similar. | 因为意思相近而在向量空间中接近的数字表示。 |
| vector search | 向量搜索 | Search that compares vector representations for semantic similarity. | 通过比较向量来找语义相似内容的搜索。 |
| vector | 向量 | An ordered list of numbers representing an item. | 用一串数字表示文字、文档或其他对象。 |
| embedding | 嵌入；向量表示 | A numerical representation used to compare meaning or features. | 把内容变成可比较的一串数字。 |
| dense retrieval | 稠密检索 | Retrieval using dense vector representations. | 用稠密向量找语义相关内容。 |
| lexical retrieval | 词法检索 | Retrieval based mainly on words or token overlap. | 主要根据词语或词元重合来搜索。 |
| keyword search | 关键词搜索 | Search based on matching important words. | 根据关键词查找内容。 |
| exact match | 精确匹配 | A match requiring the same or nearly identical text. | 文字相同或几乎相同才算匹配。 |
| hybrid search | 混合搜索 | Search combining lexical and vector retrieval. | 把关键词搜索和向量搜索结合起来。 |
| cross-encoder | 交叉编码器 | A model that reads a query and candidate together to score relevance. | 把问题和候选内容一起读后再打相关性分的模型。 |
| bi-encoder | 双编码器 | A model that encodes query and items separately for efficient retrieval. | 分别编码问题和内容、适合快速检索的模型。 |
| query-document pair | 查询—文档对 | A query and a document evaluated together. | 把一个问题和一篇文档配在一起判断是否相关。 |
| query-passage pair | 查询—段落对 | A query and a passage evaluated together. | 把查询和一段文字放在一起做相关性判断。 |
| pointwise reranking | 逐项重排序 | Score each candidate independently. | 一个候选一个候选地单独打分。 |
| pairwise reranking | 成对重排序 | Compare candidates in pairs to learn which should rank higher. | 两个候选一组比较谁应该排前面。 |
| listwise reranking | 列表式重排序 | Evaluate or optimize the ordering of a whole candidate list. | 从整张候选列表角度优化排序。 |
| query-document interaction | 查询—文档交互 | Detailed relationships between query terms and document content. | 详细比较问题和文档内容之间的对应关系。 |
| score fusion | 分数融合 | Combine scores from multiple retrieval or ranking methods. | 把多个搜索或排序方法的分数合在一起。 |
| RAG | 检索增强生成（RAG） | Generation that uses retrieved information to help answer. | 先查资料，再用查到的资料帮助生成答案。 |
| Retrieval-Augmented Generation | 检索增强生成 | A system pattern that retrieves information before generation. | 生成答案前先检索资料的系统方式。 |
| RAG assistant | RAG 助手 | An assistant that retrieves passages and uses them in generation. | 会先找资料再回答问题的 AI 助手。 |
| retrieved information | 检索到的信息 | Information found by a retrieval step. | 检索阶段找到的外部资料。 |
| generate an answer | 生成答案 | Produce a response using information and a model. | 根据信息和模型产出回答。 |
| answer generation | 答案生成 | The step that creates the final response. | 生成最终回答的步骤。 |
| application | 应用 | A product or workflow that consumes ranked results. | 使用这些排序结果的实际产品或流程。 |
| downstream application | 下游应用 | The application that receives results from retrieval. | 接收检索结果并继续处理的应用。 |
| model | 模型 | A computational system that scores or generates outputs. | 用来打分、排序或生成内容的计算程序。 |
| language model | 语言模型 | A model that processes or generates language. | 处理或生成文字的模型。 |
| passage | 段落；文本片段 | A smaller piece of a document sent to a model. | 从文档中截取、交给模型的一小段文字。 |
| passages | 段落；文本片段 | Multiple pieces of retrieved text. | 检索并传给模型的多段文字。 |
| top 3–5 passages | 前 3–5 个段落 | The three to five highest-ranked passages. | 重排序后最前面的三到五段资料。 |
| 20 candidates | 20 个候选项 | The example number of candidates retrieved before reranking. | 示例中第一轮找到的二十个候选结果。 |
| retrieve 20 candidates | 检索 20 个候选项 | Return twenty possible matches before reranking. | 先找出二十个可能相关的结果。 |
| send passages to the model | 将段落发送给模型 | Provide selected passages as model context. | 把选出的资料段落交给模型参考。 |
| context | 上下文；参考内容 | Information supplied to help a model respond. | 帮助模型回答问题的背景资料。 |
| shopping search | 购物搜索 | Search for products that meet a shopping request. | 根据购物需求查找商品。 |
| waterproof walking shoes | 防水步行鞋 | The example shopping query in the page. | 页面用来示范购物搜索的查询词。 |
| product | 产品；商品 | An item that can be returned by a shopping search. | 购物搜索中可以被找到的商品。 |
| products | 商品；产品 | Multiple items returned by a shopping search. | 购物搜索返回的多个商品。 |
| useful products first | 先显示有用商品 | Put the most useful shopping items at the top. | 把最符合需求的商品排在前面。 |
| input | 输入 | Information given to the search or ranking system. | 交给搜索或排序系统的信息。 |
| output | 输出 | The results returned after processing. | 系统处理后给出的结果。 |
| system | 系统 | The complete process that retrieves, reranks, and passes results. | 负责检索、重排并传递结果的整套机制。 |
| process | 流程；处理过程 | The sequence from query to top results. | 从提出问题到得到前列结果的一连串步骤。 |
| flow | 流程；流转 | The movement through ordered processing stages. | 信息依次经过各处理阶段的过程。 |
| process flow | 流程图；处理流程 | A sequence showing the stages of the system. | 展示系统各阶段先后关系的流程。 |
| workflow | 工作流 | A repeatable sequence of retrieval and ranking actions. | 可以重复执行的检索和排序步骤。 |
| pipeline | 流水线；处理管线 | Connected stages that transform a query into results. | 把查询逐步处理成结果的一组模块。 |
| query-to-results pipeline | 从查询到结果的管线 | The complete path from a request to ranked results. | 从用户问题走到排序结果的完整路径。 |
| librarian analogy | 图书管理员类比 | An analogy for retrieving books and sorting the stack. | 用图书管理员先找书、再把最好书放前面来理解重排。 |
| librarian | 图书管理员 | The person in the analogy who finds and sorts books. | 类比中先找书、再整理书的人。 |
| book | 书籍 | An item in the librarian analogy. | 类比检索结果的一本书。 |
| books | 书籍 | Multiple items in the librarian analogy. | 类比候选结果的一摞书。 |
| stack | 一摞；堆叠集合 | A group of possibly relevant books awaiting sorting. | 等待进一步整理的一摞候选内容。 |
| stack of possibly relevant books | 一摞可能相关的书 | The initial group gathered by the librarian analogy. | 类比第一轮搜索找到的一批可能相关内容。 |
| best matches on top | 把最佳匹配放在最上面 | Place the best matches first in the stack. | 把最符合要求的内容放到最前面。 |
| first search | 第一轮搜索 | The initial search before reranking. | 重排序前进行的第一次搜索。 |
| second search | 第二轮搜索 | An informal description sometimes used for reranking. | 对已有结果再判断的一轮处理；不一定是真正重新搜索。 |
| final selection | 最终选择 | The small group ultimately used or shown. | 最后真正展示或交给后续系统的结果。 |
| retrieval quality | 检索质量 | How well the retrieval stage finds useful candidates. | 第一轮能否找全有用候选结果的程度。 |
| ranking quality | 排序质量 | How well the ordered list puts useful items first. | 排序是否把真正有用的结果排在前面的程度。 |
| reranking quality | 重排序质量 | How much reranking improves the usefulness of the order. | 重排序后结果先后是否变得更有用。 |
| recall | 召回率 | The share of relevant items that were retrieved. | 所有相关内容里，第一轮找回了多少。 |
| recall@k | Top-k 召回率 | The share of relevant items appearing within the first k results. | 前 k 个结果覆盖了多少相关内容。 |
| precision | 精确率 | The share of returned items that are relevant. | 返回的结果里有多少真正相关。 |
| precision@k | Top-k 精确率 | The share of the first k results that are relevant. | 前 k 个结果里有多少真正相关。 |
| MRR | 平均倒数排名（MRR） | A metric that rewards the position of the first relevant result. | 相关结果第一次出现得越靠前，分数越高。 |
| Mean Reciprocal Rank | 平均倒数排名 | The expanded name of MRR. | MRR 的完整英文名称。 |
| MAP | 平均准确率均值（MAP） | A metric averaging precision across relevant results. | 综合多个相关结果位置来衡量排序效果的指标。 |
| Mean Average Precision | 平均准确率均值 | The expanded name of MAP. | MAP 的完整英文名称。 |
| NDCG | 归一化折损累计增益（NDCG） | A ranking metric that gives more credit to relevant items near the top. | 越相关且越靠前的结果贡献越大的排序指标。 |
| normalized discounted cumulative gain | 归一化折损累计增益 | The expanded name of NDCG. | NDCG 的完整英文名称。 |
| hit rate | 命中率 | The share of queries with at least one useful result. | 有至少一个有用结果的查询占比。 |
| top-k accuracy | Top-k 准确率 | Whether a correct or relevant item appears in the first k. | 正确或相关结果是否出现在前 k 个里。 |
| latency | 延迟 | Time taken to return the reranked results. | 用户等待重排序结果所花的时间。 |
| throughput | 吞吐量 | The number of queries a system handles per unit time. | 系统一段时间内能处理多少查询。 |
| candidate count | 候选数量 | The number of items sent into reranking. | 进入重排序阶段的候选结果数量。 |
| computational cost | 计算成本 | Resources needed to score candidates in detail. | 精细给很多候选打分所需的计算资源。 |
| trade-off | 权衡 | A balance between ranking quality, speed, and cost. | 在效果、速度和成本之间做平衡。 |
| relevance-performance trade-off | 相关性与性能权衡 | Balance between better ordering and system efficiency. | 更准确的排序和更快响应之间的平衡。 |
| application context | 应用上下文 | The product or workflow in which results are used. | 这些结果实际被使用的产品或流程环境。 |
| source | 来源；资料来源 | The document or item from which a passage comes. | 片段来自哪篇文档或哪条资料。 |
| document | 文档 | A source that can be retrieved as a result. | 可以被搜索和返回的资料。 |
| corpus | 文档集合；语料库 | The collection searched for candidate results. | 搜索系统可以查找的全部资料集合。 |
| index | 索引 | A structure that helps retrieve items quickly. | 帮助系统快速找到资料的数据结构。 |
| top results sent downstream | 传给下游的前列结果 | Highest-ranked results forwarded for use. | 排名前面的结果被传给后面的模块。 |

## Potential Missing Concepts

- **retriever vs reranker（检索器与重排序器）**：页面通过“initial retrieval”和“reranker”说明两者顺序，但没有展开两类组件的输入、输出和模型差异。
- **two-stage retrieval（两阶段检索）**：页面描述了先初步检索、后重排序的结构，但没有给出该流程的正式术语。
- **candidate generation（候选生成）**：页面说 initial retrieval finds candidates，但没有说明如何从大型文档库生成可处理的候选集合。
- **top-k（前 k 个）**：页面使用 smaller set 和 top 3–5，但没有定义 k 或 top-k 截断策略。
- **precision / recall（精确率／召回率）**：页面强调“最有用的候选项”，但没有给出检索质量指标。
- **MRR / MAP / NDCG（排序指标）**：页面没有明确列出平均倒数排名、平均准确率均值或归一化折损累计增益。
- **hit rate（命中率）**：页面没有说明“至少一个相关结果出现在前列”的衡量方式。
- **cross-encoder（交叉编码器）**：页面没有说明常见 reranker 如何同时读取 query 和 candidate 并进行精细打分。
- **bi-encoder（双编码器）**：页面没有把初始向量检索器与精排模型的编码方式进行比较。
- **BM25（BM25 排序）**：页面提到 first search，但没有说明关键词检索或 BM25 这类初始检索方法。
- **dense retrieval / lexical retrieval（稠密检索／词法检索）**：页面给出 vector search 的对照，但没有分类说明不同检索范式。
- **hybrid search（混合搜索）**：页面没有讨论如何融合向量搜索与关键词搜索的候选或分数。
- **query-document interaction（查询—文档交互）**：页面说 compare candidates with the query in more detail，但没有解释精排的交互特征。
- **pointwise / pairwise / listwise ranking（逐项／成对／列表式排序）**：页面没有说明不同学习排序目标。
- **learning to rank / LTR（学习排序）**：页面使用 score relevance，但没有说明排序器如何通过标注或反馈学习。
- **relevance labels（相关性标签）**：页面没有说明训练或评估时如何标注一个候选是否相关。
- **score calibration（分数校准）**：页面提到 new relevance scores，但没有说明不同模型分数是否可比较。
- **score fusion（分数融合）**：页面没有说明多个检索器或排序器如何合并结果。
- **embedding（嵌入）**：页面提到 semantically similar vectors，但没有解释内容如何变成向量。
- **vector database（向量数据库）**：页面提到 vector search，但没有展开存储和索引向量的数据库。
- **approximate nearest neighbor / ANN（近似最近邻）**：页面没有说明向量搜索如何在大型集合中快速找候选。
- **context window（上下文窗口）**：页面给出 top 3–5 passages sent to the model，但没有解释模型能接收的上下文容量限制。
- **grounding（基于资料生成）**：页面说明 RAG uses retrieved information，但没有介绍检索资料如何约束答案。
- **citation / source attribution（引用／来源归属）**：页面没有讨论如何把重排后的段落与答案中的来源对应起来。
- **latency（延迟）**：页面没有讨论精细重排序增加的响应时间。
- **throughput（吞吐量）**：页面没有讨论每秒查询数或并发能力。
- **computational cost（计算成本）**：页面没有讨论对 20 个或更多候选逐一精排的资源代价。
- **candidate count（候选数量）**：示例给出 20 candidates，但没有讨论候选数和质量、延迟之间的关系。
- **ablation（消融实验）**：页面没有说明如何验证 reranking 相比仅使用初始检索的增益。
- **offline evaluation / online evaluation（离线评估／在线评估）**：页面没有介绍用测试集指标或真实用户行为评估排序。
- **click-through rate / CTR（点击率）**：页面没有用点击行为衡量结果顺序是否更有用。
- **user satisfaction（用户满意度）**：页面没有讨论最终用户是否更快找到所需内容。
- **position bias（位置偏差）**：页面没有说明用户更容易点击排在前面的结果会怎样影响排序反馈。
- **duplicate results（重复结果）**：页面没有讨论重排序是否要去重或保证多样性。
- **diversity（多样性）**：页面强调相关性，但没有讨论结果之间是否应覆盖不同方面。
- **freshness（新鲜度）**：页面没有讨论时效性在相关性排序中的作用。
- **business rules（业务规则）**：页面没有说明重排序后是否还要应用库存、权限、地区或合规规则。
- **filtering vs reranking（过滤与重排序）**：页面说 order candidates，但没有区分改变顺序与删除候选。
- **retrieval failure（检索失败）**：页面没有描述初始检索没有找到相关候选时的处理。
- **reranking failure（重排序失败）**：页面没有描述重排模型出错、超时或返回空结果时的回退路径。

## Aliases / Synonyms

- Reranking ↔ re-ranking ↔ rerank ↔ second-stage ranking
- Reranker ↔ reranking model ↔ second-stage ranker ↔ precision-stage ranker
- Retrieval ↔ initial retrieval ↔ first-stage retrieval ↔ candidate retrieval ↔ information retrieval
- Retriever ↔ first-stage retriever ↔ candidate generator ↔ recall-stage component
- Candidate ↔ possible match ↔ retrieved candidate ↔ candidate result
- Candidate set ↔ candidate list ↔ retrieved result set ↔ pool of candidates
- Result ordering ↔ ranking ↔ rank order ↔ sorted order
- Relevance ↔ query-result match ↔ usefulness for the query ↔ semantic relevance
- Relevance score ↔ relevance signal ↔ ranking score ↔ candidate score
- Top results ↔ highest-ranked results ↔ top-ranked items ↔ first results
- Top-k results ↔ first k results ↔ top k ↔ leading results
- Initial search ↔ first search ↔ fast search ↔ coarse retrieval
- Detailed comparison ↔ careful examination ↔ fine-grained scoring ↔ query-candidate comparison
- Vector Search ↔ semantic vector search ↔ dense retrieval（不完全同义：vector search 是检索方式，dense retrieval 是其中一类实现）
- Keyword search ↔ lexical search ↔ term matching ↔ exact match（不完全同义：exact match 要求更严格）
- Cross-encoder ↔ query-document interaction reranker ↔ pair-scoring reranker
- Bi-encoder ↔ dual encoder ↔ two-tower encoder
- RAG ↔ Retrieval-Augmented Generation ↔ retrieval-enhanced generation
- Passage ↔ text passage ↔ document chunk ↔ retrieved text segment
- Application ↔ downstream application ↔ consuming system
- Recall ↔ coverage of relevant items ↔ recall@k（recall@k 是限定在前 k 个结果的版本）
- Precision ↔ relevance proportion ↔ precision@k（precision@k 是限定在前 k 个结果的版本）
- MRR ↔ Mean Reciprocal Rank ↔ mean reciprocal rank
- MAP ↔ Mean Average Precision ↔ mean average precision
- NDCG ↔ normalized discounted cumulative gain ↔ normalized DCG
- Latency ↔ response time ↔ ranking delay
- Candidate count ↔ number of candidates ↔ retrieval depth

## Do Not Confuse Candidates

- **Reranking vs Retrieval**：Reranking 对已经找到的 candidates 重新排序；retrieval 负责从集合中找到 candidates。
- **Reranking vs Vector Search**：Reranking 是初始检索后的第二阶段步骤；vector search 是通过向量寻找语义相似内容的一种检索方式。
- **Reranking vs RAG**：Reranking 负责排列结果；RAG 使用检索到的信息帮助模型生成答案。
- **Reranker vs Retriever**：reranker 精细比较并排序已有候选；retriever 先快速产生候选。
- **Initial Retrieval vs Reranking**：initial retrieval 追求快速找出可能匹配；reranking 追求把最相关的候选放到前面。
- **Candidate vs Top Result**：candidate 只是可能匹配项；top result 是排序后位于前列的候选。
- **Relevance vs Usefulness**：relevance 关注和查询的匹配程度；usefulness 也可能受到用户场景和下游用途影响。
- **Ranking vs Filtering**：ranking 改变顺序；filtering 通常会删除不满足条件的项，两者不是同一步。
- **Score vs Rank**：score 是用于比较的数值；rank 是根据分数或规则得到的位置。
- **Top-k vs All Retrieved Results**：top-k 只保留前 k 个；retrieval 可以先返回更大的候选集合。
- **Recall vs Precision**：recall 关注相关项找回了多少；precision 关注返回项中有多少相关。
- **MRR vs NDCG**：MRR 重点奖励第一个相关结果的位置；NDCG 可综合多个相关结果及其位置。
- **Semantic Similarity vs Relevance**：语义相似不一定等于对当前任务最相关；重排序可以结合查询意图做更细判断。
- **Vector Search vs Keyword Search**：vector search 比较向量表示；keyword search 主要匹配词语或词元。
- **Dense Retrieval vs Reranking**：dense retrieval 是产生候选的检索范式；reranking 是随后重新安排候选的阶段。
- **Cross-Encoder vs Bi-Encoder**：cross-encoder 通常一起读取查询和候选以精细打分；bi-encoder 通常分别编码，便于快速召回。
- **RAG vs Search**：search 或 retrieval 找信息；RAG 还会把找到的信息交给生成模型组织答案。
- **Passage vs Document**：passage 是文档中的片段；document 是更完整的来源资料。
- **20 Candidates vs Top 3–5 Passages**：20 是示例中重排前的候选数量；3–5 是重排后传给模型的较小集合。
- **Improved Order vs New Information**：重排序改善已有结果的先后，不会凭空检索出初始集合中不存在的新资料。
- **Reranking vs Generation**：reranking 选择和排序已有内容；generation 创建新的文字或其他输出。
- **Reranking vs Recommendation**：reranking 可用于推荐结果排序，但“推荐”还包含判断什么可能对用户有用的产品或内容决策。
- **Relevance Score vs Confidence**：相关性分数表达 query-result 匹配程度；confidence 通常表达系统对自身结果的确信程度，两者不必相同。
- **Reranking vs Business Rules**：重排序模型根据相关性等信号排序；权限、库存、地域或合规限制可能需要独立的业务规则过滤。

## Notes

- 本文件是 Module 08 Topic 10 的 raw glossary 收集稿，目标是最大化保留页面正文和直接上下文中的候选，不做去重、归并或最终取舍。
- 页面正文的核心链路是：`Query → Initial Retrieval → Candidate Results → Reranking → Top Results → RAG / Application`。
- 页面明示的五个流程节点是：`Query`、`Initial retrieval`、`Reranker`、`Improved order`、`Top results`；每个节点的动作分别是 read the request、find candidates、score relevance、put the best first、send a smaller set。
- 页面明确给出的定义是：reranking is a second-stage ranking step applied after an initial retrieval；其结果是把 most useful candidates 放到前面。
- 页面给出的类比是 librarian 先拉出一摞 possibly relevant books，再 sorting the stack，把 best matches 放在 top；librarian、books、stack、best matches on top 因此作为低优先级但可追踪候选保留。
- 页面两个现实例子分别是 shopping search（查询为 `waterproof walking shoes`，把 most useful products first）和 RAG assistant（先 retrieves 20 candidates，再把 top 3–5 passages sent to the model）。
- 页面三组“不是”对照直接涉及 `Retrieval`、`Vector Search`、`RAG`，并明确区分：retrieval finds candidates，vector search finds semantically similar vectors，RAG uses retrieved information to help generate an answer。
- 页面没有显式写出 BM25、cross-encoder、bi-encoder、MRR、MAP、NDCG、precision@k、recall@k 等专业实现或指标；这些词作为领域相关的最大候选保留，并在 Potential Missing Concepts 中标记为页面未展开。
- 页面也没有给出 reranking 的具体模型架构、训练数据、标注方式、评分函数、索引实现、延迟或成本分析；相关词不应在后续阶段被误标成页面已经定义的机制。
- `RAG` 是正文中的缩写；`MRR`、`MAP`、`NDCG`、`ANN`、`LTR`、`CTR` 是候选扩展缩写，属于相关领域补充，不是页面原文明确出现的全部缩写。
- 页面只说明 reranking 改善已检索候选的 order；它没有主张 reranking 会发现初始候选集合之外的新内容，也没有把 reranking 等同于 retrieval、vector search 或 RAG。
- 页面的视频区域标记为 `Video unavailable`、`visual explainer not yet available` 和 `No video is available for this topic yet`；这些是呈现状态词，不是 reranking 核心术语，但为完整原始候选集合保留。
