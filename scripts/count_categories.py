# -*- coding: utf-8 -*-
from pathlib import Path
import re
from collections import Counter

c = Counter()
for f in Path("src/content/products/en").glob("item-*.md"):
    t = f.read_text(encoding="utf-8")
    m = re.search(r"category: '([^']+)'", t)
    c[m.group(1) if m else "NONE"] += 1
print(dict(c))
print("total", sum(c.values()))
