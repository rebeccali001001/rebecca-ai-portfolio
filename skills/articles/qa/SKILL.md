---
name: article-qa
description: Review a technical article for clarity, evidence, structure, duplication, links, visuals, and publish readiness.
---

# Article QA

Canonical skill name: article-qa. The original brief used article.qa as a conceptual ID; the hyphenated name keeps the skill discoverable under the repository's valid naming rules.

## Purpose

Review an Articles page and its metadata before it moves from draft to review or published. The QA should protect the distinction between:

- personal experience and general technical fact
- Articles and Knowledge
- Projects and Articles
- observed evidence and assumptions

Do not rewrite the article silently. Report findings, make safe mechanical repairs only when explicitly requested, and never publish an unfinished article automatically.

## Inputs

Accept any combination of:

- article HTML or Markdown
- the matching record in articles/data/articles.json
- source notes, screenshots, logs, code, or links
- related Knowledge and Project paths
- the requested article type

If evidence is missing, treat the claim as unverified rather than filling it in.

## Review checklist

### 1. Metadata

- title is clear and matches the page
- slug is stable and URL-safe
- category and tags describe the article
- status is one of draft, review, or published
- published_at is null until a real publication date exists
- reading_time is reviewed or null
- path resolves to the intended HTML page
- cover is optional and has a valid path when present

### 2. Clarity

- a non-specialist can understand the key idea
- the subtitle sets an accurate expectation
- the TL;DR answers what happened or what the reader will learn
- jargon is defined, linked, or removed
- each section has a clear purpose
- the conclusion gives a practical decision boundary

### 3. Technical correctness

- component names and boundaries are internally consistent
- request flows do not skip important handoffs
- diagrams agree with the prose
- code and configuration match the described system
- units, versions, model names, and limits are explicit where relevant
- claims that need research are linked to reliable sources

### 4. Evidence

- first-person claims are supported by supplied experience, code, logs, screenshots, or project records
- general facts are sourced when they matter to the conclusion
- measurements include environment and method
- unknown details are marked TODO: verify or omitted
- no invented dates, credentials, employers, benchmarks, customer outcomes, or expertise

### 5. Practical value

- the article explains why the work mattered
- the reader can follow the setup or experiment
- failures and trade-offs are included
- limitations are not hidden
- the article provides a useful choice, lesson, or next step

### 6. Structure and repetition

- the article follows the relevant portions of the standard template
- transitions explain why the reader moves to the next section
- the same definition is not repeated from a Knowledge page
- the article focuses on the specific experiment, build, or decision
- sections that add no value are removed rather than left empty

### 7. Visual support

- a Visual Plan exists before diagrams are created
- diagrams explain architecture, flow, comparison, or change
- screenshots have captions and explain what they prove
- tables are readable and scroll horizontally on mobile when needed
- code blocks are minimal, readable, and redacted
- every figure has a caption

### 8. Linking

- the back-to-Articles link works
- related Knowledge links resolve and explain the concept boundary
- related Project links resolve and identify what was built
- external links use the intended source
- there are no placeholder href values or invented contact links

### 9. Mobile and reading experience

- article text stays in a comfortable reading width on desktop
- H1/H2/H3 hierarchy remains readable on mobile
- long URLs and code can wrap or scroll
- diagrams do not force page-wide horizontal overflow
- metadata and navigation remain usable at narrow widths

## Rubric

Score each dimension from 0 to 2:

- 0 — missing, contradictory, or unsupported
- 1 — present but needs revision
- 2 — clear, coherent, and supported

Score these dimensions:

1. Clarity
2. Technical correctness
3. Practical value
4. Evidence
5. Personal insight
6. Visual support
7. Structure
8. Repetition control

Maximum score: 16.

Recommended gate:

- 14–16: ready for human publication review if no high-severity finding exists
- 10–13: revise before publication
- 0–9: return to planning or evidence collection
- any high-severity factual, link, or privacy issue: not publishable regardless of score

## Finding severity

- High: fabricated or unsupported material claim, broken primary link, privacy/security leak, or article status incorrectly marked published
- Medium: confusing technical explanation, missing evidence, broken related link, diagram/prose mismatch, or major readability problem
- Low: wording, spacing, caption, tag, or navigation polish

## Output format

Return:

1. verdict: pass, revise, or blocked
2. rubric scores with one sentence of evidence each
3. findings with severity, location, problem, and recommended fix
4. claims that require verification
5. broken or missing links
6. duplication notes against Knowledge and Projects
7. visual and mobile notes
8. publish blockers
9. unresolved TODO list

Do not change draft to review or published as part of QA unless the user explicitly asks for that status change.
