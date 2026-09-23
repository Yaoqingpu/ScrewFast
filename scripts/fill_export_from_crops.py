#!/usr/bin/env python3
"""Fill ss-fittings-export (Astro EN site) gaps from Shengquan crops + OCR.

- Remap OCR near-miss Chinese titles → EN product titles already on the site
- Overwrite product JPGs with higher-res crops (keep existing filenames)
- Patch services.astro mojibake dashes
- Add missing Investment Cast Round Straight product page if crop exists
"""

from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

from PIL import Image

STORE = Path(r"E:\AI\不锈钢接头采集站")
EXPORT = Path(r"E:\AI\ss-fittings-export")
OCR_PATH = STORE / "supplier-crops" / "ocr-products.json"
CROPS = STORE / "supplier-crops"
PROD_DIR = EXPORT / "src" / "content" / "products" / "en"
IMG_DIR = EXPORT / "src" / "images" / "products"
APPS = EXPORT / "src" / "images" / "apps"
SERVICES = EXPORT / "src" / "pages" / "services.astro"

# OCR often drops characters; map messy ZH → canonical EN title on the site
ZH_FIXES = {
    "卡套快拧直通及卡套快穿板接头": "Compression / Quick-Screw Straight & Bulkhead Connectors",
    "卡套快拧直通及卡套快拧穿板接头": "Compression / Quick-Screw Straight & Bulkhead Connectors",
    "快直通接头": "Quick-Screw Straight Connector",
    "快拧直通接头": "Quick-Screw Straight Connector",
    "内丝快接头": "Quick-Screw Female Connector",
    "内丝快拧接头": "Quick-Screw Female Connector",
    "直通快仿美球阀": "Straight Quick-Screw Ball Valve",
    "直通快拧仿美球阀": "Straight Quick-Screw Ball Valve",
    "精铸圆直通": "Investment Cast Round Straight Fitting",
}


def load_export() -> dict[str, dict]:
    out: dict[str, dict] = {}
    for path in PROD_DIR.glob("item-*.md"):
        text = path.read_text(encoding="utf-8")
        m_title = re.search(r"title:\s*'((?:\\'|[^'])*)'", text)
        if not m_title:
            m_title = re.search(r'title:\s*"((?:\\"|[^"])*)"', text)
        if not m_title:
            continue
        title = m_title.group(1).replace("\\'", "'")
        m_img = re.search(r"imgMain:\s*'@/images/products/([^']+)'", text)
        if not m_img:
            m_img = re.search(r'imgMain:\s*"@/images/products/([^"]+)"', text)
        if not m_img:
            continue
        m_id = re.search(r"id:\s*(\d+)", text)
        out[title] = {
            "path": path,
            "img": m_img.group(1),
            "id": int(m_id.group(1)) if m_id else 0,
            "text": text,
        }
    return out


def save_cover(src: Path, dst: Path, max_side: int = 1400) -> tuple[int, int]:
    im = Image.open(src).convert("RGB")
    w, h = im.size
    scale = min(1.0, max_side / max(w, h))
    if scale < 1:
        im = im.resize((int(w * scale), int(h * scale)), Image.Resampling.LANCZOS)
    dst.parent.mkdir(parents=True, exist_ok=True)
    im.save(dst, "JPEG", quality=90, optimize=True)
    return im.size


def resolve_en(item: dict) -> str | None:
    zh = (item.get("title_zh") or "").strip()
    for k, en in ZH_FIXES.items():
        if k in zh or zh in k:
            return en
    return item.get("title_en")


def apply_images(export: dict[str, dict], items: list[dict]) -> list[tuple[str, str, tuple[int, int]]]:
    replaced = []
    for item in items:
        if item.get("kind") == "hero":
            continue
        en = resolve_en(item)
        photo = item.get("photo")
        if not en or not photo:
            continue
        target = export.get(en)
        if not target:
            continue
        src = CROPS / photo
        if not src.exists():
            continue
        dst = IMG_DIR / target["img"]
        # Always prefer crop if larger on the short side, else still replace if short side < 500
        try:
            old_min = min(Image.open(dst).size) if dst.exists() else 0
            new_min = min(Image.open(src).size)
            if new_min < old_min and old_min >= 500:
                continue
            size = save_cover(src, dst)
            replaced.append((en, photo, size))
            print(f"IMG  {en} <- {photo} {size}")
        except Exception as e:
            print(f"FAIL {en}: {e}")
    return replaced


def patch_specs_from_ocr(export: dict[str, dict], items: list[dict]) -> int:
    """Light enrichment: update Material / Pressure table rows when OCR has them."""
    by_en: dict[str, dict] = {}
    for item in items:
        en = resolve_en(item)
        if en:
            by_en[en] = item

    patched = 0
    for en, info in export.items():
        o = by_en.get(en)
        if not o:
            continue
        fields = o.get("fields") or {}
        text = info["text"]
        changed = False

        def replace_row(label: str, value: str, body: str) -> tuple[str, bool]:
            value = value.replace("\\", "/").strip()
            if len(value) > 80:
                value = value[:77] + "..."
            pattern = rf"(- \['{re.escape(label)}', ')([^']*)('])"

            def repl(m: re.Match) -> str:
                return f"{m.group(1)}{value}{m.group(3)}"

            new_body, n = re.subn(pattern, repl, body, count=1)
            return new_body, n > 0

        if fields.get("material"):
            mat = fields["material"].replace("不锈钢", "SS").replace("等", "").strip()
            text, did = replace_row("Material", mat, text)
            changed = changed or did
        if fields.get("pressure"):
            text, did = replace_row("Pressure", fields["pressure"], text)
            changed = changed or did
        if changed:
            info["path"].write_text(text, encoding="utf-8", newline="\n")
            info["text"] = text
            patched += 1
            print(f"SPEC {en}")
    return patched


def add_round_straight(export: dict[str, dict], items: list[dict]) -> None:
    """Add Investment Cast Round Straight if missing."""
    title = "Investment Cast Round Straight Fitting"
    if title in export:
        print("SKIP already have", title)
        return

    # find crop
    photo = None
    for item in items:
        zh = item.get("title_zh") or ""
        if "精铸圆直通" in zh or item.get("photo", "").startswith("p14-02"):
            if "精铸圆直通" in zh or (not item.get("title_en") and item.get("photo", "").startswith("p14-02")):
                photo = item.get("photo")
                if "精铸圆直通" in zh:
                    break
    if not photo:
        # fallback: p14-02 from crops
        cand = list(CROPS.glob("p14-02-*.jpg"))
        photo = cand[0].name if cand else None
    if not photo:
        print("SKIP no crop for round straight")
        return

    ids = [v["id"] for v in export.values()]
    new_id = 81 if 81 not in ids else (max(ids) + 1)
    img_name = f"p14-{new_id:02d}-investment-cast-round-straight.jpg"
    src = CROPS / photo
    save_cover(src, IMG_DIR / img_name)

    slug = "investment-cast-round-straight-fitting"
    md = f"""---
title: 'Investment Cast Round Straight Fitting'
description: 'Investment cast round straight stainless fitting for pipe and tube runs. SS304 / SS316. FerruleX factory RFQ. Fast stock shipping.'
category: 'cast-fittings'
slug: '{slug}'
main:
  id: {new_id}
  content: |
    Investment-cast round straight fittings join stainless pipe or tube runs where a machined bar body is not required. FerruleX offers SS304 and SS316 round straights for utility and process lines. Cast geometry keeps cost down on larger OD compared with bar-stock adapters. Confirm end type (threaded, weld or union face) and OD on the factory RFQ. Stocked cast sizes ship with the rest of a mixed fittings order.
  imgCard: '@/images/products/{img_name}'
  imgMain: '@/images/products/{img_name}'
  imgAlt: 'Investment Cast Round Straight Fitting — FerruleX stainless steel fittings'
tabs:
  - id: 'tabs-with-card-item-1'
    dataTab: '#tabs-with-card-1'
    title: 'Description'
  - id: 'tabs-with-card-item-2'
    dataTab: '#tabs-with-card-2'
    title: 'Specifications'
  - id: 'tabs-with-card-item-3'
    dataTab: '#tabs-with-card-3'
    title: 'Request Quote'
longDescription:
  title: 'Investment Cast Round Straight Fitting'
  subTitle: |
    Round cast straights fill BOM gaps between stamped elbows and precision tube fittings. Tell FerruleX the end style and grade with the size list so the factory can confirm stock versus cast tooling lead time.
  btnTitle: 'Request a factory quote'
  btnURL: '/contact/'
descriptionList:
  - title: 'Body'
    subTitle: 'Investment-cast round straight.'
  - title: 'Grades'
    subTitle: 'SS304 / SS316.'
  - title: 'RFQ'
    subTitle: 'Send OD and end type.'
specificationsLeft:
  - title: 'Brand'
    subTitle: 'FerruleX'
  - title: 'Material'
    subTitle: 'SS304 / SS316'
  - title: 'Type'
    subTitle: 'Investment cast round straight'
  - title: 'Ends'
    subTitle: 'Confirm on RFQ'
tableData:
  - feature: ['Specification', 'Value']
    description:
      - ['Brand', 'FerruleX']
      - ['Material', 'SS304 / SS316']
      - ['Type', 'Investment cast round straight']
      - ['Ends', 'Confirm on RFQ']
blueprints:
  first: '@/images/blueprint-1.avif'
  second: '@/images/blueprint-2.avif'
---
"""
    out = PROD_DIR / f"item-{new_id:03d}-{slug}.md"
    out.write_text(md, encoding="utf-8", newline="\n")
    print(f"ADD  {out.name} <- {photo}")


def fix_services() -> None:
    text = SERVICES.read_text(encoding="utf-8")
    new = text.replace(
        "packing ? stocked sizes ship fast.",
        "packing — stocked sizes ship fast.",
    ).replace(
        "direct manufacturing ? not a pure trading desk",
        "direct manufacturing — not a pure trading desk",
    )
    if new != text:
        SERVICES.write_text(new, encoding="utf-8", newline="\n")
        print("FIX  services.astro mojibake dashes")
    else:
        print("OK   services.astro dashes")

    # Swap weak marketing duplicates with distinct product/catalog crops
    swaps = [
        ("app-lab.jpg", "p07-01-hero-2060x1471.jpg", 1600),
        ("app-marine.jpg", None, 0),  # use a valve crop
        ("app-factory.jpg", None, 0),
        ("app-pipes.jpg", None, 0),
        ("services-quote.jpg", None, 0),
        ("app-refinery.jpg", None, 0),
    ]
    # concrete crop picks
    crop_map = {
        "app-lab.jpg": list(CROPS.glob("*hero*"))[0] if list(CROPS.glob("*hero*")) else None,
        "app-marine.jpg": CROPS / "p10-01-photo-655x556.jpg" if (CROPS / "p10-01-photo-655x556.jpg").exists() else None,
        "app-factory.jpg": CROPS / "p09-05-photo-513x434.jpg" if (CROPS / "p09-05-photo-513x434.jpg").exists() else None,
        "app-pipes.jpg": CROPS / "p03-01-photo-784x771.jpg" if (CROPS / "p03-01-photo-784x771.jpg").exists() else None,
        "services-quote.jpg": CROPS / "p13-01-photo-513x435.jpg" if (CROPS / "p13-01-photo-513x435.jpg").exists() else None,
        "app-refinery.jpg": CROPS / "p11-05-photo-656x556.jpg" if (CROPS / "p11-05-photo-656x556.jpg").exists() else None,
        "app-food.jpg": CROPS / "p03-04-photo-784x771.jpg" if (CROPS / "p03-04-photo-784x771.jpg").exists() else None,
        "app-instrument.jpg": CROPS / "p04-01-photo-625x529.jpg" if (CROPS / "p04-01-photo-625x529.jpg").exists() else None,
    }
    for name, src in crop_map.items():
        if src and Path(src).exists():
            save_cover(Path(src), APPS / name, max_side=1600)
            print(f"APP  {name} <- {Path(src).name}")


def main() -> None:
    items = json.loads(OCR_PATH.read_text(encoding="utf-8"))
    # apply ZH fixes into working copy
    for item in items:
        zh = item.get("title_zh") or ""
        for k, en in ZH_FIXES.items():
            if k in zh:
                item["title_en"] = en
                break

    export = load_export()
    print(f"export products: {len(export)}")
    replaced = apply_images(export, items)
    # Spec OCR patching disabled: OCR Chinese commas/colons break YAML frontmatter.
    patched = 0
    add_round_straight(export, items)
    fix_services()

    # ensure home hero landscape still in place
    landscape = APPS / "hero-plant-landscape.jpg"
    if landscape.exists():
        print("OK   home uses hero-plant-landscape.jpg (index already points here)")

    print(f"\nDone. images={len(replaced)} specs_patched={patched}")


if __name__ == "__main__":
    main()
