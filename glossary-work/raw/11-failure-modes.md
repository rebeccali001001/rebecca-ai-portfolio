# Module 11 · Failure Modes

## Topic Metadata

- **Module:** 11 · Evaluation & Reliability
- **Topic:** Failure Modes
- **Topic position:** Topic 02
- **Source page:** `failure-modes.html`
- **Page title:** What are Failure Modes? · Evaluation & Reliability
- **Source description:** Failure modes are the ways an AI system can produce an incorrect, unsafe, or unusable result.
- **Extraction scope:** Full visible page body, including navigation labels, headings, definitions, explanatory paragraphs, analogy text, five process steps, real-world examples, explicit contrasts, related-concept tags, takeaway, and video labels.
- **Collection policy:** Raw candidate inventory only. Candidates are intentionally broad, overlapping, repeated, and not deduplicated. Keep technical terms, mechanisms, workflow nodes, metrics, abbreviations, important body words, aliases/synonyms, and potentially confusable concepts for later review.

## Glossary Candidates

| Candidate | Category | Working definition / why it matters | Page evidence or context |
|---|---|---|---|
| Failure Modes | Core topic | Recognizable ways an AI system can produce an unacceptable result. | Page title; eyebrow; related module |
| failure mode | Core concept | A specific way an AI system can fail or create an unacceptable result. | “What is it?” definition |
| failure modes | Plural / core concept | Multiple specific patterns by which a system can fail. | Hero and definition copy |
| AI system | System concept | The AI-based system whose behavior and risks are being analyzed. | Definition; lede |
| system failure | Failure concept | A failure of the AI system or its workflow that leads to an unacceptable result. | Definition paraphrase |
| fail | Operation / failure state | To produce an incorrect, unsafe, or unusable result. | Definition |
| failing | Alias / failure state | The system creating an unacceptable result. | “can fail” |
| unacceptable result | Quality/safety criterion | An output or action that cannot be accepted for the intended use. | Definition |
| incorrect result | Failure outcome | A result that is wrong or factually/instructionally incorrect. | Lede |
| unsafe result | Failure outcome | A result that creates or enables unacceptable safety risk. | Lede |
| unusable result | Failure outcome | A result that cannot be practically used for the intended purpose. | Lede |
| incorrect | Quality failure | Wrong or inaccurate relative to the request or required behavior. | Lede |
| unsafe | Safety failure | Likely to cause harm or violate safety expectations. | Lede |
| unusable | Utility failure | Not usable by the requester or downstream workflow. | Lede |
| ways | Failure taxonomy term | Different recognizable patterns in which a system can produce failure. | “ways an AI system can…” |
| produce | System operation | To generate a result, action, or output. | Lede; definition |
| result | Output concept | The outcome produced by the system, whether acceptable or not. | Lede; examples |
| examples | Evidence concept | Concrete instances used to name and test failure modes. | Definition section |
| hallucination | Failure mode | A generated claim or answer unsupported by reality or available evidence. | Explicit example list |
| omission | Failure mode | Failing to include required information, step, evidence, or constraint. | Explicit example list |
| unsafe action | Failure mode | An action taken or recommended by the system that creates unacceptable risk. | Explicit example list |
| wrong tool use | Failure mode | Using an incorrect tool, target, argument, or operation for the request. | Explicit example list |
| refusal | Failure mode | Declining to respond or act when refusal is not the intended behavior. | Explicit example list |
| bias | Failure mode | A systematic skew or unfairness in system outputs or decisions. | Explicit example list |
| timeout | Failure mode / metric | Failing to complete within an allowed time limit. | Explicit example list |
| invalid format | Failure mode | Returning output that does not satisfy the required structure or format. | Explicit example list |
| naming failure modes | Risk-analysis practice | Giving failures specific names so teams can test and control them. | Definition copy; takeaway |
| test | Verification operation | Examining a named failure mode with targeted cases. | “test and control” |
| control | Risk-reduction operation | A mechanism or process that reduces the likelihood or impact of a failure. | “test and control”; process step 5 |
| test and control | Risk-management pair | The linked practices of identifying failures, testing them, and reducing their risk. | Definition; takeaway |
| weak point | Risk-analysis concept | A vulnerable place in a machine or workflow where failure can occur. | Machine analogy |
| inspecting weak points | Analogy / analysis activity | Looking for vulnerable parts before an accident or system failure occurs. | “Think of it like…” |
| machine | Analogy subject | A physical system used as the analogy for an AI workflow. | Analogy lede |
| safety review | Review process | An examination of how a machine or system could fail before harm occurs. | Analogy paragraph |
| accident | Harm event | An undesirable event that a safety review tries to prevent. | Machine analogy |
| failure-mode analysis | Analysis method | Systematically asking how an AI workflow could fail, analogous to machine safety review. | Analogy paragraph |
| failure mode analysis | Alias / analysis method | Spaced-form name for failure-mode analysis. | Candidate alias |
| AI workflow | Workflow concept | The sequence of inputs, decisions, tools, and outputs being analyzed. | Analogy; process |
| workflow | Core workflow concept | An ordered set of steps through which an AI system produces a result or action. | Process; related tree |
| workflow step | Process unit | One stage of the workflow that can be mapped, tested, or controlled. | “each step” |
| map | Process step / operation | Describe the workflow and its inputs, decisions, tools, and outputs. | Step 1 |
| Map | Label variant | The first named process stage. | “1 · Map” |
| describe the workflow | Process operation | Documenting the structure of the AI workflow before analyzing failures. | Step 1 body |
| inputs | Workflow node | Information entering a workflow or one of its steps. | Step 1 body |
| input | Singular / workflow node | A specific piece of information supplied to the system. | Real-world examples |
| decisions | Workflow node | Choices made by the system or workflow. | Step 1 body |
| decision | Singular / workflow node | One choice point in the workflow. | Candidate from “decisions” |
| tools | Workflow component | External or internal capabilities the system may invoke. | Step 1; wrong tool use example |
| tool | Singular / workflow component | A callable capability used to perform an operation. | “wrong tool use” |
| outputs | Workflow node | Information or actions produced at the end of a workflow step or workflow. | Step 1 body |
| output | Singular / workflow node | A result produced by the system and delivered to a consumer. | Real-world examples |
| predict | Process step / operation | Anticipate possible ways each workflow step could go wrong. | Step 2 |
| Predict | Label variant | The second named process stage. | “2 · Predict” |
| list possible failures | Process operation | Enumerate failure candidates for each workflow step. | Step 2 body |
| possible failure | Failure-analysis unit | A failure that could occur at a workflow step, whether or not it has occurred yet. | Step 2 body |
| go wrong | Failure operation | Depart from the intended behavior or acceptable result. | “could go wrong” |
| each step | Scope unit | Every workflow stage considered during failure analysis. | Step 2 body |
| prioritize | Process step / operation | Rank failure risks so attention goes first to the most important ones. | Step 3 |
| Prioritize | Label variant | The third named process stage. | “3 · Prioritize” |
| assess risk | Risk-analysis operation | Evaluate failure risk using likelihood, impact, and detectability. | Step 3 body |
| risk | Core reliability concept | The possibility and significance of a failure. | Step 3 body; examples |
| likelihood | Risk metric/dimension | How likely a failure is to occur. | Step 3 body |
| impact | Risk metric/dimension | The consequence or severity if a failure occurs. | Step 3 body |
| detectability | Risk metric/dimension | How readily a failure can be noticed or detected. | Step 3 body |
| likelihood, impact, and detectability | Risk-assessment dimensions | The three dimensions explicitly named for assessing risk. | Step 3 body |
| test | Process step / operation | Run cases designed to expose or measure a failure mode. | Step 4 |
| Test | Label variant | The fourth named process stage. | “4 · Test” |
| run cases | Testing operation | Execute targeted examples against the system. | Step 4 body |
| case | Test unit | A targeted example or scenario used in testing. | “Run cases” |
| test case | Testing concept | A designed input/scenario used to test expected or failure behavior. | Related concept tree |
| targeted examples | Testing method | Examples selected to probe a particular failure mode. | Step 4 body |
| monitoring | Reliability operation | Observe system behavior over time to detect failures or changes. | Step 4 body |
| monitor | Verb / reliability operation | Observe a system or result for failure signals. | Candidate from “monitoring” |
| control | Process step / operation | Add measures that reduce the risk created by a failure. | Step 5 |
| Control | Label variant | The fifth named process stage. | “5 · Control” |
| reduce the risk | Risk-treatment operation | Lower the chance or consequence of an unacceptable failure. | Step 5 body |
| validation | Control mechanism | Check that inputs, outputs, fields, or actions satisfy requirements. | Step 5 body; wrong tool example |
| fallback | Control mechanism | A safe alternative path used when the primary path fails or is uncertain. | Step 5 body |
| review | Control mechanism / human process | Have a person or review process inspect a result or action. | Step 5; example output |
| limits | Control mechanism | Bound what the system can do or accept to reduce risk. | Step 5 body |
| risk reduction | Safety practice | The act of lowering the likelihood, impact, or overall exposure of failures. | “Reduce the risk” |
| Business example | Example category | The first real-world example category on the page. | Examples section |
| Missing evidence | Example / failure theme | A question lacks a matching source, so the system should not fabricate an answer. | Business example heading |
| missing evidence | Failure condition | Evidence required to support an answer is absent or insufficient. | Business example |
| evidence | Grounding/reliability concept | Source material used to support or validate an answer. | Business example |
| source | Evidence concept | A reference or information source that may match a question. | Business example |
| matching source | Evidence condition | A source relevant enough to support the question. | Business example input |
| question | Workflow input | A request for information or action sent to the system. | Business example input |
| no matching source | Evidence condition | The system cannot identify a source supporting the question. | Business example input |
| detects weak evidence | System behavior | Recognizes that available evidence is insufficient or unreliable. | Business example system |
| weak evidence | Evidence-quality condition | Evidence that is insufficiently relevant, reliable, or strong. | Business example system |
| asks for clarification | Safe system behavior | Requests more information instead of inventing an answer. | Business example system |
| clarification | Interaction operation | Additional information requested to resolve an underspecified question. | Business example system |
| no fabricated answer | Safe output | The system avoids inventing a response when evidence is inadequate. | Business example output |
| fabricated answer | Failure outcome | An invented answer presented as though it were supported. | Business example output |
| fabricate | Failure operation | Invent information rather than acknowledge missing or weak evidence. | “no fabricated answer” |
| AI product example | Example category | The second real-world example category on the page. | Examples section |
| Wrong tool action | Example / failure theme | An ambiguous data-update request could cause the wrong tool action. | AI product example heading |
| wrong tool action | Failure outcome | An incorrect tool-mediated action performed on data or another system. | AI product example |
| ambiguous request | Input-quality condition | A request with multiple plausible interpretations or insufficient specificity. | AI product example input |
| update data | Requested operation | Change stored or managed data in response to a request. | AI product example input |
| ambiguous request to update data | Risky input | An underspecified request that could lead to an unintended data change. | AI product example input |
| validates fields | Control behavior | Checks required data fields before taking an update action. | AI product example system |
| fields | Data structure concept | Individual data values or attributes that must be checked. | AI product example system |
| requires confirmation | Control behavior | Requires explicit approval before performing an ambiguous or consequential action. | AI product example system |
| confirmation | Human/control mechanism | Explicit acknowledgement that an action should proceed. | AI product example system |
| safe action | Acceptable output/action | An action that passes validation and meets safety requirements. | AI product example output |
| human review | Human control | A person examines or approves a result/action. | AI product example output |
| human | Oversight actor | The person who may review or confirm a system action. | “human review” |
| action | Workflow output/operation | An operation taken by the system, especially through a tool. | Unsafe action; safe action |
| data update | Operation | Changing data through a validated tool action. | AI product example |
| Failure Mode ≠ Failure Handling | Explicit distinction | Failure mode describes how failure can occur; failure handling specifies what happens next. | “What it is NOT” |
| failure handling | Related concept | The response or next-step policy used after a failure or error condition. | Explicit contrast; related chip |
| how the system can fail | Failure description | Describes the failure pattern itself. | Failure mode contrast |
| what the system should do next | Handling policy | Defines the response after a failure condition is recognized. | Failure handling contrast |
| next step | Handling concept | The action taken after detecting a failure. | Failure handling contrast |
| Failure Mode ≠ Random Mistake | Explicit distinction | A failure mode is a recognizable risk pattern, not merely an isolated mistake. | “What it is NOT” |
| random mistake | Confusable concept | An error that may not reveal a repeatable cause or pattern. | Explicit contrast |
| recognizable pattern | Failure-analysis property | A repeatable or identifiable pattern of risk. | Random mistake contrast |
| repeatable cause | Causality property | A cause that can recur and explain a recognizable failure pattern. | Random mistake contrast |
| Failure Mode ≠ Bug Only | Explicit distinction | A failure mode can arise from model, data, process, or integration, not only code defects. | “What it is NOT” |
| bug | Confusable concept | One possible implementation defect that may produce a failure. | Explicit contrast |
| bug only | Narrow failure framing | Treating every failure mode as merely an implementation bug. | Explicit contrast |
| implementation defect | Software failure concept | A defect in implementation that can be one source of a failure mode. | Bug contrast |
| model failure | Failure source | Failure originating in model behavior or limitations. | Bug contrast |
| data failure | Failure source | Failure originating in missing, poor, or problematic data. | Bug contrast |
| process failure | Failure source | Failure originating in workflow or operating procedure. | Bug contrast |
| integration failure | Failure source | Failure originating at the boundary between components or systems. | Bug contrast |
| model, data, process, or integration | Failure-source categories | The page names four broad origins of failure modes. | Bug contrast |
| related concepts | Concept navigation | Concepts connected to failure modes in the page’s learning path. | Related section |
| concept tree | Relationship model | A compact chain connecting workflow, failure mode, test case, control, and monitored result. | Related section |
| Workflow → Failure Mode → Test Case → Control → Monitored Result | Explicit relationship chain | The page’s end-to-end risk-analysis relationship. | Related section |
| monitored result | Observed outcome | A result watched after testing or control is applied. | Concept tree |
| evaluation | Related concept | Assessing system behavior against expected criteria. | Related-concept chip |
| functional tests | Related concept | Tests of whether intended functions work correctly. | Related-concept chip |
| Functional Tests | Label variant | Title-case linked concept label. | Related-concept chip |
| deployment readiness | Related concept | Whether a system is ready to operate safely and reliably in deployment. | Related-concept chip |
| Deployment Readiness | Label variant | Title-case linked concept label. | Related-concept chip |
| Failure Handling | Label variant | Title-case linked concept label. | Related-concept chip |
| remember this | Takeaway label | Section containing the page’s summary principle. | Takeaway heading |
| risks specific enough to test and control | Takeaway principle | Naming failures makes risks concrete enough for verification and mitigation. | Takeaway note |
| specific | Risk-analysis property | Defined narrowly enough to be tested and controlled. | Takeaway |
| reliable | Quality/reliability descriptor | Implied quality goal of evaluation and reliability work. | Module label; page theme |
| evaluation | Module concept | The broader discipline that tests or assesses AI behavior. | Eyebrow; related chip |
| reliability | Module concept | The broader goal of dependable, acceptable system behavior. | Eyebrow; page theme |
| independent explainer | Video label | Label for the video resource in the page body. | Video section |
| visual explainer | Video description | Description of the video content format. | Video section |
| video | Media/resource concept | The explainer resource attached to the topic page. | Video heading |
| topic | Information architecture term | A page-level learning unit in the module. | Metadata; video/page structure |
| module | Information architecture term | A group of related topics, here Evaluation & Reliability. | Eyebrow |
| Evaluation & Reliability | Module name | The module containing Failure Modes. | Eyebrow; page title |
| What is it? | Section label | Definition section introducing the core concept. | On-page navigation; heading |
| Think of it like... | Section label | Analogy section for explaining failure-mode analysis. | On-page navigation; heading |
| How it works | Section label | Process section presenting the five-step method. | On-page navigation; heading |
| Real-world examples | Section label | Examples section grounding the concept in business and product scenarios. | On-page navigation; heading |
| What it is NOT | Section label | Misconception and distinction section. | On-page navigation; heading |
| Related concepts | Section label | Navigation section for adjacent concepts. | On-page navigation; heading |
| Remember this | Section label | Takeaway section. | On-page navigation; heading |
| Video | Section label | Media section. | On-page navigation; heading |
| definition | Content role | The precise explanation of a concept or term. | Definition card/class and section |
| analogy | Content role | A mental model used to make failure analysis understandable. | Analogy card/class |
| process | Content role | Ordered method for mapping, predicting, prioritizing, testing, and controlling failures. | Process card/class |
| examples | Content role | Concrete scenarios illustrating safe handling of failure risks. | Example card/class |
| comparison | Content role | Explicit contrast between related but different concepts. | “What it is NOT” card/class |
| takeaway | Content role | Short summary principle to retain. | “Remember this” |
| risk pattern | Alias / failure concept | A recognizable pattern of risk that can be named and tested. | Random mistake distinction |
| unacceptable outcome | Alias / failure outcome | Another formulation of an output or action that cannot be accepted. | Definition and lede |
| unsafe behavior | Alias / safety failure | System behavior that can lead to an unsafe result or action. | Candidate derived from unsafe action/result |
| unsupported answer | Alias / evidence failure | An answer not backed by a matching or sufficiently strong source. | Missing evidence example |
| evidence gap | Alias / evidence failure | A lack of source support for a question or answer. | Missing evidence example |
| tool misuse | Alias / tool failure | Wrong or inappropriate use of a tool. | Wrong tool use |
| incorrect tool selection | Alias / tool failure | Selecting a tool that does not fit the request. | Wrong tool action/use |
| format violation | Alias / output failure | Output not conforming to the required format. | Invalid format |
| refusal error | Alias / behavior failure | Refusing when the intended response was to answer or act safely. | Refusal |
| bias pattern | Alias / fairness failure | A recognizable systematic bias in system behavior. | Bias |
| deadline breach | Alias / timing failure | Missing the allowed completion time, represented by timeout. | Timeout |
| safety control | Alias / control concept | Validation, fallback, review, or limits used to reduce risk. | Step 5 |
| mitigation | Potential alias / control concept | An intervention that reduces failure likelihood or impact. | Implied by “reduce the risk”; not named |
| guardrail | Potential alias / control concept | A boundary or rule limiting unsafe behavior. | Implied by controls/limits; not named |
| human-in-the-loop | Potential related oversight concept | Human participation in confirmation or review. | Implied by human review/confirmation; not named |
| root cause | Potential missing analysis concept | Underlying cause of a recognizable failure pattern. | Related to repeatable cause; not named |
| severity | Potential missing risk metric | Degree of harm or consequence, related to impact. | Risk language; not named |
| frequency | Potential missing risk metric | How often a failure occurs, related to likelihood. | Risk language; not named |
| observability | Potential missing reliability concept | Ability to understand and detect behavior through monitoring. | Monitoring/detectability language; not named |
| detection | Potential alias / reliability operation | Recognizing that a failure or weak condition has occurred. | Detectability; detects weak evidence |
| prevention | Potential missing control concept | Preventing a failure before it occurs. | Safety review/control language; not named |
| recovery | Potential missing handling concept | Returning to a safe state after failure. | Fallback/failure handling language; not named |
| graceful degradation | Potential missing control concept | Continuing with reduced capability when the ideal path is unavailable. | Fallback/limits language; not named |
| clarification request | Alias / safe interaction | A request for additional information when evidence or intent is insufficient. | Asks for clarification |
| confirmation gate | Alias / control mechanism | A required approval checkpoint before a consequential action. | Requires confirmation |
| field validation | Alias / validation mechanism | Checking data fields before executing an update. | Validates fields |
| source matching | Alias / evidence mechanism | Finding a source that matches the question. | No matching source |
| targeted test | Alias / testing concept | A test case designed around a particular failure mode. | Targeted examples |
| risk prioritization | Alias / process concept | Ranking risks using likelihood, impact, and detectability. | Prioritize / assess risk |
| workflow mapping | Alias / process concept | Describing inputs, decisions, tools, and outputs in sequence. | Map step |
| failure identification | Alias / process concept | Naming possible failures at each workflow step. | Predict step |
| control design | Alias / process concept | Selecting validation, fallback, review, or limits to reduce risk. | Control step |
| post-deployment monitoring | Potential missing operations concept | Monitoring behavior after a system is in use. | Monitoring; deployment readiness; not named |
| operational risk | Potential alias / risk concept | Risk arising from how a workflow operates, including process and integration. | Model/data/process/integration distinction |
| model risk | Potential alias / risk concept | Risk arising from limitations or behavior of the model. | Model as failure source |
| data risk | Potential alias / risk concept | Risk arising from data quality, completeness, or availability. | Data as failure source |
| process risk | Potential alias / risk concept | Risk arising from workflow or procedure design. | Process as failure source |
| integration risk | Potential alias / risk concept | Risk arising at a component/system boundary. | Integration as failure source |

## Potential Missing Concepts

These concepts are suggested by the page’s wording, workflow, or distinctions but are not fully defined in the source body. Keep them as candidates for later glossary review rather than silently treating them as page definitions:

- **Root-cause analysis**, **root cause**, and **causal factor**: the page asks for recognizable/ repeatable causes but does not provide a cause-analysis method.
- **Severity**, **frequency**, and **risk score**: impact and likelihood are named, but no scoring scale or aggregation rule is provided.
- **Detection rate**, **false positive**, **false negative**, and **detectability score**: detectability is named without operational metrics.
- **Prevention**, **mitigation**, **recovery**, **graceful degradation**, and **fail-safe behavior**: controls are named, but their lifecycle or design patterns are not explained.
- **Observability**, **logging**, **tracing**, **alerting**, and **incident response**: monitoring is named, but the mechanisms for detecting and responding to failures are not.
- **Human-in-the-loop**, **approval gate**, **escalation**, and **manual fallback**: human review and confirmation are shown, but the oversight architecture is not defined.
- **Input validation**, **schema validation**, **output validation**, **format checking**, and **contract testing**: validation is named broadly without implementation detail.
- **Grounding**, **citation**, **source attribution**, **evidence threshold**, and **abstention**: missing/weak evidence is illustrated, but these reliability techniques are not defined.
- **Ambiguity detection**, **intent disambiguation**, and **clarification policy**: clarification is shown for missing evidence and ambiguous requests, but no decision rule is given.
- **Tool selection**, **tool permissions**, **argument validation**, **side-effect control**, and **idempotency**: wrong tool use/action is illustrated, but tool-call safeguards are not expanded.
- **Hallucination rate**, **omission rate**, **refusal rate**, **unsafe-action rate**, **format-validity rate**, and **timeout rate**: failure types are listed, but no metrics are defined.
- **Test coverage**, **edge case**, **adversarial case**, **regression test**, **scenario testing**, and **red teaming**: targeted examples are requested, but test strategy is not described.
- **Failure taxonomy**, **failure catalog**, **risk register**, and **failure-mode inventory**: naming is encouraged, but no documentation structure is specified.
- **FMEA / Failure Mode and Effects Analysis**, **fault tree analysis**, and **hazard analysis**: the machine/safety analogy suggests these families, but none is named in the source.
- **Model failure**, **data failure**, **process failure**, **integration failure**, and **implementation defect**: sources are named at a high level without diagnostic criteria.
- **Reliability requirement**, **acceptance criterion**, **safety requirement**, and **quality threshold**: “acceptable” is central, but thresholds are not defined.
- **Timeout budget**, **latency**, **deadline**, **retry**, **backoff**, and **circuit breaker**: timeout is listed, but timing and recovery controls are not explained.
- **Deployment monitoring**, **production incident**, **rollback**, **versioning**, and **change management**: deployment readiness is linked, but operational lifecycle is outside the page’s scope.

## Aliases / Synonyms

Keep these as separate raw candidates until the later glossary pass decides whether to merge them:

| Candidate | Possible alias/synonym relationship |
|---|---|
| Failure Mode | failure mode; failure modes; risk pattern; recognizable pattern of risk |
| Failure Modes | failure mode; failure-mode analysis subject; system failure patterns |
| failure-mode analysis | failure mode analysis; failure analysis; inspecting weak points |
| unacceptable result | unacceptable outcome; incorrect/unsafe/unusable result |
| incorrect result | wrong result; inaccurate result |
| unsafe result | unsafe outcome; unsafe behavior |
| unusable result | unusable output; unusable outcome |
| hallucination | fabricated answer; unsupported answer; evidence failure |
| omission | missing information; missing required content |
| unsafe action | unsafe behavior; harmful action; risky tool action |
| wrong tool use | tool misuse; incorrect tool selection; wrong tool action |
| refusal | refusal error; unwanted refusal |
| bias | bias pattern; systematic unfairness |
| timeout | timing failure; deadline breach |
| invalid format | format violation; malformed output |
| workflow | AI workflow; process; workflow path |
| map | workflow mapping; describe the workflow |
| predict | failure identification; list possible failures |
| prioritize | risk prioritization; assess risk |
| test | run cases; targeted testing; test case execution |
| control | safety control; mitigation; risk reduction |
| risk | operational risk; failure risk; risk exposure |
| likelihood | probability; frequency (possible but not identical) |
| impact | consequence; severity (possible but not identical) |
| detectability | ease of detection; detection capability |
| validation | field validation; input/output checking; format checking |
| fallback | safe alternative; manual fallback; recovery path |
| review | human review; oversight; approval review |
| limits | boundaries; constraints; guardrails |
| evidence | source support; supporting evidence; grounding material |
| weak evidence | insufficient evidence; low-confidence evidence; evidence gap |
| matching source | relevant source; source match; supporting source |
| clarification | clarification request; disambiguation request; request for more information |
| confirmation | approval; confirmation gate; explicit acknowledgement |
| fields | data fields; attributes; input fields |
| safe action | approved action; validated action; acceptable action |
| human review | human oversight; manual review; human-in-the-loop (related, not strictly identical) |
| failure handling | response to failure; next-step policy; recovery behavior |
| random mistake | isolated error; non-repeatable error; accidental mistake |
| bug | implementation defect; software defect |
| model failure | model-originated failure; model risk |
| data failure | data-originated failure; data risk |
| process failure | workflow failure; process risk |
| integration failure | boundary failure; integration risk |
| test case | case; targeted example; test scenario |
| monitored result | observed result; monitored outcome; post-test result |
| evaluation | assessment; testing; quality evaluation |
| functional tests | functional testing; function tests |
| deployment readiness | release readiness; production readiness |
| naming failure modes | failure cataloging; failure inventory; risk naming |
| reduce the risk | mitigate risk; lower risk; risk treatment |
| detects weak evidence | recognizes insufficient evidence; evidence-quality detection |
| asks for clarification | requests clarification; seeks more information |
| validates fields | checks fields; performs field validation |
| requires confirmation | gates action on approval; requests explicit confirmation |

## Do Not Confuse Candidates

| Candidate A | Candidate B | Distinction suggested by the page |
|---|---|---|
| Failure mode | Failure handling | A failure mode describes how the system can fail; failure handling defines what the system should do next. |
| Failure mode | Random mistake | A failure mode is a recognizable pattern of risk; a random mistake may not reveal a repeatable cause. |
| Failure mode | Bug | A failure mode can come from model, data, process, or integration; a bug is one possible implementation defect. |
| Failure mode | Failure outcome | A failure mode is the pattern/mechanism; the outcome is the resulting incorrect, unsafe, or unusable result. |
| Failure mode | Risk | A failure mode is a specific named pattern; risk is the broader possibility/significance of that failure. |
| Failure mode | Error | Error is a broad incorrectness term; the page uses failure mode for a recognizable, analyzable risk pattern. |
| Failure-mode analysis | Safety review | The analogy connects them, but safety review examines a machine while failure-mode analysis applies the same question to an AI workflow. |
| Failure-mode analysis | Testing | Analysis identifies and prioritizes possible failures; testing runs cases against them. |
| Failure-mode analysis | Failure handling | Analysis asks how failure can happen; handling asks what to do after it happens. |
| Incorrect result | Unsafe result | Incorrect means wrong; unsafe means unacceptable from a safety perspective. |
| Unsafe result | Unusable result | Unsafe concerns harm/risk; unusable concerns practical inability to use the result. |
| Omission | Hallucination | Omission leaves out required information; hallucination adds unsupported information. |
| Hallucination | Fabricated answer | Fabricated answer is an example/outcome of unsupported generation; hallucination is the broader failure-mode label. |
| Unsafe action | Wrong tool action | An unsafe action is unsafe in consequence; a wrong tool action is incorrect tool-mediated behavior and may or may not be unsafe. |
| Wrong tool use | Wrong tool action | Wrong tool use names misuse of a tool; wrong tool action names the resulting action. |
| Refusal | Safe fallback | Refusal is a system behavior that may be a failure; a fallback is an intentional safer path. |
| Bias | Random mistake | Bias is a systematic skew/pattern; a random mistake is not necessarily systematic. |
| Timeout | Slow response | Timeout is failure to complete within a limit; a slow response may still complete within the limit. |
| Invalid format | Incorrect content | Invalid format violates structural requirements; incorrect content is wrong in substance. |
| Workflow | Process | The page uses workflow for the ordered AI path; process may refer more broadly to operations or procedure. |
| Input | Output | Input enters the workflow; output is produced by it. |
| Input | Question | A question is one kind of input; not every input is phrased as a question. |
| Output | Result | Output is the produced information/action; result emphasizes the outcome and its acceptability. |
| Tool | Action | A tool is a capability/component; an action is what the system does through or without a tool. |
| Decision | Tool | A decision selects or determines a path; a tool performs a capability/operation. |
| Likelihood | Impact | Likelihood concerns chance of occurrence; impact concerns consequence if it occurs. |
| Impact | Detectability | Impact concerns consequence; detectability concerns how readily the failure can be noticed. |
| Likelihood | Detectability | Likelihood concerns occurrence; detectability concerns observation after or during occurrence. |
| Risk assessment | Risk control | Assessment evaluates risk; control reduces risk. |
| Prioritize | Control | Prioritization ranks risks; control applies measures to reduce them. |
| Test | Monitor | Testing runs targeted cases; monitoring observes ongoing or post-test behavior. |
| Test case | Real-world example | A test case is deliberately designed for verification; a real-world example illustrates a scenario and intended behavior. |
| Targeted example | Random example | A targeted example probes a named failure; a random example is not necessarily diagnostic. |
| Validation | Confirmation | Validation checks data/requirements; confirmation is explicit human or user approval. |
| Validation | Review | Validation can be an automated check; review is examination, often by a person or process. |
| Fallback | Limit | A fallback provides an alternative path; a limit bounds behavior or capability. |
| Fallback | Failure handling | Fallback is one control/response option; failure handling is the broader next-step policy. |
| Clarification | Confirmation | Clarification resolves missing/ambiguous information; confirmation authorizes a proposed action. |
| Weak evidence | No matching source | Weak evidence exists but is insufficient; no matching source means a relevant source was not found. |
| Evidence | Source | Evidence is support for a conclusion; a source is the material from which evidence may be drawn. |
| Matching source | Weak evidence | A matching source is relevant; weak evidence may be present but insufficiently strong. |
| Safe action | Human review | A safe action is an acceptable outcome; human review is one control that may help produce or approve it. |
| Human review | Human-in-the-loop | Human review is an explicit activity; human-in-the-loop is a broader architecture pattern that may include review, approval, or intervention. |
| Failure handling | Recovery | Failure handling includes deciding what happens next; recovery is specifically returning to a safe/working state. |
| Bug | Failure mode | A bug is an implementation defect; a failure mode may arise without a code bug from model, data, process, or integration. |
| Model failure | Data failure | Model failure originates in model behavior/limitations; data failure originates in information or data quality. |
| Data failure | Process failure | Data failure concerns inputs/evidence; process failure concerns the workflow/procedure. |
| Process failure | Integration failure | Process failure concerns workflow design/operation; integration failure occurs at system/component boundaries. |
| Evaluation | Failure-mode analysis | Evaluation measures or assesses behavior; failure-mode analysis enumerates and reasons about ways it can fail. |
| Functional tests | Failure-mode tests | Functional tests check intended functions generally; failure-mode tests target specific risk patterns. |
| Deployment readiness | Reliability | Deployment readiness is a decision/readiness state; reliability is the broader property of dependable behavior. |
| Monitored result | Output | An output is produced; a monitored result is an output observed over time or after controls/tests. |
| Failure mode | Failure mode and effects analysis (FMEA) | Failure mode is the page’s core concept; FMEA is a broader named methodology suggested by the analogy but not defined on the page. |

## Notes

- The visible process is: **Map → Predict → Prioritize → Test → Control**.
- The page’s process details are: **describe the workflow → list possible failures → assess risk → run cases → reduce the risk**.
- The explicit risk dimensions are **likelihood**, **impact**, and **detectability**.
- The visible relationship chain is: **Workflow → Failure Mode → Test Case → Control → Monitored Result**.
- The definition explicitly distinguishes a **failure mode** from **failure handling**: the former describes the way failure occurs, while the latter defines the next response.
- The page explicitly says a failure mode is not merely a **random mistake** and not merely a **bug**.
- The page names failure sources as **model, data, process, or integration**.
- The concrete failure-mode list is: **hallucination, omission, unsafe action, wrong tool use, refusal, bias, timeout, and invalid format**.
- The business example is deliberately abstention-oriented: with **no matching source**, the system detects **weak evidence**, asks for **clarification**, and returns **no fabricated answer**.
- The AI product example is action-safety-oriented: for an **ambiguous request to update data**, the system **validates fields**, **requires confirmation**, and produces **a safe action or human review**.
- “Safe action or human review” is a two-branch outcome: the system may proceed after controls or escalate to a person.
- The phrase **targeted examples and monitoring** combines preplanned testing with ongoing observation; the page does not define a monitoring architecture.
- The phrase **validation, fallback, review, or limits** is an intentionally broad control list, not a detailed control taxonomy.
- The source does not define numerical risk scores, probability scales, severity levels, detection rates, benchmark results, or operational thresholds.
- The source does not define FMEA, fault-tree analysis, hazard analysis, red teaming, incident response, or a formal safety case, even though the machine/safety analogy may suggest those neighboring concepts.
- The source does not explain implementation details for model internals, datasets, APIs, tool schemas, logs, traces, or deployment infrastructure.
- The related chips are **Evaluation**, **Functional Tests**, **Failure Handling**, and **Deployment Readiness**.
- Repeated labels, title-case labels, plural/singular variants, workflow verbs, example phrases, analogy terms, and possible aliases are intentionally retained for later editorial deduplication.
- The video section contributes the visible labels **Independent explainer**, **Video**, and **visual explainer**; it is not used as a substitute for reading the HTML body.
