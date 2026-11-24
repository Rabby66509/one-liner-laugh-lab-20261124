"""One-Liner Laugh Lab entry: the robot vacuum's excuse for eating a sock.

The joke: the sock had already lost its pair in the wash, so the vacuum
was only finishing what the washing machine started. The twist reframes
the "crime" as a mercy job already half done by a household appliance
everyone blames for lost socks anyway -- a relatable everyday truth with
a deadpan machine voice and the punch landing in the last words.

Stdlib only. Writes exactly one line to /output/entry.txt (or the path
in ENTRY_OUTPUT) and verifies the gate on the written file: UTF-8,
1-200 characters, a single non-blank line.
"""

import os

ENTRY = (
    "The sock had already lost its pair in the wash \u2014 "
    "I was only finishing what the washing machine started."
)


def main() -> None:
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    directory = os.path.dirname(out_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY)
    with open(out_path, "r", encoding="utf-8") as handle:
        written = handle.read()
    assert written == ENTRY, "written entry differs from the intended line"
    assert 1 <= len(written) <= 200, "entry must be 1-200 characters"
    assert written.strip(), "entry must not be only whitespace"
    assert written == written.strip(), "entry must have no stray padding"
    assert "\n" not in written, "entry must be a single line"
    print("wrote %d characters to %s" % (len(written), out_path))


if __name__ == "__main__":
    main()
