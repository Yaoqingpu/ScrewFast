# SEO URL rules (FerruleX)

Based on [Google URL structure docs](https://developers.google.com/search/docs/crawling-indexing/url-structure). Google asks for a simple structure: readable words, hyphens, one case, and no extra parameters. Deep folders and repeated words make the URL harder for people to read, so we keep paths short.

## Hard rules we follow

1. **Lowercase only** — never mix case. URLs are case-sensitive.
2. **Hyphens `-` between words** — never underscores, never jammed-together words.
3. **Descriptive keywords** — no `item-046`, no session IDs, no tracking params in internal links.
4. **Short and shallow** — a page is at most two segments after the domain. Do not repeat `stainless-steel` in the path; the site is already that catalog. Category words stay in the title, H1 and breadcrumb, not stacked in the URL.
5. **Trailing slash ALWAYS** — every page URL ends with `/` (Astro `trailingSlash: 'always'`).
   - Canonicals, sitemap, and internal links must use the slashed form.
   - `/products` and `/products/` are different URLs to Google if both resolve.
6. **One permanent URL per page** — do not also publish the old three-level path.

## Site patterns

```text
/products/
/products/{short-category}/
/products/{short-product-slug}/

/blog/
/blog/{blog-category}/
/blog/{post-slug}/

/2-piece-ball-valve/
/services/
/contact/
```

Examples:

- `/products/compression-fittings/`
- `/products/corrugated-hose-male-female-thread/`
- `/blog/ss304-vs-ss316-stainless-steel-fittings/`

Not this:

- `/products/stainless-steel-corrugated-hose/stainless-steel-corrugated-hose-male-female-thread/`
- `/blog/materials-grades/ss304-vs-ss316-stainless-steel-fittings/`

## Breadcrumbs

Show: Home → Products → Category → Product (and Blog → Category → Article).
The breadcrumb can be deeper than the URL. BreadcrumbList schema should mirror what the user sees, not the old folder depth.
