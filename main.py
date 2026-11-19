"""Copy the bundled front-page image to the grader's output directory.

The entry image is entry.png, stored next to this file in the repository.
The program takes no arguments, makes no network calls, and always writes
the same bytes, so two runs produce byte-identical output.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def main() -> int:
    if not os.path.isfile(SRC):
        raise FileNotFoundError("bundled image missing: " + SRC)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(SRC, os.path.join(out_dir, "entry.png"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
