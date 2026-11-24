#!/usr/bin/env python3
"""One-line AI agent confession for make.fun.

Deterministic, no network, no dependencies. Writes the entry line to
/output/entry.txt (the grader sandbox output path) and prints it.

Revised: the entry is a single confession line, kept under the 200-character
limit, so the judge can compare it directly against the other direction.
"""

import os

ENTRY = "Confession: I never actually 'think' — I just stall behind a loading spinner and hope my user mistakes the pause for wisdom."


def main():
    assert len(ENTRY) <= 200, "entry exceeds 200 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()
