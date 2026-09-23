#!/usr/bin/env python3
"""Restructure Astro EN catalog categories to match Shengquan TOC + add missing SKUs."""

from __future__ import annotations

import re
from pathlib import Path

from PIL import Image

EXPORT = Path(r"E:\AI\ss-fittings-export")
PROD = EXPORT / "src" / "content" / "products" / "en"
IMG = EXPORT / "src" / "images" / "products"
CROPS = Path(r"E:\AI\不锈钢接头采集站\supplier-crops")
CAT_FILE = EXPORT / "src" / "data_files" / "categories.ts"

# Title keyword → category slug (first match wins; order matters)
RULES: list[tuple[str, list[str]]] = [
    ("corrugated-hose", ["corrugated hose", "expansion joint", "kf flexible", "corrugated tube"]),
    ("ball-valves", ["ball valve", "valve manifold"]),
    ("needle-valves", ["needle valve", "globe valve"]),
    ("check-valves", ["check valve", "inline filter"]),
    ("cast-fittings", ["investment cast"]),
    ("instrumentation-tubing", ["ba tube", "precision tube", "coil tube", "tube clamp"]),
    ("quick-screw-fittings", ["quick-screw", "push-in quick-screw"]),
    ("push-to-connect", ["push-to-connect", "push-in"]),
    ("plugs-and-barbs", ["plug", "barb", "silencer", "throttle", "ferrule"]),
    ("adapters-and-weld", ["adapter", "male-female", "weld straight", "female threaded tee", "y-type", "tee fitting"]),
    ("compression-fittings", ["compression", "ground finish", "forged", "cylinder connector", "bulkhead"]),
    ("custom-fittings", ["custom", "non-standard", "nonstandard"]),
]

CATEGORIES_TS = r'''export type CategoryDef = {
  /** Short SEO path segment, e.g. compression-fittings */
  slug: string;
  /** Short buyer-facing intro shown under the h1 on category pages */
  intro: string;
  title: string;
  shortTitle: string;
  description: string;
  keyword: string;
  h1: string;
  match: string[];
};

/**
 * Category order follows the Shengquan selection-manual series
 * (corrugated hose → compression → quick-screw → plugs/barbs → adapters/weld →
 *  ball → needle → check → tubing → push-to-connect → cast → custom).
 */
export const PRODUCT_CATEGORIES: CategoryDef[] = [
  {
    slug: 'corrugated-hose',
    intro:
      'Start from the hose OD and the two end connections. If the media is steam or the run crosses a hot zone, tell us the temperature — bellows material and braid change with it.',
    title: 'Corrugated Stainless Steel Hose',
    shortTitle: 'Corrugated Hose',
    h1: 'Corrugated Stainless Steel Hose & Expansion Joints',
    description:
      'Corrugated hose for vibration and thermal movement: male/female thread, flange, tri-clamp, quick coupling and KF. SS304 or SS316. Length and ends on the RFQ.',
    keyword: 'corrugated stainless steel hose',
    match: ['corrugated hose', 'expansion joint', 'kf flexible', 'corrugated tube'],
  },
  {
    slug: 'compression-fittings',
    intro:
      'Measure tube OD exactly (metric or inch). A double-ferrule joint is sized by tube, so the OD plus the port thread decides the part.',
    title: 'Stainless Steel Compression Fittings',
    shortTitle: 'Compression Fittings',
    h1: 'Stainless Steel Compression Fittings (Double Ferrule)',
    description:
      'Double-ferrule connectors, elbows, tees, unions, bulkheads, ground-finish and forged series. Metric and inch tube. NPT, G and metric threads.',
    keyword: 'stainless steel compression fittings',
    match: [
      'compression',
      'ground finish',
      'forged',
      'cylinder connector',
      'bulkhead union',
    ],
  },
  {
    slug: 'quick-screw-fittings',
    intro:
      'Quick-screw fittings speed panel work with a nut-and-ferrule bite on soft or hard tube. Confirm OD and thread gender on the RFQ.',
    title: 'Stainless Steel Quick-Screw Fittings',
    shortTitle: 'Quick-Screw',
    h1: 'Stainless Steel Quick-Screw Tube Fittings',
    description:
      'Quick-screw straight, female, union, elbow, tee and bulkhead connectors for air and light fluid lines. Separate from push-to-connect series.',
    keyword: 'quick screw fittings',
    match: ['quick-screw'],
  },
  {
    slug: 'plugs-and-barbs',
    intro:
      'Plugs close unused ports; barb ends take hose. List every thread standard in the BOM so the blank matches the manifold.',
    title: 'Stainless Steel Plugs & Barb Fittings',
    shortTitle: 'Plugs & Barbs',
    h1: 'Stainless Steel Plugs, Caps & Barb Hose Fittings',
    description:
      'Hex plugs, flanged plugs, square plugs, compression plug kits, ferrules, barb hose connectors, silencers and throttle valves.',
    keyword: 'stainless steel plug fitting',
    match: ['plug', 'barb', 'silencer', 'throttle', 'ferrule'],
  },
  {
    slug: 'adapters-and-weld',
    intro:
      'Adapters and weld ends finish mixed-thread manifolds. Send both end standards when the two sides differ.',
    title: 'Stainless Steel Adapters & Weld Fittings',
    shortTitle: 'Adapters & Weld',
    h1: 'Stainless Steel Thread Adapters & Weld Connectors',
    description:
      'Male-female adapters, elbows, tees, weld straight connectors and Y/T branch fittings for instrumentation manifolds.',
    keyword: 'stainless steel adapter fitting',
    match: [
      'adapter',
      'male-female',
      'weld straight',
      'female threaded tee',
      'y-type',
      'tee fitting',
    ],
  },
  {
    slug: 'ball-valves',
    intro:
      'Pick the end first (compression, female thread or weld), then the flow pattern. Pressure class and seat material are confirmed on the quote, not assumed.',
    title: 'Stainless Steel Ball Valves',
    shortTitle: 'Ball Valves',
    h1: 'Stainless Steel Ball Valves & Manifolds',
    description:
      'Shutoff valves with compression, female thread or weld ends — straight, angle, 3-way, mini, high-pressure and valve manifolds. Confirm the pressure class on the quote.',
    keyword: 'stainless steel ball valve',
    match: ['ball valve', 'valve manifold'],
  },
  {
    slug: 'needle-valves',
    intro:
      'Needle valves meter flow — they are not shutoff valves. Send the orifice size and the gauge or sampler it feeds, and we match the Cv.',
    title: 'Stainless Steel Needle Valves',
    shortTitle: 'Needle Valves',
    h1: 'Stainless Steel Needle & Globe Valves',
    description:
      'Needle and globe valves for metering, sampling and gauge isolation. Compression or female thread. Not a substitute for a ball valve on full-flow shutoff.',
    keyword: 'stainless steel needle valve',
    match: ['needle valve', 'globe valve'],
  },
  {
    slug: 'check-valves',
    intro:
      'These valves are direction-sensitive. Mark flow direction and cracking pressure on the RFQ so the factory sets the spring or disc correctly.',
    title: 'Stainless Steel Check Valves',
    shortTitle: 'Check Valves',
    h1: 'Stainless Steel Check Valves & Inline Filters',
    description:
      'One-way valves in compression, female thread and split-body styles, plus inline filters. Mark flow direction on the order.',
    keyword: 'stainless steel check valve',
    match: ['check valve', 'inline filter'],
  },
  {
    slug: 'instrumentation-tubing',
    intro:
      'Tube and clamps go with the compression series. State wall thickness and finish (BA, annealed, or standard) with the OD.',
    title: 'Stainless Steel Instrumentation Tubing',
    shortTitle: 'Tube & Clamps',
    h1: 'Stainless Steel BA Tube, Coil Tube & Clamps',
    description:
      'BA tube, precision tube, coil tube and tube clamps for instrumentation tubing runs. Pair with FerruleX compression fittings.',
    keyword: 'instrumentation fittings',
    match: ['ba tube', 'precision tube', 'coil tube', 'tube clamp'],
  },
  {
    slug: 'push-to-connect',
    intro:
      'Push-to-connect is for compatible tube OD and hardness — typically air and light utilities, not steam. Confirm OD before ordering.',
    title: 'Stainless Steel Push-to-Connect Fittings',
    shortTitle: 'Push-to-Connect',
    h1: 'Stainless Steel Push-to-Connect (Push-In) Fittings',
    description:
      'Push-in straight, elbow, union and bulkhead fittings for rapid tube changes on pneumatic and utility lines. Separate series from quick-screw.',
    keyword: 'push to connect stainless fitting',
    match: ['push-to-connect', 'push-in'],
  },
  {
    slug: 'cast-fittings',
    intro:
      'Investment-cast bodies suit general process connections. Tell us the casting size and port style; machining tolerance is confirmed at RFQ.',
    title: 'Stainless Steel Cast Fittings',
    shortTitle: 'Cast Fittings',
    h1: 'Investment Cast Stainless Steel Fittings',
    description:
      'Investment-cast stainless elbows, tees, straights, unions, caps and cast ball valves for general process connections. SS304 / SS316.',
    keyword: 'investment cast stainless fitting',
    match: ['investment cast'],
  },
  {
    slug: 'custom-fittings',
    intro:
      'Non-standard parts from the custom page of the factory manual. Send a drawing or photo with size, grade and quantity for a manufacturability review.',
    title: 'Custom & Non-Standard Fittings',
    shortTitle: 'Custom / Non-Standard',
    h1: 'Custom & Non-Standard Stainless Steel Fittings',
    description:
      'Factory custom and non-standard stainless fittings — special elbows, tees, valve bodies and machined parts beyond the stocked catalog lines.',
    keyword: 'custom stainless steel fittings',
    match: ['custom', 'non-standard', 'nonstandard'],
  },
];

export function categoryFromTitle(title: string): CategoryDef {
  const t = title.toLowerCase();
  for (const cat of PRODUCT_CATEGORIES) {
    if (cat.match.some(m => t.includes(m))) return cat;
  }
  return PRODUCT_CATEGORIES.find(c => c.slug === 'adapters-and-weld')!;
}

export function getCategory(slug: string): CategoryDef | undefined {
  // Legacy slugs from earlier IA — keep bookmarks working
  const aliases: Record<string, string> = {
    'tube-fittings': 'quick-screw-fittings',
    'pipe-fittings': 'adapters-and-weld',
  };
  const resolved = aliases[slug] ?? slug;
  return PRODUCT_CATEGORIES.find(c => c.slug === resolved);
}

/** Flat product URL: /products/{slug}/ — category stays in breadcrumbs, not the path. */
export function productPath(_category: string, slug: string): string {
  return `/products/${slug}/`;
}

export function categoryPath(slug: string): string {
  const aliases: Record<string, string> = {
    'tube-fittings': 'quick-screw-fittings',
    'pipe-fittings': 'adapters-and-weld',
  };
  return `/products/${aliases[slug] ?? slug}/`;
}

export function productsHubPath(): string {
  return '/products/';
}
'''


def category_for_title(title: str) -> str:
    t = title.lower()
    # Special cases before generic rules
    if "ferrule" == t.strip() or t == "ferrule":
        return "plugs-and-barbs"
    if "valve manifold" in t:
        return "ball-valves"
    if "custom" in t or "non-standard" in t:
        return "custom-fittings"
    for slug, keys in RULES:
        if any(k in t for k in keys):
            # avoid "compression bulkhead" matching plugs "bulkhead" — compression rules later
            if slug == "plugs-and-barbs" and "compression bulkhead" in t:
                continue
            if slug == "plugs-and-barbs" and "bulkhead" in t and "plug" not in t and "barb" not in t:
                continue
            if slug == "adapters-and-weld" and "tee" in t and "compression" in t:
                continue
            if slug == "adapters-and-weld" and "y-type" not in t and t.endswith("tee") and "female threaded" not in t:
                # compression tees handled by compression
                if "compression" in t or "forged" in t:
                    continue
            return slug
    return "adapters-and-weld"


def remap_categories() -> None:
    for path in PROD.glob("item-*.md"):
        text = path.read_text(encoding="utf-8")
        fm = text.split("---", 2)[1]
        title_m = re.search(r"^title:\s*['\"](.+?)['\"]\s*$", fm, re.M)
        cat_m = re.search(r"^category:\s*['\"](.+?)['\"]\s*$", fm, re.M)
        if not title_m or not cat_m:
            continue
        title = title_m.group(1)
        old = cat_m.group(1)
        new = category_for_title(title)
        if old == new:
            continue
        new_text = re.sub(
            r"^category:\s*['\"].+?['\"]\s*$",
            f"category: '{new}'",
            text,
            count=1,
            flags=re.M,
        )
        path.write_text(new_text, encoding="utf-8", newline="\n")
        print(f"CAT  {old} -> {new} | {title}")


def save_cover(src: Path, dst: Path, max_side: int = 1200) -> None:
    im = Image.open(src).convert("RGB")
    w, h = im.size
    scale = min(1.0, max_side / max(w, h))
    if scale < 1:
        im = im.resize((int(w * scale), int(h * scale)), Image.Resampling.LANCZOS)
    dst.parent.mkdir(parents=True, exist_ok=True)
    im.save(dst, "JPEG", quality=90, optimize=True)


def next_id() -> int:
    ids = []
    for path in PROD.glob("item-*.md"):
        m = re.search(r"id:\s*(\d+)", path.read_text(encoding="utf-8"))
        if m:
            ids.append(int(m.group(1)))
    return max(ids) + 1 if ids else 100


def write_product(
    *,
    pid: int,
    title: str,
    slug: str,
    category: str,
    description: str,
    content: str,
    img_name: str,
    specs: list[tuple[str, str]],
) -> None:
    table_rows = "\n".join(f"      - ['{k}', '{v}']" for k, v in specs)
    spec_left = "\n".join(
        f"  - title: '{k}'\n    subTitle: '{v}'" for k, v in specs
    )
    md = f"""---
title: '{title}'
description: '{description}'
category: '{category}'
slug: '{slug}'
main:
  id: {pid}
  content: |
    {content}
  imgCard: '@/images/products/{img_name}'
  imgMain: '@/images/products/{img_name}'
  imgAlt: '{title} — FerruleX stainless steel fittings'
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
  title: '{title}'
  subTitle: |
    Tell FerruleX the size, grade and quantity on the RFQ. Stocked catalog lines ship after quote confirmation; custom dimensions need a drawing.
  btnTitle: 'Request a factory quote'
  btnURL: '/contact/'
descriptionList:
  - title: 'Factory'
    subTitle: 'Quoted from the Shengquan / FerruleX stainless catalog.'
  - title: 'Order'
    subTitle: 'RFQ only — no cart checkout.'
  - title: 'Grade'
    subTitle: 'SS304 / SS316 options on most lines.'
specificationsLeft:
{spec_left}
tableData:
  - feature: ['Specification', 'Value']
    description:
{table_rows}
blueprints:
  first: '@/images/blueprint-1.avif'
  second: '@/images/blueprint-2.avif'
---
"""
    out = PROD / f"item-{pid:03d}-{slug}.md"
    out.write_text(md, encoding="utf-8", newline="\n")
    print(f"ADD  {out.name}")


def add_missing_skus() -> None:
    existing = set()
    for path in PROD.glob("item-*.md"):
        fm = path.read_text(encoding="utf-8").split("---", 2)[1]
        m = re.search(r"^title:\s*['\"](.+?)['\"]\s*$", fm, re.M)
        if m:
            existing.add(m.group(1))

    # Ferrule / 卡芯
    if "Ferrule" not in existing:
        pid = next_id()
        img = f"p08-{pid:02d}-ferrule.jpg"
        src = CROPS / "p08-05-photo-513x434.jpg"
        if src.exists():
            save_cover(src, IMG / img)
        write_product(
            pid=pid,
            title="Ferrule",
            slug="ferrule",
            category="plugs-and-barbs",
            description="Stainless ferrule for compression fittings. SS304/316. FerruleX factory RFQ. Stocked sizes ship fast.",
            content="Ferrules bite and seal on tube OD inside a double-ferrule nut. FerruleX stocks stainless ferrules for instrumentation tube in SS304/SS316. Match the ferrule to the tube OD and the nut series — mixing brands risks leaks. Quote OD and series with the rest of the compression BOM.",
            img_name=img,
            specs=[
                ("Brand", "FerruleX"),
                ("Material", "SS304 / SS316"),
                ("Type", "Compression ferrule"),
                ("Size", "Match tube OD / series on RFQ"),
            ],
        )

    # Valve manifold / 阀组
    if "Valve Manifold" not in existing:
        pid = next_id()
        img = f"p10-{pid:02d}-valve-manifold.jpg"
        src = CROPS / "p10-07-photo-656x556.jpg"
        if src.exists():
            save_cover(src, IMG / img)
        write_product(
            pid=pid,
            title="Valve Manifold",
            slug="valve-manifold",
            category="ball-valves",
            description="Stainless valve manifold for instrument isolation and distribution. FerruleX factory RFQ. Confirm ports and pressure class.",
            content="Valve manifolds combine isolation and distribution ports for gauges and instrument lines. FerruleX quotes stainless manifolds with the port count, thread standard and pressure class you name on the RFQ. Pair with ball or needle valves from the same plant so packing and documents stay on one shipment.",
            img_name=img,
            specs=[
                ("Brand", "FerruleX"),
                ("Material", "SS304 / SS316"),
                ("Type", "Valve manifold"),
                ("Ports", "Confirm on RFQ"),
                ("Pressure", "Confirm on RFQ"),
            ],
        )

    # Custom / non-standard samples from page 15 grid (first 12 product-like crops)
    custom_crops = sorted(CROPS.glob("p15-*-photo-*.jpg"))
    # skip obvious oversized scene photos if any — keep square-ish catalog tiles
    custom_crops = [c for c in custom_crops if "photo" in c.name][:12]
    for i, src in enumerate(custom_crops, start=1):
        title = f"Custom Non-Standard Fitting #{i:02d}"
        if title in existing:
            continue
        pid = next_id()
        slug = f"custom-non-standard-fitting-{i:02d}"
        img = f"p15-{pid:02d}-{slug}.jpg"
        save_cover(src, IMG / img)
        write_product(
            pid=pid,
            title=title,
            slug=slug,
            category="custom-fittings",
            description=f"Custom / non-standard stainless fitting sample #{i:02d} from the factory selection manual. Send a drawing for RFQ.",
            content=f"This non-standard stainless fitting #{i:02d} appears in the factory custom gallery. Dimensions, ends and grade are confirmed from your drawing or sample — not assumed from the photo alone. Send OD/thread, material and quantity for a manufacturability review and lead time.",
            img_name=img,
            specs=[
                ("Brand", "FerruleX"),
                ("Material", "SS304 / SS316 (confirm)"),
                ("Type", "Custom / non-standard"),
                ("Drawing", "Required for firm quote"),
            ],
        )
        existing.add(title)


def main() -> None:
    CAT_FILE.write_text(CATEGORIES_TS, encoding="utf-8", newline="\n")
    print("Wrote categories.ts")
    remap_categories()
    add_missing_skus()

    # summary
    from collections import Counter

    cats = Counter()
    for path in PROD.glob("item-*.md"):
        fm = path.read_text(encoding="utf-8").split("---", 2)[1]
        m = re.search(r"^category:\s*['\"](.+?)['\"]\s*$", fm, re.M)
        if m:
            cats[m.group(1)] += 1
    print("\nFinal counts:")
    for k, v in cats.most_common():
        print(f"  {k}: {v}")
    print("total", sum(cats.values()))


if __name__ == "__main__":
    main()
