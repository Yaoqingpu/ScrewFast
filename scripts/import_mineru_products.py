# -*- coding: utf-8 -*-
"""Import MinerU-extracted Shengquan catalog into ScrewFast product collection."""
import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXTRACT = ROOT / "mineru-out" / "extracted"
IMG_DST = ROOT / "src" / "images" / "products"
PROD_EN = ROOT / "src" / "content" / "products" / "en"
PROD_FR = ROOT / "src" / "content" / "products" / "fr"

IMG_DST.mkdir(parents=True, exist_ok=True)

for d in (PROD_EN, PROD_FR):
    for f in d.glob("item-*.md"):
        f.unlink()

TRANS = {
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
}

SKIP_PREFIX = (
    "链接方式",
    "尺寸范围",
    "球阀类型",
    "产品类型",
    "产品特点",
    "1、",
    "2、",
    "3、",
    "4、",
    "5、",
    "6、",
    "卡套式",
    "卡套接头使用",
    "卡套管及",
    "将管子",
    "快拧接头是一种",
    "快拧接头安装",
    "卡套式管接头组成",
)

PRODUCT_RE = re.compile(
    r"(接头|波纹管|补偿器|球阀|针阀|截止阀|堵头|堵芯|宝塔|管夹|BA管|精密管|盘管|节流阀|消音器|弯通|三通|管帽)"
)


def is_product_title(c: str) -> bool:
    c = c.strip()
    if not c or len(c) > 40:
        return False
    if c.startswith(SKIP_PREFIX):
        return False
    if c in TRANS:
        return True
    return bool(PRODUCT_RE.search(c)) and "：" not in c and ":" not in c


def en_title(cn: str) -> str:
    return TRANS.get(cn, f"SS Fitting — {cn}")


def slugify(s: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    return s[:60] or "product"


def esc(s: str) -> str:
    return s.replace("'", "''")


data = json.loads((EXTRACT / "structured_content.json").read_text(encoding="utf-8"))

products = []
seen_titles = set()

for page in data["pages"]:
    titles = []
    images = []
    for b in page["blocks"]:
        t = b.get("type")
        c = (b.get("content") or "").strip()
        if t == "paragraph_title" and is_product_title(c):
            titles.append(c)
        if t == "image" and b.get("image_source"):
            images.append(b["image_source"])
    n = min(len(titles), len(images))
    for i in range(n):
        cn = titles[i]
        if cn in seen_titles:
            continue
        seen_titles.add(cn)
        products.append(
            {
                "cn": cn,
                "en": en_title(cn),
                "image": images[i],
                "page": page["page_idx"],
            }
        )

print(f"Paired products: {len(products)}")

written = 0
for idx, p in enumerate(products, start=1):
    src = EXTRACT / p["image"]
    if not src.exists():
        print("MISSING", src)
        continue
    if src.stat().st_size < 8000:
        print("skip small", src.name)
        continue

    fname = f"p{p['page']:02d}-{idx:02d}-{slugify(p['en'])}.jpg"
    dst = IMG_DST / fname
    shutil.copy2(src, dst)
    img_ref = f"@/images/products/{fname}"
    slug = f"item-{idx:03d}-{slugify(p['en'])[:40]}"
    title = p["en"]
    desc = (
        f"{title}. Stainless steel industrial fitting for instrumentation, "
        "fluid and gas systems. SS304 / SS316 / SS316L. Request a quote."
    )[:160]

    content = f"""---
title: '{esc(title)}'
description: '{esc(desc)}'
main:
  id: {idx}
  content: |
    {title} from our stainless steel valves and fittings catalog. Suitable for liquid and gas service in petrochemical, instrumentation, food, pharma and OEM equipment. Materials include SS304, SS316 and SS316L. Threads available in NPT, BSP/G, metric and ZG(R). Send your size list for a quotation — all orders are negotiated.
  imgCard: '{img_ref}'
  imgMain: '{img_ref}'
  imgAlt: '{esc(title)}'
tabs:
  - id: 'tabs-with-card-item-1'
    dataTab: '#tabs-with-card-1'
    title: 'Description'
  - id: 'tabs-with-card-item-2'
    dataTab: '#tabs-with-card-2'
    title: 'Specifications'
  - id: 'tabs-with-card-item-3'
    dataTab: '#tabs-with-card-3'
    title: 'Drawings'
longDescription:
  title: '{esc(title)}'
  subTitle: |
    Industrial stainless steel fitting for export OEM and project buyers. Typical working pressure around 1000 PSI (higher-pressure options available). Custom sizes and non-standard machining on request.
  btnTitle: 'Request a quote'
  btnURL: '/contact'
descriptionList:
  - title: 'Materials'
    subTitle: 'SS304 / SS316 / SS316L (brass optional on selected items).'
  - title: 'Connections'
    subTitle: 'Compression, threaded, weld, quick-screw or push-fit depending on series.'
  - title: 'Applications'
    subTitle: 'Instrumentation tubing, petrochemical, marine, food and pharma, OEM machinery.'
specificationsLeft:
  - title: 'Material'
    subTitle: 'Stainless steel 304 / 316 / 316L'
  - title: 'Size range'
    subTitle: 'Metric and imperial tube OD; NPT / G / Metric threads'
  - title: 'Media'
    subTitle: 'Liquid and gas'
  - title: 'Pressure'
    subTitle: 'Approx. 1000 PSI standard; high-pressure series available'
tableData:
  - feature: ['Specification', 'Value']
    description:
      - ['Material', 'SS304 / SS316 / SS316L']
      - ['Origin', 'China']
      - ['MOQ', 'Negotiable']
      - ['Lead time', 'Discuss after RFQ']
blueprints:
  first: '@/images/blueprint-1.avif'
  second: '@/images/blueprint-2.avif'
---
"""
    (PROD_EN / f"{slug}.md").write_text(content, encoding="utf-8")
    written += 1

print("Wrote", written, "EN products")
print("Images:", len(list(IMG_DST.glob("*.jpg"))))
