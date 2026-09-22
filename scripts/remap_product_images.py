# -*- coding: utf-8 -*-
"""Remap catalog photos using markdown order; skip guide/diagram sections."""
from __future__ import annotations

import re
import shutil
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
MD = ROOT / "mineru-out" / "extracted" / "markdown-utf8.md"
EXTRACT = ROOT / "mineru-out" / "extracted"
PROD_DIR = ROOT / "src" / "content" / "products" / "en"
IMG_DST = ROOT / "src" / "images" / "products"
NEED_FILE = ROOT / "scripts" / "product-images-need-you.txt"

CN_TO_EN = {
    "不锈钢波纹管【内丝外丝】": "SS Corrugated Hose — Male/Female Thread",
    "不锈钢法兰波纹管": "SS Flanged Corrugated Hose",
    "不锈钢法兰补偿器": "SS Flanged Expansion Joint",
    "不锈钢卡盘波纹管": "SS Tri-Clamp Corrugated Hose",
    "不锈钢快速接头波纹管": "SS Quick-Coupling Corrugated Hose",
    "不锈钢KF柔性真空管波纹管": "SS KF Flexible Vacuum Corrugated Hose",
    "卡套直通终端接头": "Compression Tube to Male Connector",
    "内丝卡套直通接头": "Compression Tube to Female Connector",
    "卡套直通接头": "Compression Straight Union",
    "卡套变径直通接头": "Compression Reducing Union",
    "卡套弯通终端接头": "Compression Male Elbow Connector",
    "卡套弯中接头": "Compression Union Elbow",
    "内丝外丝卡套三通接头": "Compression Male/Female Tee",
    "变径式卡套三通接头": "Compression Reducing Tee",
    "钢瓶接头": "Cylinder Connector",
    "卡套穿板接头": "Compression Bulkhead Union",
    "研磨直通终端接头": "Ground Finish Tube to Male Connector",
    "研磨变径卡套直通接头": "Ground Finish Reducing Union",
    "研磨卡套直通接头": "Ground Finish Straight Union",
    "研磨弯通终端接头": "Ground Finish Male Elbow",
    "模锻卡套弯通接头": "Forged Compression Elbow",
    "模锻卡套三通接头": "Forged Compression Tee",
    "快拧接头": "Push-In Quick-Screw Fittings",
    "快拧直通接头": "Quick-Screw Straight Connector",
    "内丝快拧接头": "Quick-Screw Female Connector",
    "快拧直中接头": "Quick-Screw Straight Union",
    "快拧穿板接头": "Quick-Screw Bulkhead Connector",
    "宝塔接头": "Barb Hose Connector",
    "卡套堵头三件套": "Compression Plug Kit (3-Piece)",
    "卡套堵芯": "Compression Plug Insert",
    "内六角堵头": "Hex Socket Plug",
    "外六角堵头": "Hex Head Plug",
    "带边内六角堵头": "Flanged Hex Socket Plug",
    "带边外六角堵头": "Flanged Hex Head Plug",
    "四方堵头": "Square Head Plug",
    "内外丝直通接头": "Male-Female Straight Adapter",
    "内外丝弯通接头": "Male-Female Elbow Adapter",
    "内丝三通接头": "Female Threaded Tee",
    "焊接直通接头": "Weld Straight Connector",
    "直通卡套仿美球阀": "Straight Compression Ball Valve",
    "直角卡套仿美球阀": "Angle Compression Ball Valve",
    "三通卡套仿美球阀": "3-Way Compression Ball Valve",
    "内丝仿美球阀": "Female Threaded Ball Valve",
    "角式内丝仿美球阀": "Angle Female Ball Valve",
    "内丝三通仿美球阀": "Female 3-Way Ball Valve",
    "焊接仿美球阀": "Weld-End Ball Valve",
    "仿进口高压卡套球阀": "High-Pressure Compression Ball Valve",
    "仿进口六角式卡套球阀": "Hex-Body Compression Ball Valve",
    "仿进口长柄六角式卡套球阀": "Long-Handle Hex Compression Ball Valve",
    "直通卡套针阀": "Straight Compression Needle Valve",
    "直通内丝针阀": "Straight Female Needle Valve",
    "内外丝直通针阀": "Male-Female Straight Needle Valve",
    "角式内丝针阀": "Angle Female Needle Valve",
    "高压内丝截止阀": "High-Pressure Female Globe Valve",
    "不锈钢BA管": "Stainless Steel BA Tube",
    "不锈钢精密管": "Stainless Steel Precision Tube",
    "不锈钢盘管": "Stainless Steel Coil Tube",
    "不锈钢波纹管": "Stainless Steel Corrugated Tube",
    "管夹": "Tube Clamp",
    "精铸弯通": "Investment Cast Elbow",
    "精铸三通": "Investment Cast Tee",
    "精铸管帽": "Investment Cast Cap",
    "精铸球阀": "Investment Cast Ball Valve",
    "快插节流阀": "Push-to-Connect Throttle Valve",
    "消音器": "Pneumatic Silencer",
    "卡套快拧直通及卡套快拧穿板接头": "Compression / Quick-Screw Straight & Bulkhead Connectors",
    "卡套四通接头": "Compression Cross Fitting",
    "模锻卡套变径三通接头": "Forged Compression Reducing Tee",
    "模锻卡套四通接头": "Forged Compression Cross Fitting",
    "快拧弯通接头": "Quick-Screw Elbow Connector",
    "快拧三通接头": "Quick-Screw Tee Connector",
    "直通快拧仿美球阀": "Straight Quick-Screw Ball Valve",
    "三通快拧仿美球阀": "3-Way Quick-Screw Ball Valve",
    "迷你球阀": "Mini Ball Valve",
    "高压内丝球阀": "High-Pressure Female Ball Valve",
    "气源球阀": "Air-Source Ball Valve",
    "角式卡套针阀": "Angle Compression Needle Valve",
    "模锻卡套针阀": "Forged Compression Needle Valve",
    "焊接针阀": "Weld-End Needle Valve",
    "快插直通接头": "Push-to-Connect Straight Fitting",
    "快插弯通接头": "Push-to-Connect Elbow Fitting",
    "快插直通中间接头": "Push-to-Connect Straight Union",
    "快插穿板接头": "Push-to-Connect Bulkhead Fitting",
    "Y型+T型三通接头": "Y-Type and T-Type Tee Fitting",
    "卡套单向阀": "Compression Check Valve",
    "内丝单向阀": "Female Thread Check Valve",
    "内丝分体单向阀": "Female Split-Body Check Valve",
    "过滤器系列": "Inline Filter",
    "精铸直通": "Investment Cast Straight Fitting",
    "精铸活接": "Investment Cast Union",
}

SKIP_HEADINGS = {
    "卡套式管接头组成及解剖图",
    "卡套接头使用指南",
    "卡套管及卡套接头建议工作压力值",
    "公制不锈钢管",
    "英制不锈钢管",
    "快拧接头安装方法:",
    "注意事项:",
    "Company Introduction系简介",
    "材质合格设备完善系统管理品质保障",
    "用实力造就品牌",
    "泰州晟泉不锈钢制品厂",
    "不断改进追求卓越",
    "精铸圆直通",  # no EN product page
}


def is_skip(title: str) -> bool:
    if title in SKIP_HEADINGS:
        return True
    if title.startswith(("1、", "2、", "3、", "4、", "5、", "6、", "链接方式", "尺寸范围", "球阀类型", "产品类型", "产品特点")):
        return True
    return False


def is_product(title: str) -> bool:
    return title in CN_TO_EN and not is_skip(title)


def usable_photo(path: Path) -> bool:
    if not path.exists() or path.stat().st_size < 6000:
        return False
    try:
        with Image.open(path) as im:
            w, h = im.size
    except Exception:
        return False
    if w * h < 12000:
        return False
    if w > 900 and h < 450:
        return False
    return True


def lookahead_image(lines, start, end) -> str | None:
    for i in range(start, end):
        m = re.search(r"!\[\]\((images/[^)]+)\)", lines[i])
        if m:
            return m.group(1)
    return None


def page_of(img_rel: str) -> int | None:
    m = re.search(r"page_(\d+)_", img_rel)
    return int(m.group(1)) if m else None


def peek_page(lines: list[str], start: int) -> int | None:
    """Page number of the next image under this heading (same section only)."""
    for j in range(start + 1, min(start + 15, len(lines))):
        if lines[j].startswith("## "):
            return None
        m = re.search(r"page_(\d+)_", lines[j])
        if m:
            return int(m.group(1))
    return None


def parse_pairs(text: str) -> list[tuple[str, str]]:
    """Queue gallery images before titles; drop images that sit under skip headings."""
    lines = text.splitlines()
    events: list[tuple[str, int, str]] = []
    for i, line in enumerate(lines):
        if line.startswith("## "):
            events.append(("h", i, line[3:].strip()))
        m = re.search(r"!\[\]\((images/[^)]+)\)", line)
        if m:
            events.append(("img", i, m.group(1)))

    pending: list[str] = []
    pairs: list[tuple[str, str]] = []
    skip_mode = False
    skip_page: int | None = None
    current_page: int | None = None
    consumed: set[str] = set()

    def next_heading_line(from_idx: int) -> int:
        for kind, li, _ in events:
            if kind == "h" and li > from_idx:
                return li
        return len(lines)

    for kind, i, val in events:
        if kind == "img":
            pg = page_of(val)
            if pg is not None and pg != current_page:
                current_page = pg
                pending.clear()
                # Keep skip only if the skip heading belongs to this new page
                if not (skip_mode and skip_page == pg):
                    skip_mode = False
                    skip_page = None
            if skip_mode or val in consumed:
                continue
            pending.append(val)
            continue

        title = val
        if is_skip(title):
            skip_mode = True
            skip_page = peek_page(lines, i)
            continue

        if is_product(title):
            skip_mode = False
            skip_page = None
            if pending:
                rel = pending.pop(0)
                consumed.add(rel)
                pairs.append((title, rel))
            else:
                end = next_heading_line(i)
                rel = lookahead_image(lines, i + 1, end) or ""
                if rel:
                    consumed.add(rel)
                    if rel in pending:
                        pending.remove(rel)
                pairs.append((title, rel))
            continue

        skip_mode = False
        skip_page = None
        pending.clear()

    return pairs


def load_products():
    out = {}
    for path in PROD_DIR.glob("item-*.md"):
        text = path.read_text(encoding="utf-8")
        title = re.search(r"title:\s*'(.+?)'", text).group(1)
        img = re.search(r"imgMain:\s*'@/images/products/(.+?)'", text).group(1)
        mid = int(re.search(r"id:\s*(\d+)", text).group(1))
        out[title] = {"path": path, "img": img, "id": mid, "text": text}
    return out


def main():
    pairs = parse_pairs(MD.read_text(encoding="utf-8"))
    products = load_products()
    unmatched = set(products)
    updated = []
    need = []

    for cn, rel in pairs:
        en = CN_TO_EN[cn]
        if en not in products:
            need.append((-1, en, "", f"CN '{cn}' mapped but EN product missing"))
            continue
        unmatched.discard(en)
        info = products[en]
        if not rel:
            need.append((info["id"], en, info["img"], f"no catalog image after '{cn}'"))
            continue
        src = EXTRACT / rel
        if not usable_photo(src):
            need.append((info["id"], en, info["img"], f"catalog extract too small/bad: {rel}"))
            continue
        shutil.copy2(src, IMG_DST / info["img"])
        text2 = re.sub(
            r"imgAlt:\s*'[^']*'",
            f"imgAlt: '{en} — FerruleX stainless steel fittings'",
            info["text"],
            count=1,
        )
        if text2 != info["text"]:
            info["path"].write_text(text2, encoding="utf-8", newline="\n")
        updated.append((info["id"], en, info["img"], rel))

    for en in unmatched:
        info = products[en]
        need.append((info["id"], en, info["img"], "no Chinese title match in catalog extract"))

    updated.sort()
    need.sort()
    print(f"UPDATED {len(updated)}")
    for row in updated[:12]:
        print(" ", row)
    if len(updated) > 12:
        print(f"  ... +{len(updated)-12}")
    print(f"\nNEED YOU {len(need)}")
    for row in need:
        print(f"  {row[0]:03d} | {row[1]} | {row[2]} | {row[3]}")

    lines = [
        "Put JPG files into: E:\\AI\\ss-fittings-export\\src\\images\\products\\",
        "Use the exact filename below. Prefer white-background product shots from the Shengquan catalog.",
        "",
        "ID\tEnglish title\tFilename to replace\tReason",
    ]
    for row in need:
        lines.append(f"{row[0]:03d}\t{row[1]}\t{row[2]}\t{row[3]}")
    NEED_FILE.write_text("\n".join(lines), encoding="utf-8")
    print("\nList:", NEED_FILE)


if __name__ == "__main__":
    main()
