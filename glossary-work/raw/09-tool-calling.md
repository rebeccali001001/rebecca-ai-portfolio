# Topic

Tool Calling

## Topic Metadata

- Module: 06 · Agents, Tools & MCP
- Topic: Tool Calling
- Topic Number: 03
- Source Page Context: 06 · Agents, Tools & MCP · Topic 03 (as shown in the HTML)
- Source File: `tool-calling.html`
- Source Title: What is Tool Calling?
- Source Description: Tool calling lets an AI application ask an external function or service to perform a defined action.
- Raw-stage policy: Maximum candidate inventory; retain overlapping, repeated, surface-form, alias, and potentially confusable candidates for later normalization.

## Glossary Candidates

| English Term | 中文 | Simple English | 中文小白理解 |
|---|---|---|---|
| Tool Calling | 工具调用 | A structured way for an AI application to ask an external function or service to perform an action. | 让 AI 应用按照规定格式请求外部工具做一件事。 |
| Tool calling | 工具调用 | The process of requesting a tool through a model and application. | 模型和应用一起请求工具执行任务的过程。 |
| tool calling | 工具调用 | Lowercase wording for tool calling. | “Tool Calling”的小写写法。 |
| tool-calling | 工具调用（连字符写法） | Hyphenated wording for the tool-calling capability. | 用连字符写的“工具调用”。 |
| tool call | 工具调用；工具请求 | One request to use a tool. | 一次使用工具的请求。 |
| call | 调用；调用请求 | A request that asks a tool or service to do something. | 请工具或服务做事的一次调用。 |
| tool | 工具 | A defined function or service that an application can invoke. | 应用可以调用的、事先定义好的功能或服务。 |
| external tool | 外部工具 | A tool outside the model itself. | 不属于模型本身、由外部系统提供的工具。 |
| AI application | AI 应用 | An application that uses AI and can ask an external service to act. | 使用 AI、也能请求外部服务办事的应用程序。 |
| AI / System | AI／系统 | The AI model and surrounding application working together. | AI 模型和外围应用一起工作的整体。 |
| application | 应用程序；应用 | Software that defines, validates, authorizes, and executes tool calls. | 负责定义、检查、授权和执行工具调用的软件。 |
| system | 系统 | Software or infrastructure that checks and performs the requested action. | 检查请求并执行动作的软件或基础设施。 |
| separate system | 独立系统 | A system separate from the model that checks and performs the request. | 和模型分开的、负责检查和执行请求的系统。 |
| external function | 外部函数 | A function outside the model that can perform a defined action. | 模型之外、可以执行规定动作的函数。 |
| external service | 外部服务 | A service outside the model that can perform a requested action. | 模型之外、可以完成请求动作的服务。 |
| external function or service | 外部函数或服务 | Either an outside function or an outside service used by the application. | 应用可以使用的外部函数或外部服务。 |
| external system | 外部系统 | A system outside the model that owns or performs the action. | 模型之外、真正拥有或执行动作的系统。 |
| defined action | 定义好的动作 | An action described and bounded by the application. | 应用事先规定好的、范围明确的动作。 |
| action | 动作；行动 | The operation requested from an external function or service. | 要外部函数或服务完成的操作。 |
| external action | 外部动作 | An action performed outside the model. | 在模型之外的系统中实际发生的动作。 |
| controlled external action | 受控外部动作 | An external action performed within application controls. | 在应用控制范围内执行的外部操作。 |
| structured way | 结构化方式 | A way of making a request follow a defined structure. | 按规定结构提出请求的方式。 |
| structured request | 结构化请求 | A request represented in a defined form. | 按固定形式表示的请求。 |
| structured tool request | 结构化工具请求 | A model-produced request to use a tool in a defined structure. | 模型按固定结构生成的工具使用请求。 |
| structured calendar request | 结构化日历请求 | A structured request to create a calendar event. | 按规定格式创建日历事件的请求。 |
| defined shape | 定义好的形状；规定格式 | The required form of a tool request. | 工具请求必须遵守的格式。 |
| request in a defined shape | 按规定格式的请求 | A request expressed in the shape required by the application. | 按应用要求的结构写出的请求。 |
| model | 模型 | The AI component that proposes a tool call. | 提出工具调用建议的 AI 模型。 |
| AI | 人工智能 | The technology used to interpret a request and propose an action. | 用来理解请求并提出动作建议的智能技术。 |
| model decision | 模型决策 | A model-generated choice about what action or tool may be needed. | 模型判断应该使用哪个工具或做什么动作。 |
| model decisions | 模型决策 | Choices made by the model during the workflow. | 模型在流程中作出的多个判断。 |
| request | 请求 | An instruction asking a system or tool to do something. | 要求系统或工具完成某件事的指令。 |
| model request | 模型请求 | A request associated with the model's proposed tool use. | 和模型提出的工具使用有关的请求。 |
| tool request | 工具请求 | A request to use a specified tool. | 请求使用某个指定工具。 |
| service request | 服务请求 | A request that names a service and the information it needs. | 写明服务名称和所需信息的请求。 |
| request to use a tool | 使用工具的请求 | A request asking an application to invoke a tool. | 要应用调用某个工具的请求。 |
| request an action | 请求一个动作 | Ask an external function or service to perform an operation. | 请外部函数或服务执行一个操作。 |
| ask an external function | 请求外部函数 | Ask an outside function to perform the action. | 请外部函数帮忙执行动作。 |
| ask an external service | 请求外部服务 | Ask an outside service to perform the action. | 请外部服务帮忙执行动作。 |
| propose a call | 提出调用建议 | Have the model suggest a tool call for the application to inspect. | 由模型先建议一次工具调用，交给应用检查。 |
| model proposes a call | 模型提出调用 | The model suggests a call instead of directly controlling the external system. | 模型只是提出调用建议，不是直接控制外部系统。 |
| tool call proposal | 工具调用提议 | A proposed call that still needs application handling. | 仍需应用处理的一次工具调用建议。 |
| choose a call | 选择调用 | Select the tool call that fits the request. | 选择适合当前请求的工具调用。 |
| required fields | 必填字段 | Fields that a service request must contain. | 服务请求中必须填写的字段。 |
| field | 字段 | A named piece of information in a request. | 请求中的一个命名信息栏位。 |
| fields | 字段集合 | The named pieces of information in a request. | 请求中包含的多个信息栏位。 |
| tool inputs | 工具输入 | Values supplied to a tool when it is called. | 调用工具时传给工具的内容。 |
| input | 输入 | Information supplied to a model, application, or tool. | 传给模型、应用或工具的信息。 |
| inputs | 输入项 | The values a tool call provides to a tool. | 工具调用提供给工具的一组值。 |
| tool input | 工具输入项 | One value supplied to a tool. | 传给工具的一个具体值。 |
| name | 名称 | The identifier used to name a tool or service. | 用来识别工具或服务的名字。 |
| tool name | 工具名称 | The name used to identify a callable tool. | 用来识别可调用工具的名称。 |
| service name | 服务名称 | The name of the service named in a request. | 请求中写明的服务名称。 |
| limits | 限制；边界 | Boundaries on what a tool call may do. | 工具调用可以做什么、不能做什么的边界。 |
| tool limits | 工具限制 | Boundaries defined for a tool. | 为工具规定的操作范围和限制。 |
| permissions | 权限 | Application-defined authority governing tool use. | 应用规定的、决定工具能否使用的授权范围。 |
| application permissions | 应用权限 | Permissions under which the application allows a call to work. | 应用允许工具调用使用的权限范围。 |
| permission boundary | 权限边界 | The limit on what the model or tool is allowed to do. | 模型或工具被允许做什么的边界。 |
| automatic permission | 自动权限 | Permission that a model would receive without an explicit application grant. | 模型没有默认自动获得的权限。 |
| authorization | 授权 | A check or decision about whether the requested action is allowed. | 检查或决定某个动作是否被允许。 |
| application authorization | 应用授权 | Authorization determined by the application. | 由应用决定是否批准的授权。 |
| authorized tool use | 已授权的工具使用 | Tool use permitted by the application's rules. | 符合应用规则、被批准的工具使用。 |
| validate | 验证；校验 | Check a proposed call and its inputs before execution. | 执行前检查调用建议和输入。 |
| validation | 验证；校验 | The process of checking whether a tool request is acceptable. | 检查工具请求是否可以接受的过程。 |
| application validates | 应用进行验证 | The application checks the proposed call. | 应用检查模型提出的调用。 |
| check permissions | 检查权限 | Verify that the requested tool use is allowed. | 确认请求的工具使用是否获准。 |
| check inputs | 检查输入 | Verify the values supplied to the tool. | 检查传给工具的输入值。 |
| input validation | 输入验证 | Checking tool inputs before running the tool. | 运行工具前检查输入内容。 |
| permission check | 权限检查 | A check of whether the caller is authorized. | 检查调用者是否有权限。 |
| authorization check | 授权检查 | A check that confirms permission for an action. | 确认某个动作是否获授权的检查。 |
| execute | 执行 | Run the approved tool or service action. | 运行已经批准的工具或服务动作。 |
| execution | 执行过程 | The stage in which the external function or service performs the action. | 外部函数或服务真正执行动作的阶段。 |
| tool execution | 工具执行 | Running a selected tool. | 运行选定的工具。 |
| execute the call | 执行调用 | Run the requested tool call after checks. | 检查通过后运行工具调用。 |
| run the tool | 运行工具 | Execute the selected external tool. | 实际运行被选中的外部工具。 |
| perform the action | 执行动作 | Carry out the action requested in the call. | 执行调用中要求的动作。 |
| external function performs the action | 外部函数执行动作 | The external function carries out the requested operation. | 外部函数真正完成请求的操作。 |
| external service performs the action | 外部服务执行动作 | The external service carries out the requested operation. | 外部服务真正完成请求的操作。 |
| return | 返回 | Send the tool's result back to the application or model. | 把工具结果传回应用或模型。 |
| return the result | 返回结果 | Send the result after tool execution. | 工具执行后把结果传回来。 |
| send the result | 发送结果 | Pass the tool output to the next system component. | 把工具输出传给流程的下一个环节。 |
| tool output | 工具输出 | Information produced by a tool after execution. | 工具执行后产生的信息。 |
| result | 结果 | The outcome returned by a tool or service. | 工具或服务返回的结果。 |
| returned result | 返回结果 | A result sent back after execution. | 执行后传回来的结果。 |
| application result | 应用结果 | A result received by the application. | 应用收到的工具执行结果。 |
| model result | 模型结果 | A result returned to the model for the next step. | 返回给模型、供下一步使用的结果。 |
| output | 输出 | Information returned by the tool or model. | 工具或模型返回的信息。 |
| output returned after execution | 执行后返回的输出 | The output produced only after a tool has run. | 工具真正运行后才返回的输出。 |
| next step | 下一步 | The next stage after a tool result is returned. | 工具结果返回后流程继续进行的下一步。 |
| workflow | 工作流程 | The ordered sequence from request through execution and result handling. | 从请求、执行到处理结果的一连串步骤。 |
| application workflow | 应用工作流 | The surrounding software process that handles the call. | 应用外围处理工具调用的软件流程。 |
| workflow node | 流程节点 | One named stage in the tool-calling flow. | 工具调用流程中的一个明确阶段。 |
| process | 流程；过程 | The ordered method used to complete a tool call. | 完成工具调用所采用的有序方法。 |
| process step | 流程步骤 | One stage in the ordered process. | 有序流程中的一个阶段。 |
| five-step process | 五步流程 | Define, Request, Validate, Execute, and Return. | 定义、请求、验证、执行、返回五个步骤。 |
| 1 · Define | 1·定义 | The first step: describe the tool. | 第一步：先描述工具。 |
| Define | 定义 | Specify what the tool is and how it may be used. | 规定工具是什么、可以怎样使用。 |
| define the tool | 定义工具 | Establish the tool's name, inputs, permissions, or limits. | 规定工具名称、输入、权限或限制。 |
| describe the tool | 描述工具 | Explain the callable tool to the application or model. | 向应用或模型说明这个可调用工具。 |
| declare the tool | 声明工具 | Formally state the tool's callable information. | 正式声明工具的调用信息。 |
| declare its name | 声明名称 | Specify the identifier of the tool. | 规定工具的识别名称。 |
| declare its inputs | 声明输入 | Specify what values the tool accepts. | 规定工具接受哪些输入值。 |
| declare its limits | 声明限制 | Specify the boundaries of tool use. | 规定工具调用的边界。 |
| tool definition | 工具定义 | The description of a tool, its inputs, and its limits. | 对工具、输入和限制的说明。 |
| tool specification | 工具规格 | The declared information that describes how a tool can be called. | 说明工具如何被调用的规格信息。 |
| 2 · Request | 2·请求 | The second step: choose a call. | 第二步：选择一个调用。 |
| Request | 请求 | Have the model return a structured tool request. | 让模型返回结构化工具请求。 |
| choose a tool call | 选择工具调用 | Select a call for the requested action. | 为请求的动作选择合适的工具调用。 |
| model returns a structured tool request | 模型返回结构化工具请求 | The model produces the requested call in a structured form. | 模型按结构化形式生成工具调用请求。 |
| 3 · Validate | 3·验证 | The third step: check permissions and inputs. | 第三步：检查权限和输入。 |
| Validate | 验证 | Check the proposed call before it runs. | 工具运行前检查调用建议。 |
| application checks inputs | 应用检查输入 | The application verifies the supplied input values. | 应用核对传入的输入值。 |
| application checks authorization | 应用检查授权 | The application verifies that the action is permitted. | 应用确认这个动作是否获准。 |
| 4 · Execute | 4·执行 | The fourth step: run the tool. | 第四步：运行工具。 |
| Execute | 执行 | Run the external function or service after validation. | 验证后运行外部函数或服务。 |
| Run the tool | 运行工具 | Perform the selected tool operation. | 执行选定的工具操作。 |
| 5 · Return | 5·返回 | The fifth step: send the result. | 第五步：发送结果。 |
| Return | 返回 | Pass tool output to the application or model. | 把工具输出传给应用或模型。 |
| Send the result | 发送结果 | Deliver the execution result to the next recipient. | 把执行结果交给下一个接收方。 |
| calendar event | 日历事件 | An event created in a calendar as the result of a request. | 根据请求在日历里创建的一项事件。 |
| Everyday example | 日常示例 | The page's everyday tool-calling example. | 页面用来说明工具调用的日常例子。 |
| Calendar event example | 日历事件示例 | The example of scheduling a meeting through a calendar tool. | 通过日历工具安排会议的例子。 |
| schedule a meeting tomorrow at 10 | 安排明天十点的会议 | A natural-language request to create a calendar event. | 用自然语言要求创建明天十点的会议。 |
| “Schedule a meeting tomorrow at 10.” | “安排明天十点的会议。” | The example user's calendar instruction. | 页面中的日历安排示例请求。 |
| calendar request | 日历请求 | A request to create or update a calendar event. | 请求创建或更新日历事件。 |
| confirmed event | 已确认事件 | A calendar event successfully created or confirmed. | 已成功创建或确认的日历事件。 |
| confirmation | 确认 | A signal that the requested event was completed. | 表示请求的事件已经完成的确认信息。 |
| account lookup | 账户查询 | A request to retrieve permitted information about an account. | 查询账户许可信息的操作。 |
| Business example | 业务示例 | The page's business-oriented tool-calling example. | 页面用来说明业务工具调用的例子。 |
| account lookup example | 账户查询示例 | The example of calling an approved account service. | 调用获批账户服务的例子。 |
| support request | 支持请求；客服请求 | A request from a support workflow. | 客服或支持流程收到的请求。 |
| account ID | 账户 ID；账户标识符 | An identifier used to look up an account. | 用来查询账户的唯一标识。 |
| approved account service | 获批准的账户服务 | An account service approved for the workflow to call. | 这个工作流获准调用的账户服务。 |
| permitted account data | 获准的账户数据 | Account information the workflow is allowed to receive. | 工作流被允许取得的账户信息。 |
| data | 数据 | Information returned by the account service. | 账户服务返回的信息。 |
| workflow data | 工作流数据 | Data returned for use in the business workflow. | 返回给业务流程使用的数据。 |
| confirmed event or error | 已确认事件或错误 | The possible outcomes of the calendar request. | 日历请求可能成功确认，也可能报错。 |
| error | 错误；报错 | An indication that the requested action did not succeed. | 请求动作没有成功时返回的错误信息。 |
| failure | 失败 | A condition in which the tool action cannot complete as expected. | 工具动作没有按预期完成的情况。 |
| error outcome | 错误结果 | An unsuccessful outcome returned by the workflow. | 工作流返回的未成功结果。 |
| Text Generation | 文本生成 | Producing language as model output. | 模型生成文字内容的过程。 |
| text generation | 文本生成 | A model capability that returns language rather than an external action. | 返回语言内容、而不是执行外部动作的能力。 |
| language | 语言；文字 | The language content returned as model output. | 模型输出的文字内容。 |
| model output | 模型输出 | Language or data returned by the model. | 模型返回的文字或数据。 |
| external action request | 外部动作请求 | A request for an outside system to perform a defined action. | 请求外部系统完成规定动作。 |
| Automatic Permission | 自动权限 | The idea that a model automatically receives authority. | 认为模型会自动获得权限的概念。 |
| by default | 默认情况下 | Without an explicit application grant or configuration. | 没有额外明确授权时。 |
| model does not receive by default | 模型默认不会获得 | The model is not automatically granted external-system authority. | 模型不会自动拥有外部系统的权限。 |
| application-controlled permission | 应用控制的权限 | Authority managed by the application rather than assumed by the model. | 由应用管理、而不是由模型自行拥有的权限。 |
| Tool Result | 工具结果 | The output returned after a tool executes. | 工具执行后返回的输出。 |
| tool result | 工具结果 | The result produced by an executed tool. | 已运行工具产生的结果。 |
| result after execution | 执行后的结果 | Output available after the external action is performed. | 外部动作完成后才可得到的输出。 |
| output returned after execution | 执行后返回的输出 | The tool output sent back after execution. | 工具执行完后传回的输出。 |
| AI Agent | AI 智能体 | A related system that can use tools as part of its work. | 可以把工具作为工作一部分来使用的 AI 系统。 |
| Agent Loop | 智能体循环 | A related loop in which a model acts, receives results, and continues. | 模型行动、收到结果并继续工作的循环。 |
| Structured Outputs | 结构化输出 | A related way to require model output to follow a defined shape. | 要求模型输出遵守规定结构的相关概念。 |
| Failure Handling | 失败处理 | A related practice for responding when a tool call or result fails. | 工具调用或结果失败时采取应对措施的相关概念。 |
| related concept | 相关概念 | A concept connected to tool calling. | 和工具调用有联系的概念。 |
| Model Request → Validate → Tool Execution → Tool Result → Next Step | 模型请求→验证→工具执行→工具结果→下一步 | The page's conceptual chain for a tool call. | 页面展示的工具调用概念链。 |
| request-validation-execution-return flow | 请求-验证-执行-返回流程 | The end-to-end path from a proposed request to its result. | 从提出请求到拿到结果的完整路径。 |
| model decision to controlled external action | 从模型决策到受控外部动作 | The connection made by tool calling. | 工具调用把模型判断连接到受控的外部操作。 |
| controlled action | 受控动作 | An action governed by application checks and permissions. | 经过应用检查和权限控制的动作。 |
| Independent explainer | 独立讲解内容 | A separate explanatory video or visual resource. | 独立提供说明的讲解视频或视觉资源。 |
| visual explainer | 可视化讲解 | Visual material that explains the topic. | 用视觉方式解释主题的内容。 |
| Video | 视频 | The explainer media section on the page. | 页面上的讲解视频部分。 |

## Potential Missing Concepts

- The page does not explicitly define **function calling**, **API calling**, **API**, **endpoint**, **SDK**, **webhook**, or a provider-specific tool-calling interface; these are adjacent implementation candidates.
- It does not name a concrete serialization format such as **JSON**, **JSON Schema**, XML, YAML, or a typed function signature.
- It says “structured” and “defined shape” but does not explain schema syntax, object properties, arrays, nested objects, optional fields, defaults, enums, unions, nullability, or versioning.
- It does not distinguish prompt-only requests from provider-enforced structured arguments, constrained decoding, grammar-constrained generation, or decoder-time token constraints.
- It does not explain how a model selects among multiple tools, how tool descriptions are ranked, or what happens when no tool is appropriate.
- It does not define the exact request envelope: tool name, call ID, arguments, conversation turn, message role, or protocol fields.
- It does not explain argument parsing, malformed arguments, type coercion, missing fields, extra fields, or schema-validation errors.
- It does not describe client-side versus server-side validation, policy engines, access-control lists, identity, authentication, or authorization tokens.
- It does not explain human approval, confirmation prompts, least privilege, sandboxing, isolation, or side-effect policy for high-impact actions.
- It does not cover retries, backoff, idempotency, deduplication, cancellation, timeouts, rate limits, circuit breakers, fallbacks, or partial failure.
- It does not define transport failures, service unavailability, network errors, stale data, duplicate execution, or tool-result corruption.
- It does not explain how tool results are represented, escaped, summarized, returned to the model, or prevented from causing prompt injection.
- It does not distinguish a tool request from a tool result, a model message from an application message, or an in-memory object from persisted data beyond the short comparison.
- It does not define transaction boundaries, atomicity, compensation, rollback, or consistency when an external action changes state.
- It does not give a concrete API request/response example or runnable tool schema.
- It does not provide quantitative metrics. Useful follow-up candidates include tool-call success rate, valid-argument rate, tool-selection accuracy, execution latency, time to first tool call, error rate, authorization-denial rate, retry rate, timeout rate, duplicate-execution rate, result-grounding rate, and cost per successful action.
- It does not explain evaluation datasets, golden tool-call traces, exact-match evaluation for arguments, semantic argument accuracy, contract tests, fuzzing, regression tests, or end-to-end tests.
- It does not cover observability concepts such as call IDs, tracing, structured logs, audit logs, dashboards, alerts, or production drift.
- It does not discuss privacy, PII, secrets, data minimization, retention, tenant isolation, or sensitive account data handling.
- It does not discuss prompt injection, indirect instruction attacks, tool poisoning, confused-deputy attacks, data exfiltration, or unsafe tool descriptions.
- It does not explain model/provider capability differences, streaming tool calls, parallel tool calls, multiple tool calls in one turn, or tool-call ordering.
- It does not explain how tool calling relates to agents, planning, memory, MCP, workflows, orchestration, or the agent loop beyond linking related topics.
- It does not define calendar-specific concepts such as time zones, attendee identity, event conflicts, recurrence, confirmation semantics, or cancellation.
- It does not define account-lookup concepts such as identity matching, record-level authorization, field-level authorization, auditability, or data freshness.
- It does not specify what “permitted account data” means or how the application filters returned fields.
- It does not distinguish tool-call correctness from business correctness, factual correctness, user intent satisfaction, or successful external side effects.

## Aliases / Synonyms

- Tool Calling / Tool calling / tool calling / tool-calling / tool call / call to a tool
- Tool / external tool / callable tool / defined tool / approved tool
- External function / external service / external function or service / outside function / outside service
- AI application / application / software / surrounding application / AI system / AI / System
- External system / separate system / downstream system / service system
- Action / defined action / external action / requested action / operation / controlled external action
- Request / model request / tool request / structured request / structured tool request / service request / support request
- Request an action / ask an external function / ask an external service / request to use a tool
- Propose a call / model proposes a call / tool-call proposal / proposed tool use
- Tool input / tool inputs / input / inputs / call arguments / argument values
- Field / fields / required field / required fields / request field
- Name / tool name / service name / identifier
- Limits / tool limits / boundaries / operating limits / action boundaries
- Permission / permissions / application permissions / permission boundary / application-controlled permission
- Authorization / authorization check / application authorization / permission check / access check
- Validate / validation / application validates / check inputs / check permissions / input validation
- Execute / execution / tool execution / execute the call / run the tool / perform the action
- Return / return the result / send the result / result return / pass back the result
- Tool output / output / result / returned result / model result / application result
- Tool Result / tool result / result after execution / output returned after execution
- Error / failure / error outcome / unsuccessful outcome / execution error
- Calendar event / calendar request / structured calendar request / confirmed event / meeting event
- Schedule a meeting tomorrow at 10 / schedule meeting / create calendar event / calendar action
- Account lookup / account lookup example / account query / retrieve account data
- Support request / account ID / approved account service / permitted account data
- Text Generation / text generation / language generation / model output / returned language
- Automatic Permission / automatic permission / permission by default / default authority
- Structured way / structured request / defined shape / structured tool request / structured calendar request
- AI Agent / agent / intelligent agent / tool-using agent
- Agent Loop / agent loop / observe-act loop / model-action-result loop
- Structured Outputs / structured output / schema-constrained output / defined-shape output
- Failure Handling / failure handling / error handling / recovery handling
- Model Request → Validate → Tool Execution → Tool Result → Next Step / request-validation-execution-return flow / tool-call lifecycle

## Do Not Confuse Candidates

- Tool calling ≠ text generation: tool calling requests an external action in a defined shape; text generation returns language as model output.
- Tool calling ≠ automatic permission: a model may propose a call, but it does not receive external-system authority by default.
- Tool calling ≠ tool result: tool calling is the request to use a tool; a tool result is output returned after execution.
- Tool call ≠ tool: a call is one request to use a tool; the tool is the defined function or service being called.
- Tool request ≠ tool output: the request goes into the execution workflow; the output comes back after the tool runs.
- Model proposal ≠ external action: the model proposes a call; the application validates and executes it.
- Model decision ≠ authorization: a model can suggest an action without being authorized to perform it.
- Application validation ≠ execution: checking inputs and permissions is different from running the external function or service.
- Validation ≠ authorization: validation may check shape and inputs; authorization decides whether the caller may perform the action.
- Permission ≠ capability: having a declared tool capability does not necessarily mean a particular request is authorized.
- Tool execution ≠ tool result: execution is the act of running the tool; the result is what that run returns.
- External function ≠ model function: an external function is executed outside the model; the model only produces a request or proposal.
- External service ≠ external system: a service may be one interface to a larger external system.
- Defined action ≠ arbitrary action: a tool call should stay within the action and limits declared by the application.
- Required field ≠ valid value: providing a required field does not prove that its value is acceptable.
- Input validation ≠ business correctness: accepted inputs do not guarantee that the resulting business action is appropriate.
- Confirmed event ≠ successful user intent: a calendar event can be created while still having the wrong time, attendees, or interpretation.
- Account ID ≠ account authorization: knowing an identifier does not itself grant access to account data.
- Permitted account data ≠ all account data: the workflow may be allowed to receive only selected fields.
- Tool output ≠ trusted instruction: returned tool content may require filtering and should not automatically override application policy.
- Structured tool request ≠ JSON specifically: JSON may be one representation, but the page only requires a structured request and does not name JSON.
- Tool calling ≠ structured outputs: tool arguments may be structured, but structured outputs can also be returned without invoking an external tool.
- Tool calling ≠ agent: an agent may use tool calling, but tool calling is one capability or workflow mechanism.
- Tool calling ≠ agent loop: a tool call can be one step in an agent loop; the terms are not interchangeable.
- Tool calling ≠ MCP: MCP can provide a protocol or ecosystem for tools, while tool calling is the broader request-and-execution pattern.
- Tool result ≠ next step: the result is returned data; the next step is whatever the application or model does afterward.
- Error ≠ permission denial: an error can come from many causes; a permission denial is one specific authorization outcome.
- Failure ≠ validation failure: execution or transport can fail even when inputs and permissions pass validation.
- Return ≠ execute: execution performs the action; return sends the resulting information back.
- Application ≠ model: the model proposes; the application defines, validates, authorizes, and executes.
- Application permission ≠ model ownership: the model does not automatically own or control the external system.
- External action ≠ model output: an action changes or queries an outside system; model output is generated content.
- Account lookup ≠ unrestricted database access: the example limits access to an approved service and permitted data.
- Calendar request ≠ confirmed event: the request asks for an event; confirmation is an outcome after processing.
- Text generation ≠ tool output: generated language and output returned by an executed external tool have different origins.
- Error outcome ≠ empty result: an error communicates unsuccessful processing; an empty result may be a valid response.
- Visual explainer ≠ tool execution: the video explains the concept and does not perform a tool action.

## Notes

- The source page was read in full, including the title, description, page navigation, definition, analogy, five process steps, calendar example, account-lookup example, three “What it is NOT” comparisons, related-concepts chain, takeaway, and video section.
- The direct definition says that tool calling is a structured way for a model to request an action from an external function or service.
- The application defines each tool, its inputs, and its permissions; the model proposes a call, but the application validates and executes it.
- The direct five-step process is Define → Request → Validate → Execute → Return.
- The Define step says to describe the tool by declaring its name, inputs, and limits.
- The Request step says to choose a call and have the model return a structured tool request.
- The Validate step says the application checks inputs and authorization.
- The Execute step says to run the tool so the external function or service performs the action.
- The Return step says to send tool output back to the application or model.
- The everyday example is a natural-language request to schedule a meeting tomorrow at 10; the outcome is a confirmed event or an error.
- The business example is a support request with an account ID; the application calls an approved account service and returns permitted account data for the workflow.
- The page explicitly contrasts tool calling with text generation, automatic permission, and tool result.
- The page's related-concept chain is “Model Request → Validate → Tool Execution → Tool Result → Next Step”.
- The page links AI Agent, Agent Loop, Structured Outputs, and Failure Handling as related concepts; it does not explain those concepts in detail on this page.
- Candidate rows intentionally retain capitalization variants, singular/plural variants, wording from process labels, repeated concepts, beginner-facing phrases, and potentially confusable concepts.
- The page does not explicitly name JSON, schemas, APIs, function calling, metrics, retries, timeouts, human approval, or security controls; those are listed as potential missing concepts rather than treated as direct source claims.
- The page's core boundary is that the model proposes and the application controls, validates, authorizes, executes, and returns results.
- No website files, video assets, GitHub state, or other project files were modified.
