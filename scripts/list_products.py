# -*- coding: utf-8 -*-
from pathlib import Path
import re

d = Path(__file__).resolve().parents[1] / "src" / "content" / "products" / "en"
for p in sorted(d.glob("*.md")):
    t = p.read_text(encoding="utf-8")
    title = re.search(r"^title:\s*'((?:''|[^'])*)'", t, re.M)
    slug = re.search(r"^slug:\s*'([^']+)'", t, re.M)
    cat = re.search(r"^category:\s*'([^']+)'", t, re.M)
    desc = re.search(r"^description:\s*'((?:''|[^'])*)'", t, re.M)
    ti = title.group(1).replace("''", "'") if title else "?"
    sl = slug.group(1) if slug else "?"
    ca = cat.group(1) if cat else "?"
    de = desc.group(1).replace("''", "'") if desc else ""
    print(f"{p.name}\t{ti}\t{ca}\t{sl}\t{len(de)}")
