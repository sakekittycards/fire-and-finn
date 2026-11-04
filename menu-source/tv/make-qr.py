"""Fire & Finn — QR codes for the signage templates.

Usage:  python make-qr.py order "https://order.toasttab.com/online/..."
        python make-qr.py google "https://g.page/r/..../review"
Writes qr/<name>.svg (crisp at any size) and points location.js at it.
Only run it with a link you have opened and checked yourself; the slide shows
a labelled placeholder until then. Test every rendered slide with a phone
camera from the far side of the room before it goes on a TV.
"""
import sys, os, re
import qrcode, qrcode.image.svg

name, url = sys.argv[1], sys.argv[2]
assert name in ("order", "google", "tripadvisor", "yelp"), "name must be order, google, tripadvisor or yelp"
assert url.startswith("https://"), "give the full https:// link"
here = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(here, "qr"), exist_ok=True)
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, border=0)   # the white panel in the slide is the quiet zone
qr.add_data(url); qr.make(fit=True)
img = qr.make_image(image_factory=qrcode.image.svg.SvgPathImage)
out = os.path.join(here, "qr", f"{name}.svg")
img.save(out)
loc_path = os.path.join(here, "location.js")
loc = open(loc_path, encoding="utf-8").read()
loc, n = re.subn(rf'(\b{name}:\s*)"[^"]*"', rf'\1"qr/{name}.svg"', loc, count=1)
open(loc_path, "w", encoding="utf-8").write(loc)
print(f"wrote {out} and pointed location.js at it ({n} field updated). Re-render the slides.")
