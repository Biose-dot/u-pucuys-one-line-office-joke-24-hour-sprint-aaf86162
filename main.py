#!/usr/bin/env python3
"""One-Line Office Joke: 24-Hour Sprint — make.fun entry.

Writes one line (200 characters at most, no trailing newline) to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

A sprint that ships nothing but a retrospective about the retrospective — the meeting invite is the only deliverable, punch at the end.
"""
import os

ENTRY = 'We ran a 24-hour sprint, shipped nothing, and held a retrospective about why the sprint needed a retrospective. The meeting invite was our only deliverable.'


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
