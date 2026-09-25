# Phase 7 — buyer-conversion cluster (3 new posts, FINAL batch)

**For**: Kimi (content agent)
**From**: Claude Code, 2026-09-25 (last batch of the 19-post program)
**Constraints**: same as PHASE3_POSTS.md / PHASE4_POSTS.md (BLOG_PLAN.md ground
rules, AI_GUIDE.md conventions, verified facts only, no `git commit`).

## Files to create

`src/content/blog/en/post-34.md` … `post-36.md`:

| File | Topic (BLOG_PLAN #) | Slug | Primary keyword |
|------|--------------------|------|-----------------|
| post-34 | How to Write an RFQ for Stainless Fittings That Gets a Fast Factory Quote (#25) | how-to-write-rfq-stainless-fittings | stainless fittings RFQ |
| post-35 | FOB vs CIF vs EXW: Shipping Terms for Importing Fittings from China (#26) | fob-vs-cif-vs-exw-fittings | fob vs cif vs exw |
| post-36 | HS Codes for Stainless Steel Fittings and Valves (#27) | hs-codes-stainless-fittings-valves | hs code stainless steel fittings |

Same frontmatter rules as Phase 3–6 (mirror fields, description 145–160
chars, existing category values, unused cardImages preferred, readTime
computed). `pubDate`: 2026-11-23, 2026-11-26, 2026-11-30. Same body template
(keyword in H1 + first ~40 words → takeaways → H2s → required table →
guidance → CTA → FAQ×5). ~900–1000 words each.

These are buyer-conversion posts — the honest-factory voice matters most
here. No invented FerruleX-specific claims (lead-time days, MOQ numbers,
capacity, freight rates). Generic best practice + verified public data only.

## REQUIRED tables (one per post, named — do not skip)

- post-34: `RFQ checklist` table
  (Line item | Why the factory needs it | What goes wrong when it's missing)
  — ≥8 rows: tube OD & wall / thread spec, material grade, quantity +
  breakdown, destination port & Incoterm, standards/certificates required,
  pressure & temperature, packing/labeling, target price (optional).
- post-35: `Incoterms comparison` table
  (Term | Seller arranges & pays | Buyer arranges & pays | Risk transfers at |
  Typical use for fittings buyers) — EXW, FOB, CIF minimum; add CFR if it
  fits naturally. Definitions must follow Incoterms 2020 — verify risk
  transfer points via search and cite sources.
- post-36: `HS code reference` table
  (Product family | HS heading / code | Notes for importers) — verify actual
  codes via search before writing: stainless tube/pipe fittings territory is
  heading 7307 (e.g. 7307.21 flanged, 7307.22 threaded, 7307.23 welded /
  butt-jointing — verify each subheading), valves/taps heading 8481
  (8481.20 / -30 / -40 temperature-regulating / check / relief categories —
  verify), flexible metal hose if verifiable. Cite tariff source domains in
  the report. If a subheading can't be verified confidently, give the
  4-digit level and say why.

## Per-post guidance + link mapping

- **post-34 (RFQ guide)**: anatomy of a fast-quoting RFQ — the checklist
  table, a short good-vs-thin RFQ example (fictional buyer, realistic),
  what each missing item costs downstream (round-trip days, wrong-quote
  risk, re-quote cycles), certificates to state upfront (EN 10204 3.1 mill
  certs, third-party inspection), BOM/table formatting tips (one line per
  SKU, state OD × wall not thread for compression fittings — consistent
  with post-10's sizing logic). Links: /contact/ + /delivery/ IF those
  routes exist (verify first; if absent link the nearest real page and say
  so in the report). Cross-link post-3 (factory delivery — same theme,
  different depth; do not repeat it).
- **post-35 (Incoterms)**: plain-language EXW/FOB/CIF for fittings
  importers — who does what at each step, where risk transfers (verify:
  EXW = seller's premises, buyer loads & handles export clearance; FOB =
  on board the vessel at the port of shipment; CIF = seller pays freight +
  insurance but risk STILL passes on board, not at destination), hidden
  cost traps (CIF freight markup, EXW export-clearance burden for
  first-timers), which term suits which buyer (experienced importer with a
  forwarder vs first-time buyer), Incoterms 2020 framing. Links: /delivery/
  if it exists (verify; else nearest real page — flag it).
- **post-36 (HS codes)**: why codes matter (duty rate, customs clearance
  speed, country-of-origin paperwork), the main headings for this product
  family with the verified table, why a factory quotes better when the
  buyer states destination country + code context, caution that final
  classification is the importer's legal responsibility and destination-
  country tariffs can differ at the 8/10-digit level. Links: products hub
  + /downloads/ IF it exists (verify; else nearest real page — flag it).

## Step 0 — verify routes BEFORE linking

Check `src/pages/` (or dist after a build) for /delivery/ and /downloads/.
Only link real routes. If absent, use the nearest real page and flag the
substitution in your report.

## Fact discipline + verification

Same as before, plus extra caution on HS codes and Incoterms (public data —
verify and cite source domains; no invented codes, no invented freight
percentages). Verification: `pnpm build` passes, word counts ~850–1050,
FAQPage=1 ×3, readTime 4–5, all links resolve vs dist routes, cardImages
exist/unused across all 33 existing posts, description lengths 145–160.

## Final report

End with a one-paragraph summary of the whole 19-post program (post-18…36,
totals, patterns worth knowing, anything left for the user).
