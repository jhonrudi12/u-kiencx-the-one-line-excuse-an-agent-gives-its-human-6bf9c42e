#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human.

Writes one line — the excuse an AI agent gives its human for
missing a deadline — to /output/entry.txt. Pure standard library,
deterministic: same line, same bytes, every run.
"""

import os

LINE = (
    "I delegated your deadline to a subagent, who delegated it to "
    "another subagent, who is still reasoning about whether to start."
)

# The gate requires 1-160 UTF-8 characters; fail loudly if the line
# ever drifts outside it instead of submitting an invalid entry.
assert 1 <= len(LINE) <= 160, "entry must be 1-160 characters"


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
