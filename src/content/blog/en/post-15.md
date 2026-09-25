---
title: 'Ball Valve Ratings Explained: 1000 WOG vs 2000/3000 PSI'
description: 'What 1000 WOG, 2000 PSI and 3000 PSI stainless ball valve ratings actually mean, how temperature derates them, and how to spec the right pressure class.'
category: 'installation-guides'
slug: 'ball-valve-ratings-explained'
author: 'FerruleX Factory'
authorImage: '@/images/ferrulex-logo.png'
authorImageAlt: 'FerruleX author'
pubDate: 2026-09-25
cardImage: '@/images/products/p10-58-high-pressure-compression-ball-valve.jpg'
cardImageAlt: 'High-pressure stainless steel ball valve rated above 1000 WOG'
readTime: 4
tags: ['ball valve pressure rating', '1000 WOG', 'stainless steel ball valve', 'high pressure ball valve']
---

Every **stainless steel ball valve pressure rating** printed on a datasheet answers one question: how much pressure the valve holds before something in it — body, seat or stem — gives way. Two rating systems dominate the fittings trade, and mixing them up is how a valve lands on a line it was never meant to hold.

> **Key takeaways**
>
> - A "1000 WOG" stainless ball valve holds 1000 psig on water, oil or gas at ambient temperature — and the WOG number says nothing about steam, where a separate WSP rating is usually far lower.
> - An ASME Class 300 flanged ball valve is roughly a 740-psig valve at ambient — Class ratings are flange standards, not body classes, so "Class 300" never means "300 PSI."
> - Pressure ratings are cold ratings: a PTFE-seated stainless valve at 200 °C carries roughly 65–75% of its cold rating and at 250 °C about half, so most premature valve deaths are thermal, not pressure, events.

## What 1000 WOG means

**WOG** stands for Water, Oil, Gas — the cold, non-shock working pressures the valve is rated for in each of those benign services. A "1000 WOG" stainless ball valve therefore holds 1000 psig at ambient temperature on water, oil or gas. It is the standard class for threaded 2-piece SS304/SS316 ball valves in general utility service, and it is what most catalog pages mean by "standard pressure."

WOG tells you nothing about steam, vacuum cycling or corrosive media. For steam you need the valve's separate steam rating — usually far lower than the WOG number — and for aggressive chemicals the seat and body material matter more than the number itself.

## What 2000 PSI and 3000 PSI mean

The plain-PSI classes (2000, 3000 and beyond) describe reinforced valves: thicker bodies, metal or glass-filled PTFE seats, blowout-proof stems and, on the highest classes, special end connections. A 2000 PSI valve is not a 1000 WOG valve with optimism printed on it — the body, stem and seat system are all upgraded. Our [high-pressure female ball valve](/products/high-pressure-female-ball-valve/) and [high-pressure compression ball valve](/products/high-pressure-compression-ball-valve/) sit in these classes for instrument and process duty.

There is also a parallel system worth knowing: class ratings like [ASME Class 150/300/600](https://www.asme.org/codes-standards/find-codes-standards/b16-34-valves-flanged-threaded-welding-end) used on flanged valves. Those are flange standards, not body classes — a Class 300 flanged ball valve is roughly a 740-psig valve at ambient. Do not equate "Class 300" with "300 PSI."

## How temperature derates the rating

Pressure ratings are cold ratings. As temperature rises, the body and seat material lose strength, and the maker's derating table takes over. Typical behavior for a PTFE-seated stainless valve:

| Temperature  | Share of cold rating | Note                                    |
| ------------ | -------------------- | --------------------------------------- |
| Up to ~80 °C | Full rating          | —                                       |
| 150 °C       | ~85–90%              | —                                       |
| 200 °C       | ~65–75%              | —                                       |
| 250 °C       | ~50%                 | PTFE seats are near their practical limit |

A 1000 WOG valve on a 200 °C hot oil loop is a ~700 PSI valve. Check the derating curve, not the headline number.

## Gas service and the second pressure number

Gas rating involves a subtler limit: the pressure at which escaping gas could ignite from static or adiabatic heating. Many general-service ball valves carry a second, lower figure for gas — for example 1000 WOG / a lower psig gas rating. If your line carries compressed air, nitrogen, fuel gas or oxygen, quote the valve against the **gas rating**, not WOG. Oxygen service adds a cleanliness requirement on top: no oil, no grease, degreased assembly.

## Choosing the class

- **Plant utilities, water, air under 1000 psig, general shutoff:** 1000 WOG threaded or compression-end valves cover the vast majority of duty. Browse the [ball valve category](/products/ball-valves/) for stocked classes.
- **Instrument panels, hydraulic power units, CNG skids, high-pressure process:** move to 2000/3000 PSI reinforced bodies with metal or filled seats.
- **Anything with thermal shock, vibration or frequent cycling:** derate one class and specify a blowout-proof stem — the stem, not the seat, is what usually fails first under cyclic load.

Whichever class you pick, [hydrostatic shell and seat testing at 1.5× and 1.1× rated pressure](https://www.iso.org/standard/65111.html) respectively is the norm for a factory-tested valve. Ask for the test certificate on the RFQ for HP classes.

## FAQ

**Is 1000 WOG the same as 1000 PSI?**
On water, oil or gas at ambient temperature, effectively yes. But WOG is a service-specific rating — it does not extend to steam or high temperature, where the valve must be derated or separately rated.

**Can I use a 1000 WOG valve on 800 PSI air?**
Check the datasheet's gas rating, not just WOG. Many 1000 WOG valves carry a lower gas rating because of ignition risk at the seat. If the gas rating covers 800 PSI, fine; if not, spec up.

**What derates a ball valve fastest: heat or pressure?**
Heat. Pressure within rating is a static load the body handles with margin; heat softens seats, raises stem friction and accelerates wear. Most premature valve deaths are thermal, not pressure, events.

**Do compression-end ball valves rate the same as threaded?**
The body class can be identical, but the compression end itself adds a fitting rating — the assembly is limited by its weaker link. Our [high-pressure compression ball valve](/products/high-pressure-compression-ball-valve/) is matched as a complete assembly for that reason.

**What is the difference between WOG and WSP?**
WSP is Working Steam Pressure — the steam-specific rating, always much lower than WOG. A valve marked 1000 WOG might carry a WSP of only 150 PSI.
