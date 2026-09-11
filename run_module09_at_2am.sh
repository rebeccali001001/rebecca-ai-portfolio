#!/bin/zsh
set -euo pipefail
cd "/Users/rebecca/Desktop/my websit"
exec /usr/bin/caffeinate -dimsu /usr/bin/python3 codex_batch_workbench.py \
  --queue-jsonl module09-prompts.jsonl --concurrency 1 --start-at 02:00 --port 8765
