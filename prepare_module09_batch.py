#!/usr/bin/env python3
"""Extract the 22 independent Module 09 prompts into a JSONL queue."""
from pathlib import Path
import json, re

source = Path('/Users/rebecca/.codex/attachments/7ece5f99-f7ba-48f7-932a-1ce96df45675/pasted-text.txt')
out = Path(__file__).parent / 'module09-prompts.jsonl'
blocks = re.findall(r'```text\n(.*?)\n```', source.read_text(encoding='utf-8'), re.S)
if len(blocks) != 22:
    raise SystemExit(f'Expected 22 prompts, found {len(blocks)}')
rows = []
for i, prompt in enumerate(blocks, 1):
    m = re.search(r'(?:Topic|Topic：)\s*\n([^\n]+)', prompt)
    topic = m.group(1).strip() if m else f'Module 09 Topic {i:02d}'
    rows.append({'id': f'09-{i:02d}', 'topic': topic, 'prompt': prompt})
out.write_text('\n'.join(json.dumps(row, ensure_ascii=False) for row in rows) + '\n', encoding='utf-8')
print(f'Wrote {len(rows)} prompts to {out}')
