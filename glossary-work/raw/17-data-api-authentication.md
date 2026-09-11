# Topic

Data, APIs & Authentication

## Module/Topic/Source File

- Module: 17 · Product Architecture
- Topic: Data, APIs & Authentication
- Source File: `data-api-authentication.html`
- Page Title: `Data, APIs & Authentication · Product Architecture`
- Page framing: Products need ways to store information, communicate between systems, identify users, and control access.

## Glossary Candidates

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| data | 数据 | Information a product stores, moves, or uses. | 产品要保存、传递和使用的信息。 |
| data system | 数据系统 | A system that stores or handles information. | 负责保存或处理数据的一套系统。 |
| data systems | 数据系统（复数） | Multiple systems that store or handle information. | 多套保存或处理数据的系统。 |
| product | 产品 | A software product that needs data, communication, identity, and access control. | 需要数据和权限能力的软件产品。 |
| store information | 存储信息 | Keep information so it can be used later. | 把信息保存下来以后继续使用。 |
| communicate between systems | 系统之间通信 | Exchange requests and information between software systems. | 不同软件之间互相传递请求和信息。 |
| identify users | 识别用户 | Determine which user is trying to use a product. | 判断当前使用产品的人是谁。 |
| control access | 控制访问 | Decide who can reach or change something. | 决定谁可以访问或修改内容。 |
| USER | 用户（页面流程标签） | The person or actor starting the product flow. | 发起使用流程的人或参与者。 |
| user | 用户 | A person using the application. | 使用应用的人。 |
| authentication | 身份认证；身份验证 | The process of confirming who someone is. | 证明“你是谁”的过程。 |
| AUTHENTICATION | 身份认证（页面大写标签） | The identity-confirming step in the product flow. | 流程中确认用户身份的一步。 |
| who are you? | 你是谁？ | The question authentication answers. | 身份认证要回答的问题。 |
| application | 应用程序；应用 | Software that handles the product experience and requests data or services. | 用户使用的、负责处理工作的软件。 |
| APPLICATION | 应用（页面流程标签） | The application between the user and the API. | 流程中接收用户操作并调用接口的应用。 |
| API | 应用程序编程接口；接口 | A defined way for software systems to communicate. | 软件按约定互相请求数据或动作的入口。 |
| Application Programming Interface | 应用程序编程接口 | The expanded form of API. | API 这个缩写的完整名称。 |
| API interface | API 接口 | The communication boundary exposed for software requests. | 软件发请求时使用的接口边界。 |
| how systems communicate | 系统如何通信 | The role an API plays between software systems. | API 负责规定系统之间如何交换信息。 |
| defined way | 约定好的方式 | A specified format or boundary for communication. | 双方事先约定好的沟通方式。 |
| software system | 软件系统 | Software that can communicate with another system. | 能和其他软件交换信息的程序系统。 |
| software systems | 软件系统（复数） | Separate programs or services that exchange requests and results. | 互相交换请求和结果的多套软件。 |
| database | 数据库 | A place for structured application data. | 按结构保存应用数据的地方。 |
| DATABASE | 数据库（页面流程标签） | The structured-data component in the product flow. | 流程中保存结构化数据的部分。 |
| structured data | 结构化数据 | Data organized into fields or a predictable structure. | 按字段和固定结构组织的数据。 |
| structured application data | 结构化应用数据 | Product data organized for application use. | 按应用需要组织好的业务数据。 |
| user record | 用户记录 | Structured data describing a user. | 数据库里描述用户的一条记录。 |
| user | 用户 | An example of structured application data. | 数据库中可以保存的一类对象。 |
| order | 订单 | An example of structured application data. | 数据库中可以保存的订单信息。 |
| lesson progress | 课程进度 | An example of structured application data. | 学习应用中记录用户学到哪里的数据。 |
| storage | 存储；文件存储 | A place for files and media. | 保存文件和媒体的地方。 |
| STORAGE | 存储（页面流程标签） | The file/media component in the product flow. | 流程中提供文件或媒体的部分。 |
| file | 文件 | A separately stored piece of content. | 被单独保存的一份内容。 |
| files | 文件（复数） | Stored content such as images, videos, PDFs, or audio. | 图片、视频、PDF、音频等保存的内容。 |
| media | 媒体 | Content such as images, video, or audio. | 图片、视频、音频等媒体内容。 |
| image | 图片；图像 | A file or media example stored outside the database. | 通常放在文件存储中的图片文件。 |
| video | 视频 | A file or media example stored outside the database. | 通常放在文件存储中的视频文件。 |
| PDF | PDF 文件 | A document file example stored in storage. | 放在文件存储中的 PDF 文档。 |
| audio | 音频 | A media file example stored in storage. | 放在文件存储中的声音文件。 |
| database vs storage | 数据库与存储的区别 | A comparison between structured records and files. | 数据库保存结构化记录，存储保存文件。 |
| Database ≠ File Storage | 数据库不等于文件存储 | A reminder that structured records and files are different things. | 数据库和文件存储用途不同，不能混为一谈。 |
| file storage | 文件存储 | Storage intended for files and media. | 专门保存文件和媒体的存储。 |
| record | 记录 | A structured item stored in a database. | 数据库里的一条结构化信息。 |
| information | 信息 | Content that can be stored or returned by a system. | 系统保存或返回的内容。 |
| API request | API 请求 | A request sent through an API to another system. | 按接口规则发给另一个系统的请求。 |
| request | 请求 | A message asking a system for data or an action. | 一个系统向另一个系统提出的要求。 |
| REQUEST | 请求（页面流程标签） | The message sent from App A toward an API. | 应用 A 发往接口的消息。 |
| API response | API 响应 | A result returned through an API. | 通过接口返回给调用方的结果。 |
| response | 响应；回复 | Information returned after a request is handled. | 请求处理后返回的信息。 |
| RESPONSE | 响应（页面流程标签） | The result sent back to the requesting application. | 返回给请求方应用的结果。 |
| APP A | 应用 A（页面流程标签） | The software system starting the API exchange. | 发起接口请求的应用。 |
| APP B / SERVICE | 应用 B／服务（页面流程标签） | The application or service receiving the request. | 接收并处理请求的另一个应用或服务。 |
| service | 服务 | Software that receives requests and provides a capability or result. | 接收请求并提供能力或结果的软件。 |
| software systems communicate | 软件系统通信 | One system sends a request and another returns a response. | 一个系统发请求，另一个系统返回结果。 |
| request-response flow | 请求—响应流程 | A flow in which a request is followed by a response. | 先提出请求、再收到回复的流程。 |
| request-response exchange | 请求—响应交换 | The two-way exchange between a caller and a service. | 调用方和服务之间的一来一回。 |
| call an API | 调用 API | Send a request through an API. | 通过接口请另一个系统做事。 |
| API call | API 调用 | One invocation of an API. | 对某个接口发起的一次调用。 |
| caller | 调用方 | The application or system sending a request. | 发出接口请求的一方。 |
| backend | 后端 | Server-side software behind the application. | 网站或应用背后处理数据和业务的部分。 |
| backend service | 后端服务 | A server-side service reached by an application. | 应用通过接口访问的服务端程序。 |
| communicate with backend | 与后端通信 | Use an API to exchange requests and results with server-side software. | 应用通过接口和后端交换信息。 |
| authentication vs authorization | 身份认证与授权的区别 | A comparison between proving identity and deciding permissions. | 一个确认身份，一个决定能做什么。 |
| authorization | 授权；访问控制 | The process of deciding what an identified user is allowed to do. | 决定“你能做什么”的过程。 |
| AUTHORIZATION | 授权（页面大写标签） | The access-control step in the product flow. | 流程中判断权限的一步。 |
| what are you allowed to do? | 你被允许做什么？ | The question authorization answers. | 授权要回答的问题。 |
| access | 访问；使用权限 | The ability to reach or use a resource or operation. | 能不能进入或使用某项内容。 |
| access control | 访问控制 | Rules that limit access to data or actions. | 限制谁能访问数据或执行操作的规则。 |
| permission | 权限 | An allowed ability to view, change, or perform something. | 被允许查看、修改或执行某事的资格。 |
| login | 登录 | An example of authentication. | 用户输入凭证进入产品的动作。 |
| log in | 登录 | Authenticate a user into an application. | 用户完成身份确认并进入应用。 |
| admin | 管理员 | A user role with elevated permissions in the example. | 拥有更多管理权限的用户。 |
| delete record | 删除记录 | An operation an authorized admin may perform. | 有权限的管理员可以执行的删除操作。 |
| admin can delete record | 管理员可以删除记录 | An example of authorization deciding an allowed action. | 例子：只有有相应权限的管理员能删记录。 |
| identify | 识别 | Determine the identity of a user or actor. | 判断使用者是谁。 |
| confirm identity | 确认身份 | Verify that a login belongs to the claimed user. | 验证登录者确实是所声称的那个人。 |
| identity | 身份 | The user or actor represented by an authenticated session. | 系统确认后的用户身份。 |
| AI learning app | AI 学习应用 | A learning application that uses AI and connected product services. | 用 AI 帮助学习的应用。 |
| one real example | 一个真实示例 | The page's end-to-end AI learning app scenario. | 页面用来串起各个概念的完整例子。 |
| USER LOGS IN | 用户登录（页面流程标签） | The first action in the example flow. | 示例流程的第一步：用户登录。 |
| confirms identity | 确认身份 | Authentication verifies the user in the example. | 身份认证确认当前用户是谁。 |
| APP REQUESTS LESSON | 应用请求课程（页面流程标签） | The application asks the backend for a lesson. | 应用向后端请求课程内容。 |
| requests lesson | 请求课程 | Ask the backend for a lesson. | 应用发请求获取一节课。 |
| AI API | AI 接口 | An API that provides an AI capability. | 能调用 AI 能力的接口。 |
| AI API generates feedback | AI 接口生成反馈 | An AI API returns generated learning feedback. | AI 接口根据学习内容生成反馈。 |
| generates feedback | 生成反馈 | Produce feedback using an AI capability. | 用 AI 产出对学习者有帮助的意见。 |
| feedback | 反馈 | A response or guidance generated for the learner. | 给学习者的评价、建议或回应。 |
| returns progress | 返回进度 | The database returns stored lesson progress. | 数据库返回用户之前保存的学习进度。 |
| progress | 进度 | Stored information about how far a learner has advanced. | 表示用户学习到哪里的信息。 |
| provides audio file | 提供音频文件 | Storage supplies an audio file to the application. | 文件存储把音频文件提供给应用。 |
| audio file | 音频文件 | A sound file provided by storage. | 文件存储中的一份声音内容。 |
| data flow | 数据流 | The path data and requests take through product components. | 数据和请求在各个组件之间经过的路线。 |
| application flow | 应用流程 | The sequence from user action to returned product result. | 从用户操作到系统返回结果的一系列步骤。 |
| process | 过程；流程 | An ordered set of actions that produces a result. | 按顺序完成的一组动作。 |
| component | 组件 | One part of the product architecture. | 产品架构中的一个组成部分。 |
| product architecture | 产品架构 | The arrangement of product components and their interactions. | 产品各部分如何组成并互相配合。 |
| architecture | 架构 | The structure connecting applications, APIs, data, and access control. | 应用、接口、数据和权限的整体结构。 |
| common platform examples | 常见平台示例 | Tools and patterns encountered in this area. | 数据和接口领域中常见的工具或模式。 |
| platform | 平台 | A software service or technology used to build a product. | 用来搭建产品的一类软件平台。 |
| Supabase | Supabase | A platform example associated with data and backend services. | 页面列出的一个后端与数据平台例子。 |
| Firebase | Firebase | A platform example associated with application backend services. | 页面列出的一个应用后端平台例子。 |
| PostgreSQL | PostgreSQL | A database technology example. | 页面列出的一个数据库技术例子。 |
| Cloud Storage | 云存储 | A storage technology or pattern for files and media. | 页面列出的一个云端文件存储例子。 |
| REST APIs | REST API；REST 接口 | A common API pattern for communicating with services. | 页面列出的常见接口设计模式。 |
| tool | 工具 | A technology or pattern used to build or connect a product. | 用来实现产品能力的工具或技术。 |
| pattern | 模式 | A reusable way of organizing a technical solution. | 可以反复使用的一种技术组织方式。 |
| detailed comparisons | 详细比较 | Deeper comparisons planned for later content. | 页面说明后续会再详细比较这些例子。 |
| remember this | 记住这一点 | The page's summary of the architecture. | 页面最后帮助记忆的总结。 |
| store information | 存储信息 | The role of data systems in a product. | 数据系统把信息保存下来。 |
| connect software | 连接软件 | The role of APIs in a product. | API 把不同软件连接起来。 |
| controls who can access the product | 控制谁能访问产品 | The role of authentication and access control. | 身份和权限机制决定谁可以使用产品。 |
| product access | 产品访问权限 | Permission to access the product or its capabilities. | 用户进入和使用产品的资格。 |

## Potential Missing Concepts

The page introduces the concepts at a high level but does not define the following likely next-step terms. Keep these as missing-concept candidates rather than treating them as page claims:

- endpoint（端点）
- route（路由）
- URL（统一资源定位符）
- HTTP（超文本传输协议）
- HTTP method（HTTP 方法）
- GET / POST / PUT / PATCH / DELETE
- status code（状态码）
- JSON（JavaScript Object Notation）
- request header（请求头）
- response header（响应头）
- request body（请求体）
- response body（响应体）
- payload（载荷）
- schema（模式；数据结构）
- validation（校验）
- serialization（序列化）
- deserialization（反序列化）
- API documentation（API 文档）
- OpenAPI（开放 API 规范）
- SDK（软件开发工具包）
- client library（客户端库）
- ORM（对象关系映射）
- CRUD（创建、读取、更新、删除）
- SQL（结构化查询语言）
- relational database（关系型数据库）
- NoSQL database（非关系型数据库）
- table / row / column（表／行／列）
- primary key（主键）
- foreign key（外键）
- database index（数据库索引）
- transaction（事务）
- consistency（一致性）
- migration（迁移）
- backup（备份）
- replication（复制）
- object storage（对象存储）
- blob（对象／二进制大对象）
- bucket（存储桶）
- CDN（内容分发网络）
- signed URL（签名 URL）
- file metadata（文件元数据）
- MIME type（媒体类型）
- authentication factor（认证因素）
- credential（凭证）
- password hashing（密码哈希）
- session（会话）
- cookie（Cookie）
- token（令牌）
- access token（访问令牌）
- refresh token（刷新令牌）
- bearer token（Bearer 令牌）
- JWT（JSON Web Token）
- OAuth（开放授权）
- OpenID Connect（身份层协议）
- SSO（单点登录）
- MFA / 2FA（多因素／双因素认证）
- API key（API 密钥）
- service account（服务账户）
- authorization scope（授权范围）
- role-based access control / RBAC（基于角色的访问控制）
- ACL（访问控制列表）
- row-level security / RLS（行级安全）
- user role（用户角色）
- ownership（资源归属）
- least privilege（最小权限）
- audit log（审计日志）
- CORS（跨源资源共享）
- CSRF（跨站请求伪造）
- TLS / HTTPS（传输层安全／安全 HTTP）
- encryption（加密）
- secret management（密钥管理）
- rate limiting（速率限制）
- quota（配额）
- pagination（分页）
- filtering / sorting（过滤／排序）
- retry（重试）
- timeout（超时）
- idempotency（幂等性）
- caching（缓存）
- webhook（网络钩子）
- polling（轮询）
- event-driven integration（事件驱动集成）
- API versioning（API 版本管理）
- backward compatibility（向后兼容）
- deprecation（弃用）
- latency（延迟）
- response time（响应时间）
- throughput（吞吐量）
- availability（可用性）
- error rate（错误率）
- observability（可观测性）
- monitoring（监控）
- logging（日志记录）

## Aliases / Synonyms

- Data ↔ information
- data system ↔ data layer ↔ data service
- database ↔ structured data store ↔ application data store
- record ↔ row ↔ structured item（row 更具体，页面未展开）
- storage ↔ file storage ↔ media storage
- file ↔ stored file ↔ media file（media file 更具体）
- API ↔ Application Programming Interface ↔ application interface ↔ software interface
- API request ↔ request ↔ API call（call 强调调用动作）
- API response ↔ response ↔ returned result
- application ↔ app ↔ software application
- service ↔ backend service ↔ software service
- backend ↔ server side ↔ backend service（不完全同义）
- caller ↔ requesting application ↔ client application
- authentication ↔ identity verification ↔ login authentication
- authorization ↔ access control ↔ permission control
- identity ↔ user identity ↔ authenticated identity
- permission ↔ allowed action ↔ access right
- login ↔ log in ↔ sign in（sign in 是常用别名，页面未出现）
- user progress ↔ lesson progress ↔ learning progress
- feedback ↔ generated feedback ↔ learning feedback
- audio ↔ audio file ↔ sound file
- image ↔ image file
- video ↔ video file
- PDF ↔ PDF file ↔ document file
- REST APIs ↔ REST API ↔ RESTful APIs（RESTful 是常见别名，页面未展开）
- Cloud Storage ↔ cloud file storage ↔ object storage（object storage 更具体）
- data flow ↔ application flow ↔ product flow
- product architecture ↔ application architecture ↔ system architecture
- AI API ↔ AI service API ↔ model API（model API 更具体）
- control access ↔ control permissions ↔ restrict access
- confirm identity ↔ verify identity ↔ authenticate the user
- request a lesson ↔ app requests lesson ↔ lesson request
- return progress ↔ return learning progress ↔ progress response
- provides audio file ↔ serves audio ↔ returns an audio asset

## Do Not Confuse Candidates

- **database vs storage**：数据库保存结构化应用数据；存储保存文件和媒体。页面明确写出 “Database ≠ File Storage”。
- **data vs database**：data 是信息本身；database 是保存结构化信息的系统或位置。
- **record vs file**：record 是数据库中的结构化条目；file 是文件存储中的独立内容。
- **storage vs Cloud Storage**：storage 是通用的文件存储概念；Cloud Storage 是页面列出的平台或技术示例。
- **API vs application**：API 是通信接口；application 是使用接口或承载用户体验的软件。
- **API vs service**：API 是服务暴露出来的调用方式；service 是实际接收请求并提供能力的程序。
- **API vs API call**：API 是接口定义；API call 是对该接口发起的一次调用。
- **request vs response**：request 是提出要求；response 是处理后返回的结果。
- **request vs API**：request 是一次消息；API 是规定消息如何交互的接口。
- **caller vs called service**：caller 发出请求；called service 接收和处理请求。
- **backend vs API**：backend 是服务端软件；API 是访问后端能力的接口。
- **software system vs application**：application 是一种软件系统；software system 是更宽泛的称呼。
- **authentication vs authorization**：authentication 回答“你是谁”；authorization 回答“你能做什么”。
- **authentication vs login**：authentication 是确认身份的机制或过程；login 是页面给出的一个认证例子或用户动作。
- **identity vs permission**：identity 表示用户是谁；permission 表示用户被允许做什么。
- **access vs authorization**：access 是实际能够使用；authorization 是决定是否允许使用的控制过程。
- **admin vs authorization**：admin 是一个角色；authorization 是判断该角色能否执行某动作的机制。
- **identify users vs control access**：识别用户先确认是谁；控制访问再决定能否访问或操作。
- **user vs user record**：user 是现实中的使用者或业务对象；user record 是数据库中描述该对象的数据。
- **lesson progress vs feedback**：lesson progress 是保存的学习进度；feedback 是 AI 生成的反馈。
- **AI API vs API**：AI API 是提供 AI 能力的一类 API；API 是更广泛的接口概念。
- **AI API vs AI model**：AI API 是访问入口；模型是可能在接口后面生成结果的 AI 组件，页面未展开模型本身。
- **audio file vs audio**：audio 是媒体类型；audio file 是作为文件提供的具体音频内容。
- **file vs media**：file 强调存储形式；media 强调内容类型。
- **REST APIs vs APIs**：REST APIs 是 API 的一种常见模式；API 还可以采用其他设计方式。
- **Supabase vs PostgreSQL**：Supabase 是平台示例；PostgreSQL 是数据库技术示例，二者不是同一层级。
- **Firebase vs database**：Firebase 是平台示例；database 是数据存储组件或概念。
- **Cloud Storage vs database**：Cloud Storage 用于文件或媒体；database 用于结构化应用数据。
- **platform vs pattern**：platform 是工具或服务；pattern 是可复用的组织方式。
- **application flow vs data flow**：application flow 强调步骤顺序；data flow 强调请求和数据经过的路径。
- **defined way vs implementation detail**：API 的定义方式是对外约定；具体数据库、网络和代码实现可能不同。
- **authentication vs authorization vs access**：认证证明身份，授权决定许可，访问是许可生效后的实际使用能力。
- **API response vs feedback**：response 是任何请求返回的结果；feedback 是 AI 学习场景中的一种具体结果。
- **database returns progress vs storage provides audio file**：前者从数据库取结构化记录；后者从存储取文件。
- **communicate between systems vs user login**：系统通信描述软件间交互；登录描述用户身份确认。
- **product access vs record deletion**：访问产品不代表允许删除记录；具体操作还受授权控制。

## Notes

- 本文件是 Module 17 Topic “Data, APIs & Authentication” 的 raw glossary 收集稿；按 `data-api-authentication.html` 的完整可见正文收集，目标是最大化保留候选，不做去重、归并或最终取舍。
- 页面主流程按原文保留为：`USER → AUTHENTICATION → APPLICATION → API → DATABASE ＋ STORAGE`；旁注补充 `AUTHORIZATION`，分别对应确认身份和判断允许做什么。
- 页面把 database 定义为 structured application data，并以 user、order、lesson progress 为例；把 storage 定义为 files，并以 image、video、PDF、audio 为例。
- 页面明确强调 `Database ≠ File Storage`，这是本主题最重要的易混淆边界之一。
- 页面把 API 定义为软件系统通信的 defined way，并用 `APP A → REQUEST → API → APP B / SERVICE → RESPONSE` 展示请求—响应交互。
- 页面将 authentication 的例子写为 `Login`，将 authorization 的例子写为 `Admin can delete record`；不要把登录成功理解成自动拥有所有操作权限。
- AI Learning App 示例的原始流程是：`USER LOGS IN → AUTHENTICATION（confirms identity）→ APP REQUESTS LESSON → API（communicates with backend）→ DATABASE（returns progress）→ AI API（generates feedback）＋ STORAGE（provides audio file）`。
- Common Platform Examples 原文列出 `Supabase`、`Firebase`、`PostgreSQL`、`Cloud Storage`、`REST APIs`，并说明它们是可能遇到的 tools and patterns，详细比较留到后续。
- 页面没有给出数值指标或性能数据；`latency`、`response time`、`throughput`、`availability`、`error rate` 等因此只放入 Potential Missing Concepts，不应写成页面已说明的指标。
- 页面是 beginner-friendly guide，正文没有展开 endpoint、HTTP、JSON、API key、OAuth、JWT、session、RBAC、RLS、加密、错误处理、版本管理等实现细节；这些候选保留用于后续 glossary 扩展。
- HTML 中还出现页面导航词 `How the pieces fit`、`Database vs Storage`、`What is an API?`、`Authentication vs authorization`、`Real example`、`Examples`、`Remember this`；这些标题语义已映射进候选和备注。
- `API`、`DATABASE`、`STORAGE`、`AUTHENTICATION`、`AUTHORIZATION` 等大写形式来自流程图或卡片标签；raw 阶段保留大小写语义，不强行统一。
- 本文件只新增 glossary raw 资料，不修改网站文件或 GitHub。
