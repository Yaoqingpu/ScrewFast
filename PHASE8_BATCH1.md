# Phase 8 Batch 1 — expand 3 high-value short posts

**For**: Kimi (content agent)
**From**: Claude Code, 2026-09-25 (user-approved scope: post-1, post-2, post-9)
**Constraints**: same as previous rounds — preserve voice, no `git commit`,
follow AI_GUIDE.md and BLOG_PLAN.md ground rules.

## Goal

Expand these 3 posts from their current ~120–180 words to **~900 words each**
(same length class as post-10…17), using the long-post structure:

1. `src/content/blog/en/post-1.md` — SS304 vs SS316 for fittings
2. `src/content/blog/en/post-2.md` — NPT vs G (BSP) threads
3. `src/content/blog/en/post-8.md` — Needle valve vs ball valve (mapping corrected: post-8 is needle-vs-ball, post-9 is check-valve-vs-ball)

## Required structure (mirror post-10…17)

- Keep the existing frontmatter title/slug/category/author untouched; update
  `readTime` after expansion (`max(1, round(words/200))` → expect 4–5).
- Intro paragraph (2–4 sentences, direct answer orientation).
- `> **Key takeaways**` blockquote immediately after intro: 3 self-contained
  bullets (entity + number + verdict; quotable out of context; no "this post").
- Definitional / mechanism sections with `## H2`s.
- At least one markdown comparison table.
- "How to choose" / spec-guidance section with RFQ-oriented bullets.
- Closing RFQ CTA with internal product links (keep ALL existing internal
  links; you may add more that already exist on the site).
- `## FAQ` section with exactly 5 `**question**` + paragraph pairs (this
  activates the FAQPage JSON-LD automatically — no template changes needed).

## Content guidance per post

- **post-1 (SS304 vs SS316)**: composition difference (316 adds ~2% Mo),
  PREn comparison (~18 vs ~24), chloride/marine/chemical-dosing thresholds,
  realistic price delta, when 316L matters (weld corrosion), stock/delivery
  reality from a factory view. Verdict-driven, not encyclopedia.
- **post-2 (NPT vs G)**: tapered vs parallel geometry, how each seals
  (thread sealant/dope vs gasket/O-ring), the standards behind them
  (ASME B1.20.1 for NPT; ISO 228 / BS 2779 for G), why mixing leaks, how to
  identify what you have, regional conventions, RFQ checklist.
- **post-9 (needle vs ball)**: shutoff vs metering as the core split,
  throttling damage on ball seats, orifice/Cv character, gauge isolation
  practice, seat/trim materials, ends and materials at FerruleX. Link to the
  existing ball-valve long posts (ratings, full vs reduced port) instead of
  repeating their content.

## Technical fact discipline (critical)

The existing long posts' numbers were audit-verified — never contradict them.
For every NEW technical claim you introduce (compositions, PREn values,
standard numbers, pressure classes), verify via search (perplexity MCP or
FetchURL) before writing. If a specific number cannot be verified, write the
claim qualitatively instead and note it in your report. List every number you
verified with its source domain in the report.

## Voice

Opinionated, honest about limitations, export-buyer focused, no fluff, no
keyword stuffing. Read post-10…17 first to calibrate tone.

## Verification (run all, include output in report)

1. `pnpm build` passes.
2. `wc -w` body word count for the 3 posts → ~850–1000 each.
3. `grep -c "FAQPage" dist/blog/<each-of-3-slugs>/index.html` → 1 each.
4. `grep -h "readTime"` for the 3 posts → 4–5.
5. List the numbers you verified + source domains.
6. Confirm all pre-existing internal links survived.
