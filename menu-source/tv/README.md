# Fire & Finn digital signage system (v4)

Fifteen 1920 × 1080 templates in one file, `slides.html`, rendered to PNG with headless Edge. The brand lives in the template; a location lives in `location.js`.

## Render

```
msedge --headless=new --disable-gpu --hide-scrollbars --virtual-time-budget=4000 --window-size=1920,1080 --screenshot=welcome.png "file:///C:/.../slides.html?slide=welcome"
```

Slide names: `welcome`, `menu-hot`, `menu-cold`, `menu-full`, `drinks`, `promo-hibachi`, `promo-poke`, `promo-drinks`, `hours`, `order-online`, `review-google`, `review-tripadvisor`, `review-yelp`, `location`, `lto`. Export every slide as a PNG at 1920 × 1080; the TVs play the PNGs in a loop.

## The system in one paragraph

Three silhouettes and one signature. **Boards** are dark and dense and are meant to be read for a while. **Appetite slides** are dark with a photograph on the right and one big sentence. **Utility slides** split the screen in half: logo and headline on the dark left, a cream pane on the right that holds the thing you act on (a QR code, the hours, the address or map). The signature is the **baseline**: a 48 px band along the bottom edge of every slide that lights the slide from below. It is 48 px because consumer TVs overscan 2 to 3 % (32 px at 1080p); a 12 px line vanished behind the bezel, a 48 px band still shows. It is solid fire on hot slides, solid sea on cold slides, and fire | sea split at the centre on brand and utility slides, where the seam lands exactly on the edge of the cream pane. It is the logo's flames-over-waves told as geometry, and it tells you a slide's temperature from across the room.

## Loop order

Alternate silhouettes so the loop has rhythm: a board, then an appetite slide, then a utility slide. One review slide per cycle, never two; three in a row reads as nagging. A cycle that works: `menu-hot`, `promo-hibachi`, `hours`, `menu-cold`, `promo-poke`, `order-online`, `drinks`, `promo-drinks`, `welcome`, `location`, `lto`, then one of `review-google` / `review-tripadvisor` / `review-yelp`, rotating each cycle (or each week). Boards hold 20 to 40 seconds, everything else 8 to 10. A single-TV setup replaces the two boards with `menu-full` and holds it longer.

## Nationally controlled (do not edit per location)

| Element | Standard |
|---|---|
| Logo | `assets/logo-compact.svg`, 300 px wide, always at x 70 / y 44, always on the dark ground. Never redrawn, never recoloured. |
| Canvas | 1920 × 1080, safe margin 70 px on every side. Only photographs, the cream pane and the baseline touch the edges. Nothing that must be read lives in the outer 3 % (58 px left and right, 32 px top and bottom), because consumer TVs crop it. Set the TV to Just Scan / Screen Fit / 1:1 where the menu allows. |
| Baseline | 48 px band on the bottom edge of every slide. Fire `#F07840` on hot slides, sea `#62C6EC` on cold slides, fire \| sea split at x 960 on brand and utility slides. The only glow on a slide rises from the baseline in its colour. |
| Silhouettes | Boards: title at x 420 / y 52, grid from y 205 to the footer. Appetite: copy column 820 px wide from x 70, vertically centred, photo on the right feathered into the dark over its left 32 %. Utility: dark left half, cream pane `#E6E2D9` from x 960 to 1920, content centred in the pane. |
| Headlines | Jost 600. Sentence case for anything with a voice (promos, hours, order, reviews, location), 150 px (180 px for a single word, 168 px for the two-line welcome). Tracked caps are wayfinding only: board titles (66 px, .1em), section headers (34 px, .14em), the QR label (30 px, .14em). No eyebrow labels above headlines. |
| Menu type | Item names Jost 500 32 px, prices Jost 600 32 px in ink (never in fire or sea: cream carries more light than orange on a TV, and saturated small type blooms), dotted leaders in the board's temperature colour at 40 %, descriptions Jost 400 26 px, section headers with a rule. The hot board has room and runs names 36 px, descriptions 28 px. Hibachi proteins and classic rolls are price tiles with prices in ink. |
| Full menu | `menu-full` carries names and prices only (27 px) with the hibachi lede, kids notes and poke steps at 22 px. Descriptions live on the two-board set. |
| Floors | Nothing under 22 px on a board. Nothing under 18 px anywhere. |
| Tagline | Outfit 400 36 px, tracked caps, "Hibachi • Sushi • Poke" with sea dots. Welcome slide only. The welcome slide is typographic: sea line, fire line, split baseline. It is the key to the colour code and carries no photograph. |
| Colours | Ground `#0B0C0E`, cream `#E6E2D9` (dropped from `#F2F0EB` in v4 so the pane is not a lamp in a dim room), coal `#15161A` (type on cream), ink `#F2F0EB`, muted `#CFCAC2`, dim `#A39D95`. Hot (hibachi, katsu, hot appetizers): `#F07840`. Cold (sushi, poke, drinks): `#62C6EC`. Fire and sea are never used as text on the cream pane. Film grain at 4 %, there only to break banding in the glow. |
| Photography | Real-looking plated food on dark surfaces, warm directional light for hot items, cool clean light for cold. Photo sits on the right, 980 to 1040 px wide, and never crosses x 820 so it stays clear of the logo and copy. No text, logos or hands in photos. |
| QR | 620 × 620 directly on the cream pane (the pane is the quiet zone), label beneath in tracked caps. A dashed placeholder shows until `location.js` points at a real code. |
| Footer | Allergen line left, website right, 22 px dim, on boards only, sitting 26 px above the baseline. |
| Voice | Plain, confident, short. One idea per appetite slide: a headline and at most two short lines. "Hot off the grill", "Build your bowl", "Order ahead", "The cooler". The three review slides each give a different reason (how did we do / tell other travelers / menu, photos and hours); none says "every one helps". No slogans tied to a place. Yelp says "Find us", never "Rate us". |

## Location-editable (`location.js`)

Area name, address, city, phone, hours, website, optional map image, QR file paths, and the limited-time-offer copy and photo. Change the file, re-render, done.

- `hours` is rendered at 150 px on the cream pane; keep it to about ten characters ("11am – 8pm").
- `map` sits on the cream pane at up to 860 × 900 px. Supply a transparent PNG with dark linework and no baked-in text; the address and phone move to the dark side when a map is present. Leave it `""` until such an asset exists.
- `ltoTitle` is rendered at 120 px; two short words per line.

## QR codes

`make-qr.py <order|google|tripadvisor|yelp> <https link>` writes an SVG into `qr/` and points `location.js` at it. Use only links you have opened yourself. Yelp's guidelines prohibit asking for reviews, so the Yelp slide links to the business page and says "Find us", not "Rate us". Test each rendered slide with a phone camera from the far side of the room.

## Checks before a slide goes on a TV

No cropped or overflowing text, no hard image rectangles, no ghosting, prices and ingredients match the printed menu, raw markers on the right items, allergen line present on boards, baseline present and in the right colour, nothing but the baseline and photographs in the outer 3 %, QR scans to the right place.

## TV-tuned export

Consumer TVs crush blacks and push reds. Alongside the plain PNGs, export a tuned set with ffmpeg and try both on the actual TV; keep whichever reads better in the room:

```
ffmpeg -i welcome.png -vf "eq=contrast=1.10:brightness=-0.025,curves=r='0/0 0.5/0.52 1/1':b='0/0 0.5/0.46 1/1'" tv-tuned/welcome.png
```

## Verified with the owner (2026-11-05)

- Gluten-free hibachi: confirmed; it means gluten-free soy sauce on request.
- Raw (*) markers on the boards match the kitchen's list.
- Tessake is a 6% canned sparkling sake and is labelled on the board. "Senorita" in the cooler is a THC-infused canned margarita and is deliberately left off every screen.
- Still open: QR links (order, Google, Tripadvisor, Yelp) and a clean Sanibel map asset (transparent, dark linework).

## History

`slides-v1.html` is the first pass, kept for reference. v2 added the location config and the franchise rules. v3 (2026-11-07) replaced the wave strip and twin glows with the baseline, split the utility slides into dark and cream halves, removed eyebrow labels and bullet lists, and rebuilt `menu-full` so nothing drops under 22 px. v4 (2026-11-08) was the distance-and-TV pass: the baseline grew from 12 to 48 px so it survives overscan, the footer and boards moved up with it, prices went to ink, the hot board's type grew to fill its room, the cream pane dropped to `#E6E2D9`, grain to 4 %, the welcome slide became typographic (it had duplicated the hibachi photo), every appetite slide was cut to one idea, the hours slide lost its web line, the three review slides got three different reasons and a one-per-cycle loop rule, and a TV-tuned export joined the deliverable.
