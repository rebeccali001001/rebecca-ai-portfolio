# Topic 11 · Deployment Readiness

## Topic Metadata

- **Module:** 11 · Evaluation, Safety & Reliability
- **Topic:** Deployment Readiness
- **Source page:** deployment-readiness.html
- **Page title:** What is Deployment Readiness? · Evaluation & Reliability
- **Page eyebrow:** 07 · Evaluation & Reliability · Topic 04
- **Topic overview source:** evaluation-safety-reliability.html identifies this topic family as Module 11.
- **Extraction scope:** Full visible page body, including the title, lede, on-page navigation, definition, analogy, five-step process, real-world examples, comparison cards, related-concept chain, related-topic links, takeaway, and video metadata.
- **Collection policy:** Raw candidate inventory only. Keep professional terms, mechanisms, workflow nodes, operating conditions, evidence types, controls, metrics, abbreviations, important body words, aliases/synonyms, repeated labels, and potentially confusable concepts for later review. Candidates are intentionally broad, overlapping, and not deduplicated.

## Glossary Candidates

| Candidate | Category | Working definition / why it matters | Page evidence or context |
|---|---|---|---|
| Deployment Readiness | Core concept / title form | The evidence-based state of being ready to operate an AI system in its intended environment. | Page title; definition |
| deployment readiness | Core concept / lowercase form | Readiness for releasing and operating an AI system with evidence and controls. | Lede; takeaway |
| Deployment readiness | Process / decision concept | A release-readiness assessment covering the complete operating system around a model. | Comparison cards |
| deployment-readiness | Hyphenated variant | Hyphenated form used in the page filename and media filenames. | Source filename |
| ready for deployment | Alias / status | A system state in which the evidence supports operating the system in its intended environment. | Topic concept |
| release readiness | Alias / lifecycle concept | Readiness to release an AI system to real users. | Candidate synonym |
| operational readiness | Related concept / alias | Readiness of the system and its operating arrangements for real use. | Candidate synonym |
| production readiness | Related concept / alias | Readiness to run a system in a production environment. | Candidate synonym |
| AI system | System concept | The system being prepared, evaluated, controlled, monitored, and released. | Lede; definition |
| AI | Domain term | Artificial intelligence capability whose deployment is under consideration. | “AI system” |
| artificial intelligence | Domain expansion | Expanded form of AI. | Candidate expansion |
| system | General system term | The complete technical and operational system, not only the model. | Definition; comparison |
| complete operating system | System boundary | The whole collection of model, software, controls, operations, and ownership needed to run the AI system. | “covers the complete operating system” |
| intended environment | Deployment context | The real environment where the AI system is expected to operate. | Definition |
| real users | User context | People who may depend on the system after release. | Lede; analogy |
| real operating conditions | Runtime context | Actual conditions, constraints, traffic, failures, and dependencies encountered in operation. | Lede |
| operating conditions | Runtime context | Conditions that determine whether the system can function reliably after release. | Definition |
| evidence-based state | Readiness evidence | A readiness status supported by observed evidence rather than a demo or assertion. | Definition |
| evidence | Evidence concept | Results and operational proof used to decide whether the system is ready. | Definition; release step |
| readiness evidence | Evidence concept | Evidence showing that the complete system can operate safely and reliably. | Takeaway |
| real-user evidence | Evidence concept | Evidence gathered from or representative of use by actual users. | Lede; release step |
| live evidence | Evidence concept | Evidence from the system while it is operating after or during a controlled release. | Release step |
| model quality | Quality dimension | The quality of the model, treated as one part of deployment-readiness evidence. | Definition; comparison |
| quality | Evaluation dimension | How good the model or system behavior is along relevant dimensions. | Model-quality comparison |
| model | System component | The learned component whose quality is considered within the broader deployment system. | Model quality |
| functional tests | Test evidence | Tests that check whether required system behavior works. | Definition; page link |
| Functional Tests | Related topic / title form | A related topic concerning tests of required behavior. | Related-topic chip |
| functional test | Alias / singular form | One planned test of a required task or system behavior. | Candidate singular |
| safety controls | Safety mechanism | Controls that reduce or constrain unsafe system behavior. | Definition |
| safety | Risk dimension | Protection against harmful, unsafe, or unacceptable behavior. | Safety controls |
| controls | Control mechanism | Technical or operational mechanisms that constrain, govern, or stop system behavior. | Definition; release step |
| monitoring | Operations mechanism | Ongoing observation of system behavior and operating signals. | Definition; process |
| failure handling | Resilience mechanism | Procedures and system behaviors for responding to failures. | Definition; related link |
| Failure Handling | Related topic / title form | A related topic concerning responses to failed cases. | Related-topic chip |
| failure handling plan | Readiness artifact | A prepared approach for identifying and responding to failures. | Candidate expansion |
| failure response | Operations mechanism | The action taken when the system or a dependency fails. | Candidate synonym |
| failure | Failure concept | An event or condition in which the system does not operate as required. | Failure handling; analogy |
| failure modes | Failure concept | Recurring patterns or categories of ways the AI system can fail. | Candidate expansion |
| Failure Modes | Related topic / title form | A related topic concerning failure patterns. | Related-topic chip |
| access | Operations requirement | The ability of authorized users or services to reach and use the system. | Definition; process |
| cost | Operating metric / constraint | Expense of running the AI system at the intended scale and conditions. | Definition; process |
| latency | Operating metric | Time taken for the system to respond or complete an operation. | Definition; process |
| ownership | Operating responsibility | Clearly assigned responsibility for the system and its operation. | Definition; process |
| owner | Responsible actor | Person or team accountable for system operation and response. | Prepare step |
| owners | Responsibility assignment | The people or teams responsible for the system and failure response. | Process step 4 |
| rollback plans | Change-safety mechanism | Plans for reversing a release or returning to a previous working state. | Definition |
| rollback plan | Alias / singular form | A prepared procedure to undo or withdraw a deployment. | Candidate singular |
| rollback | Recovery operation | Reversing a deployment or change when evidence or conditions are unacceptable. | Candidate process term |
| plan | Readiness artifact | A documented approach for failure response, ownership, fallback, or rollback. | Definition; process |
| controls | Release mechanism | Guardrails and operational checks applied during deployment. | “start with controls” |
| release controls | Release mechanism | Controls used to constrain or supervise a release. | Candidate expansion |
| operating target | Acceptance dimension | A target for how the system should operate, including access, cost, or latency. | Define step |
| quality target | Acceptance dimension | A target for acceptable model or system quality. | Define step |
| safety target | Acceptance dimension | A target for acceptable safety performance or risk handling. | Define step |
| target | Requirement concept | A desired value or condition against which readiness is assessed. | Quality, safety, operating targets |
| quality, safety, and operating targets | Requirement set | The three target families agreed before validation. | Process step 1 |
| release criteria | Acceptance criteria | Conditions that must be met before the system is released. | Process step 1 |
| release criterion | Acceptance criterion / singular | One condition used to decide whether a release can proceed. | Candidate singular |
| criteria | Acceptance concept | Plural conditions used to judge release readiness. | “Set release criteria” |
| acceptance criteria | Alias / formal term | Explicit conditions defining acceptable release behavior and operation. | Candidate synonym |
| release gate | Release control | A decision checkpoint that prevents or permits release based on criteria. | Potential missing concept |
| deployment gate | Alias / release control | A checkpoint applied before deployment. | Potential missing concept |
| readiness gate | Alias / release control | A checkpoint requiring readiness evidence before release. | Candidate synonym |
| define | Process step | First stage: set the release criteria. | Step 1 label |
| Define | Process label | Capitalized first process-stage label. | “1 · Define” |
| set release criteria | Process action | Agree on the conditions the system must satisfy before release. | Step 1 |
| set | Process action | Establish or agree on criteria and targets. | “Set release criteria” |
| release | Lifecycle event | Make the system available for real use. | Step 5; comparison |
| validate | Process step | Second stage: run evaluations against relevant cases. | Step 2 label |
| Validate | Process label | Capitalized second process-stage label. | “2 · Validate” |
| run evaluations | Process action | Execute evaluations for common, difficult, and risky cases. | Step 2 |
| evaluation | Evidence process | A process of measuring or judging system performance and risk. | Related concept chain |
| Evaluation | Related topic / title form | A related topic concerning measurement and judgment of system performance. | Related-topic chip |
| evaluations | Plural process form | Multiple evidence-generating checks across relevant cases. | Step 2 |
| common cases | Validation scope | Ordinary or expected situations the system will encounter. | Step 2 |
| difficult cases | Validation scope | Challenging situations that place greater demands on the system. | Step 2 |
| risky cases | Validation scope | Situations with higher potential harm, failure cost, or operational risk. | Step 2 |
| case | Validation unit | A specific situation used to test or evaluate system behavior. | “common, difficult, and risky cases” |
| common | Case category | Ordinary case category in validation. | Step 2 |
| difficult | Case category | Challenging case category in validation. | Step 2 |
| risky | Case category | High-risk case category in validation. | Step 2 |
| operate | Process step | Third stage: check whether the system can be operated under intended conditions. | Step 3 label |
| Operate | Process label | Capitalized third process-stage label. | “3 · Operate” |
| check the system | Process action | Confirm monitoring, access, cost, and latency. | Step 3 |
| monitoring check | Readiness check | Confirmation that ongoing system observation is in place. | Step 3 |
| access check | Readiness check | Confirmation that intended access is available and controlled. | Step 3 |
| cost check | Readiness check | Confirmation that operating cost is understood and acceptable. | Step 3 |
| latency check | Readiness check | Confirmation that response time is acceptable for the intended use. | Step 3 |
| prepare | Process step | Fourth stage: plan the response to failure. | Step 4 label |
| Prepare | Process label | Capitalized fourth process-stage label. | “4 · Prepare” |
| plan failure response | Process action | Define the operational response when something goes wrong. | Step 4 |
| failure response plan | Readiness artifact | Documented response procedure for failures. | Step 4 |
| fallback | Resilience mechanism | Alternative behavior, system, route, or service used when the primary path fails. | Step 4 |
| fallbacks | Resilience mechanism / plural | Alternative paths prepared for failure conditions. | Step 4 |
| fallback plan | Resilience artifact | Plan for switching to an alternative path or degraded behavior. | Candidate expansion |
| rollback steps | Recovery procedure | Concrete steps for reversing the deployment. | Step 4 |
| response plan | Operations artifact | Plan specifying what happens after a failure. | Candidate synonym |
| release | Process step | Fifth stage: deploy gradually and review live evidence. | Step 5 label |
| Release | Process label | Capitalized fifth process-stage label. | “5 · Release” |
| start with controls | Process action | Begin deployment under explicit controls. | Step 5 |
| deploy gradually | Release strategy | Increase exposure in stages rather than releasing to everyone at once. | Step 5 |
| gradual deployment | Release strategy | Controlled, staged rollout of the AI system. | Candidate noun form |
| staged deployment | Release strategy / alias | Deployment performed through successive exposure stages. | Candidate synonym |
| gradual release | Release strategy / alias | Release with increasing scope or exposure. | Candidate synonym |
| controlled release | Release strategy | Release conducted with constraints, monitoring, and review. | Example; step 5 |
| pilot | Release stage | A limited controlled release used to gather evidence before broader deployment. | Related concept chain; example |
| controlled pilot release | Release outcome | A limited release of the support assistant with controls and monitoring. | Business example output |
| pilot release | Release stage / alias | Initial limited deployment for evidence gathering. | Candidate synonym |
| production process | Operating outcome | A measurable process in which the deployed AI system handles real work. | Document extraction output |
| measurable production process | Operating outcome | A production process whose behavior and results can be measured. | AI product example |
| live evidence review | Operations process | Review of evidence gathered during actual or controlled live operation. | Step 5 |
| review live evidence | Process action | Inspect operating evidence after or during a gradual release. | Step 5 |
| intended use | Deployment scope | The use case and context for which the AI system is being prepared. | Intended environment |
| real use | Deployment context | Use by actual users or production workflows. | Lede; examples |
| operate safely | Safety outcome | Run without unacceptable unsafe behavior under intended conditions. | Takeaway |
| operate reliably | Reliability outcome | Run dependably enough for users and workflows to rely on it. | Takeaway |
| safely | Safety qualifier | In a manner that manages relevant safety risks. | Takeaway |
| reliably | Reliability qualifier | In a dependable, repeatable, operationally acceptable manner. | Takeaway |
| whole AI system | System boundary | The model plus the surrounding controls, operations, dependencies, and responsibilities. | Takeaway |
| operating system | Operational system | The complete system that must function, including more than model quality. | Definition |
| shop | Analogy | A new shop represents a system being prepared before customers depend on it. | Analogy lead |
| opening a new shop | Analogy / lifecycle | Analogy for preparing an AI system before opening it to real users. | “Think of it like opening a new shop.” |
| equipment | Analogy requirement | Shop resource corresponding to working technical components. | Analogy |
| working equipment | Analogy requirement | Equipment that functions before the shop opens. | Analogy |
| staff | Analogy actor | Shop personnel corresponding to owners/operators of the AI system. | Analogy |
| trained staff | Analogy requirement | Prepared personnel who know how to operate the shop. | Analogy |
| safety procedures | Analogy control | Shop procedures corresponding to safety controls. | Analogy |
| supplies | Analogy resource | Shop resources corresponding to operating dependencies and provisions. | Analogy |
| plan for problems | Analogy resilience | Preparation for failures or issues before users depend on the system. | Analogy |
| customer | Analogy actor | Shop customer corresponding to a real user of the AI system. | Analogy |
| users depend on a system | Reliance concept | Users rely on the system, increasing the need for readiness evidence. | Analogy |
| working equipment, trained staff, safety procedures, supplies, and a plan for problems | Analogy checklist | The shop-readiness checklist mapped to AI deployment readiness. | Analogy paragraph |
| business example | Example category | Example showing a support assistant in an organizational setting. | Example heading |
| Business example · Support assistant | Example label | Label for the support-assistant scenario. | Examples section |
| support assistant | AI application | AI system that supports a user workflow. | Business example |
| Support assistant | Title-case variant | Capitalized form of the support-assistant example. | Example heading |
| support workflow | Workflow | Tested workflow in which the support assistant operates. | Business example input |
| tested support workflow | Evidence input | Support workflow used as the input to the readiness example. | Business example |
| policy grounding | Safety/reliability control | Grounding the assistant in relevant policy so its responses follow approved rules. | Business example system |
| grounding | Control mechanism | Connecting outputs to an approved source, policy, or knowledge base. | Policy grounding |
| escalation | Failure/safety process | Routing a case to a person or higher-level process when the assistant should not proceed alone. | Business example system |
| escalation path | Workflow mechanism | Defined route for handing a case to a human or another responsible process. | Candidate expansion |
| monitoring | Support operation | Observation of support-assistant behavior after release. | Business example system |
| owners | Support responsibility | Responsible people or teams for the support assistant. | Business example system |
| policy | Domain constraint | Rules or approved guidance that ground the support assistant. | Policy grounding |
| controlled pilot | Release stage | Limited deployment with explicit controls before wider use. | Business example output |
| AI product example | Example category | Example showing document extraction in an AI product. | Example heading |
| AI product · Document extraction | Example label | Label for the document-extraction scenario. | Examples section |
| document extraction | AI capability | Extracting known fields or information from documents. | AI product example |
| Document extraction | Title-case variant | Capitalized form of the document-extraction example. | Example heading |
| document | Input artifact | Source artifact supplied to the extraction system. | AI product example |
| documents | Input artifact / plural | Documents containing fields for the system to extract. | Input line |
| known fields | Extraction target | Fields whose expected presence or meaning is known in advance. | AI product input |
| field | Structured data unit | A discrete piece of information extracted from a document. | Known fields |
| validates outputs | Output control | Checks that extracted results satisfy required conditions. | AI product system |
| validate outputs | Process action | Verify the fields or result returned by the extraction system. | Candidate verb form |
| output validation | Quality/control mechanism | Validation applied to results produced by the system. | Candidate noun form |
| routes exceptions to review | Exception process | Sends unusual or failed cases to a review workflow. | AI product system |
| exception | Exception concept | A case that cannot safely proceed through the normal automated path. | AI product example |
| exception routing | Workflow mechanism | Directing exceptions to a review queue or responsible person. | Candidate noun form |
| review | Human/operational process | Examination of exceptions or evidence before deciding what to do. | “routes exceptions to review” |
| human review | Review mechanism | Review by a person when automated extraction is insufficient. | Candidate expansion |
| production | Deployment context | Live environment in which the measurable extraction process operates. | Output |
| input | Workflow node | A tested workflow or document with known fields supplied to the system. | Both examples |
| Input | Example label | Capitalized label for example inputs. | Example cards |
| system | Workflow node | The AI system and its controls that process the input. | Both examples |
| System | Example label | Capitalized label for example systems. | Example cards |
| output | Workflow node | The resulting controlled pilot or measurable production process. | Both examples |
| Output | Example label | Capitalized label for example outputs. | Example cards |
| input → system → output | Simplified system relationship | Framing of how an input is processed into an operational output. | Examples |
| input / system / output | System model | Three-part example structure shown by the page. | Examples |
| output validation and exception review | Control pattern | Combined mechanism for checking outputs and routing uncertain cases. | Document extraction example |
| What it is NOT | Comparison section | Section distinguishing deployment readiness from narrower or unrealistic conditions. | On-page navigation; heading |
| Deployment Readiness ≠ Model Quality | Distinction | Readiness covers the complete operating system; model quality is only one part. | Comparison card |
| Deployment Readiness ≠ A Demo | Distinction | Readiness requires repeatable evidence and controls; a demo shows a limited successful path. | Comparison card |
| Deployment Readiness ≠ No Risk | Distinction | Readiness makes risks known and manageable; it does not mean risk disappears. | Comparison card |
| demo | Confusable concept | A limited successful demonstration that does not establish full deployment readiness. | Comparison |
| A Demo | Comparison concept / title form | Demonstration of a limited path. | Comparison heading |
| limited successful path | Demo property | Narrow scenario that can work without proving complete operational readiness. | Demo comparison |
| repeatable evidence | Readiness evidence | Evidence that can be reproduced or checked consistently. | Demo comparison |
| known risks | Risk concept | Risks identified well enough to be managed. | No-risk comparison |
| manageable risks | Risk outcome | Risks that are understood and can be controlled or responded to. | No-risk comparison |
| risk | Risk concept | Possibility of harmful, failed, or unacceptable system behavior. | No-risk comparison |
| no risk | Unrealistic condition | The absence of all risk, explicitly rejected as a realistic release condition. | Comparison card |
| realistic release condition | Release criterion | A release condition that acknowledges and manages risk rather than requiring its absence. | No-risk comparison |
| release condition | Acceptance concept | A state or requirement used to determine whether release is appropriate. | Comparison |
| known and manageable | Risk qualifier | The target relationship between identified risks and operational controls. | Comparison |
| related concepts | Navigation section | Section linking readiness to evaluation, controls, monitoring, pilot, deployment, and continuous review. | Related section |
| Evaluation → Controls → Monitoring → Pilot → Deployment → Continuous Review | Concept chain | Lifecycle relationship presented on the page. | Concept tree |
| Controls → Monitoring | Concept relationship | Controls are followed by operational monitoring in the displayed chain. | Concept tree |
| Monitoring → Pilot | Concept relationship | Monitoring supports or accompanies a pilot release. | Concept tree |
| Pilot → Deployment | Concept relationship | A pilot precedes broader deployment in the displayed progression. | Concept tree |
| Deployment → Continuous Review | Concept relationship | Deployment is followed by continuing review. | Concept tree |
| continuous review | Operations process | Ongoing review of evidence and system operation after deployment. | Related concept chain |
| Continuous Review | Title-case variant | Capitalized chain label for ongoing post-deployment review. | Concept tree |
| deployment | Lifecycle event / related concept | Making the AI system available in its intended environment. | Concept tree |
| Deployment | Title-case variant | Capitalized chain label for the release event. | Concept tree |
| controls | Related chain node | Mechanisms used to constrain and manage operation. | Concept tree |
| monitoring | Related chain node | Ongoing observation of the released system. | Concept tree |
| pilot | Related chain node | Limited release used before wider deployment. | Concept tree |
| evaluation | Related chain node | Evidence-generating measurement or judgment before release. | Concept tree |
| Enterprise AI Deployment | Related topic / title form | Related topic about deploying AI in enterprise settings. | Related-topic chip |
| enterprise AI deployment | Related concept / lowercase form | Enterprise-focused deployment of AI systems. | Related-topic chip |
| related topic | Navigation concept | A linked topic page with adjacent concepts. | Explore next |
| Explore next | Navigation label | Label introducing linked topic chips. | Related section |
| Remember this | Takeaway label | Section label introducing the central summary. | Takeaway heading |
| takeaway | Summary concept | Short statement of the page's main idea. | Takeaway section |
| evidence that the whole AI system can operate safely and reliably | Summary statement | The page's concise characterization of deployment readiness. | Takeaway |
| safe operation | Outcome | Operation without unacceptable safety failures. | Takeaway |
| reliable operation | Outcome | Dependable operation under intended conditions. | Takeaway |
| Independent explainer | Media label | Label for the standalone explainer video. | Video section |
| visual explainer | Media type | Video intended to explain the topic visually. | Video metadata |
| video | Media artifact | Explainer media associated with the topic. | Video section |
| video playback | Media behavior | Browser behavior of playing the explainer video. | Video fallback text |
| English captions | Accessibility asset | English caption track provided for the video. | Video track metadata |
| captions | Accessibility asset | Synchronized text for the video. | Video track |
| poster | Media asset | Preview image displayed before playback. | Video element |
| source | Media asset | Video file resource used by the page. | Video element |
| deployment-readiness.mp4 | Media filename | MP4 explainer resource referenced by the page. | Video source |
| deployment-readiness.vtt | Media filename | WebVTT caption resource referenced by the page. | Video track |
| deployment-readiness.png | Media filename | Poster image resource referenced by the page. | Video poster |
| MP4 | Media format / abbreviation | Video file format used by the source resource. | `.mp4` source |
| VTT | Media format / abbreviation | Caption file format used by the track resource. | `.vtt` track |
| WebVTT | Caption format | Web video text track format implied by the caption resource. | Candidate expansion |
| playback fallback | Media behavior | Message shown when the browser cannot play video. | Video fallback |
| browser | Software actor | Client that loads the page and may support or fail to support playback. | Video fallback text |
| browser support | Capability concept | Whether the browser supports the video playback requirement. | Candidate expansion |

## Potential Missing Concepts

These concepts are useful for a fuller glossary of deployment readiness but are not fully defined in the source page. They are retained as follow-up candidates rather than being presented as page-defined concepts:

- production deployment, deployment pipeline, release lifecycle, release management, change management, go-live, go-live checklist
- pre-deployment review, readiness review, launch review, operational acceptance, production acceptance, sign-off
- acceptance criterion, acceptance threshold, release gate, deployment gate, quality gate, safety gate, risk threshold
- model evaluation, system evaluation, offline evaluation, online evaluation, benchmark, test suite, test dataset, test coverage
- happy path, difficult case, edge case, boundary case, corner case, negative case, adversarial case, abuse case
- safety evaluation, red teaming, misuse testing, policy test, guardrail test, refusal test, escalation test
- risk assessment, risk register, hazard analysis, threat model, impact assessment, residual risk, risk owner
- guardrail, policy enforcement, content filter, moderation, access control, authentication, authorization, least privilege
- human-in-the-loop, human oversight, human review, manual fallback, escalation queue, approval workflow
- observability, logs, metrics, traces, dashboard, alerting, alert threshold, incident detection, incident response
- service-level objective, SLO, service-level agreement, SLA, service-level indicator, SLI, error budget
- availability, uptime, reliability, error rate, failure rate, success rate, throughput, requests per second, RPS
- p50 latency, p95 latency, p99 latency, tail latency, time to first token, TTFT, response time
- cost per request, inference cost, token cost, budget, cost forecast, capacity planning, utilization
- load test, stress test, soak test, capacity test, performance test, resilience test, chaos test
- staging environment, test environment, production environment, sandbox, canary environment, shadow mode
- canary release, blue-green deployment, rolling deployment, feature flag, dark launch, traffic splitting, progressive delivery
- rollback trigger, rollback automation, rollback verification, version pinning, model version, prompt version
- fallback model, backup provider, degraded mode, graceful degradation, circuit breaker, timeout, retry, retry policy
- dependency, external service, API dependency, rate limit, quota, authentication failure, network failure, outage
- data quality, data drift, concept drift, distribution shift, schema drift, input validation, data validation
- privacy review, security review, compliance review, audit trail, data retention, sensitive data, PII, personally identifiable information
- ownership model, on-call owner, escalation owner, runbook, playbook, operating procedure, support process
- monitoring plan, alert policy, incident severity, incident ticket, postmortem, root-cause analysis, corrective action
- continuous improvement, post-deployment review, feedback loop, user feedback, production feedback, review cadence
- repeatability, reproducibility, deterministic behavior, nondeterministic behavior, sampling variance, confidence interval
- documentation, architecture decision record, deployment record, release notes, model card, system card, operating manual
- model quality, functional correctness, safety, reliability, latency, cost, access, ownership, rollback as readiness dimensions

## Aliases / Synonyms

Keep these as separate raw candidates until the later glossary pass decides whether to merge them:

| Candidate | Possible alias/synonym relationship |
|---|---|
| Deployment Readiness | deployment readiness; release readiness; operational readiness; production readiness |
| deployment readiness | ready for deployment; release readiness; production readiness |
| AI system | AI; artificial intelligence system; system under deployment; whole AI system |
| intended environment | target environment; operating environment; production environment; deployment context |
| real users | actual users; end users; people who depend on the system |
| real operating conditions | live operating conditions; production conditions; runtime conditions |
| evidence-based state | evidence-backed status; readiness evidence; supported readiness decision |
| model quality | model performance; model quality score; model capability quality |
| functional tests | Functional Tests; functional test; functional testing |
| safety controls | safety guardrails; safety mechanisms; control mechanisms |
| controls | release controls; operating controls; guardrails |
| monitoring | system monitoring; operational monitoring; live monitoring; post-deployment monitoring |
| failure handling | Failure Handling; failure response; error handling; failure management |
| access | system access; service access; authorized access |
| cost | operating cost; run cost; inference cost; cost of operation |
| latency | response latency; response time; end-to-end latency |
| ownership | accountability; responsible ownership; operational responsibility |
| owner | system owner; operational owner; accountable team |
| rollback plans | rollback plan; rollback procedure; rollback steps; recovery plan |
| release criteria | release criterion; acceptance criteria; go-live criteria |
| quality target | quality goal; quality threshold; acceptable quality target |
| safety target | safety goal; safety threshold; acceptable safety target |
| operating target | operational target; runtime target; service target |
| Define | define; set release criteria; specify release requirements |
| Validate | validate; run evaluations; evaluate the system |
| Operate | operate; check the system; verify operability |
| Prepare | prepare; plan failure response; prepare for failure |
| Release | release; deploy; make available; go live |
| common cases | normal cases; typical cases; ordinary cases |
| difficult cases | challenging cases; hard cases; stress cases |
| risky cases | high-risk cases; hazardous cases; sensitive cases |
| fallback | fallback path; backup path; alternate path; degraded mode |
| gradual deployment | staged deployment; progressive delivery; phased rollout |
| controlled pilot release | controlled pilot; pilot release; limited rollout |
| review live evidence | inspect production evidence; review runtime evidence; monitor live evidence |
| shop | new shop analogy; opening-a-shop analogy |
| equipment | working equipment; technical components; operational resources |
| trained staff | prepared operators; trained operators; responsible team |
| safety procedures | safety controls; operating procedures; safety practices |
| plan for problems | failure plan; incident plan; contingency plan |
| support assistant | support AI; customer-support assistant; AI support agent |
| support workflow | customer-support workflow; service workflow; support process |
| policy grounding | policy-based grounding; grounded support; policy-constrained responses |
| escalation | human escalation; escalation path; handoff to review |
| controlled pilot | pilot; limited pilot; controlled release |
| document extraction | information extraction; field extraction; document-processing AI |
| known fields | expected fields; predefined fields; target fields |
| validates outputs | output validation; validates results; checks extracted fields |
| routes exceptions to review | exception routing; sends exceptions for review; human-review routing |
| exception | outlier case; nonstandard case; review case; manual-review case |
| production process | live process; production workflow; operational process |
| Deployment | deployment; release; rollout; go-live |
| Continuous Review | continuous review; ongoing review; post-deployment review |
| demo | demonstration; proof of concept; limited successful path |
| no risk | zero risk; risk-free operation; absence of risk |
| known and manageable risks | identified risks; controlled risks; acceptable residual risk |
| English captions | English subtitles; caption track; WebVTT captions |
| poster | poster image; preview image; video thumbnail |
| source | video source; media source; MP4 resource |

## Do Not Confuse Candidates

| Candidate A | Candidate B | Distinction suggested by the page |
|---|---|---|
| Deployment Readiness | Model Quality | Deployment readiness covers the complete operating system; model quality is one part of the evidence. |
| Deployment Readiness | Demo | Readiness requires repeatable evidence and controls; a demo shows only a limited successful path. |
| Deployment Readiness | No Risk | Readiness makes risks known and manageable; it is not the unrealistic condition of having no risk. |
| Deployment readiness | Release readiness | These may overlap, but deployment readiness emphasizes the full operating environment, controls, and evidence. |
| Deployment readiness | Production readiness | Production readiness can be used as a synonym, but the page frames readiness around the intended environment, which may be broader than production. |
| AI system | Model | The AI system includes the model plus controls, monitoring, access, operations, owners, and response plans. |
| Complete operating system | Model quality | The complete operating system is the broad deployment boundary; model quality is a narrower quality dimension. |
| Intended environment | Real operating conditions | Intended environment names where the system should operate; real operating conditions describe what it encounters there. |
| Evidence | Opinion | Evidence is observed support for readiness; an opinion or assertion alone is not evidence-based readiness. |
| Release criteria | Target | Release criteria are decision conditions; targets are desired quality, safety, or operating values that may feed those conditions. |
| Quality target | Model quality | A quality target is a threshold or goal; model quality is the observed quality dimension. |
| Safety controls | Safety target | Controls are mechanisms; a safety target is the condition those mechanisms help the system meet. |
| Operating target | Operating condition | A target is desired performance; an operating condition is the actual context in which performance is observed. |
| Functional tests | Evaluations | Functional tests are one type of evidence; evaluations are the broader activity used for common, difficult, and risky cases. |
| Evaluate | Validate | Evaluation generates or examines evidence; validation is the readiness stage of confirming the system against requirements. |
| Common case | Difficult case | A common case represents ordinary use; a difficult case stresses the system with a more challenging situation. |
| Difficult case | Risky case | Difficulty concerns challenge; risk concerns potential harm or unacceptable consequence. |
| Risky case | Failure | A risky case is an input situation; a failure is an undesirable outcome or event. |
| Monitoring | Evaluation | Monitoring observes operation over time; evaluation is a planned measurement or judgment activity. |
| Monitoring | Continuous Review | Monitoring is an observation mechanism; continuous review is the ongoing process of interpreting evidence and deciding what to do. |
| Access | Authorization | Access is the ability to reach or use the system; authorization is the decision about who or what is permitted. |
| Cost | Latency | Cost is an operating-resource metric; latency is a time-to-response metric. |
| Ownership | Access | Ownership assigns responsibility; access controls who can use or reach the system. |
| Failure handling | Failure mode | Failure handling is the response process; a failure mode is a recurring pattern or category of failure. |
| Failure response | Rollback | Failure response is the broader reaction; rollback is one specific recovery operation that reverses a release or change. |
| Fallback | Rollback | A fallback switches to an alternative behavior or path; rollback returns to a previous release or state. |
| Rollback plan | Fallback plan | A rollback plan reverses the deployment; a fallback plan uses an alternative path or degraded behavior. |
| Owner | Operator | An owner is accountable for the system; an operator may perform day-to-day operational actions. |
| Deploy gradually | Controlled pilot | Gradual deployment is a rollout strategy; a controlled pilot is a limited release stage or outcome. |
| Pilot | Deployment | A pilot is limited exposure used to gather evidence; deployment may mean broader availability in the intended environment. |
| Controlled pilot release | Production process | A controlled pilot is an initial release; a measurable production process is an operating result after the system is running in production. |
| Live evidence | Evaluation result | Live evidence comes from operation; an evaluation result may come from planned validation before release. |
| Support assistant | Document extraction | The support assistant example centers on a support workflow; document extraction centers on extracting known fields from documents. |
| Support workflow | Document | A support workflow is a process; a document is an input artifact in the extraction example. |
| Policy grounding | Escalation | Grounding constrains or informs responses; escalation routes a case to another person or process. |
| Escalation | Fallback | Escalation transfers responsibility for review; a fallback is an alternative system behavior or route. |
| Known fields | Validated outputs | Known fields are expected input targets; validated outputs are the checked results. |
| Output validation | Exception routing | Validation checks the result; exception routing sends cases that need additional handling to review. |
| Exception | Failure | An exception is a case requiring a different path; it may or may not be caused by a system failure. |
| Human review | Continuous review | Human review examines a specific case; continuous review is an ongoing readiness or operational review process. |
| Demo | Pilot | A demo illustrates a limited successful path; a pilot is a controlled real-use release that gathers live evidence. |
| No risk | Manageable risk | No risk requires complete absence of risk; manageable risk is identified and controlled enough for the intended release. |
| Known risk | Manageable risk | Knowing a risk does not itself make it manageable; controls, owners, and response plans are also relevant. |
| Safe operation | Reliable operation | Safety concerns unacceptable harm or unsafe behavior; reliability concerns dependable operation over cases and time. |
| Reliable operation | Availability | Reliability is broad dependable behavior; availability is one specific measure of whether the service is usable. |
| Release | Rollback | Release makes a system available; rollback reverses a release when conditions require it. |
| Deployment | Continuous Review | Deployment is a lifecycle event or state; continuous review is the ongoing post-deployment evidence process. |
| Monitoring | Observability | Monitoring is the act of watching signals; observability is the broader ability to understand internal state from outputs and telemetry. |
| Video | Video captions | The video is the media artifact; captions are synchronized text associated with it. |
| Video poster | Video source | The poster is a preview image; the source is the playable media file. |
| MP4 | VTT | MP4 is the video resource format; VTT is the caption-track format. |

## Notes

- The source page defines deployment readiness as **the evidence-based state of being ready to operate an AI system in its intended environment**.
- The lede explicitly frames the topic around **real users** and **real operating conditions**.
- The page lists the readiness dimensions: model quality, functional tests, safety controls, monitoring, failure handling, access, cost, latency, ownership, and rollback plans.
- The page's analogy is opening a new shop. Working equipment, trained staff, safety procedures, supplies, and a plan for problems are retained as raw analogy candidates because they map to deployment prerequisites.
- The visible five-step process is: **Define → Validate → Operate → Prepare → Release**.
- The process expands to: **set release criteria → run evaluations → check the system → plan failure response → start with controls → deploy gradually → review live evidence**.
- Step 1 says to agree on **quality, safety, and operating targets**. The source does not provide numerical thresholds or a specific acceptance framework.
- Step 2 says to test **common, difficult, and risky cases**. It does not define a test-set size, benchmark, statistical method, or pass-rate requirement.
- Step 3 explicitly checks **monitoring, access, cost, and latency**. These are retained as separate operating metrics/requirements even though the page gives no units, thresholds, or measurement windows.
- Step 4 explicitly names **owners, fallbacks, and rollback steps**. The page does not state whether owners are individuals, teams, or an on-call rotation.
- Step 5 says to **deploy gradually** and review **live evidence**. Gradual deployment is retained as both a process action and a release strategy candidate.
- The business example is a support assistant with a tested support workflow, policy grounding, escalation, monitoring, and owners, resulting in a controlled pilot release.
- The AI product example is document extraction from documents with known fields; the system validates outputs and routes exceptions to review, resulting in a measurable production process.
- The explicit comparison set is: **Deployment Readiness ≠ Model Quality**, **Deployment Readiness ≠ A Demo**, and **Deployment Readiness ≠ No Risk**.
- The page says readiness requires **repeatable evidence and controls**, and that risks should be **known and manageable**. It does not claim that a ready system is risk-free.
- The related-concept chain is: **Evaluation → Controls → Monitoring → Pilot → Deployment → Continuous Review**.
- The related-topic links are retained as candidates even though their linked pages contain fuller definitions: Evaluation, Functional Tests, Failure Modes, Failure Handling, and Enterprise AI Deployment.
- The page does not define a deployment platform, model-serving architecture, infrastructure topology, compliance standard, security control, service-level target, statistical confidence requirement, or release approval authority.
- The page does not specify particular abbreviations for metrics or processes. Common follow-up abbreviations such as SLO, SLA, SLI, CI/CD, PII, RPS, and TTFT are retained only under Potential Missing Concepts.
- The page does not give numerical metrics, but **cost** and **latency** are explicit operating dimensions; possible aggregate metrics and units are retained as follow-up candidates.
- The video section contributes the visible media concepts and filenames: deployment-readiness.mp4, deployment-readiness.vtt, and deployment-readiness.png; these filenames are raw candidates, not glossary definitions.
- The source page contains a taxonomy mismatch worth preserving in metadata: the topic page eyebrow says **07 · Evaluation & Reliability · Topic 04**, while the parent overview identifies the topic family as **11 · Evaluation, Safety & Reliability**. The requested output uses the Module 11 convention.
- Repeated labels, uppercase/lowercase forms, singular/plural forms, hyphenated variants, related concepts, analogy words, workflow nodes, possible aliases, and broader follow-up concepts are intentionally retained for later deduplication and editorial review.
