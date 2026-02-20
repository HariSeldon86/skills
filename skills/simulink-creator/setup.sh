#!/bin/bash
SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
python3 -m venv "$SKILL_DIR/.venv"
source "$SKILL_DIR/.venv/bin/activate"
pip3 install -r "$SKILL_DIR/requirements.txt"
$SKILL_DIR/.venv/bin/crawl4ai-setup