"""Flatten product and blog URLs. One-shot content rewrite."""
import re
from collections import Counter
from pathlib import Path

ROOT = Path(r"E:\AI\ss-fittings-export")
SRC = ROOT / "src"

CAT = {
    "stainless-steel-corrugated-hose": "corrugated-hose",
    "stainless-steel-ball-valves": "ball-valves",
    "stainless-steel-check-valves": "check-valves",
    "stainless-steel-needle-valves": "needle-valves",
    "stainless-steel-compression-fittings": "compression-fittings",
    "stainless-steel-tube-fittings": "tube-fittings",
    "stainless-steel-pipe-fittings": "pipe-fittings",
    "stainless-steel-instrumentation-tubing": "instrumentation-tubing",
    "stainless-steel-cast-fittings": "cast-fittings",
}

BLOG_CATS = (
    "materials-grades|threads-standards|installation-guides|"
    "industry-applications|factory-export"
)
BLOG_RE = re.compile(rf"/blog/(?:{BLOG_CATS})/([a-z0-9-]+)/")


def short_slug(value: str) -> str:
    for prefix in ("stainless-steel-", "ss-"):
        if value.startswith(prefix):
            return value[len(prefix) :]
    return value


def main() -> None:
    prod_dir = SRC / "content" / "products" / "en"
    shorts: list[str] = []
    for path in prod_dir.glob("*.md"):
        text = path.read_text(encoding="utf-8")
        match = re.search(r"^slug: '([^']+)'", text, re.M)
        if not match:
            raise SystemExit(f"no slug in {path.name}")
        shorts.append(short_slug(match.group(1)))

    dupes = [key for key, count in Counter(shorts).items() if count > 1]
    collide = [slug for slug in shorts if slug in set(CAT.values())]
    if dupes or collide:
        raise SystemExit(f"slug conflict dupes={dupes} collide={collide}")

    for path in prod_dir.glob("*.md"):
        text = path.read_text(encoding="utf-8")

        def repl_slug(match: re.Match[str]) -> str:
            return f"slug: '{short_slug(match.group(1))}'"

        def repl_cat(match: re.Match[str]) -> str:
            old = match.group(1)
            return f"category: '{CAT.get(old, old)}'"

        updated = re.sub(r"^slug: '([^']+)'", repl_slug, text, count=1, flags=re.M)
        updated = re.sub(r"^category: '([^']+)'", repl_cat, updated, count=1, flags=re.M)
        if updated != text:
            path.write_text(updated, encoding="utf-8", newline="\n")

    exts = {".astro", ".ts", ".md", ".mdx", ".mjs"}
    for path in SRC.rglob("*"):
        if path.suffix not in exts:
            continue
        text = path.read_text(encoding="utf-8")
        updated = text
        for old, new in sorted(CAT.items(), key=lambda item: -len(item[0])):
            updated = updated.replace(f"/products/{old}/", f"/products/{new}/")
        updated = updated.replace(
            "/series/stainless-steel-2-piece-ball-valve/",
            "/2-piece-ball-valve/",
        )
        updated = BLOG_RE.sub(r"/blog/\1/", updated)
        if updated != text:
            path.write_text(updated, encoding="utf-8", newline="\n")

    print(f"products {len(shorts)} ok")


if __name__ == "__main__":
    main()
