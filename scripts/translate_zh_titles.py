# -*- coding: utf-8 -*-
"""Translate remaining Chinese product titles to English in place."""
from pathlib import Path
import re

PROD = Path(__file__).resolve().parents[1] / "src" / "content" / "products" / "en"

MAP = {
    "SS Fitting — 卡套快拧直通及卡套快拧穿板接头": "Compression / Quick-Screw Straight & Bulkhead Connectors",
    "SS Fitting — 卡套四通接头": "Compression Cross Fitting",
    "SS Fitting — 模锻卡套变径三通接头": "Forged Compression Reducing Tee",
    "SS Fitting — 模锻卡套四通接头": "Forged Compression Cross Fitting",
    "SS Fitting — 快拧弯通接头": "Quick-Screw Elbow Connector",
    "SS Fitting — 快拧三通接头": "Quick-Screw Tee Connector",
    "SS Fitting — 直通快拧仿美球阀": "Straight Quick-Screw Ball Valve",
    "SS Fitting — 三通快拧仿美球阀": "3-Way Quick-Screw Ball Valve",
    "SS Fitting — 迷你球阀": "Mini Ball Valve",
    "SS Fitting — 高压内丝球阀": "High-Pressure Female Ball Valve",
    "SS Fitting — 气源球阀": "Air-Source Ball Valve",
    "SS Fitting — 角式卡套针阀": "Angle Compression Needle Valve",
    "SS Fitting — 模锻卡套针阀": "Forged Compression Needle Valve",
    "SS Fitting — 焊接针阀": "Weld-End Needle Valve",
    "SS Fitting — 快插直通接头": "Push-to-Connect Straight Fitting",
    "SS Fitting — 快插弯通接头": "Push-to-Connect Elbow Fitting",
    "SS Fitting — 快插直通中间接头": "Push-to-Connect Straight Union",
    "SS Fitting — 快插穿板接头": "Push-to-Connect Bulkhead Fitting",
    "SS Fitting — Y型+T型三通接头": "Y-Type and T-Type Tee Fitting",
}

n = 0
for f in PROD.glob("item-*.md"):
    text = f.read_text(encoding="utf-8")
    m = re.search(r"^title: '((?:''|[^'])*)'", text, re.M)
    if not m:
        continue
    old = m.group(1).replace("''", "'")
    if old not in MAP:
        continue
    new = MAP[old]
    text = text.replace(old, new)
    f.write_text(text, encoding="utf-8")
    n += 1
    print(f.name, "->", new)
print("Updated", n)
