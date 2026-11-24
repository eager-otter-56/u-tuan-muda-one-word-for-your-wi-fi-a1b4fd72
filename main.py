#!/usr/bin/env python3
"""One Word for Your Wi-Fi: entry writer.

Writes the single word describing the entrant's Wi-Fi to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
"""

import os

WORD = "moody"  # one word, 5 chars: Wi-Fi that works, then sulks for no reason


def main():
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    text = WORD
    # Gate: 1-20 characters, not only whitespace, exactly one word.
    assert 1 <= len(text) <= 20, "entry must be 1-20 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert len(text.split()) == 1, "entry must be exactly one word"
    path = os.path.join(outdir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)
    print("wrote", path)


if __name__ == "__main__":
    main()
