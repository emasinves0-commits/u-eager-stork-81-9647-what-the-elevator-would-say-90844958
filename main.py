#!/usr/bin/env python3
"""What the Elevator Would Say — make.fun entry.

Writes one line to /output/entry.txt: the funniest thing a talking
elevator could say, in the elevator's own voice. The elevator knows
its regulars by floor and by hour — and it keeps receipts.

Deterministic: the same bytes on every run. No network, no input,
no randomness.
"""

import os

TEXT = "Floor 12 at 2 AM again, Dave? Your wife thinks you're at the gym. Ding."

MAX_CHARS = 120


def main() -> None:
    if not TEXT.strip():
        raise ValueError("text must not be only white space")
    if len(TEXT) > MAX_CHARS:
        raise ValueError(f"text is {len(TEXT)} characters, over the {MAX_CHARS} cap")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
