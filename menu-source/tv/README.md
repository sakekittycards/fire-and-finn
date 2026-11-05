# Fire & Finn digital signage system

Fourteen 1920 × 1080 templates in one file, `slides.html`, rendered to PNG with headless Edge. The brand lives in the template; a location lives in `location.js`.

## Render

```
msedge --headless=new --disable-gpu --hide-scrollbars --window-size=1920,1080 --screenshot=welcome.png "file:///C:/.../slides.html?slide=welcome"
```

Slide names: `welcome`, `menu-hot`, `menu-cold`, `drinks`, `promo-hibachi`, `promo-poke`, `promo-drinks`, `hours`, `order-online`, `review-google`, `review-tripadvisor`, `review-yelp`, `location`, `lto`. Export every slide as PNG at 1920 × 1080; TVs play the PNGs in a loop (8 to 12 seconds per slide, menu boards longer).

## Nationally controlled (do not edit per location)

| Element | Standard |
|---|---|
| Logo | `assets/logo-compact.svg`, 300 px wide, always at x 70 / y 44. Never redrawn, never recoloured. |
| Canvas | 1920 × 1080, safe margin 70 px on every side. Nothing but photographs and the waterline touch the edges. |
| Headlines | Jost 600, uppercase, letter-spacing .04em; sizes 140 (hours), 112 (promo), 104 (QR slides), 66 (menu board titles). |
| Menu type | Item names Jost 500 32 px, prices Jost 600 32 px with dotted leaders, descriptions Jost 400 26 px, section headers Jost 600 34 px tracked caps with a rule. |
| Tagline | Outfit 400, tracked caps, "Hibachi • Sushi • Poke" with cyan dots. |
| Colours | Background #080808, ink #F2F0EB, muted #CFCAC2, dim #A39D95. Hot (hibachi, katsu, hot appetizers): #F07840. Cold (sushi, poke, drinks): #62C6EC. |
| Glow | Warm radial bottom-left, cool radial top-right; hot slides lean warm, cold slides lean cool. Film grain at 6 %. |
| Photography | Real-looking plated food on dark surfaces, warm directional light for hot items, cool clean light for cold. Photo sits on the right, feathered into the dark over the left 30 %. No text, logos or hands in photos. |
| Waterline | The cyan wave strip along the bottom edge on promo, hours, QR and location slides. Never on menu boards. |
| QR panel | 600 × 600 white rounded panel at x 1170 / y 230, code inside with 34 px of white around it, label beneath in tracked caps. |
| Footer | Allergen line left, website right, 22 px dim, on menu boards only. |
| Voice | Plain, confident, short. "Hot off the grill", "Build your bowl", "Order ahead". No slogans tied to a place. |

## Location-editable (`location.js`)

Address, city, phone, hours, website, optional map image, QR file paths, and the limited-time-offer copy and photo. Change the file, re-render, done.

## QR codes

`make-qr.py <order|google|tripadvisor|yelp> <https link>` writes an SVG into `qr/` and points `location.js` at it. Use only links you have opened yourself. Yelp's guidelines prohibit asking for reviews, so the Yelp slide links to the business page and says "Find us", not "Rate us". Test each rendered slide with a phone camera across the room.

## Checks before a slide goes on a TV

No cropped or overflowing text, no hard image rectangles, no ghosting, prices and ingredients match the printed menu, raw markers on the right items, allergen line present on menu boards, QR scans to the right place.

## Open verification items

- "Gluten-free hibachi available" and the raw (*) markers are copied from the printed v8 menu; the kitchen should confirm them before the boards go live.
- Drinks list is the current Toast beverage and alcohol list. Tessake is a 6% canned sparkling sake (labelled on the board). "Senorita" is unconfirmed: the name belongs to both a bottled 12.5% margarita and a THC-infused canned margarita line; the owner must confirm which is stocked before it stays on the board, and if it is the THC product it should come off the board entirely.
