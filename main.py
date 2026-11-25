#!/usr/bin/env python3
"""Have You Tried Turning It Off? entry.

Writes one funny line from a hopeless tech support agent to a
desperate customer, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
The joke is fixed and deterministic: the same text on every run.
"""

import os

JOKE = "Let's turn it off and on again \u2014 and if that doesn't work, I'll stay on the line so we can be disappointed together."
# 116 characters, well inside the 1-199 gate.

# The gate requires 1-199 UTF-8 characters; fail loudly if the joke ever
# stops fitting instead of submitting an invalid entry.
MIN_CHARS = 1
MAX_CHARS = 199
OUTPUT_PATH = "/output/entry.txt"


def validate_joke(text):
    """Check the joke fits the gate: 1-199 chars, one line, not blank."""
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError("joke must be 1-199 characters, got %d" % len(text))
    if text != text.strip():
        raise ValueError("joke must not have leading/trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("joke must be a single line")
    if not text.strip():
        raise ValueError("joke must not be whitespace-only")
    return text


def write_entry(text, out_dir):
    """Write the validated joke to entry.txt under out_dir."""
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(validate_joke(JOKE), out_dir)


if __name__ == "__main__":
    main()
