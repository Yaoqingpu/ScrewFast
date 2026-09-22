# -*- coding: utf-8 -*-
"""Rewrite EVERY EN product markdown with unique FerruleX SEO copy (v2)."""
from __future__ import annotations

import re
from pathlib import Path

PROD_DIR = Path(__file__).resolve().parents[1] / "src" / "content" / "products" / "en"

CATEGORY_FIX = {
    33: "stainless-steel-tube-fittings",
    77: "stainless-steel-tube-fittings",
}

COPY = {
    1: {
        'description': 'SS Corrugated Hose — Male/Female Thread: corrugated stainless steel hose, SS304/SS316, Φ6–Φ100. FerruleX factory RFQ. Stocked sizes ship fast. OEM RFQ welcome.',
        'content': 'Corrugated stainless steel hose with male or female thread ends solves vibration and thermal movement where rigid tube cannot bend. FerruleX manufactures this hose in SS304 and SS316 with NPT, G, ZG(R) or metric threads across OD Φ6–Φ100. Common plant lengths ship from stock; custom cut lengths and mixed thread genders are quoted from your RFQ. Use it for HVAC jumps, petrochemical utility lines and OEM panels that need a flexible stainless link without flanges. Tell us hose OD, thread code, length and media so the factory can confirm pressure class and ship stocked sizes quickly. Mixed thread genders on opposite ends are fine when both codes appear on the RFQ.',
        'subTitle': 'Threaded corrugated hose is the fastest way to drop a flexible stainless segment between two ports without welding. Specify thread standard on both ends when they differ, and note whether you need SS316 for chloride or marine exposure. FerruleX packs export cartons after PO; start with an RFQ listing OD and length tolerances.',
        'bullets': [('Thread ends', 'Male/female NPT, G, ZG(R) or metric.'), ('Hose OD', 'Φ6–Φ100 corrugated stainless.'), ('Alloys', 'SS304 or SS316 bellows and fittings.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 / SS316'), ('Hose OD', 'Φ6–Φ100'), ('Ends', 'Male/female thread'), ('Order mode', 'Factory RFQ')],
    },
    2: {
        'description': 'SS Flanged Corrugated Hose: corrugated stainless steel hose with flanged ends, SS304/SS316, Φ6–Φ100. FerruleX RFQ. Stocked sizes ship fast. Fast stock shipping.',
        'content': 'Flanged corrugated stainless steel hose connects process and utility lines that already use gasketed flange joints. FerruleX builds SS304/SS316 bellows with flange ends sized for OD Φ6–Φ100 hose, with drill patterns confirmed on RFQ. It absorbs pump vibration and pipe growth on heat-transfer loops, skids and plant headers where threaded hose is not preferred. Stocked common flange sizes support fast delivery; non-standard facing or bolt circles are OEM-machined after drawing review. Include flange standard, hose OD, length and design temperature in your FerruleX factory quote request. Call out raised-face or flat-face preference before FerruleX locks the flange blank.',
        'subTitle': 'Choose flanged ends when maintenance teams expect to break joints with standard flange hardware rather than thread sealant. Confirm raised-face or flat-face preference and gasket material with the process engineer before locking the RFQ. FerruleX can match mixed flange sizes on opposite ends when the skid layout requires a transition.',
        'bullets': [('Ends', 'Flanged joints for bolted process connections.'), ('Hose range', 'Corrugated OD typically Φ6–Φ100.'), ('OEM', 'Custom flange drill pattern and length on RFQ.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 / SS316'), ('Hose OD', 'Φ6–Φ100'), ('Ends', 'Flange'), ('Customization', 'Length and flange facing on RFQ')],
    },
    3: {
        'description': 'SS Flanged Expansion Joint: corrugated stainless compensator, SS304/SS316, OD Φ6–Φ100. FerruleX factory RFQ — stocked fast. Stocked sizes ship fast.',
        'content': 'This flanged expansion joint uses corrugated stainless steel hose geometry to take axial and lateral pipe movement. FerruleX supplies SS304 and SS316 compensators in the Φ6–Φ100 OD family with flanged ends for building, power and petrochemical lines. It is not a simple jumper hose: the corrugation count and free length are selected to match expected thermal travel. Stocked patterns cover frequent plant sizes; longer strokes or special flanges move to custom RFQ machining. Send design travel, pressure, media and flange standard so FerruleX can validate the joint before production. Stroke length and corrugation count are selected against the travel you list on the quote.',
        'subTitle': 'Expansion joints protect anchors and pumps from thermal growth that would otherwise overload rigid spool pieces. Provide hot/cold temperature extremes and installed length so the factory does not undersize the corrugation stack. FerruleX quotes stocked and custom compensators on the same RFQ sheet for mixed project packages. Provide hot and cold setpoints plus installed length so corrugation travel is not undersized on first article.',
        'bullets': [('Function', 'Absorbs axial/lateral thermal and settlement movement.'), ('Size range', 'Corrugated OD Φ6–Φ100 typical.'), ('Ends', 'Flanged compensator style.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 / SS316'), ('Size range', 'OD Φ6–Φ100'), ('Type', 'Flanged expansion joint'), ('Lead time', 'Stocked + custom RFQ')],
    },
    4: {
        'description': 'SS Tri-Clamp Corrugated Hose: sanitary corrugated stainless steel hose, SS304/SS316, Φ6–Φ100. FerruleX factory RFQ. Stocked sizes ship fast. OEM RFQ welcome.',
        'content': 'Tri-clamp corrugated stainless steel hose gives hygienic process lines a flexible link that opens with a clamp, not a wrench marathon. FerruleX forms SS304/SS316 hose in OD Φ6–Φ100 with tri-clamp ferrules sized to your clamp standard. Food, beverage and clean-utility skids use it for CIP jumpers, tank connections and equipment change-outs. Stocked clamp sizes ship fast from the factory; odd ferrule OD or electropolish notes belong in the RFQ. List clamp size, hose OD, length and media when you request a FerruleX quote — RFQ only, no cart. Electropolish or surface-finish notes belong on the same RFQ if the hose sits in a validated zone.',
        'subTitle': 'Sanitary buyers pick tri-clamp ends to keep tear-down time short during cleaning cycles. Call out surface-finish expectations if the hose sits in a visible or validated clean zone. FerruleX can supply matching clamps and gaskets as a separate line on the same factory RFQ. Tri-clamp ferrules for sanitary clamp assemblies. SS304/SS316 corrugated hose for clean routing. Clamp size, length and media required.',
        'bullets': [('Ends', 'Tri-clamp ferrules for sanitary clamp assemblies.'), ('Hygiene', 'SS304/SS316 corrugated hose for clean routing.'), ('RFQ data', 'Clamp size, length and media required.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 / SS316'), ('Hose OD', 'Φ6–Φ100'), ('Ends', 'Tri-clamp'), ('Industry', 'Sanitary / clean process')],
    },
    5: {
        'description': 'SS Quick-Coupling Corrugated Hose: corrugated stainless steel hose with quick-coupling ends, SS304/SS316. FerruleX RFQ. Stocked sizes ship fast. Export only.',
        'content': 'Quick-coupling corrugated stainless steel hose lets operators swap flexible lines on test benches and utility drops without full thread make-up. FerruleX builds SS304/SS316 hose (OD Φ6–Φ100) with quick-coupling ends matched to the coupler style you specify on RFQ. Portable equipment, maintenance bypasses and OEM test stands benefit when hose change-out time matters more than a permanent joint. Common coupler sizes are stocked for fast factory shipping; uncommon profiles are machined after drawing review. Include coupler brand/series if known, hose OD, length and working pressure in your FerruleX RFQ. Coupler gender on each end must be stated so the assembly arrives ready to click together.',
        'subTitle': 'Quick-coupling ends trade a small amount of joint complexity for minutes saved on every hose swap. Confirm male/female coupler gender on each end so the assembly arrives ready to click together. FerruleX keeps export packaging dry and labeled by length for multi-hose kits on one PO. Quick-coupling for rapid connect/disconnect. SS304 / SS316 corrugated hose. OD Φ6–Φ100; coupler style on RFQ.',
        'bullets': [('Ends', 'Quick-coupling for rapid connect/disconnect.'), ('Materials', 'SS304 / SS316 corrugated hose.'), ('Sizing', 'OD Φ6–Φ100; coupler style on RFQ.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 / SS316'), ('Hose OD', 'Φ6–Φ100'), ('Ends', 'Quick-coupling'), ('Order mode', 'Factory RFQ')],
    },
    6: {
        'description': 'SS KF Flexible Vacuum Corrugated Hose: KF16–50 / ISO63–100 vacuum hose, SS304. FerruleX factory RFQ — stocked fast. Stocked sizes ship fast. OEM RFQ welcome.',
        'content': 'KF flexible vacuum corrugated hose bridges chambers and pumps where rigid vacuum spool pieces would fight alignment. FerruleX supplies SS304 corrugated vacuum hose in KF16, KF25, KF40, KF50 plus ISO63, ISO80 and ISO100 flanges. Analytical instruments, coating tools and clean-gas utilities use these flexible links to cut vibration into the chamber. Stocked KF lengths support fast delivery; unusual ISO lengths or mixed KF-to-ISO adapters are RFQ items. State flange sizes both ends, free length and vacuum level when you request a FerruleX factory quote. Centering rings and clamps can ship with the hose or be sourced locally — say which on the RFQ.',
        'subTitle': 'Vacuum service needs clean welds and correct flange geometry more than high liquid pressure ratings. Call out whether you need centering rings and clamps with the hose or will source them locally. FerruleX reviews leak-check expectations on custom vacuum assemblies after the initial size quote. KF16–KF50 and ISO63–ISO100. SS304 corrugated vacuum hose. Vacuum and clean-gas flexible links.',
        'bullets': [('Vacuum ends', 'KF16–KF50 and ISO63–ISO100.'), ('Material', 'SS304 corrugated vacuum hose.'), ('Use', 'Vacuum and clean-gas flexible links.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304'), ('KF sizes', 'KF16 / 25 / 40 / 50'), ('ISO sizes', 'ISO63 / 80 / 100'), ('Type', 'Flexible vacuum corrugated hose')],
    },
    7: {
        'description': 'Compression Tube to Male Connector: stainless steel compression fittings, double ferrule, SS316/304, NPT/G. FerruleX RFQ. Stocked sizes ship fast.',
        'content': 'Stainless steel compression fittings in this tube-to-male pattern take instrumentation tubing into a male NPT, G or metric port. FerruleX double-ferrule connectors cover tube OD 3–25 mm and 1/8"–1" with M5–M24 thread options in SS316, SS316L or SS304. Typical working pressure is about 1000 PSI; high-pressure versions approach 4500 PSI when the tube wall allows. Gauge blocks, manifold outlets and analyzer panels use this connector daily because make-up needs no welding. Send tube OD, male thread and quantity for a FerruleX factory RFQ — common sizes are stocked for fast export shipping. Fully annealed tube below the recommended hardness range seals more reliably on gas service.',
        'subTitle': 'Seat the tube fully before tightening the nut so the front ferrule bites evenly on annealed stainless tubing. Hard tubing above the recommended hardness range raises leak risk on gas service; ask for guidance if you are unsure. FerruleX can mix thread standards across a single PO when your panel drawing calls for both NPT and G ports.',
        'bullets': [('Seal', 'Double ferrule bite on annealed stainless tube.'), ('Threads', 'Male NPT, G, ZG(R) or metric.'), ('Pressure', '~1000 PSI standard; HP ~4500 PSI.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS316 / SS316L / SS304'), ('Tube OD', '3–25 mm / 1/8"–1"'), ('Threads', 'NPT / G / ZG(R) / Metric'), ('Pressure', '~1000 PSI (HP ~4500 PSI)')],
    },
    8: {
        'description': 'Compression Tube to Female Connector: stainless steel compression fittings, double ferrule to female thread. FerruleX RFQ. Stocked sizes ship fast.',
        'content': 'This stainless steel compression fitting joins tube OD to a female threaded port for gauges, valves and instrument blocks. FerruleX double-ferrule bodies in SS316/SS316L/SS304 take metric or fractional tube from 3–25 mm / 1/8"–1" into female NPT, G or metric. Sampling lines and hook-ups that already use female ports avoid an extra male adapter when you start with this connector. Standard pressure class is near 1000 PSI with HP options for thicker tube. List tube OD, female thread and media on your FerruleX RFQ; stocked sizes leave the factory quickly. Gauge the female thread before ordering mixed BSPP and NPT lots on one manifold drawing.',
        'subTitle': 'Female-thread connectors simplify drop-in replacement on manifolds that were drilled for NPT gauges years ago. Verify thread pitch with a gauge before ordering mixed BSPP/NPT lots on the same skid. FerruleX marks bags by tube OD and thread so receiving can kitting without opening every pouch. Tube OD into female thread in one body. Metric and fractional tube with mixed threads. Common sizes stocked for fast FerruleX shipping.',
        'bullets': [('Pattern', 'Tube OD into female thread in one body.'), ('Sizes', 'Metric and fractional tube with mixed threads.'), ('Stock', 'Common sizes stocked for fast FerruleX shipping.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS316 / SS316L / SS304'), ('Tube OD', '3–25 mm / 1/8"–1"'), ('Female threads', 'NPT / G / Metric'), ('Pressure', '~1000 PSI standard')],
    },
    9: {
        'description': 'Compression Straight Union: stainless steel compression fittings, equal tube-to-tube double ferrule. FerruleX factory RFQ. Stocked sizes ship fast.',
        'content': 'A compression straight union joins two equal tube ends with double ferrules and no weld bead in the line. FerruleX unions run SS316/SS316L/SS304 across OD 3–25 mm and 1/8"–1" for instrumentation and light process tubing. Inline repairs, skid tubing and analyzer runs stay demountable for future instrument swaps. Working pressure typically sits near 1000 PSI; HP series are available when the tube rating supports them. Quote tube OD and alloy preference to FerruleX — stocked unions ship fast on export RFQs. Leave straight tube beyond each nut so ferrules seat without fighting a nearby bend.',
        'subTitle': 'Unions are the preferred break point when a transmitter must come out of line without cutting tube. Leave straight tube length beyond each nut so the ferrules seat without fighting a nearby bend. FerruleX can supply matched nut/ferrule spare kits on the same RFQ for field stores. Equal-size double-ferrule union. Insert tube to shoulder, then tighten nut. SS304 / SS316 / SS316L.',
        'bullets': [('Connection', 'Equal-size double-ferrule union.'), ('Install', 'Insert tube to shoulder, then tighten nut.'), ('Materials', 'SS304 / SS316 / SS316L.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS316 / SS316L / SS304'), ('Tube OD', '3–25 mm / 1/8"–1"'), ('Type', 'Straight compression union'), ('Pressure', '~1000 PSI (HP available)')],
    },
    10: {
        'description': 'Compression Reducing Union: stainless steel compression fittings joining unequal tube OD. SS316/304. FerruleX RFQ. Stocked sizes ship fast. Fast stock shipping.',
        'content': 'Compression reducing unions bridge two different tube outside diameters on one straight axis with double ferrules both sides. FerruleX covers reducing pairs inside the 3–25 mm / 1/8"–1" envelope in SS316, SS316L or SS304. Panel redesigns and OEM machines that mix metric and fractional tubing need this fitting instead of two adapters. Pressure follows the smaller tube’s wall rating; plan near 1000 PSI unless you order the HP series. Put both tube OD values on the FerruleX RFQ so the factory pulls the correct reducing blank from stock. List the larger OD first in notes so purchasing and the factory read the same reducing direction.',
        'subTitle': 'Always list the larger OD first in your notes so purchasing and the factory read the same reducing direction. If one side is fractional and the other metric, say so explicitly to avoid near-size mix-ups. FerruleX holds common reducing pairs for fast shipment and machines odd pairs after drawing approval.',
        'bullets': [('Function', 'Reduces between two tube OD sizes.'), ('Seal', 'Double ferrule on each side.'), ('RFQ', 'Both tube OD values required.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS316 / SS316L / SS304'), ('Size range', 'OD 3–25 mm / 1/8"–1"'), ('Type', 'Reducing compression union'), ('Pressure', '~1000 PSI')],
    },
    11: {
        'description': 'Compression Male Elbow Connector: 90° stainless steel compression fittings, tube to male thread. FerruleX RFQ. Stocked sizes ship fast. Fast stock shipping.',
        'content': 'The compression male elbow turns instrumentation tubing 90° into a male threaded port without a separate elbow plus connector. FerruleX double-ferrule elbows in SS316/SS316L/SS304 cover tube OD 3–25 mm / 1/8"–1" with NPT, G or metric male threads. Tight panel corners and crowded skids clear obstacles that a straight connector cannot. Expect about 1000 PSI on standard bodies; confirm HP needs on the RFQ. FerruleX stocks frequent OD/thread pairs for fast factory delivery after your quote request. Orient the male thread before final ferrule pull-up so the elbow is not fighting the port.',
        'subTitle': 'Orient the male thread before final ferrule pull-up so you do not fight the elbow while making up the port. On gas service, use fully annealed tube and follow the nut-turn procedure recommended for double-ferrule fittings. FerruleX can laser-mark heat codes on larger lots when your QA package requires traceability.',
        'bullets': [('Geometry', '90° elbow into a male port.'), ('Threads', 'NPT, G, ZG(R) or metric male.'), ('Pressure', '~1000 PSI instrumentation class.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS316 / SS316L / SS304'), ('Tube OD', '3–25 mm / 1/8"–1"'), ('Pattern', 'Male elbow'), ('Threads', 'NPT / G / Metric')],
    },
    12: {
        'description': 'Compression Union Elbow: 90° stainless steel compression fittings, tube-to-tube double ferrule. FerruleX RFQ. Stocked sizes ship fast. Fast stock shipping.',
        'content': 'Compression union elbows route equal (or reducing) tube runs around a corner with double ferrules on both ends. FerruleX makes these stainless steel compression fittings in SS316/SS316L/SS304 for OD 3–25 mm / 1/8"–1". OEM cabinets and instrument tubing layouts stay compact without adding a welded bend. Standard pressure is about 1000 PSI with HP options on request. Ask FerruleX for equal or reducing elbow unions by listing both tube OD values on the RFQ; stocked pairs ship fast. Union elbows remove cold-bend risk that kinks thin-wall tube and ruins sealing surfaces.',
        'subTitle': 'Union elbows remove the need to cold-bend thin-wall tube in place, which often kinks and ruins ferrule sealing surfaces. Keep at least a short straight tube segment before each nut for proper ferrule engagement. FerruleX bags left and right reducing elbows separately when the BOM uses both orientations.',
        'bullets': [('Pattern', 'Equal or reducing 90° union elbows.'), ('Seal', 'Double-ferrule metal bite both ends.'), ('Stock', 'Common OD pairs stocked at FerruleX.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS316 / SS316L / SS304'), ('Tube OD', '3–25 mm / 1/8"–1"'), ('Type', 'Compression union elbow'), ('Pressure', '~1000 PSI')],
    },
    13: {
        'description': 'Compression Male/Female Tee: stainless steel compression fittings tee with thread branch options. FerruleX RFQ. Stocked sizes ship fast. Fast stock shipping.',
        'content': 'This compression male/female tee branches instrumentation lines using double-ferrule tube ports plus optional threaded branches. FerruleX tees in SS316/SS316L/SS304 span tube OD 3–25 mm / 1/8"–1" for gauge taps, purge legs and sample take-offs. Run-and-branch combinations let you keep the main tube continuous while adding a threaded instrument port. Plan near 1000 PSI unless the RFQ calls for high-pressure bodies. Specify run OD, branch style and thread on your FerruleX factory RFQ for stocked or machined tees. Unused branches should be plugged during commissioning rather than left open to collect debris.',
        'subTitle': 'Tees are where leak paths multiply, so clean tube ends and correct ferrule orientation matter more than on a simple union. If the branch is threaded, confirm whether you need male or female before the blank is pulled. FerruleX can supply plug kits for unused branches on commissioning spares lists.',
        'bullets': [('Ports', 'Run and branch mixes for instrumentation.'), ('Materials', 'SS304 / SS316 / SS316L.'), ('RFQ', 'Run OD, branch style and thread.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS316 / SS316L / SS304'), ('Tube OD', '3–25 mm / 1/8"–1"'), ('Type', 'Compression male/female tee'), ('Pressure', '~1000 PSI')],
    },
    14: {
        'description': 'Compression Reducing Tee: stainless steel compression fittings with smaller branch take-off. FerruleX factory RFQ. Stocked sizes ship fast. Fast stock shipping.',
        'content': 'A compression reducing tee pulls a smaller instrument branch from a larger tube run without upsizing the whole tap. FerruleX double-ferrule reducing tees in SS316/SS316L/SS304 work inside OD 3–25 mm / 1/8"–1". Gauge trees and sample points stay compact when the branch only needs a few millimeters of tube. Pressure is governed by the smallest port and tube wall; 1000 PSI is the usual catalog class. List main-run OD and branch OD on the FerruleX RFQ — stocked reducing tees ship fast, odd pairs are OEM. The branch cannot automatically carry full run pressure if wall thickness differs on that leg.',
        'subTitle': 'Reducing tees beat drilling and welding a sockolet when the line must remain demountable for validation work. Do not assume the branch can carry full run pressure if the wall thickness differs. FerruleX prints both OD sizes on the label to stop warehouse mix-ups between near reductions. Smaller branch off a larger tube run. Double ferrule on all tube ports. Mixed OD pairs from stock or OEM.',
        'bullets': [('Function', 'Smaller branch off a larger tube run.'), ('Seal', 'Double ferrule on all tube ports.'), ('Factory', 'Mixed OD pairs from stock or OEM.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS316 / SS316L / SS304'), ('Size range', 'OD 3–25 mm / 1/8"–1"'), ('Type', 'Reducing compression tee'), ('Pressure', '~1000 PSI')],
    },
    15: {
        'description': 'Cylinder Connector: compact stainless instrumentation fitting for cylinder and specialty ports. SS316/304. FerruleX RFQ. Stocked sizes ship fast.',
        'content': 'Cylinder connectors give gas bottles and specialty ports a compact stainless entry when wrench swing is limited. FerruleX machines these instrumentation fittings in SS316/SS316L/SS304 to match the port and tube OD on your drawing. They sit in the compression catalog family but are not a generic male connector — port geometry drives the blank. OEM equipment and portable gas panels are the usual homes for this pattern. Attach a port sketch or size code with your FerruleX RFQ so the factory quotes the correct cylinder-style body. Measure thread engagement depth and any undercut before assuming a standard male connector fits.',
        'subTitle': 'Specialty ports fail when a standard hex connector hits a shoulder or regulator casting. Measure thread engagement depth and any undercut before assuming a catalog male connector will seat. FerruleX holds common cylinder patterns in stock and cuts others after RFQ approval. Cylinder-style body for specialty ports. SS304 / SS316 / SS316L. Port drawing or size code with RFQ.',
        'bullets': [('Form', 'Cylinder-style body for specialty ports.'), ('Materials', 'SS304 / SS316 / SS316L.'), ('Ordering', 'Port drawing or size code with RFQ.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS316 / SS316L / SS304'), ('Series', 'Compression instrumentation'), ('Type', 'Cylinder connector'), ('Order mode', 'Factory RFQ')],
    },
    16: {
        'description': 'Compression Bulkhead Union: panel-pass stainless steel compression fittings, double ferrule. SS316/304. FerruleX RFQ. Stocked sizes ship fast. OEM RFQ welcome.',
        'content': 'Compression bulkhead unions pass instrumentation tubing through a panel wall with double ferrules on both sides. FerruleX bulkheads in SS316/SS316L/SS304 cover OD 3–25 mm / 1/8"–1" and lock with a bulkhead nut for enclosure thickness. Control cabinets, analyzer shelters and skid walls stay sealed without welding a tube stub through the plate. Standard duty is about 1000 PSI; confirm panel thickness and OD on the RFQ. FerruleX stocks frequent bulkhead sizes for fast factory shipping after quote. Drill the panel hole to the recommended diameter so the locknut seats flat without tilt.',
        'subTitle': 'Drill the panel hole to the bulkhead’s recommended diameter so the locknut seats flat without crushing the gasket face. If the wall is thicker than the nut stack allows, call it out — FerruleX can extend the shank on OEM lots. Label both sides of the panel during install so maintenance knows which nut is the process side.',
        'bullets': [('Mounting', 'Bulkhead locknut for panel thickness ranges.'), ('Seal', 'Double ferrule both sides of the wall.'), ('Pressure', '~1000 PSI; confirm panel thickness.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS316 / SS316L / SS304'), ('Tube OD', '3–25 mm / 1/8"–1"'), ('Type', 'Compression bulkhead union'), ('Pressure', '~1000 PSI')],
    },
    17: {
        'description': 'Compression / Quick-Screw Straight & Bulkhead: hybrid stainless fittings for mixed tube styles. FerruleX RFQ. Stocked sizes ship fast. Fast stock shipping.',
        'content': 'These hybrid straight and bulkhead connectors combine stainless steel compression fittings with quick-screw ends on one panel strategy. FerruleX offers compression OD 3–25 mm alongside quick-screw OD 4–16 mm in SS316/SS316L/SS304 so pneumatic and instrument tube can share a wall. Straight bodies handle inline joins; bulkhead versions pass through the enclosure. Both styles sit near 1000 PSI when correctly sized. Tell FerruleX which end is compression versus quick-screw, plus both OD values, on the factory RFQ for stocked hybrids. Keep BOM notes clear for each hybrid SKU so the warehouse does not issue a full-compression twin.',
        'subTitle': 'Mixed end styles stop you from forcing plastic pneumatic tube into a double-ferrule bite that was meant for hard stainless. Keep a clear BOM note for each SKU so the warehouse does not issue a full-compression twin by mistake. FerruleX kits hybrid bulkheads with the matching locknuts in one bag for panel assemblers.',
        'bullets': [('Styles', 'Straight and bulkhead; compression or quick-screw.'), ('Sizes', 'Match OD to the end style you select.'), ('Factory', 'Common hybrids stocked for export RFQs.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS316 / SS316L / SS304'), ('Compression OD', '3–25 mm / 1/8"–1"'), ('Quick-screw OD', '4–16 mm / 1/8"–1/2"'), ('Pressure', '~1000 PSI')],
    },
    18: {
        'description': 'Compression Cross Fitting: four-port stainless steel compression fittings for intersecting lines. FerruleX RFQ. Stocked sizes ship fast. Fast stock shipping.',
        'content': 'Compression cross fittings give four double-ferrule ports for intersecting instrumentation lines on one stainless body. FerruleX crosses in SS316/SS316L/SS304 cover OD 3–25 mm / 1/8"–1", equal or reducing. Calibration benches, multi-leg sample systems and complex manifolds use crosses instead of stacked tees. Expect about 1000 PSI on standard bodies. Confirm all four OD values on the FerruleX RFQ so reducing ports land on the correct legs before machining. Support nearby tubing; a cross should not be the only structural member in the manifold. Brand FerruleX; Material SS316 / SS316L / SS304; Tube OD 3–25 mm / 1/8"–1"; Type Compression cross; Pressure ~1000 PSI.',
        'subTitle': 'A cross concentrates stress at the center; support nearby tubing so the fitting is not the only structural member. Bleed and plug unused ports rather than leaving open ferrule pockets that collect debris. FerruleX can supply reducing crosses with two large and two small ports when the P&ID shows that split.',
        'bullets': [('Ports', 'Four equal or reducing compression ports.'), ('Seal', 'Double ferrule on each tube end.'), ('RFQ', 'All four OD values before ordering.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS316 / SS316L / SS304'), ('Tube OD', '3–25 mm / 1/8"–1"'), ('Type', 'Compression cross'), ('Pressure', '~1000 PSI')],
    },
    19: {
        'description': 'Ground Finish Tube to Male Connector: refined stainless steel compression fittings, tube to male. FerruleX RFQ. Stocked sizes ship fast. Fast stock shipping.',
        'content': 'Ground-finish tube-to-male connectors keep the exterior smoother for visible OEM panels while retaining double-ferrule sealing. FerruleX offers this stainless steel compression fitting in SS316/SS316L/SS304 for OD 3–25 mm / 1/8"–1" with NPT/G/metric male threads. Labs and export machines that leave fittings in plain sight prefer the ground look over a heavy machine finish. Function and pressure match the standard connector family near 1000 PSI. Request ground-finish explicitly on the FerruleX RFQ so stock is pulled from the correct bin. Electropolish or passivation certificates can be added on the same RFQ when QA requires them.',
        'subTitle': 'Ground finish is cosmetic and cleanability driven; it does not change the ferrule bite or allowable pressure by itself. If you also need electropolish or passivation certificates, add those notes to the same RFQ. FerruleX photographs ground-finish lots on request for customer approval before large OEM runs. Ground exterior for cleaner presentation. Double-ferrule tube to male thread. SS304 / SS316 / SS316L.',
        'bullets': [('Finish', 'Ground exterior for cleaner presentation.'), ('Function', 'Double-ferrule tube to male thread.'), ('Materials', 'SS304 / SS316 / SS316L.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS316 / SS316L / SS304'), ('Tube OD', '3–25 mm / 1/8"–1"'), ('Finish', 'Ground'), ('Threads', 'NPT / G / Metric')],
    },
    20: {
        'description': 'Ground Finish Reducing Union: polished-look stainless steel compression fittings, unequal OD. FerruleX RFQ. Stocked sizes ship fast. Export RFQ only — no cart.',
        'content': 'Ground-finish reducing unions transition unequal tube OD with a refined exterior for displayable stainless runs. FerruleX double-ferrule reducing unions in SS316/SS316L/SS304 sit inside the 3–25 mm / 1/8"–1" range. Medical device OEM, analytical benches and polished skids use them where every fitting stays visible after install. Sealing performance matches standard reducing unions at roughly 1000 PSI. Provide both tube OD values and request ground finish on your FerruleX factory RFQ. Do not substitute a standard machined union if the specification names ground finish explicitly.',
        'subTitle': 'Do not substitute a standard machined reducing union if the customer specification calls out ground finish by name. Wipe fingerprints before packaging; ground surfaces show handling marks more than bead-blasted parts. FerruleX can match ground-finish elbows and tees on the same PO for a uniform panel appearance. Ground body reduces machining marks. Reducing double-ferrule union. Both tube OD plus finish callout.',
        'bullets': [('Finish', 'Ground body reduces machining marks.'), ('Function', 'Reducing double-ferrule union.'), ('RFQ', 'Both tube OD plus finish callout.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS316 / SS316L / SS304'), ('Size range', 'OD 3–25 mm / 1/8"–1"'), ('Finish', 'Ground'), ('Type', 'Reducing union')],
    },
    21: {
        'description': 'Ground Finish Straight Union: equal tube stainless steel compression fittings with ground exterior. FerruleX RFQ. Stocked sizes ship fast. Fast stock shipping.',
        'content': 'Ground-finish straight unions join equal tube ends when the stainless steel compression fittings must look as good as they seal. FerruleX makes SS316/SS316L/SS304 ground unions for OD 3–25 mm / 1/8"–1". Export OEM panels that remain open-frame after FAT often specify this finish across the tubing bill. Pressure class mirrors standard unions near 1000 PSI. Order by tube OD with a ground-finish note on the FerruleX RFQ; common sizes are stocked. Keep finish grades segregated in stores so a rough body never lands on a show panel.',
        'subTitle': 'Ground unions are a drop-in dimensional twin of the standard union, so BOM swaps are usually painless. Still, keep finish grades segregated in stores so a rough body does not land on a show panel. FerruleX offers mixed cartons of ground and standard only when the RFQ lists both clearly.',
        'bullets': [('Pattern', 'Equal-size ground-finish union.'), ('Seal', 'Double-ferrule instrumentation seal.'), ('Stock', 'Common OD stocked at FerruleX.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS316 / SS316L / SS304'), ('Tube OD', '3–25 mm / 1/8"–1"'), ('Finish', 'Ground'), ('Type', 'Straight union')],
    },
    22: {
        'description': 'Ground Finish Male Elbow: 90° ground stainless steel compression fittings, tube to male. FerruleX RFQ. Stocked sizes ship fast. Export RFQ only — no cart.',
        'content': 'Ground-finish male elbows turn tube into a male port with a cleaner exterior for compact cabinets on display. FerruleX double-ferrule elbows in SS316/SS316L/SS304 cover OD 3–25 mm / 1/8"–1" with NPT/G/metric male threads. They solve the same space problem as standard male elbows while meeting appearance notes on OEM drawings. Instrumentation pressure near 1000 PSI applies unless you order HP. Call out ground finish, tube OD and male thread on the FerruleX factory RFQ. Align the elbow so the ground face outward if only one side is customer-visible after FAT.',
        'subTitle': 'Appearance grades still need correct ferrule pull-up; a shiny leak is still a leak on gas service. Align the elbow so the ground faces outward if only one side is customer-visible. FerruleX can supply touch-up notes if secondary machining nicks the ground surface on custom threads. 90° male elbow with ground exterior. NPT / G / metric male options. ~1000 PSI instrumentation duty.',
        'bullets': [('Geometry', '90° male elbow with ground exterior.'), ('Threads', 'NPT / G / metric male options.'), ('Pressure', '~1000 PSI instrumentation duty.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS316 / SS316L / SS304'), ('Tube OD', '3–25 mm / 1/8"–1"'), ('Finish', 'Ground'), ('Pattern', 'Male elbow')],
    },
    23: {
        'description': 'Forged Compression Elbow: forged-body stainless steel compression fittings for vibrating service. FerruleX RFQ. Stocked sizes ship fast. Fast stock shipping.',
        'content': 'Forged compression elbows start from a forged blank for higher mechanical toughness on instrument turns. FerruleX forges and machines SS316/SS316L/SS304 double-ferrule elbows for OD 3–25 mm / 1/8"–1". Marine skids, petrochemical trees and mobile equipment that shake continuously prefer forged bodies over light bar-stock elbows. Standard pressure is about 1000 PSI with HP series available. Ask FerruleX for forged elbows by tube OD on the RFQ; stocked sizes support fast delivery. Forge heat numbers can be stamped when your inspector requires them on the packing list.',
        'subTitle': 'Forged grain flow helps when fittings see repeated vibration that fatigues lighter bodies. It does not replace proper tube support clips along the run. FerruleX can stamp forge heat numbers when your inspector requires them on the packing list. Forged elbow blank for strength. Double-ferrule tube ends. SS304 / SS316 / SS316L.',
        'bullets': [('Body', 'Forged elbow blank for strength.'), ('Seal', 'Double-ferrule tube ends.'), ('Materials', 'SS304 / SS316 / SS316L.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS316 / SS316L / SS304'), ('Tube OD', '3–25 mm / 1/8"–1"'), ('Body', 'Forged'), ('Pressure', '~1000 PSI (HP series available)')],
    },
    24: {
        'description': 'Forged Compression Tee: forged stainless steel compression fittings for three-port branching. FerruleX RFQ. Stocked sizes ship fast. Export RFQ only — no cart.',
        'content': 'Forged compression tees branch three double-ferrule ports from a tough forged stainless body. FerruleX offers equal or reducing tees in SS316/SS316L/SS304 across OD 3–25 mm / 1/8"–1". High-cycle skids and outdoor instrument trees specify forged tees when vibration and impact are expected. Working pressure stays near 1000 PSI unless HP is requested. List run and branch OD on the FerruleX RFQ for stocked forged tees or OEM reducing blanks. Equal and reducing forged tees should be labeled separately so the wrong blank never reaches the skid.',
        'subTitle': 'Forged tees pair well with forged elbows when the entire tree sits on a vibrating package. Support the branch leg; a long cantilevered gauge still fatigues the port regardless of forge quality. FerruleX ships forged and bar-stock tees in separate labeled bags to prevent BOM confusion. Forged tee for impact and vibration resistance. Three compression tube ports. Equal or reducing branch OD.',
        'bullets': [('Body', 'Forged tee for impact and vibration resistance.'), ('Ports', 'Three compression tube ports.'), ('RFQ', 'Equal or reducing branch OD.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS316 / SS316L / SS304'), ('Tube OD', '3–25 mm / 1/8"–1"'), ('Body', 'Forged'), ('Type', 'Compression tee')],
    },
    25: {
        'description': 'Forged Compression Reducing Tee: forged stainless steel compression fittings, unequal branch. FerruleX RFQ. Stocked sizes ship fast. Export RFQ only — no cart.',
        'content': 'Forged reducing tees combine forged toughness with a smaller branch take-off for rugged sample and gauge trees. FerruleX machines these stainless steel compression fittings in SS316/SS316L/SS304 within OD 3–25 mm / 1/8"–1". Mobile analyzers and vibrating packages use them when a light reducing tee is not enough mechanically. Double ferrules seal every tube port; pressure follows the smaller branch near the usual 1000 PSI class. Give FerruleX both OD values on the RFQ for stocked or special forged reducing tees. If the branch sees pulsing sample flow, add a root valve on that leg during design review.',
        'subTitle': 'Reducing forged tees are easy to mis-pick against equal forged tees in a busy crib — label both OD sizes on the shelf. If the branch sees pulsing sample flow, consider a root valve on that leg as well. FerruleX quotes forge surcharges clearly when the blank must be custom reduced.',
        'bullets': [('Function', 'Forged reducing branch off main run.'), ('Seal', 'Double ferrule on tube ports.'), ('Factory', 'Special OD pairs after drawing review.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS316 / SS316L / SS304'), ('Size range', 'OD 3–25 mm / 1/8"–1"'), ('Body', 'Forged'), ('Type', 'Reducing tee')],
    },
    26: {
        'description': 'Forged Compression Cross Fitting: forged four-port stainless steel compression fittings. SS316/304. FerruleX RFQ. Stocked sizes ship fast. Fast stock shipping.',
        'content': 'Forged compression crosses put four double-ferrule ports on a forged body for tougher intersecting manifolds. FerruleX builds SS316/SS316L/SS304 crosses for OD 3–25 mm / 1/8"–1" aimed at mobile test carts and offshore instrument racks. The forge blank resists the knocks that light crosses see in the field. Standard pressure is about 1000 PSI; HP is available on request. Confirm equal or reducing port layout on the FerruleX factory RFQ before the cross is machined. Check panel hole clearance; forged crosses are heavier than light bar-stock crosses.',
        'subTitle': 'Four-port forged crosses are heavier; check panel hole clearance and wrench access before you commit the layout. Plug unused ports with matching compression plugs rather than leaving open nuts. FerruleX can balance reducing ports opposite each other when flow symmetry matters on the bench. Forged four-port cross. Double-ferrule instrumentation seal. ~1000 PSI class; HP on request.',
        'bullets': [('Body', 'Forged four-port cross.'), ('Seal', 'Double-ferrule instrumentation seal.'), ('Pressure', '~1000 PSI class; HP on request.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS316 / SS316L / SS304'), ('Tube OD', '3–25 mm / 1/8"–1"'), ('Body', 'Forged'), ('Type', 'Compression cross')],
    },
    27: {
        'description': 'Push-In Quick-Screw Fittings: stainless steel tube fittings, OD 4–16 mm, ~1000 PSI. SS304/316. FerruleX RFQ. Stocked sizes ship fast. Export RFQ only — no cart.',
        'content': 'Push-in quick-screw stainless steel tube fittings speed tube install on air and water lines without flare tools. FerruleX covers OD 4–16 mm and 1/8"–1/2" in SS304/SS316/SS316L: insert the tube, seat fully, then tighten the nut. Pneumatic cabinets, cooling loops and OEM machines that change tubing often favor this style over full compression. Working pressure is about 1000 PSI when tube and nut are correctly matched. Send your tube OD list to FerruleX for a factory RFQ; stocked sizes ship fast. Do not reuse a nut that was over-tightened onto scored tube — grab quality suffers.',
        'subTitle': 'Quick-screw joints forgive soft tube better than double-ferrule bites, but they still need a square cut and full insertion depth. Do not reuse a nut that has been over-tightened onto scored tube. FerruleX can kit elbows and tees with the same OD on one RFQ for a complete pneumatic panel.',
        'bullets': [('Install', 'Insert tube, seat fully, tighten nut — no flare tool.'), ('Sizes', 'OD 4–16 mm / 1/8"–1/2" typical.'), ('Materials', 'SS304 / SS316 corrosion resistance.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 / SS316 / SS316L'), ('Tube OD', '4–16 mm / 1/8"–1/2"'), ('Pressure', '~1000 PSI'), ('Type', 'Push-in quick-screw')],
    },
    28: {
        'description': 'Quick-Screw Straight Connector: stainless steel tube fittings, tube to thread, ~1000 PSI. FerruleX factory RFQ. Stocked sizes ship fast. Fast stock shipping.',
        'content': 'Quick-screw straight connectors take tube OD to male or female thread on plant air drops and light fluid lines. FerruleX stainless steel tube fittings in SS304/SS316/SS316L cover OD 4–16 mm / 1/8"–1/2" with NPT, G or metric threads. The straight body keeps pressure drop low compared with an elbow stack. About 1000 PSI is the usual working class. Quote tube OD and thread gender to FerruleX for stocked fast delivery after RFQ. Confirm male versus female thread ends before the blank is selected from stock bins.',
        'subTitle': 'Straight quick-screw connectors replace many plastic push fittings when the customer wants stainless in a washdown area. Confirm whether the thread end is male or female before the blank is selected. FerruleX bags connectors by thread code to speed kitting on multi-drop air headers. Straight body for low pressure drop. NPT, G or metric options. ~1000 PSI working class.',
        'bullets': [('Pattern', 'Straight body for low pressure drop.'), ('Threads', 'NPT, G or metric options.'), ('Pressure', '~1000 PSI working class.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 / SS316 / SS316L'), ('Tube OD', '4–16 mm / 1/8"–1/2"'), ('Type', 'Quick-screw straight'), ('Pressure', '~1000 PSI')],
    },
    29: {
        'description': 'Quick-Screw Female Connector: stainless steel tube fittings to female NPT/G ports. SS304/316. FerruleX RFQ. Stocked sizes ship fast. Export RFQ only — no cart.',
        'content': 'Quick-screw female connectors mate stainless tube to female-threaded valves, cylinders and manifolds. FerruleX builds SS304/SS316/SS316L bodies for OD 4–16 mm / 1/8"–1/2" with female NPT, G or metric. When the port is already female, this fitting removes an extra nipple from the stack. Duty is typically air and water near 1000 PSI. List tube OD and female thread on the FerruleX RFQ; common sizes are stocked for export. Use sealant only on the male thread make-up, never inside the quick-screw tube bore.',
        'subTitle': 'Female quick-screw connectors are popular on FRL outlets and solenoid banks that ship with NPT ports from the valve maker. Use thread sealant or tape only on the male side of the joint, not inside the quick-screw tube bore. FerruleX can match parallel G threads when BSPP is on the drawing instead of NPT.',
        'bullets': [('Ends', 'Tube quick-screw to female thread.'), ('Sizes', 'Metric and fractional tube OD.'), ('Stock', 'Common sizes stocked at FerruleX.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 / SS316 / SS316L'), ('Tube OD', '4–16 mm / 1/8"–1/2"'), ('Female threads', 'NPT / G / Metric'), ('Pressure', '~1000 PSI')],
    },
    30: {
        'description': 'Quick-Screw Straight Union: stainless steel tube fittings for equal tube-to-tube joins. FerruleX factory RFQ. Stocked sizes ship fast. Fast stock shipping.',
        'content': 'Quick-screw straight unions join two equal tube ends for inline repairs on pneumatic and water tubing. FerruleX stainless unions in SS304/SS316/SS316L cover OD 4–16 mm / 1/8"–1/2" with push-and-tighten make-up on both sides. No welding means a damaged hose segment can be swapped during a short maintenance window. Working pressure is about 1000 PSI. Order by tube OD from FerruleX on an RFQ; stocked unions leave the factory quickly. Cut both tube ends square so each side inserts to the same depth on the union.',
        'subTitle': 'Unions are the right break point when a soft tube run must be opened often for filter changes. Cut both tube ends square so each side inserts to the same depth. FerruleX can color-band large lots by OD for plants that stock multiple sizes in one crib. Equal-size quick-screw union. Push-and-tighten on both tube ends. SS304 / SS316 / SS316L.',
        'bullets': [('Connection', 'Equal-size quick-screw union.'), ('Install', 'Push-and-tighten on both tube ends.'), ('Materials', 'SS304 / SS316 / SS316L.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 / SS316 / SS316L'), ('Tube OD', '4–16 mm / 1/8"–1/2"'), ('Type', 'Quick-screw straight union'), ('Pressure', '~1000 PSI')],
    },
    31: {
        'description': 'Quick-Screw Elbow Connector: 90° stainless steel tube fittings for tight cabinets. OD 4–16 mm. FerruleX RFQ. Stocked sizes ship fast. Export RFQ only — no cart.',
        'content': 'Quick-screw elbow connectors route tube around tight corners to threaded ports without sharply bending soft tube. FerruleX 90° elbows in SS304/SS316/SS316L take OD 4–16 mm / 1/8"–1/2" with NPT, G or metric threads. Crowded OEM cabinets and machine sidewalls are the usual homes for this pattern. Air and water duty near 1000 PSI is typical. Give FerruleX tube OD and thread on the RFQ for stocked elbows with fast shipping. Leave free length after the elbow so tube is not strained against a cover plate.',
        'subTitle': 'Elbows protect polyurethane and nylon tube from kink damage that would otherwise create a leak under the jacket. Leave enough free length after the elbow so the tube is not strained against a cover plate. FerruleX offers male and female thread elbows in the same OD family for mixed port genders.',
        'bullets': [('Geometry', '90° elbow reduces bend stress on soft tube.'), ('Sizes', 'OD 4–16 mm with NPT/G/metric threads.'), ('Duty', '~1000 PSI air and water class.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 / SS316 / SS316L'), ('Tube OD', '4–16 mm / 1/8"–1/2"'), ('Pattern', 'Elbow'), ('Pressure', '~1000 PSI')],
    },
    32: {
        'description': 'Quick-Screw Tee Connector: three-way stainless steel tube fittings for air circuits. FerruleX factory RFQ. Stocked sizes ship fast. Export RFQ only — no cart.',
        'content': 'Quick-screw tee connectors branch a third leg from pneumatic or shared cooling tubing in stainless. FerruleX tees in SS304/SS316/SS316L cover OD 4–16 mm / 1/8"–1/2" for multi-actuator air circuits. One run feeds two devices without stacking plastic Y fittings that crack in washdown. Plan near 1000 PSI working pressure. List run OD, branch OD and any thread ports on the FerruleX RFQ for stocked or hybrid tees. Cap unused branches with matching plugs during phased commissioning of air circuits. Brand FerruleX; Material SS304 / SS316 / SS316L; Tube OD 4–16 mm / 1/8"–1/2"; Type Quick-screw tee; Pressure ~1000 PSI.',
        'subTitle': 'Balance branch lengths when two cylinders must stroke together; unequal restriction shows up as timing skew. Cap unused branches with matching quick-screw plugs during phased commissioning. FerruleX can supply equal tees and reducing tees under separate SKUs on one factory quote. Three-way quick-screw branching. SS304 / SS316 corrosion resistance. Run and branch OD with thread needs.',
        'bullets': [('Ports', 'Three-way quick-screw branching.'), ('Materials', 'SS304 / SS316 corrosion resistance.'), ('RFQ', 'Run and branch OD with thread needs.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 / SS316 / SS316L'), ('Tube OD', '4–16 mm / 1/8"–1/2"'), ('Type', 'Quick-screw tee'), ('Pressure', '~1000 PSI')],
    },
    33: {
        'description': 'Quick-Screw Bulkhead Connector: panel-pass stainless steel tube fittings, OD 4–16 mm. FerruleX factory RFQ. Stocked sizes ship fast. Export RFQ only — no cart.',
        'content': 'Quick-screw bulkhead connectors pass air or light fluid tubing through a panel with a locknut and quick-screw tube ends. FerruleX stainless steel tube fittings in SS304/SS316/SS316L cover OD 4–16 mm / 1/8"–1/2" at about 1000 PSI. Enclosure walls and skid panels stay sealed without welding stubs through the plate. This is a tube-fittings bulkhead, not a double-ferrule compression bulkhead — match the tube style accordingly. Confirm panel thickness and tube OD on the FerruleX RFQ for stocked bulkheads with fast delivery. Keep a spare locknut in the kit; it is the part most often dropped inside cabinets.',
        'subTitle': 'Drill the bulkhead hole cleanly so the locknut face sits flat; a tilted nut leaks past the panel gasket. If both sides of the wall use different OD tube, say so — FerruleX can machine a reducing bulkhead on RFQ. Keep a spare locknut in the commissioning kit; they are the part most often dropped inside cabinets.',
        'bullets': [('Mounting', 'Bulkhead nut locks through panel thickness.'), ('Sizes', 'OD 4–16 mm / 1/8"–1/2" quick-screw.'), ('Duty', '~1000 PSI pneumatic/water class.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 / SS316 / SS316L'), ('Tube OD', '4–16 mm / 1/8"–1/2"'), ('Type', 'Quick-screw bulkhead'), ('Pressure', '~1000 PSI')],
    },
    34: {
        'description': 'Barb Hose Connector: stainless barb to NPT/G/metric thread for soft hose. SS304/316. FerruleX RFQ. Stocked sizes ship fast. Export RFQ only — no cart.',
        'content': 'Barb hose connectors grip soft hose on one end and screw into NPT, G, ZG(R) or metric ports on the other. FerruleX offers SS304/SS316 barbs typically from 1/8"–1" with M5–M24 thread options; hose ID and clamp style set the real pressure limit (catalog notes up to ~3000 PSI depending on hose). Cooling drops, washdown lines and light process hose prefer barbs over ferrule tube when the media runs in elastomer hose. Always match barb OD to hose ID and use a proper clamp. Put hose ID, thread and media on the FerruleX factory RFQ. A barb without a clamp is unfinished — specify ear, worm or crimp clamps with the hose.',
        'subTitle': 'A barb without a clamp is not a finished joint — specify clamp type (ear, worm, or crimp) with the hose vendor. For food hose, ask whether the barb needs a smoother finish than industrial barbs. FerruleX can supply double-barb hose menders as a related line when you are splicing hose in the field.',
        'bullets': [('Ends', 'Barb stem to NPT, G, ZG(R) or metric.'), ('Sizes', 'Typically 1/8"–1" with M5–M24 threads.'), ('Note', 'Confirm hose ID and clamp on RFQ.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 / SS316'), ('Thread range', '1/8"–1" / M5–M24'), ('Type', 'Barb hose connector'), ('Pressure', 'Up to ~3000 PSI (hose limited)')],
    },
    35: {
        'description': 'Compression Plug Kit (3-Piece): blank unused stainless steel compression fittings ports. FerruleX factory RFQ. Stocked sizes ship fast. Fast stock shipping.',
        'content': 'The three-piece compression plug kit blanks unused double-ferrule ports with nut, ferrules and plug body as a set. FerruleX kits match the compression OD series 3–25 mm / 1/8"–1" in SS316/SS316L/SS304. Manifold commissioning, spare ports and temporary isolation use plugs instead of welding the port shut. They seal to the same practice as a tube make-up on that OD. Order by tube OD from FerruleX on RFQ; stocked kits ship with the matching ferrule orientation notes. Always use the ferrules that ship with the kit; mixing used ferrules invites leaks.',
        'subTitle': 'Always use the ferrules that ship with the kit; mixing used ferrules from a prior tube joint invites leaks. Label plugged ports on the P&ID so future techs know the blank is intentional. FerruleX can print OD on the plug head for cribs that stock many sizes. Nut, ferrules and plug body as a set. Matches FerruleX compression OD series. Seal unused ports without welding.',
        'bullets': [('Kit', 'Nut, ferrules and plug body as a set.'), ('Fit', 'Matches FerruleX compression OD series.'), ('Use', 'Seal unused ports without welding.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS316 / SS316L / SS304'), ('Compatibility', 'Compression OD 3–25 mm / 1/8"–1"'), ('Type', '3-piece plug kit'), ('Order mode', 'Factory RFQ')],
    },
    36: {
        'description': 'Compression Plug Insert: insert blank for stainless steel compression fittings ports. SS316/304. FerruleX RFQ. Stocked sizes ship fast. Fast stock shipping.',
        'content': 'Compression plug inserts seat inside the fitting to blank a tube port when a full three-piece kit is not required. FerruleX machines inserts in SS316/SS316L/SS304 for the double-ferrule OD you name on the RFQ. Service kits and field blanks use inserts to close a port that already has a nut on the body. They are not a substitute for the correct ferrule set if the nut is missing. State tube OD or fitting code on the FerruleX factory RFQ. Order a few extra inserts per OD; they disappear easily in field service bags.',
        'subTitle': 'Inserts are easy to lose in a parts bag — order a few extras for each OD on the skid. If the port will see frequent open/close cycles, prefer the full plug kit with fresh ferrules each time. FerruleX bags inserts by OD with desiccant for export shipments. Insert plug for double-ferrule ports. SS304 / SS316 / SS316L. Tube OD or fitting code.',
        'bullets': [('Part', 'Insert plug for double-ferrule ports.'), ('Materials', 'SS304 / SS316 / SS316L.'), ('RFQ', 'Tube OD or fitting code.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS316 / SS316L / SS304'), ('Type', 'Compression plug insert'), ('Series', 'Double ferrule'), ('Order mode', 'Factory RFQ')],
    },
    37: {
        'description': 'Hex Socket Plug: internal-hex stainless steel pipe fittings blank for female ports. SS304/316. FerruleX RFQ. Stocked sizes ship fast. Export RFQ only — no cart.',
        'content': 'Hex socket plugs seal female NPT, G or metric ports with an internal hex drive when external wrench clearance is gone. FerruleX stainless steel pipe fittings in SS304/SS316 drop into manifolds and valve bodies that sit flush to a wall. The recessed drive keeps the plug face tidy on compact blocks. Thread size drives the RFQ — there is no tube OD on this part. Ask FerruleX for the thread code and alloy; stocked plugs ship fast on factory quotes. Apply anti-gall compound appropriate to the media when seating stainless into stainless.',
        'subTitle': 'Use the correct hex key length so you do not round the socket under high seating torque. Apply thread sealant appropriate to the media; stainless dry threads can gall if you force them. FerruleX can supply plugs with nylon tip options when a soft seal face is on the drawing.',
        'bullets': [('Drive', 'Internal hex for recessed install.'), ('Threads', 'NPT, G or metric per RFQ.'), ('Materials', 'SS304 / SS316.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 / SS316'), ('Type', 'Hex socket plug'), ('Threads', 'NPT / G / Metric'), ('Order mode', 'Factory RFQ')],
    },
    38: {
        'description': 'Hex Head Plug: external-hex stainless steel pipe fittings blank for female ports. FerruleX factory RFQ. Stocked sizes ship fast. Export RFQ only — no cart.',
        'content': 'Hex head plugs blank female ports with external wrench flats for process blocks, cylinders and test points. FerruleX SS304/SS316 plugs cover common NPT, G and metric threads as durable stainless steel pipe fittings. They are the default blank when you have room to swing a wrench and want a robust head. No tube ferrule is involved — thread and alloy define the part. Send thread size and quantity to FerruleX for a factory RFQ with stocked fast delivery. Hex heads can be stamp-coded if QA wants each plugged port identified after FAT.',
        'subTitle': 'Hex heads mark easily with stamp codes if your QA wants each plugged port identified after FAT. Do not use an impact gun on fine instrumentation threads; hand torque is safer for stainless. FerruleX offers flanged-head variants when a stop shoulder is required — see those SKUs separately. External hex for standard wrenches. Threaded plug for female ports. SS304 / SS316.',
        'bullets': [('Drive', 'External hex for standard wrenches.'), ('Seal', 'Threaded plug for female ports.'), ('Materials', 'SS304 / SS316.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 / SS316'), ('Type', 'Hex head plug'), ('Threads', 'NPT / G / Metric'), ('Order mode', 'Factory RFQ')],
    },
    39: {
        'description': 'Flanged Hex Socket Plug: stainless plug with flange shoulder and internal hex. SS304/316. FerruleX RFQ. Stocked sizes ship fast. Export RFQ only — no cart.',
        'content': 'Flanged hex socket plugs add a sealing shoulder plus internal hex drive for ports that need a positive stop. FerruleX stainless steel pipe fittings in SS304/SS316 clean up the exterior after install compared with a plain socket plug. Hydraulic and pneumatic blocks that specify a flange face on the blank use this pattern. Thread size and any special flange OD belong on the RFQ. FerruleX quotes stocked and custom flanged socket plugs from the factory — RFQ only. The flange does not replace a gasket unless the block drawing calls for that seal method.',
        'subTitle': 'The flange does not replace a gasket unless the design calls for one; confirm sealing method with the block drawing. Internal hex still needs clear tool access even though the flange is present. FerruleX can match flange OD across a family of plugs when the casting pocket is shared. Flange shoulder plus internal hex. SS304 / SS316. Thread size and flange OD if special.',
        'bullets': [('Feature', 'Flange shoulder plus internal hex.'), ('Materials', 'SS304 / SS316.'), ('RFQ', 'Thread size and flange OD if special.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 / SS316'), ('Type', 'Flanged hex socket plug'), ('Threads', 'NPT / G / Metric'), ('Order mode', 'Factory RFQ')],
    },
    40: {
        'description': 'Flanged Hex Head Plug: stainless plug with hex head and flange stop. SS304/316. FerruleX factory RFQ. Stocked sizes ship fast. Export RFQ only — no cart.',
        'content': 'Flanged hex head plugs combine wrench flats with a flange stop for hydraulic and pneumatic blocks that want a shouldered blank. FerruleX machines SS304/SS316 stainless steel pipe fittings in common NPT/G/metric threads. The flange helps operators feel full make-up without guessing depth in a deep port. Stocked threads support fast factory shipping after RFQ. List thread and alloy preference for FerruleX; call out special flange OD when the pocket is nonstandard. Start the plug by hand before wrenching so the shoulder finds the seat without cross-threading.',
        'subTitle': 'Shouldered plugs are harder to cross-thread if you start them by hand before applying the wrench. If the flange must seal metal-to-metal, keep the face free of sealant blobs that hold it off the seat. FerruleX can etch thread size on the hex for cribs that mix many plugs in one drawer.',
        'bullets': [('Feature', 'Hex head with flange stop.'), ('Materials', 'SS304 / SS316.'), ('Stock', 'Common threads stocked for fast delivery.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 / SS316'), ('Type', 'Flanged hex head plug'), ('Threads', 'NPT / G / Metric'), ('Order mode', 'Factory RFQ')],
    },
    41: {
        'description': 'Square Head Plug: high-torque stainless steel pipe fittings blank with square drive. FerruleX RFQ. Stocked sizes ship fast. Export RFQ only — no cart.',
        'content': 'Square head plugs blank female ports when high seating torque and a square drive are preferred on heavy equipment. FerruleX SS304/SS316 stainless steel pipe fittings cover common plug threads for process valves and large blocks. The square head takes a wrench securely when hex heads round off under abuse. Permanent or semi-permanent blanks are the usual duty. Quote thread size to FerruleX on a factory RFQ; stocked plugs ship fast. Check guard clearance; square heads stand proud of socket plugs on mobile equipment. Brand FerruleX; Material SS304 / SS316; Type Square head plug; Threads NPT / G / Metric; Order mode Factory RFQ.',
        'subTitle': 'Square heads stick out farther than socket plugs — check guard clearance on mobile equipment. Anti-seize on stainless threads reduces galling when the plug may be removed years later. FerruleX can supply drilled and wired square heads when vibration lockwire is on the drawing. Square head for high seating torque. SS304 / SS316. Permanent or semi-permanent port blanks.',
        'bullets': [('Drive', 'Square head for high seating torque.'), ('Materials', 'SS304 / SS316.'), ('Use', 'Permanent or semi-permanent port blanks.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 / SS316'), ('Type', 'Square head plug'), ('Threads', 'NPT / G / Metric'), ('Order mode', 'Factory RFQ')],
    },
    42: {
        'description': 'Male-Female Straight Adapter: stainless steel pipe fittings converting NPT/G/metric threads. FerruleX RFQ. Stocked sizes ship fast. Export RFQ only — no cart.',
        'content': 'Male-female straight adapters convert thread standards or sizes inline without adding an elbow. FerruleX stainless steel pipe fittings in SS304/SS316 bridge NPT, G, ZG(R) and metric combinations for import equipment hook-ups. Low-profile straight bodies keep hose and tube aligned on crowded skids. List both thread codes on the RFQ — that pair is the entire specification. FerruleX stocks frequent NPT-to-G adapters for fast factory delivery after quote. If one side is tapered and the other parallel, confirm tape versus washer sealing on the RFQ.',
        'subTitle': 'Thread conversion errors are expensive; gauge both sides before you approve the packing list. If one side is tapered and the other parallel, confirm seal method (tape vs. washer) with the designer. FerruleX can laser both thread callouts on the hex for field identification. Thread standard or size adapter. Straight low-profile body. Both thread codes required.',
        'bullets': [('Function', 'Thread standard or size adapter.'), ('Pattern', 'Straight low-profile body.'), ('RFQ', 'Both thread codes required.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 / SS316'), ('Type', 'Male-female straight adapter'), ('Threads', 'NPT / G / ZG(R) / Metric'), ('Order mode', 'Factory RFQ')],
    },
    43: {
        'description': 'Male-Female Elbow Adapter: 90° stainless steel pipe fittings changing thread gender/standard. FerruleX RFQ. Stocked sizes ship fast. Export RFQ only — no cart.',
        'content': 'Male-female elbow adapters turn 90° while changing thread gender or standard in one stainless body. FerruleX SS304/SS316 fittings mix NPT/G/metric pairs for tight machine frames that need both direction change and conversion. They save a hose bend radius and an extra adapter stack. Both thread codes plus the elbow orientation note belong on the RFQ. FerruleX quotes stocked and special elbows from the factory for export OEM programs. Make up the fixed port before the hose end so the elbow does not clock wrong under torque.',
        'subTitle': 'Elbow adapters can clock wrong if you tighten the wrong end first — make up the fixed port before the hose end. Watch overall height when the elbow sits under a cover. FerruleX can supply street-elbow style genders when one side must be male into a female block. 90° adapter saves hose/tube bend radius. Mixed NPT/G/metric male-female pairs. SS304 / SS316.',
        'bullets': [('Geometry', '90° adapter saves hose/tube bend radius.'), ('Threads', 'Mixed NPT/G/metric male-female pairs.'), ('Materials', 'SS304 / SS316.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 / SS316'), ('Type', 'Male-female elbow adapter'), ('Threads', 'NPT / G / Metric'), ('Order mode', 'Factory RFQ')],
    },
    44: {
        'description': 'Female Threaded Tee: all-female stainless steel pipe fittings for branching headers. FerruleX factory RFQ. Stocked sizes ship fast. Export RFQ only — no cart.',
        'content': 'Female threaded tees branch air headers, water manifolds and gauge trees with three female ports. FerruleX stainless steel pipe fittings in SS304/SS316 cover common NPT, G and metric tee sizes, equal or reducing. They accept nipples and valves directly without male-to-female extras on every leg. Equal tees are stocked; reducing branches are RFQ items. Send port sizes to FerruleX for a factory quote with stocked fast delivery on standard equals. Consider orientation and drain legs on wet air headers where condensate collects in the tee. Brand FerruleX; Material SS304 / SS316; Type Female threaded tee; Threads NPT / G / Metric; Order mode Factory RFQ.',
        'subTitle': 'Tees collect condensate on wet air systems — consider orientation and drain legs when you lay out the header. Do not overtighten stainless into stainless without lubrication appropriate to the service. FerruleX can supply matching hex nipples as a companion line on the same RFQ. Three female threaded ports. SS304 / SS316. Equal or reducing branch sizes.',
        'bullets': [('Ports', 'Three female threaded ports.'), ('Materials', 'SS304 / SS316.'), ('RFQ', 'Equal or reducing branch sizes.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 / SS316'), ('Type', 'Female threaded tee'), ('Threads', 'NPT / G / Metric'), ('Order mode', 'Factory RFQ')],
    },
    45: {
        'description': 'Weld Straight Connector: stainless weld-end pipe/tube connector for permanent joints. SS304/316. FerruleX RFQ. Stocked sizes ship fast. Fast stock shipping.',
        'content': 'Weld straight connectors create permanent tube or pipe joins when demountable fittings are not wanted on the skid. FerruleX SS304/SS316 weld pieces follow the weld schedule and OD you put on the RFQ, including weld-to-thread variants. Process skids that prefer welded integrity over ferrule joints specify this pattern. Custom lengths and transitions are OEM work after drawing review. Attach the weld prep sketch to your FerruleX factory RFQ for accurate quoting. Protect threads on weld-by-thread variants from weld heat with caps and purge practice. Brand FerruleX; Material SS304 / SS316; Type Weld straight connector; Ends Weld (options per RFQ); Order mode Factory RFQ / OEM.',
        'subTitle': 'Weld connectors demand clean prep and purge practice; the fitting cannot fix a poor weld procedure. If one end stays threaded for a valve, protect that thread during welding heat. FerruleX ships weld blanks with end caps to keep bevels clean in transit. Weld prep for permanent installation. SS304 / SS316. Custom lengths and transitions from drawings.',
        'bullets': [('Ends', 'Weld prep for permanent installation.'), ('Materials', 'SS304 / SS316.'), ('OEM', 'Custom lengths and transitions from drawings.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 / SS316'), ('Type', 'Weld straight connector'), ('Ends', 'Weld (options per RFQ)'), ('Order mode', 'Factory RFQ / OEM')],
    },
    46: {
        'description': 'Straight Compression Ball Valve: stainless steel ball valve, double-ferrule ends, ~1000 PSI. SS304/316. FerruleX RFQ. Stocked sizes ship fast. OEM RFQ welcome.',
        'content': 'Straight compression-end stainless steel ball valves isolate instrumentation and process lines with a quarter-turn and low pressure drop. FerruleX builds SS304/SS316/SS316L bodies with double-ferrule ports matched to your tube OD, typically near 1000 PSI with HP series available. Panels, pneumatic lines and process skids use the straight pattern when flow should stay on axis. No elbow is buried in the valve, so Cv stays high for the tube size. Send tube OD, seat material and quantity to FerruleX for a factory RFQ — stocked sizes ship fast. Operate fully open or closed; throttling on a ball seat shortens seat life quickly.',
        'subTitle': 'Compression ball valves let you break the tube joint for valve service without cutting welded pipe. Operate the handle fully open or closed; throttling on a ball seat shortens life. FerruleX can add panel nuts on selected models when the valve mounts through a plate. Straight compression (double ferrule) ports. Quarter-turn shutoff with low Cv loss. ~1000 PSI standard; HP series available.',
        'bullets': [('Ends', 'Straight compression (double ferrule) ports.'), ('Action', 'Quarter-turn shutoff with low Cv loss.'), ('Pressure', '~1000 PSI standard; HP series available.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 / SS316 / SS316L'), ('Ends', 'Compression'), ('Pattern', 'Straight'), ('Pressure', '~1000 PSI (HP available)')],
    },
    47: {
        'description': 'Angle Compression Ball Valve: 90° stainless steel ball valve with double-ferrule ends. FerruleX factory RFQ. Stocked sizes ship fast. Export RFQ only — no cart.',
        'content': 'Angle compression stainless steel ball valves put shutoff and a 90° turn in one body for cramped panels. FerruleX SS304/SS316/SS316L valves use double-ferrule ends so wall-mounted instruments clear the cabinet without a separate elbow. OEM skids gain fewer leak points than valve-plus-elbow stacks. Pressure is typically about 1000 PSI. Quote tube OD and handle style to FerruleX; stocked angle valves support fast factory shipping. Wall clearance and handle swing must be checked against the enclosure drawing before lock-in. Brand FerruleX; Material SS304 / SS316 / SS316L; Ends Compression; Pattern Angle; Pressure ~1000 PSI.',
        'subTitle': 'Angle valves change the handle swing envelope — check door clearance before you commit the layout. Flow direction marks on the body matter when seats are not symmetric. FerruleX can soft-seat or hard-seat options depending on media notes on the RFQ. Angle body replaces elbow + valve stack. Double-ferrule compression. SS304 / SS316 / SS316L.',
        'bullets': [('Pattern', 'Angle body replaces elbow + valve stack.'), ('Ends', 'Double-ferrule compression.'), ('Materials', 'SS304 / SS316 / SS316L.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 / SS316 / SS316L'), ('Ends', 'Compression'), ('Pattern', 'Angle'), ('Pressure', '~1000 PSI')],
    },
    48: {
        'description': '3-Way Compression Ball Valve: diverting stainless steel ball valve with double-ferrule ports. FerruleX RFQ. Stocked sizes ship fast. Export RFQ only — no cart.',
        'content': 'Three-way compression stainless steel ball valves divert or mix instrument flows without breaking tube joints. FerruleX SS304/SS316/SS316L valves offer three double-ferrule ports for L or T path switching on sample and calibration loops. Dual-source selection and bypass legs are common uses. Confirm the porting diagram on the RFQ so the ball drilling matches your P&ID. FerruleX quotes stocked 3-way compression valves near 1000 PSI with factory RFQ pricing. Exercise every path during FAT so L-port versus T-port mistakes show up before ship.',
        'subTitle': '3-way valves are easy to order wrong if L-port and T-port are confused — attach a sketch. Exercise the handle through all positions during FAT to prove the intended paths. FerruleX can latch handles or add lockout provisions on OEM lots. Three compression ends for L or T paths. Quarter-turn diversion without breaking tubes. Porting diagram required.',
        'bullets': [('Ports', 'Three compression ends for L or T paths.'), ('Control', 'Quarter-turn diversion without breaking tubes.'), ('RFQ', 'Porting diagram required.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 / SS316 / SS316L'), ('Ends', 'Compression'), ('Pattern', '3-way'), ('Pressure', '~1000 PSI')],
    },
    49: {
        'description': 'Straight Quick-Screw Ball Valve: stainless steel ball valve with quick-screw tube ends. FerruleX factory RFQ. Stocked sizes ship fast. Fast stock shipping.',
        'content': 'Straight quick-screw stainless steel ball valves combine quarter-turn isolation with fast tube ends for air lines. FerruleX SS304/SS316/SS316L valves target OD in the 4–16 mm class at about 1000 PSI so pneumatic OEM machines get valve and fitting in one body. Straight flow keeps drops short on manifold legs. Media is typically compressed air or light fluids after confirmation. List tube OD and handle preference on the FerruleX RFQ for stocked valves with fast shipping. Do not force hard instrumentation tube into quick-screw ends meant for soft tube OD.',
        'subTitle': 'Quick-screw valve ends are not double-ferrule ends — do not force hard instrumentation tube into them. If the line later converts to stainless tube with ferrules, swap to a compression-end ball valve instead. FerruleX kits these valves with matching tube inserts when the OEM ships soft tube. Quick-screw tube connections. Straight flow path. Air and light fluid isolation.',
        'bullets': [('Ends', 'Quick-screw tube connections.'), ('Pattern', 'Straight flow path.'), ('Duty', 'Air and light fluid isolation.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 / SS316 / SS316L'), ('Ends', 'Quick-screw'), ('Pattern', 'Straight'), ('Pressure', '~1000 PSI')],
    },
    50: {
        'description': '3-Way Quick-Screw Ball Valve: diverting stainless steel ball valve with quick-screw ends. FerruleX RFQ. Stocked sizes ship fast. Export RFQ only — no cart.',
        'content': 'Three-way quick-screw stainless steel ball valves divert pneumatic paths while keeping push-style tube ends. FerruleX SS304/SS316/SS316L valves suit multi-circuit air panels and portable test equipment near 1000 PSI. Operators switch sources without breaking soft tube joints. Porting must be confirmed on the RFQ before the ball is drilled. FerruleX factory quotes cover stocked 3-way quick-screw valves for export OEM programs. Color-coded handles keep multi-circuit air panels readable when several 3-ways sit together. Brand FerruleX; Material SS304 / SS316 / SS316L; Ends Quick-screw; Pattern 3-way; Pressure ~1000 PSI.',
        'subTitle': 'Color-code handles when several 3-way valves sit on one panel so operators do not grab the wrong circuit. Soft tube still needs clamps or proper insertion depth at each quick-screw port. FerruleX can supply matching tees and elbows in the same OD for a full pneumatic kit.',
        'bullets': [('Ports', 'Three quick-screw tube ends.'), ('Function', 'Divert or select flow paths quickly.'), ('Materials', 'SS304 / SS316 ball valve construction.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 / SS316 / SS316L'), ('Ends', 'Quick-screw'), ('Pattern', '3-way'), ('Pressure', '~1000 PSI')],
    },
    51: {
        'description': 'Female Threaded Ball Valve: stainless steel ball valve with female NPT/G ends. SS304/316. FerruleX RFQ. Stocked sizes ship fast. Export RFQ only — no cart.',
        'content': 'Female threaded stainless steel ball valves isolate process headers, utility lines and equipment with NPT, G or metric ports. FerruleX SS304/SS316/SS316L valves cover common female sizes at roughly 1000 PSI for everyday shutoff duty. Full-port or reduced-port options depend on the size you request on the RFQ. No tube ferrule is involved — thread size is the key dimension. FerruleX stocks frequent female ball valves for fast factory shipping after quote. Support heavy actuators if automation is added later; body threads are not pipe hangers. Brand FerruleX; Material SS304 / SS316 / SS316L; Ends Female thread; Threads NPT / G / Metric; Pressure ~1000 PSI typical.',
        'subTitle': 'Female valves accept nipples from both sides, which simplifies header fabrication. Support heavy actuators if you later add automation; the body threads are not a pipe hanger. FerruleX can match lockable handles when site safety rules require them. Female NPT, G or metric threads. Full-port or reduced-port shutoff. Common sizes stocked at FerruleX.',
        'bullets': [('Ends', 'Female NPT, G or metric threads.'), ('Action', 'Full-port or reduced-port shutoff.'), ('Stock', 'Common sizes stocked at FerruleX.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 / SS316 / SS316L'), ('Ends', 'Female thread'), ('Threads', 'NPT / G / Metric'), ('Pressure', '~1000 PSI typical')],
    },
    52: {
        'description': 'Angle Female Ball Valve: 90° stainless steel ball valve with female threads. FerruleX factory RFQ. Stocked sizes ship fast. Export RFQ only — no cart.',
        'content': 'Angle female stainless steel ball valves give 90° shutoff on threaded wall outlets and compact machine frames. FerruleX SS304/SS316/SS316L valves use female NPT or G ends so you avoid a separate elbow on the drop. Pressure is typically about 1000 PSI. Handle swing and outlet direction should be checked against the enclosure drawing. Quote size and thread standard to FerruleX for stocked angle valves on factory RFQ. Confirm which port is inlet when seats are directional on the angle body you select. Brand FerruleX; Material SS304 / SS316 / SS316L; Ends Female thread; Pattern Angle; Pressure ~1000 PSI.',
        'subTitle': 'Angle female valves are popular under washdown stations where a straight valve would stick into the aisle. Confirm which port is inlet if the seat is directional. FerruleX can add a drain port option on custom angle bodies when winterization matters. Angle female body. NPT / G options. SS304 / SS316 / SS316L.',
        'bullets': [('Pattern', 'Angle female body.'), ('Threads', 'NPT / G options.'), ('Materials', 'SS304 / SS316 / SS316L.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 / SS316 / SS316L'), ('Ends', 'Female thread'), ('Pattern', 'Angle'), ('Pressure', '~1000 PSI')],
    },
    53: {
        'description': 'Female 3-Way Ball Valve: diverting stainless steel ball valve with female threads. FerruleX RFQ. Stocked sizes ship fast. Export RFQ only — no cart.',
        'content': 'Female 3-way stainless steel ball valves divert flow on threaded headers, bypass manifolds and dual-supply loops. FerruleX SS304/SS316/SS316L valves provide three female ports for L or T switching near typical 1000 PSI service. Quarter-turn operation keeps changeover fast during tests. Porting diagrams must accompany the RFQ. FerruleX factory pricing covers stocked and special female 3-way valves for export projects. Tag each port on the body during install so operators match the P&ID without guessing. Brand FerruleX; Material SS304 / SS316 / SS316L; Ends Female thread; Pattern 3-way; Pressure ~1000 PSI typical.',
        'subTitle': 'Tag each port on the valve body during install so future operators match the P&ID without guessing. Do not use a 3-way ball as a throttling valve for long periods. FerruleX can supply mounting pads when the valve needs to bolt to a panel. Three female threaded ends. Quarter-turn L/T path switching. Size and porting with FerruleX.',
        'bullets': [('Ports', 'Three female threaded ends.'), ('Control', 'Quarter-turn L/T path switching.'), ('RFQ', 'Size and porting with FerruleX.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 / SS316 / SS316L'), ('Ends', 'Female thread'), ('Pattern', '3-way'), ('Pressure', '~1000 PSI typical')],
    },
    54: {
        'description': 'Weld-End Ball Valve: stainless steel ball valve with weld prep for permanent lines. FerruleX factory RFQ. Stocked sizes ship fast. Export RFQ only — no cart.',
        'content': 'Weld-end stainless steel ball valves isolate permanent process lines that must not rely on threaded joints at the valve. FerruleX SS304/SS316/SS316L valves follow the weld schedule on your RFQ and sit near 1000 PSI in standard classes. Skids that ban demountable joints at isolation points specify weld ends. Custom end prep is available after drawing review. Attach weld details and size to the FerruleX factory RFQ for accurate quoting and stocked-body matches. Cap weld bevels in transit and keep seats cool during welding to avoid post-weld leaks.',
        'subTitle': 'Protect seats from weld heat with proper purge and cooling practice; a burned seat leaks after the first cycle. If one end must stay threaded for a instrument tap, ask for a weld-by-thread variant. FerruleX caps weld bevels for export so they arrive clean. Weld prep for permanent install. SS304 / SS316 ball valve. Custom end prep from drawings.',
        'bullets': [('Ends', 'Weld prep for permanent install.'), ('Materials', 'SS304 / SS316 ball valve.'), ('OEM', 'Custom end prep from drawings.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 / SS316 / SS316L'), ('Ends', 'Weld'), ('Type', 'Ball valve'), ('Pressure', '~1000 PSI typical')],
    },
    55: {
        'description': 'Mini Ball Valve: compact stainless steel ball valve for dense OEM panels. SS304/316. FerruleX RFQ. Stocked sizes ship fast. Export RFQ only — no cart.',
        'content': 'Mini stainless steel ball valves fit tight OEM panels and low-flow instrument isolation where a full-size valve will not clear. FerruleX SS304/SS316/SS316L mini bodies use small NPT/G or compact ends defined on the RFQ. Analytical instruments, gas panels and portable devices are typical homes. Cv is lower than full-size valves — confirm flow needs up front. Tell FerruleX the end style and size on the factory RFQ for stocked mini valves with fast shipping. Use light wrench make-up on tiny threads; mini handles round off easily under impact tools.',
        'subTitle': 'Mini handles are easy to over-torque; use finger-plus-light-wrench make-up on tiny threads. If the panel later grows flow demand, plan a larger valve footprint instead of forcing a mini past its Cv. FerruleX can color handles for gas species identification on multi-gas panels. Mini envelope for dense panels. SS304 / SS316. End style and Cv needs.',
        'bullets': [('Form', 'Mini envelope for dense panels.'), ('Materials', 'SS304 / SS316.'), ('RFQ', 'End style and Cv needs.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 / SS316 / SS316L'), ('Type', 'Mini ball valve'), ('Ends', 'Per RFQ (thread/compact)'), ('Order mode', 'Factory RFQ')],
    },
    56: {
        'description': 'High-Pressure Female Ball Valve: HP stainless steel ball valve, female thread. SS316 preferred. FerruleX RFQ. Stocked sizes ship fast. Fast stock shipping.',
        'content': 'High-pressure female stainless steel ball valves serve elevated system pressures on test benches and HP gas service after review. FerruleX SS304/SS316/SS316L HP series use female threads; allowable pressure depends on size and can approach the ~4500 PSI class when specified. SS316 is preferred for corrosive HP media. Design pressure, media and size must be on the RFQ before FerruleX confirms the body. Factory quotes cover HP female valves with stocked and special sizes — RFQ only. Match upstream fittings to the same HP class or the valve rating is meaningless in service.',
        'subTitle': 'HP valves need matching HP tubing and adapters; a standard 1000 PSI fitting upstream defeats the rating. Ask for hydrostatic test documentation when the end user requires it. FerruleX will not ship an HP valve against an incomplete pressure note on the RFQ. High-pressure female thread series. SS316 preferred for corrosive media. Design pressure, media and size.',
        'bullets': [('Duty', 'High-pressure female thread series.'), ('Materials', 'SS316 preferred for corrosive media.'), ('RFQ', 'Design pressure, media and size.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 / SS316 / SS316L'), ('Ends', 'Female thread'), ('Pressure', 'HP series (confirm on RFQ)'), ('Type', 'High-pressure ball valve')],
    },
    57: {
        'description': 'Air-Source Ball Valve: stainless steel ball valve for compressed-air headers and FRL feeds. FerruleX RFQ. Stocked sizes ship fast. Export RFQ only — no cart.',
        'content': 'Air-source stainless steel ball valves isolate compressed-air headers, FRL feeds and OEM pneumatic lines. FerruleX SS304/SS316 valves use utility thread sizes common to plant air and stock frequently for fast factory shipping. They are built for air service rather than aggressive chemicals — confirm media if you are outside air/water. Straight patterns dominate, with angle options on request. Send thread size and quantity to FerruleX on an RFQ for stocked air-line valves. Place the valve upstream of the FRL so filters can be serviced with the header isolated.',
        'subTitle': 'Put the air-source valve upstream of the FRL so filters can be serviced safely. Drain legs still need a separate petcock; this valve is isolation, not a water trap. FerruleX can lock handles in the closed position for lockout/tagout programs. Compressed air isolation. SS304 / SS316. Common air-line sizes stocked.',
        'bullets': [('Service', 'Compressed air isolation.'), ('Materials', 'SS304 / SS316.'), ('Stock', 'Common air-line sizes stocked.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 / SS316'), ('Type', 'Air-source ball valve'), ('Media', 'Compressed air'), ('Order mode', 'Factory RFQ')],
    },
    58: {
        'description': 'High-Pressure Compression Ball Valve: HP stainless steel ball valve with double ferrules. FerruleX RFQ. Stocked sizes ship fast. Export RFQ only — no cart.',
        'content': 'High-pressure compression stainless steel ball valves pair double-ferrule ends with HP shutoff for elevated instrument pressures. FerruleX SS316/SS316L/SS304 valves take tube OD directly so you avoid threaded adapters in the HP path, with ratings toward ~4500 PSI class when confirmed. Tube OD and design pressure are mandatory on the RFQ. Stocked HP compression valves ship after factory approval of the pressure note. Ask FerruleX for the matching HP tube wall recommendation when you quote. Replace ferrules if an HP gas joint is remade; reused ferrules are a common leak source.',
        'subTitle': 'Double-ferrule HP joints still need annealed tube and correct pull-up; pressure rating is not a substitute for installation care. Replace ferrules if a joint is remade on HP gas service. FerruleX can supply HP plugs and caps for unused branches on the same RFQ. Double-ferrule compression both sides. High-pressure ball shutoff. Tube OD + design pressure required.',
        'bullets': [('Ends', 'Double-ferrule compression both sides.'), ('Duty', 'High-pressure ball shutoff.'), ('RFQ', 'Tube OD + design pressure required.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS316 / SS316L / SS304'), ('Ends', 'Compression'), ('Pressure', 'HP series (confirm on RFQ)'), ('Type', 'HP compression ball valve')],
    },
    59: {
        'description': 'Hex-Body Compression Ball Valve: compact hex stainless steel ball valve, compression ends. FerruleX RFQ. Stocked sizes ship fast. Export RFQ only — no cart.',
        'content': 'Hex-body compression stainless steel ball valves shrink the envelope for dense OEM cabinets while keeping double-ferrule ports. FerruleX SS304/SS316/SS316L hex bodies give wrench flats where a round valve wastes space, typically near 1000 PSI. Tube OD defines the end size; the hex is about access, not a different pressure class by itself. Stocked hex valves support fast factory shipping after RFQ. List tube OD and handle style for FerruleX. Check handle interference against hex corners when valves sit side-by-side in a dense row. Brand FerruleX; Material SS304 / SS316 / SS316L; Ends Compression; Body Hex; Pressure ~1000 PSI.',
        'subTitle': 'Hex bodies help when valves sit side-by-side and round bodies would collide. Check handle interference against the hex corners during the open swing. FerruleX can shorten handles on request when adjacent instruments are tight. Short handles are available when adjacent instruments leave little swing room on the hex row.',
        'bullets': [('Body', 'Hex envelope for wrench flats.'), ('Ends', 'Compression tube ports.'), ('Materials', 'SS304 / SS316 / SS316L.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 / SS316 / SS316L'), ('Ends', 'Compression'), ('Body', 'Hex'), ('Pressure', '~1000 PSI')],
    },
    60: {
        'description': 'Long-Handle Hex Compression Ball Valve: hex stainless steel ball valve with extended lever. FerruleX RFQ. Stocked sizes ship fast. Export RFQ only — no cart.',
        'content': 'Long-handle hex compression stainless steel ball valves add leverage and visible handle position on field panels and skids. FerruleX SS304/SS316/SS316L hex bodies with double-ferrule ends typically work near 1000 PSI. Gloved operators and elevated valves benefit from the extended lever. Tube OD and handle length notes belong on the RFQ. FerruleX stocks common long-handle hex valves for fast factory delivery after quote. Extended levers need a clear swing arc beside cable trays and neighboring instruments. Brand FerruleX; Material SS304 / SS316 / SS316L; Ends Compression; Handle Long lever; Pressure ~1000 PSI.',
        'subTitle': 'Long handles need clear swing arcs — measure before you mount beside a cable tray. Bright handle covers improve position visibility in dark skids. FerruleX can supply spring-return handles only when that mechanism is explicitly requested. Bright handle covers help operators read open versus closed from across a dark skid aisle.',
        'bullets': [('Handle', 'Extended lever for leverage and visibility.'), ('Body', 'Hex compression ball valve.'), ('Materials', 'SS304 / SS316 / SS316L.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 / SS316 / SS316L'), ('Ends', 'Compression'), ('Handle', 'Long lever'), ('Pressure', '~1000 PSI')],
    },
    61: {
        'description': 'Straight Compression Needle Valve: stainless steel needle valve, double-ferrule, fine metering. FerruleX RFQ. Stocked sizes ship fast. Fast stock shipping.',
        'content': 'Straight compression stainless steel needle valves meter sampling, purge and gauge-isolation flows with a fine stem. FerruleX SS304/SS316/SS316L valves use double-ferrule ends so instrument tubing connects without threaded adapters. Straight bodies keep the panel layout linear when throttling accuracy matters more than full-bore shutoff. Tube OD and packing preference belong on the RFQ. FerruleX factory quotes cover stocked straight compression needle valves with fast shipping on common OD. Open slowly on high differential pressure to avoid stem wear and seat wire-drawing. Brand FerruleX; Material SS304 / SS316 / SS316L; Ends Compression; Pattern Straight; Type Needle valve.',
        'subTitle': 'Needle valves are for control, not as a substitute for a ball valve on frequent on/off duty. Open slowly on high differential pressure to avoid stem wear and seat wire-drawing. FerruleX can soft-tip stems when the RFQ notes delicate gases or vacuum service. Fine needle stem for metering. Double-ferrule compression. SS304 / SS316 / SS316L.',
        'bullets': [('Control', 'Fine needle stem for metering.'), ('Ends', 'Double-ferrule compression.'), ('Materials', 'SS304 / SS316 / SS316L.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 / SS316 / SS316L'), ('Ends', 'Compression'), ('Pattern', 'Straight'), ('Type', 'Needle valve')],
    },
    62: {
        'description': 'Angle Compression Needle Valve: 90° stainless steel needle valve with double ferrules. FerruleX RFQ. Stocked sizes ship fast. Export RFQ only — no cart.',
        'content': 'Angle compression stainless steel needle valves put fine metering on a 90° body for gauge boards and analyzer shelters. FerruleX SS304/SS316/SS316L valves take double-ferrule tube ends so the panel stays compact. Throttling stays precise while the angle clears depth limits behind the plate. Confirm tube OD and mounting style on the RFQ. FerruleX stocks frequent angle compression needle valves for factory RFQ shipping. Leave stem clearance under gauges so metering does not require removing the instrument. Brand FerruleX; Material SS304 / SS316 / SS316L; Ends Compression; Pattern Angle; Type Needle valve.',
        'subTitle': 'Angle needle valves often sit under gauges — leave stem clearance so operators can turn the handle without removing the gauge. Panel-mount options need the correct nut thickness for the plate. FerruleX can supply twin valve manifolds as a separate quote when two needles share a gauge. Angle body for panel mounting. Compression tube connections. Precise stainless steel needle valve throttling.',
        'bullets': [('Pattern', 'Angle body for panel mounting.'), ('Ends', 'Compression tube connections.'), ('Control', 'Precise stainless steel needle valve throttling.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 / SS316 / SS316L'), ('Ends', 'Compression'), ('Pattern', 'Angle'), ('Type', 'Needle valve')],
    },
    63: {
        'description': 'Forged Compression Needle Valve: forged-body stainless steel needle valve for vibration. FerruleX RFQ. Stocked sizes ship fast. Export RFQ only — no cart.',
        'content': 'Forged compression stainless steel needle valves use a forged blank for metering service that sees vibration. FerruleX SS304/SS316/SS316L valves keep double-ferrule ends for marine and mobile analyzer packages. Fine stem control remains the point; the forge body adds mechanical toughness around that stem. Tube OD and forge callout belong on the RFQ. FerruleX quotes forged compression needle valves from stocked blanks when OD matches, else OEM. Tube supports still matter; forged bodies help, but unsupported tube fatigues beside the valve. Brand FerruleX; Material SS304 / SS316 / SS316L; Ends Compression; Body Forged; Type Needle valve.',
        'subTitle': 'Forged needle valves still need tube supports; vibration fatigue often starts in the tube, not the body. Ask for packing materials compatible with the process temperature on the RFQ. FerruleX can heat-trace stamp forge lots when inspectors require it. Forged blank for durability. Double-ferrule compression. Fine flow control on instrument gas/liquid.',
        'bullets': [('Body', 'Forged blank for durability.'), ('Ends', 'Double-ferrule compression.'), ('Service', 'Fine flow control on instrument gas/liquid.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 / SS316 / SS316L'), ('Ends', 'Compression'), ('Body', 'Forged'), ('Type', 'Needle valve')],
    },
    64: {
        'description': 'Weld-End Needle Valve: stainless steel needle valve with weld prep for permanent metering. FerruleX RFQ. Stocked sizes ship fast. Export RFQ only — no cart.',
        'content': 'Weld-end stainless steel needle valves create permanent metering points on process tubing that cannot use demountable ferrules. FerruleX SS304/SS316/SS316L valves follow weld prep details on your RFQ for skids that ban tube fittings at the valve. Stem metering stays fine; only the ends change to weld. Custom weld ends are OEM after drawing review. Attach weld sketches and size to the FerruleX factory RFQ. Protect seats from weld heat with purge and cooling so the needle still meters smoothly. Brand FerruleX; Material SS304 / SS316 / SS316L; Ends Weld; Type Needle valve; Order mode Factory RFQ.',
        'subTitle': 'Keep seats cool during welding; a warped needle seat will never meter smoothly afterward. If future maintenance must remove the valve, reconsider a compression or threaded needle instead. FerruleX caps weld ends for clean arrival on export shipments. If future service must remove the valve, reconsider compression ends instead of permanent welds.',
        'bullets': [('Ends', 'Weld preparation.'), ('Control', 'Needle metering stem.'), ('OEM', 'Custom weld ends from drawings.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 / SS316 / SS316L'), ('Ends', 'Weld'), ('Type', 'Needle valve'), ('Order mode', 'Factory RFQ')],
    },
    65: {
        'description': 'Straight Female Needle Valve: stainless steel needle valve with female threads for manifolds. FerruleX RFQ. Stocked sizes ship fast. Export RFQ only — no cart.',
        'content': 'Straight female stainless steel needle valves isolate and meter on threaded instrument manifolds and gauge blocks. FerruleX SS304/SS316/SS316L valves use female NPT or G ports in a straight metering body. Bleed valves and gauge roots that already have male nipples prefer this pattern. Thread size is the primary RFQ dimension. FerruleX stocks common straight female needle valves for fast factory delivery after quote. Female ports take short nipples into gauges without stacking extra adapters on the block. Brand FerruleX; Material SS304 / SS316 / SS316L; Ends Female thread; Pattern Straight; Type Needle valve.',
        'subTitle': 'Female needles accept a short nipple into a gauge without adding a male-to-female adapter. Do not use them as the only shutoff on a high-energy line if a ball valve is required by code. FerruleX can soft-seat tips when the RFQ notes oxygen-clean or special gas service.',
        'bullets': [('Ends', 'Female threaded ports.'), ('Pattern', 'Straight metering body.'), ('Materials', 'SS304 / SS316 / SS316L.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 / SS316 / SS316L'), ('Ends', 'Female thread'), ('Pattern', 'Straight'), ('Type', 'Needle valve')],
    },
    66: {
        'description': 'Male-Female Straight Needle Valve: stainless steel needle valve bridging dissimilar threads. FerruleX RFQ. Stocked sizes ship fast. Export RFQ only — no cart.',
        'content': 'Male-female straight stainless steel needle valves meter while bridging dissimilar threaded ports on one body. FerruleX SS304/SS316/SS316L valves list both thread codes on the RFQ for retrofits between valves, gauges and adapters. Fine stem adjustment remains the control method. Straight pattern keeps the stack short. FerruleX factory quotes cover stocked and special male-female needle combinations for export OEM work. Write both thread callouts on the PO so receiving does not reverse gender on arrival. Brand FerruleX; Material SS304 / SS316 / SS316L; Ends Male × female thread; Pattern Straight; Type Needle valve.',
        'subTitle': 'Write both thread callouts on the PO line so receiving does not swap gender orientation. Make up the fixed port first, then the free port, to avoid twisting the stem packing. FerruleX can mark inlet/outlet when flow direction through the seat matters. Male and female threads on one valve. Fine needle adjustment. Both thread codes listed.',
        'bullets': [('Ends', 'Male and female threads on one valve.'), ('Control', 'Fine needle adjustment.'), ('RFQ', 'Both thread codes listed.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 / SS316 / SS316L'), ('Ends', 'Male × female thread'), ('Pattern', 'Straight'), ('Type', 'Needle valve')],
    },
    67: {
        'description': 'Angle Female Needle Valve: 90° stainless steel needle valve with female threads. FerruleX RFQ. Stocked sizes ship fast. Export RFQ only — no cart.',
        'content': 'Angle female stainless steel needle valves meter on a 90° female body for instrument boards with limited depth. FerruleX SS304/SS316/SS316L valves use female threads so wall outlets stay compact. Stem travel stays fine for purge and gauge control. Thread size and angle orientation notes belong on the RFQ. FerruleX stocks frequent angle female needle valves for factory RFQ shipping. Verify handle swing before drilling the plate or panel-depth savings disappear at the door. Brand FerruleX; Material SS304 / SS316 / SS316L; Ends Female thread; Pattern Angle; Type Needle valve.',
        'subTitle': 'Angle female needles free depth behind a panel when a straight valve would hit the back plate. Confirm handle clearance against adjacent gauges before drilling the panel. FerruleX can add a panel nut when the valve must clamp to the plate. Angle female body. Stainless steel needle valve stem. SS304 / SS316 / SS316L.',
        'bullets': [('Pattern', 'Angle female body.'), ('Control', 'Stainless steel needle valve stem.'), ('Materials', 'SS304 / SS316 / SS316L.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 / SS316 / SS316L'), ('Ends', 'Female thread'), ('Pattern', 'Angle'), ('Type', 'Needle valve')],
    },
    68: {
        'description': 'High-Pressure Female Globe Valve: HP stainless throttling valve, female thread. SS316 preferred. FerruleX RFQ. Stocked sizes ship fast. Fast stock shipping.',
        'content': 'High-pressure female globe-style valves throttle elevated-pressure gas or liquid after design review. FerruleX SS304/SS316/SS316L HP series use female threads; SS316 is preferred for corrosive HP media. They sit with the needle/globe family when fine control at pressure matters more than quarter-turn shutoff. Design pressure and Cv needs are mandatory on the RFQ. FerruleX confirms HP ratings before factory release — incomplete pressure notes delay the quote. Ask for hydrostatic certificates when the end user requires them on the same RFQ package. Brand FerruleX; Material SS304 / SS316 / SS316L; Ends Female thread; Pressure HP series (confirm on RFQ); Type High-pressure globe valve.',
        'subTitle': 'Globe/needle HP valves are not ball valves; expect more turns for shutoff and better throttling control. Match upstream fittings to the same HP class. FerruleX can provide hydrostatic certificates when the end user asks for them on the RFQ. High-pressure female globe / needle style. SS316 preferred for corrosive HP media. Design pressure and Cv required.',
        'bullets': [('Duty', 'High-pressure female globe / needle style.'), ('Materials', 'SS316 preferred for corrosive HP media.'), ('RFQ', 'Design pressure and Cv required.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 / SS316 / SS316L'), ('Ends', 'Female thread'), ('Pressure', 'HP series (confirm on RFQ)'), ('Type', 'High-pressure globe valve')],
    },
    69: {
        'description': 'Stainless Steel BA Tube: bright annealed instrumentation tube for compression fittings. SS304/316. FerruleX RFQ. Stocked sizes ship fast. Fast stock shipping.',
        'content': 'Bright annealed stainless steel BA tube gives clean ID/OD for gas panels, analyzers and double-ferrule systems. FerruleX supplies SS304/SS316/SS316L BA tube cut to length or as agreed on the RFQ, sized to pair with stainless steel compression fittings. Smooth annealed surface helps ferrules seal on instrumentation gas service. OD, wall, length and grade define the quote. FerruleX factory RFQs cover stocked BA cuts and custom lengths for export OEM kits. Keep hardness in the double-ferrule range; over-hard BA tube leaks on gas make-up.',
        'subTitle': 'BA tube hardness should stay in the range recommended for double-ferrule make-up; over-hard tube leaks on gas. Store coils and sticks capped so dirt does not score the sealing surface. FerruleX can certificate chemistry and anneal when the PO requires mill paper. Bright annealed tube surface. Sized for stainless steel compression fittings. OD, wall, length and grade.',
        'bullets': [('Finish', 'Bright annealed tube surface.'), ('Pairing', 'Sized for stainless steel compression fittings.'), ('RFQ', 'OD, wall, length and grade.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 / SS316 / SS316L'), ('Type', 'BA tube'), ('Finish', 'Bright annealed'), ('Order mode', 'Factory RFQ')],
    },
    70: {
        'description': 'Stainless Steel Precision Tube: tight-tolerance instrumentation tube for ferrule seals. FerruleX factory RFQ. Stocked sizes ship fast. Fast stock shipping.',
        'content': 'Precision stainless tube holds tight OD and wall tolerance so double-ferrule bites stay consistent on OEM machines. FerruleX SS304/SS316/SS316L precision tube is cut to RFQ lengths for analyzer plumbing and instrument racks. When ferrule sealing is critical, precision OD beats generic pipe tolerances. Specify OD, wall and tolerance band on the quote. FerruleX stocks common precision sizes and customs after drawing review — factory RFQ only. Square-cut and deburr every stick; tight OD tolerance cannot seal a burred tube end. Brand FerruleX; Material SS304 / SS316 / SS316L; Type Precision tube; Use Instrumentation; Order mode Factory RFQ.',
        'subTitle': 'Precision tube still needs a clean square cut; tolerance does not forgive a burred end under the ferrule. Ask for straightness notes if the tube runs long unsupported spans. FerruleX can match precision tube to a compression fitting lot on one combined RFQ. Precision OD for reliable double-ferrule sealing. SS304 / SS316 / SS316L. Cut lengths stocked or custom via RFQ.',
        'bullets': [('Tolerance', 'Precision OD for reliable double-ferrule sealing.'), ('Materials', 'SS304 / SS316 / SS316L.'), ('Factory', 'Cut lengths stocked or custom via RFQ.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 / SS316 / SS316L'), ('Type', 'Precision tube'), ('Use', 'Instrumentation'), ('Order mode', 'Factory RFQ')],
    },
    71: {
        'description': 'Stainless Steel Coil Tube: continuous stainless coil for long instrument runs. SS304/316. FerruleX RFQ. Stocked sizes ship fast. Export RFQ only — no cart.',
        'content': 'Stainless coil tube runs long instrument lengths without mid-couplings that add leak points. FerruleX SS304/SS316/SS316L coils are quoted by OD, wall and coil length for field tubing and OEM kits. Refrigeration-style instrument jumps and analyzer shelters often prefer coil over stick. Deburr and straighten only what you need; leave the rest coiled. Send coil length and size to FerruleX for a factory RFQ with stocked and special coils. Cap coil ends in storage so moisture does not stain the ID before the first cut. Brand FerruleX; Material SS304 / SS316 / SS316L; Type Coil tube; Form Coiled length; Order mode Factory RFQ.',
        'subTitle': 'Coil memory can fight you on short bends — anneal or use proper benders rather than forcing kinks. Cap coil ends in storage so moisture does not stain the ID before install. FerruleX can wind coils on smaller reels when air-freight limits apply. Continuous coil reduces joints. SS304 / SS316 / SS316L. Coil length, OD and wall thickness.',
        'bullets': [('Form', 'Continuous coil reduces joints.'), ('Materials', 'SS304 / SS316 / SS316L.'), ('RFQ', 'Coil length, OD and wall thickness.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 / SS316 / SS316L'), ('Type', 'Coil tube'), ('Form', 'Coiled length'), ('Order mode', 'Factory RFQ')],
    },
    72: {
        'description': 'Stainless Steel Corrugated Tube: corrugated SS hose/tube blank OD Φ6–Φ100 for OEM ends. FerruleX RFQ. Stocked sizes ship fast. Export RFQ only — no cart.',
        'content': 'Corrugated stainless tube stock gives OEM fabricators flexible stainless before they weld or assemble custom ends. FerruleX supplies SS304/SS316 corrugated tube in OD Φ6–Φ100; finished ends can be added on RFQ or left open. Fabricators who own weld cells buy blanks; plants that want finished hose should see the threaded/flanged hose SKUs. Length and OD drive the quote. Ask FerruleX for blank or finished options on the same factory RFQ. Specify end caps for export if open corrugated blanks ship internationally without finishing. Brand FerruleX; Material SS304 / SS316; OD range Φ6–Φ100; Type Corrugated tube; Order mode Factory RFQ.',
        'subTitle': 'Open corrugated tube arrives unprotected — specify end caps if it ships internationally. If you need KF or tri-clamp ends, order those finished hose SKUs instead of field-welding flanges without a procedure. FerruleX can corrugate special pitches when the drawing calls for a non-catalog flex rate. Corrugated stainless tube stock. OD Φ6–Φ100 typical. End finishing available on RFQ.',
        'bullets': [('Form', 'Corrugated stainless tube stock.'), ('Sizes', 'OD Φ6–Φ100 typical.'), ('OEM', 'End finishing available on RFQ.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 / SS316'), ('OD range', 'Φ6–Φ100'), ('Type', 'Corrugated tube'), ('Order mode', 'Factory RFQ')],
    },
    73: {
        'description': 'Tube Clamp: stainless clamp supporting instrumentation tubing against vibration. FerruleX factory RFQ. Stocked sizes ship fast. Export RFQ only — no cart.',
        'content': 'Tube clamps secure stainless instrument tubing to structure so vibration does not fatigue ferrule joints. FerruleX offers SS304/SS316 hardware matched to common instrument tube OD on the RFQ. Panels, skids and shipboard runs use clamps as cheap insurance against tube rattle. Spacing depends on OD and vibration level — the clamp does not replace design judgment. List tube OD and mount style for FerruleX factory quoting; stocked clamps ship fast. Place clamps near direction changes and heavy valves where vibration mass concentrates. Brand FerruleX; Material SS304 / SS316; Type Tube clamp; Fit Instrument tube OD; Order mode Factory RFQ.',
        'subTitle': 'Place clamps near changes of direction and beside heavy valves where mass concentrates. Plastic-lined clamps reduce wear on painted tube; say if you need that liner. FerruleX can supply multi-tube clamps when several lines run in parallel. Secures tubing to structure. Common instrument OD clamps. Stainless hardware options.',
        'bullets': [('Function', 'Secures tubing to structure.'), ('Sizes', 'Common instrument OD clamps.'), ('Materials', 'Stainless hardware options.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 / SS316'), ('Type', 'Tube clamp'), ('Fit', 'Instrument tube OD'), ('Order mode', 'Factory RFQ')],
    },
    74: {
        'description': 'Push-to-Connect Straight Fitting: stainless push-in tube fitting for air/water. SS304/316. FerruleX RFQ. Stocked sizes ship fast. Export RFQ only — no cart.',
        'content': 'Push-to-connect straight fittings join air or water tube with a click-in stainless body — no flare tools. FerruleX SS304/SS316 fittings typically sit in the 4–16 mm OD class; confirm exact OD on the RFQ. Pneumatic OEM and maintenance-friendly utility lines use them for rapid tube changes. Release the collar to remove tube; do not pry with screwdrivers that scar the OD. FerruleX factory RFQs cover stocked straight push-in fittings with fast shipping. Keep tube ovality in check after unreeling or the grab ring will not seat evenly.',
        'subTitle': 'Push-in stainless is still for compatible tube OD and hardness; forcing oversized tube ruins the grab ring. Keep tube ovality in check after unreeling. FerruleX can supply matching elbows and bulkheads in the same series on one quote. Push tube to click; release collar to remove. Straight body. SS304 / SS316.',
        'bullets': [('Install', 'Push tube to click; release collar to remove.'), ('Pattern', 'Straight body.'), ('Materials', 'SS304 / SS316.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 / SS316'), ('Type', 'Push-to-connect straight'), ('Media', 'Air / water (confirm)'), ('Order mode', 'Factory RFQ')],
    },
    75: {
        'description': 'Push-to-Connect Elbow Fitting: 90° stainless push-in fitting for crowded bases. FerruleX factory RFQ. Stocked sizes ship fast. Export RFQ only — no cart.',
        'content': 'Push-to-connect elbow fittings turn soft tube 90° in stainless without a sharp manual bend. FerruleX SS304/SS316 elbows serve crowded machine bases and control boxes in the push-in OD series on RFQ. No flaring tools are required — square-cut tube and push to depth. Air and light water service are typical after media confirmation. Order OD and quantity from FerruleX for stocked elbows with factory RFQ pricing. Keep a short straight segment into the elbow so the grab ring reaches full depth. Brand FerruleX; Material SS304 / SS316; Type Push-to-connect elbow; Pattern 90°; Order mode Factory RFQ.',
        'subTitle': 'Elbows reduce kink failures beside motors where tube must exit a tight corner. Leave a short straight segment into the elbow so the grab ring seats fully. FerruleX bags left/right if your BOM distinguishes orientation for molded tubes. Left and right orientations can be bagged separately when molded tube exits dictate a handed elbow.',
        'bullets': [('Geometry', '90° push-in elbow.'), ('Install', 'No flaring tools required.'), ('Materials', 'SS304 / SS316.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 / SS316'), ('Type', 'Push-to-connect elbow'), ('Pattern', '90°'), ('Order mode', 'Factory RFQ')],
    },
    76: {
        'description': 'Push-to-Connect Straight Union: stainless push-in tube-to-tube union. SS304/316. FerruleX RFQ. Stocked sizes ship fast. Export RFQ only — no cart.',
        'content': 'Push-to-connect straight unions join two equal tube OD ends for inline repairs and modular pneumatic assemblies. FerruleX SS304/SS316 unions use grab-ring ends on both sides in the push-in series sized on RFQ. Air and light fluid lines are typical after a media check. Swapping a damaged mid-section takes seconds compared with glued plastic unions. Quote tube OD to FerruleX for stocked unions with fast factory shipping. Mark insertion depth during training so technicians seat tube fully on every remake. Brand FerruleX; Material SS304 / SS316; Type Push-to-connect union; Pattern Straight; Order mode Factory RFQ.',
        'subTitle': 'Unions are the preferred break for filters that must come out of soft tube runs often. Mark insertion depth on the tube during training so techs seat fully every time. FerruleX can supply collet lock clips when vibration might creep the tube out. Tube-to-tube push union. SS304 / SS316. Air and light fluid lines after media check.',
        'bullets': [('Connection', 'Tube-to-tube push union.'), ('Materials', 'SS304 / SS316.'), ('Service', 'Air and light fluid lines after media check.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 / SS316'), ('Type', 'Push-to-connect union'), ('Pattern', 'Straight'), ('Order mode', 'Factory RFQ')],
    },
    77: {
        'description': 'Push-to-Connect Bulkhead Fitting: panel-pass stainless push-in fitting. SS304/316. FerruleX factory RFQ. Stocked sizes ship fast. Export RFQ only — no cart.',
        'content': 'Push-to-connect bulkhead fittings pass soft tube through a panel with a locknut and push-in ports on the tube side. FerruleX SS304/SS316 bulkheads suit enclosure walls on pneumatic OEM equipment in the push-in OD series. This is a tube-fittings bulkhead, not a compression bulkhead — use compatible tube only. Panel thickness and OD belong on the RFQ. FerruleX stocks common push-in bulkheads for fast factory delivery after quote. Tighten the bulkhead nut to the panel before inserting tube to avoid twisting the ring. Brand FerruleX; Material SS304 / SS316; Type Push-to-connect bulkhead; Mount Panel bulkhead; Order mode Factory RFQ.',
        'subTitle': 'Tighten the bulkhead nut to the panel before inserting tube so you do not twist the grab ring. If the cabinet is washed down, confirm gasket needs under the locknut face. FerruleX can extend shanks for thick insulated walls on OEM RFQs. Bulkhead lock for panel thickness. Push-to-connect tube ports. SS304 / SS316.',
        'bullets': [('Mounting', 'Bulkhead lock for panel thickness.'), ('Ends', 'Push-to-connect tube ports.'), ('Materials', 'SS304 / SS316.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 / SS316'), ('Type', 'Push-to-connect bulkhead'), ('Mount', 'Panel bulkhead'), ('Order mode', 'Factory RFQ')],
    },
    78: {
        'description': 'Y-Type and T-Type Tee Fitting: stainless Y/T branching pipe fittings, NPT/G/metric. FerruleX RFQ. Stocked sizes ship fast. Export RFQ only — no cart.',
        'content': 'Y-type and T-type tee fittings branch stainless headers for washdown, utilities and multi-leg lines. FerruleX SS304/SS316 stainless steel pipe fittings take male/female thread combinations listed on the RFQ. Y patterns split flow more gently; T patterns match standard header language. Port sizes and thread standard define the part. FerruleX factory quotes cover equal and reducing Y/T tees with stocked fast delivery on common equals. Choose Y when a sharp T has caused noise or erosion on prior utility headers. Brand FerruleX; Material SS304 / SS316; Type Y-type / T-type tee; Threads NPT / G / Metric; Order mode Factory RFQ.',
        'subTitle': 'Pick Y when erosion or noise at a sharp T branch has been a problem on slurry-light utilities. Do not assume a decorative Y is rated for the same pressure as a forged T without checking the RFQ reply. FerruleX can machine reducing Y legs when the branch is a utility take-off only.',
        'bullets': [('Patterns', 'Y-type and T-type branching.'), ('Materials', 'SS304 / SS316.'), ('RFQ', 'Port sizes and thread standard.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 / SS316'), ('Type', 'Y-type / T-type tee'), ('Threads', 'NPT / G / Metric'), ('Order mode', 'Factory RFQ')],
    },
    79: {
        'description': 'Investment Cast Elbow: economical stainless cast elbow for pipe direction changes. SS304/316. FerruleX RFQ. Stocked sizes ship fast. Export RFQ only — no cart.',
        'content': 'Investment cast elbows change direction on general stainless piping and OEM assemblies at a cast economy. FerruleX SS304/SS316 cast elbows follow sizes on the RFQ; non-standard angles are reviewed from drawings. They are cast fittings, not double-ferrule instrument elbows — use them on pipe threads or weld prep as specified. Stocked angles support fast factory shipping. Send size, end type and alloy to FerruleX for a factory RFQ. Check ID finish if the line is sanitary; cast may need polish beyond as-cast surfaces. Brand FerruleX; Material SS304 / SS316; Type Investment cast elbow; Process Investment casting; Order mode Factory RFQ.',
        'subTitle': 'Cast elbows suit utility stainless where forged instrumentation fittings would be oversized cost. Check ID finish if the line is sanitary; cast may need further polishing. FerruleX can quote matching cast tees on the same RFQ for a consistent cast family. Investment cast stainless elbow. SS304 / SS316. Non-standard angles from drawings.',
        'bullets': [('Process', 'Investment cast stainless elbow.'), ('Materials', 'SS304 / SS316.'), ('OEM', 'Non-standard angles from drawings.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 / SS316'), ('Type', 'Investment cast elbow'), ('Process', 'Investment casting'), ('Order mode', 'Factory RFQ')],
    },
    80: {
        'description': 'Investment Cast Tee: economical stainless cast tee for three-port branching. SS304/316. FerruleX RFQ. Stocked sizes ship fast. Export RFQ only — no cart.',
        'content': 'Investment cast tees branch utility stainless piping and OEM frames with three ports at cast pricing. FerruleX SS304/SS316 cast tees cover equal or reducing ports listed on the RFQ. They belong with cast elbows when the BOM standardizes on investment cast pipe fittings. Thread or weld ends follow the drawing — say which on the quote. FerruleX stocks common cast tees for fast factory delivery after RFQ. Label equal versus reducing cast tees in the crib — bodies look alike until ports are gauged. Brand FerruleX; Material SS304 / SS316; Type Investment cast tee; Process Investment casting; Order mode Factory RFQ.',
        'subTitle': 'Reducing cast tees need both port sizes on the label to avoid crib mix-ups with equals. Cast tees are not a substitute for forged high-pressure instrument tees on vibrating analyzer trees. FerruleX can passivate cast lots when the customer specification requires it. Investment cast tee body. SS304 / SS316. Equal or reducing ports.',
        'bullets': [('Process', 'Investment cast tee body.'), ('Materials', 'SS304 / SS316.'), ('RFQ', 'Equal or reducing ports.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 / SS316'), ('Type', 'Investment cast tee'), ('Process', 'Investment casting'), ('Order mode', 'Factory RFQ')],
    },
    82: {
        'description': 'Investment Cast Ball Valve: cast-body stainless steel ball valve for utility shutoff. SS304/316. FerruleX RFQ. Stocked sizes ship fast. Fast stock shipping.',
        'content': 'Investment cast stainless steel ball valves balance cost and corrosion resistance for water, air and light process isolation. FerruleX SS304/SS316 cast bodies with threaded ends suit OEM equipment that does not need forged instrument valves. Quarter-turn shutoff is the function; size, thread and seat material define the RFQ. Stocked cast valves support fast factory shipping. Ask FerruleX for seat options (PTFE, etc.) when media temperature needs them. Confirm pressure class before using cast utility valves on elevated HP service. Brand FerruleX; Material SS304 / SS316; Type Investment cast ball valve; Process Investment casting; Order mode Factory RFQ.',
        'subTitle': 'Cast ball valves are utility workhorses — confirm pressure class before using them on elevated HP service. If you need compression ends, see the compression ball valve SKUs instead. FerruleX can lock handles for LOTO on cast valves when site rules require it. Investment cast body and ends. Quarter-turn stainless steel ball valve shutoff. Size, thread and seat material.',
        'bullets': [('Process', 'Investment cast body and ends.'), ('Function', 'Quarter-turn stainless steel ball valve shutoff.'), ('RFQ', 'Size, thread and seat material.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 / SS316'), ('Type', 'Investment cast ball valve'), ('Process', 'Investment casting'), ('Order mode', 'Factory RFQ')],
    },
    84: {
        'description': 'Pneumatic Silencer: stainless exhaust muffler for solenoid and cylinder vents. FerruleX factory RFQ. Stocked sizes ship fast. Export RFQ only — no cart.',
        'content': 'Pneumatic silencers / mufflers cut exhaust noise on solenoid valves and cylinder vents in OEM machines. FerruleX offers SS304 (series dependent) silencers that thread into common pneumatic exhaust ports. Flow capacity and thread size drive the selection more than tube OD. Plant air exhausts and packaging machines are typical installs. Send thread size and required flow to FerruleX for a factory RFQ; stocked silencers ship fast. Match silencer flow to the valve exhaust path or cylinder return time will suffer. Brand FerruleX; Material SS304 (series dependent); Type Pneumatic silencer; Mount Threaded exhaust; Order mode Factory RFQ.',
        'subTitle': 'A silencer that is too restrictive slows cylinder return — match Cv to the valve’s exhaust path. Keep sintered elements clean; oil-laden air can clog them and raise backpressure. FerruleX can supply elbow silencers when the exhaust must turn away from operators. Attenuates pneumatic exhaust noise. Threaded into exhaust ports. Thread size and flow capacity.',
        'bullets': [('Function', 'Attenuates pneumatic exhaust noise.'), ('Mount', 'Threaded into exhaust ports.'), ('RFQ', 'Thread size and flow capacity.')],
        'specs': [('Brand', 'FerruleX'), ('Material', 'SS304 (series dependent)'), ('Type', 'Pneumatic silencer'), ('Mount', 'Threaded exhaust'), ('Order mode', 'Factory RFQ')],
    },
}


def esc(s: str) -> str:
    return s.replace("'", "''")


def rewrite_file(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    title_m = re.search(r"^title:\s*'((?:''|[^'])*)'", text, re.M)
    category_m = re.search(r"^category:\s*'((?:''|[^'])*)'", text, re.M)
    slug_m = re.search(r"^slug:\s*'((?:''|[^'])*)'", text, re.M)
    id_m = re.search(r"^  id:\s*(\d+)", text, re.M)
    img_card_m = re.search(r"imgCard:\s*'([^']+)'", text)
    img_main_m = re.search(r"imgMain:\s*'([^']+)'", text)
    if not all([title_m, category_m, slug_m, id_m, img_card_m, img_main_m]):
        raise RuntimeError(f"Incomplete frontmatter: {path.name}")
    title = title_m.group(1).replace("''", "'")
    category = category_m.group(1)
    slug = slug_m.group(1)
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
