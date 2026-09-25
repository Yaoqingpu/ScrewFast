# Phase 6 — technical deep-dive cluster (4 new posts)

**For**: Kimi (content agent)
**From**: Claude Code, 2026-09-25 (continuation of the 19-post program)
**Constraints**: same as previous phase files. All Phase 5 posts passed
verification — keep the same standard.

## Files to create

`post-30.md` … `post-33.md`:

| File | Topic (#) | Slug | Primary keyword |
|------|-----------|------|-----------------|
| post-30 | Metric vs Fractional Tube Sizes for Compression Fittings (#21) | metric-vs-fractional-tube-sizes | metric compression fittings |
| post-31 | Compression Fitting Leaks: Causes and How to Fix (#22) | compression-fitting-leaks-causes-fixes | compression fitting leaks |
| post-32 | What Is Bright Annealed (BA) Tubing and Why Instrumentation Uses It (#23) | bright-annealed-tubing-instrumentation | bright annealed tubing |
| post-33 | Stainless Steel vs Brass Ball Valves (#24) | stainless-steel-vs-brass-ball-valves | stainless steel ball valve vs brass |

Frontmatter rules identical. `pubDate`: 2026-11-09, 2026-11-12, 2026-11-16,
2026-11-19. Body template identical (~900–1000 words, keyword in H1 + first
~40 words, takeaways, H2s, FAQ×5, RFQ CTA).

## REQUIRED tables (one per post, named — do not skip)

- post-30: size conversion table (Fractional OD | Closest metric | Actual mm
  | Interchangeable?) — verify conversions (e.g. 1/4" = 6.35 mm vs 6 mm —
  NOT interchangeable; 3/8" = 9.53 vs 10 mm — not; 1/2" = 12.7 vs 12 mm —
  not; verify each).
- post-31: leak diagnosis table (Symptom | Likely cause | Fix) — at least 6
  rows (weep on gas, pull-out, leak after remake, leaks only hot, leak at
  body joint, crushed tube).
- post-32: BA vs standard annealed table (Aspect | Standard annealed | BA) —
  surface condition, oxide layer, cleanliness, cost, typical service.
- post-33: SS vs brass valve table (Aspect | Stainless | Brass) — corrosion,
  media limits, pressure/temperature envelope, cost, weight, where each wins.

## Per-post guidance + link mapping

- **post-30 (metric vs fractional)**: why the two systems coexist (regional
  OEM conventions), the near-miss trap (6 mm is NOT 1/4"), how to identify
  what you have (measure OD with calipers, check the stamp/label), ferrules
  are size-specific so mixing fails, what to state on the RFQ. Verify every
  conversion. Links: /products/compression-fittings/ + 2 SKUs. Cross-link
  post-10 (its sizing section) without repeating.
- **post-31 (leaks)**: the troubleshooting hub. Cause families: installation
  errors (short insertion, wrong ferrule order, under/over-tighten — keep
  consistent with post-5's 1-1/4 to 1-1/2 turns), tube problems (hard tube,
  oval, scratched), component mistakes (mixed brands, reused ferrules —
  consistent with post-6), service conditions (temperature cycling, media).
  Diagnosis walkthrough + fix table + when to cut back vs replace. Links:
  post-5 (install), post-6 (ferrule rules), post-11 (tube compatibility) +
  replacement-ferrule SKU. Cross-link all three posts — this post is the
  hub that binds them.
- **post-32 (BA tubing)**: what bright annealing is (annealed in
  hydrogen/vacuum atmosphere → no oxide scale, bright clean ID), why
  instrumentation/high-purity wants it (cleanliness, consistent ferrule bite,
  corrosion initiation), typical specs (verify: ASTM A269/A270 territory,
  Ra expectations if verifiable), where standard annealed is fine. Links:
  instrumentation-tubing product route if it exists (verify; else nearest
  real category — say so in report).
- **post-33 (SS vs brass valves)**: material trade-off for valve buyers —
  corrosion/chlorides (brass dezincification risk — verify), media
  compatibility (potable water, air, fuels, chemicals), temperature limits
  (verify typical), pressure class availability, cost gap, hygiene/washdown.
  Honest verdict per duty. Links: /products/ball-valves/ + 2 SKUs.
  Cross-link post-1 (stainless grade choice) and post-11 (brass ferrule on
  copper — the same material-matching logic).

## Fact discipline + verification

Same as before: verified numbers + source domains in report; qualitative
where unverifiable; no invented factory claims. Verification: pnpm build,
word counts, FAQPage=1 ×4, readTime 4–5, links resolve vs dist, cardImages
exist/unused, description lengths 145–160.
