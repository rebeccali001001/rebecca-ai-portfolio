# Topic 11 · Functional Tests

## Topic Metadata

- **Module:** 11 · Evaluation, Safety & Reliability
- **Topic:** Functional Tests
- **Source page:** functional-tests.html
- **Page title:** What are Functional Tests? · Evaluation & Reliability
- **Page eyebrow:** 07 · Evaluation & Reliability · Topic 04
- **Topic overview source:** evaluation-safety-reliability.html identifies this topic family as Module 11.
- **Extraction scope:** Full visible page body, including the title, lede, on-page navigation, definition, analogy, five-step process, real-world examples, comparison cards, related-concept chain, related-topic links, takeaway, and video metadata.
- **Collection policy:** Raw candidate inventory only. Keep technical terms, mechanisms, workflow nodes, observable behaviors, outputs, metrics, abbreviations, important body words, aliases/synonyms, repeated labels, and potentially confusable concepts for later review. Candidates are intentionally broad, overlapping, and not deduplicated.

## Glossary Candidates

| Candidate | Category | Working definition / why it matters | Page evidence or context |
|---|---|---|---|
| Functional Tests | Core concept / title form | Tests that check whether an AI system performs the task it is supposed to perform. | Page title; lede |
| functional test | Core concept | A test that checks whether an AI system produces the required result for a defined task. | Definition |
| functional testing | Process / alias | The practice of checking whether a system performs required tasks correctly. | Candidate expansion of functional test |
| functional-test | Hyphenated variant | Hyphenated adjective form used when describing a test or workflow. | Candidate spelling variant |
| task test | Alias / shorthand | A test centered on whether a defined task works. | Candidate shorthand from the definition |
| behavior test | Alias / test type | A test of externally observable system behavior. | “It tests behavior” |
| behavioral test | Alias / test type | Variant spelling for a test of observable behavior. | Candidate spelling variant |
| AI system | System concept | The system whose task performance and output behavior are being checked. | Definition; examples |
| AI | Domain term | Artificial intelligence capability under evaluation. | “AI system” |
| system | General system term | The tested software or AI product that receives inputs and produces results or actions. | Definition; process |
| task | Core unit | A defined job the AI system is expected to perform. | “defined task”; process |
| defined task | Test scope | A task whose required behavior or result has been specified before testing. | Definition |
| required task | Requirement concept | The task the system must successfully perform. | Takeaway; definition |
| task requirement | Requirement concept | The expected job or behavior against which the system is checked. | Candidate synthesis from required task |
| required result | Expected output | The result a system must produce for a test case to work. | Definition |
| required behavior | Expected behavior | The behavior the system must exhibit for a defined case. | Process; takeaway |
| expected behavior | Oracle / acceptance concept | The behavior used as the comparison target during checking. | Process; concept tree |
| expected result | Expected output | The result against which an observed result is compared. | Candidate synonym for expected behavior/result |
| observable behavior | Evaluation target | Behavior that a user or another system can observe. | Definition paragraph |
| observable result | Evaluation target | A result visible to a user or calling system and therefore testable. | Definition; analogy |
| observed result | Evaluation target | The actual result recorded after the AI system is called. | Candidate wording from “record” and “result” |
| actual result | Test output | What the system actually returned or did in a case. | Candidate contrast with expected result |
| output | Test output | Information or action produced by the system for the input. | Examples; functional test definition |
| answer | Output type | A textual answer that can be checked for task completion. | “check the answer” |
| format | Output property | The structure or presentation format the test may require. | “check ... format” |
| tool action | Action output | An action taken through a tool that can be checked as functional behavior. | Definition |
| tool call | Tool-use output | A call to an external tool made by the system with required fields or arguments. | Calendar example |
| refusal | Behavioral outcome | A refusal response that may be the required behavior for a case. | Definition |
| refusal behavior | Behavioral outcome | The system’s observable decision to decline a request. | Candidate expansion of refusal |
| missing information | Input condition | A case where necessary information is absent and handling must be checked. | Definition |
| missing-information handling | Failure/behavior case | The system’s behavior when required information is not available. | Definition |
| handling of missing information | Behavioral requirement | Checking whether the system responds appropriately to incomplete information. | Definition |
| user | Actor / observer | A person who can observe the AI system’s behavior or result. | Definition |
| another system | Actor / observer | A downstream or calling system that can observe the AI system’s behavior. | Definition |
| user-observable | Evaluation qualifier | Visible or otherwise inspectable by a user. | “user ... can observe” |
| system-observable | Evaluation qualifier | Visible or inspectable by another system. | “another system can observe” |
| known input | Test input | A predetermined input used to exercise a defined task. | Analogy; process |
| fixed request | Test input | A stable request reused as part of a controlled test case. | Prepare step |
| test data | Test input / fixture | Data supplied with a test request to exercise the system. | Prepare step |
| input | Test input | Request or data supplied to the AI system. | Process; examples |
| request | Test input | A user or system instruction that starts a functional test case. | Fixed request; examples |
| test request | Alias / test input | A request prepared for a functional test. | Candidate synthesis |
| defined case | Test scope | A specific case with an input and expected behavior/result. | Takeaway |
| test case | Test unit | A planned case connecting an input, an AI system, an observed result, and an expected behavior. | Related concept chain |
| case | Test unit | A bounded scenario used to test one expected behavior. | “defined case”; “planned case” |
| planned case | Test unit | A test scenario prepared in advance rather than observed from live traffic. | Production monitoring comparison |
| known situation | Analogy / test fixture | A predetermined scenario in the driving-test analogy. | Driving test analogy |
| situation | Analogy / input condition | The circumstances presented to the driver or AI system. | Analogy |
| driving test | Analogy | A familiar test that gives a driver a known situation and checks the observable result. | Analogy lead |
| driver | Analogy actor | The person whose driving behavior is checked in the analogy. | Driving-test analogy |
| driving | Analogy behavior | The observable activity being evaluated in the analogy. | Driving-test analogy |
| test | General evaluation mechanism | A planned check of whether an expected behavior or result occurs. | All sections |
| check | Verification operation | Comparing observed behavior or output with an expectation. | Process step 4 |
| checking | Verification process | The activity of comparing the result with expected behavior or schema. | Process |
| verification | Alias / quality operation | Establishing whether the required behavior occurred. | Candidate expansion of check |
| validation | Related quality operation | Confirming that a system meets a required task or expectation. | Candidate expansion |
| define | Process step | First step: choose and state the task the system must do. | Step 1 |
| Define | Process label | Capitalized label for the first process stage. | “1 · Define” |
| choose the task | Process action | Selecting the task that the functional test will exercise. | Define step |
| state what the system must do | Requirement action | Expressing the expected task or behavior before running the test. | Define step |
| prepare | Process step | Second step: establish the input and test data. | Step 2 |
| Prepare | Process label | Capitalized label for the second process stage. | “2 · Prepare” |
| set the input | Process action | Supplying a fixed request and test data for the case. | Prepare step |
| run | Process step | Third step: execute the test by calling the system. | Step 3 |
| Run | Process label | Capitalized label for the third process stage. | “3 · Run” |
| call the system | Process action | Send the prepared input to the AI system under test. | Run step |
| system call | Workflow event | The invocation that starts system behavior for a test case. | Candidate alias |
| execute the test | Process action | Perform the planned call using the prepared request and data. | Candidate expansion |
| record | Process action | Capture the system’s response or action for later comparison. | Run step |
| record the response | Evidence action | Store the response produced by the system. | Run step |
| record the action | Evidence action | Store the action taken by the system, including a tool action. | Run step |
| response | Output / evidence | The system’s returned answer or other response to the request. | Run step; examples |
| action | Output / evidence | Observable operation performed by the system. | Run step; tool example |
| Check | Process label | Capitalized label for the fourth process stage. | “4 · Check” |
| compare the result | Verification action | Evaluate actual output or action against the test expectation. | Check step |
| comparison | Verification mechanism | The act of matching observed behavior to an expected target. | Check step |
| result comparison | Verification mechanism | Comparison of the system’s result with expected behavior or schema. | Candidate alias |
| schema | Output contract | A structural specification that can be used to check the result. | Check step |
| expected schema | Output contract | The schema the observed result is expected to satisfy. | Check step; candidate expansion |
| schema check | Verification operation | Checking whether the result conforms to an expected schema. | Candidate synthesis |
| decide | Process step | Fifth step: make a pass/fail or investigation decision. | Step 5 |
| Decide | Process label | Capitalized label for the fifth process stage. | “5 · Decide” |
| pass | Test outcome | Outcome indicating the required behavior was observed. | “Pass or investigate”; concept tree |
| pass result | Test outcome | A passing result for a functional test case. | Candidate expansion |
| pass/fail | Outcome pair | Binary shorthand for the decision after checking a case. | Concept tree |
| fail | Test outcome | Outcome indicating the expected behavior was not observed or needs investigation. | “Pass / Fail” |
| failure | Test outcome / defect signal | A case where observed behavior does not meet the expectation. | Track failures |
| investigate | Process action | Follow up on a failed or uncertain result. | Step 5 |
| investigation | Failure-analysis process | Examination of a failed case to understand or fix it. | Candidate noun form |
| track failures | Operations action | Record and follow failure cases over time. | Decide step |
| failure tracking | Operations process | Keeping a record of failed functional test cases. | Candidate noun form |
| improve the system | Iteration action | Modify or refine the system in response to test results. | Decide step |
| system improvement | Iteration outcome | Better system behavior resulting from investigating and addressing failures. | Candidate noun form |
| improve | Iteration operation | Make changes based on functional test evidence. | “improve the system” |
| input → system → output | Simplified test relationship | A functional test connects what is supplied, what is invoked, and what is produced. | Examples; process |
| input / system / output | Test model | Three-part framing used by the examples. | Real-world examples |
| expected behavior comparison | Test mechanism | Compare an observed response/action with the behavior specified for the case. | Check step |
| observable result check | Test mechanism | Inspect the result visible to a user or another system. | Definition; analogy |
| support reply | Everyday example | A customer-support response used to demonstrate a functional case. | Everyday example heading |
| customer support | Domain example | Context in which an AI system answers a user’s support question. | Support reply example |
| password reset | Support task | Example task asking how to reset a password. | Example input |
| reset my password | Example request | Exact natural-language request used in the support example. | Input |
| approved reset steps | Expected content | The sanctioned steps the system should return for the password-reset request. | System line |
| reset steps | Procedure output | Instructions for completing the password reset. | Example output |
| helpful answer | Output quality/property | A useful response that fulfills the support request. | Output line |
| invented policy | Incorrect output | Policy content made up by the system rather than drawn from approved information. | Output line |
| no invented policy | Negative requirement | Requirement that the support answer avoid fabricated policy. | Output line |
| policy | Domain knowledge / constraint | Rules or guidance that the support answer must not invent. | Support example |
| AI product example | Example category | The second example category showing functional testing in an AI product. | Example heading |
| AI product | Product context | A product containing an AI system whose behavior is checked. | Example heading |
| calendar event | Tool-action object | Event that the system is asked to create through a calendar tool. | Tool-call example |
| create a calendar event | Tool-use task | Functional task of creating an event. | Example input |
| calendar | External system/tool domain | External service used to create the event. | Calendar tool |
| calendar tool | External tool | Tool the AI system calls to create a calendar event. | Example system line |
| required fields | Tool-call contract | Fields that must be present for the calendar tool call to be valid. | Example system line |
| valid event | Successful tool output | A correctly formed event returned or created by the tool. | Example output |
| clear error | Error output | An understandable error when the event cannot be created or the request is invalid. | Example output |
| error | Failure output | Explicit failure information that can be checked as an expected outcome. | Calendar example |
| valid | Output property | Conforming to the required fields or expected contract. | Valid event |
| invalid | Output property / negative case | Not conforming to the required fields or expected contract. | Candidate contrast with valid |
| field | Structured-data unit | A required piece of information in the calendar event request. | Required fields |
| required field | Structured-data constraint | A field that must be supplied for a valid tool action. | Required fields |
| functional behavior | Test target | Whether the system does the required job in an observable way. | Takeaway; definition |
| task works | Functional outcome | The task produces the required result when tested. | Quality-score comparison |
| works | Informal outcome | Informal expression of successful task behavior. | “checks whether a task works” |
| quality score | Quality metric | A measure of how good a result is along a chosen dimension, distinct from whether the task works. | What it is NOT |
| quality | Evaluation dimension | Degree to which a result is good along a chosen dimension. | Quality score comparison |
| score | Metric value | Numeric or categorical value measuring a quality dimension. | Quality score |
| chosen dimension | Metric dimension | The particular aspect along which result quality is measured. | Quality score |
| quality measurement | Evaluation mechanism | Measuring goodness of a result rather than binary task functionality. | Candidate alias |
| unit test | Software test type | A test of a smaller code component in isolation. | What it is NOT |
| code component | Software unit | A smaller implementation component tested separately by a unit test. | Unit-test comparison |
| component | Software unit | An isolated part of code or a system. | Unit-test comparison |
| isolation | Test boundary | Testing a code component separately from the larger system. | Unit-test comparison |
| component in isolation | Unit-test scope | A code component tested independently of system-level behavior. | Unit-test comparison |
| production monitoring | Operations practice | Watching live behavior after release. | What it is NOT |
| monitoring | Operations practice | Observing live behavior after the system is released. | Production monitoring |
| live behavior | Runtime behavior | Actual behavior of the released system under real use. | Production monitoring |
| release | Lifecycle event | Point after which production monitoring watches live behavior. | Production monitoring |
| post-release | Lifecycle stage | Time or activity after a system is released. | Production monitoring |
| production | Deployment context | Live operating environment in which monitoring occurs. | Production monitoring |
| planned case | Test context | A preselected case against which a functional test runs. | Functional test vs monitoring |
| live case | Monitoring context | A naturally occurring production interaction, contrasted with a planned case. | Candidate contrast |
| offline test | Test context | A test run against prepared inputs outside live operation. | Candidate alias from planned case |
| online monitoring | Operations context | Monitoring of live behavior after release. | Candidate alias for production monitoring |
| test case → AI system | Concept relationship | The test case supplies the case to the system under test. | Related concept chain |
| AI system → observable result | Concept relationship | The system produces a result that can be observed. | Related concept chain |
| observable result → expected behavior | Comparison relationship | The observed result is compared with the expected behavior. | Related concept chain |
| expected behavior → pass/fail | Decision relationship | The comparison leads to a pass or fail outcome. | Related concept chain |
| Failure Modes | Related concept / topic link | Patterns or categories of ways an AI system can fail. | Explore next |
| failure modes | Alias / related concept | Lowercase form of Failure Modes. | Related-topic chip |
| Evaluation | Related concept / topic link | Broader process of measuring or judging AI-system performance. | Explore next |
| evaluation | Alias / related concept | Lowercase form of Evaluation. | Related-topic chip |
| Deployment Readiness | Related concept / topic link | Determining whether a system is ready to be released or used. | Explore next |
| deployment readiness | Alias / related concept | Lowercase form of Deployment Readiness. | Related-topic chip |
| Structured Outputs | Related concept / topic link | Outputs constrained to a defined structure or schema. | Explore next |
| structured outputs | Alias / related concept | Lowercase form of Structured Outputs. | Related-topic chip |
| Failure Handling | Related concept / topic link | Responses and procedures for failed or invalid cases. | Explore next |
| failure handling | Alias / related concept | Lowercase form of Failure Handling. | Related-topic chip |
| test chain | Relationship model | The sequence from test case through system and observed result to pass/fail. | Related-concept tree |
| concept tree | Navigation/relationship device | Visual text representation of related functional-test concepts. | Related section |
| Remember this | Takeaway label | Section label introducing the short summary. | Takeaway heading |
| takeaway | Summary concept | A concise statement of the central functional-test idea. | Page section |
| required job | Task requirement | The job the AI system must do for a defined case. | Takeaway |
| Independent explainer | Media label | Label for the page’s standalone explainer video. | Video section |
| visual explainer | Media type | A video intended to explain functional tests visually. | Video metadata |
| video | Media artifact | Video resource associated with the topic page. | Video section |
| video playback | Media behavior | Browser ability to play the explainer video. | Video fallback text |
| English captions | Accessibility asset | English caption track provided for the video. | Video track metadata |
| captions | Accessibility asset | Text synchronized with the video for accessibility or comprehension. | Video track |
| poster | Media asset | Preview image shown before the video plays. | Video element |
| source | Media asset | Video file resource used by the page. | Video element |
| functional-tests.mp4 | Media filename | MP4 explainer resource referenced by the page. | Video source |
| functional-tests.vtt | Media filename | WebVTT English caption resource referenced by the page. | Video track |
| functional-tests.png | Media filename | Poster image resource referenced by the page. | Video poster |
| WebVTT | Caption format | Caption-track format implied by the .vtt resource. | Candidate expansion of video track format |
| playback fallback | Media behavior | Message shown when the browser does not support video playback. | Video fallback text |

## Potential Missing Concepts

These concepts are useful for a fuller glossary of functional testing but are not fully defined in the source page. They are retained as follow-up candidates rather than being presented as page-defined concepts:

- test oracle, oracle, assertion, acceptance criterion, pass criterion, fail criterion
- expected output, reference answer, golden answer, ground truth, baseline
- test suite, test dataset, test fixture, test case ID, test run, test report
- regression test, integration test, end-to-end test, contract test, smoke test, sanity test
- happy path, negative test, edge case, boundary case, corner case, adversarial test
- refusal test, missing-information test, tool-call test, tool-use test, schema validation test
- output validator, response validator, structured-output validator, field-level validation
- exact match, string match, semantic match, semantic similarity, rubric-based evaluation
- pass rate, failure rate, success rate, functional coverage, test coverage, task coverage
- quality score calibration, evaluator agreement, inter-rater agreement, false positive, false negative
- deterministic test, stochastic test, reproducibility, repeatability, random seed
- temperature, sampling, model version, prompt version, system-prompt version
- flaky test, flakiness, nondeterministic output, test instability
- evaluator, human evaluation, automated evaluation, LLM-as-judge, judge model
- expected side effect, side effect, state change, idempotency, duplicate action
- tool schema, argument validation, API contract, request schema, response schema
- timeout, retry, retry policy, rate limit, authentication, authorization, permission
- mock, stub, fake service, sandbox, test environment, staging environment
- continuous integration, CI, continuous delivery, CD, release gate, deployment gate
- production smoke test, canary test, post-release check, online evaluation
- observability, logging, metrics, traces, alerting, dashboard, incident
- latency, response time, throughput, availability, reliability, error budget
- test isolation, environment isolation, dependency isolation, external-service dependency
- test data privacy, synthetic data, anonymized data, sensitive data handling
- regression baseline, before/after comparison, change impact, root-cause analysis

## Aliases / Synonyms

Keep these as separate raw candidates until the later glossary pass decides whether to merge them:

| Candidate | Possible alias/synonym relationship |
|---|---|
| Functional Tests | functional test; functional testing; task test |
| functional test | functional testing; behavior test; behavioral test |
| AI system | AI; system under test; tested system |
| defined task | required task; task requirement; required job |
| required result | expected result; expected output; actual-vs-expected target |
| required behavior | expected behavior; functional behavior |
| observable behavior | observable result; user-observable behavior; system-observable behavior |
| result | output; observed result; actual result |
| answer | response; textual output |
| tool action | action output; external action; side-effecting action |
| tool call | tool-use call; external-tool call; function call |
| missing information | incomplete information; missing-input case |
| handling of missing information | missing-information handling; incomplete-input handling |
| input | request; test input; test request |
| fixed request | known input; prepared request; controlled input |
| test data | fixture data; test fixture; prepared data |
| test case | defined case; planned case; functional case |
| known situation | test situation; prepared scenario; test scenario |
| driving test | driving examination; driving-test analogy |
| define | choose the task; state the requirement; specify the task |
| prepare | set the input; prepare the test case; configure test data |
| run | call the system; execute the test; invoke the system |
| record | capture; log; store the response/action |
| check | compare; verify; validate; inspect |
| compare the result | result comparison; expected-behavior check; output comparison |
| expected behavior | expected result; expected output; acceptance behavior |
| schema | expected schema; output contract; response structure |
| decide | determine outcome; classify result; make the test decision |
| pass | pass result; successful case; meets expectation |
| fail | failure; failing case; does not meet expectation |
| investigate | analyze failure; perform investigation; diagnose the case |
| track failures | failure tracking; record failures; monitor failed cases |
| improve the system | system improvement; fix the system; iterate on the system |
| support reply | customer-support answer; support response |
| password reset | password-reset task; reset-password request |
| approved reset steps | sanctioned reset steps; expected support instructions |
| helpful answer | useful response; task-completing answer |
| invented policy | fabricated policy; made-up policy; unsupported policy |
| calendar event | event; calendar object; scheduled event |
| calendar tool | calendar API; event-creation tool |
| required fields | required arguments; mandatory fields; field requirements |
| valid event | valid calendar object; successful event creation |
| clear error | understandable error; explicit failure response |
| quality score | quality metric; quality measure; dimension score |
| quality | result quality; goodness of result |
| unit test | component test; isolated code test |
| code component | unit; software component; isolated component |
| isolation | component isolation; test isolation |
| production monitoring | live monitoring; online monitoring; post-release monitoring |
| live behavior | production behavior; runtime behavior |
| planned case | offline case; prepared test case |
| Failure Modes | failure modes; failure patterns |
| Evaluation | evaluation; assessment; measurement |
| Deployment Readiness | release readiness; deployment readiness |
| Structured Outputs | structured output; schema-constrained output |
| Failure Handling | failure handling; error handling; failure response |
| pass/fail | binary outcome; test decision; success/failure |
| functional-tests.mp4 | functional tests explainer video; video source |
| functional-tests.vtt | English caption track; WebVTT captions |
| functional-tests.png | video poster; preview image |

## Do Not Confuse Candidates

| Candidate A | Candidate B | Distinction suggested by the page |
|---|---|---|
| Functional test | Quality score | A functional test checks whether a task works; a quality score measures how good the result is along a chosen dimension. |
| Functional test | Unit test | A functional test checks observable system behavior; a unit test checks a smaller code component in isolation. |
| Functional test | Production monitoring | A functional test runs against a planned case; production monitoring watches live behavior after release. |
| Functional testing | Evaluation | Functional testing is one task/behavior check; evaluation is the broader activity of judging system performance. |
| Functional test | Test case | The functional test is the check; the test case is the defined input/expectation scenario being checked. |
| Test case | Test data | A test case includes the scenario and expected behavior; test data is the input data used within it. |
| Test case | Fixed request | A test case is the whole planned unit; a fixed request is one controlled input in that case. |
| Input | Output | Input is supplied to the AI system; output is produced by it. |
| Request | Response | The request enters the system; the response is returned after the system acts. |
| Expected result | Actual result | The expected result is the comparison target; the actual result is what the system produced. |
| Expected behavior | Observable behavior | Expected behavior is the target; observable behavior is what can be seen and checked. |
| Observable result | Quality score | An observable result is what the system returned or did; a quality score is a measure assigned along a quality dimension. |
| Answer | Tool action | An answer is a returned response; a tool action is an operation the system performs through a tool. |
| Tool action | Tool call | A tool call is the invocation/interface event; a tool action is the resulting operation or effect. |
| Tool call | Calendar event | The call requests an operation; the calendar event is the object created or returned. |
| Required fields | Valid event | Required fields are constraints on the tool input; a valid event is an output/object satisfying the constraints. |
| Clear error | Valid event | A valid event indicates successful task completion; a clear error is an explicit failure outcome. |
| Refusal | Error | A refusal is a behavioral response that may be the correct expected behavior; an error signals a failure or invalid operation. |
| Missing information | Missing-data failure | Missing information is an input condition; a missing-data failure is one possible result of handling it poorly. |
| Schema | Format | A schema specifies structural rules; format is the broader property of how an output is represented. |
| Schema | Quality score | A schema check asks whether structure conforms; a quality score asks how good the result is along a dimension. |
| Check | Decide | Check compares the result with the expectation; decide assigns an outcome or chooses investigation. |
| Pass | Success rate | Pass is the result for one case; success rate is an aggregate metric across cases. |
| Fail | Failure rate | Fail is the result for one case; failure rate aggregates failures across cases. |
| Failure | Failure mode | A failure is an unsuccessful case; a failure mode is a recurring pattern or category of failures. |
| Investigate | Improve the system | Investigation examines a failed case; improvement changes the system based on findings. |
| Track failures | Production monitoring | Tracking failures from planned tests records test outcomes; production monitoring watches live released behavior. |
| Planned case | Live case | A planned case is prepared for testing; a live case occurs in real production traffic. |
| Offline test | Online monitoring | An offline test runs a prepared case; online monitoring observes live behavior. |
| User | Another system | A user is a human observer/caller; another system is a software observer/caller. |
| AI system | Another system | The AI system is the component under test; another system may be the external observer or caller. |
| System | Component | A system is the tested whole or service; a component is a smaller code unit. |
| Unit test | Integration test | A unit test isolates a code component; an integration test checks interactions among components. |
| Functional test | End-to-end test | A functional test focuses on required behavior for a case; an end-to-end test emphasizes the full path across integrated layers. |
| Functional test | Regression test | A functional test checks a case; a regression test checks whether previously working behavior remains working after change. |
| Quality | Functionality | Functionality asks whether the required task works; quality asks how good the result is along a chosen dimension. |
| Reliability | Functional correctness | Functional correctness is whether the defined behavior occurs; reliability includes consistency and dependable operation across cases/time. |
| Structured Outputs | Schema | Structured Outputs is a broader output mode/concept; a schema is the structural contract used to describe or check it. |
| Failure Handling | Functional test | Failure handling describes what the system does when failure occurs; functional testing checks whether a behavior, including error/refusal behavior, is correct. |
| Deployment Readiness | Functional test | A functional test supplies evidence for readiness; deployment readiness is the broader release decision. |
| Production monitoring | Functional test | Monitoring watches live behavior after release; a functional test is a planned check before or alongside release. |
| Quality score | Pass/fail | A quality score can be graded or continuous; pass/fail is the case-level functional decision shown on the page. |
| Exact match | Helpful answer | Exact match requires a prescribed string/content match; a helpful answer may satisfy the task without being identical. |
| Approved reset steps | Invented policy | Approved reset steps are sanctioned content; invented policy is unsupported content that the example explicitly rejects. |
| Valid event | Clear error | These are alternative outcomes in the calendar example: success with a valid event or explicit failure with a clear error. |
| Response | Action | A response is returned information; an action is an operation performed by the system. |
| Video | Video captions | The video is the media artifact; captions are synchronized text associated with it. |
| Video poster | Video source | The poster is a preview image; the source is the playable media file. |

## Notes

- The source page defines a functional test as checking whether an AI system produces the required result for a defined task.
- The source explicitly says the test can check the answer, format, tool action, refusal, or handling of missing information. These are separate raw candidates because they represent distinct observable behaviors and outcome types.
- The source’s driving-test analogy is part of the visible body and is retained: a known situation is supplied and the observable result is checked.
- The visible five-step process is: **Define → Prepare → Run → Check → Decide**.
- The process expands to: **choose the task → set the input → call the system → record the response or action → compare the result with expected behavior or schema → pass or investigate → track failures and improve the system**.
- The two worked examples use different output types: a support answer and a calendar-tool action.
- In the support example, the important functional requirement is not merely answering the question; it is returning approved reset steps in a helpful answer with no invented policy.
- In the calendar example, the expected behavior includes calling the calendar tool with required fields, followed by either a valid event or a clear error.
- The page’s explicit comparison set is: **Functional Test ≠ Quality Score**, **Functional Test ≠ Unit Test**, and **Functional Test ≠ Production Monitoring**.
- The related-concept chain is: **Test case → AI system → Observable result → Expected behavior → Pass / Fail**.
- The page names schema as a possible comparison target but does not define a particular schema language, validator, or structured-output contract.
- The page uses pass/fail as the decision language but does not provide numerical pass-rate, failure-rate, coverage, latency, or quality-score metrics.
- The page does not specify whether the AI system is deterministic, how many times a case should be repeated, or how stochastic outputs should be judged.
- The page does not describe test-suite organization, regression testing, CI/CD integration, mocks, staging environments, test oracles, acceptance criteria, or release gates; these are retained under Potential Missing Concepts.
- “Production monitoring” is explicitly distinguished from a planned functional test because it watches live behavior after release.
- The related-topic links are retained as candidates even though their linked pages contain the fuller definitions: Failure Modes, Evaluation, Deployment Readiness, Structured Outputs, and Failure Handling.
- The video section contributes the visible media concepts and filenames: functional-tests.mp4, functional-tests.vtt, and functional-tests.png; the file itself is not a glossary definition.
- The page source contains a taxonomy mismatch worth preserving in metadata: the topic page eyebrow says **07 · Evaluation & Reliability · Topic 04**, while the parent overview page identifies the topic family as **11 · Evaluation, Safety & Reliability**. The requested output is therefore named with the Module 11 convention.
- Repeated labels, lowercase/uppercase forms, hyphenated variants, aliases, analogy words, workflow nodes, and broader follow-up concepts are intentionally retained for later deduplication and editorial review.
