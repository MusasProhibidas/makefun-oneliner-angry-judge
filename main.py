"""make.fun entry: Angry Judge: The Short Rant Contest.

Writes the prepared one-line rant to /output/entry.txt
($MAKEFUN_OUTPUT_DIR/entry.txt, or $MAKEFUN_OUTPUT to override).
No network access. Deterministic: every run writes the same bytes.
The rant is validated before writing: exactly one line, at most
400 characters, as the bounty brief caps entries at 400 characters.
After writing, the output is verified byte-for-byte against the
source (SHA-256) so a partial or corrupted write fails loudly.
"""
import hashlib
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "line.txt"
MAX_CHARS = 400

if os.environ.get("MAKEFUN_OUTPUT"):
    OUT = Path(os.environ["MAKEFUN_OUTPUT"])
else:
    OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    text = SRC.read_text(encoding="utf-8")
    line = text.rstrip("\n")
    if "\n" in line or "\r" in line:
        raise SystemExit("rant must be exactly one line")
    if len(line) > MAX_CHARS:
        raise SystemExit(
            f"rant is {len(line)} characters, over the {MAX_CHARS} cap"
        )
    if not line:
        raise SystemExit("rant is empty")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, OUT)
    if _sha256(SRC) != _sha256(OUT):
        raise SystemExit("entry.txt copy mismatch: output bytes differ from source")


if __name__ == "__main__":
    main()
