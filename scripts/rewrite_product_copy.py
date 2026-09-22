# -*- coding: utf-8 -*-
"""Rewrite EN product copy with SEO keywords + catalog specs for FerruleX."""
from __future__ import annotations

import re
from pathlib import Path

PROD_DIR = Path(__file__).resolve().parents[1] / "src" / "content" / "products" / "en"


def shape_hint(title: str) -> str:
    t = title.lower()
    if "3-way" in t or "three-way" in t:
        return "a three-way pattern for diverting or mixing flow"
    if "cross" in t:
        return "a four-port cross for branching instrumentation lines"
    if "elbow" in t or "angle" in t:
        return "an angle / elbow body for compact panel routing"
    if "tee" in t or "y-type" in t:
        return "a tee for branching tube or threaded lines"
    if "bulkhead" in t:
        return "a bulkhead / panel-pass design for wall mounting"
    if "reducing" in t or "reducer" in t:
        return "a reducing size for metric or imperial tube transitions"
    if "union" in t:
        return "a union for inline tube-to-tube connection"
    if "male" in t and "female" in t:
        return "a male-female adapter between thread standards or sizes"
    if "female" in t:
        return "a female-thread end style for manifolds and gauges"
    if "male" in t:
        return "a male-thread end style for ports and adapters"
    if "weld" in t:
        return "a weld-end design for permanent process connections"
    if "plug" in t or "cap" in t:
        return "a sealing accessory to blank unused ports"
    if "mini" in t:
        return "a compact mini body for tight OEM panels"
    if "high-pressure" in t or "high pressure" in t:
        return "a higher-pressure series for demanding service"
    if "straight" in t:
        return "a straight-through body for low pressure drop"
    if "hex" in t:
        return "a hex-body design for compact wrench access"
    if "flanged" in t or "flange" in t:
        return "a flanged-end style for process connections"
    if "tri-clamp" in t:
        return "a tri-clamp sanitary / hygienic end style"
    if "quick-coupling" in t or "quick-screw" in t or "push-to-connect" in t:
        return "a fast-connect style for air and light fluid lines"
    return "part of our stainless instrumentation catalog"


CATEGORY_COPY = [
    (
        ("corrugated hose", "corrugated tube", "expansion joint", "kf flexible"),
        {
            "desc": (
                "{title} - corrugated stainless steel hose for instrumentation and OEM "
                "lines. SS304 / SS316. Threaded, flanged, tri-clamp, quick-coupling or KF "
                "ends. Request length and ends for a FerruleX quote."
            ),
            "intro": (
                "{title} is {shape} in our corrugated stainless steel hose range. "
                "Use it for vibration absorption, thermal movement and tight routing "
                "where rigid tube will not work. Typical OD 6-100 mm; KF/ISO sizes for "
                "vacuum styles. Materials SS304 / SS316. Tell us end connection, length "
                "and media for an RFQ."
            ),
            "long": (
                "FerruleX factory manufactures corrugated stainless steel hose with male/female "
                "thread, flanged, tri-clamp, quick-coupling and KF vacuum ends. Custom "
                "lengths and non-standard ends are available for OEM projects."
            ),
            "bullets": [
                ("Ends", "Thread, flange, tri-clamp, quick-coupling or KF vacuum."),
                ("Materials", "SS304 / SS316 stainless steel."),
                ("Sizes", "Typically OD 6-100 mm; KF16-ISO100 for vacuum hose."),
            ],
            "specs": [
                ("Brand", "FerruleX"),
                ("Material", "SS304 / SS316"),
                ("Size range", "OD 6-100 mm (series dependent)"),
                ("Customization", "Non-standard ends and lengths on request"),
            ],
        },
    ),
    (
        ("ball valve",),
        {
            "desc": (
                "{title} - stainless steel ball valve for instrumentation and process "
                "lines. Compression, female thread or weld ends. SS304 / SS316 / SS316L. "
                "Request size and pressure from FerruleX."
            ),
            "intro": (
                "{title} is {shape}. This stainless steel ball valve suits liquid and "
                "gas service on instrumentation panels, pneumatic lines and process "
                "skids. Choose compression (double-ferrule), female NPT/G/metric or weld "
                "ends. Typical working pressure around 1000 PSI; high-pressure series "
                "available. Send size, thread and quantity for a factory quote — stocked sizes ship fast."
            ),
            "long": (
                "Stainless steel ball valves shut off flow quickly with low pressure "
                "drop. Our factory covers compression-end and threaded styles for OEM and "
                "project buyers who need SS316 compatibility and mixed threads "
                "(NPT, G, ZG/R, metric)."
            ),
            "bullets": [
                ("Patterns", "Straight, angle and 3-way; panel mount on selected models."),
                ("Ends", "Compression, female thread or weld."),
                ("Materials", "SS304 / SS316 / SS316L."),
            ],
            "specs": [
                ("Brand", "FerruleX"),
                ("Material", "SS304 / SS316 / SS316L"),
                ("Connections", "Compression / threaded / weld"),
                ("Pressure", "~1000 PSI standard; HP series available"),
            ],
        },
    ),
    (
        ("needle valve", "globe valve"),
        {
            "desc": (
                "{title} - stainless steel needle valve for fine flow control. "
                "Compression or threaded ends, straight and angle bodies. SS304 / SS316. "
                "Request size and Cv needs from FerruleX."
            ),
            "intro": (
                "{title} is {shape}. Use this stainless steel needle valve for sampling, "
                "pressure-gauge isolation and metering lines where throttling accuracy "
                "matters. Compression tube ends or female threads; angle patterns for "
                "panels. Materials SS304 / SS316 / SS316L. Include tube OD or thread, "
                "media and pressure in your RFQ."
            ),
            "long": (
                "Needle valves excel where control matters more than full-bore shutoff. "
                "Pair with FerruleX factory stainless steel tube fittings and ball valves for "
                "complete instrumentation manifolds."
            ),
            "bullets": [
                ("Control", "Fine stem metering for precise flow adjustment."),
                ("Ends", "Compression or female thread; straight / angle."),
                ("Materials", "SS304 / SS316 / SS316L."),
            ],
            "specs": [
                ("Brand", "FerruleX"),
                ("Material", "SS304 / SS316 / SS316L"),
                ("Connections", "Compression / threaded"),
                ("Service", "Sampling, isolation, metering"),
            ],
        },
    ),
    (
        ("check valve",),
        {
            "desc": (
                "{title} - stainless steel check valve for one-way flow protection. "
                "SS304 / SS316 options. Request size and cracking pressure from FerruleX."
            ),
            "intro": (
                "{title} is {shape}. This stainless steel check valve helps protect "
                "pumps, gauges and process lines from reverse flow. Confirm size, "
                "end style and media when you request a quotation."
            ),
            "long": (
                "Add check valves alongside FerruleX compression fittings and shutoff "
                "valves to complete liquid and gas manifolds."
            ),
            "bullets": [
                ("Function", "One-way flow / reverse-flow protection."),
                ("Materials", "SS304 / SS316."),
                ("Ordering", "RFQ with size, ends and media."),
            ],
            "specs": [
                ("Brand", "FerruleX"),
                ("Material", "SS304 / SS316"),
                ("Type", "Check / non-return"),
                ("MOQ", "Negotiable"),
            ],
        },
    ),
    (
        (
            "compression",
            "ferrule",
            "bulkhead",
            "union elbow",
            "forged",
            "ground finish",
            "cylinder connector",
        ),
        {
            "desc": (
                "{title} - stainless steel compression fittings (double-ferrule) for "
                "instrumentation tubing. OD 3-25 mm / 1/8\"-1\". SS304 / SS316 / SS316L. "
                "NPT, G, ZG(R), metric. Quote via FerruleX."
            ),
            "intro": (
                "{title} is {shape} in our stainless steel compression fittings / "
                "double-ferrule tube fittings series. Size range typically OD 3-25 mm "
                "and 1/8\"-1\", with threads M5-M24 plus NPT / G / ZG(R). Materials "
                "SS316, SS316L, SS304. Working pressure around 1000 PSI; HP versions "
                "up to ~4500 PSI. Send tube OD, thread and quantity for an RFQ."
            ),
            "long": (
                "Double-ferrule compression fittings grip annealed stainless tubing "
                "for a metal-to-metal seal on gas and liquid service. Use ASTM A269 / "
                "GB/T 14976 tubing where specified. FerruleX supports petrochemical, "
                "marine, food, pharma and OEM equipment panels."
            ),
            "bullets": [
                ("Seal", "Double-ferrule bite for leak-resistant tube joints."),
                ("Sizes", "Metric OD 3-25 mm; imperial 1/8\"-1\"; M5-M24 threads."),
                ("Pressure", "~1000 PSI standard; HP series ~4500 PSI."),
            ],
            "specs": [
                ("Brand", "FerruleX"),
                ("Material", "SS316 / SS316L / SS304"),
                ("Tube OD", "OD 3-25 mm / 1/8\"-1\""),
                ("Threads", "NPT, G, ZG(R), Metric"),
            ],
        },
    ),
    (
        ("quick-screw", "push-in", "push-to-connect", "barb", "push-to-connect"),
        {
            "desc": (
                "{title} - stainless steel quick-screw / push-style tube fittings for "
                "air and water lines. OD 4-16 mm / 1/8\"-1/2\". SS304 / SS316. "
                "Request tube OD and thread from FerruleX."
            ),
            "intro": (
                "{title} is {shape} for fast tube connection on pneumatic and light "
                "hydraulic lines. Insert tube, seat fully, tighten the nut. Sizes "
                "typically OD 4-16 mm and 1/8\"-1/2\" with NPT / G / metric threads. "
                "Materials SS304 / SS316 / SS316L. Send your tube OD list for pricing."
            ),
            "long": (
                "Quick-screw stainless fittings reduce install time versus fully "
                "welded joints while keeping corrosion resistance for plant air, "
                "water and light process media."
            ),
            "bullets": [
                ("Install", "Push tube to stem, then tighten nut - no special flaring."),
                ("Sizes", "OD 4-16 mm / 1/8\"-1/2\"; M5-M24 threads."),
                ("Materials", "SS304 / SS316 / SS316L."),
            ],
            "specs": [
                ("Brand", "FerruleX"),
                ("Material", "SS304 / SS316 / SS316L"),
                ("Tube OD", "OD 4-16 mm / 1/8\"-1/2\""),
                ("Pressure", "~1000 PSI"),
            ],
        },
    ),
    (
        (
            "plug",
            "cap",
            "silencer",
            "throttle",
            "clamp",
            "ba tube",
            "precision tube",
            "coil tube",
            "cast",
            "tee fitting",
        ),
        {
            "desc": (
                "{title} - stainless steel fittings accessory for instrumentation and "
                "OEM assemblies. SS304 / SS316. Request dimensions from FerruleX."
            ),
            "intro": (
                "{title} is {shape}. It completes stainless tubing systems alongside "
                "compression fittings, ball valves and needle valves. Materials "
                "SS304 / SS316. Provide a drawing or size table for custom and OEM RFQs."
            ),
            "long": (
                "Accessories and tubing keep manifolds sealed and lines supported. "
                "FerruleX reviews non-standard machining when catalog sizes do not "
                "match your drawing."
            ),
            "bullets": [
                ("Role", "Seal, support or route stainless instrumentation lines."),
                ("Materials", "SS304 / SS316 (series dependent)."),
                ("OEM", "Custom sizes available after drawing review."),
            ],
            "specs": [
                ("Brand", "FerruleX"),
                ("Material", "SS304 / SS316"),
                ("Standards", "Catalog + custom OEM"),
                ("MOQ", "Negotiable"),
            ],
        },
    ),
]

DEFAULT = {
    "desc": (
        "{title} - stainless steel fittings for instrumentation and OEM export. "
        "SS304 / SS316 / SS316L. Request size, thread and quantity from our factory — fast delivery on stocked SKUs."
    ),
    "intro": (
        "{title} is {shape} in the FerruleX stainless steel valves and fittings "
        "factory catalog. Materials include SS304, SS316 and SS316L. Connections may "
        "include compression, threaded, weld or quick-connect styles. Factory RFQs "
        "are negotiated — stocked sizes support fast delivery; send your size list."
    ),
    "long": (
        "Buy stainless steel tube fittings and valves direct from the FerruleX factory for "
        "petrochemical, marine, food, pharma and OEM equipment projects. Fast delivery "
        "on common stocked sizes."
    ),
    "bullets": [
        ("Materials", "SS304 / SS316 / SS316L."),
        ("Connections", "Compression, threaded, weld or quick-connect."),
        ("Ordering", "RFQ based - no online checkout."),
    ],
    "specs": [
        ("Brand", "FerruleX"),
        ("Material", "SS304 / SS316 / SS316L"),
        ("Origin", "China"),
        ("Lead time", "Discuss after RFQ"),
    ],
}


CATEGORY_RULES = [
    (
        "stainless-steel-corrugated-hose",
        ["corrugated hose", "expansion joint", "kf flexible", "corrugated tube"],
    ),
    ("stainless-steel-ball-valves", ["ball valve"]),
    ("stainless-steel-needle-valves", ["needle valve", "globe valve"]),
    (
        "stainless-steel-compression-fittings",
        [
            "compression",
            "ferrule",
            "ground finish",
            "forged",
            "cylinder connector",
            "bulkhead",
        ],
    ),
    (
        "stainless-steel-tube-fittings",
        ["quick-screw", "push-in", "push-to-connect", "barb"],
    ),
    (
        "stainless-steel-pipe-fittings",
        [
            "plug",
            "adapter",
            "male-female",
            "female threaded tee",
            "weld straight",
            "silencer",
            "throttle",
            "y-type",
            "tee fitting",
        ],
    ),
    (
        "stainless-steel-instrumentation-tubing",
        ["ba tube", "precision tube", "coil tube", "tube clamp"],
    ),
    ("stainless-steel-cast-fittings", ["investment cast"]),
]


def category_slug(title: str) -> str:
    t = title.lower()
    for slug, keys in CATEGORY_RULES:
        if any(k in t for k in keys):
            return slug
    return "stainless-steel-pipe-fittings"


def product_slug(title: str) -> str:
    s = title.lower().strip()
    s = re.sub(r"^ss\s+", "stainless steel ", s)
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    s = re.sub(r"^ss-", "stainless-steel-", s)
    if not s.startswith("stainless-steel-"):
        s = f"stainless-steel-{s}"
    # collapse accidental doubles
    s = re.sub(r"(?:stainless-steel-)+", "stainless-steel-", s)
    s = re.sub(r"-{2,}", "-", s).strip("-")
    return s[:90] or "product"


def pick_copy(title: str) -> dict:
    t = title.lower()
    for keys, copy in CATEGORY_COPY:
        if any(k in t for k in keys):
            return copy
    return DEFAULT


def esc(s: str) -> str:
    return s.replace("'", "''")


def main() -> None:
    files = sorted(PROD_DIR.glob("item-*.md"))
    used_slugs: dict[str, int] = {}
    for f in files:
        text = f.read_text(encoding="utf-8")
        m = re.search(r"^title:\s*'((?:''|[^'])*)'", text, re.M)
        if not m:
            continue
        title = m.group(1).replace("''", "'")
        base = product_slug(title)
        n = used_slugs.get(base, 0)
        used_slugs[base] = n + 1
        slug = base if n == 0 else f"{base}-{n + 1}"
        rewrite_file(f, forced_slug=slug)
    print(f"Rewrote {len(files)} products")


def rewrite_file(path: Path, forced_slug: str | None = None) -> None:
    text = path.read_text(encoding="utf-8")
    m = re.search(r"^title:\s*'((?:''|[^'])*)'", text, re.M)
    if not m:
        return
    title = m.group(1).replace("''", "'")
    id_m = re.search(r"id:\s*(\d+)", text)
    img_m = re.search(r"imgCard:\s*'([^']+)'", text)
    if not id_m or not img_m:
        return
    idx = id_m.group(1)
    img = img_m.group(1)
    copy = pick_copy(title)
    shape = shape_hint(title)
    desc = esc(copy["desc"].format(title=title, shape=shape)[:160])
    intro = copy["intro"].format(title=title, shape=shape)
    long = copy["long"]
    bullets = "\n".join(
        f"  - title: '{esc(a)}'\n    subTitle: '{esc(b)}'" for a, b in copy["bullets"]
    )
    specs = "\n".join(
        f"  - title: '{esc(a)}'\n    subTitle: '{esc(b)}'" for a, b in copy["specs"]
    )
    table_rows = "\n".join(f"      - ['{esc(a)}', '{esc(b)}']" for a, b in copy["specs"])

    cat = category_slug(title)
    slug = forced_slug or product_slug(title)
    content = f"""---
title: '{esc(title)}'
description: '{desc}'
category: '{cat}'
slug: '{slug}'
main:
  id: {idx}
  content: |
    {intro}
  imgCard: '{img}'
  imgMain: '{img}'
  imgAlt: '{esc(title)} - FerruleX stainless steel fittings'
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
  title: '{esc(title)}'
  subTitle: |
    {long}
  btnTitle: 'Request a factory quote'
  btnURL: '/contact'
descriptionList:
{bullets}
specificationsLeft:
{specs}
tableData:
  - feature: ['Specification', 'Value']
    description:
{table_rows}
blueprints:
  first: '@/images/blueprint-1.avif'
  second: '@/images/blueprint-2.avif'
---
"""
    path.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    main()
