# Phase 4 — needle & check valve cluster (4 new posts)

**For**: Kimi (content agent)
**From**: Claude Code, 2026-09-25 (continuation of the 19-post program)
**Constraints**: same as PHASE3_POSTS.md — BLOG_PLAN.md ground rules,
AI_GUIDE.md conventions, verified facts only, no `git commit`.

## Step 0 — fix Phase 3 leftovers first

post-19 and post-21 are the only two new posts without a markdown table:

- post-19: convert the spec-checklist list into a table
  (Parameter | Why it matters | Typical mistake) using facts already present.
- post-21: convert the five-failure-modes list into a table
  (Failure mode | Root cause | Early signal / prevention), same rule.

Rebuild and confirm FAQPage still 1 for both.

## Files to create

`post-22.md` … `post-25.md`:

| File | Topic (BLOG_PLAN #) | Slug | Primary keyword |
|------|--------------------|------|-----------------|
| post-22 | How Does a Needle Valve Work (and Where to Use One) (#13) | how-does-a-needle-valve-work | stainless steel needle valve |
| post-23 | Can a Needle Valve Regulate Pressure? (#14) | can-a-needle-valve-regulate-pressure | do needle valves reduce pressure |
| post-24 | High-Pressure Needle Valves: Integral vs Union Bonnet (#15) | high-pressure-needle-valves-integral-vs-union-bonnet | high pressure needle valves |
| post-25 | Types of Stainless Check Valves: Spring vs Swing vs Dual-Plate (#16) | types-of-stainless-check-valves | stainless steel check valve |

Same frontmatter rules as Phase 3 (mirror fields, description 145–160 chars,
existing category values, unused cardImages preferred, readTime computed).
`pubDate`: 2026-10-12, 2026-10-15, 2026-10-19, 2026-10-22 in file order.

Same body template: keyword in H1 + first ~40 words → takeaways box → H2s →
≥1 comparison table → guidance → RFQ CTA + mapped links → FAQ ×5.
~900–1000 words each.

## Per-post guidance + link mapping

- **post-22 (needle valve how it works)**: mechanism (tapered needle/seat,
  fine thread turns → axial travel → orifice area), non-rotating stem designs,
  flow direction convention, where used (gauge isolation, metering, bleed),
  what it is NOT for (dead-heading a pump, shutoff duty — ball valve job).
  Links: /products/needle-valves/ + 2 SKUs (verify routes). Cross-link
  post-8 (needle vs ball) for the comparison angle — do NOT repeat its
  content.
- **post-23 (regulate pressure?)**: the honest engineering answer — a needle
  valve drops pressure only while flow passes (flow-dependent); it is not a
  pressure regulator and cannot hold downstream pressure under varying flow;
  when it works (bleed/vent, sampling, dampening a gauge), when you need a
  real regulator; cavitation/flash risk when dropping large ΔP; seat damage
  from operating near shutoff. Links: needle valves + a throttle-valve SKU if
  the route exists (verify). Cross-link post-22.
- **post-24 (integral vs union bonnet)**: what the bonnet is, integral
  (one-piece, weld/sealed, cheaper, for fixed HP duty) vs union/adjustable
  bonnet (repackable/maintainable, stem packing adjust), pressure classes
  (verify typical ranges via search), packing options (PTFE/graphite —
  temperature fit), when each wins. Links: HP needle valve SKUs (verify
  routes, e.g. high-pressure needle valve product page if present).
- **post-25 (check valve types)**: taxonomy deep-dive — spring/piston
  (inline, silent, orientation-free), swing (low pressure drop, horizontal
  preference), dual-plate (wafer, compact, compact for flanged lines), plus
  lift/piston variants if verified; cracking pressure ranges per type (verify
  via search); orientation rules; where each fails. ⚠️ post-9 already has a
  compact swing/spring/dual-plate table — go DEEPER (design mechanics,
  numbers, selection rules) and cross-link it; no duplicated rows.

## Fact discipline + verification

Same as Phase 3: verified numbers with source domains in the report;
qualitative where unverifiable; no invented factory claims. Verification:
pnpm build, word counts, FAQPage=1 ×4, readTime 4–5, all links resolve vs
dist routes, cardImages exist/unused, description lengths.
