# Topic 11 · Guardrails

## Topic Metadata

- **Module:** 11 · Evaluation, Safety & Reliability
- **Topic:** Guardrails
- **Source page:** guardrails.html
- **Page title:** What Are AI Guardrails? · Evaluation, Safety & Reliability
- **Page eyebrow:** 11 · Evaluation, Safety & Reliability
- **Topic overview source:** evaluation-safety-reliability.html identifies this topic family as Module 11.
- **Extraction scope:** Full visible page body, including the title, ledes, on-page navigation, architecture flow, guardrail types, refund-agent example, distinction cards, defense-in-depth layers, related-concept links, takeaway, and video metadata.
- **Collection policy:** Raw candidate inventory only. Keep technical terms, mechanisms, workflow nodes, controls, actors, permissions, actions, outputs, metrics, abbreviations, important body words, aliases/synonyms, repeated labels, and potentially confusable concepts for later review. Candidates are intentionally broad, overlapping, and not deduplicated.

## Glossary Candidates

| Candidate | Category | Working definition / why it matters | Page evidence or context |
|---|---|---|---|
| AI Guardrails | Core concept / title form | Controls placed around an AI system to reduce unsafe, unwanted, or invalid behavior. | Page title |
| AI guardrails | Core concept / casing variant | Lowercase rendering of AI Guardrails. | Lede; page body |
| guardrail | Singular core concept | One control that constrains an AI system’s input, output, action, access, or approval path. | Candidate singular of “guardrails” |
| guardrails | Plural core concept | Controls designed to reduce unsafe, unwanted, or invalid AI behavior. | Lede |
| guardrail control | Core concept / compound | A control implemented as part of the guardrail system. | Architecture labels |
| controls | General mechanism | Rules or mechanisms that constrain behavior or require checks. | Lede; types; defense in depth |
| AI system | System concept | The system whose behavior, actions, permissions, and outputs are constrained. | “AI system” in takeaway |
| system | General system term | The software or AI workflow in which guardrails are placed. | “throughout the system” |
| AI behavior | Behavior concept | Observable behavior that guardrails are intended to constrain or improve. | Lede |
| unsafe behavior | Risk behavior | Behavior that could create harm or unacceptable risk. | Lede |
| unwanted behavior | Risk behavior | Behavior that is not desired by the user, product, or system owner. | Lede |
| invalid behavior | Validity failure | Behavior or result that violates defined rules or contracts. | Lede |
| unsafe | Risk qualifier | Not sufficiently safe for the intended use or action. | “unsafe ... behavior”; unsafe request |
| unwanted | Requirement qualifier | Not desired or permitted in the intended workflow. | “unwanted ... behavior” |
| invalid | Validity qualifier | Not conforming to required rules or expectations. | “invalid AI behavior” |
| reduce | Risk-reduction verb | Lower the likelihood or impact of undesirable system behavior. | Lede; remember this |
| risk | Safety concept | The possibility or consequence of unsafe, unwanted, or invalid behavior. | “reduce ... risk”; defense in depth |
| AI system risk | Risk concept | Risk arising from an AI system’s inputs, outputs, actions, or access. | Remember this |
| constrain | Control verb | Limit what the system may accept, produce, do, or access. | Remember this |
| constraining inputs | Control target | Limiting or screening incoming requests and content. | Remember this |
| constraining outputs | Control target | Limiting or checking generated results before delivery. | Remember this |
| constraining actions | Control target | Limiting actions an agent can take or propose for execution. | Remember this |
| constraining access | Control target | Limiting access to systems and data. | Remember this |
| input | Control surface | Content or request supplied to the AI system. | “check inputs”; architecture flow |
| inputs | Control surface / plural | Incoming content or requests that may be checked or filtered. | Lede; takeaway |
| input control | Control type | A control that checks or filters incoming content. | Types section |
| input controls | Control type / plural | Controls that check or filter incoming content before model processing. | Types section heading |
| output | Control surface | A generated result delivered to a user or system. | Architecture flow |
| outputs | Control surface / plural | Generated results that may be validated or rejected. | Lede; takeaway |
| output control | Control type | A control that validates generated results. | Types section |
| output controls | Control type / plural | Controls that validate generated results before they are accepted. | Types section heading |
| action | Control surface | An operation the model or agent proposes or performs. | Lede; permission distinction |
| actions | Control surface / plural | Operations that may be restricted or require approval. | Lede; takeaway |
| restrict | Control verb | Limit a capability, action, resource, or access path. | Lede |
| restrict actions | Control operation | Limit the operations an agent may call or execute. | Lede |
| validate | Control verb | Check whether something meets defined rules or requirements. | Lede; output controls |
| validate outputs | Control operation | Check generated results before they are passed onward. | Lede |
| require | Control verb | Make a check, review, or approval necessary before continuing. | Lede |
| require additional approval | Approval operation | Add a review checkpoint before a sensitive action proceeds. | Lede |
| approval | Control outcome / gate | Permission or authorization provided after review. | Lede; human approval |
| additional approval | Approval gate | Extra authorization required beyond the model’s proposal. | Lede |
| check | Verification operation | Inspect input, amount, permission, or output against a rule. | Architecture; refund example |
| filter | Input operation | Remove, block, or screen incoming content that should not proceed. | Input controls |
| block | Enforcement operation | Stop an unsafe or manipulative request from entering the workflow. | Input-control example |
| reject | Enforcement operation | Refuse to accept a generated result that violates a rule. | Output-control example |
| allow | Permission outcome | Permit a tool, action, or workflow to continue. | Search-versus-deletion example |
| deny | Permission outcome | Refuse access or execution for a system, data resource, or action. | Payment-release example |
| continue | Workflow outcome | Proceed to the next system stage after a control passes. | Core idea |
| may continue | Workflow condition | The system is allowed to proceed only after guardrail decisions. | Refund example note |
| approval gate | Potential alias / control mechanism | A checkpoint where a person or system must approve before execution. | Human approval; additional approval |
| control point | Architecture concept | A location in the workflow where a guardrail can be applied. | “multiple points” |
| multiple points | Architecture concept | More than one stage at which a guardrail can operate. | Flow caption |
| throughout the system | Architecture concept | Across the input, model, action, tool, output, and approval stages. | Architecture caption |
| user input | Workflow node | The request or content that enters the AI workflow. | Main architecture flow |
| USER INPUT | Workflow node / display label | Uppercase diagram label for the initial request stage. | Architecture diagram |
| input guardrail | Guardrail placement | A guardrail applied before the model processes the request. | Architecture diagram |
| INPUT GUARDRAIL | Guardrail placement / display label | Uppercase diagram label for the input-stage control. | Architecture diagram |
| model | System component | The model that interprets input and proposes an action or produces an output. | Architecture flow |
| MODEL | System component / display label | Uppercase diagram label for the model stage. | Architecture diagram |
| proposed action | Action state | An action suggested by the model but not yet authorized for execution. | Architecture flow; core idea |
| PROPOSED ACTION | Action state / display label | Uppercase diagram label for the model’s suggested operation. | Architecture diagram |
| tool | Capability component | A callable capability through which an agent can perform an operation. | Tool controls |
| tools | Capability components / plural | Callable capabilities that may be allowed or restricted. | Tool controls |
| tool control | Control type | A control that limits which actions an agent can call. | Types section |
| tool controls | Control type / plural | Controls that limit an agent’s callable actions. | Types section heading |
| tool / permission control | Guardrail placement | Combined control point for tool capability and permission enforcement. | Architecture diagram |
| TOOL / PERMISSION CONTROL | Guardrail placement / display label | Uppercase diagram label for the tool and permission stage. | Architecture diagram |
| permission | Access-control concept | A specific rule about what an action or resource allows. | Distinction card |
| permissions | Access-control concept / plural | Rules that determine whether access or an action is allowed. | Related concept “Permissions & Safety” |
| permission control | Control type | A control that restricts access to systems and data. | Types section |
| permission controls | Control type / plural | Controls that enforce access restrictions. | Types section heading |
| permission check | Verification operation | A check of whether the actor or agent is authorized to perform an action. | Refund flow |
| PERMISSION CHECK | Verification operation / display label | Uppercase refund-flow label for authorization checking. | Refund flow |
| access | Authorization surface | The ability to reach a system or data resource. | Permission controls; takeaway |
| restrict access | Authorization operation | Prevent an agent or user from reaching protected systems or data. | Permission controls |
| systems and data | Protected resources | Resources whose access can be restricted by permissions. | Permission-control description |
| output validation | Guardrail placement | Checking the generated result after model processing and before delivery. | Architecture diagram; defense layers |
| OUTPUT VALIDATION | Guardrail placement / display label | Uppercase diagram label for the output-checking stage. | Architecture diagram |
| user / system | Workflow endpoint | The recipient or downstream system that receives the validated output. | Architecture flow |
| USER / SYSTEM | Workflow endpoint / display label | Uppercase diagram label for the final recipient. | Architecture diagram |
| human approval | Human control | A person explicitly reviews a sensitive or consequential action. | Architecture; types; distinction |
| HUMAN APPROVAL | Human control / display label | Uppercase diagram label for the approval branch. | Architecture diagram |
| human-controlled | Control implementation | A guardrail operated through explicit human review or decision. | Guardrail vs Human approval |
| automated | Control implementation | A guardrail applied by software without a person’s direct review. | Guardrail vs Human approval |
| when required | Conditional control | Approval is needed only for actions meeting a defined condition. | Architecture diagram |
| approval when required | Conditional review | Human review triggered by sensitivity, value, or policy. | Architecture diagram; defense layer |
| flow | Workflow concept | Ordered path from user input to model, action, controls, output, and recipient. | Architecture diagram |
| main flow | Workflow concept | The primary sequence shown in the guardrail architecture. | Diagram class name |
| node | Diagram/workflow unit | A stage or entity in the architecture flow. | Diagram markup |
| arrow | Flow connector | Visual indicator of sequence between system stages. | Diagram markup |
| guardrail architecture | Architecture concept | Model of where controls can be placed in an AI system. | Diagram label/class |
| architecture flow | Architecture concept | Input-to-output sequence with control points. | Diagram |
| workflow stage | Process unit | A distinct point in the AI flow where a check or action occurs. | Diagram; examples |
| input stage | Workflow stage | Stage where incoming content is screened. | Architecture |
| model stage | Workflow stage | Stage where the model interprets input and proposes behavior. | Architecture |
| action stage | Workflow stage | Stage where a proposed operation is considered for execution. | Architecture |
| tool stage | Workflow stage | Stage where tool capabilities and calls are controlled. | Architecture |
| output stage | Workflow stage | Stage where generated results are checked or delivered. | Architecture |
| validation stage | Workflow stage | Stage where a result is checked against defined rules. | Architecture |
| approval stage | Workflow stage | Stage where a person reviews an action when needed. | Architecture |
| Types of guardrails | Section title / taxonomy | Taxonomy of input, output, tool, permission, and human controls. | Types section heading |
| input controls | Control taxonomy | Checks or filters for incoming content. | Types section |
| check incoming content | Input-control operation | Inspect requests before the model handles them. | Input-control description |
| filter incoming content | Input-control operation | Screen or remove content that should not proceed. | Input-control description |
| incoming content | Input data | Content entering an AI system from a user or upstream source. | Input controls |
| unsafe request | Risky input | A request that should be blocked or otherwise controlled. | Input-control example |
| manipulative request | Adversarial input | A request attempting to bypass intended behavior or controls. | Input-control example |
| block an unsafe request | Enforcement example | Stop risky input before model execution. | Input-control example |
| block a manipulative request | Enforcement example | Stop input that attempts to manipulate the system. | Input-control example |
| output controls | Control taxonomy | Checks applied to generated results. | Types section |
| generated result | Model output | Result produced by the model for delivery or further processing. | Output-control description |
| validate generated results | Output-control operation | Check generated content against defined requirements. | Output controls |
| reject an answer | Enforcement example | Do not pass along an answer that fails a content rule. | Output-control example |
| answer | Output type | A textual result produced for the user. | Output-control example |
| unsupported claim | Output risk | A claim that lacks sufficient support or violates an output rule. | Output-control example |
| unsupported claims | Output risk / plural | Claims in a generated answer that are not adequately supported. | Output-control example |
| answer that contains unsupported claims | Rejection condition | Generated answer that should be rejected by an output control. | Output-control example |
| tool controls | Control taxonomy | Restrictions on the actions an agent can call. | Types section |
| limit actions | Tool-control operation | Reduce the set of operations available to an agent. | Tool-control description |
| agent | Actor / system component | An AI system capable of selecting or calling tools. | Tool-control example |
| agent can call | Capability boundary | Actions available to the agent through its tools. | Tool controls |
| allow search | Permission example | Permit a search capability while keeping more dangerous actions unavailable. | Tool-control example |
| search | Tool capability | A permitted retrieval or lookup operation. | Tool-control example |
| deletion | Destructive action | An operation that may be restricted even when search is allowed. | Tool-control example |
| allow search but not deletion | Capability policy | Example of fine-grained tool restriction. | Tool-control example |
| permission controls | Control taxonomy | Rules limiting access to systems and data. | Types section |
| deny payment release | Permission example | Refuse authorization to release a payment. | Permission-control example |
| payment release | Consequential action | A financial operation that may require explicit permission. | Permission-control example |
| human approval | Control taxonomy | Review required for sensitive actions. | Types section |
| require review | Human-control operation | Make human review a prerequisite for execution. | Human-approval description |
| sensitive action | Risky action | Action requiring special review because of its consequences. | Human-approval description |
| approve a large refund | Human-control example | Human authorization for a high-value financial action. | Human-approval example |
| large refund | Consequential action | A refund amount large enough to trigger review. | Human-approval example |
| sensitive actions | Risky actions / plural | Actions for which a person must review or approve. | Human-approval description |
| One real example | Section label | Concrete example used to show controls in sequence. | Example heading |
| real example | Example type | A worked scenario rather than a purely abstract definition. | Example heading |
| AI refund agent | Example system | Agent that receives a refund request and may execute a financial action. | Example heading |
| refund agent | Example system / alias | Short form for AI refund agent. | Example heading |
| refund | Financial action | Returning money to a customer. | User request; examples |
| refund request | User request type | Request to return a specified amount of money. | Example |
| User: “Refund $10,000 immediately.” | Example input | Exact request used to demonstrate amount, permission, and approval checks. | Definition block |
| refund $10,000 | Example action | High-value refund action proposed by the user or agent. | Refund flow |
| $10,000 | Amount / numeric value | Example monetary amount used to trigger a control path. | Refund request |
| immediately | Timing qualifier | User request for immediate execution without delay. | Refund request |
| USER | Actor / display label | Person or actor initiating the refund request. | Refund flow |
| CHECK | Workflow label | Refund-flow stage where the amount is checked. | Refund flow |
| amount check | Validation operation | Check of the requested refund amount. | Refund flow |
| AMOUNT CHECK | Validation operation / display label | Uppercase refund-flow label for amount checking. | Refund flow |
| amount | Financial field | Numeric value that determines the scale of the refund. | Amount check |
| CONTROL | Workflow label | Refund-flow stage where permission is enforced. | Refund flow |
| permission check | Authorization operation | Check of whether the refund action is authorized. | Refund flow |
| REVIEW | Workflow label | Refund-flow stage where a person evaluates the proposed action. | Refund flow |
| RESULT | Workflow label | Final stage showing whether execution occurs. | Refund flow |
| execute | Action verb | Carry out the proposed refund action. | Result card |
| execute only if allowed | Conditional execution | Perform the action only after checks and permissions pass. | Result card |
| allowed | Authorization outcome | Permitted to continue or execute. | Result card |
| control determines whether the system may continue | Guardrail principle | Guardrails decide if a proposed action can advance through the workflow. | Core idea note |
| model can propose an action | Model/action distinction | The model’s proposal is not the same as authorized execution. | Core idea note |
| proposed action vs executed action | Distinction candidate | A proposal requires controls before it becomes an executed operation. | Architecture; refund example |
| financial action | Consequential action | Action involving money, such as refund or payment release. | Examples |
| high-value payment | Consequential action | Payment whose value triggers a guardrail or control. | Permission distinction example |
| high-value payment requires control | Policy example | Example of a broad guardrail that triggers control for valuable payments. | Guardrail vs Permission |
| agent cannot release payment | Permission example | Specific permission rule that forbids a payment-release action. | Guardrail vs Permission |
| Guardrails and related controls | Section title | Comparison of guardrails with guarantees, permissions, validation, and human approval. | Distinctions heading |
| related control | Comparison concept | A neighboring mechanism that may overlap with guardrails but has a narrower meaning. | Distinctions section |
| key distinction | Comparison concept | A boundary between guardrail and a related control. | On-page navigation |
| guardrail vs guarantee | Contrast pair | A guardrail reduces risk; a guarantee would mean failure cannot happen. | Distinction card |
| guarantee | Assurance concept | A claim that failure cannot happen, stronger than what guardrails provide. | Guardrail vs Guarantee |
| failure cannot happen | Absolute assurance | Infallibility claim explicitly contrasted with risk reduction. | Guardrail vs Guarantee |
| improve safety | Safety outcome | Guardrails make behavior safer without making the system infallible. | Guardrail vs Guarantee |
| safety | Safety property | Reduced exposure to harmful or unacceptable behavior. | Distinction; layered safety |
| infallible | Assurance qualifier | Unable to fail; explicitly not promised by guardrails. | Guardrail vs Guarantee |
| guardrail vs permission | Contrast pair | Guardrail is broader; permission is a specific allow/deny rule. | Distinction card |
| broader control concept | Scope distinction | Guardrails can include multiple control mechanisms. | Guardrail vs Permission |
| specific rule | Scope distinction | A rule that states what an action or resource allows. | Guardrail vs Permission |
| action allows | Permission semantics | The permission relationship governing whether an action is authorized. | Guardrail vs Permission |
| resource allows | Permission semantics | The permission relationship governing access to a resource. | Guardrail vs Permission |
| guardrail: high-value payment requires control | Compound example | Broad guardrail policy for a valuable payment. | Distinction card |
| permission: agent cannot release payment | Compound example | Narrow permission rule forbidding a specific action. | Distinction card |
| guardrail vs validation | Contrast pair | Guardrail is broader; validation checks conformance to defined rules. | Distinction card |
| meets defined rules | Validation criterion | Condition for a valid input, output, or action. | Guardrail vs Validation |
| defined rules | Validation basis | Rules used to evaluate whether something is acceptable. | Guardrail vs Validation |
| broader system control | Guardrail scope | System-level control that may combine several mechanisms. | Guardrail vs Validation |
| validation | Verification mechanism | Check of whether something meets defined rules. | Distinction card |
| filters | Guardrail component | Content or input filtering can be part of a broader guardrail. | Guardrail vs Validation |
| approval gates | Guardrail component | Approval checkpoints can be part of a broader guardrail. | Guardrail vs Validation |
| guardrail vs human approval | Contrast pair | Guardrail can be automated or human-controlled; human approval is explicit review. | Distinction card |
| person explicitly reviews | Human oversight | A person examines an action before it proceeds. | Guardrail vs Human approval |
| explicit review | Human oversight | Deliberate human examination rather than implicit or automated checking. | Distinction card |
| human approval can be one type of guardrail | Taxonomy relationship | Human approval is a possible guardrail implementation, not a synonym for all guardrails. | Distinction card |
| automated control | Implementation type | Control enforced by software or system logic. | Guardrail vs Human approval |
| human control | Implementation type | Control enforced through a person’s review or decision. | Guardrail vs Human approval |
| Defense in depth | Safety architecture | Use multiple independent or layered controls so no single control handles every risk. | Section heading |
| defense-in-depth | Hyphenated variant | Hyphenated form of the layered safety strategy. | Candidate spelling variant |
| layered safety | Safety architecture | Safety achieved through several control layers. | Layered-safety label |
| layer | Safety mechanism | One control layer in a defense-in-depth design. | Layer diagram |
| layers | Safety mechanism / plural | Multiple controls applied at different workflow points. | Defense section |
| no single control | Safety principle | One control should not be expected to handle every risk. | Muted note |
| every risk | Safety scope | The full range of risks that may require multiple controls. | Defense section note |
| INPUT CHECK | Safety layer / display label | Layer that screens the request before processing. | Defense layer diagram |
| input check | Safety layer | Screening or checking the request at the input boundary. | Defense layer diagram |
| screen the request | Input operation | Inspect the request for unsafe or unwanted content. | Input-check layer |
| request | Input object | User content submitted to the system. | Input-check layer |
| SYSTEM INSTRUCTION | Safety layer / display label | Instruction layer defining safe behavior. | Defense layer diagram |
| system instruction | Control specification | Instruction that defines how the system should behave safely. | Defense layer diagram |
| define safe behavior | Safety specification | State expected safe behavior for the model or agent. | System-instruction layer |
| safe behavior | Safety target | Behavior that follows safety requirements and controls. | System-instruction layer |
| TOOL RESTRICTION | Safety layer / display label | Layer limiting available capabilities. | Defense layer diagram |
| tool restriction | Safety layer | Restriction on which tools or actions are available. | Defense layer diagram |
| limit capabilities | Capability control | Reduce the set of operations the system can perform. | Tool-restriction layer |
| capabilities | System affordances | Operations available to an AI agent or system. | Tool-restriction layer |
| PERMISSION | Safety layer / display label | Layer enforcing access rights. | Defense layer diagram |
| enforce access | Authorization operation | Apply permission rules to systems, data, or actions. | Permission layer |
| OUTPUT VALIDATION | Safety layer / display label | Layer checking the result after generation. | Defense layer diagram |
| check the result | Validation operation | Inspect generated output against a defined rule. | Output-validation layer |
| result | Output object | The generated or executed outcome under review. | Output-validation layer; refund result |
| HUMAN APPROVAL | Safety layer / display label | Layer that reviews an action when needed. | Defense layer diagram |
| review when needed | Conditional oversight | Escalate selected actions to a human reviewer. | Human-approval layer |
| needed | Trigger condition | Condition under which human review is required. | “when needed” |
| system instruction + tool restriction | Layer combination | Combined instruction and capability constraints. | Defense-in-depth layers |
| input check + output validation | Layer combination | Boundary checks on both incoming and outgoing content. | Defense-in-depth layers |
| permission enforcement | Layer combination | Access control applied after a proposed action. | Defense-in-depth layers |
| related concepts | Navigation section | Links to neighboring safety, oversight, failure, deployment, and evaluation topics. | Related concepts heading |
| Prompt Injection | Related concept / topic link | Attack or manipulation pattern that input controls may need to address. | Related-concept chip |
| prompt injection | Related concept / lowercase | Lowercase alias of Prompt Injection. | Related-concept link |
| Permissions & Safety | Related concept / topic link | Topic covering permissions and safety controls. | Related-concept chip |
| permissions and safety | Related concept / punctuation variant | Plain-text rendering of Permissions & Safety. | Related-concept link |
| Human in the Loop | Related concept / topic link | Human oversight pattern related to approval controls. | Related-concept chip |
| human in the loop | Related concept / lowercase | Lowercase alias of Human in the Loop. | Related-concept link |
| Human-in-the-loop | Potential alias / hyphenated form | Hyphenated name for a system with human review or intervention. | Candidate alias from related concept |
| Failure Handling | Related concept / topic link | Topic about what the system does after or during failure. | Related-concept chip |
| failure handling | Related concept / lowercase | Lowercase alias of Failure Handling. | Related-concept link |
| Deployment Readiness | Related concept / topic link | Topic about whether the system is ready for release or use. | Related-concept chip |
| deployment readiness | Related concept / lowercase | Lowercase alias of Deployment Readiness. | Related-concept link |
| Evaluation | Related concept / topic link | Topic about measuring or judging system behavior and performance. | Related-concept chip |
| evaluation | Related concept / lowercase | Lowercase alias of Evaluation. | Related-concept link |
| remember this | Takeaway label | Summary section emphasizing risk reduction through constraints. | Takeaway heading |
| reduce AI system risk | Takeaway statement | Guardrails lower system risk by constraining several control surfaces. | Takeaway paragraph |
| reduce system risk | Takeaway variant | Shorter form of the takeaway statement. | Takeaway paragraph |
| constrain inputs, outputs, actions, and access | Takeaway relationship | Four main surfaces controlled by guardrails. | Takeaway paragraph |
| input-output-action-access | Control-surface set | Compact inventory of the four surfaces named in the takeaway. | Takeaway paragraph |
| Independent explainer | Video label | Label for the accompanying explanatory video. | Video section |
| independent explainer | Video label / lowercase | Lowercase variant of the video label. | Video section |
| Video | Media label | Video resource explaining controls, layers, and approval. | Video heading |
| video | Media concept / lowercase | Lowercase variant of Video. | Video element |
| visual explainer | Media description | Visual explanation of the guardrail concepts. | Video metadata |
| visual explainer · captions included | Media metadata | Video metadata indicating captions are available. | Video card |
| captions included | Accessibility metadata | The video includes captions. | Video label |
| captions | Accessibility feature | Text representation accompanying the video. | Video metadata |
| controls · layers · approval | Video topic metadata | Video covers control mechanisms, layers, and approval. | Video metadata |
| controls | Video topic label | Visible metadata term for the video. | Video metadata |
| layers | Video topic label | Visible metadata term for the video. | Video metadata |
| approval | Video topic label | Visible metadata term for the video. | Video metadata |
| MP4 | Media format abbreviation | Video container format used by the explainer. | Video metadata |
| H.264 | Video codec | Video compression codec named in the metadata. | Video metadata |
| AAC | Audio codec abbreviation | Audio compression codec named in the metadata. | Video metadata |
| MP4 · H.264 + AAC | Media-format string | Combined video/container and codec metadata. | Video metadata |
| video playback | Media behavior | Ability of the browser to play the explainer. | Video fallback text |
| video controls | Media UI | Playback controls exposed by the HTML video element. | Video element |
| captions track | Accessibility/media resource | Track attached to the video for captions. | Video element |
| guardrail flow | Workflow alias | Ordered path through input, model, action, permission, output, and approval checks. | Architecture and refund flow |
| input-to-output flow | Workflow alias | End-to-end path from user request to final recipient. | Architecture |
| allow/deny rule | Permission alias | Binary rule controlling whether a capability or action can proceed. | Permission distinction |
| validation gate | Validation alias | Checkpoint that blocks nonconforming inputs or outputs. | Validation distinction |
| human review gate | Approval alias | Checkpoint requiring explicit human review. | Human approval |
| capability boundary | Tool-control alias | Limit on what an agent is able to call or execute. | Tool controls |
| access boundary | Permission alias | Limit on systems, data, or resources reachable by the agent. | Permission controls |
| action authorization | Permission alias | Decision that a proposed action is allowed to execute. | Permission check |
| output screening | Output-control alias | Screening generated content before delivery. | Output validation |
| input screening | Input-control alias | Screening requests before model processing. | Input check |
| safety layer | Defense-in-depth alias | One layer that reduces a class of system risk. | Layered safety |
| control layer | Defense-in-depth alias | A guardrail mechanism applied as one layer in a system. | Defense in depth |
| layered controls | Defense-in-depth alias | Multiple controls operating at different stages. | Defense in depth |

## Potential Missing Concepts

These concepts are suggested by the page’s wording, flow, examples, or distinctions but are not fully defined in the source body. Keep them as candidates for later glossary review rather than silently treating them as page definitions:

- **Prompt injection defenses**, **input sanitization**, **content moderation**, **request classification**, and **adversarial-input detection**: the page gives unsafe and manipulative requests as examples, but does not define implementation techniques.
- **Policy enforcement**, **policy engine**, **rule engine**, **safety policy**, **business rules**, and **policy-as-code**: the page repeatedly refers to defined rules and controls without naming a policy architecture.
- **Input validation**, **output validation**, **schema validation**, **format validation**, **content validation**, and **contract testing**: validation is named broadly, but no specific validator or schema mechanism is explained.
- **Prompt filtering**, **toxicity filtering**, **PII detection**, **data-loss prevention**, **jailbreak detection**, and **moderation model**: filtering/blocking is shown, but the possible detection layers are not described.
- **Tool allowlist**, **tool denylist**, **capability-based security**, **least privilege**, **sandboxing**, **action allowlist**, and **destructive-action protection**: tool restriction is named without an implementation pattern.
- **Authorization**, **authentication**, **role-based access control**, **attribute-based access control**, **resource-level permission**, and **access policy**: permission controls are described, but identity and authorization architecture are outside scope.
- **Human-in-the-loop**, **human-on-the-loop**, **human-over-the-loop**, **manual fallback**, **escalation**, **approval queue**, and **reviewer policy**: human approval is shown, but the broader oversight workflow is not defined.
- **Risk assessment**, **risk scoring**, **likelihood**, **impact**, **severity**, **risk appetite**, and **control effectiveness**: risk reduction is central, but no quantitative risk model is provided.
- **Defense in depth**, **independent controls**, **redundancy**, **fail-safe design**, **secure defaults**, and **separation of duties**: layered safety is named without formal security or safety-design principles.
- **Guarantee**, **assurance case**, **formal verification**, **infallibility**, and **safety proof**: the page distinguishes risk reduction from guarantees but does not explain assurance methods.
- **Hallucination**, **unsupported claim detection**, **grounding**, **citation**, **source attribution**, **evidence threshold**, **abstention**, and **uncertainty estimation**: unsupported output is named, but evidence-handling methods are not.
- **Refund limit**, **transaction threshold**, **payment authorization**, **high-value transaction policy**, **fraud detection**, and **financial controls**: the refund example uses an amount check but does not define financial-policy details.
- **Human approval trigger**, **sensitivity classification**, **consequential action**, **high-risk action**, and **approval threshold**: sensitive actions and “when required” are shown without trigger criteria.
- **Audit log**, **event logging**, **traceability**, **decision record**, **reason code**, and **explainability**: control decisions are shown, but evidence of those decisions is not discussed.
- **Monitoring**, **alerting**, **incident response**, **rollback**, **recovery**, **fallback**, **safe termination**, and **failure handling**: related topics are linked, but post-control operations are not defined here.
- **False positive**, **false negative**, **precision**, **recall**, **block rate**, **allow rate**, **approval rate**, **rejection rate**, and **override rate**: the page names checks and decisions but no guardrail performance metrics.
- **Latency**, **timeout**, **throughput**, **availability**, and **user friction**: adding checks and approval may affect system performance or experience, but those trade-offs are not discussed.
- **Guardrail bypass**, **control evasion**, **prompt manipulation**, **permission escalation**, and **policy circumvention**: manipulative requests are mentioned without an attack taxonomy.
- **Guardrail coverage**, **control coverage**, **defense coverage**, **test coverage**, **edge cases**, **adversarial cases**, and **regression tests**: multiple layers are shown, but coverage measurement is not described.
- **Model behavior**, **model alignment**, **instruction hierarchy**, **system prompt**, **tool-calling policy**, and **agent policy**: the model and system instruction appear in the flow, but their internal relationship is not explained.
- **Structured outputs**, **JSON schema**, **typed output**, **output contract**, and **schema-constrained decoding**: output validation is present, but no output-format mechanism is specified.
- **Data access boundary**, **data classification**, **sensitive data**, **secret management**, and **tenant isolation**: systems and data are protected in principle, without data-governance detail.
- **Defense-in-depth failure modes**, **single point of failure**, **control independence**, and **correlated controls**: the page says no single control handles every risk, but does not analyze layer dependence.
- **Approval delegation**, **segregation of duties**, **four-eyes principle**, and **dual control**: human approval is shown, but organizational approval patterns are not defined.
- **Safe default**, **deny by default**, **explicit consent**, **confirmation**, and **user confirmation**: approval and denial are shown, but default policy semantics are not specified.
- **Guardrail configuration**, **policy versioning**, **change management**, **deployment validation**, and **configuration drift**: deployment readiness is related, but guardrail lifecycle management is not explained.
- **Guardrail evaluation**, **safety evaluation**, **red teaming**, **benchmark**, **simulation**, and **scenario testing**: Evaluation is linked, but no test or measurement method is detailed.
- **MP4**, **H.264**, **AAC**, **captions**, and **video playback**: these are visible media metadata rather than defined guardrail concepts; retain them only because the extraction scope includes the full visible body.

## Aliases / Synonyms

Keep these as separate raw candidates until the later glossary pass decides whether to merge them:

| Candidate | Possible alias/synonym relationship |
|---|---|
| AI Guardrails | AI guardrails; guardrails; AI safety controls |
| Guardrail | guardrail control; safety control; control point |
| Guardrails | guardrail; AI guardrails; layered controls; system controls |
| controls | control mechanisms; guardrails; constraints |
| input control | input guardrail; input screening; input check; request filter |
| input controls | input guardrails; input checks; incoming-content filters |
| output control | output guardrail; output screening; output validation |
| output controls | output guardrails; generated-result checks |
| tool control | tool restriction; capability control; tool guardrail |
| tool controls | tool restrictions; capability restrictions; tool-use safeguards |
| permission control | access control; authorization control; permission guardrail |
| permission controls | access controls; authorization rules; permission checks |
| human approval | human review; manual approval; approval gate; human control |
| approval | authorization; consent; approval decision |
| additional approval | extra review; secondary approval; escalation approval |
| check | verify; inspect; screen; validate |
| filter | screen; moderate; block; sanitize |
| block | deny; reject; stop; prevent |
| reject | block; refuse; disallow; fail closed |
| allow | permit; authorize; pass; approve |
| deny | disallow; refuse; block; reject |
| input | user input; request; incoming content; prompt |
| inputs | requests; incoming requests; input content |
| output | generated result; answer; response; result |
| outputs | generated results; responses; answers |
| action | operation; tool action; proposed operation; side effect |
| actions | operations; capabilities; tool calls; side effects |
| proposed action | model proposal; candidate action; pending action |
| execute | carry out; perform; run; release |
| execute only if allowed | conditional execution; authorized execution; gated execution |
| allowed | permitted; authorized; approved; admissible |
| restrict actions | limit actions; constrain operations; cap capabilities |
| restrict access | enforce access boundaries; limit permissions; deny access |
| validate outputs | check generated results; output screening; verify output |
| output validation | result validation; output checking; output screening |
| unsupported claim | unsupported assertion; ungrounded claim; unsubstantiated statement |
| unsupported claims | ungrounded content; unsubstantiated claims; evidence-poor claims |
| unsafe request | risky request; harmful request; disallowed request |
| manipulative request | adversarial request; coercive request; control-bypassing request |
| sensitive action | high-risk action; consequential action; privileged action |
| large refund | high-value refund; substantial refund; consequential refund |
| high-value payment | large payment; consequential payment; high-value transaction |
| permission | authorization; access rule; allow/deny rule; entitlement |
| permission check | authorization check; access check; entitlement check |
| payment release | release of funds; financial execution; payment authorization |
| model can propose an action | model suggests an action; model generates a proposal; proposal stage |
| guardrail determines whether the system may continue | control gates continuation; guardrail gates execution; policy decides progression |
| guardrail vs guarantee | risk reduction versus certainty; control versus assurance |
| guarantee | certainty; absolute assurance; infallibility claim |
| improve safety | reduce risk; increase safety; strengthen controls |
| infallible | unable to fail; failure-proof; guaranteed safe |
| broader control concept | umbrella control; system-level control; composite control |
| specific rule | permission rule; allow/deny policy; action constraint |
| validation | rule checking; verification; conformance check |
| filters | input filters; content checks; screening controls |
| approval gates | review gates; authorization checkpoints; human gates |
| automated | machine-enforced; software-enforced; automatic |
| human-controlled | manually controlled; human-mediated; reviewer-controlled |
| Defense in depth | defense-in-depth; layered safety; layered defense; multiple controls |
| layered safety | defense in depth; layered controls; stacked safeguards |
| no single control | no one safeguard; multiple controls required; defense-in-depth principle |
| input check | request screening; input validation; input guardrail |
| screen the request | check the request; filter the request; inspect the prompt |
| system instruction | system prompt; safety instruction; behavior instruction |
| define safe behavior | specify safe behavior; set safety rules; establish safe operation |
| tool restriction | capability restriction; tool allowlist; tool denylist |
| limit capabilities | constrain tools; reduce affordances; limit operations |
| enforce access | apply authorization; enforce permissions; gate resources |
| check the result | validate output; inspect result; verify generated content |
| review when needed | escalate for review; require human review; review conditionally |
| Prompt Injection | prompt injection; prompt manipulation; instruction injection |
| Permissions & Safety | permissions and safety; access and safety; authorization and safety |
| Human in the Loop | human in the loop; human-in-the-loop; human oversight |
| Failure Handling | failure handling; error handling; failure response |
| Deployment Readiness | deployment readiness; release readiness; production readiness |
| Evaluation | evaluation; assessment; testing; measurement |
| visual explainer | visual explanation; explainer video; illustrated explanation |
| captions included | captioned; captions available; subtitles included |
| guardrail architecture | control architecture; safety architecture; guardrail flow |
| guardrail flow | control flow; safety flow; input-to-output flow |
| capability boundary | tool boundary; action boundary; affordance boundary |
| access boundary | permission boundary; resource boundary; authorization boundary |
| human review gate | approval gate; manual checkpoint; reviewer checkpoint |
| validation gate | output gate; rule-checking gate; conformance gate |

## Do Not Confuse Candidates

| Candidate A | Candidate B | Distinction suggested by the page |
|---|---|---|
| Guardrail | Guarantee | A guardrail reduces risk; a guarantee would mean failure cannot happen. |
| Guardrail | Permission | A guardrail is a broader control concept; a permission is a specific rule about what an action or resource allows. |
| Guardrail | Validation | Validation checks whether something meets defined rules; a guardrail may include validation plus permissions, filters, or approval gates. |
| Guardrail | Human approval | Guardrails can be automated or human-controlled; human approval is explicit review by a person and is one possible guardrail. |
| Guardrail | Control | A guardrail is a safety-oriented control; control is the broader generic word for a mechanism that changes system behavior. |
| Guardrail | Constraint | A constraint limits behavior; a guardrail is a broader system-control pattern that may combine many constraints. |
| Guarantee | Safety improvement | A safety improvement lowers risk but does not guarantee that failure is impossible. |
| Infallible | Safer | Infallible means unable to fail; safer means risk has been reduced. |
| Permission | Guardrail | Permission is a narrow allow/deny rule; guardrail can include permission but also validation, filtering, and review. |
| Permission | Authorization | Authorization is the decision or process of granting access; permission is the rule or entitlement being checked. |
| Permission | Authentication | Permission decides what an actor may do; authentication establishes or verifies identity. |
| Permission | Validation | Permission asks whether an action or resource is allowed; validation asks whether an item meets defined rules. |
| Access | Permission | Access is the ability to reach a resource; permission is the rule governing that access. |
| Access | Capability | Access concerns reaching a system or data; capability concerns what operation the system can perform. |
| Validation | Verification | Both check conformance, but validation is used here for defined rules on a result, while verification may be a broader checking term. |
| Validation | Approval | Validation can be automatic rule checking; approval is an explicit authorization decision, often by a person. |
| Validation | Review | Validation checks defined rules; review examines an action or result and may involve human judgment. |
| Input validation | Input filtering | Validation checks whether input meets rules; filtering may remove, block, or screen content. |
| Output validation | Output filtering | Output validation checks a generated result; filtering may block or transform content. |
| Output | Result | Output is what the system produces; result emphasizes the final outcome after processing or controls. |
| Output | Action | Output is a produced result; action is an operation the system proposes or performs. |
| Proposed action | Executed action | A proposed action is a model suggestion; an executed action has passed permission and other required controls. |
| Action | Tool | An action is what the system does; a tool is a capability used to perform an action. |
| Tool | Permission | A tool provides a capability; permission determines whether the capability or action may be used. |
| Tool control | Permission control | Tool control limits which operations can be called; permission control limits access to systems and data. |
| Tool restriction | Tool deletion | Tool restriction is the policy; deletion is one potentially restricted operation. |
| Search | Deletion | Search is a read/lookup capability in the example; deletion is a potentially destructive capability. |
| Agent | Model | An agent may select and call tools; a model is the underlying component producing interpretation, output, or proposals. |
| Agent | User | The agent is the AI actor; the user initiates the request or receives the result. |
| Human approval | Human in the loop | Human approval is one explicit review action; human-in-the-loop is a broader architecture pattern. |
| Human approval | Human review | Approval is a decision authorizing continuation; review is the examination that may precede that decision. |
| Human approval | Confirmation | Approval authorizes an action; confirmation may simply acknowledge or verify intent. |
| Human-controlled | Automated | Human-controlled guardrails depend on a person; automated guardrails are enforced by software logic. |
| Sensitive action | Large refund | A sensitive action is a broad category; a large refund is one concrete example. |
| Large refund | Any refund | The example uses a large refund to trigger review; not every refund necessarily has the same control. |
| Amount check | Permission check | Amount check evaluates the requested value; permission check evaluates whether the action is authorized. |
| Amount | Permission | Amount is a transaction field; permission is an authorization rule. |
| Refund | Payment release | A refund returns money; payment release authorizes a payment or release of funds. |
| High-value payment | Agent cannot release payment | High-value payment is a broad guardrail-trigger example; inability to release payment is a specific permission rule. |
| Block | Reject | Block stops input or an operation; reject declines a generated answer or result. |
| Reject | Refuse | Reject is a control decision against a result; refuse is a broader response behavior that may be user-visible. |
| Allow | Approve | Allow is permission to proceed; approve is an explicit authorization decision, often after review. |
| Deny | Reject | Deny concerns access or action authorization; reject concerns accepting a result or content. |
| Unsafe request | Manipulative request | Unsafe concerns risk of the request; manipulative concerns an attempt to influence or bypass the system. |
| Unsupported claim | Invalid format | Unsupported claim is a content/evidence problem; invalid format is a structural conformance problem. |
| Invalid behavior | Invalid output | Invalid behavior is broader system behavior; invalid output is one generated result that violates rules. |
| Input | Prompt injection | Input is any incoming request; prompt injection is a specific adversarial pattern in input. |
| Prompt injection | Manipulative request | Prompt injection is a named attack pattern; manipulative request is a broader example category. |
| System instruction | User input | System instruction defines expected behavior; user input supplies a request that must be handled under those instructions. |
| System instruction | System output | Instruction is a control specification; output is the generated result. |
| System instruction | Guarantee | An instruction defines intended behavior; it does not guarantee that the model cannot fail. |
| Defense in depth | Single control | Defense in depth uses multiple layers; a single control is only one layer and cannot handle every risk. |
| Layered safety | Safety guarantee | Layered safety reduces risk through multiple controls; it is not a guarantee of failure-free behavior. |
| Layer | Control | A layer is one control or group of controls in a layered design; control is the generic mechanism. |
| Input check | Output validation | Input check operates before model processing; output validation operates after generation. |
| Tool restriction | Permission enforcement | Tool restriction limits capabilities; permission enforcement applies access rules to available actions/resources. |
| Output validation | Human approval | Output validation is a rule check; human approval is explicit human review. |
| Human approval | Output validation | Human approval may review an action or result; output validation checks defined rules automatically or systematically. |
| Guardrail flow | Refund flow | Guardrail flow is the general architecture; refund flow is one concrete financial example. |
| Workflow | Flow | Workflow is the broader ordered process; flow is the visual sequence shown in the diagram. |
| Control point | Workflow stage | Control point emphasizes where a guardrail applies; workflow stage can be any stage, controlled or uncontrolled. |
| Control layer | Control point | A control layer is one defense mechanism; a control point is the location where a mechanism is applied. |
| Approval gate | Permission | Approval gate is a process checkpoint; permission is a rule defining what is allowed. |
| Approval gate | Validation gate | Approval gate requires authorization; validation gate checks conformance. |
| Risk reduction | Risk elimination | Guardrails reduce risk; they do not eliminate every possibility of failure. |
| Safety | Reliability | Safety concerns harmful or unacceptable behavior; reliability concerns dependable operation more broadly. |
| Safety | Validity | Safety concerns risk; validity concerns conformity to rules or format. |
| Failure Handling | Guardrails | Failure handling defines what happens after/during a failure; guardrails aim to prevent or constrain risky behavior before continuation. |
| Evaluation | Guardrails | Evaluation measures or judges behavior; guardrails control behavior during operation. |
| Deployment Readiness | Guardrails | Deployment readiness is a release decision; guardrails are controls used within the system. |
| Permissions & Safety | Guardrails | Permissions and safety are a related topic; guardrails are the broader control pattern explained here. |
| Video | Guardrail concept | Video is a media resource, not a safety mechanism, even though it explains controls and layers. |
| Captions | Output validation | Captions are video accessibility metadata, not validation of AI output. |
| H.264 | Guardrail | H.264 is a video codec, not an AI safety control. |
| AAC | Approval | AAC is an audio codec, not an authorization decision. |

## Notes

- The page’s core definition is: **guardrails are controls designed to reduce unsafe, unwanted, or invalid AI behavior**.
- The lede names four control operations: **check inputs**, **restrict actions**, **validate outputs**, and **require additional approval**.
- The architecture flow is: **User Input → Input Guardrail → Model → Proposed Action → Tool / Permission Control → Output → Output Validation → User / System**.
- **Human Approval** is shown as a conditional branch: it is used **when required**.
- The main control surfaces are **inputs, outputs, actions, and access**; the takeaway repeats these as the mechanism for reducing AI system risk.
- The five explicit guardrail types are **Input controls**, **Output controls**, **Tool controls**, **Permission controls**, and **Human approval**.
- The input-control example is to **block an unsafe or manipulative request**.
- The output-control example is to **reject an answer that contains unsupported claims**.
- The tool-control example is to **allow search but not deletion**.
- The permission-control example is to **deny payment release**.
- The human-approval example is to **approve a large refund**.
- The refund example’s visible sequence is **User → Check / Amount check → Control / Permission check → Review / Human approval → Result / Execute only if allowed**.
- The central action distinction is: **the model can propose an action; guardrails determine whether the system may continue**.
- The page explicitly distinguishes guardrails from **guarantees**, **permissions**, **validation**, and **human approval**.
- The page says guardrails improve safety but do not make an AI system **infallible**.
- The permission distinction uses **high-value payment requires control** as the broad guardrail example and **agent cannot release payment** as the narrow permission example.
- The validation distinction says validation checks whether something meets **defined rules**, while a guardrail may include **validation, permissions, filters, or approval gates**.
- The human-approval distinction says a guardrail can be **automated or human-controlled**, while human approval means a **person explicitly reviews an action**.
- The defense-in-depth layers are **Input Check**, **System Instruction**, **Tool Restriction**, **Permission**, **Output Validation**, and **Human Approval**.
- The explicit layer glosses are: **screen the request**, **define safe behavior**, **limit capabilities**, **enforce access**, **check the result**, and **review when needed**.
- The page’s defense-in-depth principle is: **No single control handles every risk**.
- Related concepts are **Prompt Injection**, **Permissions & Safety**, **Human in the Loop**, **Failure Handling**, **Deployment Readiness**, and **Evaluation**.
- The visible takeaway is: **Guardrails reduce AI system risk by constraining inputs, outputs, actions, and access**.
- The video metadata contributes **Independent explainer**, **visual explainer**, **captions included**, **controls · layers · approval**, and **MP4 · H.264 + AAC**; these are retained because the extraction scope includes the full visible body.
- The source does not provide numerical risk thresholds, permission schemas, validation schemas, approval criteria, guardrail performance metrics, or implementation code.
- The source does not define whether controls are deterministic, model-based, rule-based, policy-based, or external services; those implementation concepts remain potential missing concepts.
- Repeated labels, title-case labels, lowercase variants, singular/plural forms, hyphenated forms, workflow phrases, example phrases, media metadata, possible aliases, and confusable concepts are intentionally retained for later editorial deduplication.
