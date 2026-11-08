# fireandfinn.com creative pass — report

Branch `claude/site-creative-pass-a72416`, November 2026. Nothing pushed, nothing deployed.
Screenshots in this folder: `before-*` is the v7 site, `after-*` is this branch, each at 390x844, 768x1024 and 1440x900,
as the first screen (`-WxH.jpg`) and the full page (`-WxH-full.jpg`). `*-metrics.json` holds the overflow checks.

## The one idea

The logo already says everything: flames above the name, waves below it. The site now does the same thing with the food.
The hero is two photographs, the hibachi plate on the hot side and the Fire & Finn roll on the cold side, meeting in a dark
seam that carries the headline. On a phone they stack in the logo's own order: fire above the words, water below them.
Each side names itself (The hot side, Hibachi & appetizers / The cold side, Sushi rolls & poke) and is a link into its half
of the menu, so the two-temperature idea is explained without a section of copy. Nothing else on the page competes with it.

## Major decisions and why

1. **The three showcase rows are gone; the menu is the page.**
   Hibachi, Sushi and Poke each had a marketing row with prices and picks that repeated the menu below, and on a phone they
   pushed the actual menu three screens down. The photography they carried now lives inside the menu: every category has a
   sticky side column with its title, notes and picture (hibachi plate, Spicy Lava Drops, poke bowl), and the items scroll
   beside it. One scroll, no repetition, and a takeout customer reaches prices immediately.
   Every item name, price and description is byte-for-byte unchanged. I verified this with a script that extracted all 88
   names, prices, descriptions and headings from the old menu and the new one and compared the plain text: identical.

2. **The ground warms and cools.** The page background shifts to a faint warm black under the hot categories and a faint
   cool black under the cold ones, with a soft orange or blue glow at the top of each. It is subtle on purpose; you feel
   the menu change temperature before you notice why.

3. **The category row is hot on the left, cold on the right, with one sliding line.** Instead of pill buttons, a thin row
   of links with a 2px indicator that slides under the category on screen and takes its colour (orange, then blue). On
   phones the row scrolls and fades at its right edge so it reads as scrollable.

4. **Typography: sentence case, no rules.** The tracked all-caps headings with hairline rules were the most templated
   thing on the old page. Titles are now Tenor Sans in sentence case (the brand face, as on the logo), large enough to
   carry a section on their own. Jost stays for reading. Outfit was loaded for one footer line and is gone.

5. **No cards, no glass.** The order card, the visit card, the signature-roll card and the blurred glass panels are gone.
   Order is the rolling-hands photo full bleed with left-aligned type; Visit is a plain definition list with hairlines
   and the map beside it. The only remaining surfaces are the menu's price grids, which are information.

6. **Photography, one job each.** Hero: hibachi plate (hot) and the Fire & Finn roll (cold). Menu openers: hibachi plate
   with the grill glow, Spicy Lava Drops, poke bowl. Order band: hands on the rolling mat. The roll reappears once, small,
   beside the signature-roll entry. Nothing is used twice at size. The grain overlay is gone; the photographs supply texture.

7. **Motion is one entrance and a slow drift.** On load, the two photographs settle out of the dark, then the headline,
   lead, buttons and status rise in order. Scrolling drifts the menu photographs a few pixels on wide screens. Six embers
   rise off the hot side. The waterline SVG, the breathing glow and the per-section fade-ups are removed. Under
   `prefers-reduced-motion` every animation and transition is off (verified: no embers, animation names `none`, parallax off).

8. **Header is fixed and clear over the hero**, taking its backing once the page moves. The open/closed line, the green
   light on Order buttons while the kitchen is open, the Toast link on every `[data-order]` button, the phone link, address
   and hours are all unchanged and verified (clock fixed at 1pm Eastern: "Open now, until 8pm", `body.is-open`, Toast URL).

9. **Copy edits, small.** Lead: "Hibachi seared on the flat-top. Sushi rolled to order. Poke bowls you build yourself."
   Menu intro: "One kitchen, two temperatures. The hot side runs the grill; the cold side rolls and builds to order."
   Footer: "Hibachi, sushi and poke. Grilled hot, rolled cold." "On Sanibel Island" left the hero lead and the footer;
   the location stays in the status line, the Order band, Visit, the footer address, the title tag and metadata.

10. **404** restyled to the same system (logo, two-colour headline, two buttons, a warm rule above and a cool rule below).

11. Cache-busting bumped to `?v=8` on the stylesheet and script in `index.html` and `404.html`.

## Considered and rejected

- A hard vertical seam between the two hero photographs: reads as a before/after slider. Soft masks into a dark valley instead.
- Full-bleed "chapter opener" photographs between menu categories: dramatic, but they break the menu into a slideshow and
  double the scroll on phones. Sticky side columns keep the picture and the prices together.
- Changing the page colour by scroll position in JavaScript: a CSS gradient per temperature does it without a scroll handler.
- A name-origin line ("Fire is the grill, Finn is the fish"): memorable, but it would be an invented claim. Not written.
- Keeping the Chef's picks list and the hibachi price board in the showcases: duplicates of the menu, removed with them.
- Numbered markers anywhere but the poke steps, which are a real sequence.
- A sticky "Order" button on desktop: the header already carries it, and the phone has its bottom bar.
- Keeping the Three ways to eat here heading as a short band: the hero's side labels already say it.

## Verification

- Headless Edge (`msedge` channel, viewport emulated through Playwright) at 390x844, 768x1024 and 1440x900: `scrollWidth`
  equals the viewport at all three sizes and no unclipped element extends past the viewport (`after-metrics.json`,
  overflow count 0 everywhere).
- State checks (not kept as files): sticky category row and indicator after scrolling to Specialty Rolls and Hibachi;
  hover on a hero side; open-now state on phone and desktop; the phone nav drawer; 404 at both sizes; reduced motion.
- Note on the raw command `msedge --headless=new --window-size=390,844 --screenshot`: on Windows the window cannot be
  narrower than roughly 480px, so that capture is a 390px crop of a wider layout and is not a phone render. The emulated
  viewport through the same headless Edge binary is what the `after-390x844` files show.
- Menu text identity: 88 of 88 items, headings and notes identical; the allergen advisory identical.

## Needs a human eye before it goes live

1. **Hero photographs are the AI stand-ins.** They now carry the whole first screen. When real photography arrives, the hot
   slot wants a portrait-ish plate shot with dark surroundings on its right; the cold slot wants a landscape roll or
   plate with dark surroundings on its left. Both are preloaded; real exports should be around 1200px and under 150KB each.
2. **"Hibachi & appetizers" as the hot side's label.** Three of the six appetizers are salads. "Hibachi & starters" or
   just "Hibachi" would also work; the owner should pick.
3. **"the cold side rolls and builds to order"** in the menu intro. Rolled to order was already on the site; "builds to
   order" assumes poke bowls are assembled when ordered. Confirm or cut to "the cold side rolls and builds."
4. **The Spicy Lava Drops caption** on the specialty-rolls photograph names the dish in the picture. The file was generated
   as that dish; the owner should agree it looks like theirs.
5. **The map** loads from Google when online; the review shots show the built-in fallback because the capture ran offline.
6. **Hours in Visit are written out** ("Every day, 11am to 8pm"); the live open/closed line is in the hero and the Order band.
7. **Window heights under about 640px on desktop** keep the hero at 640px, so a very short laptop window scrolls slightly to
   see the side labels. Acceptable, but worth a look on a 13-inch screen.
8. **The Toast link opens in a new tab**, as before.

## Files

- `index.html`: new shell; menu groups moved into `.g-side` / `.g-main` columns with their original markup inside.
- `styles.css`: rewritten.
- `app.js`: settings block untouched; reveal logic removed; category-row indicator added; embers now live in the hot half.
- `404.html`: restyled; `?v=8`.
- `README.md`: file list updated.
