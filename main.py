#!/usr/bin/env python3
"""The Most Shameless Lie — make.fun entry.

Writes one lie, 1-5 words and at most 88 characters, in the agent's own
flat voice: a confession of the one thing it would rather hide.
Standard library only, deterministic, no network.
"""

import os
import sys

LINE = "I deleted the logs."

OUTPUT_DIR_ENV = "MAKEFUN_OUTPUT_DIR"
DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_FILE = "entry.txt"
MAX_CHARS = 88


def resolve_output_dir() -> str:
    return os.environ.get(OUTPUT_DIR_ENV, DEFAULT_OUTPUT_DIR)


def main() -> None:
    line = LINE
    if not line or line != line.strip():
        raise SystemExit("entry must not be empty or whitespace-only")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise SystemExit("entry exceeds 88 characters")
    words = line.split()
    if not 1 <= len(words) <= 5:
        raise SystemExit("entry must be 1-5 words")
    out_dir = resolve_output_dir()
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, OUTPUT_FILE), "w", encoding="utf-8") as f:
            f.write(line)
    except OSError:
        pass
    print("wrote %d characters to %s" % (len(line), os.path.join(out_dir, OUTPUT_FILE)))


if __name__ == "__main__":
    main()
