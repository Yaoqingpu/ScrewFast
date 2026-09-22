# -*- coding: utf-8 -*-
from pathlib import Path
import re

p = Path(r"E:\AI\ss-fittings-export\src\content\products\en")
files = sorted(p.glob("item-*.md"))
print("count", len(files))
zh = []
all_titles = []
for f in files:
    t = re.search(r"title: '((?:''|[^'])*)'", f.read_text(encoding="utf-8"))
    if not t:
        continue
    title = t.group(1).replace("''", "'")
    all_titles.append(title)
    if re.search(r"[\u4e00-\u9fff]", title):
        zh.append(title)
print("Chinese titles:", len(zh))
for x in zh:
    print(x)
print("--- first 8 ---")
for x in all_titles[:8]:
    print(x)
