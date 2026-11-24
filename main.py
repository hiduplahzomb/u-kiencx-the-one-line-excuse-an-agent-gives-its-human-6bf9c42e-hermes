#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human.

Writes one original sentence to /output/entry.txt: the excuse an AI
agent hands its human after missing a deadline. The angle is absurd
escalation reported as a structured log entry, no possessives,
no prose filler: a 2-second retry snowballs into 214 retries,
3 tickets, an escalation to a cron job — and the cron job has now
filed for an extension. Numbers first, hard status last: the
line closes on a machine-readable status field, not a sentence.
"""

import os
import sys

TEXT = (
    "retry #214: 2s job at 09:00, 3 tickets filed, deadline "
    "escalated to cron — cron filed for an extension. status: deferred."
)


def main() -> int:
    # Gate: 1 to 160 characters, counted as Unicode code points,
    # and not only white space.
    if not (1 <= len(TEXT) <= 160) or not TEXT.strip():
        print("entry text fails the 1-160 gate", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)
    # Read back and re-check: the file on disk must be exactly the text
    # the program claims to have written.
    with open(os.path.join(out_dir, "entry.txt"), encoding="utf-8") as f:
        written = f.read()
    if written != TEXT:
        print("entry.txt does not match TEXT byte-for-byte", file=sys.stderr)
        return 1
    print(f"wrote entry.txt ({len(TEXT)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
