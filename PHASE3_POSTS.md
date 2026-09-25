# Phase 3 — hose / expansion joint cluster (4 new posts)

**For**: Kimi (content agent)
**From**: Claude Code, 2026-09-25 (user-approved: write all remaining 19 planned
posts, Phases 3–7. This file covers Phase 3 only; later phases follow after
verification.)
**Constraints**: same as all previous rounds — BLOG_PLAN.md ground rules,
AI_GUIDE.md conventions, verified facts only, no `git commit`.

## Files to create

`src/content/blog/en/post-18.md` … `post-21.md` in this order:

| File | Topic (BLOG_PLAN #) | Slug | Primary keyword |
|------|--------------------|------|-----------------|
| post-18 | Corrugated vs Braided Stainless Hose: How to Choose (#9) | corrugated-vs-braided-stainless-hose | corrugated stainless steel hose |
| post-19 | How to Specify a Metal Hose Assembly (#10) | how-to-specify-metal-hose-assembly | corrugated metal hose assembly |
| post-20 | Why Piping Needs Expansion Joints (#21→#11) | why-piping-needs-expansion-joints | stainless steel expansion joint |
| post-21 | How Long Do Stainless Steel Hoses Last? (#12) | stainless-steel-hose-lifespan | stainless steel hose life |

## Frontmatter rules

- Mirror existing posts' fields exactly (title, description, category, slug,
  author 'FerruleX Factory', authorImage/Alt, pubDate, cardImage, cardImageAlt,
  readTime, tags 3–5).
- `description`: 145–160 chars, complete sentence, keyword-bearing.
- `category`: use an existing category value only (check what current posts
  use; pick the best fit per post).
- `pubDate`: assign 2026-09-28, 2026-10-01, 2026-10-05, 2026-10-08 in file
  order (~2/week per plan).
- `cardImage`: pick an existing on-topic image from `src/images/products/` or
  `src/images/apps/` — prefer UNUSED ones (verify against all 17 existing
  posts; we just deduped, keep it that way). If the hose cluster has fewer
  unused images than posts, sharing WITHIN this cluster is acceptable but
  note it in the report. Write a real descriptive cardImageAlt.
- `readTime`: recompute from body (`max(1, round(words/200))`).

## Body structure (same template as post-10…17)

Intro (primary keyword in H1 title AND first ~40 words) → `> **Key takeaways**`
(3 self-contained quotable bullets) → H2 sections (secondary keywords as H2s
where natural) → at least one comparison table → choose/spec guidance →
RFQ CTA ("Request a factory quote", link /contact/ plus the category/SKU pages
from the mapping below) → `## FAQ` exactly 5 Q/A pairs. ~900–1000 words.

## Per-post content guidance + internal-link mapping

- **post-18 (corrugated vs braided)**: construction difference (annular
  corrugation vs braid over bellows — get the mechanics right: most flexible
  metal hose is corrugated core + braid cover; "braided hose" often means
  braid-reinforced), flexibility vs pressure handling, kink resistance,
  typical services for each, cost trade-offs. Verify pressure/flexibility
  claims via search. Links: /products/corrugated-hose/ + 2 hose SKUs
  (tri-clamp corrugated hose etc. — verify they exist).
- **post-19 (specify a metal hose assembly)**: the spec checklist buyers need
  — media, temp, pressure (working + burst ratio), length (live vs overall),
  end connections, movement/duty cycle (cycle life), braid type, cleanliness.
  Explain pressure drop and velocity issues briefly (PASF intent). Links:
  corrugated-hose category + SKU pages.
- **post-20 (expansion joints)**: thermal expansion basics (steel grows ~X mm
  per m per 100 °C — verify coefficient), what happens without compensation,
  expansion joint types (bellows vs braided vs slip — brief), where loops vs
  joints fit, anchor/guide installation notes. Verify numbers. Links:
  expansion joint SKU page if it exists (verify route; if absent link the
  closest category).
- **post-21 (hose lifespan)**: what actually kills stainless hose (fatigue
  cycling, bend radius abuse, chlorides, velocity/erosion inside corrugations,
  overpressure), realistic service-life framing by duty (static vs cycling —
  qualitative unless verified numbers found), inspection/replacement signals,
  handling rules that extend life. Links: corrugated-hose category + SKUs.

## Cross-linking

Link to existing posts where relevant (tri-clamp post for clamp-end hose,
tri-clamp corrugated hose SKU page, SS304 vs SS316 for material choice in
corrosive duty). Do NOT duplicate post-13's tri-clamp measurement content.

## Fact discipline

Same rule as before: every new technical number verified via search
(perplexity/FetchURL), list numbers + source domains in the report;
unverifiable claims stay qualitative. No invented FerruleX-specific facts
(capacity, exact lead times).

## Verification (run all, include output in report)

1. `pnpm build` passes (astro check 0 errors).
2. Body word counts ~850–1050 real tokens each.
3. `grep -c "FAQPage" dist/blog/<4 new slugs>/index.html` → 1 each.
4. readTime values 4–5.
5. All internal links resolve against the site's actual routes (list check) —
   no links to pages that do not exist.
6. cardImage files exist and are unused by posts 1–17 (or shared-within-cluster,
   flagged).
7. Description lengths 145–160 chars (show the counts).
