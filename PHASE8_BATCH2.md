# Phase 8 Batch 2 — expand the remaining 6 short posts

**For**: Kimi (content agent)
**From**: Claude Code, 2026-09-25 (user-approved: "finish all the rest")
**Constraints**: identical to PHASE8_BATCH1.md — same structure template,
same fact discipline, same voice, no `git commit`, follow AI_GUIDE.md.

## Goal

Expand post-3, post-4, post-5, post-6, post-7, post-9 from ~120–180 words to
~900 words each. After this batch, all 17 posts are in the ~900-word class.

Same required structure as Batch 1: intro → `> **Key takeaways**` (3
self-contained bullets) → H2 sections → at least one comparison table →
choose/RFQ guidance → CTA with internal product links (keep ALL existing
links) → `## FAQ` with exactly 5 Q/A pairs → recompute `readTime` (expect 4–5).

## Post-4 vs post-6 differentiation (DECIDED — follow exactly)

These two currently overlap. Keep BOTH, differentiated by altitude:

- **post-4 "What Is a Compression Fitting?"** — the JOINT/SYSTEM view:
  definition, how the complete joint works (nut drives ferrules onto tube),
  where compression sits vs threaded vs weld, single- vs double-ferrule as a
  brief orientation (link to `/blog/single-ferrule-vs-double-ferrule/` for
  depth — do NOT repeat its content), tube OD sizing orientation, application
  families, RFQ essentials.
- **post-6 "What Is a Ferrule Fitting?"** — the COMPONENT view: the ferrule
  itself and its bite/seal mechanics, front vs back ferrule roles, the
  ferrule-hardness rule (must be harder than the tube — consistent with
  post-10/post-11 wording), ferrule materials and matching to tube/service,
  remake/replacement rules (ferrules deform permanently), brand mixing ban.
  Link to post-4 for the joint-level picture and post-10 for single-vs-double.

Do not duplicate whole paragraphs between the two; each must stand alone.

## Per-post content guidance

- **post-3 (factory fast delivery)**: expand on lead-time mechanics — stocked
  SKU vs custom machining windows, how RFQ completeness changes quote speed,
  export packing/documentation options, MOQ and mill-cert reality.
  ⚠️ CRITICAL: do NOT invent factory-specific numbers (exact lead-time days,
  MOQ figures, capacity claims). Keep FerruleX-specific claims qualitative and
  consistent with what the current site already says. Generic export/trade
  facts (what a packing list is, why complete RFQs quote faster) are fine.
- **post-5 (how to install)**: deepen the 5 existing steps — square cut and
  deburring why/how, ferrule order and orientation, insertion-to-shoulder,
  tightening prescription (finger-tight + 1-1/4 to 1-1/2 turns — keep exactly
  consistent with post-10), pressure testing, plus a leak-troubleshooting
  section (hard tube, short insertion, mixed ferrules, over/under-tightening)
  and remake procedure. Link to post-10 and post-4.
- **post-7 (types overview)**: this is the HUB post. Expand each of the 5
  families with 2–4 sentences of real differentiation (mechanism + best
  application + limitation), upgrade the choose table, and link out to the
  deep posts (post-10 single/double ferrule, post-11 tube compatibility,
  post-12 push-to-connect) and product categories. A hub earns links by
  orienting, not by repeating.
- **post-9 (check valve vs ball)**: expand with check-valve types (swing,
  piston/spring, split-disc), cracking pressure and why it must be confirmed
  on the RFQ, flow-direction mounting rules, why a check valve never replaces
  isolation (keep existing claim), sizing/pressure-class orientation, and the
  series-installation practice (check + ball on maintenance branches).
  Verify type characteristics via search; keep the existing ~2000 PSI catalog
  claim unchanged.

## Verification (run all, include output in report)

1. `pnpm build` passes (astro check 0 errors).
2. Body word counts for all 6 → ~850–1050 real tokens each.
3. `grep -c "FAQPage" dist/blog/<each-6-slugs>/index.html` → 1 each.
4. `grep -h "readTime"` all 6 → 4–5.
5. All pre-existing internal links present in dist (list the check).
6. Numbers verified + source domains list; flag anything factory-specific you
   kept qualitative.
7. Confirm post-4 and post-6 have no duplicated paragraphs (spot-check).
