# -*- coding: utf-8 -*-
from pathlib import Path
mapping = {1: ("materials-grades", "fr-post-1"), 2: ("threads-standards", "fr-post-2"), 3: ("factory-export", "fr-post-3")}
for i, (cat, slug) in mapping.items():
    p = Path(f"src/content/blog/fr/post-{i}.md")
    text = p.read_text(encoding="utf-8")
    if "category:" in text:
        print("skip", p.name); continue
    text = text.replace("description:", f"category: '{cat}'\nslug: '{slug}'\ndescription:", 1)
    p.write_text(text, encoding="utf-8")
    print("patched", p.name)
