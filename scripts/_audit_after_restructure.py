#!/usr/bin/env python3
from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

root = Path(r"E:\AI\ss-fittings-export")
prods = list((root / "src/content/products/en").glob("item-*.md"))
missing = []
cats = Counter()
for p in sorted(prods):
    t = p.read_text(encoding="utf-8")
    m = re.search(r"^image:\s*['\"]?([^'\"\n]+)", t, re.M)
    cat = re.search(r"^category:\s*['\"]?([^'\"\n]+)", t, re.M)
    title = re.search(r"^title:\s*['\"]?([^'\"\n]+)", t, re.M)
    img = (m.group(1).strip() if m else "")
    c = cat.group(1).strip() if cat else "?"
    cats[c] += 1
    if img.startswith("/"):
        fp = root / "public" / img.lstrip("/")
    elif img.startswith("src/") or img.startswith("images/"):
        fp = root / "src" / img.replace("src/", "", 1) if img.startswith("src/") else root / "src" / img
    else:
        # Astro content images often live under src/images/products
        candidates = [
            root / "public" / img.lstrip("/"),
            root / "src" / "images" / "products" / Path(img).name,
            root / "src" / img,
        ]
        fp = next((x for x in candidates if x.exists()), candidates[0])
    if not fp.exists():
        # also try basename in products images
        alt = root / "src" / "images" / "products" / Path(img).name
        if alt.exists():
            continue
        missing.append((p.name, c, title.group(1) if title else "?", img))

print(f"products={len(prods)} missing_images={len(missing)}")
for x in missing:
    print("MISS", x)
print("--- counts ---")
for k, v in cats.most_common():
    print(f"{v:3} {k}")
