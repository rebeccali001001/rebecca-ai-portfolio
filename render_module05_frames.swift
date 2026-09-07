import AppKit
import Foundation

let outputRoot = URL(fileURLWithPath: CommandLine.arguments.count > 1 ? CommandLine.arguments[1] : NSTemporaryDirectory(), isDirectory: true)
let width: CGFloat = 1920
let height: CGFloat = 1080

struct Scene { let kind: String; let label: String; let title: String; let caption: String }
struct Topic { let slug: String; let accent: NSColor; let scenes: [Scene] }

let topics = [
    Topic(slug: "ollama", accent: NSColor(calibratedRed: 0.47, green: 0.90, blue: 0.74, alpha: 1), scenes: [
        Scene(kind: "pipeline", label: "01 · DEFINITION", title: "OLLAMA", caption: "Software that downloads, runs, and manages models locally."),
        Scene(kind: "analogy", label: "02 · EASY ANALOGY", title: "A MEDIA PLAYER FOR MODELS", caption: "The model is the file; Ollama loads and plays it."),
        Scene(kind: "context", label: "03 · HOW IT WORKS", title: "REQUEST → API → RUNTIME", caption: "A local app calls the API; the runtime loads the selected model."),
        Scene(kind: "sample", label: "04 · EXAMPLES", title: "LOCAL CHAT OR LOCAL APP", caption: "Run a Qwen model, call the local API, or switch models."),
        Scene(kind: "takeaway", label: "05 · KEY TAKEAWAY", title: "RUNTIME, NOT MODEL", caption: "Ollama runs and manages AI models; it is not the model itself.")
    ]),
    Topic(slug: "quantization", accent: NSColor(calibratedRed: 1, green: 0.78, blue: 0.43, alpha: 1), scenes: [
        Scene(kind: "vector", label: "01 · DEFINITION", title: "QUANTIZATION", caption: "Lower numerical precision can reduce memory and sometimes improve speed."),
        Scene(kind: "analogy", label: "02 · EASY ANALOGY", title: "LIKE IMAGE COMPRESSION", caption: "Smaller representation can trade some detail for easier use."),
        Scene(kind: "pipeline", label: "03 · HOW IT WORKS", title: "HIGH PRECISION → FEWER BITS", caption: "A new representation can fit more limited hardware."),
        Scene(kind: "sample", label: "04 · EXAMPLES", title: "LAPTOP OR EDGE DEVICE", caption: "A quantized model may fit where full precision does not."),
        Scene(kind: "takeaway", label: "05 · KEY TAKEAWAY", title: "MEMORY DOWN, TRADE-OFFS", caption: "Quantization changes precision; it is not fine-tuning or ZIP compression.")
    ]),
    Topic(slug: "runtime-constraints", accent: NSColor(calibratedRed: 0.50, green: 0.69, blue: 1, alpha: 1), scenes: [
        Scene(kind: "boundary", label: "01 · DEFINITION", title: "RUNTIME CONSTRAINTS", caption: "Limits on memory, time, cost, and environment shape the running system."),
        Scene(kind: "analogy", label: "02 · EASY ANALOGY", title: "A SMALL KITCHEN", caption: "The plan must fit the tools, space, ingredients, and time available."),
        Scene(kind: "pipeline", label: "03 · HOW IT WORKS", title: "MEASURE → MATCH → TEST", caption: "Configure the workload, measure behavior, and adjust the design."),
        Scene(kind: "sample", label: "04 · EXAMPLES", title: "MEMORY OR LATENCY LIMIT", caption: "Use quantization, smaller context, caching, or streaming when appropriate."),
        Scene(kind: "takeaway", label: "05 · KEY TAKEAWAY", title: "MODEL CHOICE BECOMES DESIGN", caption: "Constraints make an abstract model choice practical.")
    ]),
    Topic(slug: "latency", accent: NSColor(calibratedRed: 0.91, green: 0.57, blue: 0.96, alpha: 1), scenes: [
        Scene(kind: "pipeline", label: "01 · DEFINITION", title: "LATENCY", caption: "The time between an AI request and the result becoming available."),
        Scene(kind: "analogy", label: "02 · EASY ANALOGY", title: "WAITING FOR A PHONE REPLY", caption: "First pause resembles time to first token; full reply is total wait."),
        Scene(kind: "pipeline", label: "03 · HOW IT WORKS", title: "REQUEST → PREPARE → FINISH", caption: "Context, generation, and delivery all contribute to the wait."),
        Scene(kind: "sample", label: "04 · EXAMPLES", title: "SHORT CHAT OR LONG DOCUMENT", caption: "More context can mean a longer wait before the answer starts."),
        Scene(kind: "takeaway", label: "05 · KEY TAKEAWAY", title: "TOTAL USER WAIT", caption: "Latency is broader than model speed and different from throughput.")
    ]),
    Topic(slug: "tokens-per-second", accent: NSColor(calibratedRed: 0.78, green: 0.91, blue: 0.41, alpha: 1), scenes: [
        Scene(kind: "vector", label: "01 · DEFINITION", title: "TOKENS PER SECOND", caption: "TPS counts output tokens generated in one second."),
        Scene(kind: "analogy", label: "02 · EASY ANALOGY", title: "A PRINTER'S PAGES PER MINUTE", caption: "Generation speed is only part of the whole request experience."),
        Scene(kind: "pipeline", label: "03 · HOW IT WORKS", title: "PREDICT → EMIT → REPEAT", caption: "Count output tokens and divide by generation time."),
        Scene(kind: "sample", label: "04 · EXAMPLES", title: "SHORT ANSWER OR LONG REPORT", caption: "More output tokens can take longer even at a steady speed."),
        Scene(kind: "takeaway", label: "05 · KEY TAKEAWAY", title: "ONE GENERATION METRIC", caption: "TPS is not words per second, first-token time, or total response time.")
    ]),
    Topic(slug: "token", accent: NSColor(calibratedRed: 0.98, green: 0.66, blue: 0.35, alpha: 1), scenes: [
        Scene(kind: "token", label: "01 · DEFINITION", title: "TOKENS", caption: "Small units of text processed by a language model."),
        Scene(kind: "split", label: "02 · EXAMPLE", title: "TEXT BECOMES PIECES", caption: "A word, a word piece, or a character sequence can become a token."),
        Scene(kind: "stream", label: "03 · WORKFLOW", title: "INPUT -> PREDICTION -> OUTPUT", caption: "The model processes token pieces and predicts more token pieces."),
        Scene(kind: "compare", label: "04 · BOUNDARY", title: "TOKEN IS NOT WORD", caption: "Token boundaries depend on the tokenizer and the text."),
        Scene(kind: "takeaway", label: "05 · KEY TAKEAWAY", title: "MODELS READ TOKENS", caption: "Token counts are not the same as word, character, or parameter counts.")
    ]),
    Topic(slug: "context-window", accent: NSColor(calibratedRed: 0.36, green: 0.78, blue: 0.96, alpha: 1), scenes: [
        Scene(kind: "desk", label: "01 · DEFINITION", title: "CONTEXT WINDOW", caption: "The model's working space for tokens available right now."),
        Scene(kind: "items", label: "02 · CONTENT", title: "WHAT FITS ON THE DESK", caption: "Instructions, messages, files, retrieval, tools, and generated text can all contribute."),
        Scene(kind: "deskfull", label: "03 · LIMIT", title: "A FULL DESK", caption: "Context size is usually measured in tokens."),
        Scene(kind: "compare", label: "04 · BOUNDARY", title: "NOT PERMANENT MEMORY", caption: "A context window is runtime working space, not model knowledge or long-term memory."),
        Scene(kind: "takeaway", label: "05 · KEY TAKEAWAY", title: "ONE MOMENT OF WORK", caption: "The context window is the information a model can work with at one time.")
    ]),
    Topic(slug: "kv-cache", accent: NSColor(calibratedRed: 0.72, green: 0.58, blue: 1, alpha: 1), scenes: [
        Scene(kind: "cache", label: "01 · DEFINITION", title: "KV CACHE", caption: "Temporary memory for earlier attention information."),
        Scene(kind: "notes", label: "02 · EASY ANALOGY", title: "KEEP NOTES WHILE READING", caption: "Reuse notes instead of rereading every earlier page."),
        Scene(kind: "cacheflow", label: "03 · WORKFLOW", title: "READ -> STORE -> GENERATE", caption: "Key and value states are reused for the next token."),
        Scene(kind: "grow", label: "04 · TRADEOFF", title: "THE CACHE GROWS", caption: "New states join the cache as generation continues, using memory."),
        Scene(kind: "takeaway", label: "05 · KEY TAKEAWAY", title: "REUSE, NOT MEMORY", caption: "KV cache makes ongoing generation more efficient within an active request.")
    ]),
    Topic(slug: "embeddings", accent: NSColor(calibratedRed: 0.47, green: 0.90, blue: 0.74, alpha: 1), scenes: [
        Scene(kind: "map", label: "01 · REPRESENT", title: "EMBEDDINGS", caption: "A sentence gets a place on a meaning map."),
        Scene(kind: "vector", label: "02 · DEFINITION", title: "NUMBERS THAT KEEP RELATIONSHIPS", caption: "Similar ideas can land near each other, even with different words."),
        Scene(kind: "sample", label: "03 · LIFE SAMPLE", title: "POST-DEPARTURE POLICY", caption: "After the vessel sails can match post-departure cancellation."),
        Scene(kind: "analogy", label: "04 · EASY ANALOGY", title: "PIN SENTENCES ON A MAP", caption: "A map helps a librarian find nearby cards."),
        Scene(kind: "takeaway", label: "05 · KEY TAKEAWAY", title: "REPRESENTATION, NOT AN ANSWER", caption: "Use the vector to find evidence, then inspect the source.")
    ]),
    Topic(slug: "rag", accent: NSColor(calibratedRed: 0.50, green: 0.69, blue: 1, alpha: 1), scenes: [
        Scene(kind: "pipeline", label: "01 · FLOW", title: "RAG", caption: "A model gets the right page before it writes."),
        Scene(kind: "context", label: "02 · DEFINITION", title: "EVIDENCE ENTERS THE PROMPT", caption: "Search selects passages; generation uses them as context."),
        Scene(kind: "sample", label: "03 · LIFE SAMPLE", title: "CURRENT SETTLEMENT POLICY", caption: "Question plus policy card becomes a traceable answer."),
        Scene(kind: "analogy", label: "04 · EASY ANALOGY", title: "THE LIBRARIAN BRINGS THE CARD", caption: "The assistant opens a page instead of guessing from memory."),
        Scene(kind: "takeaway", label: "05 · KEY TAKEAWAY", title: "RETRIEVE FIRST, ANSWER SECOND", caption: "RAG depends on fresh, relevant, permitted sources.")
    ]),
    Topic(slug: "vector-search", accent: NSColor(calibratedRed: 1, green: 0.78, blue: 0.43, alpha: 1), scenes: [
        Scene(kind: "scatter", label: "01 · FIND", title: "VECTOR SEARCH", caption: "Meaning becomes a ranked candidate list."),
        Scene(kind: "topk", label: "02 · DEFINITION", title: "QUERY -> INDEX -> TOP-K", caption: "The index returns nearby vectors, then filters can refine them."),
        Scene(kind: "sample", label: "03 · LIFE SAMPLE", title: "DELAYED SHIPMENT CLAIM", caption: "Top results keep the right policy version and region."),
        Scene(kind: "analogy", label: "04 · EASY ANALOGY", title: "WALK TO THE NEAREST SHELF", caption: "Closest does not mean correct; check the label before using it."),
        Scene(kind: "takeaway", label: "05 · KEY TAKEAWAY", title: "CANDIDATE FINDING IS NOT PROOF", caption: "Ranking, access, freshness, and source quality still matter.")
    ]),
    Topic(slug: "grounding", accent: NSColor(calibratedRed: 0.91, green: 0.57, blue: 0.96, alpha: 1), scenes: [
        Scene(kind: "receipt", label: "01 · CHECK", title: "GROUNDING", caption: "Evidence makes a response inspectable."),
        Scene(kind: "boundary", label: "02 · DEFINITION", title: "SOURCE -> CONTEXT -> CITATION", caption: "Grounding sets a boundary around what the model may claim."),
        Scene(kind: "sample", label: "03 · LIFE SAMPLE", title: "POLICY V4.2, SECTION 3.1", caption: "A cited exception is stronger than a fluent guess."),
        Scene(kind: "analogy", label: "04 · EASY ANALOGY", title: "A RECEIPT BESIDE THE ANSWER", caption: "If the receipt is missing, say you cannot confirm."),
        Scene(kind: "takeaway", label: "05 · KEY TAKEAWAY", title: "EVIDENCE IS AN HONEST CONTRACT", caption: "Grounding reduces unsupported claims, not every mistake.")
    ]),
    Topic(slug: "transformer", accent: NSColor(calibratedRed: 0.47, green: 0.76, blue: 1, alpha: 1), scenes: [
        Scene(kind: "pipeline", label: "01 · DEFINITION", title: "TRANSFORMER", caption: "A neural-network architecture for relationships between tokens."),
        Scene(kind: "analogy", label: "02 · EASY ANALOGY", title: "A READING GROUP", caption: "Every word looks around and weighs which other words matter."),
        Scene(kind: "transform", label: "03 · HOW IT WORKS", title: "TOKENS → ATTENTION → LAYERS", caption: "Embeddings enter attention and feed-forward layers that refine representations."),
        Scene(kind: "sample", label: "04 · REAL EXAMPLE", title: "PRONOUN RESOLUTION", caption: "Attention can weigh nearby words when a sentence contains it or they."),
        Scene(kind: "pipeline", label: "05 · OUTPUT", title: "SCORES → DECODE", caption: "The final layer scores possible next tokens or task labels."),
        Scene(kind: "takeaway", label: "06 · REMEMBER", title: "ARCHITECTURE, NOT PRODUCT", caption: "A Transformer uses attention and stacked layers to process token relationships.")
    ]),
    Topic(slug: "retrieval", accent: NSColor(calibratedRed: 0.42, green: 0.86, blue: 0.96, alpha: 1), scenes: [
        Scene(kind: "pipeline", label: "01 · SELECT", title: "RETRIEVAL", caption: "Find and select useful existing information."),
        Scene(kind: "context", label: "02 · DEFINITION", title: "QUERY TO EVIDENCE", caption: "Search can combine text, vectors, metadata, and filters."),
        Scene(kind: "topk", label: "03 · HOW IT WORKS", title: "SEARCH, RANK, FILTER", caption: "Put useful candidates first, then apply source rules."),
        Scene(kind: "analogy", label: "04 · EASY ANALOGY", title: "THE RIGHT LIBRARY PAGES", caption: "A question needs a small selection from a large collection."),
        Scene(kind: "takeaway", label: "05 · KEY TAKEAWAY", title: "SELECT, THEN USE", caption: "Retrieval finds evidence; generation is a separate step.")
    ])
]

func fill(_ rect: NSRect, _ color: NSColor, radius: CGFloat = 0) { color.setFill(); if radius > 0 { NSBezierPath(roundedRect: rect, xRadius: radius, yRadius: radius).fill() } else { rect.fill() } }
func stroke(_ rect: NSRect, _ color: NSColor, radius: CGFloat = 0, width: CGFloat = 2) { color.setStroke(); let path = NSBezierPath(roundedRect: rect, xRadius: radius, yRadius: radius); path.lineWidth = width; path.stroke() }
func text(_ value: String, x: CGFloat, top: CGFloat, size: CGFloat, color: NSColor, weight: NSFont.Weight = .regular, width: CGFloat = 1600) { let font = NSFont.systemFont(ofSize: size, weight: weight); let attrs: [NSAttributedString.Key: Any] = [.font: font, .foregroundColor: color]; let rect = NSRect(x: x, y: height - top - size * 1.38, width: width, height: size * 1.7); NSString(string: value).draw(in: rect, withAttributes: attrs) }
func card(_ rect: NSRect, accent: NSColor, label: String, value: String, detail: String, valueSize: CGFloat = 30) { fill(rect, NSColor(calibratedRed: 0.055, green: 0.13, blue: 0.20, alpha: 0.98), radius: 20); stroke(rect, accent, radius: 20, width: 2); text(label, x: rect.minX + 26, top: height - rect.maxY + 24, size: 18, color: accent, weight: .bold, width: rect.width - 52); text(value, x: rect.minX + 26, top: height - rect.maxY + 68, size: valueSize, color: .white, weight: .semibold, width: rect.width - 52); text(detail, x: rect.minX + 26, top: height - rect.maxY + 122, size: 19, color: NSColor(calibratedWhite: 0.78, alpha: 1), width: rect.width - 52) }
func arrow(_ x1: CGFloat, _ y1: CGFloat, _ x2: CGFloat, _ y2: CGFloat, _ color: NSColor) { color.setStroke(); let path = NSBezierPath(); path.move(to: NSPoint(x: x1, y: y1)); path.line(to: NSPoint(x: x2, y: y2)); path.lineWidth = 5; path.stroke(); let head = NSBezierPath(); head.move(to: NSPoint(x: x2, y: y2)); head.line(to: NSPoint(x: x2 - 18, y: y2 + 10)); head.move(to: NSPoint(x: x2, y: y2)); head.line(to: NSPoint(x: x2 - 18, y: y2 - 10)); head.lineWidth = 5; head.stroke() }
func dot(_ x: CGFloat, _ y: CGFloat, _ r: CGFloat, _ color: NSColor) { color.setFill(); NSBezierPath(ovalIn: NSRect(x: x-r, y: y-r, width: r*2, height: r*2)).fill() }

func drawGraphic(_ topic: Topic, _ scene: Scene) {
    let a = topic.accent
    switch scene.kind {
    case "map":
        card(NSRect(x: 120, y: 390, width: 450, height: 175), accent: a, label: "INPUT", value: "policy sentence", detail: "meaning in words")
        arrow(620, 478, 820, 478, a)
        card(NSRect(x: 900, y: 390, width: 450, height: 175), accent: a, label: "OUTPUT", value: "a point on a map", detail: "meaning as location")
        for i in 0..<7 { dot(1450 + CGFloat(i % 3) * 105, 430 + CGFloat(i / 3) * 95, 18, i == 4 ? a : NSColor(calibratedWhite: 0.55, alpha: 0.9)) }
        text("nearby meaning", x: 1400, top: 610, size: 22, color: a, weight: .semibold, width: 350)
    case "vector":
        card(NSRect(x: 170, y: 370, width: 440, height: 190), accent: a, label: "TEXT", value: "after the vessel sails", detail: "one query")
        arrow(660, 465, 850, 465, a)
        card(NSRect(x: 940, y: 370, width: 620, height: 190), accent: a, label: "VECTOR", value: "[0.21, -0.08, 0.74 ...]", detail: "numbers preserve useful relationships", valueSize: 27)
        for i in 0..<8 { fill(NSRect(x: 1040 + CGFloat(i)*54, y: 265, width: 34, height: CGFloat(35 + (i*17)%95)), a, radius: 7) }
    case "sample":
        card(NSRect(x: 130, y: 385, width: 490, height: 180), accent: a, label: "QUESTION", value: "after the vessel sails", detail: "user wording", valueSize: 27)
        arrow(670, 475, 850, 475, a)
        card(NSRect(x: 900, y: 385, width: 760, height: 180), accent: a, label: "NEARBY CHUNK", value: "post-departure cancellation", detail: "different words, related meaning", valueSize: 30)
        text("similar intent", x: 760, top: 625, size: 23, color: a, weight: .bold, width: 300)
    case "analogy":
        for i in 0..<4 { card(NSRect(x: 130 + CGFloat(i)*420, y: 365, width: 330, height: 200), accent: i == 2 ? a : NSColor(calibratedWhite: 0.42, alpha: 1), label: "CARD 0\(i+1)", value: i == 2 ? "nearest idea" : "another idea", detail: i == 2 ? "pull this one first" : "farther away", valueSize: 26) }
        text("a librarian chooses the nearby card", x: 460, top: 800, size: 25, color: a, weight: .semibold, width: 1000)
    case "pipeline":
        let labels = [("01", "QUESTION"), ("02", "SEARCH"), ("03", "CONTEXT"), ("04", "ANSWER")]
        for i in 0..<4 { card(NSRect(x: 105 + CGFloat(i)*450, y: 390, width: 330, height: 180), accent: a, label: labels[i].0, value: labels[i].1, detail: i == 0 ? "what the user asks" : i == 1 ? "find the source" : i == 2 ? "put it beside model" : "write with evidence", valueSize: 27); if i < 3 { arrow(455 + CGFloat(i)*450, 480, 525 + CGFloat(i)*450, 480, a) } }
    case "context":
        card(NSRect(x: 145, y: 370, width: 430, height: 200), accent: a, label: "SOURCE", value: "policy page", detail: "external knowledge")
        arrow(650, 470, 840, 470, a)
        card(NSRect(x: 910, y: 370, width: 770, height: 200), accent: a, label: "MODEL CONTEXT", value: "question + selected passages", detail: "evidence arrives before generation", valueSize: 29)
    case "scatter":
        stroke(NSRect(x: 180, y: 290, width: 690, height: 360), NSColor(calibratedWhite: 0.32, alpha: 1), radius: 16, width: 2); for i in 0..<17 { dot(235 + CGFloat((i*137)%570), 345 + CGFloat((i*83)%260), 14, i == 11 ? a : NSColor(calibratedWhite: 0.55, alpha: 0.9)) }; dot(705, 495, 28, a); text("QUERY", x: 675, top: 320, size: 20, color: a, weight: .bold, width: 140); arrow(930, 470, 1110, 470, a); card(NSRect(x: 1180, y: 390, width: 540, height: 180), accent: a, label: "RESULT", value: "top-k candidates", detail: "ranked by closeness", valueSize: 28)
    case "topk":
        card(NSRect(x: 130, y: 390, width: 380, height: 180), accent: a, label: "QUERY", value: "claim documents", detail: "embed the intent", valueSize: 27); arrow(570, 480, 730, 480, a); card(NSRect(x: 790, y: 330, width: 420, height: 130), accent: a, label: "1 · 0.93", value: "claim documents", detail: "strong match", valueSize: 26); card(NSRect(x: 790, y: 490, width: 420, height: 130), accent: NSColor(calibratedWhite: 0.45, alpha: 1), label: "2 · 0.86", value: "delay policy", detail: "supporting context", valueSize: 26); card(NSRect(x: 1300, y: 390, width: 430, height: 180), accent: a, label: "FILTER", value: "current region", detail: "keep the right evidence", valueSize: 27)
    case "receipt", "boundary":
        card(NSRect(x: 100, y: 390, width: 390, height: 185), accent: a, label: "SOURCE", value: "policy v4.2", detail: "approved evidence", valueSize: 28); arrow(540, 480, 700, 480, a); card(NSRect(x: 770, y: 390, width: 390, height: 185), accent: a, label: "CONTEXT", value: "section 3.1", detail: "inside the prompt", valueSize: 28); arrow(1210, 480, 1370, 480, a); card(NSRect(x: 1440, y: 390, width: 390, height: 185), accent: a, label: "ANSWER", value: "with a citation", detail: "inspectable claim", valueSize: 28)
    case "transform":
        card(NSRect(x: 90, y: 390, width: 300, height: 180), accent: a, label: "1 · INPUT", value: "TOKENS", detail: "IDs and vectors", valueSize: 27); arrow(425, 480, 555, 480, a)
        card(NSRect(x: 600, y: 390, width: 360, height: 180), accent: a, label: "2 · MIX", value: "ATTENTION", detail: "compare context", valueSize: 27); arrow(995, 480, 1125, 480, a)
        card(NSRect(x: 1170, y: 390, width: 300, height: 180), accent: a, label: "3 · REFINE", value: "LAYERS", detail: "feed-forward stack", valueSize: 27); arrow(1505, 480, 1635, 480, a)
        card(NSRect(x: 1650, y: 390, width: 210, height: 180), accent: a, label: "4 · SCORE", value: "OUTPUT", detail: "next token", valueSize: 25)
    default:
        card(NSRect(x: 180, y: 390, width: 450, height: 190), accent: a, label: "EVIDENCE", value: "source card", detail: "available to check", valueSize: 28); arrow(700, 485, 900, 485, a); card(NSRect(x: 970, y: 390, width: 690, height: 190), accent: a, label: "BOUNDARY", value: "answer or abstain", detail: "no source means no guess", valueSize: 30)
    }
}

func render(_ topic: Topic, _ scene: Scene, _ index: Int) {
    let folder = outputRoot.appendingPathComponent(topic.slug, isDirectory: true); try? FileManager.default.createDirectory(at: folder, withIntermediateDirectories: true)
    let canvas = NSImage(size: NSSize(width: width, height: height)); canvas.lockFocus()
    fill(NSRect(x: 0, y: 0, width: width, height: height), NSColor(calibratedRed: 0.027, green: 0.063, blue: 0.098, alpha: 1))
    fill(NSRect(x: 92, y: 132, width: 8, height: 790), topic.accent); text("REBECCA LI  /  MODULE 07", x: 130, top: 74, size: 20, color: NSColor(calibratedWhite: 0.70, alpha: 1), weight: .medium); text(scene.label, x: 130, top: 126, size: 19, color: topic.accent, weight: .bold); text(scene.title, x: 130, top: 166, size: scene.title.count > 28 ? 48 : 64, color: .white, weight: .bold, width: 1640); drawGraphic(topic, scene)
    fill(NSRect(x: 120, y: 70, width: 1680, height: 4), NSColor(calibratedWhite: 0.18, alpha: 1)); fill(NSRect(x: 120, y: 70, width: CGFloat(index + 1) * 330, height: 4), topic.accent)
    fill(NSRect(x: 120, y: 18, width: 1680, height: 104), NSColor(calibratedRed: 0.02, green: 0.045, blue: 0.07, alpha: 0.98), radius: 16); text(scene.caption, x: 155, top: 1015, size: 23, color: NSColor(calibratedWhite: 0.88, alpha: 1), weight: .medium, width: 1580)
    canvas.unlockFocus(); guard let cgImage = canvas.cgImage(forProposedRect: nil, context: nil, hints: nil) else { return }; let rep = NSBitmapImageRep(cgImage: cgImage); guard let data = rep.representation(using: .png, properties: [:]) else { return }; try? data.write(to: folder.appendingPathComponent(String(format: "scene-%02d.png", index)))
}

for topic in topics { for (index, scene) in topic.scenes.enumerated() { render(topic, scene, index) } }
