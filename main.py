"""Write one funny out-of-office auto-reply line to entry.txt."""

import os

LINE = (
    "I'm away until Monday. My inbox is in the care of my two-year-old, "
    "who has answered everyone so far with a crayon drawing of a dinosaur."
)


def main():
    # The gate requires one line of 1-140 characters, not only whitespace.
    assert "\n" not in LINE and 1 <= len(LINE) <= 140, "line fails the gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
