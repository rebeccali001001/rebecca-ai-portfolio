# Topic

Structured Outputs

## Topic Metadata

- Module: 06 · Structured Outputs
- Topic: Structured Outputs
- Source Page Context: 04 · Prompting & System Design · Topic 02 (as shown in the HTML)
- Source File: `structured-outputs.html`
- Source Title: What are Structured Outputs?
- Source Description: Structured outputs make an AI response follow a defined data shape.
- Raw-stage policy: Maximum candidate inventory; retain overlapping, repeated, surface-form, alias, and potentially confusable candidates for later normalization.

## Glossary Candidates

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Structured Outputs | 结构化输出 | A way to make an AI response follow a defined data shape. | 让 AI 的回答按照规定好的数据形状返回。 |
| structured output | 结构化输出 | A model response that follows a defined schema or format. | 符合指定结构或格式的模型回答。 |
| structured outputs | 结构化输出 | Model responses constrained to a defined shape. | 按固定形状组织的模型回答。 |
| Structure output (singular wording) | 结构化输出（单数写法） | The singular form of structured outputs. | “structured outputs” 的单数说法。 |
| AI response | AI 回应 | A response produced by an artificial-intelligence system. | AI 系统给出的回答。 |
| model response | 模型回应 | A response produced by a model. | 模型产生的回答。 |
| response | 回应；回答 | The result returned in response to a task or request. | 系统回答问题后返回的结果。 |
| result | 结果 | The produced answer or data returned by a system. | 系统最终产出的东西。 |
| defined data shape | 定义好的数据形状 | The required organization of a response's data. | 事先规定好的数据组织方式。 |
| data shape | 数据形状；数据结构 | The arrangement and organization expected for data. | 数据应该长什么样、怎样组织。 |
| defined shape | 定义好的形状 | A response form specified in advance. | 提前规定好的返回形态。 |
| shape | 形状；结构 | The overall organization of a response. | 回答整体的组织结构。 |
| schema | 模式；架构；结构定义 | A formal description of the fields and rules a result should follow. | 描述结果有哪些字段、什么类型、有什么规则的说明。 |
| defined schema | 定义好的模式 | A schema specified before a model returns a result. | 模型返回结果前就规定好的结构说明。 |
| schema or format | 模式或格式 | The defined structure or representation of a response. | 结果需要遵守的结构或格式。 |
| format | 格式 | The way data is represented and arranged. | 数据呈现和排列的方式。 |
| defined format | 定义好的格式 | A required representation selected in advance. | 提前规定的结果格式。 |
| data format | 数据格式 | The representation used for data. | 数据采用的表达格式。 |
| field | 字段 | A named part of a structured result. | 结构化结果中的一个命名栏位。 |
| fields | 字段集合 | Named parts that make up a structured result. | 组成结构化结果的多个栏位。 |
| field definition | 字段定义 | A description of what a field represents. | 说明某个字段代表什么。 |
| field name | 字段名 | The name used to identify a field. | 用来识别字段的名称。 |
| field value | 字段值 | The value stored in a field. | 填入某个字段里的具体内容。 |
| required field | 必填字段 | A field that must be present in the result. | 结果中必须出现的字段。 |
| required values | 必填值；要求的值 | Values that the result is required to contain. | 结果必须提供的内容。 |
| required value | 必填值 | One value that must be supplied. | 必须填上的一个值。 |
| type | 类型 | The kind of value a field is allowed to contain. | 某个值属于哪一种数据类型。 |
| data type | 数据类型 | A category such as text, number, or boolean. | 例如文字、数字或真假值这样的类别。 |
| field type | 字段类型 | The data type assigned to a field. | 某个字段规定使用什么类型的数据。 |
| allowed option | 允许选项 | An option permitted by the schema. | 结构定义允许出现的选项。 |
| allowed options | 允许的选项集合 | The set of options permitted in a result. | 结果可以选择的一组规定选项。 |
| option | 选项 | One permitted choice among possible values. | 可以选择的一个值或答案。 |
| constraint | 约束 | A rule limiting the allowed result shape or values. | 限制结果结构或取值的规则。 |
| requirement | 要求 | A condition the requested result should satisfy. | 结果需要满足的条件。 |
| schema rule | 模式规则 | A rule describing valid fields, types, or values. | 规定字段、类型或取值是否合法的规则。 |
| validation | 验证；校验 | Checking whether a result follows the required structure. | 检查结果是否符合规定结构。 |
| schema validation | 模式验证 | Checking a result against a schema. | 按结构定义检查结果。 |
| structure validation | 结构验证 | Checking whether the data arrangement is valid. | 检查数据组织方式是否正确。 |
| validate | 验证；校验 | To check whether a result meets structural rules. | 检查结果有没有符合规则。 |
| validated result | 已验证结果 | A result that has passed structural checks. | 已经通过结构检查的结果。 |
| validated contact object | 已验证的联系人对象 | A contact object whose structure has been checked. | 结构已经检查过的联系人资料对象。 |
| check the structure | 检查结构 | Verify the organization and types of a result. | 检查结果的组织方式和类型。 |
| check types | 检查类型 | Verify that values have the required data types. | 检查值是不是规定的数据类型。 |
| check required values | 检查必填值 | Verify that required content is present. | 检查必须填写的内容有没有出现。 |
| reliably | 可靠地 | In a way that software can depend on more consistently. | 让软件更稳定、更放心地使用。 |
| reliable use | 可靠使用 | Using a result after relevant checks make it dependable. | 经过检查后较可靠地使用结果。 |
| machine-readable structure | 机器可读结构 | A data structure software can parse and process. | 软件可以直接读取和处理的结构。 |
| machine-readable | 机器可读的 | Organized so a computer can read it consistently. | 按电脑容易识别的方式组织。 |
| plain text | 纯文本 | Text without a required machine-readable data structure. | 没有规定机器结构的普通文字。 |
| plain-text response | 纯文本回应 | A response returned as ordinary text. | 以普通文字形式返回的回答。 |
| unstructured response | 非结构化回应 | A response without a required data shape. | 没有固定数据结构的回答。 |
| structured data | 结构化数据 | Data organized into defined fields and types. | 按字段和类型整理好的数据。 |
| unstructured data | 非结构化数据 | Data without a required predefined organization. | 没有预先固定组织方式的数据。 |
| software | 软件 | An application that can validate or use a result. | 可以检查和使用结果的程序。 |
| application | 应用程序；应用 | A program that validates and uses model output. | 接收模型结果并继续处理的程序。 |
| system | 系统 | The software or workflow that requests and checks a result. | 发出请求、检查结果并继续工作的系统。 |
| AI / System | AI／系统 | The model and surrounding software acting together. | AI 模型和外围软件一起完成的工作。 |
| model | 模型 | A learned system that produces a response. | 根据输入生成结果的学习系统。 |
| AI | 人工智能 | Systems that perform tasks associated with human intelligence. | 能完成一些通常需要人来做的智能任务的系统。 |
| artificial intelligence | 人工智能 | The broader field of systems that perform intelligent tasks. | 研究和构建智能系统的领域。 |
| model output | 模型输出 | The result returned by a model. | 模型返回的结果。 |
| output | 输出 | Information produced by a model or system. | 模型或系统产出的信息。 |
| input | 输入 | Information supplied to a model or system. | 送进模型或系统的信息。 |
| user request | 用户请求 | A task or instruction supplied by a user. | 用户要求系统完成的事情。 |
| request | 请求 | An instruction asking a model to produce a result. | 请模型做事并返回结果的要求。 |
| task | 任务 | The job the model is asked to perform. | 模型被要求完成的工作。 |
| send the task | 发送任务 | Send the requested work to the model. | 把任务交给模型处理。 |
| model request | 模型请求 | A request sent to a model for a response. | 发给模型、要求它回答的请求。 |
| response request | 回应请求 | A request asking for a particular response. | 要求系统返回特定回答的请求。 |
| request the defined shape | 请求定义好的形状 | Ask the model to return the specified structure. | 要模型按照规定的结构返回。 |
| ask the model | 请求模型 | Give the model an instruction to perform a task. | 告诉模型要做什么。 |
| return the defined shape | 返回定义好的形状 | Produce the response in the requested structure. | 按指定结构把结果返回。 |
| generate | 生成 | Produce a response or structured result. | 产出一个回答或结构化结果。 |
| generation | 生成过程 | The process of producing the model result. | 模型产出结果的过程。 |
| generate the result | 生成结果 | Create the requested response. | 产生被要求的结果。 |
| create the result | 创建结果 | Produce the output that fills the requested shape. | 生成填入规定结构的输出。 |
| fill the fields | 填充字段 | Put values into the fields of a schema. | 把内容填进结构定义的字段。 |
| field filling | 字段填充 | Supplying values for the requested fields. | 为每个规定字段提供内容。 |
| handle | 处理 | Decide what the system should do with the result or failure. | 决定如何处理结果或失败。 |
| continue | 继续处理 | Proceed with the workflow after a usable result. | 结果可用后继续后面的流程。 |
| recover | 恢复；补救 | Take corrective action after a problem. | 出现问题后采取措施补救。 |
| continue or recover | 继续或恢复 | Use a valid result or respond to a failure. | 结果能用就继续，失败就补救。 |
| validation failure | 验证失败 | A result that does not pass the required checks. | 结果没有通过规定检查。 |
| failure | 失败 | A condition in which the requested result cannot be used as expected. | 结果没有达到可用要求的情况。 |
| error | 错误；报错 | An indication that the result or operation did not succeed. | 结果或操作没有成功的提示。 |
| handle a validation failure | 处理验证失败 | Recover or take another action when validation fails. | 校验失败时补救或采取其他处理。 |
| workflow | 工作流程 | The ordered series of actions from request to use. | 从请求到使用结果的一连串步骤。 |
| process | 流程；过程 | An ordered way of completing the structured-output task. | 完成结构化输出任务的步骤。 |
| process flow | 流程图；流程 | The ordered sequence of stages in the workflow. | 按顺序排列的工作阶段。 |
| workflow stage | 工作阶段 | One part of the end-to-end process. | 整个流程中的一个阶段。 |
| process node | 流程节点 | One named action in the process. | 流程中一个明确的动作节点。 |
| step | 步骤 | One action in an ordered process. | 流程中的一步。 |
| five-step process | 五步流程 | The page's sequence of define, request, generate, validate, and handle. | 页面列出的定义、请求、生成、验证、处理五步。 |
| 1 · Define | 1·定义 | The first process stage: specify the schema. | 第一步：先规定结构。 |
| Define | 定义 | Specify the response schema before requesting the result. | 先写清楚结果的结构。 |
| write the schema | 编写模式 | Create the schema that describes the result. | 写出描述结果的结构定义。 |
| schema specification | 模式规格说明 | The written description of fields, types, and requirements. | 写下字段、类型和要求的规格。 |
| specify fields | 指定字段 | List the fields the response should contain. | 列出回答要包含哪些字段。 |
| specify types | 指定类型 | State the type allowed for each value. | 说明每个值允许是什么类型。 |
| specify requirements | 指定要求 | State the conditions the response must satisfy. | 说明回答必须满足的条件。 |
| 2 · Request | 2·请求 | The second process stage: send the task. | 第二步：把任务和结构要求交给模型。 |
| Request | 请求 | Ask the model to return the defined shape. | 请求模型按照规定结构回答。 |
| 3 · Generate | 3·生成 | The third process stage: create the result. | 第三步：模型产生结果。 |
| Generate | 生成 | Have the model fill the fields in the result. | 让模型把字段内容生成出来。 |
| 4 · Validate | 4·验证 | The fourth process stage: check the structure. | 第四步：检查结构是否正确。 |
| Validate | 验证 | Check types and required values in the result. | 检查类型和必填值。 |
| system checks | 系统检查 | The surrounding software verifies the response. | 外围系统检查模型回答。 |
| 5 · Handle | 5·处理 | The fifth process stage: use the result or recover. | 第五步：使用结果或处理失败。 |
| Handle | 处理 | Use a valid result or handle a validation failure. | 结果可用就继续，否则进行补救。 |
| result lifecycle | 结果生命周期 | The path from defining a schema to handling the result. | 从定义结构到处理结果的完整路径。 |
| application action | 应用动作 | What the application does after receiving the result. | 应用拿到结果后执行的动作。 |
| schema validation → application action | 模式验证→应用动作 | A related-concepts link from checking the result to acting on it. | 先检查结果，再让应用执行后续动作。 |
| User request → Model response | 用户请求→模型回应 | The first part of the related-concepts chain. | 用户提出要求，模型返回回答。 |
| Model response → Schema validation | 模型回应→模式验证 | Passing the model result into structural checking. | 把模型回答交给结构检查。 |
| Schema validation | 模式验证 | Checking the model response against the requested schema. | 按规定模式检查模型回答。 |
| Application action | 应用动作 | The next software operation based on the validated result. | 应用根据已检查结果进行的下一步操作。 |
| contact card | 联系人卡片 | A structured record containing a person's contact details. | 保存一个人联系方式的资料卡。 |
| contact-card example | 联系人卡片例子 | The everyday example used to show extraction into fields. | 页面用来说明字段提取的日常例子。 |
| everyday example | 日常例子 | The contact-card example in the page. | 页面中的联系人卡片例子。 |
| message | 消息；讯息 | Text containing information about a person. | 包含某人资料的一段文字。 |
| person's details | 某人的资料 | Information about a person in a message. | 消息里关于某个人的信息。 |
| contact details | 联系方式 | Information such as a name, email, and phone number. | 姓名、邮箱、电话等联系资料。 |
| extract | 提取 | Find and return selected information from an input. | 从输入中找出需要的信息。 |
| extracts name | 提取姓名 | Pull the person's name into a field. | 把人的姓名提取出来。 |
| name | 姓名 | A person's identifying name field. | 表示某个人姓名的字段。 |
| email | 电子邮箱 | An electronic mail address field. | 电子邮件地址字段。 |
| phone | 电话 | A telephone contact field. | 电话号码字段。 |
| phone field | 电话字段 | A field containing a phone number. | 存放电话号码的字段。 |
| email field | 邮箱字段 | A field containing an email address. | 存放电子邮箱地址的字段。 |
| contact object | 联系人对象 | A software-readable object representing contact information. | 用软件可读结构表示的联系人资料。 |
| object | 对象 | A structured software value containing named fields. | 包含多个命名字段的软件数据。 |
| validated contact object | 已验证联系人对象 | A contact object checked for required fields and types. | 已检查字段和类型的联系人对象。 |
| invoice extraction | 发票提取 | Extracting structured fields from an invoice document. | 从发票文件里提取结构化字段。 |
| invoice-extraction example | 发票提取例子 | The business example used to show structured finance data. | 页面用来说明财务资料结构化的商业例子。 |
| business example | 商业例子 | The invoice-extraction example in the page. | 页面中的发票提取例子。 |
| invoice | 发票 | A business document containing billing information. | 记录开票和账务信息的商业文件。 |
| invoice document | 发票文件 | A document that contains invoice information. | 包含发票内容的文件。 |
| document | 文档；文件 | A source document supplied as input. | 交给系统处理的一份文件。 |
| finance system | 财务系统 | A system that requires particular invoice fields. | 需要特定发票字段的财务软件系统。 |
| fields required by the finance system | 财务系统要求的字段 | Fields needed by the downstream finance application. | 后续财务系统必须收到的字段。 |
| structured invoice data | 结构化发票数据 | Invoice information returned in defined fields. | 按规定字段返回的发票资料。 |
| error output | 错误输出 | An error returned instead of usable structured data. | 没有得到可用结构化数据时返回的错误。 |
| return structured invoice data or an error | 返回结构化发票数据或错误 | The possible output of invoice extraction. | 发票处理可能返回结构化资料，也可能返回错误。 |
| accurate value | 准确值 | A value that correctly represents the input. | 真正符合输入事实的值。 |
| accuracy | 准确性 | Whether the returned values are correct. | 结果里的内容到底对不对。 |
| guaranteed accuracy | 保证准确性 | A claim that the result's values are necessarily correct. | 认为结构化结果里的值一定正确。 |
| value correctness | 值的正确性 | Whether individual values match reality or the source. | 每个值是否和事实或原文一致。 |
| shape and types | 结构和类型 | The form and data types checked by structured output. | 结构化输出检查的形状与数据类型。 |
| structural correctness | 结构正确性 | Whether fields and types follow the schema. | 字段和类型是否遵守结构定义。 |
| semantic correctness | 语义正确性 | Whether the values mean or state the right thing. | 内容含义和事实是否正确。 |
| database storage | 数据库存储 | Saving a result in a database. | 把结果保存到数据库里的动作。 |
| database | 数据库 | A system for storing and retrieving application data. | 保存和读取应用数据的系统。 |
| storage | 存储 | Keeping data for later use. | 把数据保存下来以后再用。 |
| persist | 持久化保存 | Store a result beyond the current response. | 把结果长期保存，不只停留在当前回答。 |
| model result | 模型结果 | The result returned by the model before application storage. | 模型先返回、应用之后可能保存的结果。 |
| returned by the model | 由模型返回 | Produced as the model's response. | 由模型直接产出的意思。 |
| used by an application | 由应用使用 | Consumed or processed by software. | 被应用程序接收并继续处理。 |
| stored by an application | 由应用存储 | Saved by software after receiving the result. | 应用拿到结果后把它保存起来。 |
| model output vs database storage | 模型输出与数据库存储 | A returned result is different from later persistence. | 模型输出不是数据库保存，后者是应用后续动作。 |
| structured output vs plain text | 结构化输出与纯文本 | Defined machine-readable shape versus no required structure. | 一个有固定结构，一个只是普通文字。 |
| structured output vs guaranteed accuracy | 结构化输出与保证准确性 | Shape checking versus correctness of values. | 检查格式不等于保证内容事实正确。 |
| structured output vs database storage | 结构化输出与数据库存储 | A model result versus an application's storage action. | 模型返回结果不等于应用把它存进数据库。 |
| plain text comparison | 纯文本对比 | The comparison between defined structure and ordinary text. | 用普通文字来对比结构化结果。 |
| correctness check | 正确性检查 | Checking whether values are actually right. | 检查内容本身是否正确。 |
| structural check | 结构检查 | Checking fields, types, and required values. | 检查字段、类型和必填值。 |
| downstream system | 下游系统 | A later application that consumes the result. | 接着使用结果的后续系统。 |
| data extraction | 数据提取 | Pulling selected information into fields. | 把需要的信息抽取出来放进字段。 |
| information extraction | 信息抽取 | Extracting named information from text or documents. | 从文字或文件中提取指定信息。 |
| contact extraction | 联系人信息提取 | Extracting name, email, and phone information. | 提取姓名、邮箱和电话等联系人资料。 |
| invoice field extraction | 发票字段提取 | Extracting fields required for invoice processing. | 提取处理发票所需的字段。 |
| structured representation | 结构化表示 | A defined representation of information. | 用固定字段和类型表示信息。 |
| data object | 数据对象 | A software object representing structured data. | 表示结构化资料的软件对象。 |
| schema-driven response | 模式驱动回应 | A response generated according to a schema. | 按结构定义生成的回答。 |
| schema-constrained generation | 模式约束生成 | Generation constrained by an expected schema. | 生成时受到结构定义约束。 |
| constrained output | 受约束输出 | Output limited to required fields, types, or options. | 被字段、类型或选项规则限制的输出。 |
| output contract | 输出契约 | An agreed shape that a model result should satisfy. | 模型和应用约定好的结果格式。 |
| interface contract | 接口契约 | A shared agreement about data passed between components. | 不同软件组件之间约定的数据格式。 |
| API response shape | API 回应结构 | The expected structure of data returned by an API. | API 返回资料应该遵守的结构。 |
| JSON-like object | 类 JSON 对象 | A machine-readable object with named fields. | 类似 JSON、由字段组成的软件数据。 |
| JSON | JSON | A common machine-readable format for structured data. | 软件常用的一种结构化数据格式。 |
| type checking | 类型检查 | Verifying that values use the expected types. | 确认值有没有使用规定类型。 |
| required-value checking | 必填值检查 | Verifying that required values are present. | 确认必填内容有没有提供。 |
| option checking | 选项检查 | Verifying that a value is among allowed options. | 确认值是否属于允许选项。 |
| parseable result | 可解析结果 | A result software can read into data fields. | 软件可以拆解读取的结果。 |
| reliable integration | 可靠集成 | Connecting model output to software with dependable structure. | 让模型结果更稳定地接入软件系统。 |
| application integration | 应用集成 | Connecting the model result to an application workflow. | 把模型结果接到应用流程中。 |
| automation | 自动化 | Letting software continue work from a structured result. | 应用拿到结构化结果后自动做后续工作。 |
| downstream action | 下游动作 | An action taken after the result is validated. | 结果检查后由后续系统执行的动作。 |
| recovery path | 恢复路径 | The handling route taken after a validation failure. | 校验失败后采取的补救路线。 |
| fallback | 备用处理 | An alternative action when the requested result is unusable. | 结果不能用时采取的替代办法。 |
| retry | 重试 | Request the result again after a failure. | 失败后再请求一次。 |
| rejection | 拒绝；不接受 | Declining a result that violates the schema. | 结果不符合规则时不接受它。 |
| error handling | 错误处理 | Managing errors during structured result production or validation. | 生成或检查结果出错时的处理方式。 |
| reliability | 可靠性 | The degree to which a system can consistently provide usable results. | 系统持续提供可用结果的程度。 |
| format compliance | 格式遵从 | Whether a result follows the requested format. | 结果有没有遵守规定格式。 |
| schema compliance | 模式遵从 | Whether a result follows the schema. | 结果有没有遵守结构定义。 |
| data contract compliance | 数据契约遵从 | Whether returned data satisfies an agreed contract. | 返回数据有没有符合双方约定。 |
| output quality | 输出质量 | The overall usefulness and correctness of a result. | 输出结果整体好不好用、对不对。 |
| data quality | 数据质量 | The quality of the values contained in the result. | 结果里数据内容本身的好坏。 |
| content quality | 内容质量 | Whether the result's content is useful and correct. | 回答内容是否有用、准确。 |
| validation layer | 验证层 | The part of a system that checks model output. | 专门检查模型结果的系统层。 |
| application layer | 应用层 | The part of a system that uses the result. | 接收结果并执行业务动作的系统层。 |
| model layer | 模型层 | The part that generates the response. | 负责生成回答的模型部分。 |
| input document | 输入文档 | A document provided to the model or extraction workflow. | 交给模型处理的文件。 |
| contact information | 联系人信息 | Personal contact details represented in fields. | 用字段表示的联系人资料。 |
| finance data | 财务数据 | Financial information returned for a finance system. | 交给财务系统使用的资料。 |
| field extraction pipeline | 字段提取流程 | A workflow that extracts, validates, and uses fields. | 提取字段、检查字段并继续使用的流程。 |
| model-assisted extraction | 模型辅助提取 | Using a model to extract fields from input. | 用模型帮忙从资料中提取字段。 |
| API integration | API 集成 | Connecting a model response to another software interface. | 通过接口把模型回答接到其他软件。 |
| structured response contract | 结构化回应契约 | An agreed schema for a model response. | 约定模型回答要遵守的结构。 |
| response parser | 回应解析器 | Software that reads a structured response. | 把回答拆解成软件字段的程序。 |
| parser | 解析器 | A component that converts formatted data into usable values. | 把格式化数据读成可使用值的程序。 |
| schema parser | 模式解析器 | A component that reads data according to a schema. | 按结构定义读取结果的程序。 |
| validation result | 验证结果 | The outcome of checking whether output is valid. | 检查结果后得到的通过或失败状态。 |
| valid result | 有效结果 | A result that meets the defined structural rules. | 符合规定结构、可以继续处理的结果。 |
| invalid result | 无效结果 | A result that violates one or more structural rules. | 违反结构规则、不能直接使用的结果。 |
| valid schema | 有效模式 | A schema that defines a usable response contract. | 能清楚规定结果的结构。 |
| result handling | 结果处理 | Using, rejecting, retrying, or recovering from a result. | 对结果进行使用、拒绝、重试或补救。 |
| human-readable text | 人类可读文字 | Text intended for people rather than direct parsing. | 主要给人看、不一定方便程序解析的文字。 |
| machine-readable data | 机器可读数据 | Data arranged for software processing. | 按软件处理方式整理的数据。 |
| semantic extraction | 语义提取 | Extracting information based on meaning. | 根据内容含义提取信息。 |
| format error | 格式错误 | An output that does not use the required format. | 输出没有采用规定的格式。 |
| type error | 类型错误 | A value that has the wrong type for its field. | 某字段里的值类型不对。 |
| missing required value | 缺少必填值 | A required value is absent from the result. | 结果漏掉了必须提供的内容。 |
| invalid option | 无效选项 | A value not included among allowed options. | 返回了规定选项之外的值。 |
| schema mismatch | 模式不匹配 | A result's structure differs from the schema. | 返回结构和规定结构对不上。 |
| output mismatch | 输出不匹配 | The returned result does not match the request. | 返回结果没有符合请求。 |
| response reliability | 回应可靠性 | How consistently responses have a usable defined structure. | 回答持续符合可用结构的程度。 |
| structured-output workflow | 结构化输出工作流 | The full define-to-handle process for structured responses. | 从定义到处理结构化回答的完整流程。 |
| structured-output system | 结构化输出系统 | A system that requests, validates, and uses structured results. | 会请求、检查并使用结构化结果的系统。 |
| structured-output feature | 结构化输出功能 | A capability that makes model responses follow a schema. | 让模型回答遵守结构定义的功能。 |
| schema-based output | 基于模式的输出 | Output organized according to a schema. | 按模式规定组织的输出。 |
| format-based output | 基于格式的输出 | Output organized according to a defined format. | 按规定格式组织的输出。 |
| schema field | 模式字段 | A field declared in a schema. | 在结构定义里声明的字段。 |
| schema type | 模式类型 | A type declared for a schema field. | 结构定义为字段声明的数据类型。 |
| schema option | 模式选项 | An allowed option declared by a schema. | 结构定义声明的允许选项。 |
| schema requirement | 模式要求 | A requirement declared by a schema. | 结构定义声明的必须满足的条件。 |
| defined data contract | 定义好的数据契约 | A specified agreement about returned data. | 事先约定好的返回资料规则。 |
| application-readable result | 应用可读结果 | A result an application can reliably parse and use. | 应用可以稳定读取和使用的结果。 |
| real-world example | 现实例子 | An example showing a practical workflow. | 说明实际应用方式的例子。 |
| related concept | 相关概念 | A concept connected to structured outputs. | 和结构化输出有关的概念。 |
| next concept | 下一个概念 | A related topic suggested for further exploration. | 页面建议接着了解的相关主题。 |
| independent explainer | 独立讲解 | A separate visual explanation associated with the topic. | 配套主题的独立视频讲解。 |
| visual explainer | 可视化讲解 | An explanation presented through visual media. | 通过视频等视觉方式讲解。 |
| video | 视频 | The visual explainer section associated with the topic. | 页面附带的视觉讲解内容。 |
| System Prompts | 系统提示词 | Instructions that guide model behavior at the system level. | 在系统层面指导模型行为的指令。 |
| system prompt | 系统提示词 | A high-priority instruction supplied to a model. | 优先级较高、用来指导模型的提示。 |
| Failure Handling | 失败处理 | The practice of responding to unsuccessful operations. | 系统出错或失败时如何应对。 |
| failure handling | 失败处理 | Managing an unusable result or failed validation. | 处理不能使用的结果或验证失败。 |
| Tool Calling | 工具调用 | Having a model request an external tool or function. | 让模型请求调用外部工具或函数。 |
| tool calling | 工具调用 | A model-to-tool interaction pattern. | 模型和工具之间的一种交互方式。 |
| LLM | 大型语言模型 | Abbreviation for large language model. | large language model 的缩写。 |
| large language model | 大型语言模型 | A model designed to process and generate language. | 处理和生成语言的大模型。 |
| LLM response | 大型语言模型回应 | A response generated by an LLM. | 大型语言模型生成的回答。 |
| schema validation vs application action | 模式验证与应用动作 | Checking the result is different from acting on it. | 检查结果和根据结果做事是两件事。 |
| structured output vs plain text response | 结构化输出与纯文本回答 | One follows required structure; the other has no required machine structure. | 一个遵守固定结构，另一个只是普通文字。 |
| structure vs content | 结构与内容 | The shape of a result is different from whether its values are correct. | 结果长什么样，和里面说得对不对不同。 |
| schema validation vs accuracy | 模式验证与准确性 | Structural validation does not establish factual correctness. | 通过结构检查不代表内容事实正确。 |
| model response vs database record | 模型回应与数据库记录 | A returned response is not automatically a stored database record. | 模型回答不会自动变成数据库记录。 |

## Potential Missing Concepts

- JSON, JSON Schema, XML, YAML, CSV, and other concrete serialization formats are not named.
- The page says “schema” but does not explain schema syntax, schema languages, versioning, nesting, arrays, objects, nullability, enums, unions, or recursive structures.
- It names fields and types but does not list common primitive types such as string, number, integer, boolean, and null.
- It mentions required values and allowed options but does not explain optional fields, default values, minimum/maximum constraints, pattern constraints, or enum validation.
- It says the application can validate the result but does not describe parser behavior, validation libraries, error messages, retry policy, fallback policy, repair, or human escalation.
- It does not distinguish provider-enforced constrained decoding from prompt-only formatting instructions.
- It does not explain constrained decoding, grammar-constrained generation, finite-state constraints, token masking, or decoder-time enforcement.
- It does not explain whether validation happens client-side, server-side, at the API boundary, or in a downstream service.
- It does not discuss refusals, truncated output, malformed JSON, partial output, timeouts, rate limits, or transport failures.
- It gives a contact-card extraction example but does not discuss source spans, provenance, confidence, uncertainty, or evidence for extracted values.
- It gives an invoice example but does not define OCR, document parsing, table extraction, currency normalization, dates, totals, tax, line items, or accounting validation.
- It contrasts structure with accuracy but does not explain semantic validation, factuality, grounding, business-rule validation, or human review.
- It does not explain data contracts, API contracts, interface compatibility, backward compatibility, or schema migration.
- It does not discuss nested objects, arrays of objects, multiple output formats, discriminated unions, or polymorphic responses.
- It does not define tool calling arguments, function calling, action schemas, or the relationship between structured outputs and tool invocation.
- It links System Prompts, Failure Handling, Tool Calling, and LLM but does not explain their interfaces or boundaries in detail.
- It does not give quantitative metrics such as schema-validity rate, parse success rate, field-completeness rate, extraction accuracy, exact match, precision, recall, latency, token cost, or retry rate.
- It does not discuss reliability under adversarial input, prompt injection, ambiguous source documents, out-of-distribution inputs, or conflicting instructions.
- It does not cover security concerns such as unsafe field values, injection through extracted strings, data exfiltration, or validation bypass.
- It does not discuss privacy, retention, access controls, PII handling, or sensitive invoice/contact data.
- It does not distinguish model-generated values from source-grounded values or explain how an application should treat uncertain fields.
- It does not describe testing strategies such as unit tests, contract tests, golden datasets, property-based tests, fuzzing, regression tests, or end-to-end tests.
- It does not discuss observability, logging, tracing, monitoring, dashboards, alert thresholds, or production drift.
- It does not explain how structured outputs behave across different models, providers, SDKs, API versions, or capability levels.
- It does not describe streaming structured output, incremental parsing, or partial validation.
- It does not explain the difference between a typed programming-language object and a serialized structured response.
- It does not discuss database schema design, normalization, transactions, or safe persistence after a model response.
- It does not define idempotency, deduplication, record matching, or update semantics for application actions triggered by output.
- It does not cover multilingual extraction, locale-specific names, phone formats, currencies, date formats, or international addresses.
- It does not provide a concrete API request/response example or a runnable schema.

## Aliases / Synonyms

- Structured Outputs / Structured output / structured outputs / schema-constrained output / constrained output
- Structured response / structured model response / structured AI response / schema-based response / schema-driven response
- Defined data shape / defined shape / response shape / output shape / data structure / response structure
- Schema / defined schema / response schema / output schema / data schema / schema definition / schema specification
- Format / defined format / response format / output format / data format / serialization format
- Field / fields / schema field / output field / response field / named field / data field
- Required value / required values / required field / mandatory field / non-optional field
- Allowed option / allowed options / permitted option / valid option / enum value / allowed value
- Type / data type / field type / value type / type constraint
- Requirement / schema requirement / output requirement / response requirement / constraint / rule
- Validation / schema validation / structure validation / output validation / response validation / type checking
- Validate / check the structure / check types / check required values / verify the schema
- Valid result / validated result / schema-valid output / compliant response / parseable response
- Invalid result / validation failure / schema mismatch / format error / malformed output / non-compliant response
- Machine-readable / machine-readable structure / machine-readable data / software-readable / parseable
- Plain text / plain-text response / free-form text / unstructured text / ordinary text
- Model response / AI response / model output / AI output / generated response / generated result
- Result / output / response / returned data / generated data / model result
- Input / request input / source input / input message / input document
- Task / request / user request / model request / instruction / prompt (related runtime instruction)
- Generate / generation / create the result / produce the result / return the result
- Fill the fields / populate fields / supply field values / complete the schema / instantiate the object
- Handle / result handling / output handling / response handling / error handling / failure handling
- Continue or recover / proceed or retry / use or recover / success path or failure path / fallback path
- Error / failure / validation failure / format failure / invalid response
- Contact card / contact object / contact record / contact information object / person record
- Person's details / contact details / personal details / contact information
- Name / name field / person's name / contact name
- Email / email field / email address / electronic mail address
- Phone / phone field / phone number / telephone number
- Invoice extraction / invoice field extraction / invoice parsing / invoice information extraction / document extraction
- Invoice data / structured invoice data / finance data / billing data / accounting data
- Document / invoice document / source document / input document / business document
- Accuracy / value correctness / factual correctness / semantic correctness / extraction accuracy
- Database storage / persistence / data storage / record storage / application persistence
- Database / datastore / storage system / persistence layer
- Application / software / downstream system / consuming system / client application
- System / application system / surrounding software / orchestration layer / validation layer
- User request → Model response → Schema validation → Application action / request-to-action flow / structured-output lifecycle
- System Prompts / system prompt / system-level instruction / high-priority instruction
- Failure Handling / failure handling / error handling / recovery handling / exception handling
- Tool Calling / tool calling / function calling / external-tool invocation / action calling
- LLM / large language model / large-language model / language model
- JSON-like object / object / contact object / structured object / typed object
- Output contract / response contract / data contract / interface contract / API contract
- Schema compliance / format compliance / contract compliance / structural compliance

## Do Not Confuse Candidates

- Structured output ≠ plain text: structured output follows a defined data shape; plain text has no required machine-readable structure.
- Structured output ≠ unstructured output: a structured response has declared fields or rules, while an unstructured response does not.
- Structured output ≠ guaranteed accuracy: validation checks shape and types, not whether the values are factually correct.
- Schema validation ≠ semantic validation: schema validation checks form, while semantic validation checks meaning, truth, or business validity.
- Type correctness ≠ value correctness: a value can have the right type and still be wrong.
- Required value ≠ accurate value: presence does not prove correctness.
- Allowed option ≠ true answer: an option can be permitted by the schema without being the right answer for the input.
- Schema ≠ format: a schema describes rules and meaning; a format describes representation, although the terms overlap in beginner usage.
- Field ≠ field value: the field is the named slot; the field value is what is placed in it.
- Field type ≠ field value: the type describes what kind of value is allowed; the value is the actual content.
- Input ≠ output: input is supplied to the model; output is produced by it.
- User request ≠ model response: the request asks for work; the response is the returned result.
- Model response ≠ application action: the model returns data; the application may act on it afterward.
- Model output ≠ database storage: output is returned by the model; storage is a later application operation.
- Contact object ≠ contact card: a contact card is the user-facing example; a contact object is the software-readable representation.
- Contact details ≠ contact object: details are the information; the object is the structured container for that information.
- Invoice document ≠ structured invoice data: the document is the source input; structured invoice data is the extracted result.
- Data extraction ≠ validation: extraction finds values; validation checks whether the result follows rules.
- Extraction ≠ accuracy: extracting a value does not prove it was extracted correctly.
- Generated result ≠ validated result: generation creates an answer; validation checks whether it can be accepted.
- Valid result ≠ correct result: a result can be structurally valid but factually or semantically wrong.
- Validation failure ≠ model failure: a schema check can fail even when the model returned text; a model can also fail before producing a result.
- Error ≠ invalid value: an error may describe a failed operation; an invalid value is content that violates a rule.
- Recover ≠ continue: recovery responds to a problem; continuing proceeds with a usable result.
- Retry ≠ repair: retry requests another result; repair modifies or fixes an existing result.
- Schema compliance ≠ business-rule compliance: matching fields and types does not guarantee that an invoice total or business condition is valid.
- Machine-readable ≠ human-readable: software parsing and human understanding are different properties.
- JSON ≠ structured outputs: JSON is one possible representation; structured outputs are the broader response-shaping concept.
- Object ≠ database record: an object may exist only in memory or in a response; a record is persisted database data.
- Database storage ≠ schema validation: storage saves data; validation checks data before or during use.
- Application ≠ model: the model generates; the application orchestrates, validates, stores, or acts.
- AI ≠ LLM: AI is the broad field; an LLM is one kind of AI model.
- LLM ≠ structured output: an LLM is the generating model; structured output is a response format or constraint.
- System prompt ≠ output schema: a system prompt is an instruction; a schema defines data shape and validation rules.
- Prompting ≠ schema enforcement: asking for JSON in a prompt may not guarantee valid structured output.
- Tool calling ≠ structured outputs: tool arguments often use structured data, but structured output can be returned without invoking a tool.
- Failure handling ≠ validation: validation detects a problem; failure handling decides what to do next.
- Serialization format ≠ data contract: serialization says how data is represented; a contract says what data and rules are expected.
- Required field ≠ only field: required fields must appear, but a schema may also allow optional fields.
- Allowed options ≠ unlimited free text: an enumerated set restricts values to declared choices.
- Defined shape ≠ fixed factual answer: a schema fixes organization, not the truth of the content.
- Reliable use ≠ guaranteed correctness: checks improve dependable software handling but do not make every value correct.
- Schema validation → application action ≠ automatic action: the system may still need policy, authorization, safety checks, or business validation.
- Structured response contract ≠ database schema: one governs an exchanged response; the other governs persisted data.
- Application action ≠ model generation: an action can create an external side effect, while generation only produces model output.
- Contact-card extraction ≠ invoice extraction: both extract fields, but their source documents and field requirements differ.
- Field extraction ≠ summarization: extraction returns defined fields; summarization produces a condensed free-form account.
- Structured output ≠ database storage ≠ plain text: these describe response shape, persistence, and unstructured representation respectively.

## Notes

- The source page was read in full, including the document title and description, page navigation, definition, analogy, five process steps, contact-card example, invoice-extraction example, three “What it is NOT” comparisons, related-concepts chain, takeaway, and video section.
- The page's direct definition is that a structured output is a model response following a defined schema or format.
- Directly named structural elements include fields, types, required values, allowed options, data shape, schema, format, validation, and machine-readable structure.
- Directly named workflow nodes are Define, Request, Generate, Validate, and Handle; their action phrases are write the schema, send the task, create the result, check the structure, and continue or recover.
- Directly named example entities include message, person's details, name, email, phone fields, contact object, invoice document, finance system, structured invoice data, and error.
- Directly named comparison concepts include plain text, guaranteed accuracy, accuracy, database storage, application, and result returned by the model.
- Directly named neighboring concepts are User request, Model response, Schema validation, Application action, System Prompts, Failure Handling, Tool Calling, and LLM.
- The word “AI” is present in the page's lede and “AI / System” example label; “LLM” is a related-concept link rather than a definition in the body.
- Candidate rows intentionally retain capitalization variants, singular/plural variants, repeated wording, process labels, explanatory phrases, adjacent implementation concepts, and beginner-facing language.
- Some candidates such as JSON, constrained decoding, parser libraries, extraction metrics, and business-rule validation are not stated by the source. They are retained as follow-up candidates only where relevant and are explicitly marked under Potential Missing Concepts.
- “Structured output” concerns the shape and machine usability of a response; it does not by itself establish factual accuracy, semantic correctness, safe content, successful persistence, or an external application action.
- No website files, source HTML, video assets, GitHub state, or other project files were modified.
