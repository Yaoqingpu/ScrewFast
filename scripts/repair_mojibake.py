"""Repair GBK mojibake baked into UTF-8 files.

Corruption model: UTF-8 text was decoded as GBK and saved as UTF-8.
Recovery: encode back to GBK, decode as UTF-8.  Sequences where the
invalid GBK pair became '?' leave U+FFFD behind and are reported for
manual curation.
"""
import sys
from pathlib import Path

MOJIBAKE_CHARS = '鈥脳锛銆鐢鐨嬶紝鐒＄洍绔欑珯'


def has_cjk(s: str) -> bool:
    return any('\u4e00' <= c <= '\u9fff' or '\u3400' <= c <= '\u4dbf' for c in s)


def main() -> None:
    root = Path('src')
    files = [
        p
        for p in root.rglob('*')
        if p.suffix in {'.md', '.astro', '.ts', '.mdx'} and p.is_file()
    ]
    # also constants.ts lives under src/data_files -> already covered

    changed, skipped, pending = [], [], []
    for p in sorted(files):
        try:
            text = p.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            skipped.append((p, 'not utf-8'))
            continue
        if not has_cjk(text):
            continue
        had_bom = text.startswith('\ufeff')
        body = text.lstrip('\ufeff')
        try:
            fixed = body.encode('gbk').decode('utf-8', errors='replace')
        except UnicodeEncodeError as e:
            skipped.append((p, f'gbk encode failed: {e}'))
            continue
        if had_bom:
            fixed = '\ufeff' + fixed
        if fixed == text:
            skipped.append((p, 'round-trip unchanged'))
            continue
        n_fffd = fixed.count('\ufffd')
        # count CJK left after round-trip (should be zero for pure mojibake)
        leftover = ''.join(sorted({c for c in fixed if '\u4e00' <= c <= '\u9fff'}))
        p.write_text(fixed, encoding='utf-8', newline='')
        changed.append((p, n_fffd, leftover))
        if n_fffd:
            for i, line in enumerate(fixed.splitlines(), 1):
                if '\ufffd' in line:
                    pending.append((str(p), i, line.strip()))

    print('=== changed files ===')
    for p, n, leftover in changed:
        flag = f'  LEFTOVER CJK: {leftover}' if leftover else ''
        print(f'{p}  (ufffd={n}){flag}')
    print('\n=== skipped ===')
    for p, why in skipped:
        print(f'{p}  ({why})')
    print('\n=== lines still containing U+FFFD (need manual fix) ===')
    for f, i, line in pending:
        print(f'{f}:{i}: {line}')


if __name__ == '__main__':
    main()
