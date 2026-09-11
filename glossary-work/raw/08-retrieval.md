# Topic

Retrieval

## Topic Metadata

- Requested Module: 08
- Page Module: 05 · Embeddings, RAG & Vector Search
- Page Topic: Topic 05 · Retrieval
- Topic Title: What is Retrieval?
- Source File: `retrieval.html`
- Source Page Description: Retrieval selects relevant information from a larger source collection for a task.
- Collection Mode: Raw, maximum candidate collection; candidates are intentionally not deduplicated, merged, or reduced.

## Glossary Candidates

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Retrieval | 检索；信息检索 | The process of finding and selecting relevant information. | 从很多资料里找出和问题有关的内容。 |
| retrieval | 检索；取回 | Finding and returning useful existing information. | 把有用的已有信息找回来。 |
| retrieve | 检索；取回 | Find and return relevant information or records. | 找到并返回相关资料或记录。 |
| relevant information | 相关信息 | Information that helps answer or complete a task. | 对当前问题或任务有帮助的信息。 |
| information | 信息 | Data or knowledge that can be used by a person, application, or model. | 可以被人、程序或模型使用的内容。 |
| source collection | 来源集合；资料集合 | A larger collection from which information is selected. | 存放候选资料的大集合。 |
| larger source collection | 更大的来源集合 | The full set of possible source information. | 所有可能被查找的资料总库。 |
| collection | 集合；资料库 | A group of information sources or records. | 放在一起的一组资料或记录。 |
| source | 来源；资料来源 | An original place or item from which information comes. | 信息最初来自的文件、记录或资料。 |
| source information | 来源信息 | Information supplied by an original source. | 来自原始资料的内容。 |
| source record | 来源记录 | A stored record that can provide evidence. | 可以被找回并提供证据的一条记录。 |
| source document | 来源文档 | An original document that may be retrieved. | 可能被检索出来的原始文件。 |
| source material | 来源材料 | Material available for retrieval. | 系统可以查找的资料内容。 |
| task | 任务 | The job for which relevant information is selected. | 系统找资料是为了完成的事情。 |
| downstream task | 下游任务 | A later task that uses retrieved information. | 使用检索结果继续完成的后续任务。 |
| query | 查询；查询内容 | A request used to find related information. | 用户提出的、用来找资料的问题或请求。 |
| request | 请求 | The information need submitted to a system. | 用户希望系统处理或回答的要求。 |
| information need | 信息需求 | The information required to complete a task. | 为完成任务真正需要知道的内容。 |
| question | 问题 | A request for information. | 向系统提出、期待得到信息的问题。 |
| current request | 当前请求 | The request being processed now. | 系统此刻正在处理的请求。 |
| relevant to a query | 与查询相关 | Connected or useful for the current query. | 和当前问题有关、能派上用场。 |
| relevance | 相关性 | How useful a result is for a query or task. | 一个结果和问题到底有多相关。 |
| relevant result | 相关结果 | A result that matches the information need. | 符合问题需要的结果。 |
| result | 结果 | An item returned by a search or retrieval operation. | 系统查找后返回的项目。 |
| search result | 搜索结果 | An item returned from search. | 搜索后显示或返回的内容。 |
| search results | 搜索结果 | Results that may be shown directly to a user. | 搜索产生、可能直接展示给用户的一组结果。 |
| candidate | 候选项 | An item considered as a possible match. | 正在考虑是否相关的候选内容。 |
| candidate item | 候选项目 | A possible result considered for return. | 可能被返回的一条候选记录。 |
| candidate set | 候选集合 | The items available for ranking or filtering. | 排序或过滤前的一组候选结果。 |
| find candidates | 找到候选项 | Locate possible matches for a query. | 先找出可能相关的内容。 |
| selection | 选择；筛选 | Choosing useful information from a larger collection. | 从大集合中挑出有用内容。 |
| select information | 选择信息 | Choose information relevant to a query or task. | 根据问题挑出相关资料。 |
| selected information | 已选择的信息 | Information chosen for a downstream step. | 已经被系统挑中、交给下一步的内容。 |
| selected record | 已选记录 | A record chosen to be returned. | 被选中并准备返回的记录。 |
| small selection | 少量选择结果 | A small subset of a much larger collection. | 从大量资料中挑出的少数内容。 |
| subset | 子集；部分集合 | A smaller group selected from a larger group. | 大集合中的一部分。 |
| return | 返回 | Send selected information back from retrieval. | 把选中的资料交回系统或用户。 |
| returned evidence | 返回的证据 | Evidence returned for use by a person, application, or model. | 检索后交给后续使用的依据。 |
| returned record | 返回记录 | A record sent back as a retrieval result. | 作为检索结果返回的一条记录。 |
| return relevant items | 返回相关项目 | Send useful matching items to the next step. | 把相关项目交给下一步。 |
| evidence | 证据；依据 | Information used to support an answer or review. | 用来支持回答或审查的资料依据。 |
| evidence for an answer | 回答依据 | Retrieved information that supports an answer. | 帮助形成回答的资料证据。 |
| evidence for a review | 审查依据 | Retrieved information used in a review. | 审查政策或资料时使用的证据。 |
| evidence source | 证据来源 | A source that supplies supporting information. | 提供回答依据的资料来源。 |
| person | 人员；用户 | A human who can receive or use retrieved evidence. | 可以查看或使用检索资料的人。 |
| application | 应用程序 | A software system that can receive or use evidence. | 可以接收或利用检索结果的软件。 |
| model | 模型 | A model that can use retrieved evidence for a task. | 可以使用检索资料完成任务的模型。 |
| downstream use | 下游使用 | What happens after information is returned. | 检索结果交给后续系统或任务使用。 |
| next step | 下一步 | The stage that receives selected information. | 接收检索结果的后续环节。 |
| before the next step | 下一步之前 | The point at which retrieval happens before later use. | 先检索、再让后续步骤使用。 |
| retrieval system | 检索系统 | A system that finds and selects relevant information. | 专门从资料集合中查找和挑选信息的系统。 |
| system | 系统 | The software or workflow performing retrieval. | 执行查找、排序、过滤和返回的整体。 |
| retrieval workflow | 检索工作流 | The ordered process from query to returned evidence. | 从问题到返回证据的一连串流程。 |
| process | 过程 | A sequence of operations that performs retrieval. | 完成检索所经历的一组步骤。 |
| process step | 流程步骤 | One stage in a retrieval process. | 检索流程中的一个环节。 |
| workflow stage | 工作流阶段 | A named stage in the retrieval workflow. | 工作流中可以单独说明的阶段。 |
| Query | 查询 | Step 1: read and interpret the request. | 第一步：读懂用户请求。 |
| query step | 查询步骤 | The first stage of the retrieval flow. | 检索流程的第一步。 |
| read the request | 读取请求 | Inspect the request before searching. | 搜索前先读懂用户提出的要求。 |
| identify the information needed | 识别所需信息 | Determine what information the task requires. | 判断这个任务到底需要哪些资料。 |
| information needed | 所需信息 | The content required by the request. | 为回答问题必须找到的内容。 |
| Search | 搜索 | Step 2: look for possible matching items. | 第二步：找候选内容。 |
| search step | 搜索步骤 | The stage that finds candidates. | 检索流程中负责查找候选项的步骤。 |
| find candidates | 查找候选项 | Search the source collection for possible matches. | 在资料库里找可能相关的项目。 |
| text search | 文本搜索 | Search using text terms or text representations. | 根据文字内容查找资料。 |
| vector search | 向量搜索 | Search using vector representations and similarity. | 根据向量之间的接近程度查找资料。 |
| metadata search | 元数据搜索 | Search using descriptive fields about items. | 根据资料的时间、来源、类别等字段查找。 |
| hybrid search | 混合搜索 | Search using more than one method together. | 把文字、向量或元数据等多种查找方式结合起来。 |
| search method | 搜索方法 | A method used to find candidates. | 用来找候选结果的一种方式。 |
| search by keywords | 按关键词搜索 | Find items through keyword matching. | 按问题里出现的词去找资料。 |
| search by vectors | 按向量搜索 | Find items through vector similarity. | 按数字向量的相似程度去找资料。 |
| search by metadata | 按元数据搜索 | Find items through metadata constraints or fields. | 按资料附带的描述字段查找。 |
| Rank | 排名；排序 | Step 3: order candidates by usefulness. | 第三步：按有用程度排序。 |
| rank | 排序；排名 | Order candidates so the most useful appear first. | 把最有用的候选放在前面。 |
| ranking | 排序 | The operation of ordering candidate results. | 给候选结果排先后顺序。 |
| ranking step | 排序步骤 | The stage that orders search candidates. | 检索流程中负责排列候选项的步骤。 |
| order results | 排列结果 | Put results into an ordered list. | 把结果按顺序排列。 |
| most useful candidates | 最有用的候选项 | Candidates judged most useful for the task. | 对当前任务最可能有帮助的候选内容。 |
| useful candidate | 有用候选项 | A candidate likely to help the task. | 可能帮助解决问题的候选项。 |
| first | 首位；前面 | The earlier position given to a higher-ranked result. | 排序后更优的结果放在前面。 |
| ranked result | 排序后的结果 | A result placed in an order by a ranking method. | 已经按相关性或有用程度排好位置的结果。 |
| score | 分数 | A value used to order or compare candidates. | 用来比较候选结果的数值。 |
| relevance score | 相关性分数 | A score estimating how relevant a result is. | 表示结果和问题有多相关的分数。 |
| usefulness | 有用程度 | How much an item helps the task. | 一条资料对完成任务有多大帮助。 |
| Filter | 过滤；筛选 | Step 4: apply constraints to candidates. | 第四步：按规则筛掉不合适的内容。 |
| filter | 过滤 | Remove or exclude items that fail constraints. | 按条件排除不符合要求的结果。 |
| filtering | 过滤操作 | Applying constraints to a candidate set. | 对候选集合应用限制条件。 |
| filter step | 过滤步骤 | The stage that applies access, freshness, or source rules. | 检索流程中负责应用规则的步骤。 |
| apply constraints | 应用约束 | Enforce rules that results must satisfy. | 让结果遵守必须满足的条件。 |
| constraint | 约束；限制条件 | A rule that limits which results may be returned. | 限制哪些结果可以被返回的规则。 |
| access | 访问权限 | Permission to view or use information. | 某人或系统是否有权查看资料。 |
| access rule | 访问规则 | A rule controlling who can receive a source. | 控制谁可以拿到资料的规则。 |
| permission | 权限 | Authorization to access or use information. | 被允许查看或使用某些资料的资格。 |
| user permissions | 用户权限 | The permissions associated with a user. | 某个用户被授予的资料访问范围。 |
| freshness | 新鲜度；时效性 | How current or up to date information is. | 资料是不是最新、是否仍然有效。 |
| freshness rule | 时效规则 | A rule requiring current or recently updated sources. | 要求优先使用最新资料的规则。 |
| current document | 当前文档；最新文档 | A document considered up to date. | 目前有效或较新的文件。 |
| source rule | 来源规则 | A rule restricting acceptable source material. | 规定哪些来源可以使用的规则。 |
| source rules | 来源规则 | Rules about which sources are allowed. | 对资料来源进行限制的一组规则。 |
| access, freshness, and source rules | 权限、时效与来源规则 | Three kinds of constraints in the example flow. | 检索时要同时考虑谁能看、是否最新、来源是否合规。 |
| respect constraints | 遵守约束 | Return only items that satisfy required rules. | 只返回符合限制条件的结果。 |
| allowed document | 允许访问的文档 | A document the user is permitted to receive. | 用户有权查看的文件。 |
| allowed source | 允许的来源 | A source permitted by access or source rules. | 符合权限和来源要求的资料。 |
| Return | 返回 | Step 5: send selected records as evidence. | 第五步：发送选中的证据。 |
| return step | 返回步骤 | The final stage that passes selected records onward. | 将选定记录交给下一步的阶段。 |
| send evidence | 发送证据 | Pass retrieved evidence to a person, application, or model. | 把找到的依据交给人、程序或模型。 |
| pass selected records | 传递选定记录 | Send the chosen records to the next stage. | 把挑出的记录传给后续环节。 |
| selected records | 已选记录 | Records that survived search, ranking, and filtering. | 经过查找、排序和过滤后留下的记录。 |
| record | 记录 | A unit of stored information that can be returned. | 数据库或资料集合中的一条信息。 |
| source records | 来源记录 | Records belonging to the source collection. | 资料库中来自原始来源的记录。 |
| evidence packet | 证据包 | A group of returned evidence for later use. | 交给后续任务的一组证据资料。 |
| pass to the next step | 传给下一步 | Forward selected results in a workflow. | 将检索结果交给后续处理。 |
| text | 文本；文字 | Written content used for search or retrieval. | 可以按文字查找的内容。 |
| keyword | 关键词 | A word or phrase used for literal matching. | 用来按字面查找资料的词或短语。 |
| keywords | 关键词 | Words or phrases used by keyword search. | 一组用于字面搜索的词。 |
| vector | 向量 | A numerical representation used for vector search. | 表示内容的一串数字。 |
| vectors | 向量 | Numerical representations used for comparison or search. | 多个内容对应的数字表示。 |
| metadata | 元数据 | Descriptive information attached to an item. | 描述资料来源、类别、时间等的附加信息。 |
| metadata field | 元数据字段 | A named descriptive field used for filtering or search. | 记录时间、来源、类别等信息的字段。 |
| metadata filter | 元数据过滤器 | A filter based on descriptive fields. | 按附加描述信息筛选结果的规则或工具。 |
| combination of methods | 方法组合 | Using multiple retrieval methods together. | 同时使用多种检索方法。 |
| keyword search | 关键词搜索 | Search based mainly on literal terms. | 主要按词面是否出现来查找。 |
| literal matching | 字面匹配 | Matching words or phrases as written. | 看原文中的词是否直接匹配。 |
| semantic search | 语义搜索 | Search based on meaning or semantic similarity. | 按意思相近而不只是词相同来查找。 |
| lexical search | 词法搜索 | Search based on words and lexical overlap. | 按词语本身和词面重合来搜索。 |
| hybrid retrieval | 混合检索 | Retrieval combining different search signals. | 将关键词、向量或元数据等信号一起用于检索。 |
| information retrieval | 信息检索 | The broader field of finding relevant information. | 研究如何从资料集合中找出相关信息的领域。 |
| IR | 信息检索缩写 | A common abbreviation for information retrieval. | information retrieval 的常见缩写。 |
| relevant source | 相关来源 | A source that contains useful information for the query. | 含有当前问题所需内容的资料来源。 |
| support article | 支持文章；帮助中心文章 | An article retrieved to answer a support question. | 帮助回答用户问题的帮助文档。 |
| help center | 帮助中心 | A collection of support articles. | 存放产品帮助文章的资料库或页面。 |
| account question | 账户问题 | A question about an account in the everyday example. | 用户关于账户的一个问题。 |
| question about an account | 账户相关问题 | The input to the help-center retrieval example. | 帮助中心场景中输入的账户问题。 |
| input | 输入 | The question or request given to the system. | 送进系统开始处理的内容。 |
| system retrieves support articles | 系统检索支持文章 | The system finds relevant help articles for a question. | 系统根据问题找出相关帮助文章。 |
| support articles | 支持文章；帮助文章 | Articles that explain how to solve user issues. | 帮助用户解决问题的文章。 |
| short list | 简短列表 | A small returned list of useful sources. | 系统返回的少量有用来源。 |
| useful sources | 有用来源 | Sources likely to help with the input question. | 对解决问题有帮助的资料来源。 |
| policy question | 政策问题 | A question about a policy in the business example. | 用户关于政策规定的问题。 |
| user permissions | 用户权限 | Access information used when retrieving policy documents. | 检索政策资料时用来判断能否查看的权限。 |
| business example | 业务示例 | The policy-review retrieval scenario. | 用业务场景说明检索如何工作的例子。 |
| policy review | 政策审查 | A review that uses retrieved policy evidence. | 查找政策资料并据此进行检查。 |
| review | 审查；复核 | An activity supported by retrieved evidence. | 根据资料检查或复核某件事情。 |
| current documents | 当前文档；最新文件 | Documents that are up to date for the policy question. | 目前有效、适合用于政策问题的文件。 |
| allowed, current documents | 有权限且最新的文档 | Documents that satisfy permission and freshness needs. | 用户能看并且仍然有效的文件。 |
| retrieves allowed, current documents | 检索有权限的当前文档 | The system retrieves documents that pass access and freshness requirements. | 系统只找用户有权查看且内容最新的文件。 |
| answer or review | 回答或审查 | A downstream use of the retrieved evidence. | 找到的证据可以用来回答问题或进行复核。 |
| output | 输出 | The information produced by the retrieval system. | 系统处理后交付出来的结果。 |
| short list of useful sources | 有用来源的短列表 | The output of the help-center example. | 帮助中心场景中返回的一小组资料来源。 |
| evidence for an answer or review | 回答或审查的证据 | The output of the policy-review example. | 用于回答或审查的资料依据。 |
| search results only | 仅搜索结果 | Results shown directly without a downstream task. | 只把搜索结果显示出来，不再交给后续任务处理。 |
| Search Results Only | 仅搜索结果 | A misconception contrasted with retrieval. | 页面用来和 Retrieval 对比的概念。 |
| downstream processing | 下游处理 | Further processing after results are found. | 找到资料后由后续系统继续处理。 |
| further processing | 后续处理 | Processing performed after a search result is returned. | 结果返回后继续进行的处理。 |
| direct display | 直接展示 | Showing search results directly to a user. | 不经额外步骤就把结果展示给用户。 |
| generation | 生成 | Creating new model output. | 模型根据输入生成新的文字或其他输出。 |
| Generation | 生成 | The production of new model output, contrasted with retrieval. | 页面用来和 Retrieval 对比的“产生新内容”。 |
| create new model output | 创建新的模型输出 | Produce new content with a model. | 让模型生成以前没有直接返回的新内容。 |
| existing information | 已有信息 | Information already present in a source collection. | 资料库中原本就存在的内容。 |
| new output | 新输出 | Output newly created by a model. | 模型这次新产生的内容。 |
| retrieval versus generation | 检索与生成 | Finding existing information versus creating new output. | 检索是找已有资料，生成是产生新内容。 |
| RAG | 检索增强生成 | A workflow combining retrieval with model generation. | 先找资料，再让模型利用资料生成回答的方法。 |
| Retrieval-Augmented Generation | 检索增强生成 | The expanded form of RAG. | RAG 的英文全称。 |
| retrieval-augmented generation | 检索增强生成 | Generation supported by retrieved information. | 用检索到的资料帮助模型生成内容。 |
| combines retrieval with model generation | 将检索与模型生成结合 | Use retrieved information as part of a generation workflow. | 把找回来的资料交给生成模型使用。 |
| model generation | 模型生成 | New output produced by a model. | 模型根据输入生成的新内容。 |
| retrieval step | 检索步骤 | The information-selection part of a larger workflow. | 在完整工作流里负责找资料的部分。 |
| selection step | 选择步骤 | The step that chooses relevant information. | 从候选内容中挑出相关信息的环节。 |
| RAG workflow | RAG 工作流 | A workflow in which retrieval supports generation. | 由检索和生成共同组成的工作流程。 |
| retrieved evidence | 检索到的证据 | Evidence selected from existing sources. | 从已有资料中找回并挑选出的依据。 |
| retrieved context | 检索上下文 | Retrieved material supplied to a downstream model or task. | 检索出的、交给后续模型参考的上下文资料。 |
| context | 上下文 | Information supplied to help a later task. | 帮助后续处理理解问题的背景内容。 |
| related concepts | 相关概念 | Concepts connected to retrieval. | 和检索有关、可以继续学习的概念。 |
| concept tree | 概念流程树 | A compact sequence of related retrieval concepts. | 把检索相关步骤和结果串起来的概念链。 |
| Query → Search → Rank → Filter → Retrieved evidence | 查询 → 搜索 → 排序 → 过滤 → 检索证据 | The page's retrieval process sequence. | 页面展示的从问题到证据的五步路线。 |
| retrieved evidence | 检索证据 | Evidence produced after query, search, ranking, and filtering. | 完成检索流程后留下的资料依据。 |
| Vector Search | 向量搜索 | Search using vector representations. | 页面列出的相关概念：用向量相似性查找内容。 |
| Retrieval | 检索 | The broader task of finding relevant information. | 页面列出的相关概念：从资料中找相关信息。 |
| RAG | 检索增强生成 | Retrieval combined with generation. | 页面列出的相关概念：检索加模型生成。 |
| Embeddings | 嵌入；向量表示 | Numerical representations used to compare meaning or features. | 页面列出的相关概念：把内容变成可比较的数字表示。 |
| embedding | 嵌入表示 | A numerical representation that can support retrieval. | 可用于查找相似资料的数字表示。 |
| embedding model | 嵌入模型 | A model that converts content into vectors. | 把内容变成向量、帮助比较相似性的模型。 |
| query embedding | 查询嵌入 | An embedding representing the query. | 把用户问题转成的数字表示。 |
| document embedding | 文档嵌入 | An embedding representing a document or passage. | 把文档或片段转成的数字表示。 |
| semantic similarity | 语义相似度 | Similarity based on meaning. | 两段内容意思有多接近。 |
| similarity | 相似度 | A measure of how close two items or representations are. | 用数字表示两个内容有多像。 |
| similarity score | 相似度分数 | A numerical value used to compare candidates. | 用来判断候选资料相似程度的数值。 |
| distance | 距离 | A measure of how far representations are apart. | 用数字表示两个向量相差多远。 |
| nearest neighbor | 最近邻 | An item whose representation is closest to a query. | 在向量空间里离问题最近的资料。 |
| top-k | 前 k 个 | The first k ranked results returned for a query. | 排名最前面的 k 条结果。 |
| top-k retrieval | Top-k 检索 | Returning the highest-ranked k candidates. | 只返回排序最靠前的 k 个候选。 |
| reranking | 重排序 | Reordering an initial set of retrieved candidates. | 对初步找回的结果再排一次顺序。 |
| filter after ranking | 排序后过滤 | Apply constraints after candidates have been ranked. | 排好顺序后，再检查权限和其他条件。 |
| access control | 访问控制 | Rules that determine who may receive information. | 控制谁有资格查看哪些资料。 |
| authorization | 授权 | Permission granted to a user or system. | 系统正式允许某人访问资料。 |
| freshness check | 时效检查 | Check whether a source is current enough. | 检查资料是否足够新、仍然有效。 |
| provenance | 来源溯源 | Information about where retrieved evidence came from. | 说明证据来自哪份原始资料。 |
| citation | 引用；出处 | A pointer back to a source supporting an answer. | 让人能回到原始资料的出处信息。 |
| source attribution | 来源归属 | Identifying the source of returned information. | 明确说明检索内容来自哪里。 |
| document | 文档 | A source item that can be searched or returned. | 一份可以被查找和返回的文件。 |
| passage | 文本片段 | A smaller section of a source document. | 文档中的一小段文字。 |
| chunk | 文档块；片段 | A chunked portion of a larger document. | 为了检索而从文档切出的较小片段。 |
| chunking | 文档切分 | Splitting documents into retrievable pieces. | 把长文档切成方便查找的小块。 |
| corpus | 语料库；资料语料集合 | A body of documents available for retrieval. | 可以被检索的一大批文档。 |
| index | 索引 | A structure that makes searching a collection efficient. | 帮助系统更快找到资料的目录结构。 |
| retrieval index | 检索索引 | An index built for finding candidate records. | 专门帮助检索候选资料的索引。 |
| inverted index | 倒排索引 | A keyword-search index mapping terms to documents. | 根据词找到包含这些词的文档的目录。 |
| vector index | 向量索引 | An index supporting efficient vector similarity search. | 帮助快速寻找相似向量的索引。 |
| vector database | 向量数据库 | A database designed to store and search vectors. | 能保存并按向量相似度查找内容的数据库。 |
| database | 数据库 | A system that stores records and metadata. | 保存资料记录及其附加信息的系统。 |
| search engine | 搜索引擎 | A system that finds and ranks results. | 负责查找并排序结果的系统。 |
| retriever | 检索器 | A component that retrieves candidate information. | 工作流中负责找回候选资料的组件。 |
| retrieval pipeline | 检索管线 | A sequence of retrieval operations. | 把查询、搜索、排序、过滤串起来的处理管线。 |
| retrieval pipeline stage | 检索管线阶段 | One stage in a retrieval pipeline. | 检索管线中的一个处理阶段。 |
| query understanding | 查询理解 | Interpreting what information the request needs. | 判断用户问题真正想找什么。 |
| query parsing | 查询解析 | Breaking a request into searchable components. | 把请求拆成系统可以搜索的部分。 |
| query expansion | 查询扩展 | Adding related terms or representations to a query. | 给查询补充相关词或表达，扩大查找范围。 |
| candidate generation | 候选生成 | Producing an initial candidate set for ranking. | 先产生一批候选结果，再进行排序。 |
| recall stage | 召回阶段 | An early stage intended to find many relevant candidates. | 尽量找全相关内容的前期阶段。 |
| ranking stage | 排序阶段 | A stage that orders candidate results. | 对候选结果按优先级排列的阶段。 |
| post-filtering | 后过滤 | Filtering candidates after search or ranking. | 搜索或排序之后再应用限制条件。 |
| result set | 结果集 | The set of results returned or considered. | 系统返回或正在处理的一组结果。 |
| retrieval quality | 检索质量 | How well a system finds useful relevant information. | 系统找资料找得准不准、全不全。 |
| retrieval effectiveness | 检索效果 | How effectively retrieval supports the task. | 检索对完成任务的实际帮助程度。 |
| answer quality | 回答质量 | How good an answer is after using evidence. | 使用检索资料后形成的回答质量。 |
| precision | 精确率 | The fraction of returned items that are relevant. | 返回的内容中有多少是真相关的。 |
| recall | 召回率 | The fraction of all relevant items that were found. | 所有相关内容中有多少被找回来了。 |
| precision@k | 前 k 精确率 | Precision measured among the first k results. | 前 k 条结果里相关内容的比例。 |
| recall@k | 前 k 召回率 | Recall measured using the first k results. | 只看前 k 条时找回相关内容的比例。 |
| mean reciprocal rank | 平均倒数排名 | The average reciprocal rank of the first relevant result. | 相关结果平均排得有多靠前的指标。 |
| MRR | 平均倒数排名缩写 | Abbreviation for mean reciprocal rank. | mean reciprocal rank 的缩写。 |
| NDCG | 归一化折损累计增益 | A ranking-quality metric that rewards useful order. | 衡量排序是否把更相关结果放前面的指标。 |
| normalized discounted cumulative gain | 归一化折损累计增益 | A metric for graded ranking quality. | 用结果相关程度和排名位置评估排序的指标。 |
| hit rate | 命中率 | The proportion of queries with a useful retrieved result. | 有找到至少一个有用结果的问题比例。 |
| relevance judgment | 相关性判断 | A judgment about whether a result is relevant. | 判断一条结果是否真的和问题有关。 |
| ground truth | 真实标注；基准答案 | The trusted relevance labels used for evaluation. | 用来检查检索对不对的标准答案或人工标注。 |
| benchmark | 基准测试 | A fixed evaluation setup for comparing retrieval systems. | 用统一题目比较不同检索系统的方法。 |
| evaluation set | 评估集 | Queries and labels used to measure retrieval quality. | 用来测试检索效果的一组问题和标准结果。 |
| offline evaluation | 离线评估 | Evaluate retrieval on a prepared dataset. | 不在线服务用户时，用准备好的数据测试系统。 |
| online evaluation | 在线评估 | Evaluate retrieval during real usage. | 在真实使用过程中观察检索效果。 |
| latency | 延迟 | The time a retrieval request takes to return. | 从发出查询到拿到结果要等多久。 |
| throughput | 吞吐量 | The number of retrieval requests handled per unit time. | 一段时间内系统能处理多少次检索。 |
| scalability | 可扩展性 | The ability to keep working as data or traffic grows. | 资料和用户增加时系统还能否稳定工作。 |
| freshness versus relevance | 时效性与相关性 | The tradeoff between current sources and query match. | 最新资料不一定最相关，检索常要平衡两者。 |
| access-aware retrieval | 感知权限的检索 | Retrieval that applies user access rules. | 检索时会根据用户权限隐藏不能看的内容。 |
| permission-aware retrieval | 权限感知检索 | Retrieval constrained by permissions. | 只从用户有权访问的资料中查找。 |
| source-aware retrieval | 来源感知检索 | Retrieval that respects allowed source rules. | 检索时会遵守指定的资料来源范围。 |
| freshness-aware retrieval | 时效感知检索 | Retrieval that considers how current sources are. | 检索时会考虑资料的新旧和有效期。 |
| secure retrieval | 安全检索 | Retrieval that avoids exposing unauthorized sources. | 确保不会把无权查看的资料返回出去。 |
| grounded answer | 有依据的回答 | An answer supported by retrieved source evidence. | 有检索资料作为依据的回答。 |
| grounding | 基于依据；接地 | Connecting model output to retrieved evidence. | 让模型回答建立在找到的资料上。 |
| hallucination | 幻觉；虚构 | An unsupported or invented model output. | 模型没有依据却编出来的内容。 |
| hallucination reduction | 减少幻觉 | Using evidence to reduce unsupported output. | 用检索资料帮助减少模型乱编。 |
| source coverage | 来源覆盖度 | How much of the needed source collection is available. | 资料库覆盖用户可能需要的信息有多完整。 |
| corpus coverage | 语料覆盖度 | How much relevant material the corpus contains. | 资料集合里包含相关内容的程度。 |
| data freshness | 数据新鲜度 | How recently the source data was updated. | 资料距离最近更新有多久。 |
| stale document | 过时文档 | A document that is no longer current. | 已经过期或不再适用的文件。 |
| duplicate result | 重复结果 | A result that repeats another returned item. | 和另一个结果实际上重复的内容。 |
| deduplication | 去重 | Removing duplicate records or results. | 把重复资料删掉或合并。 |
| noisy result | 噪声结果 | A returned item that is not useful for the task. | 被返回但对问题没什么帮助的内容。 |
| false positive | 假阳性；误相关 | A result marked relevant by the system but not truly relevant. | 系统以为相关、实际不相关的结果。 |
| false negative | 假阴性；漏检 | A relevant result that the system fails to return. | 实际相关、但系统没有找回的结果。 |
| retrieval failure | 检索失败 | Failure to return useful relevant evidence. | 系统没有找到足够有用的资料。 |
| missed evidence | 漏掉的证据 | Relevant evidence that was not retrieved. | 本来应该找回、但被漏掉的依据。 |
| irrelevant evidence | 不相关证据 | Returned material that does not help the task. | 找回来但和问题无关的资料。 |
| search failure | 搜索失败 | Failure to find suitable candidate information. | 搜索没有找到合适候选结果。 |
| ranking failure | 排序失败 | Failure to put useful candidates near the top. | 有用结果存在，却没有排在前面。 |
| filtering failure | 过滤失败 | Failure to apply access, freshness, or source constraints correctly. | 权限、时效或来源规则没有正确执行。 |
| access leakage | 权限泄露 | Returning information a user is not allowed to see. | 把用户无权查看的资料错误地返回出来。 |
| stale evidence | 过时证据 | Evidence that is no longer current. | 已不适合支持当前回答的旧资料。 |
| source mismatch | 来源不匹配 | Evidence coming from a source that does not meet requirements. | 资料来自不符合要求的来源。 |
| query drift | 查询漂移 | Retrieval moving away from the actual information need. | 搜索越找越偏离用户真正的问题。 |
| ambiguity | 歧义；含义不明确 | A query or source can be interpreted in multiple ways. | 同一句话可能有不止一种理解。 |
| disambiguation | 消歧 | Resolve multiple possible query meanings. | 判断用户到底指的是哪一种意思。 |
| multilingual retrieval | 多语言检索 | Retrieval across more than one language. | 用不同语言查找和返回相关资料。 |
| multimodal retrieval | 多模态检索 | Retrieval across text, images, or other modalities. | 不只查文字，也能查图片等不同类型的内容。 |
| cross-modal retrieval | 跨模态检索 | Retrieve one modality using a query from another modality. | 例如用文字问题找相关图片。 |
| metadata | 元数据 | Descriptive fields that can guide retrieval. | 帮助搜索和过滤的资料说明信息。 |
| filter expression | 过滤表达式 | A structured condition used to restrict results. | 用程序写出的筛选条件。 |
| query-time filter | 查询时过滤器 | A filter applied when a query is executed. | 用户发起查询时才应用的条件。 |
| pre-filtering | 预过滤 | Apply constraints before similarity search or ranking. | 搜索或排序前先筛掉不符合条件的资料。 |
| post-filtering | 后过滤 | Apply constraints after candidate retrieval. | 找到候选后再筛选。 |
| access boundary | 权限边界 | The boundary of information a requester may use. | 用户可以看到的资料范围边界。 |
| audit trail | 审计轨迹 | A record of what was retrieved and why. | 记录查了什么、返回了什么以及原因。 |
| observability | 可观测性 | The ability to inspect retrieval behavior and quality. | 能看清检索系统如何工作、哪里出问题。 |
| retrieval trace | 检索追踪记录 | A trace of query, candidates, ranking, filters, and output. | 记录一次检索全过程的调试信息。 |
| explainable retrieval | 可解释检索 | Retrieval whose selection or ranking can be explained. | 能说明为什么返回这些资料的检索。 |
| query-document pair | 查询-文档对 | A query together with a candidate document. | 一个问题和一份候选文档组成的一对。 |
| query-document relevance | 查询-文档相关性 | How relevant a document is to a query. | 一份文档对某个问题有多相关。 |
| document collection | 文档集合 | A collection of searchable documents. | 可以被系统查找的一批文档。 |
| source collection | 来源集合 | The collection searched for task-relevant information. | 检索系统查找信息的大资料集合。 |
| information source | 信息来源 | A document, record, or system supplying information. | 提供内容的一份文档、记录或系统。 |
| existing source | 已有来源 | A source that already contains information before retrieval. | 检索前就已经存在的资料来源。 |
| downstream model | 下游模型 | A model that uses retrieved evidence. | 接收检索资料并继续处理的模型。 |
| downstream application | 下游应用 | An application that uses returned evidence. | 接收检索结果并完成业务工作的应用。 |
| human reviewer | 人工审核者 | A person who reviews retrieved evidence or results. | 检查检索资料是否合适的人。 |
| policy compliance | 政策合规 | Following policy and permission requirements. | 返回的资料符合政策和权限要求。 |
| business rule | 业务规则 | A domain-specific constraint on acceptable results. | 业务场景规定必须满足的条件。 |
| task-specific relevance | 任务相关性 | Relevance judged for a particular task. | 不是绝对相关，而是对当前任务是否有用。 |
| use case | 使用场景 | A situation in which retrieval is applied. | 检索技术被使用的一种实际场景。 |
| real-world example | 现实示例 | An example showing retrieval in practice. | 用现实工作说明检索用途的例子。 |
| everyday example | 日常示例 | The help-center example on the page. | 页面中帮助中心这一贴近日常的例子。 |
| policy-review example | 政策审查示例 | The business example involving permissions and current documents. | 页面中按权限找最新政策文件的例子。 |
| library analogy | 图书馆类比 | Comparing retrieval with finding pages in a library. | 用图书馆找书页来帮助理解检索。 |
| library | 图书馆 | The analogy's collection of many pages. | 页面用来比喻资料集合的地方。 |
| page | 页面；页 | A unit of information in the library analogy. | 类比中可以被挑出来的一页资料。 |
| right pages | 正确页面；相关页 | The small set of pages useful for a question. | 和问题最相关、应该找出的页面。 |
| finding the right pages | 找到正确页面 | The page's analogy for retrieval. | 页面用“找到合适页面”比喻检索。 |
| many pages | 大量页面 | The larger collection available in the analogy. | 图书馆里大量可供查找的页面。 |
| question needs only a small selection | 问题只需要少量选择结果 | A question usually needs only a subset of the full collection. | 回答一个问题通常不用看完整资料库。 |
| choose that selection | 选择那部分内容 | Retrieval selects the pages or items needed next. | 检索把下一步需要的内容挑出来。 |
| useful existing information | 有用的已有信息 | Existing information selected before another system uses it. | 先从已有资料中找出有用内容。 |
| another system or model | 另一个系统或模型 | A later consumer of retrieved information. | 接着使用检索结果的软件或模型。 |
| use retrieved information | 使用检索信息 | Apply returned evidence to a later task. | 把找回的资料拿去完成后续任务。 |
| selection before use | 使用前筛选 | Retrieval selects information before it is used. | 先挑资料，再让后续系统使用。 |
| existing information versus new output | 已有信息与新输出 | The boundary between retrieval and generation. | 找已有内容和生成新内容的区别。 |

## Potential Missing Concepts

The following are plausible glossary candidates triggered by the topic and common retrieval implementations, but they are not explicitly defined in the page body. They should remain candidates rather than being treated as page-established facts.

- **cosine similarity** — 常见的向量相似度计算方法；页面只说 vectors、similarity 和 vector search，没有给出具体公式。
- **dot product / inner product** — 常见的向量评分方式；页面没有指定相似度函数。
- **Euclidean distance / L2 distance** — 常见的向量距离；页面没有说明距离度量。
- **Manhattan distance** — 另一种可能的向量距离；页面未提及。
- **vector dimension / dimensionality** — 向量的维度数量；页面只说 vectors，没有解释维度。
- **dense vector** — 多数维度都有数值的向量；页面未区分 dense 与 sparse。
- **sparse vector** — 大量维度为零的向量；页面未具体展开。
- **approximate nearest neighbor / ANN** — 大规模向量检索常用的近似最近邻方法；页面未介绍。
- **HNSW** — 一种常见的 ANN 索引结构；页面没有给出具体索引实现。
- **IVF** — 一类向量索引方法；页面没有涉及索引算法。
- **product quantization / PQ** — 可用于压缩向量索引的技术；页面未提及。
- **BM25** — 关键词检索常见排序算法；页面只说 keywords / text methods，没有给出算法名。
- **TF-IDF** — 传统文本检索权重方法；页面未提及。
- **Boolean retrieval** — 基于 AND、OR、NOT 的检索；页面未介绍。
- **full-text search** — 全文检索；页面只使用 text / keywords 的概念。
- **sparse retrieval** — 稀疏检索；页面没有使用该术语。
- **dense retrieval** — 基于稠密向量的检索；页面只概括 vectors，没有明确展开。
- **dual encoder / bi-encoder** — 分别编码查询和候选的架构；页面未讨论模型架构。
- **cross-encoder** — 将查询和候选一起评分的架构；页面未讨论。
- **late interaction** — 查询与文档的延迟交互方式；页面未提及。
- **reranker** — 负责重排序的组件；页面有 Rank，但没有具体组件定义。
- **query encoder** — 将查询编码成向量的组件；页面未说明编码流程。
- **document encoder** — 将文档编码成向量的组件；页面未说明。
- **embedding model** — 页面 Related concepts 有 Embeddings，但没有展开 embedding model 的实现。
- **vector database** — 页面 Related concepts 有 Vector Search，但没有具体介绍向量数据库。
- **indexing** — 建立搜索索引的过程；页面没有写出建索引流程。
- **ingestion** — 将来源资料导入检索系统的过程；页面未提及。
- **data pipeline** — 从数据准备到检索的管线；页面只给出查询时的五步流程。
- **document parsing** — 解析文件内容的步骤；页面未提及。
- **OCR** — 从图片或扫描件提取文字；页面没有视觉或 OCR 流程。
- **chunking** — 将长文档分成检索片段；页面没有讲文档分块。
- **chunk overlap** — 相邻片段之间的重叠；页面未提及。
- **parent-child retrieval** — 同时检索片段和父文档的方式；页面未提及。
- **multi-hop retrieval** — 需要多次查找才能完成的问题；页面未提及。
- **iterative retrieval** — 根据中间结果反复查询；页面未提及。
- **query rewriting** — 改写查询以改善检索；页面未提及。
- **query expansion** — 扩展查询词或表示；页面未提及。
- **HyDE** — 用假设性文档辅助检索的查询方法；页面未提及。
- **metadata filtering** — 用元数据字段限制结果；页面提到 metadata / filters，但没有展开实现。
- **pre-filtering** — 搜索前应用过滤条件；页面只说 Filter，不指定时机。
- **post-filtering** — 搜索后应用过滤条件；页面只说 Filter，不指定时机。
- **ACL / access-control list** — 访问控制列表；页面提到 access / user permissions，但未给出缩写。
- **RBAC / role-based access control** — 基于角色的权限控制；页面未提及。
- **ABAC / attribute-based access control** — 基于属性的权限控制；页面未提及。
- **document-level security** — 文档级安全限制；页面提到 access rules，但未定义实现。
- **tenant isolation** — 多租户数据隔离；页面未提及。
- **freshness window** — 允许资料的时间窗口；页面提到 freshness，但未定义窗口。
- **time-to-live / TTL** — 资料或索引的有效期；页面未提及。
- **provenance** — 资料来源追踪；页面用 source rules / sources，但没有展开溯源机制。
- **citation grounding** — 将回答与检索来源绑定；页面提到 evidence，但未定义引用机制。
- **context window** — 下游模型能接收的上下文容量；页面未提及。
- **context compression** — 压缩检索上下文；页面未提及。
- **contextual relevance** — 结合任务上下文判断相关性；页面只说 relevant to a query。
- **answerability** — 判断检索资料是否足以回答问题；页面未提及。
- **faithfulness** — 回答是否忠实于检索证据；页面未提及。
- **attribution accuracy** — 引用是否准确指向支持内容；页面未提及。
- **precision** — 经典检索指标；页面没有列出指标。
- **recall** — 经典检索指标；页面没有列出指标。
- **F1 score** — precision 与 recall 的调和平均；页面未提及。
- **precision@k** — 前 k 结果的精确率；页面未提及。
- **recall@k** — 前 k 结果的召回率；页面未提及。
- **MRR / mean reciprocal rank** — 关注第一个相关结果排名的指标；页面未提及。
- **NDCG / normalized discounted cumulative gain** — 评估排序质量的指标；页面未提及。
- **hit rate** — 至少命中一个相关结果的比例；页面未提及。
- **coverage** — 检索系统能覆盖多少查询或资料；页面未提及。
- **recall-precision tradeoff** — 找全与找准之间的权衡；页面未讨论。
- **latency** — 检索响应时间；页面未提及。
- **throughput** — 单位时间可处理的查询数；页面未提及。
- **tail latency / p95 / p99** — 长尾响应时间指标；页面未提及。
- **caching** — 缓存重复查询或结果；页面未提及。
- **freshness-relevance tradeoff** — 最新程度和问题相关性的权衡；页面只给出 freshness rule，没有讨论 tradeoff。
- **search personalization** — 根据用户偏好调整结果；页面未提及。
- **learning to rank / LTR** — 从标注数据学习排序；页面未提及。
- **click-through rate / CTR** — 用点击行为衡量搜索效果；页面未提及。
- **human relevance labeling** — 由人工标注结果相关性；页面未提及。
- **offline relevance benchmark** — 预先构建的检索评估基准；页面未提及。
- **online A/B test** — 在线比较不同检索方案；页面未提及。
- **adversarial retrieval** — 面向攻击或异常查询的检索；页面未提及。
- **prompt injection in retrieved content** — 检索资料中可能包含的提示注入；页面未提及。
- **data poisoning** — 恶意污染检索资料或索引；页面未提及。
- **privacy-preserving retrieval** — 保护敏感资料的检索；页面只泛泛提到 access / permissions。
- **PII / personally identifiable information** — 个人可识别信息；页面未提及。
- **multilingual retrieval** — 跨语言检索；页面未提及。
- **multimodal retrieval** — 跨文字、图像等模态检索；页面未提及。
- **knowledge graph retrieval** — 从知识图谱中检索实体和关系；页面未提及。
- **graph retrieval** — 基于图结构的检索；页面未提及。
- **SQL retrieval** — 从关系数据库通过 SQL 取数；页面未提及。
- **structured retrieval** — 检索结构化记录；页面只说 records，没有定义结构化检索。
- **unstructured retrieval** — 检索非结构化文档；页面没有该分类。

## Aliases / Synonyms

- retrieval ↔ information retrieval ↔ IR
- retrieve ↔ find and return ↔ look up ↔ fetch
- relevant information ↔ useful information ↔ task-relevant information
- source collection ↔ document collection ↔ corpus ↔ searchable collection
- source ↔ information source ↔ source material ↔ source document
- query ↔ request ↔ question ↔ information need
- candidate ↔ candidate item ↔ possible match ↔ possible result
- candidate set ↔ initial result set ↔ retrieved candidates
- select information ↔ choose information ↔ filter for relevance ↔ pick relevant items
- selection ↔ subset selection ↔ information selection
- return ↔ retrieve ↔ send back ↔ pass onward
- result ↔ returned result ↔ search result ↔ retrieved item
- evidence ↔ supporting information ↔ source evidence ↔ answer support
- downstream task ↔ later task ↔ downstream use ↔ next step
- retrieval system ↔ retriever ↔ search-and-retrieval system
- retrieval workflow ↔ retrieval flow ↔ retrieval pipeline ↔ search pipeline
- Query ↔ query step ↔ read the request
- Search ↔ search step ↔ candidate search ↔ candidate generation
- Rank ↔ ranking ↔ order results ↔ rerank
- Filter ↔ filtering ↔ apply constraints ↔ post-filtering
- Return ↔ return step ↔ send evidence ↔ pass selected records
- text search ↔ keyword search ↔ lexical search ↔ sparse retrieval
- vector search ↔ semantic search ↔ dense retrieval ↔ similarity search
- metadata search ↔ metadata filtering ↔ structured filtering
- hybrid search ↔ hybrid retrieval ↔ combined retrieval
- keyword ↔ search term ↔ query term ↔ lexical term
- vector ↔ vector representation ↔ embedding vector
- metadata ↔ descriptive fields ↔ source attributes
- access ↔ permission ↔ authorization ↔ access control
- freshness ↔ recency ↔ currency ↔ up-to-dateness
- current document ↔ up-to-date document ↔ fresh document
- allowed source ↔ permitted source ↔ authorized source
- support article ↔ help article ↔ help-center article
- help center ↔ support center ↔ knowledge base (in a support context)
- policy review ↔ policy checking ↔ policy audit
- generation ↔ model generation ↔ content generation ↔ new-output creation
- existing information ↔ existing content ↔ stored information
- RAG ↔ Retrieval-Augmented Generation ↔ retrieval-augmented generation
- retrieved evidence ↔ retrieved context ↔ selected source context
- grounding ↔ evidence grounding ↔ source grounding
- query vector ↔ query embedding ↔ embedded query
- document vector ↔ document embedding ↔ embedded document
- similarity ↔ semantic similarity ↔ vector similarity
- similarity score ↔ relevance score ↔ retrieval score
- nearest neighbor ↔ nearest item ↔ closest candidate
- top-k ↔ top k ↔ first k results
- ranker ↔ reranker ↔ ranking model
- precision ↔ precision@k ↔ top-k precision (when k is explicit)
- recall ↔ recall@k ↔ top-k recall (when k is explicit)
- MRR ↔ mean reciprocal rank
- NDCG ↔ normalized discounted cumulative gain
- false positive ↔ irrelevant result returned ↔ over-retrieval
- false negative ↔ missed relevant result ↔ under-retrieval
- source provenance ↔ source attribution ↔ evidence traceability
- alias ↔ alternate name ↔ alternate term
- synonym ↔ near-synonym ↔ same-or-similar meaning term

## Do Not Confuse Candidates

- **Retrieval vs search**：search 可以泛指查找操作或用户看到的搜索结果；retrieval 更强调为一个任务选择并返回相关信息。
- **Retrieval vs search results**：search results 可能直接展示给用户；retrieval 的结果通常还要被人、应用或模型用于下游任务。
- **Retrieval vs generation**：retrieval 找已有信息；generation 创建新的模型输出。
- **Retrieval vs RAG**：retrieval 是选择资料的步骤；RAG 是把 retrieval 与 model generation 组合起来的完整工作流。
- **Retrieval vs vector search**：vector search 是一种按向量相似性查找的方法；retrieval 是更宽泛的找回相关信息的任务。
- **Retrieval vs keyword search**：keyword search 主要依赖字面词语；retrieval 可以使用关键词、向量、metadata、filters 或这些方法的组合。
- **Vector search vs semantic search**：vector search 通常用向量空间中的相似度；semantic search 强调按含义查找，具体实现不一定只有一种。
- **Keyword search vs metadata search**：keyword search 查文本词语；metadata search 查资料附带的描述字段。
- **Metadata vs source content**：metadata 描述来源、时间、类别或权限；source content 是真正被查找或作为证据使用的内容。
- **Filter vs rank**：filter 按硬性约束排除结果；rank 对仍然可用的候选排序，二者目的不同。
- **Rank vs rerank**：rank 可以是第一次排序；rerank 通常指对已有候选结果进行再次排序。
- **Candidate vs result**：candidate 仍在被考虑；result 通常指已经返回或作为输出呈现的项目。
- **Relevant vs useful**：relevant 表示与查询或任务有关；useful 还暗示它对完成任务有实际帮助。
- **Source collection vs retrieved evidence**：source collection 是待查的大集合；retrieved evidence 是从中挑出的少量资料。
- **Source document vs retrieved context**：source document 是原始文件；retrieved context 是查询后被选出来交给下游使用的内容。
- **Existing information vs new output**：已有信息在检索前就存在；new output 是模型这次生成的新内容。
- **Evidence vs answer**：evidence 是支持回答的资料；answer 是后续系统或模型形成的回应。
- **Evidence vs citation**：evidence 是实际支持内容；citation 是指向其来源的引用或出处标记。
- **Access vs freshness**：access 判断用户能不能看；freshness 判断资料是否足够新，不能互相替代。
- **Allowed document vs current document**：allowed document 满足权限要求；current document 满足时效要求，一份文档可能只满足其中一个。
- **User permissions vs source rules**：user permissions 针对请求者的访问资格；source rules 针对允许使用哪些资料来源。
- **Query vs query vector**：query 是原始问题或请求；query vector 是把查询编码后的数字表示。
- **Document vs chunk**：document 是完整或较大的原始资料；chunk 是其中为检索切出的片段。
- **Keyword vs token**：keyword 是用于查找的有意义词或短语；token 是模型处理文本时的切分单位。
- **Similarity vs relevance**：similarity 是算法计算的接近程度；relevance 是结合查询和任务判断的相关性。
- **Similarity vs truth**：相似度高不等于资料真实、正确或符合政策。
- **Nearest item vs best answer**：最接近的候选通常只是相关资料，不保证就是最终答案。
- **Precision vs recall**：precision 关注返回结果中有多少相关；recall 关注所有相关结果中有多少被找回。
- **Recall vs recall@k**：recall 是一般召回概念；recall@k 限定只看前 k 个结果。
- **MRR vs NDCG**：MRR 主要看第一个相关结果的排名；NDCG 可以综合多个结果及其相关等级。
- **Top-k vs all results**：top-k 只返回排名前 k 项；all results 表示更完整的结果集合。
- **Vector database vs retrieval system**：vector database 负责存储和支持向量查找；retrieval system 还可能包含 query understanding、ranking、filtering 和下游交付。
- **Inverted index vs vector index**：inverted index 常服务关键词检索；vector index 常服务向量相似度检索。
- **Pre-filtering vs post-filtering**：pre-filtering 在查找前限制候选；post-filtering 在候选产生后再应用条件。
- **Dense retrieval vs sparse retrieval**：dense retrieval 通常使用稠密向量；sparse retrieval 通常依赖词项或稀疏表示。
- **Bi-encoder vs cross-encoder**：bi-encoder 分别编码查询与候选以提高召回效率；cross-encoder 联合输入两者以进行更精细评分。
- **Retrieval quality vs answer quality**：检索找得好不一定保证模型回答好；回答质量还受到生成、推理和表达影响。
- **Search relevance vs business suitability**：搜索结果相关不代表满足权限、时效、来源或其他业务条件。
- **Freshness vs recency**：recency 常指距离更新时间的远近；freshness 还可能包含“当前是否有效”的含义。
- **Access control vs authentication**：access control 决定能访问什么；authentication 只确认访问者是谁。
- **Grounding vs generation**：grounding 让输出有来源依据；generation 负责产生输出内容。
- **Hallucination vs irrelevant retrieval**：hallucination 是模型生成无依据内容；irrelevant retrieval 是检索阶段返回了不相关资料。
- **Retrieval failure vs ranking failure**：retrieval failure 可能完全漏掉相关资料；ranking failure 是相关资料找到了但没排在前面。
- **Video, poster, captions vs retrieval mechanism**：页面中的 video、poster、captions 是呈现资源相关词，不是检索机制本身。

## Notes

- 本文件是 `retrieval.html` 的 raw glossary 收集稿，按要求尽可能保留正文直接出现或由正文明确触发的专业术语、流程节点、例子词、对照词、相关概念、别名和易混淆概念；不做最终去重、归并或删减。
- 页面元信息为 `05 · Embeddings, RAG & Vector Search · Topic 05`；本任务指定的输出模块编号和文件名为 `08-retrieval.md`，因此两套信息都保留在 Topic Metadata 中。
- 页面核心定义是：Retrieval selects relevant information from a larger source collection for a task；定义段进一步说明 retrieval 是 finding and selecting information relevant to a query 的过程。
- 页面明确列出 retrieval system 可以使用 keywords、vectors、metadata、filters，或这些 methods 的 combination；返回内容可以供 a person、an application 或 a model 使用。
- 页面类比是“finding the right pages in a library”：资料集合很大，但一个 question 通常只需要 small selection，retrieval 在 next step 使用前先选择该部分。
- 页面五步流程必须作为核心候选保留：1. Query / Read the request / Identify the information needed；2. Search / Find candidates / Use text, vector, metadata, or hybrid search；3. Rank / Order results / Put the most useful candidates first；4. Filter / Apply constraints / Respect access, freshness, and source rules；5. Return / Send evidence / Pass selected records to the next step。
- Everyday example 是 Help center：input 是 a question about an account；system retrieves relevant support articles；output 是 a short list of useful sources。
- Business example 是 Policy review：input 是 a policy question and user permissions；system retrieves allowed, current documents；output 是 evidence for an answer or review。
- 页面明确对比三组边界：Retrieval ≠ Search Results Only、Retrieval ≠ Generation、Retrieval ≠ RAG；这些对照标题和两侧概念都应保留。
- 页面相关概念流程树是 `Query → Search → Rank → Filter → Retrieved evidence`；Explore next 直接列出 Vector Search、RAG、Grounding、Embeddings。
- 页面 Remember this 的核心句是：Retrieval selects useful existing information before another system or model uses it。
- 页面正文明确出现的主要数据和控制对象包括 query、information、source collection、candidates、results、access、freshness、source rules、records、evidence、person、application、model；它们在 raw 阶段不应仅因常见而删掉。
- 页面正文没有明确给出 cosine similarity、dot product、ANN、BM25、具体 vector database、索引结构或评估公式；这些放入 Potential Missing Concepts，不能当作页面已定义内容。
- 页面正文没有直接列出 precision、recall、MRR、NDCG 等 retrieval metrics；这些是检索主题常见缺口候选，因此单独保留并明确标注为未明示。
- 页面没有展开 document ingestion、chunking、query rewriting、reranking、权限架构或安全攻击；相关工程词作为扩展候选保留，而非页面事实。
- 页面采用大写流程标签 `Query`、`Search`、`Rank`、`Filter`、`Return`，同时在段落中使用小写 retrieval、query、search 等形式；raw 阶段按可追踪性保留大小写和重复形式。
- 页面的视频区域只出现 Independent explainer、Video、visual explainer、poster、captions 和视频文件资源；这些低优先级词可追踪，但不应被误认为 retrieval 机制。
