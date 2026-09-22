"""Pass 2: fix remaining U+FFFD spots left by the GBK round-trip.

Corruption ate the punctuation's third byte (and sometimes one following
byte).  Context rules below restore the original characters; every rule
prints how many replacements it made so a zero-count rule is visible.
"""
from pathlib import Path

RULES = [
    # specific arrows in blog [slug].astro
    ('Read article �?', 'Read article →'),
    ('�?All blog categories', '← All blog categories'),
    # curly closing quotes (opening quotes survived round-trip)
    ('delivery�?means', 'delivery” means'),
    ('ferrule�?almost', 'ferrule” almost'),
    # numeric ranges (en dash; trailing digit was sometimes eaten)
    ('3�?5 mm', '3–5 mm'),
    ('4�?6 mm', '4–6 mm'),
    ('in 1�? business', 'in 1–2 business'),
    ('1/8"�?/2"', '1/8"–1/2"'),
    ('1/8"�?"', '1/8"–1/2"'),
    # generic: space + eaten punctuation + eaten space -> em dash
    (' �?', ' — '),
]

files = [
    p
    for p in Path('src').rglob('*')
    if p.suffix in {'.md', '.astro', '.ts', '.mdx'} and p.is_file()
]

for p in sorted(files):
    text = p.read_text(encoding='utf-8')
    if '\ufffd' not in text:
        continue
    orig = text
    for old, new in RULES:
        n = text.count(old)
        if n:
            text = text.replace(old, new)
            print(f'{p}: {old!r} -> {new!r}  x{n}')
    if text != orig:
        p.write_text(text, encoding='utf-8', newline='')

# verify nothing left
left = []
for p in sorted(files):
    t = p.read_text(encoding='utf-8')
    if '\ufffd' in t:
        for i, line in enumerate(t.splitlines(), 1):
            if '\ufffd' in line:
                left.append(f'{p}:{i}: {line.strip()}')
cjk_left = []
for p in sorted(files):
    t = p.read_text(encoding='utf-8')
    bad = sorted({c for c in t if '\u4e00' <= c <= '\u9fff'})
    if bad:
        cjk_left.append(f'{p}: {bad}')

print('\n=== remaining U+FFFD ===')
print('\n'.join(left) if left else '(none)')
print('=== remaining CJK ===')
print('\n'.join(cjk_left) if cjk_left else '(none)')
