# -*- coding: utf-8 -*-
from pathlib import Path
import re, collections

d = Path(__file__).resolve().parents[1] / "src" / "content" / "products" / "en"
intros, descs = [], []
for p in sorted(d.glob("*.md")):
    t = p.read_text(encoding="utf-8")
    m = re.search(r"content: \|\n    (.+?)\n  imgCard", t, re.S)
    if m:
        intros.append(m.group(1).strip())
    dm = re.search(r"^description:\s*'((?:''|[^'])*)'", t, re.M)
    if dm:
        descs.append((p.name, len(dm.group(1).replace("''", "'"))))

firsts = [i.split(".")[0] for i in intros]
dups = [(k, v) for k, v in collections.Counter(firsts).items() if v > 1]
print("products", len(intros))
print("desc len min/max", min(x[1] for x in descs), max(x[1] for x in descs))
print("over160", sum(1 for x in descs if x[1] > 160))
print("dup first sentences", len(dups))
for phrase in [
    "Buyers usually",
    "Pair this SKU",
    "Pressure guidance",
    "construction oriented",
    "Technical buyers use this pattern",
    "catalog cues are",
]:
    print(phrase, sum(1 for i in intros for _ in [1] if phrase in i) + sum(1 for p in d.glob('*.md') if phrase in p.read_text(encoding='utf-8')))
