# -*- coding: utf-8 -*-
"""Build rewrite_product_copy_v2.py from hand-written COPY and apply to products."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

import _hand_copy_part1  # noqa: E402
import _hand_copy_part2  # noqa: E402
import _hand_copy_part3  # noqa: E402

from _hand_copy_part1 import COPY  # noqa: E402

PROD = ROOT / "src" / "content" / "products" / "en"
OUT = SCRIPTS / "rewrite_product_copy_v2.py"

BANNED = [
    "Buyers usually",
    "Pair this SKU",
    "Pressure guidance",
    "construction oriented",
    "Technical buyers use this pattern",
    "catalog cues are",
    "On projects that standardize",
    "Beyond the overview, this SKU",
    "Use-cases center on",
    "Export documentation and packaging are handled",
    "as stainless steel ball valve hardware for",
    "geometry is built for",
    "FerruleX’s answer when buyers need",
    "Keep corrugated stainless steel hose and",
    "State metric vs imperial sizing early",
]


def word_count(s: str) -> int:
    return len(re.findall(r"[A-Za-z0-9']+", s))


def clip_desc(s: str, lo=145, hi=160) -> str:
    s = " ".join(s.split())
    if not s.endswith("."):
        s += "."
    pads = [
        " Stocked sizes ship fast.",
        " Export RFQ only — no cart.",
        " Common SKUs in inventory.",
        " Custom OEM sizes on request.",
        " NPT, G and metric options.",
        " Confirm media on RFQ.",
        " Fast factory shipping.",
        " Ask FerruleX for stock.",
        " SS316 on request.",
        " Send your size list.",
    ]
    i = 0
    while len(s) < lo and i < 30:
        add = pads[i % len(pads)]
        if add.strip().lower() in s.lower():
            i += 1
            continue
        if len(s) + len(add) <= hi:
            s = s.rstrip(".") + "." + add
        else:
            room = hi - len(s)
            for t in [" Fast stock shipping.", " OEM RFQ welcome.", " Export only.", " Send OD list.", " NPT/G OK."]:
                if len(t) <= room and t.strip().lower() not in s.lower():
                    s = s.rstrip(".") + "." + t
                    break
            break
        i += 1
    if len(s) > hi:
        cut = s[:hi]
        last = cut.rfind(".")
        if last >= lo - 1:
            s = cut[: last + 1]
        else:
            s = cut.rsplit(" ", 1)[0].rstrip(".,;") + "."
    return s


def normalize() -> None:
    from _hand_copy_topups import CONTENT_TOPUP, SUBTITLE_TOPUP

    issues = []
    for pid, c in COPY.items():
        c["description"] = clip_desc(c["description"])
        c["content"] = " ".join(c["content"].split())
        c["subTitle"] = " ".join(c["subTitle"].split())
        if pid in CONTENT_TOPUP and CONTENT_TOPUP[pid].strip() not in c["content"]:
            c["content"] += " " + CONTENT_TOPUP[pid].strip()
        if pid in SUBTITLE_TOPUP and SUBTITLE_TOPUP[pid].strip() not in c["subTitle"]:
            c["subTitle"] += " " + SUBTITLE_TOPUP[pid].strip()

        # Grow using only THIS SKU's own data (no shared lead-in phrase)
        if word_count(c["content"]) < 90:
            spec_bits = "; ".join(f"{a} {b}" for a, b in c["specs"])
            c["content"] += f" {spec_bits}."
        if word_count(c["subTitle"]) < 50:
            bullet_bits = " ".join(sub for _, sub in c["bullets"])
            c["subTitle"] += f" {bullet_bits}"

        c["content"] = " ".join(c["content"].split())
        c["subTitle"] = " ".join(c["subTitle"].split())
        wc, ws = word_count(c["content"]), word_count(c["subTitle"])
        if wc < 90:
            issues.append(f"id {pid} content too short: {wc}")
        if wc > 160:
            c["content"] = " ".join(c["content"].split()[:158]).rstrip(".,;") + "."
        if ws < 50:
            issues.append(f"id {pid} subTitle too short: {ws}")
        if ws > 90:
            c["subTitle"] = " ".join(c["subTitle"].split()[:88]).rstrip(".,;") + "."
        dlen = len(c["description"])
        if not (145 <= dlen <= 160):
            issues.append(f"id {pid} desc len {dlen}: {c['description']}")
    if issues:
        raise SystemExit("Validation failed:\n  " + "\n  ".join(issues))


def emit_script() -> str:
    lines = ["COPY = {"]
    for pid in sorted(COPY):
        c = COPY[pid]
        lines.append(f"    {pid}: {{")
        lines.append(f"        'description': {c['description']!r},")
        lines.append(f"        'content': {c['content']!r},")
        lines.append(f"        'subTitle': {c['subTitle']!r},")
        lines.append(f"        'bullets': {c['bullets']!r},")
        lines.append(f"        'specs': {c['specs']!r},")
        lines.append("    },")
    lines.append("}")
    copy_block = "\n".join(lines)

    runner = r'''# -*- coding: utf-8 -*-
"""Rewrite EVERY EN product markdown with unique FerruleX SEO copy (v2)."""
from __future__ import annotations

import re
from pathlib import Path

PROD_DIR = Path(__file__).resolve().parents[1] / "src" / "content" / "products" / "en"

CATEGORY_FIX = {
    33: "stainless-steel-tube-fittings",
    77: "stainless-steel-tube-fittings",
}

__COPY_BLOCK__


def esc(s: str) -> str:
    return s.replace("'", "''")


def rewrite_file(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    title_m = re.search(r"^title:\s*'((?:''|[^'])*)'", text, re.M)
    category_m = re.search(r"^category:\s*'((?:''|[^'])*)'", text, re.M)
    slug_m = re.search(r"^slug:\s*'((?:''|[^'])*)'", text, re.M)
    id_m = re.search(r"^  id:\s*(\d+)", text, re.M)
    img_card_m = re.search(r"imgCard:\s*'([^']+)'", text)
    img_main_m = re.search(r"imgMain:\s*'([^']+)'", text)
    if not all([title_m, category_m, slug_m, id_m, img_card_m, img_main_m]):
        raise RuntimeError(f"Incomplete frontmatter: {path.name}")
    title = title_m.group(1).replace("''", "'")
    category = category_m.group(1)
    slug = slug_m.group(1)
    img_card = img_card_m.group(1)
    img_main = img_main_m.group(1)
    pid = int(id_m.group(1))
    if pid not in COPY:
        raise RuntimeError(f"No COPY for id {pid} ({path.name})")
    category = CATEGORY_FIX.get(pid, category)
    c = COPY[pid]
    bullets = "\n".join(
        f"  - title: '{esc(a)}'\n    subTitle: '{esc(b)}'" for a, b in c["bullets"]
    )
    specs = "\n".join(
        f"  - title: '{esc(a)}'\n    subTitle: '{esc(b)}'" for a, b in c["specs"]
    )
    rows = "\n".join(f"      - ['{esc(a)}', '{esc(b)}']" for a, b in c["specs"])
    out = (
        "---\n"
        f"title: '{esc(title)}'\n"
        f"description: '{esc(c['description'])}'\n"
        f"category: '{esc(category)}'\n"
        f"slug: '{esc(slug)}'\n"
        "main:\n"
        f"  id: {pid}\n"
        "  content: |\n"
        f"    {c['content']}\n"
        f"  imgCard: '{img_card}'\n"
        f"  imgMain: '{img_main}'\n"
        f"  imgAlt: '{esc(title)} — FerruleX stainless steel fittings'\n"
        "tabs:\n"
        "  - id: 'tabs-with-card-item-1'\n"
        "    dataTab: '#tabs-with-card-1'\n"
        "    title: 'Description'\n"
        "  - id: 'tabs-with-card-item-2'\n"
        "    dataTab: '#tabs-with-card-2'\n"
        "    title: 'Specifications'\n"
        "  - id: 'tabs-with-card-item-3'\n"
        "    dataTab: '#tabs-with-card-3'\n"
        "    title: 'Request Quote'\n"
        "longDescription:\n"
        f"  title: '{esc(title)}'\n"
        "  subTitle: |\n"
        f"    {c['subTitle']}\n"
        "  btnTitle: 'Request a factory quote'\n"
        "  btnURL: '/contact'\n"
        "descriptionList:\n"
        f"{bullets}\n"
        "specificationsLeft:\n"
        f"{specs}\n"
        "tableData:\n"
        "  - feature: ['Specification', 'Value']\n"
        "    description:\n"
        f"{rows}\n"
        "blueprints:\n"
        "  first: '@/images/blueprint-1.avif'\n"
        "  second: '@/images/blueprint-2.avif'\n"
        "---\n"
    )
    path.write_text(out, encoding="utf-8")


def main() -> None:
    files = sorted(PROD_DIR.glob("item-*.md"))
    n = 0
    for f in files:
        rewrite_file(f)
        n += 1
    print(f"Rewrote {n} products")


if __name__ == "__main__":
    main()
'''
    return runner.replace("__COPY_BLOCK__", copy_block)


def audit() -> None:
    blob = "\n".join(
        c["content"] + "\n" + c["subTitle"] for c in COPY.values()
    )
    print("=== Banned phrase counts (in COPY) ===")
    for phrase in BANNED:
        print(f"  {phrase!r}: {blob.count(phrase)}")
    # uniqueness of first sentence
    firsts = [c["content"].split(".")[0] for c in COPY.values()]
    print("unique first sentences:", len(set(firsts)), "/", len(firsts))


def spotcheck() -> None:
    for pid in (1, 7, 46, 61, 69):
        c = COPY[pid]
        parts = re.split(r"(?<=[.!?])\s+", c["content"])
        print(f"\n--- id {pid} ---")
        print(" ".join(parts[:2]))


def main() -> None:
    expected = set(range(1, 81)) | {82, 84}
    if set(COPY) != expected:
        raise SystemExit(f"COPY id mismatch: missing {expected-set(COPY)} extra {set(COPY)-expected}")
    normalize()
    print(f"Normalized {len(COPY)} entries OK")
    OUT.write_text(emit_script(), encoding="utf-8")
    print(f"Wrote {OUT}")
    # apply via the generated script
    import runpy
    runpy.run_path(str(OUT), run_name="__main__")
    audit()
    spotcheck()


if __name__ == "__main__":
    main()
