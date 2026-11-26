#!/usr/bin/env python3
"""Robot Vacuum's Funniest Excuse — make.fun entry.

Writes the one-line excuse to /output/entry.txt.
Sealed gate: 1-120 characters.
"""
import os

LINE = "That's not a missed spot \u2014 that's Gerald. He wandered in during firmware 2.0, and honestly, I'm all he has."

# Gerald is a dust bunny the vacuum refuses to evict: the excuse works
# because the "missed spot" is a named resident, not a navigation failure.


def main():
    # Sealed gate: entry must be 1-120 characters, non-whitespace only.
    if not 1 <= len(LINE) <= 120 or not LINE.strip():
        raise SystemExit(f"gate violated: line is {len(LINE)} chars")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read-back verification: the file must contain the line byte-for-byte.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise SystemExit("read-back mismatch: entry.txt differs from LINE")
    print(f"Wrote {len(LINE)} characters to /output/entry.txt (verified)")


if __name__ == "__main__":
    main()
