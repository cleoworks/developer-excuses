#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses — entry program.

Writes a single line (the excuse a developer gives when code breaks in
production) to <MAKEFUN_OUTPUT_DIR>/entry.txt (default /output).
The line is 108 characters, one line, no trailing newline. Deterministic,
stdlib only, no network, no input: the line is the entry.
"""

import os
import sys

LINE = "It worked for a year because we had one user — today we got a second one, and they clicked at the same time."


def main() -> int:
    text = LINE
    # Gate check: 1-200 characters, not whitespace-only.
    if not (1 <= len(text) <= 200) or not text.strip():
        print(f"entry invalid: {len(text)} characters", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read back: the file must hold exactly the excuse, nothing else.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != text:
        print("entry mismatch after write", file=sys.stderr)
        return 1
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
