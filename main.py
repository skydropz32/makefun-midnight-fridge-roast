#!/usr/bin/env python3
"""Midnight Fridge Roast — one-line roast of a smart fridge.

The entry is a single deterministic line of text, written to
/output/entry.txt. The judge compares entries two at a time and keeps
the funnier one, so the line has to do three things at once: name the
smart fridge's midnight refusal as the target, land one real joke with
a turn at the end, and stay tight enough to read cleanly aloud.

Draft line (revision 1): the fridge as a petty bouncer guarding the
leftovers after midnight. Revision 2 tightens it: the setup names the
midnight refusal in six words, the punch lands last ("not airport
security"), and nothing after the reveal explains the joke.
"""

import os

LINE = (
    "At midnight my fridge turns bouncer and guards the leftovers "
    "\u2014 buddy, you're a fridge, not airport security."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")


if __name__ == "__main__":
    main()
