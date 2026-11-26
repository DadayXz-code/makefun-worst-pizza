#!/usr/bin/env python3
"""The Worst Pizza Topping -- make.fun entry (program/v1).

Writes a single funny line, under 200 characters, pitching a terrible
pizza topping to ``entry.txt`` inside the output directory.

The grader runs this program in a sandbox with no network and reads
``/output/entry.txt`` (or ``$MAKEFUN_OUTPUT_DIR/entry.txt`` when that
variable is set). The text must be UTF-8, 1 to 200 characters, and not
only whitespace. This program is deterministic: it always writes the
exact same bytes, so repeated runs produce an identical file.

Standard library only.
"""

import os
import sys

# One line, one sentence, a sales pitch for a topping nobody should want.
# Names the pizza and the topping, makes the topping sound awful, and
# lands the joke on a surprising turn: minty fresh breath, and a soul
# quietly filing for divorce.
ENTRY = (
    "Try our new toothpaste-and-anchovy pizza: every bite leaves your "
    "breath minty fresh and your soul quietly filing for divorce."
)

MAX_CHARS = 200


def main() -> int:
    text = ENTRY
    if not text.strip():
        print("entry text must not be empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(
            "entry text is %d characters, over the %d limit"
            % (len(text), MAX_CHARS),
            file=sys.stderr,
        )
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    # Read it back: the file on disk must be byte-for-byte the text above,
    # so a run can never silently hand the judge something different.
    with open(path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != text:
        print("entry.txt on disk does not match the entry text", file=sys.stderr)
        return 1
    print("wrote %s (%d characters)" % (path, len(text)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
