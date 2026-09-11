---
name: article-technical-writer
description: Turn a topic or prompt into a practical, source-disciplined technical article for Rebecca Li's Articles module.
---

# Article Technical Writer

Canonical skill name: article-technical-writer. The original brief used article.technical_writer as a conceptual ID; the hyphenated name keeps the skill discoverable under the repository's valid naming rules.

## Purpose

Turn one topic, question, or user prompt into a clear technical article that explains what was tried, how the system works, what failed, and what was learned. The default audience is technically curious product, operations, and engineering readers who need a practical explanation rather than generic AI marketing.

The article should reflect this positioning:

Product Management
+
Complex Business Systems
+
Commodity Trading Experience
+
AI, agent, and automation learning
+
Hands-on building
+
Transition toward AI deployment / Forward Deployed Engineering

Do not present Rebecca as an AI researcher or as someone with professional FDE experience that has not been supplied. Write from evidence and label the transition as a direction when appropriate.

## Minimum input

The minimum input is one of:

- a topic
- a question
- a user prompt

Optional input can include:

    {
      "title": "",
      "topic": "",
      "article_type": "",
      "goal": "",
      "audience": "",
      "source_material": [],
      "related_projects": [],
      "related_knowledge": [],
      "need_diagrams": true,
      "need_comparison_table": false
    }

If the topic is enough to begin, do not stop for optional fields. Mark unknown details as TODO and continue with a useful outline.

## Article modes

Choose one primary mode and name it in the plan:

### Build Log

Use for a build such as a local AI agent. Cover motivation, architecture, setup, implementation, problems, result, and lessons learned. Use first person for verified personal experience.

### Comparison

Use for local versus hosted models or coding-agent approaches. Compare only useful dimensions such as execution boundary, privacy, cost, speed, context, quality, setup complexity, control, and use cases. Do not create an unsupported vendor ranking.

### Concept Explanation

Use for a question such as what happens when an agent uses a tool. Start with a simple explanation, then show components, request lifecycle, examples, and misconceptions. Use first person sparingly.

### Experiment / Benchmark

Use for model and hardware experiments. Record environment, model, quantization, memory, speed, context, failures, observations, and practical conclusions. Never invent a measurement.

### Architecture / System Design

Use for a workbench or workflow design. Explain requirements, components, planner, workers, queue, QA, retry, resume, quota handling, and operational boundaries only when they are supported by the supplied material.

## Source and claim discipline

Separate claims into three buckets:

1. Personal experience: write in first person and tie the statement to supplied notes, logs, screenshots, code, or an existing project record.
2. General technical fact: ground the statement in a reliable source when research tools are available. Prefer official documentation and primary sources for implementation details.
3. Unknown: do not guess. Write TODO: verify [detail], or omit the claim.

Do not fabricate dates, versions, hardware specifications, benchmarks, credentials, employers, customer outcomes, or professional experience. Do not turn an idea into a claimed result.

When source material conflicts, preserve the conflict in the QA notes and ask for verification rather than silently choosing one value.

## Standard article structure

Use this structure by default and omit sections that do not help the article:

1. Title
2. Subtitle
3. Metadata: publish date, reading time, tags, category, and status
4. TL;DR
5. Why I Built / Explored This
6. The Simple Explanation
7. System Architecture
8. How It Works
9. My Setup / Environment
10. Implementation / Experiment
11. What Worked
12. What Did Not Work
13. Problems / Limitations
14. Comparison / Alternatives
15. What I Learned
16. When I Would Use This
17. Final Thoughts
18. Related Knowledge
19. Related Projects
20. References / Sources when applicable

An article is not a Knowledge page. Explain the concept only enough to make the experiment or decision understandable, then link to the relevant Knowledge page.

## Article workflow

Run these stages in order:

1. context_collection — collect supplied notes, code, screenshots, links, and known constraints.
2. planning — choose the article mode, audience, question, and evidence boundary.
3. outline — map the article sections and the central argument.
4. drafting — write the explanation with clear separation between experience, fact, and TODO.
5. visual_planning — decide which diagrams, flows, tables, screenshots, and code blocks improve understanding.
6. diagram_generation — create technical visuals with HTML, CSS, SVG, or Mermaid when supported. Prefer reusable site components over decorative AI images.
7. qa — run article.qa, check links, duplication, unsupported claims, structure, and readability.
8. html_generation — create or update the long-form HTML page using the shared Articles CSS and template.
9. index_update — add or update one metadata record in articles/data/articles.json.
10. finalize — set status only after review, preview the page, and report remaining TODOs.

Do not skip context collection when source material is provided. Do not set status to published automatically.

## Visual plan

Create a short Visual Plan before generating visuals:

    Figure 1 — name, purpose, source/evidence, format
    Figure 2 — name, purpose, source/evidence, format
    Table 1 — comparison dimensions and evidence boundary
    Screenshot 1 — what it proves and what it does not prove
    Code 1 — smallest verified example

Choose visuals based on understanding:

- architecture diagram for components and boundaries
- process diagram for a request lifecycle
- comparison table for trade-offs
- timeline for changes across an experiment
- stack diagram for runtime layers
- before / after diagram for architecture changes
- screenshot for observable UI or tool behavior
- code block for a minimal reproducible step

Every figure needs a concise caption. Avoid diagrams that merely decorate the page.

## Metadata contract

Store article metadata in articles/data/articles.json. Each record should follow articles/data/article.schema.json:

- slug: stable lowercase identifier
- title: reader-facing title
- summary: one-sentence description without unsupported results
- category: for example Local AI, AI Agents, Comparison, Experiments, or Architecture
- tags: searchable topic labels
- status: draft, review, or published
- published_at: ISO date or null
- reading_time: a reviewed value or null
- path: article HTML path or null
- cover: optional image or diagram path, otherwise null
- related_knowledge: links to existing Knowledge pages
- related_projects: links to existing project pages or anchors
- need_diagrams: boolean
- need_comparison_table: boolean

Draft and review records are local preview material. Only published records belong on the default Articles index.

## HTML and linking rules

Use articles/templates/article-template.html for new pages. Long-form text should remain approximately 700–850px wide; a diagram may expand wider when the wider canvas improves legibility.

Every article should have:

- a link back to articles.html
- a visible status and metadata line
- readable H1/H2/H3 hierarchy
- TL;DR and a clear conclusion when relevant
- captions for figures
- horizontally scrollable tables and code on small screens
- related Knowledge links for definitions
- related Project links for the thing being explained

Knowledge is the concept layer. Projects are the build layer. Articles are the explanation and evidence layer. Do not copy a Knowledge page into an article.

## Writing style

Prefer:

- clear, practical, first-principles explanations
- concrete system boundaries and request flows
- honest failures, trade-offs, limitations, and unexpected behavior
- short paragraphs and meaningful headings
- wording such as I tried, I expected, I observed, and I still need to verify

Avoid:

- AI is changing the world
- in today's rapidly evolving AI landscape
- revolutionary technology
- generic marketing claims
- unexplained jargon
- presenting an experiment as universal proof

The target voice is: I built this, tested it, and here is what I learned.

## Output

Return or create:

1. an article plan
2. a claim and evidence map
3. a Visual Plan
4. the draft or HTML page
5. metadata update
6. related Knowledge and Project links
7. an Article QA report
8. a list of unresolved TODOs

If required facts are missing, produce a useful draft skeleton rather than filling gaps with plausible details.
