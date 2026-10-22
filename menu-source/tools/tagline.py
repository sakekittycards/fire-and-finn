import sys
sys.path.insert(0, r'C:/Users/lunar/AppData/Local/Temp/ffm/lib')
import pymupdf
ORIG, JOST, OUT, TEXT = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
TRACK = float(sys.argv[5]); MIN_DASH = float(sys.argv[6])
FORCE_CAP = float(sys.argv[7]) if len(sys.argv) > 7 and sys.argv[7] != "-" else None
NODASH = len(sys.argv) > 8 and sys.argv[8] == "nodash"
pix = pymupdf.Pixmap(ORIG); assert pix.alpha, "logo has no alpha channel"
W, H, N = pix.width, pix.height, pix.n
buf = bytearray(pix.samples)

def bbox_of(samples, w, n, x0, x1, y0, y1, thr=24):
    mnx = mny = 10**9; mxx = mxy = -1
    for y in range(y0, y1):
        base = y * w * n
        for x in range(x0, x1):
            if samples[base + x * n + 3] > thr:
                if x < mnx: mnx = x
                if x > mxx: mxx = x
                if y < mny: mny = y
                if y > mxy: mxy = y
    return (mnx, mny, mxx + 1, mxy + 1) if mxx >= 0 else None

Y0 = 616                                   # everything below the wave strokes
L = bbox_of(buf, W, N, 0, 480, Y0, H); R = bbox_of(buf, W, N, 1500, W, Y0, H); T = bbox_of(buf, W, N, 480, 1500, Y0, H)
print("orig: left dash", L, "| text", T, "| right dash", R)
r = g = b = c = 0
for y in range(T[1], T[3]):
    for x in range(T[0], T[2]):
        i = (y * W + x) * N
        if buf[i + 3] > 200: r += buf[i]; g += buf[i + 1]; b += buf[i + 2]; c += 1
tc = (r // c, g // c, b // c); print("text colour", tc, "cap height", T[3] - T[1])

font = pymupdf.Font(fontfile=JOST)
def render(size, track):
    doc = pymupdf.open(); page = doc.new_page(width=3200, height=400)
    x = 100.0
    col = (tc[0] / 255, tc[1] / 255, tc[2] / 255)
    caph = size * 0.70   # cap height of Outfit is ~0.70 em
    for ch in TEXT:
        if ch == "•":
            rr = caph * 0.15
            page.draw_circle((x + rr, 250 - caph / 2), rr, color=None, fill=col)
            x += 2 * rr + size * track
            continue
        if ch != " ":
            page.insert_text((x, 250), ch, fontsize=size, fontfile=JOST, fontname="JostTag", color=col)
        x += font.text_length(ch, fontsize=size) + size * track
    pm = page.get_pixmap(alpha=True)
    return pm, bbox_of(pm.samples, pm.width, pm.n, 0, pm.width, 0, pm.height)

span_l, span_r = L[0], R[2]                 # the tagline may use the same overall width as before
gap = 26
cap = T[3] - T[1]
pm0, b0 = render(100, TRACK)
h100 = b0[3] - b0[1]; w100 = b0[2] - b0[0]
chosen = None
for cap_scale in ((FORCE_CAP,) if FORCE_CAP else (0.92, 0.88, 0.84, 0.80, 0.76, 0.72)):
    size = 100 * (cap * cap_scale) / h100
    width = w100 * size / 100
    dash = (span_r - span_l - width - 2 * gap) / 2
    print(f"  cap x{cap_scale}: size {size:.1f}px, text width {width:.0f}px, dashes {dash:.0f}px each")
    if (dash >= MIN_DASH or FORCE_CAP) and chosen is None: chosen = (size, cap_scale)
size, cap_scale = chosen
pm, tb = render(size, TRACK)
tw, th = tb[2] - tb[0], tb[3] - tb[1]
dash_len = 0 if NODASH else int(round((span_r - span_l - tw - 2 * gap) / 2))
print(f"chosen: cap x{cap_scale}, size {size:.1f}px, text {tw}x{th}px, dashes {dash_len}px")

# keep the original dashes (cropped before clearing), squeezed to the new length
def crop(src, bb):
    rect = pymupdf.IRect(*bb); p = pymupdf.Pixmap(src.colorspace, rect, True); p.clear_with(0); p.copy(src, rect); p.set_origin(0, 0); return p
ld = rd = None
if dash_len > 0: ld = pymupdf.Pixmap(crop(pix, L), dash_len, L[3] - L[1]); rd = pymupdf.Pixmap(crop(pix, R), dash_len, R[3] - R[1])

for y in range(Y0, H):                    # clear the old tagline row
    base = y * W * N
    for x in range(W):
        i = base + x * N; buf[i] = buf[i + 1] = buf[i + 2] = buf[i + 3] = 0

def paste(src, sb, cx, cy):
    sw, sn, ss = src.width, src.n, src.samples
    bw, bh = sb[2] - sb[0], sb[3] - sb[1]
    dx = int(round(cx - bw / 2)) - sb[0]; dy = int(round(cy - bh / 2)) - sb[1]
    for y in range(sb[1], sb[3]):
        for x in range(sb[0], sb[2]):
            si = (y * sw + x) * sn; a = ss[si + 3]
            if a == 0: continue
            tx, ty = x + dx, y + dy
            if 0 <= tx < W and 0 <= ty < H:
                ti = (ty * W + tx) * N
                buf[ti], buf[ti + 1], buf[ti + 2], buf[ti + 3] = ss[si], ss[si + 1], ss[si + 2], a

tcy = (T[1] + T[3]) / 2; dcy = (L[1] + L[3]) / 2
paste(pm, tb, (span_l + span_r) / 2, tcy)
if ld: paste(ld, (0, 0, ld.width, ld.height), span_l + dash_len / 2, dcy)
if rd: paste(rd, (0, 0, rd.width, rd.height), span_r - dash_len / 2, dcy)
out = pymupdf.Pixmap(pymupdf.csRGB, W, H, bytes(buf), True); out.save(OUT); print("wrote", OUT)

# side-by-side check strip: original tagline row over the new one, on the brand black
strip = pymupdf.open(); pg = strip.new_page(width=1600, height=300)
pg.draw_rect(pg.rect, color=None, fill=(8 / 255, 8 / 255, 8 / 255))
pg.insert_image(pymupdf.Rect(0, 0, 1600, 150), pixmap=crop(pix, (194, 560, 1794, 710)))
pg.insert_image(pymupdf.Rect(0, 150, 1600, 300), pixmap=crop(out, (194, 560, 1794, 710)))
pg.get_pixmap(dpi=72).save(OUT.replace(".png", "-compare.png")); print("wrote compare strip")
