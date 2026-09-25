# Handoff: Blog QA fixes after CORE-EEAT audit

**For**: Kimi (content agent)
**From**: Claude Code audit, 2026-09-25
**Scope**: `src/content/blog/en/post-10.md` … `post-17.md` (8 long posts), `src/pages/blog/[slug].astro`, `BLOG_PLAN.md`

## Context

A CORE-EEAT audit scored the 8 long posts: GEO ≈ 68/100, SEO ≈ 62/100.
Strengths to preserve: fact-checked technical claims, dense no-fluff style,
opinionated verdicts, RFQ-oriented CTAs, verified internal links.

**All technical numbers in the posts were verified correct during the audit
(e.g. Class 300 ≈ 740 psig, 1.5×/1.1× test pressures, Cv ~40 for 1" full port).
Do NOT rewrite or soften any technical claim.**

Tasks below close the top-scoring gaps. Follow repo conventions in
[AI_GUIDE.md](AI_GUIDE.md) (path aliases, Tailwind v4, content schemas).

## Task 1 — Key takeaways box (all 8 posts)

Insert a blockquote immediately after the intro paragraph, before the first
`## H2`:

```markdown
> **Key takeaways**
>
> - <self-contained quotable sentence>
> - <self-contained quotable sentence>
> - <self-contained quotable sentence>
```

Rules: each bullet must stand alone when quoted out of context (AI-extraction
friendly — entity + number + verdict, no "this post" references). Pull the
sharpest existing claims; do not invent new facts.

## Task 2 — FAQPage JSON-LD (`src/pages/blog/[slug].astro`)

The page currently emits only `BlogPosting` structured data (~line 165).
Add `FAQPage` schema alongside it:

- Parse the post's raw markdown `## FAQ` section: each `**question**` line +
  the paragraph after it = one Q/A pair.
- Strip markdown emphasis from both question and answer text.
- Only emit the FAQPage object when the post has an FAQ section; emit nothing
  otherwise.
- Keep the existing BlogPosting output unchanged.

## Task 3 — External citations to standards (post-10, post-15 only)

Add outbound links to authoritative standards bodies where they are named:

- post-15: ASME Class paragraph → ASME B16.34 page (asme.org); the
  "1.5× shell / 1.1× seat" sentence → ISO 5208 or API 598 (iso.org / api.org).
- post-10: the DIN 2353 mention → the DIN standard page (din.de or din-en.de).

Rules: max 3 external links per post; standards-organization domains only; no
competitor, retailer, or forum domains (per BLOG_PLAN.md ground rule 6).

## Task 4 — Honest readTime (all 8 posts)

`readTime` in frontmatter is inflated (950 words marked 8–9 min). Recompute as
`max(1, round(word_count / 200))` for post-10…17. Expect values around 4–5.
Leave post-1…9 untouched in this pass.

## Task 5 — BLOG_PLAN.md update

Add a new section `## Phase 8 — thin-post expansion (backlog)` listing the 9
short posts (~200 words each: SS304 vs SS316, NPT vs G, …) as expansion
candidates to ~900 words using the same structure as post-10…17. Backlog only —
do not expand them now. Keep the existing uncommitted edit (17 published) intact.

## Blocked — needs user input, do NOT attempt

- Factory photos / diagrams per post (incl. an L-port vs T-port flow diagram —
  highest-value visual). Waiting on user-supplied assets.
- Named engineer author + credentials (replacing "FerruleX Factory"). Waiting
  on the user's choice of person and bio.

## Constraints

- Do not change technical claims, comparison tables, or FAQ answers beyond
  what Tasks 1–5 require.
- Preserve voice: opinionated, honest about limitations, export-buyer focused.
- No new dependencies.
- Do NOT `git commit` — report back and let the user review and commit.

## Verification (run all, include output in report)

1. `pnpm build` passes (includes `astro check`).
2. `grep -c "FAQPage" dist/blog/<one-slug>/index.html` → non-zero for a post
   with an FAQ section.
3. `grep -h "readTime" src/content/blog/en/post-1[0-7].md` → all values 4–5.
4. List every changed file with a one-line summary of the change.
