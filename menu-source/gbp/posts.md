# Google Business Profile posts (rebrand)

Three posts, each an image from `posts.html` (1200 × 900, rendered to the PNG named here) and the text below. Text is under 300 characters, plain, no hashtags, no emoji, no claim beyond what the site and the signage already say. Nothing here is posted by anyone but the owner.

**Post the rename now. It stays up through April**: people arriving in January search the old name from out of state. The other two are optional, any time, in no particular order.

Render the images with:

```
msedge --headless=new --disable-gpu --hide-scrollbars --virtual-time-budget=4000 --window-size=1200,900 --screenshot=rename.png "file:///.../menu-source/gbp/posts.html?post=rename"
```

(`?post=hero`, `?post=order` for the other two.)

## 1. Rename — `rename.png`

Post type: Update. Button: none.

> Island Panda is now Fire & Finn. Same kitchen, same address, new name. Hibachi, sushi and poke at 2003 Periwinkle Way, Sanibel. Open daily 11am to 8pm.

(151 characters)

## 2. Grilled hot. Rolled cold. — `hero.png`

The site's share card at 4:3: hot plate left, roll right, the line in Tenor Sans in the dark gap between them. Post type: Update. Button: Learn more → https://fireandfinn.com

> Grilled hot. Rolled cold. Hibachi seared to order on one side of the menu, specialty rolls, classic rolls and build-your-own poke on the other. 2003 Periwinkle Way, Sanibel. Open daily 11am to 8pm.

(197 characters)

## 3. Order ahead — `order.png`

Post type: Update. Button: Order online → https://order.toasttab.com/online/fire-and-finn-2003-periwinkle-way (the same `ORDER_URL` the site uses; the link lives in the button, never in the image). The image names the site and the phone for people who will not tap.

> Order ahead for pickup at fireandfinn.com, or call (239) 579-0783. 2003 Periwinkle Way, Sanibel.

(96 characters)

## Rules

- Image text stays inside the central 80 % of the frame; Google crops to 4:3 and rounds the corners.
- Fonts and colours are the site's and the slides': Jost and Tenor Sans, ground `#0B0C0E`, ink `#F2F0EB`, fire `#F07840`, sea `#62C6EC`.
- No QR codes, no prices in the images (prices live on the boards and the menu page), no "same family" or sourcing claims, no promise about how fast an order is ready.
