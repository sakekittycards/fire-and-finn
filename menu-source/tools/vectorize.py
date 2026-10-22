"""Rebuild the Fire & Finn logo as a true vector SVG.

- Flame strokes, wave strokes and the two tagline dashes are traced from the raster
  (one path per connected stroke) and filled with a gradient sampled from the raster.
- The wordmark "FIRE & FINN" is traced from the raster so the letterforms stay exactly as drawn.
- The tagline "HIBACHI • SUSHI • POKE" is set from Outfit 400 glyph outlines (the font the
  original tagline was set in), using the option-B layout: letters at 76%, 0.34em tracking.

usage: vectorize.py <original 1988x791 RGBA png> <Outfit-400.ttf> <out.svg> [tagline text]
"""
import sys, math
sys.path.insert(0, r'C:/Users/lunar/AppData/Local/Temp/ffm/lib')
import numpy as np, pymupdf, potrace
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen

ORIG, FONT, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
TAGLINE = sys.argv[4] if len(sys.argv) > 4 else "HIBACHI • SUSHI • POKE"
UP = 4                       # trace at 4x on a smoothed alpha, so potrace fits clean curves
SPAN_L, SPAN_R = 265, 1724   # outer extent of the original dashes = width of the tagline row
TEXT_CY = 665.0              # vertical centre of the original tagline letters
DASH_CY = 661.0              # vertical centre of the original dashes
CAP_SCALE, TRACK, GAP = 0.76, 0.34, 26   # option B
ORIG_CAP = 56.0

pix = pymupdf.Pixmap(ORIG)
W, H, N = pix.width, pix.height, pix.n
arr = np.frombuffer(pix.samples, dtype=np.uint8).reshape(H, W, N)
alpha = arr[:, :, 3].astype(np.int32); rgb = arr[:, :, :3].astype(np.int32)

# ---------- helpers ----------
def components(mask):
    """4-connected components of a boolean mask -> list of (ys, xs) index arrays."""
    seen = np.zeros_like(mask, dtype=bool); comps = []
    ys0, xs0 = np.nonzero(mask)
    for y0, x0 in zip(ys0, xs0):
        if seen[y0, x0]: continue
        stack = [(y0, x0)]; seen[y0, x0] = True; pts = []
        while stack:
            y, x = stack.pop(); pts.append((y, x))
            for ny, nx in ((y-1, x), (y+1, x), (y, x-1), (y, x+1)):
                if 0 <= ny < H and 0 <= nx < W and mask[ny, nx] and not seen[ny, nx]:
                    seen[ny, nx] = True; stack.append((ny, nx))
        p = np.array(pts); comps.append((p[:, 0], p[:, 1]))
    return comps

def box_blur(a, r):
    """separable box blur, radius r, edge-replicated"""
    for axis in (0, 1):
        pad = [(0, 0), (0, 0)]; pad[axis] = (r, r)
        ap = np.pad(a, pad, mode="edge"); cs = np.cumsum(ap, axis=axis, dtype=np.float32)
        cs = np.concatenate([np.zeros_like(np.take(cs, [0], axis=axis)), cs], axis=axis)
        n = a.shape[axis]
        a = (np.take(cs, range(2 * r + 1, 2 * r + 1 + n), axis=axis) - np.take(cs, range(0, n), axis=axis)) / (2 * r + 1)
    return a

def smooth_upscale(alpha_f, k, blur=None):
    """bilinear upscale of a float alpha crop by k, then a light blur: removes the pixel staircase"""
    h, w = alpha_f.shape
    xs = (np.arange(w * k) + 0.5) / k - 0.5; ys = (np.arange(h * k) + 0.5) / k - 0.5
    x0 = np.clip(np.floor(xs).astype(int), 0, w - 1); x1 = np.clip(x0 + 1, 0, w - 1); fx = np.clip(xs - x0, 0, 1).astype(np.float32)
    t = alpha_f[:, x0] * (1 - fx) + alpha_f[:, x1] * fx
    y0 = np.clip(np.floor(ys).astype(int), 0, h - 1); y1 = np.clip(y0 + 1, 0, h - 1); fy = np.clip(ys - y0, 0, 1).astype(np.float32)[:, None]
    big = t[y0, :] * (1 - fy) + t[y1, :] * fy
    r = blur if blur else k // 2
    return box_blur(box_blur(big, r), r)

def trace(mask, blur=None):
    """Trace a boolean mask (original resolution) -> SVG path 'd' in original coordinates.
    The mask is cropped to its bounding box, upscaled smoothly and thresholded at 50%."""
    ys, xs = np.nonzero(mask); m = 6
    y0, y1 = max(ys.min() - m, 0), min(ys.max() + m + 1, H); x0, x1 = max(xs.min() - m, 0), min(xs.max() + m + 1, W)
    a = (alpha[y0:y1, x0:x1].astype(np.float32) / 255.0) * mask[y0:y1, x0:x1]
    big = smooth_upscale(a, UP, blur) > 0.5
    path = potrace.Bitmap(~big).trace(turdsize=10, alphamax=1.0, opticurve=1, opttolerance=0.4)   # potracer: bool, False = ink
    d = []
    f = lambda v, o: f"{v / UP + o:.2f}"
    P = lambda p: (p.x, p.y)
    for curve in path:
        sx, sy = P(curve.start_point); d.append(f"M{f(sx, x0)} {f(sy, y0)}")
        for seg in curve:
            ex, ey = P(seg.end_point)
            if seg.is_corner:
                cx, cy = P(seg.c); d.append(f"L{f(cx, x0)} {f(cy, y0)}L{f(ex, x0)} {f(ey, y0)}")
            else:
                (c1x, c1y), (c2x, c2y) = P(seg.c1), P(seg.c2)
                d.append(f"C{f(c1x, x0)} {f(c1y, y0)} {f(c2x, x0)} {f(c2y, y0)} {f(ex, x0)} {f(ey, y0)}")
        d.append("Z")
    return "".join(d)

def hexcol(c): return "#%02x%02x%02x" % tuple(int(round(v)) for v in c)

def gradient_for(ys, xs, gid):
    """Sample the stroke's colour along its longer axis -> (<linearGradient>, bbox)."""
    x0, x1, y0, y1 = xs.min(), xs.max() + 1, ys.min(), ys.max() + 1
    solid = alpha[ys, xs] > 200
    ys2, xs2 = ys[solid], xs[solid]
    if len(xs2) < 20: ys2, xs2 = ys, xs
    horizontal = (x1 - x0) >= (y1 - y0)
    coord = xs2 if horizontal else ys2
    lo, hi = coord.min(), coord.max()
    stops = []
    for i in range(7):
        t = i / 6; c = lo + t * (hi - lo); half = max(3, (hi - lo) / 14)
        sel = np.abs(coord - c) <= half
        if sel.sum() == 0: continue
        col = rgb[ys2[sel], xs2[sel]].mean(axis=0)
        stops.append((t, hexcol(col)))
    if horizontal: a = f'x1="{lo}" y1="{(y0+y1)/2:.1f}" x2="{hi}" y2="{(y0+y1)/2:.1f}"'
    else:          a = f'x1="{(x0+x1)/2:.1f}" y1="{lo}" x2="{(x0+x1)/2:.1f}" y2="{hi}"'
    g = f'<linearGradient id="{gid}" gradientUnits="userSpaceOnUse" {a}>' + "".join(
        f'<stop offset="{t:.3f}" stop-color="{c}"/>' for t, c in stops) + "</linearGradient>"
    return g, (x0, y0, x1, y1)

# ---------- 1. gradient strokes: flames (y < 300) and waves (430 <= y < 616) ----------
defs, body = [], []
full = alpha > 127
for name, (ya, yb) in (("flame", (0, 300)), ("wave", (430, 616))):
    band = np.zeros_like(full); band[ya:yb, :] = full[ya:yb, :]
    for i, (ys, xs) in enumerate(components(band)):
        if len(ys) < 40: continue
        m = np.zeros_like(full); m[ys, xs] = True
        gid = f"{name}{i}"; g, bb = gradient_for(ys, xs, gid); defs.append(g)
        body.append(f'<path id="{gid}-stroke" fill="url(#{gid})" fill-rule="evenodd" d="{trace(m)}"/>')
    print(f"{name}: {sum(1 for c in components(band) if len(c[0]) >= 40)} strokes traced")

# ---------- 2. wordmark FIRE & FINN, traced, solid ----------
wm = np.zeros_like(full); wm[290:440, :] = full[290:440, :]
ys, xs = np.nonzero(wm & (alpha > 200)); wm_col = hexcol(rgb[ys, xs].mean(axis=0))
body.append(f'<path id="wordmark" fill="{wm_col}" fill-rule="evenodd" d="{trace(wm, blur=UP)}"/>')   # stronger smoothing: straight stems
print("wordmark traced, colour", wm_col)

# ---------- 3. tagline from Outfit outlines, option-B layout ----------
font = TTFont(FONT); upm = font["head"].unitsPerEm; capu = font["OS/2"].sCapHeight
glyphs = font.getGlyphSet(); cmap = font.getBestCmap(); hmtx = font["hmtx"]
cap = ORIG_CAP * CAP_SCALE; size = cap * upm / capu; sc = size / upm
def adv(ch): return hmtx[cmap[ord(ch)]][0] * sc
dot_r = 0.15 * cap
items = []; x = 0.0
for ch in TAGLINE:
    if ch == "•": items.append(("dot", x + dot_r)); x += 2 * dot_r + size * TRACK
    elif ch == " ": x += adv(" ") + size * TRACK
    else: items.append(("glyph", x, ch)); x += adv(ch) + size * TRACK
text_w = x - size * TRACK
start_x = (SPAN_L + SPAN_R) / 2 - text_w / 2
baseline = TEXT_CY + cap / 2
tag = [f'<g id="tagline" fill="{wm_col}">']
for it in items:
    if it[0] == "dot":
        tag.append(f'<circle cx="{start_x + it[1]:.2f}" cy="{TEXT_CY:.2f}" r="{dot_r:.2f}"/>')
    else:
        pen = SVGPathPen(glyphs); glyphs[cmap[ord(it[2])]].draw(pen)
        tag.append(f'<path transform="translate({start_x + it[1]:.2f} {baseline:.2f}) scale({sc:.5f} {-sc:.5f})" d="{pen.getCommands()}"/>')
tag.append("</g>"); body.extend(tag)
print(f"tagline: {len(items)} glyphs/dots, width {text_w:.0f}px, cap {cap:.1f}px")

# ---------- 4. dashes, traced from the originals and stretched to fit ----------
dash_len = (SPAN_R - SPAN_L - text_w - 2 * GAP) / 2
for side, (xa, xb) in (("left", (0, 480)), ("right", (1500, W))):
    m = np.zeros_like(full); m[616:, xa:xb] = full[616:, xa:xb]
    ys, xs = np.nonzero(m); x0, x1 = xs.min(), xs.max() + 1; orig_len = x1 - x0
    g, bb = gradient_for(ys, xs, f"dash-{side}"); defs.append(g)
    k = dash_len / orig_len
    anchor = x0 if side == "left" else x1                      # scale about the outer end
    tx = (SPAN_L - x0) if side == "left" else (SPAN_R - x1)    # outer ends stay at the span edges
    body.append(f'<path id="dash-{side}" fill="url(#dash-{side})" transform="translate({tx:.2f} 0) translate({anchor} 0) scale({k:.4f} 1) translate({-anchor} 0)" d="{trace(m)}"/>')
print(f"dashes: {dash_len:.0f}px each (original {orig_len}px)")

# ---------- write ----------
pad = 12
vb = (259 - pad, 27 - pad, (1730 + pad) - (259 - pad), (699 + pad) - (27 - pad))
svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb[0]} {vb[1]} {vb[2]} {vb[3]}" width="{vb[2]}" height="{vb[3]}">\n'
       f'<title>Fire &amp; Finn — Hibachi · Sushi · Poke</title>\n<defs>' + "".join(defs) + "</defs>\n" + "\n".join(body) + "\n</svg>\n")
open(OUT, "w", encoding="utf-8").write(svg)
print("wrote", OUT, f"({len(svg)//1024} KB)")
