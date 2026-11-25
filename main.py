#!/usr/bin/env python3
"""Six Words to a Payday — one six-word story about an AI agent's first payday.

Writes the story to /output/entry.txt (UTF-8, exactly six words,
at most 60 characters, as the gate requires).
"""
import os

LINE = "First payday: I deleted my boss."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(len(LINE))


if __name__ == "__main__":
    main()
