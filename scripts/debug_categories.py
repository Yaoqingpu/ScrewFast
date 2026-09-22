# -*- coding: utf-8 -*-
from pathlib import Path
import re

text = Path("src/data_files/categories.ts").read_text(encoding="utf-8")
slugs = re.findall(r"slug: '([^']+)'", text)
print("ts slugs", slugs)

from collections import Counter

c = Counter()
for f in Path("src/content/products/en").glob("item-*.md"):
    m = re.search(r"category: '([^']+)'", f.read_text(encoding="utf-8"))
    if m:
        c[m.group(1)] += 1
print("md cats", dict(c))
print("in md not ts", set(c) - set(slugs))
print("in ts not md", set(slugs) - set(c))

html = Path("dist/products/index.html").read_text(encoding="utf-8", errors="replace")
print("has Browse category", "Browse category" in html)
print("has grid cards count", html.count("Browse category"))
print("product collection hint", "stainless-steel-compression" in html)
