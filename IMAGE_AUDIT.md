# FerruleX image & layout audit (2026-09-21)

Scope: all product images, blog covers, author avatars, and section image reuse.
Verified by file hash (MD5), reference scan, and dimensions.

## Summary

- 90 EN product pages reference product photos in `src/images/products/`.
- Every product page reuses the same two "blueprint" drawings
  (`blueprint-1.avif`, `blueprint-2.avif`) as the technical image pair.
- 4 pairs of files in `src/images/apps/` are byte-identical duplicates:
  - `app-food.jpg` == `app-instrument.jpg`
  - `app-pipes.jpg` == `services-quote.jpg`
  - `app-panel.jpg` == `services-oem.jpg`
  - `app-factory.jpg` == `app-refinery.jpg`
- 1 pair of product images duplicates another product image:
  - `p06-28-quick-screw-straight-connector.jpg` == `p06-29-quick-screw-female-connector.jpg`
  - `app-lab.jpg` == `p02-02-ss-flanged-corrugated-hose.jpg`
  - `app-marine.jpg` == `p09-51-female-threaded-ball-valve.jpg`
- EN blog covers: 9 posts share 6 images; `features-piping.jpg` is used by 3
  posts (post-1, post-5, post-6), `app-panel.jpg` by 2 (post-2, post-4),
  `app-pipes.jpg` by 2 (post-7, post-9).
- Author avatar: all 9 EN posts use the same file `blog/jacob.avif` while
  claiming a single factory identity.

## Stock/template images still referenced in pages

| File | Used on | Suggested action |
| --- | --- | --- |
| apps/app-food.jpg (hero) | home hero | replace with real hero shot |
| apps/features-piping.jpg | home features, blog covers | replace with fitting close-up |
| apps/app-refinery.jpg | home valve card, services | replace with valve close-up |
| apps/app-pipes.jpg | home hose card, blog, services | replace with hose close-up |
| apps/services-quote.jpg | services "Product selection support" | replace with real quote/RFQ scene |
| apps/app-panel.jpg | services "person working", blog covers | replace with real instrumentation panel |
| apps/app-factory.jpg | services "OEM factory", blog covers | replace with real production line |
| apps/services-oem.jpg | services "custom parts", blog covers | replace with real OEM scene |

## Image placeholders — pending real photography

Placeholder file: `src/images/products/placeholder.png` (neutral gray, brand
mark, and text: "Product photo coming — ask for a photo with your RFQ").

Products whose current `imgMain`/`imgCard` should be replaced with the
placeholder until real photos are ready:
- item-017 (Compression / Quick-Screw Straight & Bulkhead Connectors)
- item-025 (Forged Compression Reducing Tee)
- item-026 (Forged Compression Cross Fitting)
- item-031 (Quick-Screw Elbow Connector)
- item-032 (Quick-Screw Tee Connector)
- item-049 (Straight Quick-Screw Ball Valve)
- item-050 (3-Way Quick-Screw Ball Valve)
- item-055 (Mini Ball Valve)
- item-056 (High-Pressure Female Ball Valve)
- item-057 (Air-Source Ball Valve)
- item-062 (Angle Compression Needle Valve)
- item-063 (Forged Compression Needle Valve)
- item-064 (Weld-End Needle Valve)
- item-074 (Push-to-Connect Straight Fitting)
- item-075 (Push-to-Connect Elbow Fitting)
- item-076 (Push-to-Connect Straight Union)
- item-077 (Push-to-Connect Bulkhead Fitting)
- item-078 (Y-Type and T-Type Tee Fitting)

## Content pages that reuse generic template stock photos

- `src/pages/services.astro` uses 8 images, all from the shared `apps/` pool,
  many also used on the home page or as blog covers. Reuse confirmed.
- `src/pages/fr/index.astro` and `src/pages/fr/services.astro` use the
  original ScrewFast construction stock set (`hero-image`, `features-image`,
  `blueprints-image`, `person-working`, `before-after`, etc.). The FR pages
  still carry construction-themed copy ("Transformer les conceptions en
  realite", "projet de construction") that does not match the fittings
  catalog.

## Recommended next steps

1. Replace the 18 placeholder-listed products with real photos as they become
   available; keep the placeholder variant until then.
2. Retire the duplicate `apps/` images once unique replacements exist.
3. Rewrite the FR services page copy away from the construction template, or
   temporarily remove that page until real FR content is written.
4. Blog covers: keep one unique cover per category (see revised EN blog
   assignments), replace with real shots when photography is available.
