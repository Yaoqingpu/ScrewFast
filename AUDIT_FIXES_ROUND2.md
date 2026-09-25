# Follow-up fixes after CORE-EEAT re-audit (round 2)

**For**: Kimi (content agent)
**From**: Claude Code audit, 2026-09-25 (round 2, after the first 5-task handoff)
**Same constraints as before**: do not rewrite technical claims, no `git commit`,
follow AI_GUIDE.md conventions.

Context: re-audit scored the 8 long posts GEO 81 / SEO 72 (up from 68/62).
The items below close the remaining non-blocked gaps. Blocked items (named
author, factory photos, TOC) are still waiting on the user — do NOT attempt
them.

## Fix 1 — readTime on post-1…9 (P1, trust issue)

All 9 short posts are ~120–180 words but claim readTime 4–7 (e.g. post-1
renders "5 min read" for 170 words — confirmed in dist). Recompute with
`max(1, round(body_words / 200))` for post-1…9. Expect all values to become 1.

## Fix 2 — post-15 needs a table (P1)

post-15 is the only long post with NO markdown table. Convert the
temperature-derating bullet list under `## How temperature derates the rating`
into a markdown table:

- Columns: `Temperature | Share of cold rating | Note`
- Use the exact numbers already in the post (80 °C full, 150 °C ~85–90 %,
  200 °C ~65–75 %, 250 °C ~half + PTFE near limit). No new facts.
- Keep the "Check the derating curve" paragraph after the table.

## Fix 3 — post-13 standards links (P1)

post-13 names two standards without linking them: "3-A sanitary standards"
and "DIN 32676". Add outbound links to the standards bodies:

- 3-A → 3-a.org (find the exact standards page)
- DIN 32676 → dinmedia.de (same domain you verified for DIN 2353)

Verify both URLs resolve (curl HTTP status) before inserting; if one does not
resolve, skip it silently and note that in the report. Max 3 external links in
the post; standards-organization domains only.

## Fix 4 — post-11 ISO citation (optional)

The ferrule-hardness rule in post-11's "The basic rule" section could cite
ISO 8434-1 (metallic tube fittings) on iso.org. Add it ONLY if you can verify
the exact iso.org standard page URL resolves; otherwise skip silently and say
so in the report.

## Fix 5 — duplicate OG image (P2)

post-14 and post-16 share the same cardImage
(`p09-51-female-threaded-ball-valve.jpg`). Look in `src/images/products/` for
an unused, on-topic ball-valve image that fits the full-port-vs-reduced-port
topic; if one fits, swap post-16's cardImage and update cardImageAlt to match.
If nothing fits, leave both as-is and say so.

## Verification (run all, include output in report)

1. `pnpm build` passes.
2. `grep -h "readTime" src/content/blog/en/post-[1-9].md` → all values 1.
3. `grep -c "FAQPage" dist/blog/<long-post-slug>/index.html` → still 1 for a
   spot-checked long post.
4. List every changed file with a one-line summary.
