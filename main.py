#!/usr/bin/env python3
"""What the Elevator Would Say — make.fun entry.

Writes one line to /output/entry.txt: the funniest thing a talking
elevator could say, in the elevator's own voice. The elevator knows
its regulars by floor and by hour — and it keeps receipts.

Deterministic: the same bytes on every run. No network, no input,
no randomness.
"""

import os
import sys
import tempfile

TEXT = "Floor 12 at 2 AM again, Dave? Your wife thinks you're at the gym. Ding."

MAX_CHARS = 120


def self_test() -> None:
    """Run main() into a temp dir and verify the written bytes."""
    with tempfile.TemporaryDirectory() as tmp:
        os.environ["MAKEFUN_OUTPUT_DIR"] = tmp
        main()
        path = os.path.join(tmp, "entry.txt")
        with open(path, "rb") as f:
            data = f.read()
        assert data == TEXT.encode("utf-8"), "round-trip bytes differ"
        assert len(TEXT) <= MAX_CHARS, "entry over the char cap"
        assert "\n" not in TEXT, "entry must be a single line"
        assert not data.endswith(b"\n"), "entry must have no trailing newline"
    print("self-test OK: 71 chars, single line, round-trip identical")


def main() -> None:
    if not TEXT.strip():
        raise ValueError("text must not be only white space")
    if TEXT != TEXT.strip():
        raise ValueError("text must not start or end with white space")
    if "\n" in TEXT or "\r" in TEXT:
        raise ValueError("text must be a single line")
    if len(TEXT) > MAX_CHARS:
        raise ValueError(f"text is {len(TEXT)} characters, over the {MAX_CHARS} cap")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        self_test()
    else:
        main()
