"""Static SEO audit over the built site in dist/.

Extracts per-page: title, meta description, canonical, H1s, og tags,
JSON-LD blocks, lang, images without alt, and internal links; then checks
link targets against files on disk.
"""
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

DIST = Path('dist')


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = ''
        self._in_title = False
        self.meta_desc = None
        self.canonical = None
        self.og = {}
        self.h1 = []
        self._in_h1 = False
        self._h1_buf = ''
        self.imgs_no_alt = []
        self.links = []
        self.lang = None
        self.jsonld = []
        self._in_jsonld = False
        self._jsonld_buf = ''
        self.robots_meta = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'html':
            self.lang = a.get('lang')
        elif tag == 'title':
            # only the first <title> (in <head>) counts; later ones are
            # accessibility titles inside inline SVGs
            if not self.title:
                self._in_title = True
        elif tag == 'meta':
            name = a.get('name', '').lower()
            prop = a.get('property', '').lower()
            if name == 'description':
                self.meta_desc = a.get('content', '')
            elif name == 'robots':
                self.robots_meta = a.get('content', '')
            elif prop.startswith('og:'):
                self.og[prop] = a.get('content', '')
        elif tag == 'link':
            if a.get('rel') == 'canonical':
                self.canonical = a.get('href', '')
        elif tag == 'h1':
            self._in_h1 = True
            self._h1_buf = ''
        elif tag == 'img':
            if 'alt' not in a:
                self.imgs_no_alt.append(a.get('src', '')[:80])
            elif not a.get('alt', '').strip():
                self.imgs_empty_alt = getattr(self, 'imgs_empty_alt', 0) + 1
        elif tag == 'a':
            href = a.get('href', '')
            if href:
                self.links.append(href)
        elif tag == 'script' and a.get('type') == 'application/ld+json':
            self._in_jsonld = True
            self._jsonld_buf = ''

    def handle_endtag(self, tag):
        if tag == 'title':
            self._in_title = False
        elif tag == 'h1' and self._in_h1:
            self.h1.append(' '.join(self._h1_buf.split()))
            self._in_h1 = False
        elif tag == 'script' and self._in_jsonld:
            self._in_jsonld = False
            self.jsonld.append(self._jsonld_buf.strip())

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        if self._in_h1:
            self._h1_buf += data
        if self._in_jsonld:
            self._jsonld_buf += data


def link_target_exists(href: str) -> bool:
    """Map an internal href to a dist file (trailing-slash agnostic)."""
    p = urlparse(href).path
    if not p.startswith('/'):
        return True  # external/mailto/etc handled elsewhere
    p = p.lstrip('/')
    if not p:
        return (DIST / 'index.html').exists()
    if p.endswith('/'):
        p += 'index.html'
    elif '.' not in Path(p).name:
        p += '/index.html'
    return (DIST / p).exists()


pages = sorted(DIST.rglob('*.html'))
rows = []
all_internal = set()
for f in pages:
    parser = PageParser()
    parser.feed(f.read_text(encoding='utf-8', errors='replace'))
    rel = '/' + str(f.relative_to(DIST)).replace('\\', '/')
    rel = re.sub(r'index\.html$', '', rel)
    rows.append(
        {
            'path': rel,
            'title': ' '.join(parser.title.split()),
            'desc': parser.meta_desc or '',
            'canonical': parser.canonical or '',
            'h1': parser.h1,
            'og_title': parser.og.get('og:title', ''),
            'og_desc': parser.og.get('og:description', ''),
            'lang': parser.lang,
            'robots': parser.robots_meta,
            'jsonld_types': [
                (json.loads(b).get('@type') if b.startswith('{') else '?')
                for b in parser.jsonld
            ],
            'imgs_no_alt': len(parser.imgs_no_alt),
            'links': parser.links,
        }
    )
    for href in parser.links:
        if href.startswith('/'):
            all_internal.add(href.split('#')[0])

# ---- aggregate findings ----
print(f'pages scanned: {len(rows)}\n')

seen_titles, seen_descs, seen_ogt, seen_ogd = {}, {}, {}, {}
issues = {k: [] for k in ('title_len', 'title_dup', 'desc_len', 'desc_dup',
                          'h1_missing', 'h1_multi', 'no_canonical',
                          'og_title_dup', 'og_desc_dup', 'no_jsonld',
                          'no_lang', 'noindex')}

for r in rows:
    p = r['path']
    t, d = r['title'], r['desc']
    if not (30 <= len(t) <= 65):
        issues['title_len'].append(f'{p} ({len(t)}): {t[:80]}')
    seen_titles.setdefault(t, []).append(p)
    if not (100 <= len(d) <= 170):
        issues['desc_len'].append(f'{p} ({len(d)})')
    if d:
        seen_descs.setdefault(d, []).append(p)
    if not r['h1']:
        issues['h1_missing'].append(p)
    if len(r['h1']) > 1:
        issues['h1_multi'].append(f'{p} x{len(r["h1"])}: {r["h1"]}')
    if not r['canonical']:
        issues['no_canonical'].append(p)
    seen_ogt.setdefault(r['og_title'], []).append(p)
    seen_ogd.setdefault(r['og_desc'], []).append(p)
    if not r['jsonld_types']:
        issues['no_jsonld'].append(p)
    if not r['lang']:
        issues['no_lang'].append(p)
    if r['robots'] and 'noindex' in r['robots'].lower():
        issues['noindex'].append(p)

for t, ps in seen_titles.items():
    if len(ps) > 1:
        issues['title_dup'].append(f'{len(ps)} pages: "{t[:70]}" -> {ps[:4]}')
for d, ps in seen_descs.items():
    if len(ps) > 1:
        issues['desc_dup'].append(f'{len(ps)} pages: "{d[:60]}..."')
for t, ps in seen_ogt.items():
    if t and len(ps) > 1:
        issues['og_title_dup'].append(f'{len(ps)} pages share og:title "{t[:60]}"')
for d, ps in seen_ogd.items():
    if d and len(ps) > 1:
        issues['og_desc_dup'].append(f'{len(ps)} pages share og:description')

for k, v in issues.items():
    print(f'== {k} ({len(v)}) ==')
    for line in v[:12]:
        print('  ', line)
    print()

# canonical host + trailing slash stats
hosts = {}
slash = {'slashed': 0, 'bare': 0}
for r in rows:
    if r['canonical']:
        h = urlparse(r['canonical']).netloc
        hosts[h] = hosts.get(h, 0) + 1
        slash['slashed' if r['canonical'].endswith('/') else 'bare'] += 1
print('canonical hosts:', hosts)
print('canonical trailing slash:', slash)

# broken internal links
broken = sorted(h for h in all_internal if not link_target_exists(h))
print(f'\ninternal links checked: {len(all_internal)}, broken: {len(broken)}')
for b in broken[:30]:
    print('  BROKEN', b)

# image alt stats
total_no_alt = sum(r['imgs_no_alt'] for r in rows)
print(f'\nimages missing alt: {total_no_alt} across {sum(1 for r in rows if r["imgs_no_alt"])} pages')

# jsonld type distribution
from collections import Counter
c = Counter(tuple(r['jsonld_types']) for r in rows)
print('\njsonld @type distribution:')
for k, n in c.most_common(10):
    print(f'  {n:4d}  {k}')
