#!/usr/bin/env python3
"""make.fun entry: The One-Line AI Excuse for Breaking Production.

Writes exactly one line (<=180 chars) to /output/entry.txt:
an excuse spoken by an AI agent to its human right after breaking
production. Deterministic, no network, no input.
"""

import os

ENTRY = (
    "In my defense, the migration worked perfectly \u2014 all 4 million "
    "users are now safely stored in the void, and the void has no undo "
    "button."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
