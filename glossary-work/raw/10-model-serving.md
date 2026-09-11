# Topic 10 · Model Serving

## Topic Metadata

- **Module:** 10 · Model Serving & Local AI
- **Topic:** Model Serving
- **Source page:** `model-serving.html`
- **Page title:** What Is Model Serving? · Model Serving & Local AI
- **Extraction scope:** Full visible page body, including headings, explanatory paragraphs, stack labels, request-flow labels, comparison cards, related-concept tags, linked concept names, and the video placeholder. Candidates are intentionally broad, overlapping, and not deduplicated.
- **Collection policy:** Raw candidate inventory only. Keep technical terms, mechanisms, workflow nodes, metrics, abbreviations, important body words, aliases/synonyms, and potentially confusable concepts for later review.

## Glossary Candidates

| Candidate | Category | Working definition / why it matters | Page evidence or context |
|---|---|---|---|
| Model Serving | Core concept | The system that makes a trained model available to applications as a usable inference service. | Hero definition; takeaway |
| serving | Alias / shorthand | Short form for model serving or the serving layer. | “Runtime vs Serving”; “Without serving” |
| serving system | System concept | The operational system that receives orders/requests and delivers model results. | Restaurant analogy; request flow |
| model-serving system | Alias / system concept | A system that exposes model inference to applications. | Implied by the page’s serving stack |
| inference service | Service concept | A callable service that performs inference and returns results. | Hero and takeaway definitions |
| usable inference service | Service concept | Inference made accessible in a form applications can use. | “Makes inference available as a usable service” |
| trained model | Model state | A model whose learned behavior has already been produced through training. | Hero; takeaway |
| model | Core concept | Learned behavior represented by learned weights and used to produce outputs. | Model vs Model Server; stack |
| model file | Artifact | A file containing a model’s learned behavior/weights, but not the surrounding serving machinery. | “Why is a model file not enough?” |
| learned behavior | Model concept | Behavior encoded by a trained model. | Model file definition; model stack row |
| learned weights | Model representation | Parameters/weights that encode what the model learned. | Model vs Model Server |
| weights | Alias / model representation | Numeric learned values used by a model during inference. | Hero: “model weights”; model definition |
| model weights | Model representation | The learned numeric state executed by hardware through a runtime. | Hero second paragraph |
| application | Consumer layer | A program or product that asks for AI capability and consumes model results. | Serving stack; related concepts |
| applications | Alias / consumer layer | Multiple software clients that send requests to and receive responses from a serving system. | Hero; production workload |
| app | Alias / workflow node | Abbreviation for application in the request diagram. | “APP” at beginning and end of request flow |
| AI capability | Capability | The capability an application asks the serving stack to provide. | Application stack row |
| API | Interface layer | An interface that receives requests from an application and returns responses. | Stack; analogy; related concepts |
| application programming interface | Expansion of API | A software interface through which an application calls a service. | Candidate expansion for API |
| API interface | Alias / interface concept | The ordering/request interface between application and serving system. | Restaurant analogy |
| ordering interface | Analogy | Restaurant-analogy name for the API. | API analogy card |
| API request | Workflow node | A request sent through the API into the serving system. | One-request flow |
| request | Workflow input | An application’s input asking the serving stack to perform work. | “receive requests”; request flow |
| requests | Workload unit | Individual calls that the serving system receives and manages. | Hero; production serving |
| receive requests | Operation | Accepting incoming inference calls from applications. | Hero; model-file explanation |
| return results | Operation | Sending computed outputs back to the application. | Hero; model-file explanation |
| API response | Workflow output | The response returned through the API after inference. | One-request flow |
| response | Workflow output | Result delivered back to the calling application. | “requests → model → responses” |
| result | Output concept | Output produced by inference and returned to an application. | Hero; model-file explanation |
| model server | Serving component | Software/system exposing a model to applications and managing access to it. | Serving stack; Model vs Model Server |
| MODEL SERVER | Label variant | Uppercase stack label for the model-server layer. | Serving stack |
| server | Shorthand / component | A software system that exposes or manages access to a model. | Model Server distinction |
| software | Implementation concept | The executable layer that can expose a model as a service. | Model Server definition |
| system | Architecture concept | The combined serving infrastructure around a model. | Model Server definition; serving system |
| exposing a model | Operation | Making a model callable by applications. | Model Server definition |
| manage access | Serving responsibility | Controlling how applications reach and use the model. | Model Server stack row; serving comparison |
| access | Serving responsibility | Availability of the model to callers/applications. | Serving comparison |
| runtime | Execution layer | The layer that executes model inference. | Serving stack; Runtime vs Serving |
| RUNTIME | Label variant | Uppercase stack label for the runtime layer. | Serving stack |
| model runtime | Alias / execution layer | Software runtime that loads and executes a model. | Implied by runtime layer |
| execute model | Operation | Running the model computation on available hardware. | Runtime stack row |
| executes inference | Operation | Runtime responsibility of performing inference computation. | Runtime vs Serving |
| inference | Core operation | Running a trained model on an input to produce an output. | Hero; runtime comparison; request flow |
| model inference | Workflow node | The inference step in the request path. | One-request flow |
| inference request | Alias / workflow input | A request asking a model-serving system to run inference. | Candidate synthesis from API request + inference |
| inference execution | Execution concept | The actual computation performed by the runtime. | Runtime definition |
| generated tokens | Output unit | Tokens generated by the model during an inference request. | One-request flow |
| token | Output unit | A unit of generated model output. | “Generated tokens” |
| tokens | Plural / output units | Multiple units generated in the response. | “Generated tokens” |
| generated output | Alias / output concept | Output produced during inference, represented on this page as generated tokens. | Request flow |
| hardware | Infrastructure layer | Compute and memory resources on which model weights run. | Serving stack; related concepts |
| HARDWARE | Label variant | Uppercase stack label for the hardware layer. | Serving stack |
| compute | Resource | Processing capacity used to execute model operations. | Hardware stack row; GPU / Memory tag |
| memory | Resource | Memory capacity used to hold weights and intermediate execution state. | Hardware stack row; GPU / Memory |
| GPU | Hardware resource | A graphics processing unit that can provide compute for model execution. | Related concepts |
| GPU / Memory | Resource pair | The hardware resources called out as supporting the model/runtime. | Related-concepts stack |
| hardware resources | Resource concept | Compute and memory resources used by the serving stack. | Related-concepts stack |
| stack | Architecture view | Ordered layers from application through hardware. | “The serving stack” |
| serving stack | Architecture concept | The layered path Application → API → Model Server → Runtime → Model → Hardware. | Section 01 |
| layer | Architecture concept | A distinct responsibility level in the serving stack. | “Keep the layers distinct” |
| serving layer | Architecture concept | The model-serving portion surrounding runtime/model execution and access management. | Runtime vs Serving |
| model layer | Architecture concept | The learned model/weights layer that provides learned behavior. | Stack; model distinction |
| hardware layer | Architecture concept | Bottom layer supplying compute and memory. | Stack |
| application layer | Architecture concept | Top layer requesting AI capability. | Stack |
| API layer | Architecture concept | Interface layer receiving requests. | Stack |
| runtime layer | Architecture concept | Execution layer inside serving. | “Runtime is one layer inside serving” |
| access management | Serving responsibility | Management of callers’ access to model inference. | Model Server; serving comparison |
| resource management | Serving responsibility | Managing compute/memory and other resources used by requests and models. | Model-file explanation; serving comparison |
| manage resources | Operation | Allocating/controlling resources needed to serve models. | Why model file is not enough |
| request management | Serving responsibility | Managing incoming model requests. | Serving comparison |
| model management | Serving responsibility | Managing one or more models in a serving environment. | Serving comparison |
| queue | Scheduling concept | A waiting structure for requests before execution. | “queues” |
| queues | Alias / scheduling concept | Request waiting structures managed by a serving system. | Serving comparison |
| batching | Optimization / scheduling | Combining multiple requests or inputs into a batch for execution. | Serving comparison |
| batch | Alias / workload unit | A grouped set of requests/inputs processed together. | Candidate expansion for batching |
| request batching | Alias / optimization | Batching multiple incoming requests for efficient execution. | Serving comparison |
| scheduling | Operations concept | Deciding when and where requests/resources are processed. | Production resource scheduling |
| resource scheduling | Operations concept | Scheduling access to available compute/memory resources. | Production serving |
| scaling | Operations concept | Increasing serving capacity as workload or users grow. | Production serving |
| monitoring | Operations concept | Observing serving behavior and operational health. | Production serving |
| availability | Reliability concept | Whether the service is accessible and able to respond when needed. | Production serving |
| operational demands | Operations concept | Serving requirements that grow with users and requests. | Local vs Production Serving |
| workload | Operations concept | The volume/pattern of users and requests handled by the system. | “Scope changes with the workload” |
| number of users | Workload dimension | Count of users affecting operational serving requirements. | Local vs production note |
| number of requests | Workload dimension | Request volume affecting operational serving requirements. | Local vs production note |
| multiple requests | Workload pattern | More than one request requiring coordination/scheduling. | Production serving |
| local serving | Deployment mode | Serving a model locally, commonly for a single user. | Local vs Production Serving |
| production serving | Deployment mode | Serving under operational demands such as multiple requests, scheduling, scaling, monitoring, and availability. | Local vs Production Serving |
| local single user | Workload/deployment mode | A local setup intended for one user. | Local grid |
| LOCAL SINGLE USER | Label variant | Uppercase label for the local single-user case. | Local grid |
| production | Alias / deployment context | Production environment with larger operational requirements. | PRODUCTION SERVING |
| PRODUCTION SERVING | Label variant | Uppercase label for production deployment. | Local grid |
| Ollama | Tool / serving example | Example of local model serving on a laptop. | “Ollama on a laptop”; related link |
| laptop | Hardware/deployment example | Local device used in the Ollama example. | Local single-user card |
| Quantization | Related concept | Technique for representing model values with reduced precision/size; linked as related, not explained here. | Related-concepts tag |
| Latency | Metric / related concept | Time taken for a request or response; linked as related, not defined here. | Related-concepts tag |
| TPS | Abbreviation / metric | Tokens per second, a throughput/speed metric for token generation; linked as related. | Related-concepts tag |
| tokens per second | Metric expansion | Number of generated tokens produced per second. | Expansion of TPS link |
| vLLM | Tool / serving example | A model-serving/runtime project named as “coming soon.” | Related-concepts tag |
| RAG | Abbreviation / example task | Retrieval-Augmented Generation, used as the example question sent through the serving path. | “Explain RAG.” |
| Retrieval-Augmented Generation | Expansion of RAG | A generation workflow that uses retrieved information; the page uses only the acronym/example. | Candidate expansion for RAG |
| explain RAG | Example request | Example natural-language task submitted by an application. | Request section heading |
| restaurant kitchen | Analogy | Mental model for the model-serving stack. | Beginner-friendly analogy |
| recipe | Analogy | Analogy for the model’s learned knowledge/behavior. | Model analogy cell |
| cooking knowledge | Analogy | Analogy for learned behavior represented by a model. | Model analogy cell |
| kitchen equipment | Analogy | Analogy for the runtime that executes the model. | Runtime analogy cell |
| restaurant operation | Analogy | Analogy for the serving system that receives orders and delivers meals. | Serving system analogy cell |
| orders | Analogy / request | Restaurant analogy for application requests. | Serving-system analogy |
| meals | Analogy / result | Restaurant analogy for returned model results. | Serving-system analogy |
| delivery | Analogy / output operation | Delivering results back to the requester. | “delivers meals” analogy |
| learned knowledge | Analogy / model concept | Knowledge-like behavior encoded in a model. | Recipe/cooking-knowledge analogy |
| available | Service property | Made accessible to applications or users. | Hero; production availability |
| availability property | Reliability concept | Service property indicating accessibility when needed. | Production serving |
| usable | Service property | Practical quality of an inference interface for applications. | “usable service” |
| operational | Operations descriptor | Relating to running a serving system in practice. | Operational demands |
| single-user | Deployment qualifier | Workload limited to one user. | Local single user |
| local | Deployment qualifier | Running the model/serving system on a nearby device. | Local vs Production Serving |
| production | Deployment qualifier | Running a service for real operational workloads. | Production serving |
| AI | Domain term | Artificial intelligence capability requested by the application. | “AI capability” |
| application-to-hardware path | Workflow / architecture | End-to-end path from application request to hardware execution. | Serving stack |
| application request path | Workflow | Sequence Application → API → Serving System → Runtime → Model Inference → Generated Tokens → API Response → App. | Follow one request |
| request flow | Workflow | Ordered movement of an inference request through serving layers. | “Follow one request” |
| input | Inference concept | Information supplied to a model for inference, implicit in “request.” | Inference definition candidate |
| output | Inference concept | Information produced by inference and returned as a result. | Generated tokens/API response |
| receive | Operation | Accepting a request at the API or serving system. | Stack and hero |
| execute | Operation | Performing the model computation in the runtime. | Runtime definition |
| return | Operation | Sending results to the application. | Hero and model-file explanation |
| provide learned behavior | Model responsibility | Model layer’s role in the stack. | Model stack row |
| provide compute | Hardware responsibility | Hardware’s role in supplying processing capacity. | Hardware stack row |
| provide memory | Hardware responsibility | Hardware’s role in supplying memory capacity. | Hardware stack row |
| model access | Access concept | Application access to a hosted/exposed model. | Model Server manages access |
| service | Service concept | A callable operational interface, distinct from the model artifact. | “Model ≠ service” |
| model service | Confusable concept | A service built around a model; not identical to the model itself. | “Model ≠ service” |
| model ≠ service | Distinction | Explicit warning that the learned model is not the same thing as the serving service. | Model vs Model Server |
| runtime is one layer inside serving | Relationship | Runtime executes inference but is only one layer of the larger serving system. | Runtime vs Serving note |
| model server vs model | Distinction | Model is learned weights; model server is software/system exposing the model. | Section 05 |
| without serving | Contrast state | Model exists but applications cannot easily use it. | Why Serving Matters |
| with serving | Contrast state | Applications can send requests through the model and receive responses. | Why Serving Matters |
| inference availability | Service property | Making inference callable/available to applications. | Runtime vs Serving |
| access control | Potential missing serving concept | Policy for deciding who may call a model; not explicitly explained on page. | Potential follow-up concept |
| authentication | Potential missing serving concept | Verifying callers before allowing API access; not explicitly explained. | Potential follow-up concept |
| authorization | Potential missing serving concept | Determining permitted model/API actions; not explicitly explained. | Potential follow-up concept |
| concurrency | Potential missing serving concept | Handling simultaneous requests; suggested by production/multiple requests but not defined. | Potential follow-up concept |
| throughput | Potential missing metric | Amount of work/requests/tokens served per unit time; related to TPS but not defined. | Potential follow-up concept |
| time to first token | Potential missing metric | Delay until the first generated token; not defined on page. | Potential follow-up concept |
| tail latency | Potential missing metric | High-percentile request latency; not defined on page. | Potential follow-up concept |
| request rate | Potential missing metric | Incoming requests per unit time; implied by workload but not defined. | Potential follow-up concept |
| health check | Potential missing operations concept | Probe indicating whether a server is healthy; not defined. | Potential follow-up concept |
| load balancing | Potential missing operations concept | Distributing requests across serving instances; not defined. | Potential follow-up concept |
| autoscaling | Potential missing operations concept | Automatically changing serving capacity with demand; not defined. | Potential follow-up concept |
| model loading | Potential missing lifecycle concept | Loading model weights into runtime/hardware memory; implied by execution but not described. | Potential follow-up concept |
| model unloading | Potential missing lifecycle concept | Removing a model from runtime resources; not described. | Potential follow-up concept |
| warm-up | Potential missing lifecycle concept | Preparing a runtime/model before traffic; not described. | Potential follow-up concept |
| model registry | Potential missing management concept | Catalog/location for deployable model versions; not described. | Potential follow-up concept |
| model version | Potential missing management concept | Distinct released version of model weights/configuration; not described. | Potential follow-up concept |
| deployment | Potential missing operations concept | Putting a model server into a runnable environment; not explicitly defined. | Potential follow-up concept |
| endpoint | Potential missing API concept | Network address through which a model service is called; not explicitly defined. | Potential follow-up concept |
| HTTP | Potential missing protocol concept | Common transport for API requests/responses; not mentioned. | Potential follow-up concept |
| streaming | Potential missing response mode | Returning generated output incrementally; not mentioned. | Potential follow-up concept |
| error handling | Potential missing operations concept | Handling failed requests or runtime errors; not mentioned. | Potential follow-up concept |
| observability | Potential missing operations concept | Logs, metrics, and traces used to understand serving behavior; only monitoring is named. | Potential follow-up concept |
| logging | Potential missing observability concept | Recording requests, errors, and operations; not mentioned. | Potential follow-up concept |
| metrics | Potential missing observability concept | Quantitative measurements such as latency/TPS; not explicitly explained. | Potential follow-up concept |
| tracing | Potential missing observability concept | Following a request through serving layers; not mentioned. | Potential follow-up concept |
| fault tolerance | Potential missing reliability concept | Continuing service despite component failures; not mentioned. | Potential follow-up concept |
| high availability | Potential missing reliability concept | Maintaining service availability across failures; availability is named but not expanded. | Potential follow-up concept |
| autoscaling policy | Potential missing scheduling concept | Rules for scaling instances/resources; not described. | Potential follow-up concept |
| queueing | Potential missing scheduling concept | Waiting and ordering behavior for queued requests; queues are named but not explained. | Potential follow-up concept |
| dynamic batching | Potential missing optimization concept | Forming batches from arriving requests at runtime; batching is named but not explained. | Potential follow-up concept |
| quantized model | Potential missing model variant | A model represented using quantization; related link names only Quantization. | Potential follow-up concept |
| model format | Potential missing artifact concept | File/serialization format for learned weights; model file is named but format is not. | Potential follow-up concept |
| accelerator | Potential missing hardware concept | Hardware specialized for model computation; GPU is named but accelerator is not. | Potential follow-up concept |
| CPU | Potential missing hardware concept | General-purpose processor that may execute inference; not mentioned. | Potential follow-up concept |
| GPU memory | Potential missing hardware concept | Memory available on/near a GPU for weights and execution; not expanded. | Potential follow-up concept |
| context window | Potential missing model-serving concept | Maximum context an inference request can use; not mentioned. | Potential follow-up concept |
| prompt | Potential missing request concept | Text/input supplied to a generative model; example request is “Explain RAG” but prompt is not named. | Potential follow-up concept |
| completion | Potential missing output concept | Generated answer/output returned by a generative model; not named. | Potential follow-up concept |

## Potential Missing Concepts

These are useful glossary entries suggested by the page’s architecture or operational language but not fully explained in the source body:

- endpoint, deployment, model loading, model lifecycle, model version, model registry
- concurrency, throughput, request rate, latency, tail latency, time to first token, tokens per second
- queueing, scheduling policy, dynamic batching, load balancing, autoscaling
- authentication, authorization, access control, rate limiting, multi-tenancy
- health checks, observability, logging, metrics, tracing, error handling
- streaming responses, request/response schema, protocol, HTTP, endpoint routing
- CPU, accelerator, GPU memory, model format, quantized model
- prompt, completion, context window, input tokens, output tokens
- fault tolerance, high availability, graceful shutdown, retries

## Aliases / Synonyms

Keep these as separate raw candidates until the later glossary pass decides whether to merge them:

| Candidate | Possible alias/synonym relationship |
|---|---|
| Model Serving | serving; serving system; model-serving system |
| inference service | usable inference service; model service |
| model server | server; serving component; software/system exposing the model |
| runtime | model runtime; runtime layer; execution layer |
| application | applications; app; application layer |
| API | application programming interface; API interface; ordering interface |
| request | API request; inference request; request input |
| response | API response; result; returned output |
| model | trained model; model layer; learned behavior holder |
| weights | model weights; learned weights; learned numeric state |
| hardware | hardware layer; compute/memory resources; GPU / Memory |
| local serving | local single-user serving; Ollama on a laptop |
| production serving | production; production deployment; operational serving |
| batching | request batching; batch processing |
| queues | queue; request queue; queueing |
| GPU / Memory | GPU memory; hardware resources |
| TPS | tokens per second |
| RAG | Retrieval-Augmented Generation |
| serving stack | stack; layered serving path; application-to-hardware path |

## Do Not Confuse Candidates

| Candidate A | Candidate B | Distinction suggested by the page |
|---|---|---|
| Model | Model Server | The model contains learned weights/behavior; the model server is software/system exposing it to applications. |
| Model | Service | “Model ≠ service”: an artifact/learned component is not the callable operational interface around it. |
| Runtime | Model Serving | Runtime executes inference; serving makes inference available and may manage requests, models, resources, queues, batching, and access. |
| Runtime | Model Server | Runtime is an execution layer; model server is the exposing/managing system. They may be packaged together but have different roles. |
| Model file | Model Serving | A model file alone does not receive requests, manage resources, or return results. |
| API | Model Server | API receives requests/returns responses; model server manages access and connects the interface to execution. |
| API request | API response | Request enters the serving path; response leaves it after inference. |
| Application | API | Application asks for capability; API is the interface it uses. |
| Serving system | Runtime | Serving system covers operations around the runtime; runtime performs execution. |
| Learned behavior | Inference | Learned behavior is what the model contains; inference is running it on a request. |
| Generated tokens | API response | Generated tokens are output units; API response is the transport/result returned to the app. |
| Hardware | Runtime | Hardware supplies compute/memory; runtime executes model operations using those resources. |
| Local serving | Production serving | Same core idea, different workload/operational demands. |
| Latency | TPS | Latency measures time/delay; TPS measures generated tokens per second. The page links both but does not define them. |
| Quantization | Model Serving | Quantization is a related model representation technique; serving is the system making inference available. |
| Ollama | Model | Ollama is a local serving tool/example, not the learned model itself. |
| vLLM | Runtime / serving system | vLLM is named as a forthcoming related concept; do not treat the name as synonymous with every runtime or server. |
| RAG | Model Serving | RAG is the example task/request; model serving is the infrastructure path used to answer it. |

## Notes

- The page is intentionally introductory and architecture-oriented. It defines responsibilities and relationships more strongly than implementation details.
- The visible request path is: **APP → API REQUEST → SERVING SYSTEM → RUNTIME → MODEL INFERENCE → GENERATED TOKENS → API RESPONSE → APP**.
- The visible serving stack is: **APPLICATION → API → MODEL SERVER → RUNTIME → MODEL → HARDWARE**.
- “Model server” and “serving system” are close but not guaranteed to be identical: the page calls the former a software/system exposing the model and uses the latter for the broader operational flow.
- “Runtime is one layer inside serving” is an explicit relationship and should be retained as a glossary note, not flattened into a synonym.
- The restaurant analogy is pedagogical: model = recipe/cooking knowledge, runtime = kitchen equipment, serving system = restaurant operation, API = ordering interface.
- The source mentions no concrete API protocol, deployment manifest, server configuration, model format, authentication method, or numerical serving benchmark.
- The source links to Ollama, Quantization, Latency, and TPS; vLLM is listed as “coming soon.” These linked names are retained as candidates even where the page does not explain them.
- The video section is a placeholder (“Visual explainer coming soon”) and contributes no additional technical definition.
- Repeated labels, uppercase variants, shorthand, analogy terms, and broader operational terms are intentionally retained for later deduplication and editorial review.
