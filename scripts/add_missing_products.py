# -*- coding: utf-8 -*-
"""Add catalog products missing from the EN collection: check valves, filter, throttle, cast fittings."""
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "src" / "content" / "products" / "en"

ITEMS = [
    {
        "file": "item-085-compression-check-valve.md",
        "id": 85,
        "title": "Compression Check Valve",
        "category": "stainless-steel-check-valves",
        "slug": "stainless-steel-compression-check-valve",
        "img": "@/images/products/p20-85-compression-check-valve.jpg",
        "description": "Compression Check Valve: stainless steel check valve, double-ferrule ends, about 2000 PSI. SS304/316. FerruleX factory RFQ. Stocked sizes ship fast.",
        "content": "A compression-end stainless steel check valve stops reverse flow on instrument tubing without a separate threaded adapter. FerruleX SS304, SS316 and SS316L bodies use double-ferrule ports for tube OD typically 3–16 mm and 1/8\"–1\", with cracking behavior confirmed on the RFQ. Working pressure in the catalog is about 2000 PSI (12 MPa) at ambient temperature. Analyzer panels, pump discharge and gauge legs use this pattern when the line is already compression tubing. Send tube OD, flow direction and media to FerruleX for a factory quote — common sizes are stocked. Install the arrow with the intended flow; a reversed check valve looks sealed and still blocks the process.",
        "sub": "Seat the tube fully before tightening each ferrule nut, the same way you would on a compression connector. Spring check valves are not shutoff valves — pair them with a ball valve when the line must be isolated for maintenance. FerruleX can match the check valve alloy to the neighboring ferrules on one RFQ.",
        "bullets": [
            ("Function", "One-way flow on compression tubing."),
            ("Ends", "Double-ferrule ports, OD 3–16 mm / 1/8\"–1\"."),
            ("Pressure", "About 2000 PSI / 12 MPa at ambient temperature."),
        ],
        "specs": [
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316 / SS316L"),
            ("Ends", "Compression (double ferrule)"),
            ("Size", "OD 3–16 mm / 1/8\"–1\""),
            ("Pressure", "~2000 PSI / 12 MPa"),
        ],
    },
    {
        "file": "item-086-female-check-valve.md",
        "id": 86,
        "title": "Female Thread Check Valve",
        "category": "stainless-steel-check-valves",
        "slug": "stainless-steel-female-thread-check-valve",
        "img": "@/images/products/p20-86-female-check-valve.jpg",
        "description": "Female Thread Check Valve: stainless steel check valve, NPT/G female ends, about 2000 PSI. SS304/316. FerruleX RFQ. Stocked sizes ship fast.",
        "content": "Female-thread stainless steel check valves protect pumps, gauges and process branches from backflow on NPT, G or metric ports. FerruleX machines SS304, SS316 and SS316L bodies for 1/8\"–1\" and M10–M24 threads. Catalog pressure is about 2000 PSI at room temperature. Use this style when both sides of the line are already threaded and a compression ferrule would only add joints. Arrow direction is part of the order — state it on the RFQ with thread standard and quantity. Stocked threads ship from the factory without a cart checkout. Do not use a check valve as the only isolation point; add a ball valve upstream if the element must come out.",
        "sub": "Thread sealant belongs on the male mating part, not inside the female check-valve bore, or it can foul the poppet. Confirm whether the line needs a soft seat or a metal seat before FerruleX releases the lot. Cracking pressure is quoted, not assumed from the catalog pressure rating.",
        "bullets": [
            ("Ends", "Female NPT, G, ZG(R) or metric."),
            ("Sizes", "1/8\"–1\" and M10–M24."),
            ("Role", "Reverse-flow protection on threaded manifolds."),
        ],
        "specs": [
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316 / SS316L"),
            ("Ends", "Female thread"),
            ("Threads", "NPT / G / ZG(R) / Metric"),
            ("Pressure", "~2000 PSI / 12 MPa"),
        ],
    },
    {
        "file": "item-087-female-split-check-valve.md",
        "id": 87,
        "title": "Female Split-Body Check Valve",
        "category": "stainless-steel-check-valves",
        "slug": "stainless-steel-female-split-check-valve",
        "img": "@/images/products/p20-87-female-split-check-valve.jpg",
        "description": "Female Split-Body Check Valve: serviceable stainless steel check valve, female threads, ~2000 PSI. SS304/316. FerruleX factory RFQ. Fast stock shipping.",
        "content": "A split-body female check valve lets maintenance open the housing and reach the spring and poppet without cutting the line out of the manifold. FerruleX supplies SS304, SS316 and SS316L versions with female NPT, G or metric ends from 1/8\" to 1\" and M10–M24. Pressure class in the factory catalog is about 2000 PSI at ambient temperature. Plants that flush or inspect check elements on a schedule prefer the split body over a sealed cartridge. Tell FerruleX the thread, alloy and whether you need spare internals on the same RFQ. Stocked sizes leave the factory quickly. Torque the body joint to the drawing after service or the split face will weep before the poppet does.",
        "sub": "Keep a spare seal kit with the valve if the media attacks elastomers. The split joint is a pressure boundary — do not substitute a random gasket. FerruleX marks flow direction on the body so reassembly after cleaning stays unambiguous.",
        "bullets": [
            ("Service", "Split body for spring and poppet access."),
            ("Ends", "Female thread, 1/8\"–1\" / M10–M24."),
            ("Pressure", "About 2000 PSI at ambient temperature."),
        ],
        "specs": [
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316 / SS316L"),
            ("Body", "Split / serviceable"),
            ("Ends", "Female thread"),
            ("Pressure", "~2000 PSI / 12 MPa"),
        ],
    },
    {
        "file": "item-088-inline-filter.md",
        "id": 88,
        "title": "Inline Filter",
        "category": "stainless-steel-check-valves",
        "slug": "stainless-steel-inline-filter",
        "img": "@/images/products/p20-88-inline-filter.jpg",
        "description": "Inline Filter: stainless steel instrumentation filter, compression or NPT/G ends, about 2000 PSI. SS304/316. FerruleX RFQ. Stocked sizes ship fast.",
        "content": "Inline stainless filters catch scale and seal debris before it reaches needle valves, analyzers and small orifices. FerruleX offers SS304, SS316 and SS316L housings with compression ends or male/female NPT and G threads. Tube and thread range in the catalog runs about OD 3–16 mm and 1/8\"–1\", plus M10–M24. Working pressure is about 2000 PSI at ambient temperature. Place the filter upstream of the component you are protecting and leave enough straight tube to pull the element. Mesh or micron rating is an RFQ field — the catalog pressure is not a filtration grade. FerruleX quotes stocked housings from the factory. A clogged element raises differential pressure; size the mesh for the smallest downstream orifice, not for the pipe ID.",
        "sub": "Write the clean differential-pressure limit into the maintenance procedure. FerruleX can supply compression and threaded ends on one purchase order when the panel mixes tube and NPT. Do not install the filter backwards relative to the marked flow if the element is directional.",
        "bullets": [
            ("Duty", "Protects valves and orifices from particles."),
            ("Ends", "Compression or NPT / G male and female."),
            ("Pressure", "About 2000 PSI; micron rating on RFQ."),
        ],
        "specs": [
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316 / SS316L"),
            ("Ends", "Compression / NPT / G"),
            ("Size", "OD 3–16 mm / 1/8\"–1\""),
            ("Pressure", "~2000 PSI / 12 MPa"),
        ],
    },
    {
        "file": "item-089-push-to-connect-throttle-valve.md",
        "id": 89,
        "title": "Push-to-Connect Throttle Valve",
        "category": "stainless-steel-tube-fittings",
        "slug": "stainless-steel-push-to-connect-throttle-valve",
        "img": "@/images/products/p20-89-push-throttle-valve.jpg",
        "description": "Push-to-Connect Throttle Valve: stainless flow control for air lines, OD 3–25 mm, about 3000 PSI. SS304/316. FerruleX RFQ. Stocked sizes ship fast.",
        "content": "Push-to-connect throttle valves meter air or light fluid on stainless tube without a separate needle-valve block. FerruleX SS304, SS316 and SS316L bodies accept tube OD 3–25 mm and 1/8\"–1\", with NPT, G or metric threads where the valve also ties into a port. Catalog pressure is about 3000 PSI and the stated temperature band is roughly −10 °C to 300 °C when the media will not freeze. Cylinder speed control and bleed circuits are the usual jobs. Send tube OD, thread and whether you need meter-out or a simple restrictor. FerruleX ships stocked sizes from the factory on RFQ. A throttle valve is not a shutoff — close a ball valve when the line must be isolated.",
        "sub": "Push the tube to the shoulder before you rely on the collet. Adjust the throttle with the line pressurized only if the knob is designed for live trimming; otherwise set it offline. FerruleX can pair these valves with push-to-connect elbows on the same size list.",
        "bullets": [
            ("Control", "Adjustable restrictor on push-in tube."),
            ("Sizes", "OD 3–25 mm / 1/8\"–1\"; NPT / G / metric."),
            ("Pressure", "About 3000 PSI on catalog air and light fluid service."),
        ],
        "specs": [
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316 / SS316L"),
            ("Ends", "Push-to-connect / thread"),
            ("Tube OD", "3–25 mm / 1/8\"–1\""),
            ("Pressure", "~3000 PSI"),
        ],
    },
    {
        "file": "item-090-investment-cast-straight.md",
        "id": 90,
        "title": "Investment Cast Straight Fitting",
        "category": "stainless-steel-cast-fittings",
        "slug": "stainless-steel-investment-cast-straight-fitting",
        "img": "@/images/products/p20-90-investment-cast-straight.jpg",
        "description": "Investment Cast Straight Fitting: stainless cast coupling, DN6–DN100, NPT/G threads. SS304/316. FerruleX factory RFQ. Stocked sizes ship fast for OEM.",
        "content": "Investment-cast straight fittings join stainless pipe in a line where a forged instrument union would be the wrong cost and pressure class. FerruleX casts SS304, SS316 and SS316L bodies from DN6 to DN100 (1/8\"–4\") with NPT, G or ZG(R) threads, including reducing combinations. Catalog working pressure for this cast family is about 250 PSI — do not substitute them for 1000 PSI compression fittings. Utility water, air headers and light process skids are the fit. Round-body and hex-style cast straights can be quoted together; say which outline the drawing uses. FerruleX reviews non-catalog reductions from a sketch. Stocked DN sizes ship faster than special patterns. Check the bore if the line is hygienic; as-cast ID is not a sanitary finish.",
        "sub": "Match the thread standard on both ends before the foundry cuts the pattern. FerruleX can ship cast elbows and tees on the same order so the alloy heat is consistent. These fittings are threaded or reducing castings, not double-ferrule tube connectors.",
        "bullets": [
            ("Range", "DN6–DN100 / 1/8\"–4\"."),
            ("Threads", "NPT, G or ZG(R); reducing on request."),
            ("Pressure", "About 250 PSI — utility cast class, not instrument HP."),
        ],
        "specs": [
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316 / SS316L"),
            ("Size", "DN6–DN100 / 1/8\"–4\""),
            ("Ends", "Thread / reducing"),
            ("Pressure", "~250 PSI"),
        ],
    },
    {
        "file": "item-091-investment-cast-union.md",
        "id": 91,
        "title": "Investment Cast Union",
        "category": "stainless-steel-cast-fittings",
        "slug": "stainless-steel-investment-cast-union",
        "img": "@/images/products/p20-91-investment-cast-union.jpg",
        "description": "Investment Cast Union: stainless cast union for breakable pipe joints, DN6–DN100. SS304/316. FerruleX RFQ. Stocked sizes ship fast. Export quotes only.",
        "content": "An investment-cast union gives a threaded stainless joint you can break without cutting pipe. FerruleX supplies SS304, SS316 and SS316L unions from DN6 to DN100 with NPT, G or ZG(R) threads, including reducing ends when the drawing calls for them. The cast family is rated about 250 PSI in the catalog, so it belongs on utility pipe rather than high-pressure instrument tube. Use it where pumps, strainers or spool pieces must come out. Seat style and gasket are part of the RFQ — do not assume a metal seat. FerruleX quotes stocked sizes from the factory. Union nuts need room for a wrench; call out insulation thickness if the joint sits inside lagging.",
        "sub": "Replace the union gasket when you open the joint; reused gaskets are a common leak after the first service. FerruleX can match cast unions to cast elbows on one material certificate. Pressure class stays at the cast rating even if the adjoining pipe is heavier.",
        "bullets": [
            ("Function", "Breakable threaded joint for spool removal."),
            ("Size", "DN6–DN100 with NPT / G / ZG(R)."),
            ("Class", "About 250 PSI cast rating."),
        ],
        "specs": [
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316 / SS316L"),
            ("Type", "Investment cast union"),
            ("Size", "DN6–DN100"),
            ("Pressure", "~250 PSI"),
        ],
    },
    {
        "file": "item-092-investment-cast-cap.md",
        "id": 92,
        "title": "Investment Cast Cap",
        "category": "stainless-steel-cast-fittings",
        "slug": "stainless-steel-investment-cast-cap",
        "img": "@/images/products/p20-92-investment-cast-cap.jpg",
        "description": "Investment Cast Cap: stainless cap for unused ports, thread or compression ends. SS304/316. FerruleX factory RFQ. Stocked sizes ship fast for export.",
        "content": "Investment-cast caps close unused stainless ports on manifolds and pipe ends. FerruleX offers SS304, SS316 and SS316L caps with compression ends or male/female NPT and G threads. Instrument-port sizes in the catalog run about OD 3–16 mm and 1/8\"–1\", plus M10–M24; larger cast caps follow the DN6–DN100 family when the RFQ says so. Pressure depends on the end style — threaded cast caps in the silencer/cast section are about 250 PSI, while compression blanking follows the fitting rating you specify. Say which. Future tie-in points and hydrostatic test blanks are typical uses. FerruleX ships stocked caps with the rest of the fitting list. A cap is not a plug substitute if the port needs a hex drive from the inside — order the hex plug when that is the case.",
        "sub": "Mark capped branches on the P&ID so operators do not treat them as live nozzles. FerruleX can bag caps with the mating elbows so site crews are not hunting thread standards. Confirm whether the cap must be seal-welded later; a cast thread cap is removable.",
        "bullets": [
            ("Duty", "Blanks unused threads and tube ends."),
            ("Ends", "Compression or NPT / G, size on RFQ."),
            ("Alloy", "SS304 / SS316 / SS316L."),
        ],
        "specs": [
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316 / SS316L"),
            ("Type", "Investment cast cap"),
            ("Ends", "Thread / compression"),
            ("Order", "Factory RFQ"),
        ],
    },
]


def esc(s: str) -> str:
    return s.replace("'", "''")


def render(item: dict) -> str:
    bullets = "\n".join(
        f"  - title: '{esc(a)}'\n    subTitle: '{esc(b)}'" for a, b in item["bullets"]
    )
    specs = "\n".join(
        f"  - title: '{esc(a)}'\n    subTitle: '{esc(b)}'" for a, b in item["specs"]
    )
    rows = "\n".join(f"      - ['{esc(a)}', '{esc(b)}']" for a, b in item["specs"])
    return f"""---
title: '{esc(item["title"])}'
description: '{esc(item["description"])}'
category: '{item["category"]}'
slug: '{item["slug"]}'
main:
  id: {item["id"]}
  content: |
    {item["content"]}
  imgCard: '{item["img"]}'
  imgMain: '{item["img"]}'
  imgAlt: '{esc(item["title"])} — FerruleX stainless steel fittings'
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
  title: '{esc(item["title"])}'
  subTitle: |
    {item["sub"]}
  btnTitle: 'Request a factory quote'
  btnURL: '/contact'
descriptionList:
{bullets}
specificationsLeft:
{specs}
tableData:
  - feature: ['Specification', 'Value']
    description:
{rows}
blueprints:
  first: '@/images/blueprint-1.avif'
  second: '@/images/blueprint-2.avif'
---
"""


def main() -> None:
    for item in ITEMS:
        n = len(item["description"])
        print(f"{item['id']} desc {n}")
        if not 140 <= n <= 165:
            raise SystemExit(f"bad desc length {item['id']}: {n}")
        path = OUT / item["file"]
        path.write_text(render(item), encoding="utf-8")
    print(f"wrote {len(ITEMS)}")


if __name__ == "__main__":
    main()
