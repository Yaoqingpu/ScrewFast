# -*- coding: utf-8 -*-
"""Hand-written unique EN copy for all FerruleX products (no rotating templates)."""
from __future__ import annotations

# Each entry: description, content, subTitle, bullets, specs
# content: 90–160 words; subTitle: 50–90 words; description: 145–160 chars

COPY = {}

def _a(pid, description, content, subTitle, bullets, specs):
    COPY[pid] = {
        "description": description,
        "content": " ".join(content.split()),
        "subTitle": " ".join(subTitle.split()),
        "bullets": bullets,
        "specs": specs,
    }

# --- Hose / corrugated ---
_a(1,
"SS Corrugated Hose — Male/Female Thread: corrugated stainless steel hose, SS304/SS316, Φ6–Φ100. FerruleX factory RFQ.",
"""
Corrugated stainless steel hose with male or female thread ends solves vibration and thermal movement where rigid tube cannot bend.
FerruleX manufactures this hose in SS304 and SS316 with NPT, G, ZG(R) or metric threads across OD Φ6–Φ100.
Common plant lengths ship from stock; custom cut lengths and mixed thread genders are quoted from your RFQ.
Use it for HVAC jumps, petrochemical utility lines and OEM panels that need a flexible stainless link without flanges.
Tell us hose OD, thread code, length and media so the factory can confirm pressure class and ship stocked sizes quickly.
""",
"""
Threaded corrugated hose is the fastest way to drop a flexible stainless segment between two ports without welding.
Specify thread standard on both ends when they differ, and note whether you need SS316 for chloride or marine exposure.
FerruleX packs export cartons after PO; start with an RFQ listing OD and length tolerances.
""",
[("Thread ends", "Male/female NPT, G, ZG(R) or metric."),
 ("Hose OD", "Φ6–Φ100 corrugated stainless."),
 ("Alloys", "SS304 or SS316 bellows and fittings.")],
[("Brand", "FerruleX"), ("Material", "SS304 / SS316"), ("Hose OD", "Φ6–Φ100"),
 ("Ends", "Male/female thread"), ("Order mode", "Factory RFQ")])

_a(2,
"SS Flanged Corrugated Hose: corrugated stainless steel hose with flanged ends, SS304/SS316, Φ6–Φ100. FerruleX RFQ.",
"""
Flanged corrugated stainless steel hose connects process and utility lines that already use gasketed flange joints.
FerruleX builds SS304/SS316 bellows with flange ends sized for OD Φ6–Φ100 hose, with drill patterns confirmed on RFQ.
It absorbs pump vibration and pipe growth on heat-transfer loops, skids and plant headers where threaded hose is not preferred.
Stocked common flange sizes support fast delivery; non-standard facing or bolt circles are OEM-machined after drawing review.
Include flange standard, hose OD, length and design temperature in your FerruleX factory quote request.
""",
"""
Choose flanged ends when maintenance teams expect to break joints with standard flange hardware rather than thread sealant.
Confirm raised-face or flat-face preference and gasket material with the process engineer before locking the RFQ.
FerruleX can match mixed flange sizes on opposite ends when the skid layout requires a transition.
""",
[("Ends", "Flanged joints for bolted process connections."),
 ("Hose range", "Corrugated OD typically Φ6–Φ100."),
 ("OEM", "Custom flange drill pattern and length on RFQ.")],
[("Brand", "FerruleX"), ("Material", "SS304 / SS316"), ("Hose OD", "Φ6–Φ100"),
 ("Ends", "Flange"), ("Customization", "Length and flange facing on RFQ")])

_a(3,
"SS Flanged Expansion Joint: corrugated stainless compensator, SS304/SS316, OD Φ6–Φ100. FerruleX factory RFQ — stocked fast.",
"""
This flanged expansion joint uses corrugated stainless steel hose geometry to take axial and lateral pipe movement.
FerruleX supplies SS304 and SS316 compensators in the Φ6–Φ100 OD family with flanged ends for building, power and petrochemical lines.
It is not a simple jumper hose: the corrugation count and free length are selected to match expected thermal travel.
Stocked patterns cover frequent plant sizes; longer strokes or special flanges move to custom RFQ machining.
Send design travel, pressure, media and flange standard so FerruleX can validate the joint before production.
""",
"""
Expansion joints protect anchors and pumps from thermal growth that would otherwise overload rigid spool pieces.
Provide hot/cold temperature extremes and installed length so the factory does not undersize the corrugation stack.
FerruleX quotes stocked and custom compensators on the same RFQ sheet for mixed project packages.
""",
[("Function", "Absorbs axial/lateral thermal and settlement movement."),
 ("Size range", "Corrugated OD Φ6–Φ100 typical."),
 ("Ends", "Flanged compensator style.")],
[("Brand", "FerruleX"), ("Material", "SS304 / SS316"), ("Size range", "OD Φ6–Φ100"),
 ("Type", "Flanged expansion joint"), ("Lead time", "Stocked + custom RFQ")])

_a(4,
"SS Tri-Clamp Corrugated Hose: sanitary corrugated stainless steel hose, SS304/SS316, Φ6–Φ100. FerruleX factory RFQ.",
"""
Tri-clamp corrugated stainless steel hose gives hygienic process lines a flexible link that opens with a clamp, not a wrench marathon.
FerruleX forms SS304/SS316 hose in OD Φ6–Φ100 with tri-clamp ferrules sized to your clamp standard.
Food, beverage and clean-utility skids use it for CIP jumpers, tank connections and equipment change-outs.
Stocked clamp sizes ship fast from the factory; odd ferrule OD or electropolish notes belong in the RFQ.
List clamp size, hose OD, length and media when you request a FerruleX quote — RFQ only, no cart.
""",
"""
Sanitary buyers pick tri-clamp ends to keep tear-down time short during cleaning cycles.
Call out surface-finish expectations if the hose sits in a visible or validated clean zone.
FerruleX can supply matching clamps and gaskets as a separate line on the same factory RFQ.
""",
[("Ends", "Tri-clamp ferrules for sanitary clamp assemblies."),
 ("Hygiene", "SS304/SS316 corrugated hose for clean routing."),
 ("RFQ data", "Clamp size, length and media required.")],
[("Brand", "FerruleX"), ("Material", "SS304 / SS316"), ("Hose OD", "Φ6–Φ100"),
 ("Ends", "Tri-clamp"), ("Industry", "Sanitary / clean process")])

_a(5,
"SS Quick-Coupling Corrugated Hose: corrugated stainless steel hose with quick-coupling ends, SS304/SS316. FerruleX RFQ.",
"""
Quick-coupling corrugated stainless steel hose lets operators swap flexible lines on test benches and utility drops without full thread make-up.
FerruleX builds SS304/SS316 hose (OD Φ6–Φ100) with quick-coupling ends matched to the coupler style you specify on RFQ.
Portable equipment, maintenance bypasses and OEM test stands benefit when hose change-out time matters more than a permanent joint.
Common coupler sizes are stocked for fast factory shipping; uncommon profiles are machined after drawing review.
Include coupler brand/series if known, hose OD, length and working pressure in your FerruleX RFQ.
""",
"""
Quick-coupling ends trade a small amount of joint complexity for minutes saved on every hose swap.
Confirm male/female coupler gender on each end so the assembly arrives ready to click together.
FerruleX keeps export packaging dry and labeled by length for multi-hose kits on one PO.
""",
[("Ends", "Quick-coupling for rapid connect/disconnect."),
 ("Materials", "SS304 / SS316 corrugated hose."),
 ("Sizing", "OD Φ6–Φ100; coupler style on RFQ.")],
[("Brand", "FerruleX"), ("Material", "SS304 / SS316"), ("Hose OD", "Φ6–Φ100"),
 ("Ends", "Quick-coupling"), ("Order mode", "Factory RFQ")])

_a(6,
"SS KF Flexible Vacuum Corrugated Hose: KF16–50 / ISO63–100 vacuum hose, SS304. FerruleX factory RFQ — stocked fast.",
"""
KF flexible vacuum corrugated hose bridges chambers and pumps where rigid vacuum spool pieces would fight alignment.
FerruleX supplies SS304 corrugated vacuum hose in KF16, KF25, KF40, KF50 plus ISO63, ISO80 and ISO100 flanges.
Analytical instruments, coating tools and clean-gas utilities use these flexible links to cut vibration into the chamber.
Stocked KF lengths support fast delivery; unusual ISO lengths or mixed KF-to-ISO adapters are RFQ items.
State flange sizes both ends, free length and vacuum level when you request a FerruleX factory quote.
""",
"""
Vacuum service needs clean welds and correct flange geometry more than high liquid pressure ratings.
Call out whether you need centering rings and clamps with the hose or will source them locally.
FerruleX reviews leak-check expectations on custom vacuum assemblies after the initial size quote.
""",
[("Vacuum ends", "KF16–KF50 and ISO63–ISO100."),
 ("Material", "SS304 corrugated vacuum hose."),
 ("Use", "Vacuum and clean-gas flexible links.")],
[("Brand", "FerruleX"), ("Material", "SS304"), ("KF sizes", "KF16 / 25 / 40 / 50"),
 ("ISO sizes", "ISO63 / 80 / 100"), ("Type", "Flexible vacuum corrugated hose")])

# --- Compression fittings ---
_a(7,
"Compression Tube to Male Connector: stainless steel compression fittings, double ferrule, SS316/304, NPT/G. FerruleX RFQ.",
"""
Stainless steel compression fittings in this tube-to-male pattern take instrumentation tubing into a male NPT, G or metric port.
FerruleX double-ferrule connectors cover tube OD 3–25 mm and 1/8\"–1\" with M5–M24 thread options in SS316, SS316L or SS304.
Typical working pressure is about 1000 PSI; high-pressure versions approach 4500 PSI when the tube wall allows.
Gauge blocks, manifold outlets and analyzer panels use this connector daily because make-up needs no welding.
Send tube OD, male thread and quantity for a FerruleX factory RFQ — common sizes are stocked for fast export shipping.
""",
"""
Seat the tube fully before tightening the nut so the front ferrule bites evenly on annealed stainless tubing.
Hard tubing above the recommended hardness range raises leak risk on gas service; ask for guidance if you are unsure.
FerruleX can mix thread standards across a single PO when your panel drawing calls for both NPT and G ports.
""",
[("Seal", "Double ferrule bite on annealed stainless tube."),
 ("Threads", "Male NPT, G, ZG(R) or metric."),
 ("Pressure", "~1000 PSI standard; HP ~4500 PSI.")],
[("Brand", "FerruleX"), ("Material", "SS316 / SS316L / SS304"), ("Tube OD", "3–25 mm / 1/8\"–1\""),
 ("Threads", "NPT / G / ZG(R) / Metric"), ("Pressure", "~1000 PSI (HP ~4500 PSI)")])

_a(8,
"Compression Tube to Female Connector: stainless steel compression fittings, double ferrule to female thread. FerruleX RFQ.",
"""
This stainless steel compression fitting joins tube OD to a female threaded port for gauges, valves and instrument blocks.
FerruleX double-ferrule bodies in SS316/SS316L/SS304 take metric or fractional tube from 3–25 mm / 1/8\"–1\" into female NPT, G or metric.
Sampling lines and hook-ups that already use female ports avoid an extra male adapter when you start with this connector.
Standard pressure class is near 1000 PSI with HP options for thicker tube.
List tube OD, female thread and media on your FerruleX RFQ; stocked sizes leave the factory quickly.
""",
"""
Female-thread connectors simplify drop-in replacement on manifolds that were drilled for NPT gauges years ago.
Verify thread pitch with a gauge before ordering mixed BSPP/NPT lots on the same skid.
FerruleX marks bags by tube OD and thread so receiving can kitting without opening every pouch.
""",
[("Pattern", "Tube OD into female thread in one body."),
 ("Sizes", "Metric and fractional tube with mixed threads."),
 ("Stock", "Common sizes stocked for fast FerruleX shipping.")],
[("Brand", "FerruleX"), ("Material", "SS316 / SS316L / SS304"), ("Tube OD", "3–25 mm / 1/8\"–1\""),
 ("Female threads", "NPT / G / Metric"), ("Pressure", "~1000 PSI standard")])

_a(9,
"Compression Straight Union: stainless steel compression fittings, equal tube-to-tube double ferrule. FerruleX factory RFQ.",
"""
A compression straight union joins two equal tube ends with double ferrules and no weld bead in the line.
FerruleX unions run SS316/SS316L/SS304 across OD 3–25 mm and 1/8\"–1\" for instrumentation and light process tubing.
Inline repairs, skid tubing and analyzer runs stay demountable for future instrument swaps.
Working pressure typically sits near 1000 PSI; HP series are available when the tube rating supports them.
Quote tube OD and alloy preference to FerruleX — stocked unions ship fast on export RFQs.
""",
"""
Unions are the preferred break point when a transmitter must come out of line without cutting tube.
Leave straight tube length beyond each nut so the ferrules seat without fighting a nearby bend.
FerruleX can supply matched nut/ferrule spare kits on the same RFQ for field stores.
""",
[("Connection", "Equal-size double-ferrule union."),
 ("Install", "Insert tube to shoulder, then tighten nut."),
 ("Materials", "SS304 / SS316 / SS316L.")],
[("Brand", "FerruleX"), ("Material", "SS316 / SS316L / SS304"), ("Tube OD", "3–25 mm / 1/8\"–1\""),
 ("Type", "Straight compression union"), ("Pressure", "~1000 PSI (HP available)")])

_a(10,
"Compression Reducing Union: stainless steel compression fittings joining unequal tube OD. SS316/304. FerruleX RFQ.",
"""
Compression reducing unions bridge two different tube outside diameters on one straight axis with double ferrules both sides.
FerruleX covers reducing pairs inside the 3–25 mm / 1/8\"–1\" envelope in SS316, SS316L or SS304.
Panel redesigns and OEM machines that mix metric and fractional tubing need this fitting instead of two adapters.
Pressure follows the smaller tube’s wall rating; plan near 1000 PSI unless you order the HP series.
Put both tube OD values on the FerruleX RFQ so the factory pulls the correct reducing blank from stock.
""",
"""
Always list the larger OD first in your notes so purchasing and the factory read the same reducing direction.
If one side is fractional and the other metric, say so explicitly to avoid near-size mix-ups.
FerruleX holds common reducing pairs for fast shipment and machines odd pairs after drawing approval.
""",
[("Function", "Reduces between two tube OD sizes."),
 ("Seal", "Double ferrule on each side."),
 ("RFQ", "Both tube OD values required.")],
[("Brand", "FerruleX"), ("Material", "SS316 / SS316L / SS304"), ("Size range", "OD 3–25 mm / 1/8\"–1\""),
 ("Type", "Reducing compression union"), ("Pressure", "~1000 PSI")])

_a(11,
"Compression Male Elbow Connector: 90° stainless steel compression fittings, tube to male thread. FerruleX RFQ.",
"""
The compression male elbow turns instrumentation tubing 90° into a male threaded port without a separate elbow plus connector.
FerruleX double-ferrule elbows in SS316/SS316L/SS304 cover tube OD 3–25 mm / 1/8\"–1\" with NPT, G or metric male threads.
Tight panel corners and crowded skids clear obstacles that a straight connector cannot.
Expect about 1000 PSI on standard bodies; confirm HP needs on the RFQ.
FerruleX stocks frequent OD/thread pairs for fast factory delivery after your quote request.
""",
"""
Orient the male thread before final ferrule pull-up so you do not fight the elbow while making up the port.
On gas service, use fully annealed tube and follow the nut-turn procedure recommended for double-ferrule fittings.
FerruleX can laser-mark heat codes on larger lots when your QA package requires traceability.
""",
[("Geometry", "90° elbow into a male port."),
 ("Threads", "NPT, G, ZG(R) or metric male."),
 ("Pressure", "~1000 PSI instrumentation class.")],
[("Brand", "FerruleX"), ("Material", "SS316 / SS316L / SS304"), ("Tube OD", "3–25 mm / 1/8\"–1\""),
 ("Pattern", "Male elbow"), ("Threads", "NPT / G / Metric")])

_a(12,
"Compression Union Elbow: 90° stainless steel compression fittings, tube-to-tube double ferrule. FerruleX RFQ.",
"""
Compression union elbows route equal (or reducing) tube runs around a corner with double ferrules on both ends.
FerruleX makes these stainless steel compression fittings in SS316/SS316L/SS304 for OD 3–25 mm / 1/8\"–1\".
OEM cabinets and instrument tubing layouts stay compact without adding a welded bend.
Standard pressure is about 1000 PSI with HP options on request.
Ask FerruleX for equal or reducing elbow unions by listing both tube OD values on the RFQ; stocked pairs ship fast.
""",
"""
Union elbows remove the need to cold-bend thin-wall tube in place, which often kinks and ruins ferrule sealing surfaces.
Keep at least a short straight tube segment before each nut for proper ferrule engagement.
FerruleX bags left and right reducing elbows separately when the BOM uses both orientations.
""",
[("Pattern", "Equal or reducing 90° union elbows."),
 ("Seal", "Double-ferrule metal bite both ends."),
 ("Stock", "Common OD pairs stocked at FerruleX.")],
[("Brand", "FerruleX"), ("Material", "SS316 / SS316L / SS304"), ("Tube OD", "3–25 mm / 1/8\"–1\""),
 ("Type", "Compression union elbow"), ("Pressure", "~1000 PSI")])

_a(13,
"Compression Male/Female Tee: stainless steel compression fittings tee with thread branch options. FerruleX RFQ.",
"""
This compression male/female tee branches instrumentation lines using double-ferrule tube ports plus optional threaded branches.
FerruleX tees in SS316/SS316L/SS304 span tube OD 3–25 mm / 1/8\"–1\" for gauge taps, purge legs and sample take-offs.
Run-and-branch combinations let you keep the main tube continuous while adding a threaded instrument port.
Plan near 1000 PSI unless the RFQ calls for high-pressure bodies.
Specify run OD, branch style and thread on your FerruleX factory RFQ for stocked or machined tees.
""",
"""
Tees are where leak paths multiply, so clean tube ends and correct ferrule orientation matter more than on a simple union.
If the branch is threaded, confirm whether you need male or female before the blank is pulled.
FerruleX can supply plug kits for unused branches on commissioning spares lists.
""",
[("Ports", "Run and branch mixes for instrumentation."),
 ("Materials", "SS304 / SS316 / SS316L."),
 ("RFQ", "Run OD, branch style and thread.")],
[("Brand", "FerruleX"), ("Material", "SS316 / SS316L / SS304"), ("Tube OD", "3–25 mm / 1/8\"–1\""),
 ("Type", "Compression male/female tee"), ("Pressure", "~1000 PSI")])

_a(14,
"Compression Reducing Tee: stainless steel compression fittings with smaller branch take-off. FerruleX factory RFQ.",
"""
A compression reducing tee pulls a smaller instrument branch from a larger tube run without upsizing the whole tap.
FerruleX double-ferrule reducing tees in SS316/SS316L/SS304 work inside OD 3–25 mm / 1/8\"–1\".
Gauge trees and sample points stay compact when the branch only needs a few millimeters of tube.
Pressure is governed by the smallest port and tube wall; 1000 PSI is the usual catalog class.
List main-run OD and branch OD on the FerruleX RFQ — stocked reducing tees ship fast, odd pairs are OEM.
""",
"""
Reducing tees beat drilling and welding a sockolet when the line must remain demountable for validation work.
Do not assume the branch can carry full run pressure if the wall thickness differs.
FerruleX prints both OD sizes on the label to stop warehouse mix-ups between near reductions.
""",
[("Function", "Smaller branch off a larger tube run."),
 ("Seal", "Double ferrule on all tube ports."),
 ("Factory", "Mixed OD pairs from stock or OEM.")],
[("Brand", "FerruleX"), ("Material", "SS316 / SS316L / SS304"), ("Size range", "OD 3–25 mm / 1/8\"–1\""),
 ("Type", "Reducing compression tee"), ("Pressure", "~1000 PSI")])

_a(15,
"Cylinder Connector: compact stainless instrumentation fitting for cylinder and specialty ports. SS316/304. FerruleX RFQ.",
"""
Cylinder connectors give gas bottles and specialty ports a compact stainless entry when wrench swing is limited.
FerruleX machines these instrumentation fittings in SS316/SS316L/SS304 to match the port and tube OD on your drawing.
They sit in the compression catalog family but are not a generic male connector — port geometry drives the blank.
OEM equipment and portable gas panels are the usual homes for this pattern.
Attach a port sketch or size code with your FerruleX RFQ so the factory quotes the correct cylinder-style body.
""",
"""
Specialty ports fail when a standard hex connector hits a shoulder or regulator casting.
Measure thread engagement depth and any undercut before assuming a catalog male connector will seat.
FerruleX holds common cylinder patterns in stock and cuts others after RFQ approval.
""",
[("Form", "Cylinder-style body for specialty ports."),
 ("Materials", "SS304 / SS316 / SS316L."),
 ("Ordering", "Port drawing or size code with RFQ.")],
[("Brand", "FerruleX"), ("Material", "SS316 / SS316L / SS304"), ("Series", "Compression instrumentation"),
 ("Type", "Cylinder connector"), ("Order mode", "Factory RFQ")])

_a(16,
"Compression Bulkhead Union: panel-pass stainless steel compression fittings, double ferrule. SS316/304. FerruleX RFQ.",
"""
Compression bulkhead unions pass instrumentation tubing through a panel wall with double ferrules on both sides.
FerruleX bulkheads in SS316/SS316L/SS304 cover OD 3–25 mm / 1/8\"–1\" and lock with a bulkhead nut for enclosure thickness.
Control cabinets, analyzer shelters and skid walls stay sealed without welding a tube stub through the plate.
Standard duty is about 1000 PSI; confirm panel thickness and OD on the RFQ.
FerruleX stocks frequent bulkhead sizes for fast factory shipping after quote.
""",
"""
Drill the panel hole to the bulkhead’s recommended diameter so the locknut seats flat without crushing the gasket face.
If the wall is thicker than the nut stack allows, call it out — FerruleX can extend the shank on OEM lots.
Label both sides of the panel during install so maintenance knows which nut is the process side.
""",
[("Mounting", "Bulkhead locknut for panel thickness ranges."),
 ("Seal", "Double ferrule both sides of the wall."),
 ("Pressure", "~1000 PSI; confirm panel thickness.")],
[("Brand", "FerruleX"), ("Material", "SS316 / SS316L / SS304"), ("Tube OD", "3–25 mm / 1/8\"–1\""),
 ("Type", "Compression bulkhead union"), ("Pressure", "~1000 PSI")])

_a(17,
"Compression / Quick-Screw Straight & Bulkhead: hybrid stainless fittings for mixed tube styles. FerruleX RFQ.",
"""
These hybrid straight and bulkhead connectors combine stainless steel compression fittings with quick-screw ends on one panel strategy.
FerruleX offers compression OD 3–25 mm alongside quick-screw OD 4–16 mm in SS316/SS316L/SS304 so pneumatic and instrument tube can share a wall.
Straight bodies handle inline joins; bulkhead versions pass through the enclosure.
Both styles sit near 1000 PSI when correctly sized.
Tell FerruleX which end is compression versus quick-screw, plus both OD values, on the factory RFQ for stocked hybrids.
""",
"""
Mixed end styles stop you from forcing plastic pneumatic tube into a double-ferrule bite that was meant for hard stainless.
Keep a clear BOM note for each SKU so the warehouse does not issue a full-compression twin by mistake.
FerruleX kits hybrid bulkheads with the matching locknuts in one bag for panel assemblers.
""",
[("Styles", "Straight and bulkhead; compression or quick-screw."),
 ("Sizes", "Match OD to the end style you select."),
 ("Factory", "Common hybrids stocked for export RFQs.")],
[("Brand", "FerruleX"), ("Material", "SS316 / SS316L / SS304"), ("Compression OD", "3–25 mm / 1/8\"–1\""),
 ("Quick-screw OD", "4–16 mm / 1/8\"–1/2\""), ("Pressure", "~1000 PSI")])

_a(18,
"Compression Cross Fitting: four-port stainless steel compression fittings for intersecting lines. FerruleX RFQ.",
"""
Compression cross fittings give four double-ferrule ports for intersecting instrumentation lines on one stainless body.
FerruleX crosses in SS316/SS316L/SS304 cover OD 3–25 mm / 1/8\"–1\", equal or reducing.
Calibration benches, multi-leg sample systems and complex manifolds use crosses instead of stacked tees.
Expect about 1000 PSI on standard bodies.
Confirm all four OD values on the FerruleX RFQ so reducing ports land on the correct legs before machining.
""",
"""
A cross concentrates stress at the center; support nearby tubing so the fitting is not the only structural member.
Bleed and plug unused ports rather than leaving open ferrule pockets that collect debris.
FerruleX can supply reducing crosses with two large and two small ports when the P&ID shows that split.
""",
[("Ports", "Four equal or reducing compression ports."),
 ("Seal", "Double ferrule on each tube end."),
 ("RFQ", "All four OD values before ordering.")],
[("Brand", "FerruleX"), ("Material", "SS316 / SS316L / SS304"), ("Tube OD", "3–25 mm / 1/8\"–1\""),
 ("Type", "Compression cross"), ("Pressure", "~1000 PSI")])

_a(19,
"Ground Finish Tube to Male Connector: refined stainless steel compression fittings, tube to male. FerruleX RFQ.",
"""
Ground-finish tube-to-male connectors keep the exterior smoother for visible OEM panels while retaining double-ferrule sealing.
FerruleX offers this stainless steel compression fitting in SS316/SS316L/SS304 for OD 3–25 mm / 1/8\"–1\" with NPT/G/metric male threads.
Labs and export machines that leave fittings in plain sight prefer the ground look over a heavy machine finish.
Function and pressure match the standard connector family near 1000 PSI.
Request ground-finish explicitly on the FerruleX RFQ so stock is pulled from the correct bin.
""",
"""
Ground finish is cosmetic and cleanability driven; it does not change the ferrule bite or allowable pressure by itself.
If you also need electropolish or passivation certificates, add those notes to the same RFQ.
FerruleX photographs ground-finish lots on request for customer approval before large OEM runs.
""",
[("Finish", "Ground exterior for cleaner presentation."),
 ("Function", "Double-ferrule tube to male thread."),
 ("Materials", "SS304 / SS316 / SS316L.")],
[("Brand", "FerruleX"), ("Material", "SS316 / SS316L / SS304"), ("Tube OD", "3–25 mm / 1/8\"–1\""),
 ("Finish", "Ground"), ("Threads", "NPT / G / Metric")])

_a(20,
"Ground Finish Reducing Union: polished-look stainless steel compression fittings, unequal OD. FerruleX RFQ.",
"""
Ground-finish reducing unions transition unequal tube OD with a refined exterior for displayable stainless runs.
FerruleX double-ferrule reducing unions in SS316/SS316L/SS304 sit inside the 3–25 mm / 1/8\"–1\" range.
Medical device OEM, analytical benches and polished skids use them where every fitting stays visible after install.
Sealing performance matches standard reducing unions at roughly 1000 PSI.
Provide both tube OD values and request ground finish on your FerruleX factory RFQ.
""",
"""
Do not substitute a standard machined reducing union if the customer specification calls out ground finish by name.
Wipe fingerprints before packaging; ground surfaces show handling marks more than bead-blasted parts.
FerruleX can match ground-finish elbows and tees on the same PO for a uniform panel appearance.
""",
[("Finish", "Ground body reduces machining marks."),
 ("Function", "Reducing double-ferrule union."),
 ("RFQ", "Both tube OD plus finish callout.")],
[("Brand", "FerruleX"), ("Material", "SS316 / SS316L / SS304"), ("Size range", "OD 3–25 mm / 1/8\"–1\""),
 ("Finish", "Ground"), ("Type", "Reducing union")])

_a(21,
"Ground Finish Straight Union: equal tube stainless steel compression fittings with ground exterior. FerruleX RFQ.",
"""
Ground-finish straight unions join equal tube ends when the stainless steel compression fittings must look as good as they seal.
FerruleX makes SS316/SS316L/SS304 ground unions for OD 3–25 mm / 1/8\"–1\".
Export OEM panels that remain open-frame after FAT often specify this finish across the tubing bill.
Pressure class mirrors standard unions near 1000 PSI.
Order by tube OD with a ground-finish note on the FerruleX RFQ; common sizes are stocked.
""",
"""
Ground unions are a drop-in dimensional twin of the standard union, so BOM swaps are usually painless.
Still, keep finish grades segregated in stores so a rough body does not land on a show panel.
FerruleX offers mixed cartons of ground and standard only when the RFQ lists both clearly.
""",
[("Pattern", "Equal-size ground-finish union."),
 ("Seal", "Double-ferrule instrumentation seal."),
 ("Stock", "Common OD stocked at FerruleX.")],
[("Brand", "FerruleX"), ("Material", "SS316 / SS316L / SS304"), ("Tube OD", "3–25 mm / 1/8\"–1\""),
 ("Finish", "Ground"), ("Type", "Straight union")])

_a(22,
"Ground Finish Male Elbow: 90° ground stainless steel compression fittings, tube to male. FerruleX RFQ.",
"""
Ground-finish male elbows turn tube into a male port with a cleaner exterior for compact cabinets on display.
FerruleX double-ferrule elbows in SS316/SS316L/SS304 cover OD 3–25 mm / 1/8\"–1\" with NPT/G/metric male threads.
They solve the same space problem as standard male elbows while meeting appearance notes on OEM drawings.
Instrumentation pressure near 1000 PSI applies unless you order HP.
Call out ground finish, tube OD and male thread on the FerruleX factory RFQ.
""",
"""
Appearance grades still need correct ferrule pull-up; a shiny leak is still a leak on gas service.
Align the elbow so the ground faces outward if only one side is customer-visible.
FerruleX can supply touch-up notes if secondary machining nicks the ground surface on custom threads.
""",
[("Geometry", "90° male elbow with ground exterior."),
 ("Threads", "NPT / G / metric male options."),
 ("Pressure", "~1000 PSI instrumentation duty.")],
[("Brand", "FerruleX"), ("Material", "SS316 / SS316L / SS304"), ("Tube OD", "3–25 mm / 1/8\"–1\""),
 ("Finish", "Ground"), ("Pattern", "Male elbow")])

_a(23,
"Forged Compression Elbow: forged-body stainless steel compression fittings for vibrating service. FerruleX RFQ.",
"""
Forged compression elbows start from a forged blank for higher mechanical toughness on instrument turns.
FerruleX forges and machines SS316/SS316L/SS304 double-ferrule elbows for OD 3–25 mm / 1/8\"–1\".
Marine skids, petrochemical trees and mobile equipment that shake continuously prefer forged bodies over light bar-stock elbows.
Standard pressure is about 1000 PSI with HP series available.
Ask FerruleX for forged elbows by tube OD on the RFQ; stocked sizes support fast delivery.
""",
"""
Forged grain flow helps when fittings see repeated vibration that fatigues lighter bodies.
It does not replace proper tube support clips along the run.
FerruleX can stamp forge heat numbers when your inspector requires them on the packing list.
""",
[("Body", "Forged elbow blank for strength."),
 ("Seal", "Double-ferrule tube ends."),
 ("Materials", "SS304 / SS316 / SS316L.")],
[("Brand", "FerruleX"), ("Material", "SS316 / SS316L / SS304"), ("Tube OD", "3–25 mm / 1/8\"–1\""),
 ("Body", "Forged"), ("Pressure", "~1000 PSI (HP series available)")])

_a(24,
"Forged Compression Tee: forged stainless steel compression fittings for three-port branching. FerruleX RFQ.",
"""
Forged compression tees branch three double-ferrule ports from a tough forged stainless body.
FerruleX offers equal or reducing tees in SS316/SS316L/SS304 across OD 3–25 mm / 1/8\"–1\".
High-cycle skids and outdoor instrument trees specify forged tees when vibration and impact are expected.
Working pressure stays near 1000 PSI unless HP is requested.
List run and branch OD on the FerruleX RFQ for stocked forged tees or OEM reducing blanks.
""",
"""
Forged tees pair well with forged elbows when the entire tree sits on a vibrating package.
Support the branch leg; a long cantilevered gauge still fatigues the port regardless of forge quality.
FerruleX ships forged and bar-stock tees in separate labeled bags to prevent BOM confusion.
""",
[("Body", "Forged tee for impact and vibration resistance."),
 ("Ports", "Three compression tube ports."),
 ("RFQ", "Equal or reducing branch OD.")],
[("Brand", "FerruleX"), ("Material", "SS316 / SS316L / SS304"), ("Tube OD", "3–25 mm / 1/8\"–1\""),
 ("Body", "Forged"), ("Type", "Compression tee")])

_a(25,
"Forged Compression Reducing Tee: forged stainless steel compression fittings, unequal branch. FerruleX RFQ.",
"""
Forged reducing tees combine forged toughness with a smaller branch take-off for rugged sample and gauge trees.
FerruleX machines these stainless steel compression fittings in SS316/SS316L/SS304 within OD 3–25 mm / 1/8\"–1\".
Mobile analyzers and vibrating packages use them when a light reducing tee is not enough mechanically.
Double ferrules seal every tube port; pressure follows the smaller branch near the usual 1000 PSI class.
Give FerruleX both OD values on the RFQ for stocked or special forged reducing tees.
""",
"""
Reducing forged tees are easy to mis-pick against equal forged tees in a busy crib — label both OD sizes on the shelf.
If the branch sees pulsing sample flow, consider a root valve on that leg as well.
FerruleX quotes forge surcharges clearly when the blank must be custom reduced.
""",
[("Function", "Forged reducing branch off main run."),
 ("Seal", "Double ferrule on tube ports."),
 ("Factory", "Special OD pairs after drawing review.")],
[("Brand", "FerruleX"), ("Material", "SS316 / SS316L / SS304"), ("Size range", "OD 3–25 mm / 1/8\"–1\""),
 ("Body", "Forged"), ("Type", "Reducing tee")])

_a(26,
"Forged Compression Cross Fitting: forged four-port stainless steel compression fittings. SS316/304. FerruleX RFQ.",
"""
Forged compression crosses put four double-ferrule ports on a forged body for tougher intersecting manifolds.
FerruleX builds SS316/SS316L/SS304 crosses for OD 3–25 mm / 1/8\"–1\" aimed at mobile test carts and offshore instrument racks.
The forge blank resists the knocks that light crosses see in the field.
Standard pressure is about 1000 PSI; HP is available on request.
Confirm equal or reducing port layout on the FerruleX factory RFQ before the cross is machined.
""",
"""
Four-port forged crosses are heavier; check panel hole clearance and wrench access before you commit the layout.
Plug unused ports with matching compression plugs rather than leaving open nuts.
FerruleX can balance reducing ports opposite each other when flow symmetry matters on the bench.
""",
[("Body", "Forged four-port cross."),
 ("Seal", "Double-ferrule instrumentation seal."),
 ("Pressure", "~1000 PSI class; HP on request.")],
[("Brand", "FerruleX"), ("Material", "SS316 / SS316L / SS304"), ("Tube OD", "3–25 mm / 1/8\"–1\""),
 ("Body", "Forged"), ("Type", "Compression cross")])
