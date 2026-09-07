import AppKit
import Foundation

let outputRoot = URL(fileURLWithPath: CommandLine.arguments.count > 1 ? CommandLine.arguments[1] : NSTemporaryDirectory(), isDirectory: true)
let width: CGFloat = 1920
let height: CGFloat = 1080

struct Scene { let kind: String; let label: String; let title: String; let caption: String }
struct Topic { let slug: String; let accent: NSColor; let scenes: [Scene] }

let topics = [
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
    default:
        card(NSRect(x: 180, y: 390, width: 450, height: 190), accent: a, label: "EVIDENCE", value: "source card", detail: "available to check", valueSize: 28); arrow(700, 485, 900, 485, a); card(NSRect(x: 970, y: 390, width: 690, height: 190), accent: a, label: "BOUNDARY", value: "answer or abstain", detail: "no source means no guess", valueSize: 30)
    }
}

func render(_ topic: Topic, _ scene: Scene, _ index: Int) {
    let folder = outputRoot.appendingPathComponent(topic.slug, isDirectory: true); try? FileManager.default.createDirectory(at: folder, withIntermediateDirectories: true)
    let canvas = NSImage(size: NSSize(width: width, height: height)); canvas.lockFocus()
    fill(NSRect(x: 0, y: 0, width: width, height: height), NSColor(calibratedRed: 0.027, green: 0.063, blue: 0.098, alpha: 1))
    fill(NSRect(x: 92, y: 132, width: 8, height: 790), topic.accent); text("REBECCA LI  /  MODULE 05", x: 130, top: 74, size: 20, color: NSColor(calibratedWhite: 0.70, alpha: 1), weight: .medium); text(scene.label, x: 130, top: 126, size: 19, color: topic.accent, weight: .bold); text(scene.title, x: 130, top: 166, size: scene.title.count > 28 ? 48 : 64, color: .white, weight: .bold, width: 1640); drawGraphic(topic, scene)
    fill(NSRect(x: 120, y: 70, width: 1680, height: 4), NSColor(calibratedWhite: 0.18, alpha: 1)); fill(NSRect(x: 120, y: 70, width: CGFloat(index + 1) * 330, height: 4), topic.accent)
    fill(NSRect(x: 120, y: 18, width: 1680, height: 104), NSColor(calibratedRed: 0.02, green: 0.045, blue: 0.07, alpha: 0.98), radius: 16); text(scene.caption, x: 155, top: 1015, size: 23, color: NSColor(calibratedWhite: 0.88, alpha: 1), weight: .medium, width: 1580)
    canvas.unlockFocus(); guard let cgImage = canvas.cgImage(forProposedRect: nil, context: nil, hints: nil) else { return }; let rep = NSBitmapImageRep(cgImage: cgImage); guard let data = rep.representation(using: .png, properties: [:]) else { return }; try? data.write(to: folder.appendingPathComponent(String(format: "scene-%02d.png", index)))
}

for topic in topics { for (index, scene) in topic.scenes.enumerated() { render(topic, scene, index) } }
