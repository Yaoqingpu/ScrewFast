#!/usr/bin/env python3
"""Fill home / services / support-page marketing images from Shengquan sample crops."""

from __future__ import annotations

from pathlib import Path

from PIL import Image

STORE = Path(r"E:\AI\不锈钢接头采集站")
EXPORT = Path(r"E:\AI\ss-fittings-export")
CROPS = STORE / "supplier-crops"
APPS = EXPORT / "src" / "images" / "apps"
PROD = EXPORT / "src" / "images" / "products"


def save_cover(src: Path, dst: Path, max_side: int = 1600) -> tuple[int, int]:
    im = Image.open(src).convert("RGB")
    w, h = im.size
    scale = min(1.0, max_side / max(w, h))
    if scale < 1:
        im = im.resize((int(w * scale), int(h * scale)), Image.Resampling.LANCZOS)
    dst.parent.mkdir(parents=True, exist_ok=True)
    im.save(dst, "JPEG", quality=90, optimize=True)
    return im.size


def need(name: str) -> Path:
    p = CROPS / name
    if not p.exists():
        raise FileNotFoundError(p)
    return p


def main() -> None:
    # Marketing / apps — each file gets a distinct sample photo
    mapping: list[tuple[str, str, int]] = [
        # Home hero landscape from catalog hero spread
        ("hero-plant-landscape.jpg", "p07-01-hero-2060x1471.jpg", 1800),
        ("hero-valve.jpg", "p10-01-photo-655x556.jpg", 1600),
        ("features-piping.jpg", "p03-01-photo-784x771.jpg", 1600),
        ("services-oem.jpg", "p04-01-photo-625x529.jpg", 1600),
        ("services-quote.jpg", "p13-01-photo-513x435.jpg", 1400),
        ("app-lab.jpg", "p03-04-photo-784x771.jpg", 1600),
        ("app-marine.jpg", "p09-01-photo-655x556.jpg", 1400),
        ("app-factory.jpg", "p05-01-photo-655x556.jpg", 1400),
        ("app-pipes.jpg", "p03-02-photo-784x770.jpg", 1600),
        ("app-refinery.jpg", "p11-01-photo-655x556.jpg", 1400),
        ("app-food.jpg", "p03-05-photo-784x771.jpg", 1600),
        ("app-instrument.jpg", "p06-01-photo-655x555.jpg", 1400),
        ("app-panel.jpg", "p08-01-photo-512x434.jpg", 1400),
        # Dedicated support-page heroes (optional extras)
        ("support-about.jpg", "p07-01-hero-2060x1471.jpg", 1800),
        ("support-applications.jpg", "p04-01-photo-625x529.jpg", 1600),
        ("support-oem.jpg", "p15-01-photo-478x438.jpg", 1200),
        ("support-quality.jpg", "p05-01-photo-655x556.jpg", 1400),
        ("support-delivery.jpg", "p09-01-photo-655x556.jpg", 1400),
        ("support-faq.jpg", "p03-03-photo-783x771.jpg", 1600),
    ]

    for dst_name, src_name, max_side in mapping:
        src = need(src_name)
        size = save_cover(src, APPS / dst_name, max_side=max_side)
        print(f"OK  {dst_name} <- {src_name} {size}")

    print("Done.")


if __name__ == "__main__":
    main()
