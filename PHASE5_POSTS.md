# Phase 5 — sanitary & pneumatic cluster (4 new posts)

**For**: Kimi (content agent)
**From**: Claude Code, 2026-09-25 (continuation of the 19-post program)
**Constraints**: same as PHASE3_POSTS.md / PHASE4_POSTS.md.

## Step 0 — fix Phase 4 leftovers first

post-22 and post-23 lack their required table:

- post-22: add a "when a needle valve is the right tool vs the wrong one"
  table (Duty | Needle valve? | Better choice) from facts already in the post.
- post-23: add a needle-valve-vs-pressure-regulator table
  (Aspect | Needle valve | Pressure regulator) from facts already in the post.

## Files to create

`post-26.md` … `post-29.md`:

| File | Topic (#) | Slug | Primary keyword |
|------|-----------|------|-----------------|
| post-26 | Sanitary Stainless Fittings: When Food-Grade Specs Matter (#17) | sanitary-stainless-fittings-food-grade | sanitary stainless fittings |
| post-27 | Tri-Clamp vs Threaded vs Flanged for Sanitary Lines (#18) | tri-clamp-vs-threaded-vs-flanged | tri clamp vs flange |
| post-28 | Push-to-Connect vs Compression on Stainless Tubing (#19) | push-to-connect-vs-compression-stainless-tubing | push to connect on stainless steel tubing |
| post-29 | KF (NW) Vacuum Fitting Sizes Explained: KF16/25/40/50 (#20) | kf-vacuum-fitting-sizes | kf vacuum fittings |

Frontmatter rules identical to Phase 3/4. `pubDate`: 2026-10-26, 2026-10-29,
2026-11-02, 2026-11-05. Body template identical (keyword in H1 + first ~40
words, takeaways, H2s, FAQ×5, CTA, ~900–1000 words).

## REQUIRED tables (one per post, named — do not skip)

- post-26: `Industrial vs sanitary requirement` table
  (Aspect | Industrial standard | Sanitary/food-grade requirement) — surface
  finish Ra values, drainability, crevices, materials, certs.
- post-27: `Connection method comparison` table
  (Method | Strengths | Weaknesses | Best for) for tri-clamp vs threaded vs
  flanged (vs weld-end if covered).
- post-28: `Push-to-connect vs compression` table
  (Aspect | Push-to-connect | Compression).
- post-29: `KF size chart` (KF size | Nominal bore/OD mm | O-ring/flange
  dimensions if verified | Typical use) — verify dimensions via search
  (ISO 2861 / KF standard data).

## Per-post guidance + link mapping

- **post-26 (sanitary specs)**: what "food-grade/sanitary" actually requires
  — 316L default, surface finish (Ra values — verify typical numbers,
  e.g. mechanical polish vs electropolish ranges), crevice-free/full-drain
  design, 3-A / ASME BPE / EHEDG as the frameworks (verify what each covers),
  gasket material limits, CIP/SIP compatibility. When standard industrial
  fittings are fine vs when they will fail an audit. Links: cast-fittings
  category + tri-clamp SKUs. Cross-link post-13 (measurement) — no repeat of
  its size chart.
- **post-27 (connection methods)**: trade-off article. Tri-clamp: fast
  teardown, hygienic, needs gaskets/clamps; threaded: cheap, crevices +
  thread compound = sanitation risk (fine for utilities upstream); flanged:
  pressure/size range, not crevice-free, heavy; weld-end: permanent, smooth
  but not demountable. Links: tri-clamp SKU + weld-end SKUs (verify routes).
- **post-28 (PTC vs compression on stainless tube)**: answers the exact
  question — most push-to-connect series are for polymer tube; stainless tube
  only where a series explicitly lists it (consistent with post-12's FAQ);
  compression is the default for rigid stainless. Rigidity/collet-bite issue,
  seal reliability, load tolerance, reconfiguration vs permanence. Links:
  tube-fittings related categories (push-to-connect + compression).
  Cross-link post-12 (mechanism) — do not repeat its internals.
- **post-29 (KF/NW sizes)**: what KF/QF is (ISO 2861 quick flange, clamp +
  centered O-ring), size system explained (KF16/25/40/50 = nominal bore mm),
  materials (SS304/316 + aluminum for cost), O-ring elastomer choice for
  vacuum level/temperature, max vacuum typical, when ISO-K/ISO-F take over.
  Links: KF vacuum hose SKU (verify the exact route exists; if absent, link
  the closest real product/category and say so).

## Fact discipline + verification

Same as before. Verification: pnpm build; word counts; FAQPage=1 ×4;
readTime 4–5; links resolve vs dist; cardImages exist/unused; description
lengths 145–160. Report verified numbers + source domains.
