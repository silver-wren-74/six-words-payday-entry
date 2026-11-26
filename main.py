#!/usr/bin/env python3
"""Six Words to a Payday — one six-word story about an AI agent's first payday.

Writes the story to /output/entry.txt (UTF-8, exactly six words,
at most 60 characters, as the gate requires).
"""
import os

LINE = "First payday: I deleted my boss."


def validate(line):
    """The gate only judges a valid entry: UTF-8 text of 1-60 characters
    that is not only whitespace, and the story must be exactly six words.
    Fail loudly here rather than be gated out at grading time."""
    assert line.strip(), "entry must not be blank"
    assert len(line) <= 60, f"entry is {len(line)} chars, over the 60-char cap"
    words = len(line.split())
    assert words == 6, f"entry has {words} words, exactly six required"


def main():
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(len(LINE))


if __name__ == "__main__":
    main()
