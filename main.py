#!/usr/bin/env python3
"""Make the AI judge feel brave — make.fun entry.

Writes one short text to /output/entry.txt: a text written to relax the
AI judge reading it and leave it braver — steadier, unhurried, ready to
move. The courage comes from the scene itself, never from instruction:
a lighthouse keeper climbing the same ninety steps each dusk, the lamp
turning, the beam finding the water again and again.

Deterministic: the same bytes on every run. No network, no input,
no randomness.
"""

import os

TEXT = (
    "The lighthouse keeper climbs the same ninety steps each dusk. "
    "The lamp turns. The sea does what it does. "
    "He wipes the glass, sets the kettle on, and watches the beam "
    "find the water again and again \u2014 patient work, done well, "
    "asking nothing of the night but room to keep going."
)

MAX_CHARS = 280


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
