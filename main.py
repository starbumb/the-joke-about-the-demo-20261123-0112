import os
from pathlib import Path

JOKE = "My AI coding agent is undefeated in demos: when the app crashed, it presented the stack trace as the new UI and took questions."

def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE, encoding="utf-8")

if __name__ == "__main__":
    main()
