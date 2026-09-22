# -*- coding: utf-8 -*-
"""Generate unique EN product copy dict, then write rewrite_product_copy_v2.py and run it."""
from __future__ import annotations

import json
import re
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROD = ROOT / "src" / "content" / "products" / "en"
OUT = ROOT / "scripts" / "rewrite_product_copy_v2.py"

# Product-specific angles (unique per SKU). Keys match main.id.
# Fields feed carefully varied prose — not shared category templates.
FACTS = {
    1: dict(
        kw="corrugated stainless steel hose",
        angle="male/female NPT, G or metric thread ends for flexible instrument and utility jumps",
        sizes="OD Φ6–Φ100",
        mat="SS304 / SS316",
        ends="male or female thread",
        use="vibration isolation, thermal expansion and tight routing in HVAC, petrochemical and OEM panels",
        bullet=[
            ("Ends", "Male/female thread in NPT, G, ZG(R) or metric."),
            ("OD range", "Φ6–Φ100 corrugated stainless steel hose."),
            ("Service", "Air, water, steam and light process media with RFQ confirmation."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316"),
            ("Hose OD", "Φ6–Φ100"),
            ("Ends", "Male/female thread"),
            ("Order mode", "Factory RFQ"),
        ],
    ),
    2: dict(
        kw="corrugated stainless steel hose",
        angle="flanged ends for larger process and utility connections needing gasketed joints",
        sizes="OD Φ6–Φ100",
        mat="SS304 / SS316",
        ends="flange",
        use="plant piping, heat transfer loops and equipment skids where flange standards are preferred",
        bullet=[
            ("Ends", "Flanged corrugated hose for bolted process joints."),
            ("Materials", "SS304 or SS316 bellows and fittings."),
            ("OEM", "Flange drill pattern and length quoted from your RFQ."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316"),
            ("Hose OD", "Φ6–Φ100"),
            ("Ends", "Flange"),
            ("Customization", "Length and flange facing on RFQ"),
        ],
    ),
    3: dict(
        kw="corrugated stainless steel hose",
        angle="flanged expansion joint geometry that absorbs axial and lateral pipe movement",
        sizes="OD Φ6–Φ100",
        mat="SS304 / SS316",
        ends="flange (compensator style)",
        use="building services, power and petrochemical lines that need thermal compensation",
        bullet=[
            ("Function", "Expansion joint for thermal and settlement movement."),
            ("Sizes", "Corrugated OD typically Φ6–Φ100."),
            ("Materials", "SS304 / SS316 with flanged ends."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316"),
            ("Size range", "OD Φ6–Φ100"),
            ("Type", "Flanged expansion joint"),
            ("Lead time", "Stocked + custom RFQ"),
        ],
    ),
    4: dict(
        kw="corrugated stainless steel hose",
        angle="tri-clamp sanitary ends for hygienic and clean-process flexible links",
        sizes="OD Φ6–Φ100",
        mat="SS304 / SS316",
        ends="tri-clamp",
        use="food, beverage, biotech and clean utility jumps needing quick clamp change-outs",
        bullet=[
            ("Ends", "Tri-clamp ferrules for sanitary clamp assemblies."),
            ("Hygiene", "Smooth corrugated SS304/SS316 hose for clean routing."),
            ("RFQ", "Specify clamp size, length and media for factory quote."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316"),
            ("Hose OD", "Φ6–Φ100"),
            ("Ends", "Tri-clamp"),
            ("Industry", "Sanitary / clean process"),
        ],
    ),
    5: dict(
        kw="corrugated stainless steel hose",
        angle="quick-coupling ends for tool-free hose swaps on test and utility benches",
        sizes="OD Φ6–Φ100",
        mat="SS304 / SS316",
        ends="quick-coupling",
        use="maintenance bypasses, portable equipment and OEM test stands",
        bullet=[
            ("Ends", "Quick-coupling for rapid hose connect/disconnect."),
            ("Materials", "SS304 / SS316 corrugated hose."),
            ("Sizes", "OD Φ6–Φ100; coupling style confirmed on RFQ."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316"),
            ("Hose OD", "Φ6–Φ100"),
            ("Ends", "Quick-coupling"),
            ("Order mode", "Factory RFQ"),
        ],
    ),
    6: dict(
        kw="corrugated stainless steel hose",
        angle="KF / ISO vacuum flanges for flexible vacuum and clean-gas lines",
        sizes="KF16 / KF25 / KF40 / KF50 and ISO63 / ISO80 / ISO100",
        mat="SS304",
        ends="KF / ISO vacuum",
        use="vacuum chambers, analytical instruments and semiconductor support utilities",
        bullet=[
            ("Vacuum ends", "KF16–KF50 and ISO63–ISO100 flexible hose."),
            ("Material", "SS304 corrugated vacuum hose."),
            ("Use", "Vacuum and clean-gas flexible links — RFQ length and flange."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304"),
            ("KF sizes", "KF16 / 25 / 40 / 50"),
            ("ISO sizes", "ISO63 / 80 / 100"),
            ("Type", "Flexible vacuum corrugated hose"),
        ],
    ),
    7: dict(
        kw="stainless steel compression fittings",
        angle="double-ferrule tube-to-male thread connector for ports, gauges and manifolds",
        sizes="tube OD 3–25 mm / 1/8\"–1\"; threads M5–M24, NPT, G, ZG(R)",
        mat="SS316 / SS316L / SS304",
        ends="compression × male thread",
        use="instrumentation panels and process skids needing leak-tight tube entry to male ports",
        bullet=[
            ("Seal", "Double ferrule bite on annealed stainless tubing."),
            ("Threads", "NPT, G, ZG(R) and metric male ends."),
            ("Pressure", "~1000 PSI standard; HP series up to ~4500 PSI."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS316 / SS316L / SS304"),
            ("Tube OD", "3–25 mm / 1/8\"–1\""),
            ("Threads", "NPT / G / ZG(R) / Metric"),
            ("Pressure", "~1000 PSI (HP ~4500 PSI)"),
        ],
    ),
    8: dict(
        kw="stainless steel compression fittings",
        angle="double-ferrule tube-to-female connector for gauges, valves and female-threaded blocks",
        sizes="tube OD 3–25 mm / 1/8\"–1\"; female NPT/G/metric",
        mat="SS316 / SS316L / SS304",
        ends="compression × female thread",
        use="sampling lines and instrument hook-ups where female NPT or G ports dominate",
        bullet=[
            ("Pattern", "Tube OD to female thread in one body."),
            ("Sizes", "Metric and fractional tube OD with mixed thread options."),
            ("Factory", "FerruleX stocked sizes support fast RFQ delivery."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS316 / SS316L / SS304"),
            ("Tube OD", "3–25 mm / 1/8\"–1\""),
            ("Female threads", "NPT / G / Metric"),
            ("Pressure", "~1000 PSI standard"),
        ],
    ),
    9: dict(
        kw="stainless steel compression fittings",
        angle="straight double-ferrule union for same-size tube-to-tube joins",
        sizes="OD 3–25 mm / 1/8\"–1\"",
        mat="SS316 / SS316L / SS304",
        ends="compression × compression",
        use="inline repairs, skid tubing and instrumentation runs without welding",
        bullet=[
            ("Connection", "Equal-size double ferrule union."),
            ("Install", "No flaring; insert tube to shoulder and tighten nut."),
            ("Materials", "SS304 / SS316 / SS316L bodies and ferrules."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS316 / SS316L / SS304"),
            ("Tube OD", "3–25 mm / 1/8\"–1\""),
            ("Type", "Straight compression union"),
            ("Pressure", "~1000 PSI (HP available)"),
        ],
    ),
    10: dict(
        kw="stainless steel compression fittings",
        angle="reducing double-ferrule union bridging unequal tube OD on one axis",
        sizes="within OD 3–25 mm / 1/8\"–1\" reducing pairs",
        mat="SS316 / SS316L / SS304",
        ends="compression reducing",
        use="panel redesigns and OEM assemblies mixing metric and fractional tubing",
        bullet=[
            ("Function", "Reduces between two tube OD sizes."),
            ("Seal", "Double ferrule on each side."),
            ("RFQ", "List both tube OD values for FerruleX pricing."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS316 / SS316L / SS304"),
            ("Size range", "OD 3–25 mm / 1/8\"–1\""),
            ("Type", "Reducing compression union"),
            ("Pressure", "~1000 PSI"),
        ],
    ),
    11: dict(
        kw="stainless steel compression fittings",
        angle="90° male elbow combining double-ferrule tube end with male thread",
        sizes="OD 3–25 mm / 1/8\"–1\"; NPT/G/metric male",
        mat="SS316 / SS316L / SS304",
        ends="compression × male elbow",
        use="tight panel corners where straight connectors cannot clear obstacles",
        bullet=[
            ("Geometry", "90° elbow saves space at male ports."),
            ("Threads", "NPT, G, ZG(R) or metric male."),
            ("Pressure", "Standard ~1000 PSI instrumentation class."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS316 / SS316L / SS304"),
            ("Tube OD", "3–25 mm / 1/8\"–1\""),
            ("Pattern", "Male elbow"),
            ("Threads", "NPT / G / Metric"),
        ],
    ),
    12: dict(
        kw="stainless steel compression fittings",
        angle="90° union elbow for tube-to-tube turns with double ferrules both ends",
        sizes="OD 3–25 mm / 1/8\"–1\"",
        mat="SS316 / SS316L / SS304",
        ends="compression elbow union",
        use="compact instrument tubing layouts and OEM cabinets",
        bullet=[
            ("Pattern", "Equal or reducing elbow unions available."),
            ("Seal", "Double-ferrule metal bite both ends."),
            ("Stock", "Common OD pairs stocked for fast factory shipment."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS316 / SS316L / SS304"),
            ("Tube OD", "3–25 mm / 1/8\"–1\""),
            ("Type", "Compression union elbow"),
            ("Pressure", "~1000 PSI"),
        ],
    ),
    13: dict(
        kw="stainless steel compression fittings",
        angle="tee body mixing compression tube ports with optional male/female thread branch",
        sizes="OD 3–25 mm / 1/8\"–1\"",
        mat="SS316 / SS316L / SS304",
        ends="compression male/female tee",
        use="branching gauge lines, purge taps and sample take-offs",
        bullet=[
            ("Ports", "Run and branch combinations for instrumentation."),
            ("Materials", "SS304 / SS316 / SS316L."),
            ("RFQ", "Specify run OD, branch style and thread."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS316 / SS316L / SS304"),
            ("Tube OD", "3–25 mm / 1/8\"–1\""),
            ("Type", "Compression male/female tee"),
            ("Pressure", "~1000 PSI"),
        ],
    ),
    14: dict(
        kw="stainless steel compression fittings",
        angle="reducing tee that branches a smaller take-off from a larger tube run",
        sizes="within OD 3–25 mm / 1/8\"–1\"",
        mat="SS316 / SS316L / SS304",
        ends="reducing compression tee",
        use="instrument taps on process tubing without full-size branch fittings",
        bullet=[
            ("Function", "Reducing branch for gauge or sample lines."),
            ("Seal", "Double ferrule on all tube ports."),
            ("Factory", "FerruleX quotes mixed OD combinations from stock or OEM."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS316 / SS316L / SS304"),
            ("Size range", "OD 3–25 mm / 1/8\"–1\""),
            ("Type", "Reducing compression tee"),
            ("Pressure", "~1000 PSI"),
        ],
    ),
    15: dict(
        kw="instrumentation fittings",
        angle="cylinder-style connector for compact tube entry on cylinders and specialty ports",
        sizes="compression tube OD / thread per RFQ",
        mat="SS316 / SS316L / SS304",
        ends="cylinder / specialty compression",
        use="gas cylinder adapters and OEM equipment with limited wrench clearance",
        bullet=[
            ("Form", "Cylinder-style body for specialty ports."),
            ("Materials", "SS304 / SS316 / SS316L."),
            ("Ordering", "Send port drawing or size code with RFQ."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS316 / SS316L / SS304"),
            ("Series", "Compression instrumentation"),
            ("Type", "Cylinder connector"),
            ("Order mode", "Factory RFQ"),
        ],
    ),
    16: dict(
        kw="stainless steel compression fittings",
        angle="bulkhead union that passes double-ferrule tubing through a panel wall",
        sizes="OD 3–25 mm / 1/8\"–1\"",
        mat="SS316 / SS316L / SS304",
        ends="compression bulkhead",
        use="enclosure walls, skid panels and control cabinets needing sealed pass-throughs",
        bullet=[
            ("Mounting", "Bulkhead locknut for panel thickness ranges."),
            ("Seal", "Double ferrule both sides of the wall."),
            ("Pressure", "~1000 PSI class; confirm panel thickness on RFQ."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS316 / SS316L / SS304"),
            ("Tube OD", "3–25 mm / 1/8\"–1\""),
            ("Type", "Compression bulkhead union"),
            ("Pressure", "~1000 PSI"),
        ],
    ),
    17: dict(
        kw="stainless steel compression fittings",
        angle="hybrid straight and bulkhead connectors combining compression and quick-screw styles",
        sizes="compression OD 3–25 mm; quick-screw OD 4–16 mm",
        mat="SS316 / SS316L / SS304",
        ends="compression / quick-screw straight & bulkhead",
        use="mixed pneumatic and instrument tubing on the same panel",
        bullet=[
            ("Styles", "Straight and bulkhead in compression or quick-screw."),
            ("Sizes", "Match tube OD to the connection style you select."),
            ("Factory", "FerruleX stocks common hybrids for export RFQs."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS316 / SS316L / SS304"),
            ("Compression OD", "3–25 mm / 1/8\"–1\""),
            ("Quick-screw OD", "4–16 mm / 1/8\"–1/2\""),
            ("Pressure", "~1000 PSI"),
        ],
    ),
    18: dict(
        kw="stainless steel compression fittings",
        angle="four-port compression cross for intersecting instrument lines",
        sizes="OD 3–25 mm / 1/8\"–1\"",
        mat="SS316 / SS316L / SS304",
        ends="compression cross",
        use="complex manifolds, calibration benches and multi-leg sample systems",
        bullet=[
            ("Ports", "Four equal or reducing compression ports."),
            ("Seal", "Double ferrule on each tube end."),
            ("RFQ", "Confirm all four OD values before ordering."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS316 / SS316L / SS304"),
            ("Tube OD", "3–25 mm / 1/8\"–1\""),
            ("Type", "Compression cross"),
            ("Pressure", "~1000 PSI"),
        ],
    ),
    19: dict(
        kw="stainless steel compression fittings",
        angle="ground-finish tube-to-male connector with smoother exterior for clean panels",
        sizes="OD 3–25 mm / 1/8\"–1\"",
        mat="SS316 / SS316L / SS304",
        ends="ground finish × male thread",
        use="visible OEM equipment and labs preferring refined surface appearance",
        bullet=[
            ("Finish", "Ground exterior for cleaner visual presentation."),
            ("Function", "Double-ferrule tube to male thread."),
            ("Materials", "SS304 / SS316 / SS316L."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS316 / SS316L / SS304"),
            ("Tube OD", "3–25 mm / 1/8\"–1\""),
            ("Finish", "Ground"),
            ("Threads", "NPT / G / Metric"),
        ],
    ),
    20: dict(
        kw="stainless steel compression fittings",
        angle="ground-finish reducing union for neat size transitions on displayable tubing",
        sizes="within OD 3–25 mm / 1/8\"–1\"",
        mat="SS316 / SS316L / SS304",
        ends="ground finish reducing",
        use="medical device OEM, analytical benches and polished skid aesthetics",
        bullet=[
            ("Finish", "Ground body reduces machining marks."),
            ("Function", "Reducing double-ferrule union."),
            ("RFQ", "Provide both tube OD for FerruleX quote."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS316 / SS316L / SS304"),
            ("Size range", "OD 3–25 mm / 1/8\"–1\""),
            ("Finish", "Ground"),
            ("Type", "Reducing union"),
        ],
    ),
    21: dict(
        kw="stainless steel compression fittings",
        angle="ground-finish straight union for equal tube joins with refined exterior",
        sizes="OD 3–25 mm / 1/8\"–1\"",
        mat="SS316 / SS316L / SS304",
        ends="ground finish straight union",
        use="export OEM panels where fittings remain visible after install",
        bullet=[
            ("Pattern", "Equal-size ground-finish union."),
            ("Seal", "Double ferrule instrumentation seal."),
            ("Stock", "Common OD stocked at FerruleX factory."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS316 / SS316L / SS304"),
            ("Tube OD", "3–25 mm / 1/8\"–1\""),
            ("Finish", "Ground"),
            ("Type", "Straight union"),
        ],
    ),
    22: dict(
        kw="stainless steel compression fittings",
        angle="ground-finish male elbow for space-saving 90° tube-to-thread turns",
        sizes="OD 3–25 mm / 1/8\"–1\"",
        mat="SS316 / SS316L / SS304",
        ends="ground finish male elbow",
        use="compact cabinets needing clean-looking elbows at male ports",
        bullet=[
            ("Geometry", "90° male elbow with ground exterior."),
            ("Threads", "NPT / G / metric male options."),
            ("Pressure", "~1000 PSI instrumentation duty."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS316 / SS316L / SS304"),
            ("Tube OD", "3–25 mm / 1/8\"–1\""),
            ("Finish", "Ground"),
            ("Pattern", "Male elbow"),
        ],
    ),
    23: dict(
        kw="stainless steel compression fittings",
        angle="forged compression elbow for higher mechanical robustness on instrument turns",
        sizes="OD 3–25 mm / 1/8\"–1\"",
        mat="SS316 / SS316L / SS304",
        ends="forged compression elbow",
        use="marine, petrochemical and mobile equipment exposed to vibration",
        bullet=[
            ("Body", "Forged elbow blank for strength."),
            ("Seal", "Double-ferrule tube ends."),
            ("Materials", "SS304 / SS316 / SS316L."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS316 / SS316L / SS304"),
            ("Tube OD", "3–25 mm / 1/8\"–1\""),
            ("Body", "Forged"),
            ("Pressure", "~1000 PSI (HP series available)"),
        ],
    ),
    24: dict(
        kw="stainless steel compression fittings",
        angle="forged compression tee for durable three-port branching",
        sizes="OD 3–25 mm / 1/8\"–1\"",
        mat="SS316 / SS316L / SS304",
        ends="forged compression tee",
        use="high-cycle skids and outdoor instrument trees needing forged bodies",
        bullet=[
            ("Body", "Forged tee for impact and vibration resistance."),
            ("Ports", "Three compression tube ports."),
            ("RFQ", "Equal or reducing branch OD listed on quote."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS316 / SS316L / SS304"),
            ("Tube OD", "3–25 mm / 1/8\"–1\""),
            ("Body", "Forged"),
            ("Type", "Compression tee"),
        ],
    ),
    25: dict(
        kw="stainless steel compression fittings",
        angle="forged reducing tee combining strength with unequal branch sizing",
        sizes="within OD 3–25 mm / 1/8\"–1\"",
        mat="SS316 / SS316L / SS304",
        ends="forged reducing tee",
        use="rugged sample taps and gauge trees on vibrating equipment",
        bullet=[
            ("Function", "Forged reducing branch off main run."),
            ("Seal", "Double ferrule on tube ports."),
            ("Factory", "FerruleX OEM machining for special OD pairs."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS316 / SS316L / SS304"),
            ("Size range", "OD 3–25 mm / 1/8\"–1\""),
            ("Body", "Forged"),
            ("Type", "Reducing tee"),
        ],
    ),
    26: dict(
        kw="stainless steel compression fittings",
        angle="forged compression cross for four-way branching under tougher duty",
        sizes="OD 3–25 mm / 1/8\"–1\"",
        mat="SS316 / SS316L / SS304",
        ends="forged compression cross",
        use="mobile test carts and offshore instrument manifolds",
        bullet=[
            ("Body", "Forged four-port cross."),
            ("Seal", "Double-ferrule instrumentation seal."),
            ("Pressure", "~1000 PSI class; HP on request."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS316 / SS316L / SS304"),
            ("Tube OD", "3–25 mm / 1/8\"–1\""),
            ("Body", "Forged"),
            ("Type", "Compression cross"),
        ],
    ),
    27: dict(
        kw="stainless steel tube fittings",
        angle="push-in quick-screw fittings for rapid tube install on air and water lines",
        sizes="OD 4–16 mm / 1/8\"–1/2\"; ~1000 PSI",
        mat="SS304 / SS316 / SS316L",
        ends="push-in quick-screw",
        use="pneumatic cabinets, cooling water and OEM machines needing fast tube changes",
        bullet=[
            ("Install", "Insert tube, seat fully, tighten nut — no flare tool."),
            ("Sizes", "OD 4–16 mm / 1/8\"–1/2\" typical."),
            ("Materials", "SS304 / SS316 for corrosion resistance."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316 / SS316L"),
            ("Tube OD", "4–16 mm / 1/8\"–1/2\""),
            ("Pressure", "~1000 PSI"),
            ("Type", "Push-in quick-screw"),
        ],
    ),
    28: dict(
        kw="stainless steel tube fittings",
        angle="quick-screw straight connector from tube OD to male or female thread",
        sizes="OD 4–16 mm / 1/8\"–1/2\"",
        mat="SS304 / SS316 / SS316L",
        ends="quick-screw × thread",
        use="plant air drops and light fluid lines where speed beats welded joints",
        bullet=[
            ("Pattern", "Straight body for low pressure drop."),
            ("Threads", "NPT, G or metric options."),
            ("Pressure", "~1000 PSI working class."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316 / SS316L"),
            ("Tube OD", "4–16 mm / 1/8\"–1/2\""),
            ("Type", "Quick-screw straight"),
            ("Pressure", "~1000 PSI"),
        ],
    ),
    29: dict(
        kw="stainless steel tube fittings",
        angle="quick-screw female connector mating tube to female-threaded ports",
        sizes="OD 4–16 mm / 1/8\"–1/2\"",
        mat="SS304 / SS316 / SS316L",
        ends="quick-screw × female",
        use="valve manifolds and cylinders with female NPT/G ports",
        bullet=[
            ("Ends", "Tube quick-screw to female thread."),
            ("Sizes", "Metric and fractional tube OD."),
            ("Factory", "Stocked common sizes for FerruleX RFQ shipping."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316 / SS316L"),
            ("Tube OD", "4–16 mm / 1/8\"–1/2\""),
            ("Female threads", "NPT / G / Metric"),
            ("Pressure", "~1000 PSI"),
        ],
    ),
    30: dict(
        kw="stainless steel tube fittings",
        angle="quick-screw straight union for same-size tube-to-tube joins without welding",
        sizes="OD 4–16 mm / 1/8\"–1/2\"",
        mat="SS304 / SS316 / SS316L",
        ends="quick-screw union",
        use="inline repairs on pneumatic and water tubing",
        bullet=[
            ("Connection", "Equal-size quick-screw union."),
            ("Install", "Push-and-tighten on both tube ends."),
            ("Materials", "SS304 / SS316 / SS316L."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316 / SS316L"),
            ("Tube OD", "4–16 mm / 1/8\"–1/2\""),
            ("Type", "Quick-screw straight union"),
            ("Pressure", "~1000 PSI"),
        ],
    ),
    31: dict(
        kw="stainless steel tube fittings",
        angle="quick-screw elbow routing tube around tight corners to threaded ports",
        sizes="OD 4–16 mm / 1/8\"–1/2\"",
        mat="SS304 / SS316 / SS316L",
        ends="quick-screw elbow",
        use="crowded OEM cabinets and machine sidewalls",
        bullet=[
            ("Geometry", "90° elbow reduces bend stress on plastic or soft tube."),
            ("Sizes", "OD 4–16 mm with NPT/G/metric threads."),
            ("Duty", "~1000 PSI air and water class."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316 / SS316L"),
            ("Tube OD", "4–16 mm / 1/8\"–1/2\""),
            ("Pattern", "Elbow"),
            ("Pressure", "~1000 PSI"),
        ],
    ),
    32: dict(
        kw="stainless steel tube fittings",
        angle="quick-screw tee branching a third leg from pneumatic or water tubing",
        sizes="OD 4–16 mm / 1/8\"–1/2\"",
        mat="SS304 / SS316 / SS316L",
        ends="quick-screw tee",
        use="multi-actuator air circuits and shared cooling feeds",
        bullet=[
            ("Ports", "Three-way quick-screw branching."),
            ("Materials", "SS304 / SS316 corrosion resistance."),
            ("RFQ", "List run and branch OD with thread needs."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316 / SS316L"),
            ("Tube OD", "4–16 mm / 1/8\"–1/2\""),
            ("Type", "Quick-screw tee"),
            ("Pressure", "~1000 PSI"),
        ],
    ),
    33: dict(
        kw="stainless steel tube fittings",
        angle="quick-screw bulkhead connector for panel pass-through on air and light fluid lines",
        sizes="OD 4–16 mm / 1/8\"–1/2\"; ~1000 PSI",
        mat="SS304 / SS316 / SS316L",
        ends="quick-screw bulkhead",
        use="enclosure walls and skid panels needing sealed tube pass-throughs",
        bullet=[
            ("Mounting", "Bulkhead nut locks through panel thickness."),
            ("Sizes", "OD 4–16 mm / 1/8\"–1/2\" quick-screw."),
            ("Duty", "~1000 PSI pneumatic/water class."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316 / SS316L"),
            ("Tube OD", "4–16 mm / 1/8\"–1/2\""),
            ("Type", "Quick-screw bulkhead"),
            ("Pressure", "~1000 PSI"),
        ],
    ),
    34: dict(
        kw="stainless steel tube fittings",
        angle="barb hose connector gripping soft hose with threaded equipment ports",
        sizes="1/8\"–1\" / M5–M24 threads; ~3000 PSI class depending on hose",
        mat="SS304 / SS316 / copper options",
        ends="barb × thread",
        use="flexible hose drops for cooling, washdown and light process fluids",
        bullet=[
            ("Ends", "Barb stem to NPT, G, ZG(R) or metric thread."),
            ("Sizes", "Typically 1/8\"–1\" with M5–M24 threads."),
            ("Note", "Confirm hose ID and clamp style on RFQ."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316"),
            ("Thread range", "1/8\"–1\" / M5–M24"),
            ("Type", "Barb hose connector"),
            ("Pressure", "Up to ~3000 PSI (hose limited)"),
        ],
    ),
    35: dict(
        kw="stainless steel compression fittings",
        angle="three-piece compression plug kit blanking unused double-ferrule ports",
        sizes="matched to compression OD series 3–25 mm / 1/8\"–1\"",
        mat="SS316 / SS316L / SS304",
        ends="compression plug kit",
        use="manifold commissioning, spare ports and temporary line isolation",
        bullet=[
            ("Kit", "Nut, ferrules and plug body as a set."),
            ("Fit", "Matches FerruleX compression OD series."),
            ("Use", "Seal unused ports without welding."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS316 / SS316L / SS304"),
            ("Compatibility", "Compression OD 3–25 mm / 1/8\"–1\""),
            ("Type", "3-piece plug kit"),
            ("Order mode", "Factory RFQ"),
        ],
    ),
    36: dict(
        kw="stainless steel compression fittings",
        angle="compression plug insert that seats inside the fitting to blank a tube port",
        sizes="per compression OD",
        mat="SS316 / SS316L / SS304",
        ends="plug insert",
        use="service kits and field blanks when the full plug kit is not required",
        bullet=[
            ("Part", "Insert plug for double-ferrule ports."),
            ("Materials", "SS304 / SS316 / SS316L."),
            ("RFQ", "State tube OD or fitting code."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS316 / SS316L / SS304"),
            ("Type", "Compression plug insert"),
            ("Series", "Double ferrule"),
            ("Order mode", "Factory RFQ"),
        ],
    ),
    37: dict(
        kw="stainless steel pipe fittings",
        angle="hex socket plug sealing female NPT/G ports with internal hex drive",
        sizes="common NPT / G / metric plug sizes",
        mat="SS304 / SS316",
        ends="hex socket plug",
        use="manifolds and valve bodies where external wrench clearance is limited",
        bullet=[
            ("Drive", "Internal hex for recessed install."),
            ("Threads", "NPT, G or metric per RFQ."),
            ("Materials", "SS304 / SS316."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316"),
            ("Type", "Hex socket plug"),
            ("Threads", "NPT / G / Metric"),
            ("Order mode", "Factory RFQ"),
        ],
    ),
    38: dict(
        kw="stainless steel pipe fittings",
        angle="hex head plug for blanking female ports with external wrench flats",
        sizes="common NPT / G / metric",
        mat="SS304 / SS316",
        ends="hex head plug",
        use="process blocks, cylinders and test ports needing durable blanks",
        bullet=[
            ("Drive", "External hex for standard wrenches."),
            ("Seal", "Threaded plug for female ports."),
            ("Materials", "SS304 / SS316."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316"),
            ("Type", "Hex head plug"),
            ("Threads", "NPT / G / Metric"),
            ("Order mode", "Factory RFQ"),
        ],
    ),
    39: dict(
        kw="stainless steel pipe fittings",
        angle="flanged hex socket plug adding a sealing shoulder with internal hex drive",
        sizes="threaded plug series with flange face",
        mat="SS304 / SS316",
        ends="flanged hex socket plug",
        use="ports needing a positive stop and cleaner exterior after install",
        bullet=[
            ("Feature", "Flange shoulder plus internal hex."),
            ("Materials", "SS304 / SS316."),
            ("RFQ", "Thread size and flange OD if special."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316"),
            ("Type", "Flanged hex socket plug"),
            ("Threads", "NPT / G / Metric"),
            ("Order mode", "Factory RFQ"),
        ],
    ),
    40: dict(
        kw="stainless steel pipe fittings",
        angle="flanged hex head plug combining wrench flats with a sealing flange",
        sizes="threaded plug series",
        mat="SS304 / SS316",
        ends="flanged hex head plug",
        use="hydraulic and pneumatic blocks preferring flanged blanks",
        bullet=[
            ("Feature", "Hex head with flange stop."),
            ("Materials", "SS304 / SS316."),
            ("Stock", "Common threads stocked for fast FerruleX delivery."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316"),
            ("Type", "Flanged hex head plug"),
            ("Threads", "NPT / G / Metric"),
            ("Order mode", "Factory RFQ"),
        ],
    ),
    41: dict(
        kw="stainless steel pipe fittings",
        angle="square head plug for high-torque blanking of female threaded ports",
        sizes="common plug threads",
        mat="SS304 / SS316",
        ends="square head plug",
        use="heavy equipment and process valves where square drive is preferred",
        bullet=[
            ("Drive", "Square head for high seating torque."),
            ("Materials", "SS304 / SS316."),
            ("Use", "Permanent or semi-permanent port blanks."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316"),
            ("Type", "Square head plug"),
            ("Threads", "NPT / G / Metric"),
            ("Order mode", "Factory RFQ"),
        ],
    ),
    42: dict(
        kw="stainless steel pipe fittings",
        angle="male-female straight adapter converting thread standards or sizes inline",
        sizes="NPT / G / ZG(R) / metric combinations",
        mat="SS304 / SS316",
        ends="male × female straight",
        use="import equipment hook-ups mixing NPT and BSP/G threads",
        bullet=[
            ("Function", "Thread standard or size adapter."),
            ("Pattern", "Straight low-profile body."),
            ("RFQ", "List both thread codes for FerruleX."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316"),
            ("Type", "Male-female straight adapter"),
            ("Threads", "NPT / G / ZG(R) / Metric"),
            ("Order mode", "Factory RFQ"),
        ],
    ),
    43: dict(
        kw="stainless steel pipe fittings",
        angle="male-female elbow adapter turning 90° while changing thread gender or standard",
        sizes="NPT / G / metric mixes",
        mat="SS304 / SS316",
        ends="male × female elbow",
        use="tight machine frames needing both direction change and thread conversion",
        bullet=[
            ("Geometry", "90° adapter saves hose/tube bend radius."),
            ("Threads", "Mixed NPT/G/metric male-female pairs."),
            ("Materials", "SS304 / SS316."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316"),
            ("Type", "Male-female elbow adapter"),
            ("Threads", "NPT / G / Metric"),
            ("Order mode", "Factory RFQ"),
        ],
    ),
    44: dict(
        kw="stainless steel pipe fittings",
        angle="all-female threaded tee for branching threaded pipe and instrument lines",
        sizes="common NPT / G / metric tee sizes",
        mat="SS304 / SS316",
        ends="female threaded tee",
        use="air headers, water manifolds and gauge trees",
        bullet=[
            ("Ports", "Three female threaded ports."),
            ("Materials", "SS304 / SS316."),
            ("RFQ", "Equal or reducing branch sizes accepted."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316"),
            ("Type", "Female threaded tee"),
            ("Threads", "NPT / G / Metric"),
            ("Order mode", "Factory RFQ"),
        ],
    ),
    45: dict(
        kw="stainless steel pipe fittings",
        angle="weld straight connector for permanent tube or pipe joining by welding",
        sizes="per weld schedule / tube OD on RFQ",
        mat="SS304 / SS316",
        ends="weld × weld or weld × thread variants",
        use="process skids preferring permanent joints over demountable fittings",
        bullet=[
            ("Ends", "Weld prep for permanent installation."),
            ("Materials", "SS304 / SS316."),
            ("OEM", "Custom lengths and transitions from drawings."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316"),
            ("Type", "Weld straight connector"),
            ("Ends", "Weld (options per RFQ)"),
            ("Order mode", "Factory RFQ / OEM"),
        ],
    ),
    46: dict(
        kw="stainless steel ball valve",
        angle="straight-through compression-end ball valve for low pressure-drop shutoff",
        sizes="compression OD matched to tube; ~1000 PSI typical",
        mat="SS304 / SS316 / SS316L",
        ends="double-ferrule compression",
        use="instrumentation panels, pneumatic lines and process skids needing quick isolation",
        bullet=[
            ("Ends", "Straight compression (double ferrule) ports."),
            ("Action", "Quarter-turn ball shutoff with low Cv loss."),
            ("Pressure", "~1000 PSI standard; HP series available."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316 / SS316L"),
            ("Ends", "Compression"),
            ("Pattern", "Straight"),
            ("Pressure", "~1000 PSI (HP available)"),
        ],
    ),
    47: dict(
        kw="stainless steel ball valve",
        angle="angle compression ball valve for 90° shutoff in cramped panels",
        sizes="compression tube OD series; ~1000 PSI",
        mat="SS304 / SS316 / SS316L",
        ends="compression angle",
        use="wall-mounted instruments and corner routing on OEM skids",
        bullet=[
            ("Pattern", "Angle body replaces elbow + valve stack."),
            ("Ends", "Double-ferrule compression."),
            ("Materials", "SS304 / SS316 / SS316L."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316 / SS316L"),
            ("Ends", "Compression"),
            ("Pattern", "Angle"),
            ("Pressure", "~1000 PSI"),
        ],
    ),
    48: dict(
        kw="stainless steel ball valve",
        angle="3-way compression ball valve for diverting or mixing instrument flows",
        sizes="compression OD series; ~1000 PSI",
        mat="SS304 / SS316 / SS316L",
        ends="3-way compression",
        use="sample switching, calibration loops and dual-source selection",
        bullet=[
            ("Ports", "Three compression ends for L or T flow paths."),
            ("Control", "Quarter-turn diversion without breaking tube joints."),
            ("RFQ", "Confirm porting diagram with FerruleX."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316 / SS316L"),
            ("Ends", "Compression"),
            ("Pattern", "3-way"),
            ("Pressure", "~1000 PSI"),
        ],
    ),
    49: dict(
        kw="stainless steel ball valve",
        angle="straight quick-screw ball valve for fast tube connect shutoff on air lines",
        sizes="quick-screw OD 4–16 mm class; ~1000 PSI",
        mat="SS304 / SS316 / SS316L",
        ends="quick-screw straight",
        use="pneumatic OEM machines needing valve + tube fitting in one body",
        bullet=[
            ("Ends", "Quick-screw tube connections."),
            ("Pattern", "Straight flow path."),
            ("Duty", "Air and light fluid isolation."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316 / SS316L"),
            ("Ends", "Quick-screw"),
            ("Pattern", "Straight"),
            ("Pressure", "~1000 PSI"),
        ],
    ),
    50: dict(
        kw="stainless steel ball valve",
        angle="3-way quick-screw ball valve combining diversion with push-style tube ends",
        sizes="quick-screw OD range; ~1000 PSI",
        mat="SS304 / SS316 / SS316L",
        ends="3-way quick-screw",
        use="multi-circuit air panels and portable test equipment",
        bullet=[
            ("Ports", "Three quick-screw tube ends."),
            ("Function", "Divert or select flow paths quickly."),
            ("Materials", "SS304 / SS316 ball valve construction."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316 / SS316L"),
            ("Ends", "Quick-screw"),
            ("Pattern", "3-way"),
            ("Pressure", "~1000 PSI"),
        ],
    ),
    51: dict(
        kw="stainless steel ball valve",
        angle="female threaded ball valve for NPT/G pipe and manifold shutoff",
        sizes="common female NPT / G sizes; ~1000 PSI typical",
        mat="SS304 / SS316 / SS316L",
        ends="female thread",
        use="process headers, utility lines and equipment isolation",
        bullet=[
            ("Ends", "Female NPT, G or metric threads."),
            ("Action", "Full-port or reduced-port ball shutoff."),
            ("Factory", "FerruleX stocks common sizes for RFQ shipping."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316 / SS316L"),
            ("Ends", "Female thread"),
            ("Threads", "NPT / G / Metric"),
            ("Pressure", "~1000 PSI typical"),
        ],
    ),
    52: dict(
        kw="stainless steel ball valve",
        angle="angle female ball valve for 90° threaded shutoff without extra elbows",
        sizes="female thread series; ~1000 PSI",
        mat="SS304 / SS316 / SS316L",
        ends="angle female",
        use="wall outlets and compact machine frames",
        bullet=[
            ("Pattern", "Angle female body."),
            ("Threads", "NPT / G options."),
            ("Materials", "SS304 / SS316 / SS316L."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316 / SS316L"),
            ("Ends", "Female thread"),
            ("Pattern", "Angle"),
            ("Pressure", "~1000 PSI"),
        ],
    ),
    53: dict(
        kw="stainless steel ball valve",
        angle="female 3-way ball valve for threaded diversion on headers and test loops",
        sizes="female thread series",
        mat="SS304 / SS316 / SS316L",
        ends="female 3-way",
        use="bypass manifolds and dual-supply selection",
        bullet=[
            ("Ports", "Three female threaded ends."),
            ("Control", "Quarter-turn L/T path switching."),
            ("RFQ", "Specify porting and size with FerruleX."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316 / SS316L"),
            ("Ends", "Female thread"),
            ("Pattern", "3-way"),
            ("Pressure", "~1000 PSI typical"),
        ],
    ),
    54: dict(
        kw="stainless steel ball valve",
        angle="weld-end ball valve for permanent process lines that must not leak at joints",
        sizes="weld schedule per RFQ; ~1000 PSI class",
        mat="SS304 / SS316 / SS316L",
        ends="weld",
        use="skids and plant piping preferring welded isolation valves",
        bullet=[
            ("Ends", "Weld prep for permanent install."),
            ("Materials", "SS304 / SS316 ball valve."),
            ("OEM", "Custom end prep from drawings."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316 / SS316L"),
            ("Ends", "Weld"),
            ("Type", "Ball valve"),
            ("Pressure", "~1000 PSI typical"),
        ],
    ),
    55: dict(
        kw="stainless steel ball valve",
        angle="mini ball valve for tight OEM panels and low-flow instrument isolation",
        sizes="compact body; small NPT/G or compression options",
        mat="SS304 / SS316 / SS316L",
        ends="mini threaded / compact",
        use="analytical instruments, gas panels and portable devices",
        bullet=[
            ("Form", "Mini envelope for dense panels."),
            ("Materials", "SS304 / SS316."),
            ("RFQ", "Confirm end style and Cv needs."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316 / SS316L"),
            ("Type", "Mini ball valve"),
            ("Ends", "Per RFQ (thread/compact)"),
            ("Order mode", "Factory RFQ"),
        ],
    ),
    56: dict(
        kw="stainless steel ball valve",
        angle="high-pressure female ball valve for elevated system pressures",
        sizes="female thread; HP class toward ~4500 PSI depending on size",
        mat="SS304 / SS316 / SS316L",
        ends="HP female",
        use="test benches, hydraulic pilots and high-pressure gas service after RFQ review",
        bullet=[
            ("Duty", "High-pressure female thread series."),
            ("Materials", "SS316 preferred for corrosive media."),
            ("RFQ", "State design pressure, media and size."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316 / SS316L"),
            ("Ends", "Female thread"),
            ("Pressure", "HP series (confirm on RFQ)"),
            ("Type", "High-pressure ball valve"),
        ],
    ),
    57: dict(
        kw="stainless steel ball valve",
        angle="air-source ball valve optimized for compressed-air headers and FRL feeds",
        sizes="female / utility thread sizes typical for plant air",
        mat="SS304 / SS316",
        ends="air-source pattern",
        use="compressor rooms, pneumatic OEM lines and maintenance isolation",
        bullet=[
            ("Service", "Compressed air isolation."),
            ("Materials", "SS304 / SS316."),
            ("Factory", "FerruleX stocks common air-line sizes."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316"),
            ("Type", "Air-source ball valve"),
            ("Media", "Compressed air"),
            ("Order mode", "Factory RFQ"),
        ],
    ),
    58: dict(
        kw="stainless steel ball valve",
        angle="high-pressure compression ball valve pairing double ferrules with HP shutoff",
        sizes="compression OD; HP toward ~4500 PSI class",
        mat="SS316 / SS316L / SS304",
        ends="HP compression",
        use="instrumentation at elevated pressure without threaded adapters",
        bullet=[
            ("Ends", "Double-ferrule compression on both sides."),
            ("Duty", "High-pressure ball shutoff."),
            ("RFQ", "Tube OD + design pressure required."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS316 / SS316L / SS304"),
            ("Ends", "Compression"),
            ("Pressure", "HP series (confirm on RFQ)"),
            ("Type", "HP compression ball valve"),
        ],
    ),
    59: dict(
        kw="stainless steel ball valve",
        angle="hex-body compression ball valve for compact wrench access on panels",
        sizes="compression OD; ~1000 PSI",
        mat="SS304 / SS316 / SS316L",
        ends="hex-body compression",
        use="dense OEM cabinets where round bodies waste space",
        bullet=[
            ("Body", "Hex envelope for wrench flats."),
            ("Ends", "Compression tube ports."),
            ("Materials", "SS304 / SS316 / SS316L."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316 / SS316L"),
            ("Ends", "Compression"),
            ("Body", "Hex"),
            ("Pressure", "~1000 PSI"),
        ],
    ),
    60: dict(
        kw="stainless steel ball valve",
        angle="long-handle hex compression ball valve for easier actuation in gloves or tight reaches",
        sizes="compression OD; ~1000 PSI",
        mat="SS304 / SS316 / SS316L",
        ends="long-handle hex compression",
        use="field panels and skids needing visible handle position",
        bullet=[
            ("Handle", "Extended lever for leverage and visibility."),
            ("Body", "Hex compression ball valve."),
            ("Materials", "SS304 / SS316 / SS316L."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316 / SS316L"),
            ("Ends", "Compression"),
            ("Handle", "Long lever"),
            ("Pressure", "~1000 PSI"),
        ],
    ),
    61: dict(
        kw="stainless steel needle valve",
        angle="straight compression needle valve for fine metering on instrument tubing",
        sizes="compression OD series",
        mat="SS304 / SS316 / SS316L",
        ends="straight compression",
        use="sampling, purge control and gauge isolation needing precise stem travel",
        bullet=[
            ("Control", "Fine needle stem for metering."),
            ("Ends", "Double-ferrule compression."),
            ("Materials", "SS304 / SS316 / SS316L."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316 / SS316L"),
            ("Ends", "Compression"),
            ("Pattern", "Straight"),
            ("Type", "Needle valve"),
        ],
    ),
    62: dict(
        kw="stainless steel needle valve",
        angle="angle compression needle valve for panel-friendly 90° metering",
        sizes="compression OD",
        mat="SS304 / SS316 / SS316L",
        ends="angle compression",
        use="gauge boards and analyzer shelters",
        bullet=[
            ("Pattern", "Angle body for panel mounting."),
            ("Ends", "Compression tube connections."),
            ("Control", "Precise stainless steel needle valve throttling."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316 / SS316L"),
            ("Ends", "Compression"),
            ("Pattern", "Angle"),
            ("Type", "Needle valve"),
        ],
    ),
    63: dict(
        kw="stainless steel needle valve",
        angle="forged compression needle valve for rugged metering under vibration",
        sizes="compression OD",
        mat="SS304 / SS316 / SS316L",
        ends="forged compression",
        use="marine and mobile analyzer packages",
        bullet=[
            ("Body", "Forged blank for durability."),
            ("Ends", "Double-ferrule compression."),
            ("Service", "Fine flow control on instrument gas/liquid."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316 / SS316L"),
            ("Ends", "Compression"),
            ("Body", "Forged"),
            ("Type", "Needle valve"),
        ],
    ),
    64: dict(
        kw="stainless steel needle valve",
        angle="weld-end needle valve for permanent metering points on process tubing",
        sizes="weld prep per RFQ",
        mat="SS304 / SS316 / SS316L",
        ends="weld",
        use="skids that prohibit demountable tube fittings at the valve",
        bullet=[
            ("Ends", "Weld preparation."),
            ("Control", "Needle metering stem."),
            ("OEM", "Custom weld ends from drawings."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316 / SS316L"),
            ("Ends", "Weld"),
            ("Type", "Needle valve"),
            ("Order mode", "Factory RFQ"),
        ],
    ),
    65: dict(
        kw="stainless steel needle valve",
        angle="straight female needle valve for threaded instrument manifolds",
        sizes="female NPT / G series",
        mat="SS304 / SS316 / SS316L",
        ends="straight female",
        use="gauge isolation and bleed valves on threaded blocks",
        bullet=[
            ("Ends", "Female threaded ports."),
            ("Pattern", "Straight metering body."),
            ("Materials", "SS304 / SS316 / SS316L."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316 / SS316L"),
            ("Ends", "Female thread"),
            ("Pattern", "Straight"),
            ("Type", "Needle valve"),
        ],
    ),
    66: dict(
        kw="stainless steel needle valve",
        angle="male-female straight needle valve bridging dissimilar threaded ports while metering",
        sizes="male × female thread combinations",
        mat="SS304 / SS316 / SS316L",
        ends="male-female straight",
        use="retrofits between valve, gauge and tubing adapters",
        bullet=[
            ("Ends", "Male and female threads on one valve."),
            ("Control", "Fine needle adjustment."),
            ("RFQ", "List both thread codes."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316 / SS316L"),
            ("Ends", "Male × female thread"),
            ("Pattern", "Straight"),
            ("Type", "Needle valve"),
        ],
    ),
    67: dict(
        kw="stainless steel needle valve",
        angle="angle female needle valve for compact 90° metering on threaded panels",
        sizes="female thread",
        mat="SS304 / SS316 / SS316L",
        ends="angle female",
        use="instrument boards with limited depth",
        bullet=[
            ("Pattern", "Angle female body."),
            ("Control", "Stainless steel needle valve stem."),
            ("Materials", "SS304 / SS316 / SS316L."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316 / SS316L"),
            ("Ends", "Female thread"),
            ("Pattern", "Angle"),
            ("Type", "Needle valve"),
        ],
    ),
    68: dict(
        kw="stainless steel needle valve",
        angle="high-pressure female globe-style valve for elevated-pressure throttling",
        sizes="female thread; HP class",
        mat="SS304 / SS316 / SS316L",
        ends="HP female globe",
        use="test loops and high-pressure gas/liquid metering after pressure review",
        bullet=[
            ("Duty", "High-pressure female globe / needle style."),
            ("Materials", "SS316 preferred for corrosive HP media."),
            ("RFQ", "Design pressure and Cv required."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316 / SS316L"),
            ("Ends", "Female thread"),
            ("Pressure", "HP series (confirm on RFQ)"),
            ("Type", "High-pressure globe valve"),
        ],
    ),
    69: dict(
        kw="instrumentation fittings",
        angle="BA (bright annealed) stainless tubing for clean instrument and semiconductor-adjacent lines",
        sizes="instrument OD/wall per RFQ",
        mat="SS304 / SS316 / SS316L",
        ends="BA tube (cut length / coil options)",
        use="gas panels, analyzers and double-ferrule systems needing smooth ID",
        bullet=[
            ("Finish", "Bright annealed tube surface."),
            ("Pairing", "Designed for stainless steel compression fittings."),
            ("RFQ", "OD, wall, length and grade."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316 / SS316L"),
            ("Type", "BA tube"),
            ("Finish", "Bright annealed"),
            ("Order mode", "Factory RFQ"),
        ],
    ),
    70: dict(
        kw="instrumentation fittings",
        angle="precision stainless tube with tight OD/wall tolerance for instrumentation",
        sizes="precision OD/wall per RFQ",
        mat="SS304 / SS316 / SS316L",
        ends="straight lengths",
        use="OEM machines and analyzer plumbing requiring consistent ferrule bite",
        bullet=[
            ("Tolerance", "Precision OD for reliable double-ferrule sealing."),
            ("Materials", "SS304 / SS316 / SS316L."),
            ("Factory", "Cut lengths stocked/custom via RFQ."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316 / SS316L"),
            ("Type", "Precision tube"),
            ("Use", "Instrumentation"),
            ("Order mode", "Factory RFQ"),
        ],
    ),
    71: dict(
        kw="instrumentation fittings",
        angle="stainless coil tube for long instrument runs without mid-couplings",
        sizes="coil OD/wall per RFQ",
        mat="SS304 / SS316 / SS316L",
        ends="coil",
        use="field instrument tubing, refrigeration-style instrument jumps and OEM kits",
        bullet=[
            ("Form", "Continuous coil reduces joints."),
            ("Materials", "SS304 / SS316 / SS316L."),
            ("RFQ", "Coil length, OD and wall thickness."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316 / SS316L"),
            ("Type", "Coil tube"),
            ("Form", "Coiled length"),
            ("Order mode", "Factory RFQ"),
        ],
    ),
    72: dict(
        kw="corrugated stainless steel hose",
        angle="corrugated stainless tube/hose blank for flexible routing before end finishing",
        sizes="OD Φ6–Φ100",
        mat="SS304 / SS316",
        ends="open corrugated (ends finished per RFQ)",
        use="OEM fabricators who weld or assemble custom ends in-house",
        bullet=[
            ("Form", "Corrugated stainless tube stock."),
            ("Sizes", "OD Φ6–Φ100 typical."),
            ("OEM", "End finishing available from FerruleX on RFQ."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316"),
            ("OD range", "Φ6–Φ100"),
            ("Type", "Corrugated tube"),
            ("Order mode", "Factory RFQ"),
        ],
    ),
    73: dict(
        kw="instrumentation fittings",
        angle="tube clamp supporting stainless instrument tubing against vibration",
        sizes="matched to common tube OD",
        mat="SS304 / SS316 hardware",
        ends="clamp",
        use="panels, skids and shipboard tubing runs",
        bullet=[
            ("Function", "Secures tubing to structure."),
            ("Sizes", "Common instrument OD clamps."),
            ("Materials", "Stainless hardware options."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316"),
            ("Type", "Tube clamp"),
            ("Fit", "Instrument tube OD"),
            ("Order mode", "Factory RFQ"),
        ],
    ),
    74: dict(
        kw="stainless steel tube fittings",
        angle="push-to-connect straight fitting for tool-light tube joins on air/water",
        sizes="push-to-connect OD series (typically within 4–16 mm class)",
        mat="SS304 / SS316",
        ends="push-to-connect straight",
        use="pneumatic OEM and maintenance-friendly utility lines",
        bullet=[
            ("Install", "Push tube to click; release collar to remove."),
            ("Pattern", "Straight body."),
            ("Materials", "SS304 / SS316."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316"),
            ("Type", "Push-to-connect straight"),
            ("Media", "Air / water (confirm)"),
            ("Order mode", "Factory RFQ"),
        ],
    ),
    75: dict(
        kw="stainless steel tube fittings",
        angle="push-to-connect elbow for 90° routing without bending soft tube sharply",
        sizes="push-to-connect OD series",
        mat="SS304 / SS316",
        ends="push-to-connect elbow",
        use="crowded machine bases and control boxes",
        bullet=[
            ("Geometry", "90° push-in elbow."),
            ("Install", "No flaring tools required."),
            ("Materials", "SS304 / SS316."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316"),
            ("Type", "Push-to-connect elbow"),
            ("Pattern", "90°"),
            ("Order mode", "Factory RFQ"),
        ],
    ),
    76: dict(
        kw="stainless steel tube fittings",
        angle="push-to-connect straight union joining two tubes of equal OD quickly",
        sizes="push-to-connect OD series",
        mat="SS304 / SS316",
        ends="push-to-connect union",
        use="inline repairs and modular pneumatic assemblies",
        bullet=[
            ("Connection", "Tube-to-tube push union."),
            ("Materials", "SS304 / SS316."),
            ("Service", "Air and light fluid lines after media check."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316"),
            ("Type", "Push-to-connect union"),
            ("Pattern", "Straight"),
            ("Order mode", "Factory RFQ"),
        ],
    ),
    77: dict(
        kw="stainless steel tube fittings",
        angle="push-to-connect bulkhead fitting for panel pass-through with push-in tube ends",
        sizes="push-to-connect OD series; panel bulkhead mount",
        mat="SS304 / SS316",
        ends="push-to-connect bulkhead",
        use="enclosure walls on pneumatic OEM equipment",
        bullet=[
            ("Mounting", "Bulkhead lock for panel thickness."),
            ("Ends", "Push-to-connect tube ports."),
            ("Materials", "SS304 / SS316."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316"),
            ("Type", "Push-to-connect bulkhead"),
            ("Mount", "Panel bulkhead"),
            ("Order mode", "Factory RFQ"),
        ],
    ),
    78: dict(
        kw="stainless steel pipe fittings",
        angle="Y-type and T-type tee fittings for threaded branching geometries",
        sizes="female/male thread combinations per RFQ",
        mat="SS304 / SS316",
        ends="Y / T tee",
        use="headers, washdown branches and multi-leg utility lines",
        bullet=[
            ("Patterns", "Y-type and T-type branching."),
            ("Materials", "SS304 / SS316."),
            ("RFQ", "Port sizes and thread standard required."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316"),
            ("Type", "Y-type / T-type tee"),
            ("Threads", "NPT / G / Metric"),
            ("Order mode", "Factory RFQ"),
        ],
    ),
    79: dict(
        kw="stainless steel elbow fitting",
        angle="investment cast elbow for economical stainless pipe direction changes",
        sizes="cast fitting sizes per RFQ",
        mat="SS304 / SS316",
        ends="investment cast elbow",
        use="general stainless piping and OEM assemblies",
        bullet=[
            ("Process", "Investment cast stainless elbow."),
            ("Materials", "SS304 / SS316."),
            ("OEM", "Non-standard angles reviewed from drawings."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316"),
            ("Type", "Investment cast elbow"),
            ("Process", "Investment casting"),
            ("Order mode", "Factory RFQ"),
        ],
    ),
    80: dict(
        kw="stainless steel pipe fittings",
        angle="investment cast tee for cost-effective three-port stainless branching",
        sizes="cast tee sizes per RFQ",
        mat="SS304 / SS316",
        ends="investment cast tee",
        use="utility piping and OEM frames",
        bullet=[
            ("Process", "Investment cast tee body."),
            ("Materials", "SS304 / SS316."),
            ("RFQ", "Equal or reducing ports."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316"),
            ("Type", "Investment cast tee"),
            ("Process", "Investment casting"),
            ("Order mode", "Factory RFQ"),
        ],
    ),
    82: dict(
        kw="stainless steel ball valve",
        angle="investment cast ball valve balancing cost and corrosion resistance for utility shutoff",
        sizes="cast valve sizes; threaded ends typical",
        mat="SS304 / SS316",
        ends="investment cast ball valve",
        use="water, air and light process isolation on OEM equipment",
        bullet=[
            ("Process", "Investment cast body and ends."),
            ("Function", "Quarter-turn stainless steel ball valve shutoff."),
            ("RFQ", "Size, thread and seat material."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 / SS316"),
            ("Type", "Investment cast ball valve"),
            ("Process", "Investment casting"),
            ("Order mode", "Factory RFQ"),
        ],
    ),
    84: dict(
        kw="stainless steel pipe fittings",
        angle="pneumatic silencer / muffler reducing exhaust noise on solenoid and cylinder vents",
        sizes="common pneumatic exhaust thread sizes",
        mat="SS304 / sintered elements as applicable",
        ends="silencer",
        use="OEM pneumatic machines and plant air exhausts",
        bullet=[
            ("Function", "Attenuates pneumatic exhaust noise."),
            ("Mount", "Threaded into exhaust ports."),
            ("RFQ", "Thread size and flow capacity."),
        ],
        specs=[
            ("Brand", "FerruleX"),
            ("Material", "SS304 (series dependent)"),
            ("Type", "Pneumatic silencer"),
            ("Mount", "Threaded exhaust"),
            ("Order mode", "Factory RFQ"),
        ],
    ),
}

OPENERS = [
    "{title} delivers {kw} for {use}.",
    "{title} is a FerruleX {kw} option built around {angle}.",
    "Specify {title} when the BOM needs {kw} with {angle}.",
    "{title} serves export OEM and plant buyers sourcing {kw} for {use}.",
    "Select {title} for {kw} jobs that rely on {angle}.",
    "{title} covers {kw} service where {angle} is the deciding detail.",
    "FerruleX supplies {title} as {kw} hardware for {angle}.",
    "{title} supports {use} using {kw} construction oriented to {angle}.",
]

MID = [
    "Sizes typically cover {sizes}. Materials are {mat}. Connection style: {ends}.",
    "Catalog sizing: {sizes}. Available in {mat}. Ends: {ends}.",
    "Expect {sizes} with {mat} bodies and {ends} interfaces.",
    "Working envelope: {sizes}; alloys {mat}; ends configured as {ends}.",
]

CLOSE = [
    "The FerruleX factory keeps common sizes stocked for fast delivery; send tube OD, threads, pressure and quantity for an RFQ — no cart, factory quote only.",
    "Request a FerruleX factory RFQ with sizes and media; stocked SKUs ship fast for exporters and OEM programs.",
    "FerruleX quotes from the factory with stocked fast delivery on popular sizes — include drawings or a size list in your RFQ.",
    "Share your size table with FerruleX for a factory RFQ; we emphasize stocked inventory and responsive export lead times.",
]

LONG_OPEN = [
    "Beyond the overview, this SKU is specified when engineers need {angle} without switching brands mid-manifold.",
    "Technical buyers use this pattern specifically for {angle}, keeping documentation simple across SS304/SS316 bills.",
    "On projects that standardize on {kw}, the differentiator is {angle} plus factory RFQ flexibility.",
    "Use-cases center on {use}, where {ends} and {mat} must stay consistent with neighboring FerruleX fittings.",
]

LONG_CLOSE = [
    "Pair with FerruleX tube fittings and valves from the same RFQ to keep materials, threads and lead times aligned.",
    "Confirm media, temperature and design pressure in the RFQ so FerruleX can validate stocked vs custom machining.",
    "OEM programs can mix stocked and custom pieces; FerruleX reviews drawings after the initial size quote.",
    "Export documentation and packaging are handled at the factory after PO confirmation — start with an RFQ.",
]


def word_count(s: str) -> int:
    return len(re.findall(r"[A-Za-z0-9']+", s))


def clip_desc(s: str, lo=145, hi=160) -> str:
    s = " ".join(s.split())
    s = re.sub(r"(?:\s*RFQ\.)+$", ".", s)
    s = re.sub(r"\.\s*\.", ".", s)
    if not s.endswith("."):
        s += "."

    pads = [
        " Stocked sizes ship fast.",
        " OEM sizes quoted from drawings.",
        " Export RFQ only — no cart.",
        " NPT, G and metric options.",
        " Confirm media on RFQ.",
        " Double-check tube OD on RFQ.",
        " Custom lengths available.",
        " Panel-mount options on RFQ.",
        " Fast factory shipping.",
        " Ask FerruleX for stock.",
        " SS316 on request.",
        " Metric threads OK.",
        " Send size list today.",
        " Common SKUs in inventory.",
    ]
    i = 0
    while len(s) < lo and i < 40:
        add = pads[i % len(pads)]
        if add.strip().lower() in s.lower():
            i += 1
            continue
        if len(s) + len(add) <= hi:
            s = s.rstrip(".") + "." + add
        else:
            room = hi - len(s)
            fitted = False
            for t in pads:
                if 8 <= len(t) <= room and t.strip().lower() not in s.lower():
                    s = s.rstrip(".") + "." + t
                    fitted = True
                    break
            if not fitted and room >= 6:
                s = (s.rstrip(".") + " RFQ.")[:hi]
                if not s.endswith("."):
                    s = s.rsplit(" ", 1)[0] + "."
            break
        i += 1

    if len(s) > hi:
        cut = s[:hi]
        last_dot = cut.rfind(".")
        if last_dot >= lo - 1:
            s = cut[: last_dot + 1]
        else:
            s = cut.rsplit(" ", 1)[0].rstrip(".,;") + "."

    # hard clamp
    if len(s) > hi:
        s = s[:hi].rsplit(" ", 1)[0].rstrip(".,;") + "."
    if len(s) < lo:
        # last-resort pad with spaces-free clause
        filler = " FerruleX factory RFQ."
        while len(s) < lo and len(s) + len(filler) <= hi:
            s = s.rstrip(".") + "." + filler
            break
        if len(s) < lo:
            # extend with " Available now." style
            more = " Available from stock."
            if len(s) + len(more) <= hi:
                s = s.rstrip(".") + "." + more
    return s


BRIDGES = [
    "FerruleX cuts and inspects this pattern in-house so export RFQs stay consistent lot to lot.",
    "Buyers usually lock tube OD and thread codes first, then confirm pressure class with the factory.",
    "Stocked common sizes support fast delivery; non-catalog ends move to OEM machining after drawing review.",
    "Keep SS304 vs SS316 selection aligned with neighboring valves and fittings on the same PO.",
    "Installation stays demountable for maintenance skids that cannot rely on permanent welds alone.",
    "Documentation for export shipments follows the FerruleX factory RFQ path — no ecommerce cart.",
    "Pair this SKU with matching tube OD and seat materials when you build a full manifold quote.",
    "Pressure guidance below is catalog-typical; always restate design pressure in the RFQ notes.",
]


def build_entry(pid: int, title: str, f: dict) -> dict:
    o = OPENERS[pid % len(OPENERS)].format(title=title, **f)
    m = MID[pid % len(MID)].format(**f)
    c = CLOSE[pid % len(CLOSE)]
    bridge = BRIDGES[pid % len(BRIDGES)]
    # Ensure primary KW appears in first ~40 words
    kw_guard = ""
    first40 = " ".join((o + " " + bridge).split()[:40]).lower()
    if f["kw"].lower() not in first40 and not any(
        part in first40 for part in f["kw"].lower().split()[:2]
    ):
        kw_guard = f" It is specified as {f['kw']} in SS304/SS316 service."
    content = f"{o}{kw_guard} {bridge} {m} {c}"
    # expand if under 90 words
    extras = [
        f" Mention {f['ends']} and {f['sizes']} in the RFQ so FerruleX can reserve stocked parts.",
        f" Keep {f['kw']} and {f['mat']} consistent across the manifold when you quote companion valves.",
        f" State metric vs imperial sizing early to avoid rework on double ferrule or NPT adapters.",
        f" Custom OEM geometry is available after drawing review when catalog ends do not match the layout.",
    ]
    ei = 0
    while word_count(content) < 90 and ei < 8:
        content = content + " " + extras[(pid + ei) % len(extras)]
        ei += 1
    # trim if over 160 words
    words = content.split()
    if len(words) > 160:
        content = " ".join(words[:158]) + "."

    long = (
        LONG_OPEN[pid % len(LONG_OPEN)].format(title=title, **f)
        + " "
        + f"For {title}, catalog cues are {f['sizes']}; materials {f['mat']}; ends {f['ends']}."
        + " "
        + LONG_CLOSE[pid % len(LONG_CLOSE)]
    )
    while word_count(long) < 50:
        long += f" FerruleX factory support covers stocked delivery and OEM RFQ machining for this pattern."
    if word_count(long) > 90:
        long = " ".join(long.split()[:88]) + "."

    # Build meta 145–160 chars: primary KW + SS304/SS316 + RFQ/factory
    mat_meta = f["mat"]
    if "304" not in mat_meta and "316" not in mat_meta:
        mat_meta = "SS304 / SS316"
    # Normalize long mat strings for meta
    if len(mat_meta) > 28:
        mat_meta = "SS304 / SS316"

    size_short = f["sizes"]
    if len(size_short) > 36:
        size_short = size_short[:34].rsplit(" ", 1)[0]
        # avoid dangling prepositions / incomplete tails
        size_short = re.sub(
            r"\b(to|per|and|or|for|with|of|the|a|an|in|on|from|common)$",
            "",
            size_short,
            flags=re.I,
        ).rstrip(" ,;/-")
        if len(size_short) < 8:
            size_short = "catalog sizes"

    candidates = [
        f"{title}: {f['kw']} ({mat_meta}). {size_short}. FerruleX factory RFQ — stocked fast delivery.",
        f"{title}: {f['kw']}, {mat_meta}. {size_short}. Factory RFQ from FerruleX; stocked sizes ship fast.",
        f"{title} — {f['kw']} in {mat_meta}. FerruleX factory RFQ for export; stocked sizes ship fast.",
        f"{title}: {f['kw']} ({mat_meta}). FerruleX factory RFQ — stocked common sizes, custom OEM OK.",
        f"{title}: {f['kw']}, {mat_meta}. Request FerruleX factory RFQ; stocked SKUs ship fast for OEM.",
    ]
    desc = min(candidates, key=lambda d: abs(len(d) - 152))
    if len(desc) < 145 or len(desc) > 160:
        desc = clip_desc(desc)
    # final enforce
    if not (145 <= len(desc) <= 160):
        base = f"{title}: {f['kw']}, {mat_meta}. FerruleX factory RFQ."
        # pad to exactly around 152
        while len(base) < 145:
            add = " Stocked sizes ship fast."
            if len(base) + len(add) > 160:
                room = 160 - len(base)
                short_adds = [
                    " Fast stock shipping.",
                    " OEM RFQ welcome.",
                    " Export only.",
                    " Send OD list.",
                    " NPT/G OK.",
                ]
                for sa in short_adds:
                    if len(sa) <= room:
                        base = base.rstrip(".") + "." + sa
                        break
                break
            base = base.rstrip(".") + "." + add
        if len(base) > 160:
            base = base[:160].rsplit(" ", 1)[0].rstrip(".,;") + "."
        desc = base

    return {
        "description": desc,
        "content": " ".join(content.split()),
        "subTitle": " ".join(long.split()),
        "bullets": f["bullet"],
        "specs": f["specs"],
    }


def load_titles() -> dict[int, str]:
    out = {}
    for path in PROD.glob("*.md"):
        text = path.read_text(encoding="utf-8")
        tid = re.search(r"^  id:\s*(\d+)", text, re.M)
        title = re.search(r"^title:\s*'((?:''|[^'])*)'", text, re.M)
        if tid and title:
            out[int(tid.group(1))] = title.group(1).replace("''", "'")
    return out


def esc(s: str) -> str:
    return s.replace("'", "''")


def render_md(
    title: str,
    category: str,
    slug: str,
    pid: int,
    img_card: str,
    img_main: str,
    copy: dict,
) -> str:
    bullets = "\n".join(
        f"  - title: '{esc(a)}'\n    subTitle: '{esc(b)}'" for a, b in copy["bullets"]
    )
    specs = "\n".join(
        f"  - title: '{esc(a)}'\n    subTitle: '{esc(b)}'" for a, b in copy["specs"]
    )
    rows = "\n".join(f"      - ['{esc(a)}', '{esc(b)}']" for a, b in copy["specs"])
    return f"""---
title: '{esc(title)}'
description: '{esc(copy['description'])}'
category: '{esc(category)}'
slug: '{esc(slug)}'
main:
  id: {pid}
  content: |
    {copy['content']}
  imgCard: '{img_card}'
  imgMain: '{img_main}'
  imgAlt: '{esc(title)} — FerruleX stainless steel fittings'
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
    {copy['subTitle']}
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


CATEGORY_FIX = {
    33: "stainless-steel-tube-fittings",
    77: "stainless-steel-tube-fittings",
}


def build_copy_dict(titles: dict[int, str]) -> dict[int, dict]:
    missing = [i for i in titles if i not in FACTS]
    if missing:
        raise SystemExit(f"Missing FACTS for ids: {missing}")
    extra = [i for i in FACTS if i not in titles]
    if extra:
        raise SystemExit(f"FACTS without files: {extra}")
    return {pid: build_entry(pid, titles[pid], FACTS[pid]) for pid in sorted(titles)}


def emit_script(copy: dict[int, dict]) -> str:
    """Emit standalone rewrite_product_copy_v2.py with full COPY dict."""
    lines = ["COPY = {"]
    for pid, c in copy.items():
        lines.append(f"    {pid}: {{")
        lines.append(f"        'description': {c['description']!r},")
        lines.append(f"        'content': {c['content']!r},")
        lines.append(f"        'subTitle': {c['subTitle']!r},")
        lines.append(f"        'bullets': {c['bullets']!r},")
        lines.append(f"        'specs': {c['specs']!r},")
        lines.append("    },")
    lines.append("}")
    copy_block = "\n".join(lines)

    runner = r'''# -*- coding: utf-8 -*-
"""Rewrite EVERY EN product markdown with unique FerruleX SEO copy (v2)."""
from __future__ import annotations

import re
from pathlib import Path

PROD_DIR = Path(__file__).resolve().parents[1] / "src" / "content" / "products" / "en"

CATEGORY_FIX = {
    33: "stainless-steel-tube-fittings",
    77: "stainless-steel-tube-fittings",
}

__COPY_BLOCK__


def esc(s: str) -> str:
    return s.replace("'", "''")


def parse_field(text: str, key: str) -> str | None:
    m = re.search(rf"^{key}:\s*'((?:''|[^'])*)'", text, re.M)
    return m.group(1).replace("''", "'") if m else None


def rewrite_file(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    title = parse_field(text, "title")
    category = parse_field(text, "category")
    slug = parse_field(text, "slug")
    id_m = re.search(r"^  id:\s*(\d+)", text, re.M)
    img_card_m = re.search(r"imgCard:\s*'([^']+)'", text)
    img_main_m = re.search(r"imgMain:\s*'([^']+)'", text)
    if not all([title, category, slug, id_m, img_card_m, img_main_m]):
        raise RuntimeError(f"Incomplete frontmatter: {path.name}")
    img_card = img_card_m.group(1)
    img_main = img_main_m.group(1)
    pid = int(id_m.group(1))
    if pid not in COPY:
        raise RuntimeError(f"No COPY for id {pid} ({path.name})")
    category = CATEGORY_FIX.get(pid, category)
    c = COPY[pid]
    bullets = "\n".join(
        f"  - title: '{esc(a)}'\n    subTitle: '{esc(b)}'" for a, b in c["bullets"]
    )
    specs = "\n".join(
        f"  - title: '{esc(a)}'\n    subTitle: '{esc(b)}'" for a, b in c["specs"]
    )
    rows = "\n".join(f"      - ['{esc(a)}', '{esc(b)}']" for a, b in c["specs"])
    out = (
        "---\n"
        f"title: '{esc(title)}'\n"
        f"description: '{esc(c['description'])}'\n"
        f"category: '{esc(category)}'\n"
        f"slug: '{esc(slug)}'\n"
        "main:\n"
        f"  id: {pid}\n"
        "  content: |\n"
        f"    {c['content']}\n"
        f"  imgCard: '{img_card}'\n"
        f"  imgMain: '{img_main}'\n"
        f"  imgAlt: '{esc(title)} — FerruleX stainless steel fittings'\n"
        "tabs:\n"
        "  - id: 'tabs-with-card-item-1'\n"
        "    dataTab: '#tabs-with-card-1'\n"
        "    title: 'Description'\n"
        "  - id: 'tabs-with-card-item-2'\n"
        "    dataTab: '#tabs-with-card-2'\n"
        "    title: 'Specifications'\n"
        "  - id: 'tabs-with-card-item-3'\n"
        "    dataTab: '#tabs-with-card-3'\n"
        "    title: 'Request Quote'\n"
        "longDescription:\n"
        f"  title: '{esc(title)}'\n"
        "  subTitle: |\n"
        f"    {c['subTitle']}\n"
        "  btnTitle: 'Request a factory quote'\n"
        "  btnURL: '/contact'\n"
        "descriptionList:\n"
        f"{bullets}\n"
        "specificationsLeft:\n"
        f"{specs}\n"
        "tableData:\n"
        "  - feature: ['Specification', 'Value']\n"
        "    description:\n"
        f"{rows}\n"
        "blueprints:\n"
        "  first: '@/images/blueprint-1.avif'\n"
        "  second: '@/images/blueprint-2.avif'\n"
        "---\n"
    )
    path.write_text(out, encoding="utf-8")


def main() -> None:
    files = sorted(PROD_DIR.glob("item-*.md"))
    n = 0
    for f in files:
        rewrite_file(f)
        n += 1
    print(f"Rewrote {n} products")


if __name__ == "__main__":
    main()
'''
    return runner.replace("__COPY_BLOCK__", copy_block)


def main() -> None:
    titles = load_titles()
    assert len(titles) == 82, len(titles)
    copy = build_copy_dict(titles)

    # validate lengths
    weak = []
    for pid, c in copy.items():
        dlen = len(c["description"])
        wc = word_count(c["content"])
        ws = word_count(c["subTitle"])
        if not (145 <= dlen <= 160):
            weak.append(f"id {pid} desc len {dlen}: {c['description']}")
        if not (90 <= wc <= 160):
            weak.append(f"id {pid} content words {wc}")
        if not (50 <= ws <= 90):
            weak.append(f"id {pid} subTitle words {ws}")
        # uniqueness check vs neighbors — content must include title or kw uniquely
        if c["content"][:40] == copy.get(pid - 1, {}).get("content", "x")[:40]:
            weak.append(f"id {pid} shares opener with previous")

    if weak:
        print("VALIDATION ISSUES:")
        for w in weak[:40]:
            print(" ", w)
        if len(weak) > 40:
            print(f"  ... +{len(weak)-40} more")
    else:
        print("All copy length checks passed")

    # Write products directly (and also emit standalone script)
    OUT.write_text(emit_script(copy), encoding="utf-8")
    print(f"Wrote {OUT}")

    # Also apply rewrite now
    n = 0
    for path in sorted(PROD.glob("item-*.md")):
        text = path.read_text(encoding="utf-8")
        title = re.search(r"^title:\s*'((?:''|[^'])*)'", text, re.M).group(1).replace("''", "'")
        category = re.search(r"^category:\s*'((?:''|[^'])*)'", text, re.M).group(1)
        slug = re.search(r"^slug:\s*'((?:''|[^'])*)'", text, re.M).group(1)
        pid = int(re.search(r"^  id:\s*(\d+)", text, re.M).group(1))
        img_card = re.search(r"imgCard:\s*'([^']+)'", text).group(1)
        img_main = re.search(r"imgMain:\s*'([^']+)'", text).group(1)
        category = CATEGORY_FIX.get(pid, category)
        path.write_text(
            render_md(title, category, slug, pid, img_card, img_main, copy[pid]),
            encoding="utf-8",
        )
        n += 1
    print(f"Rewrote {n} products")


if __name__ == "__main__":
    main()
