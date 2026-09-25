---
title: 'Full Port vs Reduced Port Ball Valves'
description: 'Full port vs reduced port stainless ball valves: flow coefficient, pressure drop, pigging and when a reduced bore valve is the right cheap choice.'
category: 'installation-guides'
slug: 'full-port-vs-reduced-port-ball-valves'
author: 'FerruleX Factory'
authorImage: '@/images/ferrulex-logo.png'
authorImageAlt: 'FerruleX author'
pubDate: 2026-09-25
cardImage: '@/images/products/p09-54-weld-end-ball-valve.jpg'
cardImageAlt: 'Stainless steel weld-end ball valve inline with the flow path'
readTime: 4
tags: ['full port ball valve', 'reduced port', 'stainless steel ball valve', 'ball valve bore']
---

A **stainless steel ball valve full port** design has a ball opening the same size as the pipe bore; a **reduced port** (reduced bore) valve narrows the flow path through the ball. Everything else — body, seats, handle — can be identical, and the bore alone changes price, pressure drop and what you can push through the line.

> **Key takeaways**
>
> - A full port 1-inch stainless ball valve flows at Cv ~40 versus Cv ~15–25 for a reduced port valve of the same size — the bore alone changes price, pressure drop and what you can push through the line.
> - Reduced port is the right call for most utility isolation, tank drains and branch shutoff; full port is mandatory on pump suction lines, pigged or probed lines, and sanitary transfer.
> - A 1-inch reduced port valve and a 1-inch full port valve share end connections but not hydraulics, so swapping one for the other on a balanced loop quietly redistributes flow — quote Cv on the RFQ, not just nominal size.

## What the port actually is

The port is the drilled hole through the ball. In a full port (full bore) 1" valve, that hole is 1". In a standard reduced port valve it is typically one pipe size smaller — a 1" valve with a ~3/4" bore — though ratios vary by maker. Because the ball is smaller and lighter, reduced port valves cost less, weigh less and torque lower. A side benefit: for the same body size, the reduced ball allows a thicker body wall, which is one reason high-pressure compact valves are often reduced bore.

## Flow: the numbers that matter

A full port valve adds almost no restriction — its flow coefficient (Cv) approaches that of straight pipe. A reduced port valve acts like a short, abrupt contraction and expansion. In a 1" water line at 3 m/s, the reduced port might add the equivalent of several metres of pipe in pressure drop. That is negligible on a drain valve and meaningful on a pumped recirculation loop running near its curve.

Rule of thumb: if the valve is throttling flow continuously, neither type is right — use a control valve or needle valve. Ball valves are for shutoff, and the port question is about what happens when they are fully open.

## Side by side

| Factor             | Full port                     | Reduced port                  |
| ------------------ | ----------------------------- | ----------------------------- |
| Bore vs pipe       | Equal                         | Smaller (often one size down) |
| Pressure drop      | Minimal                       | Noticeable at high flow       |
| Cv (1" SS valve)   | ~40                           | ~15–25                        |
| Pigging / swabbing | Passes pigs and probes        | Blocks them                   |
| Slurries / solids  | Resists clogging              | Can trap at the bore          |
| Cost & weight      | Higher, heavier ball          | Cheaper, lighter              |
| Typical use        | Manifolds, pump suction, CIP  | Utilities, drain, isolation   |

## When reduced port is the right call

Most of the time, honestly. Utility isolation, tank drains, sample points and branch shutoff valves see intermittent flow at modest velocity, and a reduced port valve performs identically for less money. The smaller bore also survives cavitation-prone spots slightly better because of the thicker body around it. Our [female threaded ball valve](/products/female-threaded-ball-valve/) line ships both bores for exactly this reason — ask which bore the stocked size carries when you RFQ.

## When you must go full port

- **Pump suction lines:** added restriction at the suction raises NPSH requirements and can invite cavitation. Go full bore.
- **Pigged or probed lines:** inspection pigs, foam swabs and sampling probes need pipe-size passage. Reduced bore stops them cold.
- **High-velocity transfer or recirculation:** compute the pressure drop at design flow; if the valve's Cv costs you more than a few percent of pump head, go full port.
- **Sanitary transfer:** full bore with tri-clamp ends avoids product hold-up at the bore step. See [tri-clamp fittings](/blog/what-are-tri-clamp-fittings/) for the clamp side.

## One trap: "same size" valves that are not

A 1" reduced port valve and a 1" full port valve share end connections but not hydraulics. Swapping one for the other on a balanced loop quietly changes flow distribution across branches. If your line schedule calls out Cv values, quote the valve's Cv on the RFQ, not just the nominal size — the [ball valve category](/products/ball-valves/) lists stocked bores per size.

## FAQ

**Does port size affect pressure rating?**
No directly — rating comes from body and seat design. But reduced bore valves often rate slightly higher in compact bodies because of the thicker wall, and full port high-pressure valves get large and expensive fast.

**Can a pig pass through a full port ball valve?**
Yes, that is the point of full bore. The ball must be fully open; a partially open full port valve is still a blockage and will destroy the pig.

**Is Cv the same as port diameter?**
No. Cv is the measured flow capacity (US gpm of water at 1 PSI drop). Port diameter drives Cv, but body geometry matters too — compare Cv on the datasheet, not bore on a drawing.

**Which bore do compression-end ball valves usually have?**
Compact compression valves are typically reduced bore for the same cost and wall-thickness reasons. If you need full flow at compression ends, say so on the RFQ — it changes the body casting.

**Reduced port for slurry service: acceptable?**
Avoid it. The bore step is a trap for settled solids and a wear point for abrasive flow. Full bore, hard-faced seats, or a different valve style entirely.
