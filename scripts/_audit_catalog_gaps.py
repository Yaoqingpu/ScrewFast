import json, re
from pathlib import Path
from collections import Counter

prod = Path(r"E:\AI\ss-fittings-export\src\content\products\en")
export_titles = {}
export_cats = Counter()
for f in sorted(prod.glob("item-*.md")):
    t = f.read_text(encoding="utf-8")
    fm = t.split("---", 2)[1]
    title = re.search(r"^title:\s*['\"](.+?)['\"]\s*$", fm, re.M).group(1)
    cat = re.search(r"^category:\s*['\"](.+?)['\"]\s*$", fm, re.M).group(1)
    export_titles[title] = {"file": f.name, "category": cat}
    export_cats[cat] += 1

print("EXPORT count", len(export_titles))
print("by cat:")
for k, v in export_cats.most_common():
    print(f"  {k}: {v}")

text = Path(r"E:\AI\ss-fittings-export\scripts\remap_product_images.py").read_text(
    encoding="utf-8"
)
cn_to_en = {}
for m in re.finditer(r'"([^"]+)"\s*:\s*"([^"]+)"', text):
    cn, en = m.group(1), m.group(2)
    if any("\u4e00" <= c <= "\u9fff" for c in cn):
        cn_to_en[cn] = en

print("\nCN_TO_EN", len(cn_to_en))
missing = [(cn, en) for cn, en in cn_to_en.items() if en not in export_titles]
print("Missing product pages vs CN_TO_EN:", len(missing))
for cn, en in missing:
    print(f"  MISSING {cn} => {en}")

extra = [
    t
    for t in export_titles
    if t not in set(cn_to_en.values()) and t != "Investment Cast Round Straight Fitting"
]
print("\nOn site but not in CN_TO_EN:", len(extra))
for t in extra:
    print(" ", t, export_titles[t]["category"])

print("\n=== Catalog series vs site categories ===")
rows = [
    ("波纹管系列", "corrugated-hose", "covered"),
    ("卡套接头系列", "compression-fittings", "covered"),
    ("快拧接头系列", "tube-fittings (混了快插)", "merged/partial"),
    ("宝塔及堵头系列", "pipe-fittings (混了转换/焊接)", "merged/partial"),
    ("转换接头及焊接", "pipe-fittings", "merged"),
    ("球阀及阀组系列", "ball-valves (阀组缺页)", "partial"),
    ("针阀及截止阀", "needle-valves", "covered"),
    ("单向阀及过滤器", "check-valves", "covered"),
    ("BA管/精密管/盘管/管夹", "instrumentation-tubing", "covered"),
    ("不锈钢快插系列", "tube-fittings (应独立)", "merged/partial"),
    ("精铸接头/节流阀/消音器", "cast + pipe-fittings", "split/awkward"),
    ("非标定制系列", "无类目、无SKU", "missing"),
]
for a, b, c in rows:
    print(f"  [{c:14}] {a} -> {b}")

ocr = json.loads(
    Path(r"E:\AI\不锈钢接头采集站\supplier-crops\ocr-products.json").read_text(
        encoding="utf-8"
    )
)
print("\nSpecial OCR:")
for p in ocr:
    zh = p.get("title_zh") or ""
    if any(k in zh for k in ["阀组", "卡芯", "快拧接头", "精铸圆", "非标"]):
        print(" ", zh, "=>", p.get("title_en"), p.get("photo"))

# Count unique EN product types we could have
print("\nUnique EN targets if we had all CN_TO_EN + round straight + ferrule + manifold:")
all_en = set(cn_to_en.values()) | {"Investment Cast Round Straight Fitting", "Ferrule", "Valve Manifold"}
print("  potential", len(all_en), "current", len(export_titles), "gap", len(all_en - set(export_titles)))
for en in sorted(all_en - set(export_titles)):
    print("   need:", en)
