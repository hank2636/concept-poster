"""Render an HTML poster or card to PNG with Chromium."""

import argparse
from io import BytesIO
from pathlib import Path

from PIL import Image
from playwright.sync_api import sync_playwright


PRESETS = {
    "16x9": ((1920, 1080), ".poster", 3840),
    "square": ((1080, 1080), ".poster", 3840),
    "a4": ((780, 1103), ".poster", 3840),
    "card": ((1076, 720), "main", 1076),
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("html", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--preset", choices=PRESETS, default="16x9")
    parser.add_argument("--long-edge", type=int)
    parser.add_argument("--selector", help="Override the element to capture")
    parser.add_argument("--chromium", help="Path to an existing Chromium executable")
    args = parser.parse_args()
    if not args.html.is_file():
        parser.error(f"HTML file not found: {args.html}")
    if args.output.suffix.lower() != ".png":
        parser.error("Output must have a .png extension")
    if args.long_edge is not None and args.long_edge <= 0:
        parser.error("--long-edge must be a positive integer")

    (width, height), selector, default_edge = PRESETS[args.preset]
    long_edge = args.long_edge or default_edge
    selector = args.selector or selector
    viewport = {"width": width + 32, "height": height + 48}

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(executable_path=args.chromium)
        page = browser.new_page(viewport=viewport)
        page.goto(args.html.resolve().as_uri(), wait_until="load")
        page.evaluate("document.fonts.ready")
        element = page.locator(selector)
        box = element.bounding_box()
        if not box or min(box["width"], box["height"]) <= 0:
            parser.error(f"Element is missing or hidden: {selector}")
        scale = long_edge / max(box["width"], box["height"])
        page.close()

        page = browser.new_page(viewport=viewport, device_scale_factor=scale)
        page.goto(args.html.resolve().as_uri(), wait_until="load")
        page.evaluate("document.fonts.ready")
        image = page.locator(selector).screenshot(scale="device")
        browser.close()

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(BytesIO(image)) as png:
        target = (round(box["width"] * scale), round(box["height"] * scale))
        if args.preset == "a4":
            target = (round(long_edge * 210 / 297), long_edge)
        if max(abs(actual - expected) for actual, expected in zip(png.size, target)) > 2:
            parser.error(f"Rendered size {png.size} does not match {target}")
        if png.size != target:
            png = png.resize(target, Image.Resampling.LANCZOS)
        png.save(args.output)
    print(f"{args.output} ({target[0]} × {target[1]} px)")


if __name__ == "__main__":
    main()
