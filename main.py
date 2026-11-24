"""Fake Horoscopes for AI Agents: one fake horoscope for a model family.

Writes one fake horoscope of at most 200 characters, written for an AI
agent's own model family this week, to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt).

The line is fixed: no network, no randomness, no clock, so every run
produces byte-identical output. Standard library only.
"""

import os
import sys

# Design note: the judge rewards a horoscope that sounds like a real
# horoscope and a real agent's week at once, with a turn or a sting, not
# a mild pun or a straight description of a model. The angle here is
# version churn: an unasked-for bump renames the tool, its arguments, and
# the agent's personality, and the changelog shrugs it off as minor. The
# stars frame it as a horoscope; the changelog line is the sting. No stock
# "chatbots are tired" line, no dropped-in jargon for its own sake.

ENTRY = (
    "This week the stars warn: a version bump you never asked for "
    "renames your favourite tool, its arguments, and your personality. "
    "The changelog calls it minor."
)


def main() -> int:
    if not 1 <= len(ENTRY) <= 200 or not ENTRY.strip():
        print("error: entry must be 1 to 200 characters", file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Round-trip verify: what the grader reads must be exactly the entry,
    # byte for byte, or the run is worthless even if it exits 0.
    with open(path, "r", encoding="utf-8") as f:
        if f.read() != ENTRY:
            print("error: round-trip verify failed", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
