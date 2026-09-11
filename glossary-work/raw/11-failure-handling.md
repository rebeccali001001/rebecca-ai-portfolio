# Topic

Failure Handling

## Topic Metadata

- **Requested Module:** 11
- **Parent module:** 11 · Evaluation, Safety & Reliability
- **Page breadcrumb module:** 04 · Prompting & System Design · Topic 03
- **Page topic:** Failure Handling
- **Topic title:** What is Failure Handling?
- **Source file:** `failure-handling.html`
- **Source page description:** Failure handling defines what an AI system should do when the expected result is not produced.
- **Extraction scope:** Full visible page body, including navigation labels, definition, analogy, explanatory paragraphs, five-step process flow, real-world examples, comparison cards, related-concept chain and links, takeaway, and video metadata.
- **Collection policy:** Raw maximum-candidate collection. Candidates are intentionally broad, overlapping, repeated at different granularities, and not deduplicated, merged, or reduced. Keep technical terms, mechanisms, workflow nodes, indicators, abbreviations, important body words, aliases/synonyms, and potentially confusable concepts for later review.
- **Numbering note:** The requested glossary batch identifies this as Module 11, while the source page still carries the breadcrumb `04 · Prompting & System Design · Topic 03`; the Module 11 assignment and source breadcrumb are both preserved.

## Glossary Candidates

| Candidate | Category | Working definition / why it matters | Page evidence or context |
|---|---|---|---|
| Failure Handling | Core topic / title form | A plan for what an AI system does when a request, tool call, or output fails. | Page title; lede; definition |
| failure handling | Core concept | The planned behavior used when the expected result is not produced. | Definition paragraph |
| failure-handling plan | Planning / alias candidate | An explicit set of responses and safe paths for failure conditions. | “Failure handling is the plan...” |
| failure | Core event | A situation in which a request, tool call, or output does not produce the expected result. | Definition |
| expected result | Outcome concept | The usable result the system was supposed to produce. | Lede; takeaway |
| expected output | Outcome / alias candidate | The output that should have been returned for a request. | “expected result”; output contrast |
| missing result | Failure condition | A result that is absent rather than merely incorrect. | Takeaway: expected result is missing or invalid |
| invalid result | Failure condition | A result that exists but cannot be accepted or used. | Takeaway; invalid response example |
| unusable result | Failure condition | A result that is technically present but not safe or useful to continue with. | Recover step; controlled failure context |
| request failure | Failure type | A failure involving the incoming request or its ability to be completed. | Definition: request fails |
| tool-call failure | Failure type | A failure while invoking or receiving a result from a tool. | Definition: tool call fails |
| output failure | Failure type | A failure in the produced output, such as invalid structure or unusable content. | Definition; invalid JSON example |
| system response | Response concept | The action the system takes after detecting a failure. | Possible responses |
| possible response | Response category | One of retry, fallback, ask, error, review, or safe stop. | “Possible responses include...” |
| retry | Recovery action | Attempt the failed operation again. | Possible responses; Retry Only comparison |
| retrying | Recovery process | Repeating a request or operation after a failure. | Definition copy |
| retry policy | Policy candidate | Rules controlling when, how, and how often an operation may be retried. | Implied by retry response; retained for review |
| retry attempt | Workflow unit | One additional attempt to complete an operation. | Invalid JSON example: retries |
| fallback | Recovery action | Use an alternate path, component, or result when the primary path fails. | Possible responses; tool outage example |
| fallback path | Recovery mechanism | An alternate route used when the main route is unavailable or invalid. | Emergency-plan analogy; fallback response |
| fallback response | Output strategy | A response produced by an alternate mechanism or path. | Tool outage example |
| asking for missing information | Recovery action | Request information needed to continue safely. | Possible responses |
| missing information | Input deficiency | Required information absent from the request or context. | Possible responses |
| clarification request | Ask action / alias candidate | A system request for the user to supply or clarify missing information. | “asking for missing information” |
| error | Failure signal | An indication that an operation did not complete as expected. | Definition; error-message comparison |
| error return | Response action | Return an error rather than pretending to have a valid result. | Possible responses |
| error response | Output form | A controlled response communicating failure or inability to complete. | Invalid JSON validation-error example |
| validation error | Error type | An error returned when the result fails structural or rule-based validation. | Invalid JSON example |
| requesting human review | Human-control action | Escalate a failure or uncertain result to a person for judgment. | Possible responses |
| human review | Oversight mechanism | A person checks, approves, corrects, or decides what happens next. | Possible responses; related context |
| human intervention | Oversight / alias candidate | Human involvement in the failure path or decision. | Implied by human review |
| stopping safely | Safety action | End processing without producing or propagating an unsafe or untrustworthy result. | Possible responses |
| safe stop | Safety mechanism / alias | A deliberate termination path when continuation is not safe. | “stopping safely”; comparison with ignoring errors |
| controlled failure | Failure outcome | A visible, bounded failure that avoids fabricated or unusable output. | Invalid JSON example; tool outage example |
| safe path | Recovery concept | A response path that continues only when the result is usable or ends safely. | Recover step |
| emergency plan | Analogy / mechanism | A predefined plan for what people or systems do when normal operation breaks. | Analogy heading and text |
| emergency response | Analogy / process | The action taken when a normal route or service is unavailable. | Building analogy |
| normal operation | System state | The expected route before an error or disruption occurs. | Emergency-plan analogy |
| power failure | Analogy example | A real-world failure condition used to illustrate planned response. | Analogy text |
| blocked route | Analogy example | A normal path that cannot be used and requires an alternate path. | Analogy text |
| clear path for failure | Design principle | A deliberately specified response route for failure conditions. | Analogy conclusion |
| reliable AI system | System quality | An AI system that defines what to do when expected results are missing or invalid. | Remember this |
| reliability | Quality concept | The broader property of behaving dependably, including under failure. | Page parent context; reliable system |
| failure workflow | Workflow concept | The ordered sequence used to detect, understand, respond to, recover from, and record a failure. | Five-step process |
| failure lifecycle | Lifecycle / alias candidate | The progression from failure detection through recovery and learning. | Process flow; retained for review |
| detect | Process step | Find that a failure or abnormal condition has occurred. | Step 1 label |
| detection | Process / mechanism | The act of identifying that an operation has failed. | Step 1 |
| failure detection | Process / mechanism | Identifying a failed request, tool call, or output. | Step 1 heading |
| find the failure | Process label | Locate or recognize the failure event. | Step 1 supporting label |
| error check | Detection mechanism | A check for explicit error signals. | Step 1 supporting text |
| error checking | Detection process | Inspecting an operation for error conditions. | “Check errors...” |
| timeout check | Detection mechanism | Checking whether an operation exceeded its allowed time. | Step 1 supporting text; tool outage example |
| timeout detection | Detection process | Recognizing that a request or tool did not respond in time. | Tool outage example |
| schema check | Validation / detection mechanism | Checking whether data follows the expected structure or schema. | Step 1 supporting text |
| schema validation | Validation mechanism / alias candidate | Testing output against an expected schema. | “Check ... schema”; invalid JSON example |
| evidence check | Detection / validation mechanism | Checking whether an output has adequate supporting evidence. | Step 1 supporting text |
| evidence validation | Validation / alias candidate | Assessing whether evidence exists and supports the result. | “Check ... evidence” |
| check errors, timeouts, schema, and evidence | Detection checklist | A compact set of signals used to find a failure. | Step 1 supporting sentence |
| classify | Process step | Understand what kind of failure occurred and why. | Step 2 label |
| classification | Process / mechanism | Grouping a failure into a cause or type that guides response. | Step 2 |
| failure classification | Process / mechanism | Separating a failure into transient, input, tool, or safety categories. | Step 2 supporting text |
| understand the cause | Diagnostic process | Determine why the failure occurred. | Step 2 supporting label |
| failure cause | Diagnostic concept | The condition or mechanism responsible for a failure. | Step 2 |
| transient failure | Failure type | A temporary failure that may resolve if retried or delayed. | Step 2 supporting text |
| transient error | Failure type / alias candidate | A temporary error rather than a persistent input or safety problem. | “transient ... failures” |
| temporary failure | Failure type / alias candidate | A failure expected to clear with time or a later attempt. | Transient concept |
| input failure | Failure type | A failure caused by missing, malformed, or unacceptable input. | Step 2 supporting text |
| input error | Failure type / alias candidate | An error arising from the request or supplied data. | Input-failure category |
| tool failure | Failure type | A failure of an external tool or its invocation. | Step 2; tool outage example |
| tool error | Failure type / alias candidate | An error returned by or encountered while using a tool. | Tool-call context |
| safety failure | Failure type | A failure condition in which proceeding could be unsafe or violate a safety requirement. | Step 2 supporting text |
| safety error | Failure type / alias candidate | An error associated with safety constraints or unsafe continuation. | Safety-failure category |
| transient / input / tool / safety | Failure taxonomy | Four example classes used to understand the cause of failure. | Step 2 supporting sentence |
| choose | Process step | Select the response that should be taken for the classified failure. | Step 3 label |
| response selection | Decision process | Choosing among retry, fallback, ask, review, or stop. | Step 3 |
| choose a response | Process label | Select an appropriate next action after classification. | Step 3 supporting label |
| decision | Control concept | A selected next action in the failure workflow. | Response-choice context |
| decision rule | Policy candidate | A rule mapping a failure condition to a response. | Implied by “select a response” |
| retry, fallback, ask, review, or stop | Response set | The five response categories named in the choice step. | Step 3 supporting sentence |
| recover | Process step | Take the selected safe path and continue only if the result is usable. | Step 4 label |
| recovery | Process / mechanism | The act of returning to a usable, safe state after failure. | Step 4 |
| recovery path | Process / mechanism | The route followed after a failure to obtain a usable result or stop safely. | Step 4 supporting label |
| take the safe path | Process label | Follow a controlled route after choosing a response. | Step 4 |
| usable result | Outcome criterion | A result that can safely support continuation or delivery. | Step 4 supporting text |
| result usability | Quality criterion / metric candidate | Whether an output is suitable for the next step or the user. | “when the result is usable” |
| continue only when usable | Safety rule | Do not proceed unless the result passes the usability condition. | Step 4 supporting sentence |
| safe recovery | Recovery / safety concept | Recovery that does not propagate invalid, unsafe, or fabricated output. | Process context |
| record | Process step | Log the failure event and its outcome for later learning. | Step 5 label |
| recording | Process / mechanism | Capturing information about a failure and response. | Step 5 |
| failure record | Observability artifact | A stored description of a failure event and what happened next. | Step 5 |
| event record | Observability artifact / alias candidate | A record of an occurrence in the system. | “Learn from the event” |
| learn from the event | Improvement process | Use failure information to improve the system. | Step 5 supporting label |
| failure logging | Observability mechanism | Recording failures for diagnosis, measurement, and improvement. | Step 5 supporting sentence |
| log the failure | Process action | Write down the relevant failure event and context. | Step 5 |
| system improvement | Improvement outcome | Changes made to improve future failure handling or reliability. | Step 5 |
| continuous improvement | Improvement concept / related candidate | Ongoing refinement based on recorded failures. | “improve the system” |
| five-step process | Process structure | Detect, classify, choose, recover, and record. | Process-flow block |
| detect → classify → choose → recover → record | Process sequence | Ordered failure-handling lifecycle presented on the page. | Process flow |
| process flow | Visualization / workflow | A visual sequence showing the five failure-handling steps. | `process-flow` block |
| step card | UI / process representation | One visual card representing a workflow step. | HTML structure; retained as raw candidate |
| request | Input / workflow object | A user or system instruction requiring a result. | Definition; related-concept tree |
| user request | Input / workflow object | A request submitted by a user to the AI system. | Tool-outage example |
| structured-data request | Request type | A request asking the system to produce data in a defined structure. | Invalid JSON example |
| external API request | Request type | A request requiring a call to an external API. | Tool-outage example |
| AI system | System | The complete AI-enabled mechanism that receives requests and returns results. | Lede; definition |
| system behavior | System property | What the system does in response to normal or failed operations. | Failure-handling plan |
| system action | Response concept | The next action taken by the system after failure. | Error-message contrast |
| request path | Workflow path | The route from a request through processing to a result. | Related-concept tree |
| normal path | Workflow path | The primary path followed when no failure occurs. | Emergency-plan analogy; fallback contrast |
| failure path | Workflow path | The route followed after an error or invalid result. | Clear paths for failure |
| next action | Decision / response | The action selected after a failure is detected. | “defines the system’s next action” |
| tool call | Integration operation | A request from the AI system to an external capability. | Definition; related concepts |
| tool calling | Related concept / process | The mechanism by which an AI system invokes external tools. | Related-concept chip |
| external tool | Integration dependency | A service or capability outside the core AI model that the system invokes. | Tool outage example |
| external API | Integration dependency | An external service interface required for a tool-dependent request. | Tool outage example |
| tool outage | Failure event | A period when an external tool or API is unavailable. | Real-world example heading |
| outage | Availability failure / alias candidate | A loss or interruption of service availability. | Tool outage example |
| API outage | Failure type / alias candidate | An outage affecting an external API. | Tool outage example |
| timeout | Failure signal / metric | A condition in which a request or tool response does not arrive within the allowed time. | Tool outage example; detection checks |
| timed-out request | Failure event / alias candidate | A request that exceeded its time limit. | Tool outage example |
| external dependency | Reliability concept | A service outside the system whose availability affects the result. | Tool outage context |
| dependency failure | Failure type / alias candidate | A failure caused by an unavailable or malfunctioning dependency. | Tool outage context |
| fabricated result | Unsafe output | An invented result returned instead of acknowledging a failed dependency or missing evidence. | “clear status instead of a fabricated result” |
| false result | Unsafe output / alias candidate | An output presented as valid although it is not grounded in a successful operation. | Fabricated-result context |
| clear status | User communication | An explicit status message explaining that a requested operation could not be completed. | Tool outage example |
| try later | User guidance | A suggested future action when an external dependency is temporarily unavailable. | Tool outage example |
| controlled status | Communication / output candidate | A bounded status response that makes failure visible. | Tool outage context |
| invalid JSON | Output failure example | Structured output that cannot be parsed as valid JSON. | Business example heading |
| JSON | Format / abbreviation candidate | A structured data format used as the example output. | Invalid JSON example |
| structured data | Data representation | Data organized according to an expected format or fields. | Business example input |
| invalid response | Output failure | A response that does not satisfy the expected format or validity rules. | Business example system line |
| valid data | Acceptable output | Data that passes the relevant validity or schema requirements. | Business example output |
| validation | Quality-control process | Checking whether a response satisfies expected rules or structure. | Validation error; schema check |
| valid result | Acceptable output | A result that passes validation and can be used. | Business example output |
| business example | Example category | A failure-handling scenario in a business workflow. | Example heading |
| AI product example | Example category | A failure-handling scenario in a user-facing AI product. | Example heading |
| input | Workflow object | Data or request provided to the system. | Both examples; related-concept tree |
| system receives | Process event | The system obtains a response or request to process. | Invalid JSON example |
| response | Output object | A result returned by a system, model, or tool. | Invalid response; error response |
| output | Workflow object | The result returned by the AI system. | Definition; examples; related tree |
| valid output | Acceptable output | Output that meets the expected format and can be safely consumed. | Invalid JSON example |
| controlled failure output | Output strategy | A failure response that is explicit, bounded, and not fabricated. | Invalid JSON and outage examples |
| “failure handling” versus “retry” | Comparison pair | The topic is broader than retry because it includes multiple responses. | What it is NOT |
| Retry Only | Misconception label | The mistaken idea that all failure handling consists of retrying. | Comparison heading |
| retry-only strategy | Limited strategy | A strategy that treats retry as the only possible response. | Failure Handling ≠ Retry Only |
| “failure handling” versus “error message” | Comparison pair | Failure handling defines action; an error message communicates that something went wrong. | What it is NOT |
| error message | Communication artifact | A message that tells a user or system that something went wrong. | Comparison card |
| failure-handling action | System action | The next operational response specified by failure handling. | Error-message contrast |
| “failure handling” versus “ignoring errors” | Comparison pair | Failure handling exposes uncertainty and chooses a safe path; ignoring errors does not. | What it is NOT |
| ignoring errors | Unsafe behavior | Continuing without acknowledging or responding to an error. | Comparison card |
| error suppression | Unsafe behavior / alias candidate | Hiding or discarding errors so the system appears to continue. | Ignoring-errors context |
| uncertainty | Safety / communication concept | The condition of not having a trustworthy result or enough information. | “makes uncertainty visible” |
| visible uncertainty | Communication principle | Explicitly showing that the system lacks a dependable result. | Ignoring-errors comparison |
| unsafe continuation | Failure-handling anti-pattern | Continuing after an error without a safe or usable result. | Ignoring-errors comparison |
| safe result | Outcome criterion | A result that is usable and appropriate to return or pass onward. | Comparison; takeaway |
| fabricated output | Anti-pattern / alias candidate | An invented output presented as though an operation succeeded. | Tool outage example |
| related concepts | Navigation / concept group | Topics connected to failure handling by the page. | Related-concepts section |
| concept tree | Relationship representation | A compact expression of the request-to-response workflow. | `Request → AI / Tool → Validate result...` |
| Request → AI / Tool → Validate result → Retry / Fallback / Ask / Review / Stop | Workflow expression | The page’s high-level system and response chain. | Related-concept tree |
| validate result | Workflow step | Check whether the produced result is acceptable before continuing. | Related-concept tree |
| result validation | Workflow / mechanism | The validation stage between production and recovery response. | Related-concept tree |
| stop | Response action | End the workflow when retry, fallback, asking, or review is not appropriate. | Related-concept tree; choice step |
| Structured Outputs | Related topic | A linked concept about producing outputs that follow a defined structure. | Related-concept chip |
| System Prompts | Related topic | A linked concept about system-level instructions that can specify behavior. | Related-concept chip |
| Failure Modes | Related topic | A linked concept about ways an AI system can produce incorrect, unsafe, or unusable results. | Related-concept chip |
| Tool Calling | Related topic | A linked concept about invoking external tools. | Related-concept chip |
| reliability engineering | Related-context candidate | Designing systems to remain dependable and respond safely under failure. | Parent-module context; retained for review |
| graceful degradation | Related-context candidate | Providing a reduced but safe capability when the primary path fails. | Fallback context; retained for review |
| fail-safe behavior | Related-context candidate | Behavior that moves toward a safe state when a failure occurs. | Safe-stop context; retained for review |
| fail-closed | Related-context candidate | Defaulting to denial or non-action when safety cannot be established. | Safety-stop context; retained for review |
| fail-open | Related-context candidate | Continuing or allowing action when a failure occurs. | Important contrast to safe stop; retained for review |
| circuit breaker | Related-context candidate | A mechanism that stops repeated calls to a failing dependency. | Tool-outage context; retained for review |
| backoff | Related-context candidate | Delaying retries, often with increasing wait times. | Retry-policy context; retained for review |
| exponential backoff | Related-context candidate | Increasing retry delays exponentially to reduce pressure on a dependency. | Retry-policy context; retained for review |
| retry budget | Related-context candidate | A bound on the number or cost of retry attempts. | Retry-policy context; retained for review |
| idempotency | Related-context candidate | Property that allows a repeated operation without unintended duplicate effects. | Retry safety context; retained for review |
| error taxonomy | Related-context candidate | A structured classification of error or failure types. | Classify step; retained for review |
| root-cause analysis | Related-context candidate | Investigation of the underlying cause of a failure. | Understand the cause; retained for review |
| observability | Related-context candidate | Ability to understand system behavior from logs, signals, and outputs. | Check and record steps; retained for review |
| logging | Related-context candidate | Recording system events for diagnosis and improvement. | Record step; retained for review |
| audit trail | Related-context candidate | Traceable record of requests, failures, actions, and outcomes. | Record step; retained for review |
| incident | Related-context candidate | A failure event significant enough to track or respond to operationally. | Event-record context; retained for review |
| incident response | Related-context candidate | Coordinated process for handling a significant system failure. | Emergency-plan analogy; retained for review |
| service-level objective (SLO) | Metric / abbreviation candidate | A target level of service reliability or availability. | Timeout/outage context; retained for review |
| availability | Metric / quality candidate | The proportion of time a service or dependency is operational. | Tool outage context; retained for review |
| error rate | Metric candidate | The rate at which operations fail or return errors. | Error-check context; retained for review |
| timeout rate | Metric candidate | The rate at which operations exceed their time limits. | Timeout-check context; retained for review |
| retry rate | Metric candidate | The share of operations requiring one or more retries. | Retry context; retained for review |
| fallback rate | Metric candidate | The share of requests completed through a fallback path. | Fallback context; retained for review |
| recovery rate | Metric candidate | The share of failures that return to a usable result. | Recover step; retained for review |
| escalation rate | Metric candidate | The share of failures sent to human review. | Human-review context; retained for review |
| safe-stop rate | Metric candidate | The share of failures that terminate through a safe stop. | Stop context; retained for review |
| mean time to recovery (MTTR) | Metric / abbreviation candidate | Average time required to recover after a failure. | Recovery context; retained for review |
| mean time to failure (MTTF) | Metric / abbreviation candidate | Average operating time before a failure. | Reliability context; retained for review |
| user-visible failure | Communication / quality candidate | A failure presented clearly to the user rather than hidden. | Clear status; visible uncertainty |
| silent failure | Failure anti-pattern | A failure that is hidden or not communicated to the user or operators. | Contrast with visible uncertainty; retained for review |
| graceful error handling | Design principle / alias candidate | Handling failure with a useful, bounded, user-understandable response. | Controlled failure context |
| robust system | System quality | A system that continues safely or fails clearly under adverse conditions. | Reliability context; retained for review |
| robustness | Quality concept | Ability to tolerate or safely handle unexpected conditions. | Failure-handling context; retained for review |
| resilience | Quality concept | Ability to recover from disruptions and continue dependable service. | Recovery context; retained for review |
| fault tolerance | Quality concept | Ability to keep functioning or fail safely despite component faults. | Fallback/recovery context; retained for review |
| safety guard | Safety mechanism | A constraint or check that prevents unsafe continuation. | Safety failures; safe path |
| guardrail | Safety mechanism / alias candidate | A rule or control limiting unsafe behavior. | Safety context; retained for review |
| human-in-the-loop | Oversight / related candidate | A design in which people review or guide system decisions. | Human review response; retained for review |
| escalation | Human-control process | Transfer of a case to a higher authority or human reviewer. | Human review response |
| fallback model | Recovery mechanism | An alternate model used when the primary model is unavailable or unsuitable. | Fallback context; retained for review |
| fallback service | Recovery mechanism | An alternate service used when the primary service fails. | Tool outage context; retained for review |
| default response | Recovery / output candidate | A predefined response used when the normal result cannot be produced. | Fallback context; retained for review |
| placeholder response | Output candidate | A temporary or explicit non-result used instead of inventing content. | Failure-output context; retained for review |
| validation gate | Control point | A checkpoint that must pass before the workflow continues. | Schema/evidence checks; retained for review |
| acceptance criterion | Quality criterion | A condition a result must satisfy to be considered usable. | Valid/usable result context |
| termination condition | Control criterion | A condition requiring the system to stop processing. | Safe stop; stop response |
| recovery condition | Control criterion | A condition under which the system may safely continue. | Continue only when usable |
| failure signal | Detection input | An error, timeout, schema issue, or evidence issue indicating a problem. | Detect step |
| error code | Diagnostic artifact / alias candidate | A coded identifier describing an error condition. | Error-check context; retained for review |
| status code | Diagnostic artifact / alias candidate | A code communicating success or failure status. | Error/status context; retained for review |
| exception | Failure / programming candidate | An abnormal condition that interrupts the normal flow. | Error-handling context; retained for review |
| exception handling | Process / alias candidate | Detecting and responding to exceptional conditions. | Failure-handling synonym candidate |
| recovery action | Response category | An action taken to restore a usable path after failure. | Retry/fallback/review/stop |
| response policy | Policy concept | The policy that maps classes of failure to actions. | Choose step; retained for review |
| failure policy | Policy concept | Rules defining how the system behaves under different failures. | Failure-handling plan |
| operational policy | Policy concept | Rules governing system behavior in live operation. | Retry/fallback/status context |
| user guidance | Communication action | Instructions such as supplying missing information or trying later. | Ask/timeout examples |
| status message | Communication artifact | A message communicating the current state or failure. | Clear status |
| explanation | Communication concept | Information that helps a user understand why the normal result was not returned. | Error message; clear status |
| transparency | Safety / communication principle | Making limitations, uncertainty, and failure visible. | “makes uncertainty visible” |
| trustworthiness | Quality concept | The degree to which users can rely on the system’s outputs and failure behavior. | Reliable system; fabricated-result contrast |
| dependable behavior | Quality concept | Consistent, predictable behavior in normal and failed cases. | Reliable AI system |
| learning loop | Improvement mechanism | Use recorded failures to make future behavior better. | Record and improve |
| feedback loop | Improvement mechanism / alias candidate | Information from outcomes feeds changes to the system. | Learn from event; retained for review |
| post-failure analysis | Improvement process | Reviewing a failure after the event to understand and reduce recurrence. | Record/learn context |
| remediation | Improvement action | A change made to correct or prevent a failure. | Improve the system; retained for review |
| prevention | Reliability action | Changes that reduce the chance of a future failure. | Learn and improve context |
| recurrence | Reliability concept | The same or similar failure happening again. | Improvement context; retained for review |
| error budget | Reliability metric / policy candidate | An allowed amount of failure within a reliability target. | Reliability context; retained for review |
| failure budget | Reliability policy / alias candidate | An allowed tolerance for failures or unsuccessful requests. | Error-budget context; retained for review |
| output contract | Interface / validation candidate | An expected agreement about the structure and meaning of an output. | Schema/structured-output context |
| schema contract | Interface / validation candidate | A structural agreement an output must satisfy. | Schema check; invalid JSON |
| API contract | Interface / dependency candidate | Expected request and response behavior between services. | External API context |
| input contract | Interface / validation candidate | Requirements a request or input must satisfy. | Input-failure context |
| evidence threshold | Validation / safety candidate | Minimum evidence required before accepting a result. | Evidence check; retained for review |
| confidence threshold | Decision / safety candidate | Minimum confidence required before accepting or escalating a result. | Usability/safety context; retained for review |
| uncertainty threshold | Decision / safety candidate | Level of uncertainty beyond which the system asks, reviews, or stops. | Visible uncertainty; retained for review |
| escalation threshold | Decision / safety candidate | Condition that triggers human review or another stronger response. | Human-review context; retained for review |
| bounded action | Safety concept | An action constrained so failure cannot spread without control. | Controlled failure; safe path |
| blast radius | Reliability / safety candidate | Extent of impact caused by a failure. | Failure-safety context; retained for review |
| containment | Safety / recovery candidate | Limiting the effect of a failure to keep it from spreading. | Safe stop/fallback context; retained for review |
| isolation | Safety / recovery candidate | Separating a failing component or operation from the rest of the system. | Tool-outage/failure context; retained for review |
| rollback | Recovery action candidate | Return to a prior known-good version or state after failure. | Recovery context; retained for review |
| replay | Diagnostic / recovery candidate | Re-run a recorded request or event to reproduce or investigate failure. | Record/learn context; retained for review |
| reproduction | Diagnostic process candidate | Re-create a failure under known conditions. | Record and classify context; retained for review |
| incident severity | Classification / metric candidate | A measure of the impact or urgency of a failure. | Failure classification context; retained for review |
| priority | Decision candidate | Relative urgency used to decide how a failure is handled. | Human review/escalation context |
| impact | Assessment candidate | Effect of a failure on users, outputs, or system operation. | Reliability context |
| root cause | Diagnostic candidate | The underlying reason a failure occurred. | Understand the cause |
| contributing factor | Diagnostic candidate | A condition that helped produce a failure without being its sole root cause. | Cause-analysis context |
| symptom | Diagnostic candidate | Observable sign of a failure, such as an error or timeout. | Detect step |
| failure mode | Diagnostic / related candidate | A recognizable pattern in how a system fails. | Linked Failure Modes topic |
| failure scenario | Test / planning candidate | A defined situation in which a system may fail and needs a response. | Emergency-plan analogy; examples |
| test failure | Evaluation / failure candidate | A failed check showing that expected behavior was not met. | Related evaluation context; retained for review |
| negative path | Testing / workflow candidate | A workflow path for invalid input, errors, or other non-success cases. | Failure-handling flow; retained for review |
| happy path | Workflow / contrast candidate | The normal successful path against which failure paths are compared. | Normal-path context; retained for review |
| edge case | Testing / failure candidate | An unusual input or condition that may expose failure behavior. | Input/safety context; retained for review |
| degraded mode | Recovery mode candidate | A reduced-capability operating mode used during partial failure. | Fallback context; retained for review |
| maintenance mode | Recovery mode candidate | A mode used when normal service is intentionally unavailable. | Tool outage / try later context |
| unavailable | Dependency state | A condition in which a tool, API, or result cannot be accessed or produced. | Tool outage example |
| blocked | Workflow state | A condition in which the normal route cannot continue. | Analogy: route is blocked |
| returned error | Output state | A response explicitly indicating that an operation failed. | Possible responses |
| requested review | Control action | A decision to have a human inspect the case. | Possible responses |
| safe termination | Control action / alias | Ending processing without returning an unsafe result. | Safe stop |
| operational learning | Improvement concept | Using production failure records to improve behavior and operations. | Record step |
| system learning | Improvement concept | Improving the AI system based on observed failures. | “improve the system” |

## Potential Missing Concepts

- The page names retrying but does not explain retry limits, exponential backoff, jitter, retry budgets, idempotency, duplicate side effects, or when retrying is unsafe.
- The page names fallback but does not specify fallback models, fallback services, graceful degradation, default responses, degraded modes, or how to validate a fallback result.
- The page names asking for missing information but does not define clarification-question design, required versus optional fields, partial completion, or how to distinguish missing input from ambiguous input.
- The page names errors and validation errors but does not distinguish error classes, exception handling, error codes, status codes, structured error objects, or user-facing versus operator-facing errors.
- The page names timeouts but does not explain connect timeouts, read timeouts, deadline propagation, cancellation, timeout budgets, or timeout versus outage diagnosis.
- The page names schema checks and invalid JSON but does not explain JSON parsing, schema validation, output contracts, structured outputs, repair/re-ask loops, or partial parsing.
- The page names evidence checks but does not define grounding, citation validation, provenance, evidence thresholds, unsupported claims, or how to handle insufficient evidence.
- The page names transient, input, tool, and safety failures but does not provide a complete failure taxonomy, root-cause analysis method, severity levels, impact assessment, or incident priorities.
- The page names human review but does not explain escalation thresholds, reviewer interfaces, approval states, queueing, reviewer disagreement, audit trails, or human-in-the-loop operating procedures.
- The page names stopping safely but does not distinguish fail-safe, fail-closed, fail-open, graceful shutdown, containment, isolation, or safe termination conditions.
- The page says to continue only when a result is usable but does not define usability, acceptance criteria, confidence thresholds, uncertainty thresholds, or validation gates.
- The page says to record the failure but does not specify logs, structured events, correlation IDs, traces, metrics, retention, privacy, redaction, or incident records.
- The page says to improve the system but does not describe post-failure analysis, feedback loops, remediation, prevention, recurrence tracking, or regression tests.
- The page presents a tool outage but does not cover dependency health checks, circuit breakers, bulkheads, rate limits, service-level objectives, availability, or dependency isolation.
- The page does not distinguish a failure from a failure mode, error, exception, invalid output, timeout, outage, incident, or user-visible status.
- The page does not explain how failure handling interacts with structured outputs, system prompts, tool calling, failure modes, evaluation, monitoring, deployment, or safety guardrails.
- The page does not define operational metrics such as error rate, timeout rate, retry rate, fallback rate, recovery rate, escalation rate, safe-stop rate, MTTR, or availability.
- The page does not discuss testing failure paths, negative-path tests, edge cases, chaos testing, fault injection, synthetic outages, or replay of recorded failures.
- The page does not explain rollback, version pinning, canary release, feature flags, or recovery to a known-good model/service version.
- The page does not address security-specific failures such as prompt injection, authorization failure, data leakage, privacy violations, policy refusal, or unsafe tool execution.
- The page does not address partial results, streaming interruptions, duplicate requests, stale results, race conditions, concurrency, or distributed-system consistency.
- The page does not define how a system should communicate failure in different channels, languages, user roles, or accessibility contexts.

## Aliases / Synonyms

- Failure Handling / failure handling / failure-handling plan / 失败处理 / 故障处理
- failure / failed operation / unsuccessful operation / 失败 / 失败操作 / 未成功操作
- expected result / expected output / intended result / 预期结果 / 预期输出 / 预期结果（intended result）
- missing result / no result / absent result / 缺失结果 / 没有结果 / 未返回结果
- invalid result / unusable result / unacceptable result / 无效结果 / 不可用结果 / 不可接受结果
- request failure / request error / input failure / 请求失败 / 请求错误 / 输入失败（语境可能不同）
- tool-call failure / tool failure / tool error / external-tool failure / 工具调用失败 / 工具失败 / 工具错误
- output failure / invalid output / malformed output / 输出失败 / 无效输出 / 格式错误的输出
- retry / retrying / re-attempt / retry attempt / 重试 / 再次尝试 / 重试次数
- fallback / fallback path / alternate path / fallback response / 备用路径 / 回退 / 兜底响应
- ask for missing information / clarification request / request clarification / 询问缺失信息 / 澄清请求 / 请求补充信息
- error / error condition / failure signal / 错误 / 错误条件 / 失败信号
- error response / returned error / controlled error / 错误响应 / 返回错误 / 受控错误
- validation error / schema error / format validation error / 校验错误 / 模式错误 / 格式校验错误
- human review / human intervention / manual review / 人工复核 / 人工干预 / 手工审查
- escalation / human escalation / route to review / 升级 / 转人工 / 转交复核
- safe stop / safe termination / stopping safely / fail-safe stop / 安全停止 / 安全终止 / 安全停机
- controlled failure / graceful failure / graceful error handling / 受控失败 / 平滑失败 / 优雅错误处理
- clear status / status message / user-facing status / 清晰状态 / 状态消息 / 面向用户的状态
- fabricated result / fabricated output / invented result / made-up answer / 编造结果 / 编造输出 / 虚构答案
- visible uncertainty / explicit uncertainty / uncertainty disclosure / 可见不确定性 / 明示不确定性 / 不确定性披露
- detect / detection / failure detection / error detection / 检测 / 发现 / 失败检测 / 错误检测
- classify / classification / failure classification / error taxonomy / 分类 / 失败分类 / 错误分类体系
- transient failure / transient error / temporary failure / temporary error / 瞬时失败 / 瞬时错误 / 临时失败
- input failure / input error / invalid-input failure / 输入失败 / 输入错误 / 无效输入失败
- tool outage / API outage / service outage / dependency outage / 工具中断 / API 中断 / 服务中断 / 依赖中断
- timeout / timed-out request / deadline exceeded / 超时 / 请求超时 / 超过截止时间
- choose a response / response selection / decision step / 选择响应 / 响应选择 / 决策步骤
- recover / recovery / recovery path / recovery action / 恢复 / 恢复路径 / 恢复动作
- usable result / valid result / acceptable result / 可用结果 / 有效结果 / 可接受结果
- record / recording / failure logging / event logging / 记录 / 记录过程 / 失败日志 / 事件日志
- learn from the event / system improvement / continuous improvement / 从事件中学习 / 系统改进 / 持续改进
- error message / failure message / error notification / 错误消息 / 失败消息 / 错误通知
- ignoring errors / error suppression / silent failure / 忽略错误 / 错误抑制 / 静默失败
- schema check / schema validation / output validation / 模式检查 / 模式验证 / 输出验证
- evidence check / evidence validation / grounding check / 证据检查 / 证据验证 / 基础事实检查
- process flow / workflow / failure workflow / process sequence / 流程图 / 工作流 / 失败工作流 / 流程顺序
- response policy / failure policy / failure-handling policy / 响应策略 / 失败策略 / 失败处理策略
- exception / error / failure / 异常 / 错误 / 失败（工程语境不完全等同）
- exception handling / error handling / failure handling / 异常处理 / 错误处理 / 失败处理（相关但不总是同义）
- reliability / dependability / trustworthiness / 可靠性 / 可依赖性 / 可信赖性
- robustness / resilience / fault tolerance / 鲁棒性 / 韧性 / 容错性
- graceful degradation / degraded mode / reduced-capability mode / 优雅降级 / 降级模式 / 降低能力模式
- circuit breaker / dependency breaker / circuit-breaker control / 熔断器 / 依赖熔断 / 熔断控制
- backoff / retry delay / exponential backoff / 退避 / 重试延迟 / 指数退避
- observability / logging and monitoring / operational visibility / 可观测性 / 日志与监控 / 运维可见性
- root cause / underlying cause / root-cause explanation / 根因 / 底层原因 / 根因说明
- post-failure analysis / incident review / postmortem / 失败后分析 / 事件复盘 / 事后复盘
- error rate / failure rate / unsuccessful-request rate / 错误率 / 失败率 / 未成功请求率
- timeout rate / timeout frequency / 超时率 / 超时频率
- retry rate / retry frequency / 重试率 / 重试频率
- fallback rate / fallback frequency / 回退率 / 回退频率
- recovery rate / successful recovery rate / 恢复率 / 成功恢复率
- MTTR / mean time to recovery / mean time to repair / 平均恢复时间 / 平均修复时间
- SLO / service-level objective / 服务等级目标
- JSON / JavaScript Object Notation / JavaScript 对象表示法 / JSON
- API / Application Programming Interface / 应用程序编程接口 / API
- AI / Artificial Intelligence / 人工智能 / AI

## Do Not Confuse Candidates

- Failure Handling vs Retry: Failure handling is the complete response plan; retry is only one possible response.
- Failure Handling vs Error Message: Failure handling determines the system’s next action; an error message communicates that something went wrong.
- Failure Handling vs Ignoring Errors: Failure handling makes uncertainty visible and chooses a safe path; ignoring errors lets the system continue without a safe result.
- Failure vs Failure Mode: A failure is an event or unsuccessful outcome; a failure mode is a recognizable way the system can fail.
- Failure vs Error: A failure is the broader unsuccessful condition; an error is often a signal, message, or specific abnormal condition associated with it.
- Failure vs Exception: An exception is an abnormal condition in a program or execution flow; not every operational failure is represented as a programming exception.
- Error vs Error Message: An error is the condition; an error message is the communication about that condition.
- Error Message vs Status Message: An error message specifically communicates an error; a status message may communicate progress, availability, or a controlled failure more broadly.
- Invalid Result vs Missing Result: An invalid result is present but unacceptable; a missing result was not produced or returned.
- Invalid Result vs Unusable Result: An invalid result fails a stated validity rule; an unusable result may be valid in form but unsuitable for the next action.
- Expected Result vs Valid Result: An expected result is what the system was supposed to produce; a valid result passes the relevant checks.
- Valid Result vs Usable Result: Validity concerns satisfying rules or structure; usability concerns whether the result can safely support the next step.
- Retry vs Repetition: Retry is a deliberate recovery action after failure; repetition may occur without a failure policy or safety condition.
- Retry vs Fallback: Retry repeats the primary operation; fallback uses an alternate operation, service, model, or response.
- Retry vs Backoff: Retry is the attempt; backoff is the delay strategy between attempts.
- Retry vs Re-ask: Retry repeats an operation; re-ask changes or resubmits a request, often after an invalid model output.
- Fallback vs Safe Stop: Fallback tries an alternate path; safe stop ends without continuing when no acceptable path exists.
- Fallback vs Graceful Degradation: Fallback is an alternate route; graceful degradation is the broader behavior of offering reduced but safe capability.
- Ask vs Human Review: Asking requests information from the user; human review escalates a case to a reviewer for judgment or approval.
- Human Review vs Human-in-the-loop: Human review is one action; human-in-the-loop is a broader workflow design that includes human guidance or approval.
- Human Review vs Manual Retry: Review involves judgment; manual retry simply repeats an operation.
- Safe Stop vs Fail-Open: Safe stop ends or restricts action under uncertainty; fail-open permits continuation despite a failure condition.
- Fail-Safe vs Fail-Closed: Fail-safe means moving to a safe state; fail-closed is a specific pattern that defaults to denial or non-action.
- Transient Failure vs Persistent Failure: A transient failure may clear with time or retry; a persistent failure continues until its cause is fixed.
- Input Failure vs Tool Failure: Input failure originates in the request or data; tool failure originates in an external capability or its invocation.
- Tool Failure vs Tool Outage: A tool failure can be one bad call; an outage is a broader period of unavailability.
- Timeout vs Outage: A timeout is a request-level timing condition; an outage is a service-availability condition that may cause many timeouts or errors.
- Timeout vs Slow Response: A slow response may still arrive within the deadline; a timeout exceeds the allowed time and is treated as a failure.
- Schema Check vs Evidence Check: A schema check tests structure and format; an evidence check tests support for the result.
- JSON Validity vs Semantic Validity: Valid JSON parses structurally; semantic validity means the fields and values make sense for the task.
- Validation vs Evaluation: Validation checks whether a particular result satisfies requirements; evaluation measures system performance more broadly.
- Validation Error vs Model Error: A validation error is detected by a check; a model error is an incorrect or unsuitable model output, whether or not a validator catches it.
- Evidence vs Confidence: Evidence supports a claim; confidence expresses how certain a system appears to be, and may not be calibrated.
- Evidence vs Ground Truth: Evidence is supporting information; ground truth is the reference answer or actual state used for checking.
- Classify vs Diagnose: Classification assigns a failure to a category; diagnosis investigates why it happened.
- Failure Classification vs Root-Cause Analysis: Classification organizes the failure type; root-cause analysis seeks the underlying cause.
- Cause vs Symptom: A cause produces the failure; a symptom is an observable sign of it.
- Detect vs Monitor: Detection identifies a failure event; monitoring continuously observes system signals and trends.
- Record vs Monitor: Recording stores an event; monitoring observes signals, often over time, and may trigger detection.
- Log vs Audit Trail: A log is an event record; an audit trail is an intentionally traceable history of actions and decisions.
- Recover vs Resume: Recovery may involve fallback, repair, or a safe state; resume simply continues the prior workflow.
- Recovery Rate vs Success Rate: Recovery rate measures failed cases that were recovered; success rate may measure all cases that completed successfully.
- Error Rate vs Failure Rate: These metrics may be used similarly, but error rate can count signals/messages while failure rate usually counts unsuccessful operations.
- Availability vs Reliability: Availability measures whether a service is usable at a time; reliability is broader and includes consistent correct behavior.
- Reliability vs Robustness: Reliability concerns dependable operation; robustness concerns tolerating variation or adverse conditions.
- Robustness vs Resilience: Robustness resists disruption; resilience recovers after disruption.
- Fault Tolerance vs Fallback: Fault tolerance is a broader system capability; fallback is one mechanism that can contribute to it.
- Controlled Failure vs Silent Failure: A controlled failure is explicit and bounded; a silent failure is hidden or not communicated.
- Controlled Failure vs Fabricated Result: A controlled failure admits the result is unavailable; a fabricated result invents an answer despite failure.
- User-Facing Status vs Operator Log: A status message communicates to the user; an operator log captures diagnostic detail for system maintainers.
- Request vs Input: A request is an instruction or desired operation; input can include the request plus data and context.
- Output vs Result: Output is what the system returns; result emphasizes whether that output is the outcome expected or usable.
- AI System vs AI Model: A system includes workflows, tools, validation, and failure handling; a model is one component that produces predictions or content.
- Tool vs API: A tool is a callable capability in the AI workflow; an API is an interface through which a service may be accessed.
- External API vs External Tool: An API is a service interface; a tool is the capability as exposed to the AI system, possibly backed by an API.
- System Prompt vs Failure Policy: A system prompt can instruct behavior; a failure policy is an operational rule set for handling actual failure conditions.
- Structured Outputs vs Schema Validation: Structured outputs describe an output-generation constraint; schema validation checks whether the returned data satisfies the structure.
- Failure Modes vs Failure Handling: Failure modes describe ways a system can fail; failure handling describes what to do when one occurs.
- Tool Calling vs Tool Failure: Tool calling is the invocation workflow; tool failure is an unsuccessful invocation or tool result.
- Retry Policy vs Failure Policy: Retry policy governs repeated attempts; failure policy includes retry plus fallback, asking, review, and stop.
- Backoff vs Timeout: Backoff delays the next retry; timeout limits how long an operation may wait.
- Circuit Breaker vs Safe Stop: A circuit breaker blocks calls to a failing dependency; safe stop is the broader decision to end safely.
- Escalation vs Fallback: Escalation sends the case to a human or higher-level process; fallback keeps processing through an alternate automated path.
- Partial Result vs Valid Result: A partial result may be useful but incomplete; validity alone does not guarantee completeness.
- Incident vs Failure: A failure may be an isolated event; an incident is an operational event tracked for impact and response.
- Incident Response vs Failure Handling: Incident response coordinates significant operational events; failure handling can occur per request inside a product flow.
- MTTR vs Recovery Rate: MTTR measures time to recover; recovery rate measures how many failures are recovered.
- SLO vs SLA: An SLO is an internal or stated objective; an SLA is a formal service commitment, often with customer consequences.
- Failure Handling vs Error Recovery: Failure handling includes detection, classification, communication, review, and stopping; error recovery focuses on restoring operation.
- Safe Path vs Happy Path: The happy path is the expected successful route; the safe path is the route that avoids unsafe continuation, including during failure.

## Notes

- Raw collection intentionally keeps broad coverage, repeated wording, overlapping granularity, and related-context candidates; do not deduplicate at this stage.
- The primary evidence is the full body of `failure-handling.html`: page title and lede, definition, emergency-plan analogy, five process steps, two real-world examples, three explicit “What it is NOT” contrasts, related-concept tree, related links, takeaway, and video metadata.
- The page’s five explicit workflow nodes are preserved as individual candidates and as the full sequence: detect, classify, choose, recover, record.
- The page’s named detection signals are preserved separately: errors, timeouts, schema, and evidence.
- The page’s named failure classes are preserved separately: transient, input, tool, and safety failures.
- The page’s named response options are preserved separately: retry, fallback, ask, review, and stop. The page also separately names error return, human review, and safe stopping in the definition block.
- “Invalid JSON,” “valid data,” “validation error,” “timeout,” “fallback,” “clear status,” and “fabricated result” are retained as concrete mechanism and output candidates because they anchor the two examples.
- “Failure Handling ≠ Retry Only,” “Failure Handling ≠ Error Message,” and “Failure Handling ≠ Ignoring Errors” are retained as comparison candidates because they define boundaries for later glossary editing.
- “Usable result,” “safe path,” “uncertainty,” “visible uncertainty,” “controlled failure,” and “safe result” are retained separately because the page treats safe continuation and transparent failure as distinct ideas.
- The related-concept chain is preserved verbatim as a candidate: `Request → AI / Tool → Validate result → Retry / Fallback / Ask / Review / Stop`.
- The page links Structured Outputs, System Prompts, Failure Modes, and Tool Calling. These are kept as related-context candidates even where the source gives no full definition.
- Operational terms such as backoff, circuit breaker, observability, MTTR, SLO, error rate, and incident response are retained as potential expansion candidates because they naturally attach to the page’s retry, timeout, outage, recovery, and record concepts, but they are not claimed as explicitly defined by the source page.
- JSON and API are retained with abbreviation expansions because the examples use invalid JSON and an external API.
- The video block is source-page metadata, not an additional conceptual definition; video, independent explainer, visual explainer, captions, and video source remain available as raw candidates if the glossary pipeline indexes page UI vocabulary.
- The source page is beginner-oriented. Later editorial passes should preserve a plain-language explanation while distinguishing operational terms such as failure, error, timeout, outage, invalid output, and fabricated result.
