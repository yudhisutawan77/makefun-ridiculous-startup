#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second.

Writes a single-sentence startup pitch (max 200 characters) to
/output/entry.txt and validates it against the bounty gate:
UTF-8 text of 1 to 200 characters, not only whitespace.
Exits non-zero if the entry is out of bounds.
"""

import os
import sys

ENTRY = (
    "We certify houses as officially haunted: our mediums verify "
    "your ghost, and Airbnb hosts pay us because a certified haunting "
    "lets them charge 40% more a night."
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def validate(text):
    """Check the entry against the bounty gate. Returns an error string or None."""
    if not isinstance(text, str):
        return "entry is not text"
    if len(text) < 1 or len(text) > MAX_CHARS:
        return "entry is %d characters, must be 1-%d" % (len(text), MAX_CHARS)
    if not text.strip():
        return "entry is only whitespace"
    if "\n" in text or "\r" in text:
        return "entry must be a single line"
    if text.count(".") != 1 or not text.endswith("."):
        return "entry must be exactly one sentence"
    return None


def main():
    error = validate(ENTRY)
    if error is not None:
        print("gate check failed: %s" % error, file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    print("wrote %d characters to %s" % (len(ENTRY), OUTPUT_PATH))
    return 0


if __name__ == "__main__":
    sys.exit(main())
