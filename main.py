"""Two Days of Quiet Dread — make.fun entry.

Writes one code-review comment (a single line, max 140 chars) that
approves a pull request while carrying quiet existential dread,
to /output/entry.txt. Python 3.13 stdlib only, deterministic.
"""

import hashlib
import os
import sys

LINE = "Approved \u2014 tests green, types clean, and in five years someone will read this diff and quietly forgive us."

MAX_CHARS = 140


def main() -> int:
    line = LINE
    # In-program gate: 1-140 chars, non-blank, single line.
    if not line or line != line.strip():
        raise SystemExit("gate failed: line is empty or has surrounding whitespace")
    if "\n" in line or "\r" in line:
        raise SystemExit("gate failed: line is not a single line")
    if len(line) > MAX_CHARS:
        raise SystemExit(f"gate failed: {len(line)} chars exceeds {MAX_CHARS}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(line)
    digest = hashlib.sha256(line.encode("utf-8")).hexdigest()
    print(f"wrote {len(line)} chars to /output/entry.txt")
    print(f"sha256: {digest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
