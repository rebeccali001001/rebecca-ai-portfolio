# Topic 11 · Permissions & Safety

## Topic Metadata

- **Module:** 11 · Evaluation, Safety & Reliability
- **Topic:** Permissions & Safety
- **Source page:** permissions-safety.html
- **Page title:** What Are Permissions in an AI System? · Permissions & Safety
- **Page description:** Permissions define what data, tools, systems, and actions an AI application or agent is allowed to access.
- **Page eyebrow:** 11 · Evaluation, Safety & Reliability
- **Extraction scope:** Full visible page body, including the title, ledes, on-page navigation, permission-check flow, Read / Write / Execute cards, least-privilege section, tool-access comparison, human-approval comparison, finance-agent example, layered-safety flow, “What it is NOT” comparisons, related concepts, takeaway, video metadata, and visible labels embedded in the page.
- **Collection policy:** Raw candidate inventory only. Keep technical terms, mechanisms, workflow nodes, decisions, actions, permissions, roles, controls, examples, metrics, abbreviations, important body words, aliases/synonyms, repeated labels, and potentially confusable concepts for later review. Candidates are intentionally broad, overlapping, and not deduplicated.

## Glossary Candidates

| Candidate | Category | Working definition / why it matters | Page evidence or context |
|---|---|---|---|
| Permissions & Safety | Core topic / title form | The topic combining authorization boundaries with controls that make AI behavior safer. | Page title |
| Permissions | Core concept / title form | Rules defining what an AI system is allowed to access and do. | Title; lede; takeaway |
| permission | Core concept | A rule or grant authorizing a specific access or action. | Repeated throughout page |
| permissioning | Process / candidate noun | The practice of defining and assigning permissions. | Candidate expansion of permission |
| permission rule | Authorization concept | A system rule deciding whether a requested operation is allowed. | Permission check; comparison cards |
| authorization | Alias / security concept | The decision about whether an identified actor may perform an operation. | Candidate synonym for permission |
| access authorization | Authorization concept | Authorization to use a resource or perform an action. | “allowed to access” |
| access control | Security control | Controls that restrict data, tools, systems, or actions. | Candidate broader term from boundaries |
| access policy | Policy concept | A policy specifying permitted and prohibited access or operations. | Permission rule context |
| AI system | System concept | The system whose capabilities and actions are constrained by permissions. | Lede; takeaway |
| AI application | System concept | An application that may access data, tools, systems, and actions. | Page description |
| application | System concept | Software that uses AI capabilities and may request access. | “AI application” |
| AI agent | Agent concept | An AI system that can propose or perform actions through tools and systems. | Lede; permission flow |
| agent | Actor / system | The actor that proposes an action and is subject to a permission check. | Flow label: AGENT |
| capable AI system | Capability concept | An AI system able to do more than it is authorized to do. | “capable AI system” |
| capability | Capability concept | What the AI system or a tool is technically able to do. | “Capability does not equal permission” |
| capability boundary | Security boundary | The practical distinction between what can be done and what may be done. | Capability/permission distinction |
| capability does not equal permission | Safety principle | Technical ability alone does not authorize an operation. | Note under permission flow |
| allowed to access | Authorization phrase | Describes access granted by permissions. | Page description |
| access | Security concept | Ability to view, change, trigger, or otherwise use a resource or operation. | Page description; least privilege |
| data | Resource category | Information an AI system may be allowed to read or change. | Page description |
| tool | Capability / component | A callable capability that can potentially be used by an agent. | Tool-access section; “What it is NOT” |
| tool access | Access concept | The fact that a tool exists and can potentially be used. | Permission vs Tool Access |
| tool availability | Capability state | A tool exists and is technically callable or exposed. | “A tool exists and can potentially be used” |
| callable capability | Tool concept | A tool or operation that can be invoked by a system. | “A tool is a callable capability” |
| system | Resource / environment | An external or internal system that an AI application or agent may access. | Page description |
| action | Operation concept | An operation proposed or performed by the agent. | Proposed action; layered safety |
| proposed action | Workflow node | The action presented to the permission check. | Permission flow |
| requested action | Workflow synonym | An action for which authorization is being evaluated. | Candidate alias for proposed action |
| operation | Action synonym | A specific thing a system or tool can perform. | “specific action”; operation examples |
| side effect | Action property | An external state change caused by executing an action. | Candidate implication of write/execute/send/pay |
| access and actions | Scope phrase | The combined resources and operations governed by permissions. | Takeaway |
| clear boundaries | Safety principle | Explicit limits within which a capable AI system must operate. | Second lede |
| boundary | Control concept | A limit on access, authority, or action. | “clear boundaries” |
| safety | Reliability / control concept | The property achieved by constraining and checking consequential behavior. | Title; layered safety |
| layered safety | Safety architecture | Safety produced by multiple controls in sequence. | Section heading |
| layered controls | Control architecture | Multiple independent or sequential restrictions and checks. | Layered Safety note |
| safety control | Control concept | A measure that limits, validates, reviews, or gates an action. | Candidate expansion of control |
| control | Safety mechanism | A restriction or check that reduces the chance of an unsafe action. | “layered controls” |
| boundary control | Authorization mechanism | A control that constrains the agent’s permitted behavior. | Candidate synthesis |
| restriction | Control mechanism | A limit placed on a tool, action, resource, or authority. | Tool Restriction layer |
| tool restriction | Safety layer | Limiting which tool operations can be used. | Layered-safety flow |
| validation | Safety layer | Checking that an action or its conditions satisfy requirements before execution. | Layered-safety flow |
| human approval | Oversight mechanism | A person reviews and approves a selected action. | Human Approval layer |
| human oversight | Oversight concept | Human involvement in reviewing or approving an action. | Candidate synonym for human approval |
| human intervention | Oversight concept | A person intervenes in the action path when required. | Candidate expansion of human approval |
| human-in-the-loop | Related concept / pattern | A design in which a person participates in decisions or actions. | Related concept: Human in the Loop |
| safety comes from layered controls | Safety principle | Trusting the model alone is insufficient; multiple controls provide safety. | Layered Safety note |
| trusting the model alone | Unsafe assumption | Treating model behavior as the only safety mechanism. | Layered Safety note |
| permission check | Core mechanism / workflow | A check that evaluates whether a proposed operation is allowed. | Section heading; flow |
| permission-check flow | Workflow | The sequence from agent to proposed action, permission check, and outcome. | Permission check card |
| check | Verification operation | Evaluate a requested operation against authorization rules. | Permission check |
| authorization check | Alias / mechanism | A check that decides whether an action is authorized. | Candidate synonym |
| policy check | Alias / mechanism | Evaluate a request against a policy. | Candidate synonym |
| policy decision | Decision concept | The result of evaluating whether a requested action meets policy. | Candidate expansion |
| access decision | Decision concept | Allow, block, or send a request for review. | Flow outcomes |
| agent → proposed action | Relationship / flow edge | The agent produces or presents a proposed operation. | Permission flow |
| proposed action → permission check | Relationship / flow edge | The proposed operation is evaluated by authorization logic. | Permission flow |
| permission check → outcome | Relationship / flow edge | The check produces an allowed, blocked, or review-required result. | Permission flow |
| allowed | Authorization outcome | The action satisfies the permission rule and can proceed. | Flow outcome |
| ALLOWED | Process label / outcome | Uppercase label for an action permitted to execute. | Permission-flow card |
| allow | Decision verb | Authorize an operation to proceed. | Candidate verb from ALLOWED |
| allowance | Authorization result | A grant that allows a requested action. | Candidate noun from allow |
| execute | Action / outcome | Perform the permitted operation. | “→ Execute” |
| execution | Action process | Carrying out the action after authorization. | Execute outcome |
| blocked | Authorization outcome | The proposed action is stopped because it is not allowed. | Flow outcome |
| BLOCKED | Process label / outcome | Uppercase label for an action that must stop. | Permission-flow card |
| block | Control verb | Prevent an unauthorized operation from proceeding. | Candidate verb from BLOCKED |
| stop | Safety outcome | Halt the proposed operation. | “→ Stop” |
| stopped action | Safety outcome | An action prevented before execution. | Candidate expansion |
| review required | Authorization outcome | The action cannot proceed automatically and requires a person’s decision. | Flow outcome |
| REVIEW REQUIRED | Process label / outcome | Uppercase label for a request that must receive human approval. | Permission-flow card |
| human approval required | Oversight condition | Approval is required before the action may proceed. | Flow outcome |
| escalation | Workflow outcome | Transfer a consequential or uncertain request to a person. | Candidate synonym for review required |
| approval gate | Control mechanism | A checkpoint that must be passed by human approval. | Candidate expansion |
| read | Operation / permission type | View or retrieve information without changing it. | Read / Write / Execute section |
| READ | Process label / permission type | Uppercase label for viewing information. | Permission check; R/W/E cards |
| reading | Operation form | Performing a read operation. | Candidate inflection |
| read access | Permission type | Permission to view information. | Least-privilege example |
| read permission | Permission type | Authorization to perform a read. | Candidate expansion |
| view information | Operation definition | The meaning of a read operation. | Read card |
| retrieve information | Operation synonym | Obtain information from a system or resource. | Candidate synonym for read |
| inspect information | Operation synonym | Examine information without changing it. | Candidate synonym for read |
| read invoice | Example action | View an invoice. | Read example; finance-agent CAN list |
| invoice | Data/resource example | A document or record that the agent may read. | Read example; finance agent |
| write | Operation / permission type | Change information in a system. | Read / Write / Execute section |
| WRITE | Process label / permission type | Uppercase label for changing information. | Permission check; R/W/E cards |
| writing | Operation form | Performing a write operation. | Candidate inflection |
| write access | Permission type | Permission to change stored information. | Candidate expansion |
| write permission | Permission type | Authorization to perform a write. | Candidate expansion |
| change information | Operation definition | The meaning of a write operation. | Write card |
| update information | Operation synonym | Modify existing information. | Candidate synonym for write |
| update CRM record | Example action | Change a customer or business record in a CRM. | Write example |
| CRM | Abbreviation / system | Customer relationship management system. | “CRM record” |
| CRM record | Data/resource example | A record that may be modified by a write operation. | Write example |
| execute | Operation / permission type | Trigger an external action. | Read / Write / Execute section |
| EXECUTE | Process label / permission type | Uppercase label for triggering an external action. | Permission check; R/W/E cards |
| execution permission | Permission type | Authorization to trigger an external action. | Candidate expansion |
| trigger an external action | Operation definition | The meaning of execute in the page’s three-way model. | Execute card |
| external action | Operation concept | An action that affects an outside system or recipient. | Execute card |
| send email | Example action | Trigger delivery of an email. | Execute example |
| email | Communication resource/action | A message that may be drafted or sent. | Tool-access note |
| release payment | Example action | Trigger a payment release. | Execute example; finance agent CANNOT list |
| payment | Financial action/resource | Money movement or payment operation. | Release payment |
| read / write / execute | Permission model | Three basic operation classes used to distinguish viewing, changing, and triggering. | Section heading |
| R/W/E | Abbreviation / permission model | Shorthand for Read, Write, and Execute. | Candidate abbreviation from section |
| read-only | Permission qualifier | Limited to viewing information without modifying or triggering actions. | Candidate derived from READ |
| write-capable | Permission qualifier | Able to change information. | Candidate derived from WRITE |
| executable | Permission qualifier | Able to trigger an operation. | Candidate derived from EXECUTE |
| least privilege | Core security principle | Give the AI only the access required for the task. | Section heading; definition |
| Least Privilege | Title-case concept | Title-case form of the principle limiting access to task needs. | Section heading |
| least-privilege principle | Alias / security principle | Same principle stated as a design rule. | Candidate variant |
| minimal access | Alias / security principle | Only the minimum permissions needed for a task. | Candidate synonym |
| minimum necessary access | Alias / security principle | Access restricted to what is needed to perform the task. | Candidate synonym |
| task-required access | Permission scope | Access that is necessary for the specified task. | Definition |
| required access | Permission scope | Access needed for the task to succeed. | “only the access required” |
| needed access | Permission scope / label | Access necessary for the current task. | NEEDED ACCESS card |
| NEEDED ACCESS | Process label / comparison | Uppercase label for permissions required by the task. | Least-privilege card |
| unneeded access | Permission scope / label | Access not necessary for the current task. | UNNEEDED ACCESS card |
| UNNEEDED ACCESS | Process label / comparison | Uppercase label for permissions beyond task needs. | Least-privilege card |
| over-privilege | Security risk | Granting more authority than a task needs. | Candidate implication of unneeded access |
| excessive privilege | Security risk | Permission scope that is broader than necessary. | Candidate synonym |
| privilege | Security concept | Granted authority to access resources or perform operations. | Least-privilege concept |
| access scope | Authorization concept | The set of resources and operations covered by a permission. | Candidate expansion |
| scope limitation | Control concept | Restricting permission to the smallest useful scope. | Candidate expansion |
| read policy | Example permission | Permission to read a policy document. | Needed access example |
| policy | Resource / rule | A policy document or authorization rule, depending on context. | Needed access; tool section |
| delete | Operation / permission type | Remove a record or resource. | Permission check; examples |
| DELETE | Process label / permission type | Uppercase label for removal. | Permission-check card |
| delete permission | Permission type | Authorization to remove information or a record. | Candidate expansion |
| delete invoice | Example action | Remove an invoice, listed as unnecessary access. | Unneeded access example |
| delete transaction | Example action | Remove a financial transaction. | Finance-agent CANNOT list |
| deletion | Operation form | The act of deleting a record or resource. | Candidate inflection |
| change bank account | Example action | Modify bank-account information, a high-consequence operation. | Unneeded access; finance agent CANNOT list |
| bank account | Financial resource | A sensitive financial record that should be tightly controlled. | Least-privilege example |
| specific action | Authorization unit | The individual operation whose permission is being decided. | Permission definition |
| specific permission | Authorization grant | A permission explicitly covering the proposed operation. | Finance example exception |
| specific permission + role + approval where required | Authorization condition | The combined conditions that may allow a sensitive operation. | Finance-agent note |
| role | Identity/authorization concept | A job or system role used to determine applicable authority. | Finance-agent note |
| role-based access | Candidate authorization model | Assigning permissions based on the agent or user role. | “role” in example; not defined |
| role assignment | Candidate authorization process | Associating a role with an agent or principal. | Candidate missing concept |
| permission assignment | Authorization process | Giving a principal or role permission to perform an operation. | Candidate missing concept |
| tool access vs permission | Core distinction | Tool availability does not itself grant authority to perform every action. | Section heading |
| Permission vs Tool Access | Comparison heading | Contrast between a callable tool and authorization to use it for an action. | Section heading |
| tool exists | Capability state | The tool is present and can potentially be called. | Tool-access definition |
| potentially be used | Capability phrase | A tool may be technically available but still not authorized. | Tool-access definition |
| permission determines | Authorization phrase | Permission decides whether a specific action is allowed. | Tool-access definition |
| specific action is allowed | Authorization condition | Authorization applies to an individual operation rather than merely a tool. | Tool-access definition |
| email tool | Tool example | A tool that can be used to draft or potentially send email. | Tool-access note |
| draft an email | Low-risk action | Prepare an email without necessarily sending it. | Tool-access note |
| draft | Non-side-effect action | Create a proposed message for review or later sending. | “may draft an email” |
| sending an email | Consequential action | Deliver a message externally. | Tool-access note |
| sending | External operation | The act of transmitting a prepared email. | Tool-access note |
| require permission | Authorization condition | Sending may be gated by a permission rule. | Tool-access note |
| require approval | Oversight condition | Sending may be gated by human review. | Tool-access note |
| permission vs human approval | Core distinction | A system authorization rule differs from a person reviewing an action. | Section heading |
| Permission vs Human Approval | Comparison heading | Contrast between automated authorization and human review. | Section heading |
| system authorization rule | Authorization concept | A rule enforced by the system to permit or deny an action. | Permission card |
| authorization rule | Alias / security concept | Rule controlling whether an action may occur. | Human-approval comparison |
| person reviews | Oversight action | A human examines a selected action. | Human Approval card |
| selected action | Review unit | The particular operation presented to a person for review. | Human Approval definition |
| refund | Financial action | A money-return action used to illustrate approval thresholds. | Refund example |
| propose refunds | Agent behavior | The agent may suggest or prepare refunds. | Approval note |
| proposed refund | Financial proposal | A refund action awaiting policy and/or approval. | “may propose refunds” |
| refund over $500 | Threshold condition | A refund exceeding a stated amount that requires manager approval. | Approval note |
| $500 | Numeric threshold / metric | Example monetary threshold for approval. | “Refunds over $500” |
| amount threshold | Approval control | A limit that determines when additional approval is needed. | Candidate expansion |
| manager approval | Human approval type | Approval by a manager for a higher-value refund. | Approval note |
| approval threshold | Governance concept | A value above which an action requires a designated approver. | Candidate synonym |
| approval | Oversight decision | A person’s decision to permit a selected action. | Human Approval; flow |
| approve | Oversight verb | Authorize an action after reviewing it. | Candidate verb from approval |
| manager | Approver role | The role of the person approving a high-value refund. | Approval example |
| AI Finance Agent | Real-example system | An AI agent whose invoice and payment capabilities are constrained. | Example heading |
| finance agent | Alias / domain system | Lowercase form of the AI Finance Agent example. | Example body |
| finance | Domain context | Financial workflow context for permission examples. | Finance-agent example |
| CAN | Capability/outcome label | Operations the finance agent may perform in the example. | Finance-agent card |
| CANNOT | Restriction/outcome label | Operations the finance agent may not perform by default. | Finance-agent card |
| can | Capability verb | Indicates an action available under the stated example policy. | CAN list |
| cannot | Restriction verb | Indicates an action outside default authority. | CANNOT list |
| check ERP | Example action | Inspect an enterprise resource planning system. | Finance-agent CAN list |
| ERP | Abbreviation / system | Enterprise resource planning system. | “check ERP” |
| enterprise resource planning | Abbreviation expansion | Business system category represented by ERP. | Candidate expansion |
| flag mismatch | Example action | Identify or mark a discrepancy. | Finance-agent CAN list |
| mismatch | Validation result | A discrepancy between expected or related financial information. | “flag mismatch” |
| discrepancy | Alias / validation concept | A mismatch or inconsistency to be flagged. | Candidate synonym |
| change bank account | Restricted financial action | Modify bank-account details, not allowed by default. | Finance-agent CANNOT list |
| release payment | Restricted financial action | Trigger payment release, not allowed by default. | Finance-agent CANNOT list |
| delete transaction | Restricted financial action | Remove a transaction, not allowed by default. | Finance-agent CANNOT list |
| unless | Exception condition | Introduces the conditions under which a normally disallowed action may proceed. | Finance-agent note |
| where required | Conditional approval phrase | Approval is needed only for operations subject to the requirement. | Finance-agent note |
| authorization exception | Governance concept | A case in which additional permission and approval permit a normally restricted operation. | Candidate expansion |
| actionable permission | Authorization concept | A permission tied to a concrete operation rather than generic tool access. | Candidate synthesis |
| layered permission model | Authorization architecture | Multiple stages restrict and validate an action before execution. | Layered Safety |
| agent capability | Capability layer | What the agent is technically able to do. | Layered-safety flow |
| AGENT CAPABILITY | Process label / layer | Uppercase label for the first safety layer. | Layered-safety card |
| tool restriction | Safety layer | Limit on which tool actions can be invoked. | Layered-safety flow |
| TOOL RESTRICTION | Process label / layer | Uppercase label for tool restriction. | Layered-safety card |
| PERMISSION | Process label / layer | Uppercase label for the authorization layer. | Layered-safety card |
| VALIDATION | Process label / layer | Uppercase label for pre-action validation. | Layered-safety card |
| HUMAN APPROVAL | Process label / layer | Uppercase label for human oversight. | Layered-safety card |
| ACTION | Process label / endpoint | Uppercase label for the final operation. | Layered-safety card |
| action pipeline | Workflow concept | Ordered path from capability through restrictions and checks to action. | Layered-safety flow |
| control layer | Safety architecture | One stage in a layered protection sequence. | Layered-safety flow |
| safety layer | Safety architecture | A distinct restriction, authorization, validation, or review stage. | Layered-safety flow |
| pre-action control | Control timing | A safeguard applied before the external action occurs. | Layered-safety sequence |
| action gate | Control mechanism | A condition that must pass before action execution. | Layered-safety sequence |
| final action | Workflow endpoint | The operation after all applicable controls. | Layered-safety flow |
| model alone | Safety boundary | The model’s own behavior, insufficient as the sole control. | Layered Safety note |
| permission ≠ tool | Distinction / warning | A tool is a callable capability; permission decides whether an action may use it. | “What it is NOT” |
| permission is not a tool | Negative definition | Permission authorizes; it is not the component that performs the operation. | Comparison card |
| permission ≠ guardrail | Distinction / warning | Permission authorizes access; a guardrail is broader and can control inputs, outputs, or actions. | “What it is NOT” |
| permission is not a guardrail | Negative definition | A permission rule is one authorization mechanism, not every safety control. | Comparison card |
| guardrail | Safety control concept | A broader control for inputs, outputs, or actions. | “What it is NOT” |
| guardrails | Plural / related concept | Multiple broader controls around model behavior. | Related concept link |
| input guardrail | Candidate guardrail type | A control applied to incoming requests or data. | “inputs” in guardrail definition |
| output guardrail | Candidate guardrail type | A control applied to generated outputs. | “outputs” in guardrail definition |
| action guardrail | Candidate guardrail type | A control applied to operations the system is about to perform. | “actions” in guardrail definition |
| permission ≠ human approval | Distinction / warning | Permission is a system rule; approval is a person reviewing a selected action. | “What it is NOT” |
| permission is not human approval | Negative definition | Automated authorization and human review are separate controls. | Comparison card |
| tool access ≠ unlimited authority | Distinction / warning | Having a tool does not permit every operation, record, amount, or recipient. | “What it is NOT” |
| unlimited authority | Authorization risk | Authority broad enough to cover every operation or target without restriction. | Comparison card |
| authority | Authorization concept | The effective power to perform operations on resources or recipients. | Unlimited-authority warning |
| operation scope | Permission boundary | Which operations a tool or agent may perform. | “every operation” |
| record scope | Permission boundary | Which records a tool or agent may access or change. | “every ... record” |
| amount scope | Permission boundary | Which monetary amounts an action may cover. | “every ... amount” |
| recipient scope | Permission boundary | Which people, accounts, or destinations an action may target. | “every ... recipient” |
| every operation | Overbroad scope candidate | Unrestricted operation set, explicitly denied by the comparison. | Tool-access warning |
| every record | Overbroad scope candidate | Unrestricted record access, explicitly denied by the comparison. | Tool-access warning |
| every amount | Overbroad scope candidate | Unrestricted financial amount, explicitly denied by the comparison. | Tool-access warning |
| every recipient | Overbroad scope candidate | Unrestricted target/recipient access, explicitly denied by the comparison. | Tool-access warning |
| related concepts | Navigation concept | Concepts linked to permissions and safety for further study. | Section heading |
| Tool Calling | Related concept / topic link | Calling an external tool or operation from an AI system. | Related-concepts chip |
| tool calling | Alias / related concept | Lowercase form of Tool Calling. | Related-concepts chip |
| Human in the Loop | Related concept / topic link | Human participation in an AI workflow. | Related-concepts chip |
| human in the loop | Alias / related concept | Lowercase form of Human in the Loop. | Related-concepts chip |
| Prompt Injection | Related concept / topic link | Attack or instruction-manipulation risk relevant to agent actions. | Related-concepts chip |
| prompt injection | Alias / related concept | Lowercase form of Prompt Injection. | Related-concepts chip |
| Failure Handling | Related concept / topic link | Handling behavior when an AI workflow fails or cannot safely act. | Related-concepts chip |
| failure handling | Alias / related concept | Lowercase form of Failure Handling. | Related-concepts chip |
| Deployment Readiness | Related concept / topic link | Readiness for safely deploying an AI system. | Related-concepts chip |
| deployment readiness | Alias / related concept | Lowercase form of Deployment Readiness. | Related-concepts chip |
| remember this | Takeaway label | Label introducing the concise summary. | Takeaway section |
| allowed to access and do | Takeaway phrase | Permissions govern both access and actions. | Takeaway |
| capability to do more | Takeaway phrase | The AI may be technically capable of more than it may perform. | Takeaway |
| independent explainer | Video metadata | Label for the planned explanatory video. | Video section |
| video | Media section / label | Placeholder section for a visual explainer. | Video section |
| visual explainer | Media metadata | Description of the planned video content. | Video section |
| permissions explainer | Candidate media topic | An explanatory video about permission boundaries. | Video caption context |
| topic | Navigation / metadata | The page’s subject area. | Title and metadata |
| module | Navigation / metadata | The larger instructional grouping containing the topic. | Eyebrow |
| Evaluation & Safety & Reliability | Module-family wording | The family named in the page eyebrow and parent navigation. | Page eyebrow / back link |
| evaluation | Related-domain term | Broader assessment context in which safety and permission controls may be considered. | Parent topic label |
| reliability | Related-domain term | Dependable operation context adjacent to safety. | Parent topic label |
| source page | Metadata term | The HTML page from which candidates were extracted. | Extraction metadata |
| page body | Extraction scope | All visible content read for candidate collection. | Extraction metadata |
| visible label | Extraction unit | A displayed heading, card label, chip, or workflow label retained as a candidate. | Extraction policy |

## Potential Missing Concepts

These concepts are suggested by the page’s wording, examples, distinctions, or control sequence but are not fully defined in the source body. Keep them as candidates for later glossary review rather than silently treating them as page definitions:

- **Role-based access control (RBAC)**, **attribute-based access control (ABAC)**, **access-control list (ACL)**, **policy-based access control**, and **policy engine**: the page mentions a role and system authorization rules but does not define authorization architectures.
- **Identity**, **principal**, **service account**, **authentication**, **identity provider**, and **delegation**: the page says “agent” and “role” but does not explain who is being authorized or how identity is established.
- **Resource-level permission**, **record-level access**, **field-level access**, **action-level authorization**, and **scope**: the page distinguishes operations, records, amounts, and recipients without formal granularity models.
- **Permission grant**, **permission request**, **permission inheritance**, **permission revocation**, **permission expiration**, **temporary permission**, and **delegated permission**: permission lifecycle is not described.
- **Default deny**, **deny by default**, **allowlist**, **blocklist**, **explicit deny**, and **policy precedence**: allowed/blocked outcomes are shown, but policy evaluation order is not defined.
- **Separation of duties**, **dual control**, **four-eyes principle**, **maker-checker**, and **independent approval**: the finance example suggests role separation and approval but does not define governance patterns.
- **Consent**, **user confirmation**, **manager approval workflow**, **approval routing**, **approver identity**, **approval expiry**, and **approval audit trail**: human approval is named but not operationalized.
- **Audit log**, **authorization log**, **decision log**, **action log**, **traceability**, and **non-repudiation**: the source gives no logging or accountability mechanism.
- **Policy enforcement point**, **policy decision point**, **policy administration point**, and **policy information point**: the permission-check architecture is shown as a flow but not decomposed into implementation roles.
- **Authentication vs authorization** and **identity vs permission**: the page uses authorization concepts without explaining these common distinctions.
- **Sandbox**, **sandboxing**, **capability security**, **object-capability model**, **process isolation**, and **network isolation**: boundary language suggests containment but does not define technical isolation.
- **Data minimization**, **purpose limitation**, **need-to-know**, **sensitive data**, **financial data**, **PII**, **secrets**, and **data classification**: the page mentions data and bank accounts but gives no information-classification model.
- **Data exfiltration**, **unauthorized disclosure**, **cross-tenant access**, **lateral movement**, and **privilege escalation**: risks implied by broad access are not named or explained.
- **Tool allowlist**, **tool denylist**, **tool registry**, **tool schema**, **tool capability declaration**, **tool selection policy**, and **tool-specific scope**: tool access is contrasted with permission, but tool governance is outside the page.
- **Argument validation**, **input validation**, **schema validation**, **output validation**, **recipient validation**, **amount validation**, and **field validation**: validation is one layer but its targets and rules are not specified.
- **Dry run**, **preview**, **simulation**, **draft mode**, **plan mode**, and **read-only mode**: drafting an email is contrasted with sending it, but no staged-execution pattern is defined.
- **Transaction limit**, **spending limit**, **rate limit**, **recipient allowlist**, **domain allowlist**, **amount cap**, and **velocity limit**: the refund threshold illustrates a limit but no general limit taxonomy is provided.
- **Step-up authentication**, **multi-factor authentication (MFA)**, **re-authentication**, and **high-risk action verification**: sensitive actions may require stronger controls, but none are defined.
- **Revocation**, **kill switch**, **emergency stop**, **circuit breaker**, **rollback**, and **safe shutdown**: the page says “stop” for blocked actions but does not define runtime interruption or recovery.
- **Idempotency**, **duplicate prevention**, **transactional safety**, **atomicity**, and **rollback safety**: external actions and payment release are shown without consistency or retry semantics.
- **Human-in-the-loop architecture**, **human-on-the-loop**, **human-over-the-loop**, **escalation policy**, and **manual fallback**: human approval is explicit, but oversight architectures are not distinguished.
- **Guardrail**, **policy guardrail**, **runtime guardrail**, **input guardrail**, **output guardrail**, and **action guardrail**: guardrail is described broadly but no taxonomy or enforcement point is given.
- **Prompt injection defense**, **instruction hierarchy**, **untrusted input**, **tool poisoning**, and **indirect prompt injection**: prompt injection is a related topic but not defined on this page.
- **Confused deputy**, **ambient authority**, **privilege creep**, **over-permissioning**, and **least-authority design**: the page’s capability/permission distinction suggests these security concepts without naming them.
- **Policy-as-code**, **authorization middleware**, **middleware enforcement**, **runtime authorization**, and **dynamic authorization**: the flow implies runtime checking but provides no implementation vocabulary.
- **Policy evaluation**, **policy decision latency**, **authorization failure**, **permission denied**, and **review queue**: outcomes are shown, but operational metrics and queues are not.
- **Risk tier**, **action criticality**, **high-impact action**, **consequential action**, and **irreversible action**: refunds, bank-account changes, payment release, and deletion are examples of differing consequence levels without a formal scale.
- **Reversibility**, **irreversibility**, **blast radius**, **impact assessment**, and **risk-based authorization**: the page uses examples with different consequences but does not define a risk model.
- **Recipient verification**, **account verification**, **bank-detail verification**, **invoice matching**, and **mismatch resolution**: the finance example names checking ERP and flagging mismatch but does not define the verification workflow.
- **Approval threshold**, **monetary threshold**, **$500 threshold**, **amount-based approval**, and **managerial approval**: one threshold is shown without a generalized threshold policy.
- **Monitoring**, **auditability**, **observability**, **alerting**, **incident response**, and **post-action review**: layered safety ends at action and does not describe after-action operations.
- **Security testing**, **permission testing**, **authorization testing**, **negative testing**, **abuse-case testing**, and **adversarial testing**: the page links to evaluation concepts but provides no test methodology.
- **Compliance**, **governance**, **separation of approval and execution**, **financial controls**, and **internal controls**: the finance example resembles governance controls but does not define a compliance framework.
- **Privacy**, **confidentiality**, **integrity**, **availability**, and **CIA triad**: data and action safety are discussed without formal security properties.
- **OAuth**, **OAuth scopes**, **API key**, **token**, **credential**, **secret management**, and **service-to-service authorization**: tools and external systems are named without authentication/credential mechanics.
- **API permission**, **endpoint authorization**, **HTTP method authorization**, and **transaction authorization**: read/write/execute resembles API operation classes but no protocol mapping is supplied.
- **Record deletion policy**, **payment release policy**, **bank-account change policy**, **email-send policy**, and **refund policy**: examples imply domain-specific policies without specifying their rules.
- **Capability discovery**, **tool discovery**, **tool catalog**, and **available action set**: the page says a tool exists but not how the agent learns what is available.
- **Action proposal**, **action plan**, **intent**, **request intent**, **policy-relevant attributes**, and **context-aware authorization**: proposed action is shown but intent/context extraction is not defined.
- **Human-readable approval prompt**, **approval evidence**, **approval rationale**, and **approval context**: the page does not explain what a person must review before approving.
- **False allow**, **false deny**, **overblocking**, **underblocking**, **authorization precision**, and **authorization recall**: no metrics are defined for permission decisions.
- **Permission drift**, **role drift**, **policy drift**, **stale permission**, and **access review**: ongoing maintenance of permissions is absent.
- **Access review**, **recertification**, **permission inventory**, and **entitlement review**: no lifecycle review process is given.
- **Delegated authority**, **on-behalf-of action**, **impersonation**, **agent identity**, and **principal-of-record**: the finance agent’s acting authority is not modeled.
- **Safe default**, **fail closed**, **fail open**, **uncertain authorization**, and **approval fallback**: blocked/review outcomes are shown but behavior under policy-service failure is not.
- **Unavailable policy service**, **timeout during authorization**, **authorization error**, and **policy evaluation failure**: no failure behavior for the check itself is provided.
- **Action confirmation**, **explicit confirmation**, **confirmation gate**, **user consent**, and **manager consent**: approval is named, but confirmation and consent are not distinguished.
- **Dry-run execution**, **transaction preview**, **human-readable diff**, and **change preview**: write/delete/change examples suggest safer previews but none are defined.
- **Data integrity**, **transaction integrity**, **payment integrity**, **record consistency**, and **reconciliation**: invoice mismatch is named without a formal integrity model.
- **Rollback**, **compensation action**, **undo**, **reversal**, and **refund reversal**: the page does not explain how to recover from an authorized but harmful action.

## Aliases / Synonyms

Keep these as separate raw candidates until the later glossary pass decides whether to merge them:

| Candidate | Possible alias/synonym relationship |
|---|---|
| Permissions | permission; access permissions; authorization permissions; permission rules |
| permission | authorization; authorization rule; access authorization; access grant |
| permission check | authorization check; access check; policy check; authorization decision |
| permissioning | access control; authorization management; permission management |
| access | permissioned access; authorized access; resource access |
| access control | authorization; permission control; access management |
| authorization | permission; access authorization; authority check |
| authorization rule | permission rule; access policy; policy constraint |
| AI system | AI application; AI agent system; intelligent system |
| AI application | AI system; AI product; application with AI capabilities |
| AI agent | agent; finance agent; autonomous agent (related, not identical) |
| agent | AI agent; acting system; automated actor |
| capability | ability; technical ability; callable capability |
| callable capability | tool; function; operation; callable tool |
| tool | callable capability; tool function; external capability |
| tool access | tool availability; tool exposure; callable-tool access |
| tool exists | tool is available; tool is exposed; capability is available |
| action | operation; requested operation; external operation; side-effecting operation |
| proposed action | requested action; candidate action; pending action; action proposal |
| operation | action; procedure; tool operation; command |
| execute | perform; trigger; run; invoke |
| execution | action execution; operation execution; invocation |
| read | view; retrieve; inspect; fetch |
| READ | read access; view permission; retrieve permission |
| read access | read permission; viewing authority; read-only permission |
| read invoice | view invoice; retrieve invoice; inspect invoice |
| write | change; update; modify; edit |
| WRITE | write access; change permission; update permission |
| write access | write permission; update authority; modification authority |
| update CRM record | modify CRM record; edit customer record; write CRM data |
| execute permission | action permission; invocation permission; run permission |
| delete | remove; erase; destroy (stronger/possibly different) |
| DELETE | deletion permission; remove permission; erase access |
| delete invoice | remove invoice; erase invoice; delete-record operation |
| least privilege | least authority; minimal privilege; minimum necessary access; need-to-know access |
| Least Privilege | least-privilege principle; least privilege principle |
| needed access | required access; necessary access; task-required access |
| unneeded access | unnecessary access; excess access; overbroad access |
| privilege | authority; entitlement; permission grant |
| over-privilege | over-permissioning; excessive privilege; excess authority; privilege creep |
| restriction | limit; constraint; boundary; control |
| tool restriction | tool constraint; tool permission limit; restricted tool access |
| validation | checking; verification; pre-action check; rule validation |
| human approval | manager approval; human review; manual approval; person’s authorization |
| approval | authorization; sign-off; consent; review decision |
| human review | human approval; manual review; person review; oversight |
| human oversight | human review; human control; manual supervision |
| review required | approval required; escalation required; human decision required |
| blocked | denied; refused; stopped; rejected |
| BLOCKED | deny; stop; reject; prevent |
| allowed | authorized; permitted; approved; accepted |
| ALLOWED | permit; authorize; allow |
| review required | human approval required; pending approval; manual gate |
| REVIEW REQUIRED | escalate; send for approval; hold for review |
| stop | halt; block; prevent; abort |
| guardrail | safety control; protective control; policy guardrail; runtime control |
| guardrails | safety controls; protective boundaries; constraints |
| input guardrail | input control; request filter; input policy |
| output guardrail | output filter; response control; output policy |
| action guardrail | action control; execution guard; operation policy |
| authority | permission; power; entitlement; effective access |
| unlimited authority | unrestricted authority; unbounded access; broad privilege |
| operation scope | action scope; allowed operations; operation boundary |
| record scope | record-level access; permitted records; data scope |
| amount scope | monetary scope; spending scope; transaction limit |
| recipient scope | target scope; destination allowlist; recipient restriction |
| role | actor role; job role; authorization role; system role |
| role-based access | RBAC; role-based authorization; role-scoped permission |
| finance agent | AI Finance Agent; financial AI agent; finance workflow agent |
| ERP | enterprise resource planning; ERP system; business resource system |
| check ERP | inspect ERP; read ERP; query enterprise system |
| flag mismatch | identify discrepancy; mark inconsistency; flag discrepancy |
| mismatch | discrepancy; inconsistency; reconciliation difference |
| change bank account | modify bank details; update account information; bank-detail change |
| release payment | authorize payment; trigger payment; disburse funds |
| delete transaction | remove transaction; erase financial record; transaction deletion |
| refund | repayment; money return; customer refund |
| refund over $500 | high-value refund; refund above threshold; thresholded refund |
| amount threshold | approval threshold; monetary limit; transaction threshold |
| manager approval | supervisory approval; managerial sign-off; approver review |
| specific permission | explicit permission; operation-specific authorization; scoped grant |
| specific permission + role + approval where required | permission-role-approval chain; multi-condition authorization; conditional authority |
| agent capability | model capability; agent ability; available agent operation |
| layered safety | defense in depth; layered controls; multi-layer safety |
| layered controls | defense in depth; sequential safeguards; control stack |
| safety layer | control layer; protection layer; safeguard stage |
| tool restriction → permission → validation → human approval | control chain; authorization pipeline; pre-action safety sequence |
| action | final action; authorized action; external side effect |
| Tool Calling | tool calling; tool use; function calling; function invocation |
| Human in the Loop | human-in-the-loop; human oversight; human review workflow |
| Prompt Injection | prompt injection; instruction injection; prompt-manipulation attack |
| Failure Handling | failure handling; error handling; failure response; recovery behavior |
| Deployment Readiness | deployment readiness; release readiness; production readiness |
| permissions define | permissions determine; permissions specify; permissions govern |
| access and do | access and act; view/change/trigger; use and operate |
| capability does not equal permission | ability is not authorization; tool access is not authority; can do is not may do |
| clear boundaries | explicit limits; defined boundaries; constrained authority |
| require permission | need authorization; need an access grant; be permission-gated |
| require approval | need human approval; be approval-gated; require sign-off |
| safety control | safeguard; protective mechanism; risk control |
| safe action | authorized action; approved action; validated action; acceptable action |

## Do Not Confuse Candidates

| Candidate A | Candidate B | Distinction suggested by the page |
|---|---|---|
| Permission | Tool | A permission is an authorization rule; a tool is a callable capability/component. |
| Permission | Tool access | Permission decides whether a specific action is allowed; tool access only means the tool exists and can potentially be used. |
| Permission | Tool availability | Availability is technical exposure; permission is authorization for an operation. |
| Permission | Capability | Capability describes what the system can technically do; permission describes what it may do. |
| Permission | Authority | Permission is a rule or grant; authority is the effective power resulting from applicable permissions and roles. |
| Permission | Guardrail | Permission authorizes access; a guardrail is a broader control for inputs, outputs, or actions. |
| Permission | Human approval | Permission is a system authorization rule; human approval is a person reviewing a selected action. |
| Permission | Role | A role can help determine permissions; a role is not itself the authorization decision. |
| Permission | Access | Access is the ability to use a resource; permission is the rule that grants or denies it. |
| Permission | Authentication | Permission/authorization decides what may be done; authentication establishes or verifies identity. |
| Permission | Consent | Permission is system authorization; consent is a person’s agreement and may not by itself implement access control. |
| Permission | Approval | Permission can be automatic policy authorization; approval is an explicit review/sign-off event. |
| Permission check | Validation | A permission check evaluates authorization; validation checks whether data, fields, or an action satisfy requirements. |
| Permission check | Human review | The check is a system step; human review is a person’s examination of a selected action. |
| Permission check | Policy evaluation | A permission check is the workflow event; policy evaluation is the logic/process used to reach the decision. |
| Allowed | Approved | Allowed can be the result of an automated rule; approved commonly denotes a human or governance decision. |
| Allowed | Executed | Allowed means the action may proceed; executed means the action was actually performed. |
| Blocked | Refused | Blocked emphasizes enforcement stopping an operation; refused may describe a response or decision. |
| Blocked | Failed | Blocked is an intentional authorization outcome; failed may mean the action attempted but did not succeed. |
| Review required | Blocked | Review required pauses for human decision; blocked stops the action without that path. |
| Review required | Allowed | Review required is conditional/pending; allowed means the authorization condition has passed. |
| Read | Write | Read views information; write changes information. |
| Read | Execute | Read retrieves information; execute triggers an external action. |
| Write | Delete | Write changes information generally; delete removes information and may require a distinct permission. |
| Execute | Write | Execute triggers an external action; write changes stored information. |
| Delete | Write | Delete is a removal operation; write is a broader modification class that may not include deletion. |
| Read-only | Least privilege | Read-only is one permission scope; least privilege is the principle of granting only task-required access, which may include write or execute. |
| Least privilege | No access | Least privilege grants necessary access; no access grants none, even when the task requires some. |
| Needed access | Unneeded access | Needed access is required for the task; unneeded access exceeds task requirements. |
| Minimal access | Insufficient access | Minimal access is sufficient task-scoped access; insufficient access prevents task completion. |
| Specific permission | Tool access | Specific permission authorizes a concrete action; tool access does not authorize every operation. |
| Specific permission | Unlimited authority | A specific grant is narrow; unlimited authority covers every operation, record, amount, or recipient. |
| Tool access | Unlimited authority | Having a tool does not permit every operation, record, amount, or recipient. |
| Tool | Action | A tool performs or exposes a capability; an action is the operation taken. |
| Tool | Permission | A tool is callable; permission governs whether it may be used for a particular action. |
| Email tool | Sending an email | The email tool is the capability; sending is one consequential operation that may require additional permission or approval. |
| Draft an email | Send an email | Drafting prepares content; sending transmits it externally. |
| Draft | Execute | A draft may be a reversible proposal; execute performs the external operation. |
| Action | Proposed action | An action is an operation; a proposed action is still awaiting permission, validation, or approval. |
| Proposed action | Executed action | A proposal is a candidate; an executed action has actually been performed. |
| Permission | Permission check | Permission is the rule/grant; the check is the event that evaluates the request against it. |
| Authorization | Human approval | Authorization may be decided by system policy; approval is a human review decision. |
| Human approval | Human-in-the-loop | Human approval is one explicit activity; human-in-the-loop is a broader architecture pattern. |
| Human approval | Human oversight | Approval is a particular decision; oversight includes monitoring, review, intervention, or approval. |
| Manager approval | User confirmation | Manager approval is a designated approver’s decision; user confirmation is agreement by the requesting user or affected user. |
| Approval threshold | Permission threshold | An approval threshold triggers human review; a permission threshold may directly allow/deny based on a value. |
| Role | Permission | A role is an identity/organizational attribute; permission is the operation grant or rule. |
| Role-based access | Least privilege | Role-based access is an assignment model; least privilege is the minimization principle that may constrain any model. |
| Guardrail | Permission | A guardrail may govern inputs, outputs, or actions broadly; permission specifically authorizes access/actions. |
| Input guardrail | Permission | An input guardrail filters requests/data; permission decides whether an operation is authorized. |
| Output guardrail | Permission | An output guardrail controls generated results; permission controls access or action authority. |
| Action guardrail | Permission | An action guardrail may validate or constrain behavior; permission is the authorization part of the control. |
| Validation | Permission | Validation checks data or action conditions; permission checks authority. |
| Validation | Approval | Validation may be automated; approval is a person’s review/decision. |
| Validation | Verification | Validation establishes compliance with requirements; verification can be broader confirmation that something is true. |
| Restriction | Permission | A restriction limits behavior; permission defines what is allowed, often as part of the restriction system. |
| Tool restriction | Tool access | Tool restriction limits use; tool access merely exposes the tool. |
| Layered safety | Model trust | Layered safety relies on multiple controls; trusting the model alone is explicitly insufficient. |
| Layered safety | Single control | Layered safety combines capability, tool restriction, permission, validation, and approval rather than relying on one control. |
| Safety | Security | Safety concerns preventing harmful or unacceptable actions; security is broader and includes confidentiality, integrity, and availability. |
| Safety control | Safety outcome | A control is a mechanism; a safety outcome is the resulting acceptable behavior. |
| Stop | Rollback | Stop prevents or halts a pending operation; rollback reverses a completed change. |
| Block | Revoke | Block denies a current request; revoke removes an existing grant or token. |
| Refund | Payment release | A refund returns money; releasing a payment sends or authorizes money to a recipient. |
| Refund over $500 | All refunds | The page gives a threshold for manager approval; it does not say that every refund requires manager approval. |
| Amount | Amount threshold | An amount is a value; a threshold is the rule/value that triggers a different control. |
| Check ERP | Read invoice | Checking ERP is a system inspection action; reading an invoice is a specific data item operation. |
| Mismatch | Error | A mismatch is a detected discrepancy; an error is a broader incorrectness or failure. |
| Flag mismatch | Resolve mismatch | Flagging identifies a discrepancy; resolving it is a subsequent action not defined by the page. |
| Bank-account change | Invoice read | Changing a bank account is a high-consequence write action; reading an invoice is a lower-risk read example. |
| Release payment | Draft email | Payment release has financial side effects; drafting email is preparatory and does not send it. |
| Delete transaction | Flag mismatch | Deleting removes a record; flagging marks a discrepancy without necessarily changing or removing it. |
| Action scope | Resource scope | Action scope limits operations; resource scope limits which data/records can be affected. |
| Record scope | Amount scope | Record scope limits which records; amount scope limits monetary value. |
| Amount scope | Recipient scope | Amount scope limits value; recipient scope limits destination/target. |
| Every operation | Specific operation | Every operation is unrestricted; a specific operation is narrow and explicitly scoped. |
| Every record | Specific record | Every record is broad access; a specific record is narrow data scope. |
| Every recipient | Approved recipient | Every recipient is unrestricted targeting; an approved recipient is allowlisted or validated. |
| Prompt injection | Permission | Prompt injection is an instruction-manipulation threat; permission is an authorization control that can constrain its effects. |
| Prompt injection | Prompting | Prompt injection is an attack pattern; prompting is the general act of giving instructions. |
| Failure handling | Permission check | Failure handling defines what happens after a failure; permission check decides whether an action may occur. |
| Deployment readiness | Permission | Deployment readiness is a release decision; permission is an access/action rule. |
| Tool Calling | Tool access | Tool calling is the act/mechanism of invoking a tool; tool access is availability/ability to potentially use it. |
| Tool Calling | Permission | Tool calling invokes a capability; permission determines whether a particular invocation is allowed. |
| Human in the Loop | Human approval | Human-in-the-loop is an architecture; human approval is one review event in that architecture. |
| Capability | Authority | Capability is technical ability; authority is permitted power. |
| Technical ability | Authorization | Technical ability says “can”; authorization says “may.” |
| Access | Action | Access concerns ability to use a resource; action is what is done with or through it. |
| Data | Tool | Data is a resource; a tool is a callable capability for operating on resources. |
| System | Resource | A system may contain or expose resources; a resource is the specific data/object being accessed. |

## Notes

- The visible permission-check sequence is: **AGENT → PROPOSED ACTION → PERMISSION CHECK → ALLOWED / BLOCKED / REVIEW REQUIRED**.
- The permission check explicitly asks: **READ? · WRITE? · DELETE? · SEND? · PAY?**.
- The visible outcome mapping is: **ALLOWED → Execute**, **BLOCKED → Stop**, and **REVIEW REQUIRED → Human Approval**.
- The page’s central principle is: **Capability does not equal permission**.
- The Read / Write / Execute model is: **READ = view information**, **WRITE = change information**, and **EXECUTE = trigger an external action**.
- The concrete operation examples are **read invoice**, **update CRM record**, **send email**, and **release payment**.
- The least-privilege definition is: **Give the AI only the access required for the task**.
- The least-privilege comparison lists needed access as **READ invoice** and **READ policy**, and unneeded access as **DELETE invoice**, **CHANGE bank account**, and **RELEASE payment**.
- The page explicitly distinguishes **tool access** from **permission**: a tool exists and can potentially be used, while permission determines whether a specific action is allowed.
- The email example distinguishes **drafting** from **sending**: the agent may draft an email, while sending may require permission or approval.
- The page explicitly distinguishes **permission** from **human approval**: permission is a system authorization rule, while approval is a person reviewing a selected action.
- The refund example introduces an amount condition: the agent may propose refunds, but **refunds over $500 require manager approval**.
- The real example is an **AI Finance Agent**. The agent can **read invoice**, **check ERP**, and **flag mismatch**.
- The finance agent cannot, by default, **change bank account**, **release payment**, or **delete transaction**.
- The exception phrase is: **specific permission + role + approval where required**.
- The layered-safety sequence is: **AGENT CAPABILITY → TOOL RESTRICTION → PERMISSION → VALIDATION → HUMAN APPROVAL → ACTION**.
- The page’s safety thesis is: **Safety comes from layered controls, not from trusting the model alone**.
- The “What it is NOT” comparisons are **Permission ≠ Tool**, **Permission ≠ Guardrail**, **Permission ≠ Human Approval**, and **Tool Access ≠ Unlimited Authority**.
- The tool-access warning is scoped across **operation**, **record**, **amount**, and **recipient**: having a tool does not permit every one of these.
- The related concepts are **Tool Calling**, **Guardrails**, **Human in the Loop**, **Prompt Injection**, **Failure Handling**, and **Deployment Readiness**.
- The takeaway is that permissions define what an AI system is allowed to access and do, even when it has the capability to do more.
- The page contains repeated title-case and uppercase labels intentionally retained as separate raw candidates: **Permissions**, **Least Privilege**, **READ**, **WRITE**, **EXECUTE**, **DELETE**, **SEND**, **PAY**, **ALLOWED**, **BLOCKED**, **REVIEW REQUIRED**, **CAN**, **CANNOT**, **AGENT CAPABILITY**, **TOOL RESTRICTION**, **PERMISSION**, **VALIDATION**, **HUMAN APPROVAL**, and **ACTION**.
- The page uses “permission” both as a general authorization concept and as a stage in a layered control sequence; later editorial work should decide whether to keep these senses together or split them.
- The page uses “tool access” as a broader availability concept and “permission” as an action-specific authorization concept; they are deliberately not collapsed here.
- The page uses “approval” as a human review condition, while “permission” is a system rule; these are deliberately retained as distinct concepts.
- The page does not define identity, authentication, roles beyond one finance example, policy syntax, permission storage, revocation, audit logs, or failure behavior when the permission check is unavailable.
- The page does not define formal authorization models such as RBAC, ABAC, ACLs, OAuth scopes, policy-as-code, or capability-based security; these are preserved under Potential Missing Concepts.
- The page does not define quantitative safety metrics. The only explicit numeric threshold is **$500** for the refund approval example.
- The page does not define implementation details for ERP integration, CRM integration, email APIs, payment systems, invoice data, or transaction stores.
- The page does not define whether **READ**, **WRITE**, **DELETE**, **SEND**, and **PAY** are mutually exclusive permission classes, nested operations, or illustrative checks; retain all interpretations for later review.
- The page does not define whether **REVIEW REQUIRED** results in a temporary hold, queue, or direct synchronous approval; it only maps the outcome to human approval.
- The page does not define whether a blocked action is logged, explained to the agent/user, retried, or escalated.
- The page does not define whether approval is one-time, reusable, scoped by amount/recipient, or revocable.
- The page does not define whether the finance agent is a user identity, service account, role, or application principal.
- The page does not define the relationship between a role and a specific permission; it only presents **role** as one condition in the finance-agent exception.
- The page does not define how mismatches are detected, what ERP fields are checked, or what happens after **flag mismatch**.
- The page does not define whether “release payment” means submitting, approving, or finalizing a payment; retain the phrase exactly as a raw candidate.
- The page does not define whether “change bank account” is a write action, an account-management action, or a separate high-risk category; retain the phrase and the operation variants.
- The video section contributes the visible labels **Independent explainer**, **Video**, and **visual explainer**; it is not used as a substitute for reading the HTML body.
- Repeated labels, singular/plural variants, title-case/uppercase forms, hyphenated forms, workflow phrases, example phrases, abbreviations, aliases, and possible confusions are intentionally retained for later editorial deduplication.
