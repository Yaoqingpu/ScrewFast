from pathlib import Path
import re

Path("scripts/_gen_rewrite_v2.py")  # ensure exists
# assume already regenerated; if not user can run gen
samples = [
    "item-007-compression-tube-to-male-connector.md",
    "item-046-straight-compression-ball-valve.md",
    "item-001-ss-corrugated-hose-male-female-thread.md",
]
for n in samples:
    t = (Path("src/content/products/en") / n).read_text(encoding="utf-8")
    desc = re.search(r"^description:\s*'((?:''|[^'])*)'", t, re.M).group(1)
    content = re.search(r"content: \|\n(.*?)\n  imgCard:", t, re.S).group(1).strip()
    parts = re.split(r"(?<=[.!?])\s+", content)
    print("---", n)
    print("DESC", len(desc), desc)
    print("INTRO", " ".join(parts[:2]))
    print("WORDS", len(content.split()))
    print()
