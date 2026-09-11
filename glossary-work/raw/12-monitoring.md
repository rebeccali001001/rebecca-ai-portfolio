# Topic 12 — Monitoring

## Topic Metadata

- **Module:** 12 · Enterprise AI Deployment
- **Topic:** Monitoring
- **Source file:** `monitoring.html`
- **Page title:** What Is AI Monitoring?
- **Source description:** Monitoring is the ongoing observation of an AI system during real-world use.
- **Collection mode:** Raw, maximal candidate capture. Candidates are kept in source order; repeated terms and overlapping phrase-level candidates are intentional and have not been deduplicated, normalized away, or deleted.
- **Scope:** Visible page copy, including headings, process labels, comparison cards, example labels, takeaway copy, and explanatory text. Decorative HTML/CSS structure is excluded unless it carries a domain concept.

## Glossary Candidates

| Candidate | Candidate type | Context / possible meaning | Source wording or location |
|---|---|---|---|
| AI Monitoring | Topic term | Monitoring applied to an AI system | Page title: “What Is AI Monitoring?” |
| Enterprise AI Deployment | Module term | The deployment context for the topic | Breadcrumb and back-link context |
| Monitoring | Core professional term | Ongoing observation of an AI system during real-world use | Page description and opening copy |
| ongoing observation | Definition phrase | Continuous or repeated watching rather than a one-time check | Opening lede |
| AI system | System concept | The system whose behavior is observed | Opening lede |
| real-world use | Operating-context term | Actual production use outside controlled testing | Opening lede |
| teams | Actor / stakeholder | People responsible for understanding and improving the system | Opening lede |
| system behaves | Behavior concept | The observable behavior of the deployed system | Opening lede |
| real users | User-context term | Actual users interacting with the system | Opening lede |
| real data | Data-context term | Data encountered in actual operation | Opening lede |
| real operating conditions | Environment term | The conditions under which the system is really run | Opening lede |
| Production feedback loop | Mechanism / process | Loop from deployed use through signals, evaluation, improvement, and redeployment | On-page navigation and process section |
| monitoring closes the production feedback loop | Mechanism phrase | Monitoring connects production behavior back to improvement work | Process-section heading and note |
| deployed system | Process node | The system after it has been put into operation | Process flow step 01 |
| real usage | Process node / usage term | Actual usage of the deployed system | Process flow step 02 |
| monitor | Process node / action | Observe production behavior and signals | Process flow step 03 |
| Quality | Monitoring dimension | Quality-related behavior or outcome | Monitor step signal list |
| Failures | Monitoring dimension | Cases where the system fails | Monitor step signal list |
| Latency | Metric / monitoring dimension | Response-time behavior | Monitor step signal list |
| Cost | Metric / monitoring dimension | Resource or monetary cost of use | Monitor step signal list |
| Usage | Metric / monitoring dimension | How much and whether the system is used | Monitor step signal list |
| Overrides | Human-intervention signal | Cases where a person overrides the system result | Monitor step signal list |
| signal | Monitoring concept | An observation that may indicate system behavior or change | Process flow step 04 |
| issue | Diagnostic concept | A problem detected from a production signal | Process flow step 04 |
| signal / issue | Process node | A signal or issue that triggers follow-up | Process flow step 04 |
| evaluate | Process action | Measure or investigate a detected issue | Process flow step 05 |
| improve | Process action | Change the system or workflow based on evidence | Process flow step 05 |
| deploy again | Process action | Return an improved system to production | Process flow step 05 |
| evaluation | Process node | The evaluation stage in the production feedback loop | Process flow step 05 |
| improvement | Process node | The improvement stage in the production feedback loop | Process flow step 05 |
| redeployment | Process concept | Deploying the improved system again | Implied by “deploy again” and the example’s “REDEPLOY” |
| Monitoring closes the production feedback loop | Repeated mechanism phrase | Same core claim retained as a separate raw occurrence | Process note |
| Why Monitoring Exists | Section concept | Rationale for monitoring in production | Section heading |
| test environment | Environment term | Controlled environment used before or apart from production | Comparison card |
| known examples | Testing concept | Inputs whose behavior is already known or anticipated | Test-environment card |
| controlled conditions | Testing concept | Conditions deliberately constrained during testing | Test-environment card |
| real world | Operating-context term | Uncontrolled production context | Comparison card |
| unexpected input | Input / failure-context term | Input not represented by known test examples | Real-world card |
| edge cases | Testing / reliability term | Unusual or boundary inputs and situations | Real-world card |
| usage changes | Drift / operations signal | Changes in how people use the system | Real-world card |
| operational failure | Failure type | Failure arising during actual operation | Real-world card |
| production | Operating environment | The live environment where users and data interact with the system | Note: “Production reveals things testing may miss.” |
| testing | Evaluation / validation activity | Pre-production or controlled checking of behavior | Note: “Production reveals things testing may miss.” |
| production reveals things testing may miss | Diagnostic principle | Live usage can expose behavior absent from testing | Section note |
| What Can Be Monitored | Scope concept | Categories of signals that can be observed | Section heading |
| usage | Monitoring dimension | Whether and how the system is used | Signals card |
| people | User concept | Human users of the system | Usage question |
| actually using it | Adoption signal | Whether intended users use the system in practice | Usage question |
| quality signals | Metric / signal category | Indicators of usefulness and correctness | Signals card |
| results | Output concept | System outputs being judged or acted upon | Quality question |
| useful | Quality criterion | Whether results help the workflow or user | Quality question |
| correct enough | Quality criterion | Whether results meet the required level of correctness | Quality question |
| failures | Monitoring dimension | Places where the system does not work as intended | Failures card |
| system fail | Failure behavior | The system failing during use | Failures question |
| escalate | Workflow / failure action | Passing a case to a human or another path | Failures question |
| latency | Metric / monitoring dimension | Time taken for a response | Latency card |
| response | System-output event | The system’s reply or result delivery | Latency question |
| fast enough | Performance criterion | Sufficient speed for the intended use | Latency question |
| workflow | Operational context | The surrounding business or user process | Latency and cost questions |
| cost | Metric / monitoring dimension | Resource or monetary burden of use | Cost card |
| each request | Unit of measurement | A single system interaction used for cost measurement | Cost question |
| workflow cost | Metric | Cost attributable to a complete workflow | Cost question |
| human overrides | Human-intervention metric | How often humans correct or replace results | Human overrides card |
| correct | Human action / quality signal | A person fixes the system’s result | Human overrides question |
| replace | Human action / quality signal | A person substitutes another result for the system’s result | Human overrides question |
| result | Output concept | The output that a person may correct or replace | Human overrides question |
| Monitoring vs Evaluation | Comparison concept | Distinguishes live observation from structured measurement | Section heading |
| monitoring | Core term, repeated occurrence | Ongoing observation during real use | Monitoring comparison card |
| ongoing observation during real use | Definition phrase | Monitoring’s page-level definition in contrast with evaluation | Monitoring card |
| evaluation | Core professional term | Structured measurement against criteria | Evaluation comparison card |
| structured measurement | Measurement concept | Deliberate, organized assessment | Evaluation card |
| criteria | Evaluation concept | Standards or conditions used for measurement | Evaluation card |
| monitoring finds issue | Process relationship | Monitoring detects a candidate problem | Concept tree |
| issue | Diagnostic concept, repeated occurrence | Problem passed to evaluation | Concept tree |
| Evaluation | Core professional term, repeated occurrence | Follow-up measurement after monitoring finds an issue | Concept tree |
| confirms | Evaluation outcome | Evaluation verifies whether the suspected issue is real | Concept tree |
| measures | Evaluation action | Evaluation quantifies the issue or performance | Concept tree |
| confirms / measures | Evaluation outcome phrase | Two possible functions of evaluation | Concept tree |
| Improvement | Process outcome | Change made after evaluation | Concept tree |
| Monitoring vs Logging | Comparison concept | Distinguishes behavioral interpretation from event recording | Section heading |
| logging | Core professional term | Recording system events | Logging comparison card |
| records events | Logging definition phrase | Logging stores or records events that occurred | Logging card |
| monitoring | Core term, repeated occurrence | Uses signals to understand behavior over time | Monitoring logging card |
| signals | Monitoring input | Observations used for interpretation | Monitoring logging card |
| understand behavior over time | Monitoring purpose phrase | Interpret changes and patterns across operation | Monitoring logging card |
| logs | Data / observability artifact | Recorded events that can support monitoring | Section note |
| support monitoring | Relationship phrase | Logs can be an input to monitoring | Section note |
| not the same thing | Distinction phrase | Logging and monitoring are related but distinct | Section note |
| One Real Example | Example marker | Concrete example used to explain the loop | Example section heading |
| AI Invoice Assistant | Example system | AI system handling invoice-related work | Example section heading |
| invoice | Domain object | Document processed by the assistant | Example system name |
| monitoring finds | Process action | Monitoring identifies a production pattern | Example flow label |
| 15% | Metric value | Reported share of cases requiring intervention | Example flow |
| handwritten invoices | Input category | Invoice inputs that create a notable override rate | Example flow |
| require override | Failure / intervention signal | Cases where the assistant’s output is not accepted directly | Example flow |
| override | Human-intervention term | Human replacement or correction of the system result | Example flow |
| evaluation | Process stage, repeated occurrence | Structured follow-up test of the observed pattern | Example flow |
| test handwritten cases | Evaluation action | Test cases representing handwritten invoices | Example flow |
| improvement | Process stage, repeated occurrence | Change made after testing | Example flow |
| OCR | Abbreviation / technology | Optical character recognition; a possible system improvement | Example flow |
| prompt | System-input / control term | Prompt change as an improvement lever | Example flow |
| workflow change | Operational improvement | Change to the surrounding process | Example flow |
| redeploy | Deployment action | Put the improved assistant back into use | Example flow |
| improved system | System state | System after an improvement change | Example flow |
| return the improved system to use | Deployment phrase | Redeploy the modified system for real operation | Example flow |
| Monitoring and Adoption | Relationship concept | Monitoring can reveal whether use translates into adoption | Section heading |
| system can technically work | Capability / outcome distinction | Technical operation does not guarantee value | Adoption definition |
| technically work | Technical success criterion | System functions at a technical level | Adoption definition |
| fail to create value | Business outcome failure | A working system may not produce useful value | Adoption definition |
| value | Business outcome concept | Benefit created by actual use and results | Adoption definition |
| only 10% of users use it | Adoption metric / example | Low usage rate indicating a possible adoption issue | Adoption concept tree |
| 10% | Metric value | Example percentage of users who use the system | Adoption concept tree |
| users | User population | People expected to use the system | Adoption concept tree |
| monitoring reveals | Diagnostic relationship | Monitoring surfaces a possible adoption issue | Adoption concept tree |
| possible adoption problem | Adoption diagnostic | Suspected problem with user uptake or usage | Adoption concept tree |
| adoption | Product / operations concept | User uptake and sustained use | Adoption heading and concept tree |
| What it is NOT | Boundary-setting concept | Explicitly separates monitoring from neighboring practices | Section heading |
| Monitoring ≠ Evaluation | Do-not-confuse pair | Monitoring is not the same as structured evaluation | Misconception card |
| Monitoring ≠ Logging | Do-not-confuse pair | Monitoring is not the same as event logging | Misconception card |
| Monitoring ≠ One-time Testing | Do-not-confuse pair | Monitoring is not a single test event | Misconception card |
| Monitoring ≠ Continuous Improvement | Do-not-confuse pair | Monitoring enables improvement but is not improvement itself | Misconception card |
| one-time testing | Testing concept | A single or bounded testing activity | Misconception card |
| continuous improvement | Improvement concept | Repeated change over time based on evidence | Misconception card |
| Remember this | Takeaway marker | Summary of the topic | Takeaway heading |
| monitoring observes | Core mechanism phrase | Monitoring watches system behavior | Takeaway note |
| how an AI system behaves | Behavior phrase | The behavior being observed | Takeaway note |
| real use | Operating-context term | Actual use in operation | Takeaway note |
| detect issues | Monitoring purpose | Identify problems from live behavior | Takeaway note |
| improve it | Improvement purpose | Make the system better after detection and measurement | Takeaway note |
| over time | Temporal concept | Monitoring and improvement occur across ongoing operation | Takeaway note |

## Potential Missing Concepts

These are adjacent concepts that are suggested by the page but not explicitly defined in the visible copy. They remain candidates for follow-up glossary work rather than being silently inserted into the raw source table:

- observability
- metrics, logs, and traces as an observability model
- dashboards
- alerts and alert thresholds
- anomaly detection
- incident response
- service-level objectives (SLOs) and service-level agreements (SLAs)
- data drift and concept drift
- model drift
- input and output data quality
- feedback collection
- user feedback
- precision, recall, accuracy, and other formal quality metrics
- uptime and availability
- throughput
- error rate
- cost per token, request, or workflow
- privacy and sensitive-data handling in monitoring data
- monitoring sampling and retention
- audit trail
- human-in-the-loop review queues
- rollback and version comparison
- experiment or release monitoring

## Aliases / Synonyms

The following are candidate aliases or normalization relationships for later glossary curation. They are intentionally not used to merge or delete raw rows above.

- **AI Monitoring** ↔ AI system monitoring ↔ production AI monitoring
- **Monitoring** ↔ production monitoring ↔ runtime monitoring ↔ operational monitoring ↔ real-use observation
- **ongoing observation** ↔ continuous observation ↔ ongoing production observation
- **real-world use** ↔ live use ↔ production use ↔ actual operation
- **production feedback loop** ↔ live-system feedback loop ↔ operational feedback loop
- **deployed system** ↔ production system ↔ live system
- **real usage** ↔ actual usage ↔ live usage
- **quality signals** ↔ quality indicators ↔ usefulness/correctness signals
- **failures** ↔ errors ↔ failure events ↔ unsuccessful cases
- **latency** ↔ response time ↔ turnaround time
- **cost** ↔ usage cost ↔ request cost ↔ workflow cost
- **overrides** ↔ human overrides ↔ manual corrections ↔ human intervention
- **evaluation** ↔ structured evaluation ↔ criteria-based measurement ↔ performance assessment
- **logging** ↔ event logging ↔ event recording ↔ log collection
- **signal** ↔ monitoring signal ↔ operational signal ↔ telemetry signal
- **issue** ↔ problem ↔ detected defect ↔ incident candidate
- **improvement** ↔ system improvement ↔ corrective improvement ↔ iteration
- **deploy again** ↔ redeploy ↔ re-release ↔ return to production
- **adoption** ↔ user adoption ↔ uptake ↔ sustained usage
- **OCR** ↔ optical character recognition
- **one-time testing** ↔ single-run testing ↔ point-in-time testing
- **continuous improvement** ↔ iterative improvement ↔ ongoing optimization

## Do Not Confuse Candidates

- **Monitoring vs Evaluation:** Monitoring is ongoing observation during real use; evaluation is structured measurement against criteria. Monitoring can find an issue, while evaluation confirms or measures it.
- **Monitoring vs Logging:** Logging records events. Monitoring uses signals, including logs, to understand behavior over time. Logs can support monitoring, but the two are not the same thing.
- **Monitoring vs One-time Testing:** Testing in a controlled environment uses known examples and controlled conditions; monitoring observes the deployed system with unexpected input, edge cases, usage changes, and operational failures.
- **Monitoring vs Continuous Improvement:** Monitoring supplies evidence and detects issues; continuous improvement is the subsequent change process. Monitoring is not the change itself.
- **Monitoring vs Adoption:** Monitoring may reveal a possible adoption problem, but monitoring is the observation mechanism and adoption is the user-uptake outcome.
- **Quality signals vs Evaluation criteria:** Quality signals are observed indicators from use; evaluation criteria are the standards used in structured measurement.
- **Overrides vs Failures:** An override is a human correction or replacement signal. It may indicate a failure or quality issue, but an override is not identical to every kind of system failure.
- **Latency vs Cost:** Latency concerns response speed; cost concerns the burden of each request or workflow.
- **Usage vs Adoption:** Usage is an observable activity signal; adoption is the broader uptake or value-creation relationship.
- **Production feedback loop vs Continuous Improvement:** The feedback loop includes monitoring, issue detection, evaluation, improvement, and redeployment; continuous improvement is only one related process concept.
- **Logs vs Signals:** Logs are recorded events; signals are observations used to understand behavior. A log may become an input to monitoring but is not automatically a monitoring conclusion.
- **Technically works vs Creates value:** Technical operation does not guarantee that users adopt the system or that it creates value.
- **Redeploy vs Improve:** Improvement changes the system or workflow; redeployment returns the changed system to use.

## Notes

- Candidates were captured from the complete visible body copy of `monitoring.html`, including repeated occurrences in headings, process flows, comparison cards, example cards, concept trees, and the final takeaway.
- The table intentionally preserves repeated terms such as `monitoring`, `evaluation`, `usage`, `failures`, `improvement`, and `issue` when they recur in different source locations.
- Both atomic terms and longer explanatory phrases are retained because the later glossary pass may need entries at either granularity.
- `OCR` is the only explicit technical abbreviation in the page body; its expansion is recorded under Aliases / Synonyms as a candidate normalization.
- Percentages `15%` and `10%` are retained as raw example metric values, not generalized benchmarks.
- “Potential Missing Concepts” contains adjacent follow-up candidates inferred from the topic boundary; they are clearly separated from source-grounded raw candidates.
- No website files, generated site assets, or GitHub state were modified.
