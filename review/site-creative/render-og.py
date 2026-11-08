"""Render review/site-creative/og-card.html to assets/og.png and assets/og.jpg (1200x630) with headless Edge.
usage: python render-og.py <base-url-of-site-root>   e.g. http://127.0.0.1:8795
The card has to be served over http (not file://) so the woff2 fonts load."""
import sys, time, pathlib
from playwright.sync_api import sync_playwright
from PIL import Image
root = pathlib.Path(__file__).resolve().parents[2]
base = sys.argv[1].rstrip("/")
png, jpg = root / "assets/og.png", root / "assets/og.jpg"
with sync_playwright() as p:
    b = p.chromium.launch(channel="msedge", headless=True, args=["--disable-gpu", "--hide-scrollbars"])
    pg = b.new_page(viewport={"width": 1200, "height": 630}, device_scale_factor=1)
    pg.goto(base + "/review/site-creative/og-card.html"); pg.evaluate("() => document.fonts.ready"); time.sleep(1.2)
    pg.screenshot(path=str(png), clip={"x": 0, "y": 0, "width": 1200, "height": 630}); b.close()
im = Image.open(png).convert("RGB"); im.save(jpg, "JPEG", quality=88, optimize=True, progressive=True)
# the PNG is a fallback for scrapers that ignore JPEG; quantize it so it stays small
im.quantize(256, method=Image.Quantize.FASTOCTREE, dither=Image.Dither.FLOYDSTEINBERG).save(png, "PNG", optimize=True)
print("og.jpg", jpg.stat().st_size // 1024, "KB; og.png", png.stat().st_size // 1024, "KB")
