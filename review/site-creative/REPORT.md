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

11. Cache-busting bumped to `?v=8` on the stylesheet and script in `index.html` and `404.html` (now `?v=10`, see 22).

## Second pass (after Nick's "keep going")

12. **Responsive photographs.** Each of the six photos now has 640px and, where the original is larger, 1024px variants
    (`assets/food/*-640.jpg`, `*-1024.jpg`), wired with `srcset`/`sizes` on every `<img>` and on the two hero preloads.
    A 1x phone now downloads about 140KB and 56KB for the two hero images instead of 294KB and 184KB; the signature-roll
    thumbnail loads the 640 file instead of the 1536 one. Retina phones still receive the full-size files, which is the
    correct choice for their pixel density. Verified by reading `currentSrc` at 390@1x, 390@3x, 768@2x, 1440@1x, 1440@2x.
13. **Hero hover interplay.** Hovering a side brightens its photograph slightly and dims the other line of the headline,
    so "Grilled hot." and "Rolled cold." answer the side you are over. A first version lightened the dark mask instead and
    exposed a vertical edge at the seam (the slider look I had rejected), so it was replaced with the photo brighten.
14. **The seam inside the menu.** A one-pixel line that runs orange into blue marks where the menu turns from the hot
    categories to the cold ones, the same device as the footer's rule.
15. **Accessible names.** The two hero links now have short `aria-label`s ("Hibachi and appetizers, the hot side of the
    menu") instead of announcing a long photo description plus the label. Buttons press down one pixel on click.

Overflow metrics re-run after this pass: still 0 at all three sizes; menu text still identical.

## Third pass (the critical one, against the best restaurant sites)

Method: the page at 390, 768 and 1440, section by section, asking of each screen whether a Noma, Momofuku or Sweetgreen
designer would leave it. What changed, and what I judged fine as it was.

16. **The phone hero is the split again, not a photo with a headline under it.** At 390 the cold picture sat below the fold,
    so the first screen was a hibachi photo, a headline and two buttons: the one idea never landed. Now both pictures are on
    the first screen (each 26% of the viewport, the hot one above, the cold one below) with the headline, lead and status in
    the dark seam between them, and each picture keeps its caption at its bottom-left. The hero's own Order and See the menu
    buttons are gone on phones only: the fixed bottom bar already carries Order and Menu a thumb away, and repeating them
    200px above the bar was what cost the cold side its place on screen. Tablets (760 to 899px) keep the buttons in a row and
    also show both pictures; wide screens are unchanged. I tried a centered seam with the captions at the outer edges first;
    centered captions landed on the food and disappeared, so the whole phone hero went back to one left axis.
17. **Tablet menu openers are title-beside-photo.** Between 760 and 999px the category photographs were full-width 4:3 pictures
    (about 710 by 530px) between the notes and the prices: a screen of photo before every price list. They now sit in a
    two-column opener, title and notes left, photograph right, with the prices directly below. The page at 768 is 1,400px
    shorter. On phones the pictures are 3:2 instead of 4:3 (the poke bowl 4:3 instead of square) for the same reason.
    `sizes` on those images now tells the browser the picture is 45vw at tablet widths, so it picks the 640px file.
18. **The map is dark.** Visit ended in a bright white Google rectangle on a near-black page. The embed is now filtered
    (invert, hue-rotate 180, saturate .6) so roads are light lines on a dark ground and water stays blue; the pin, labels and
    Google attribution remain legible. The fallback panel behind it was already dark.
19. **Focus and keyboard.** Tabbing through the first screen goes skip link, logo, nav, Order, hot side, cold side, Order,
    See the menu, PDF, Order, categories: the reading order. Two rings were broken: on a hero side the inset outline painted
    beneath the photograph (positioned children paint over an element's own outline), so the ring is now drawn by the
    gradient overlay above the picture; in the scrolling category row the ring was clipped by the row's overflow, so it is
    inset there. Both verified by pressing Tab in headless Edge, not by scripting focus.
20. **Daylight.** The meta grey (`--dim`, used for the status line, notes, category links at rest) is a step brighter, 7.3:1
    on the ground instead of 6.5:1. The desktop lead over the photographs has a soft dark shadow.
21. **Entrance a third of a second quicker.** Pictures settle in 1.2s instead of 1.5s and the words follow sooner; the order
    is the same. The medium weight of Jost, used on the first screen for the captions and status, is now preloaded like the
    other two (10KB), so it no longer swaps in late.
22. Cache-busting is `?v=10` on both pages (main had moved `index.html` to v9 and left `404.html` at v8).

Judged fine as is, after looking hard:
- The desktop hero. The headline sits in the dark valley, the captions in the corners, the hover dims the other line.
- The empty sticky column beside Appetizers, Kids and Classic Rolls on wide screens: the category title in a left margin
  with the items beside it is the oldest menu layout there is, and it holds the left axis for every group. Filling it
  would be decoration.
- The header: clear over the hero, backed once the page moves; the category row and its sliding line, which crosses the
  Hot/Cold divider and changes colour as it does. Verified in motion (`transform` and `width` update, colour class flips).
- Type scale and measure: Tenor Sans titles at 2.6 to 4.4rem, Jost body at 17/18px, leads 24 to 38em, descriptions 36em.
- The Order band. Full-bleed photo, left-aligned type, two buttons, the live hours line. It is the hero's quieter sibling.
- Embers (six, slow, on the hot side only) and the drift on the menu photographs: both off under reduced motion, both tied
  to the idea rather than added to it. The grain overlay was removed in the first pass and has not come back.

Overflow metrics after this pass: 0 at all three sizes; page heights 9,055 / 7,111 / 6,631px (were 9,494 / 8,545 / 6,631).
Menu text identical: 88 of 88 items, headings, notes and the advisory.

## Board changes (after Nick's advisors read the third pass)

Conditional ship: three copy changes and two checks, one commit on top of the third pass.

23. **"Hibachi & starters"** is the hot side's hero label (was "appetizers"; three of the six appetizers are salads).
    The menu section header stays "Appetizers" as printed.
24. **The menu intro** now reads "the cold side rolls sushi and builds bowls." (was "rolls and builds to order",
    which sounded like a claim). Same sense, nothing promised.
25. **"Formerly Island Panda"** twice, so a returning customer learns in one glance that it is the same kitchen: in the
    hero meta row after the address, at the same muted size, and under the address in Visit as a dim line at the
    label size. Nowhere else; title, description and structured data unchanged per the board's "no other copy changes".
26. **Tab pass at 1440**, pressing Tab until focus wrapped: 34 stops. Skip link, brand, the four nav links, header Order;
    hero hot side, hero cold side, hero Order and See the menu; menu PDF and Order; the six category anchors; Order band
    Order and Call; Visit address, phone, Get Directions, Call Us, the map; footer links, address and phone. Nothing
    trapped, nothing skipped (the menu itself has no interactive elements). One fix came out of it: the map's fallback
    link sat beneath the loaded iframe and took focus invisibly; the fallback is now made inert when the iframe loads.
27. **The 390 map**, shot after the embed painted: road names, the house number, the pin, Google's controls and the
    attribution all read through the dark filter, so the filter stays.
28. Cache-bust `?v=11` on both pages, since styles and app.js changed.

Overflow after this pass: 0 at all three sizes; page heights 9,140 / 7,140 / 6,656px. Menu text identical: 88 of 88 items and the advisory.

## Fourth pass (findable and shareable, and a lighter first screen)

Main merged first (583389d, live as v11; only the TV signage folder had moved). One commit on top.

29. **Structured data knows the old name.** `alternateName` is now `["Island Panda", "Fire & Finn Hibachi · Sushi · Poke"]`;
    `hasMenu` already pointed at `https://fireandfinn.com/#menu` and stays; a `potentialAction` OrderAction carries the
    Toast URL (the same string as `ORDER_URL` in app.js) with pickup as the delivery method; telephone and the hours
    specification are unchanged. The JSON was parsed after the edit. `sameAs` was **not** added: the project memory
    holds the Business Profile location id but not a public Maps listing URL, and a guessed URL is worse than none.
30. **Meta description** ends "Formerly Island Panda." so the search snippet bridges the two names; the title stays
    brand-first.
31. **The share card is the hero idea.** `assets/og.jpg` and `og.png` (1200x630) are rendered from
    `review/site-creative/og-card.html` by `render-og.py` in headless Edge: the steak-and-scallops plate left, the
    Fire & Finn roll right, each fading fully into the ground so the seam is real darkness, "Grilled hot. / Rolled cold."
    in Tenor Sans in the seam with a one-line Jost sub ("Hibachi, sushi and poke on Sanibel"), the logo top left. Same
    photographs and fonts as the site. The first render let the roll run behind the headline; the halves now fade out
    by 80% of their width and the photographs are pushed outward. 137 KB JPEG, 215 KB PNG. `og:image`, `twitter:image`
    and the JSON-LD `image` carry `?v=2` so scrapers that cached the old card fetch this one; `og:image:alt` and a new
    `twitter:image:alt` describe it.
32. **The logo SVG is 24 KB, from 87 KB.** `assets/logo-compact.svg` is six traced paths (three flame strokes, two
    wave strokes, one outlined wordmark; no live text, no embedded image) with 11,759 three-decimal coordinates and
    five gradients. svgo 4.1 with multipass and one-decimal precision (the viewBox is 1,495 units wide, so a tenth of
    a unit is a fortieth of a pixel at 300px) brought it to 24 KB; renders of the old and new file at 300px and
    1,200px on a 2x canvas differ in zero pixels. Two decimals would have given 45 KB for the same zero-pixel result.
33. **The first screen weighs less.** Measured over http with the lazy menu photograph excluded: 390px at 2x went from
    about 565 KB to 418 KB, and 1440px from 565 KB to 418 KB. Not from the JPEG encoder, which was already at about
    quality 80 (re-encoding every food file saved 0 to 4%, so none were touched), but from the srcset: a phone at 2x
    needs a 780px hero and was being served the 1024px file. New 800px variants of the two hero photographs
    (`hero-hibachi-800.jpg` 187 KB, `fire-and-finn-roll-800.jpg` 72 KB) sit in the srcsets and the preloads, so
    phones at 2x and desktops at 1x pick them; 3x phones still get the 1024px files. The logo cut is the other 63 KB.
34. No change to `styles.css` or `app.js` this pass, so the cache-bust stays at `?v=11`. The two new JPEGs are new
    file names; the SVG and the card replace files in place and look the same or are only read by scrapers.

Looked at again and left alone: the hero at all three sizes, the three-line meta row on phones (status, address,
Formerly), the menu rhythm, the Order band, Visit and the footer. The footer does not repeat "Formerly Island Panda";
two mentions is the brief and the right amount.

Overflow after this pass: 0 at all three sizes; page heights unchanged. Menu text identical: 88 of 88 items and the advisory.

### Board fixes on the fourth pass

35. **The description leads with the old name.** Google clips at about 155 characters on a laptop and 120 on a phone, and
    "Formerly Island Panda." began at character 153. It is now the first phrase; "Order online for pickup." was dropped
    to keep the whole line at 150 characters. `og:description` opens the same way.
36. **The card is the logo, two plates and the line.** The 24px subline is gone (unreadable at a 420px preview and a
    fourth phrasing of the descriptor). "cold." had ended exactly on the roll's left edge; the photo halves are now 41%
    of the card each and the headline 88px, so both photographs are fully dark about 200px before the centre and the
    line ends in black on both sides, measured on the render. og.jpg 103 KB, og.png 164 KB; both alts rewritten to match.
37. **3x phones get a 1200px roll.** `fire-and-finn-roll-1200.jpg` (130 KB) joins the srcset and the preload, so a 390px
    phone at 3x fetches it instead of the 1536px file (184 KB). The hibachi hero cannot have a 1200px variant: its
    source is 1024px wide, and upscaling would add bytes without detail, so 3x phones still take the 1024px file,
    which is the largest there is. First screen at 390: 418 KB at 2x, 583 KB at 3x (was 638).

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
2. **The Spicy Lava Drops caption** on the specialty-rolls photograph names the dish in the picture. The file was generated
   as that dish; the owner should agree it looks like theirs.
3. **The map** loads from Google when online and is shown dark through a CSS filter; check it on a real phone, and if Google changes the embed's palette the filter may need retuning.
4. **Hours in Visit are written out** ("Every day, 11am to 8pm"); the live open/closed line is in the hero and the Order band.
5. **Window heights under about 640px on desktop** keep the hero at 640px, so a very short laptop window scrolls slightly to
   see the side labels. Acceptable, but worth a look on a 13-inch screen.
6. **The Toast link opens in a new tab**, as before.
7. **No Order button inside the phone hero.** The bottom bar is the order button on phones; if the owner wants one in the
   hero as well, delete the `@media (max-width: 759px) { .hero .cta { display: none; } }` rule and the cold picture drops
   below the fold again on an 844px-tall phone.
8. **"Formerly Island Panda"** is on the page twice (hero meta row, Visit address), in the meta description and in the
   JSON-LD `alternateName`. `sameAs` with the Google listing is still missing: it needs the public Maps URL of the
   Business Profile (share link from the listing), which is not in the project or its notes.
9. **The share card** is cached by Facebook, iMessage and Slack per URL; the `?v=2` on `og:image` makes them refetch, but
   a card already posted keeps the old picture. The Facebook Sharing Debugger can force a rescrape once v11 is live.

## Files

- `index.html`: new shell; menu groups moved into `.g-side` / `.g-main` columns with their original markup inside; `srcset` on every photograph.
- `assets/food/*-640.jpg`, `*-1024.jpg`: resized variants of the six photographs (same pictures, smaller).
- `styles.css`: rewritten.
- `app.js`: settings block untouched; reveal logic removed; category-row indicator added; embers now live in the hot half.
- `404.html`: restyled; `?v=11`.
- `assets/og.jpg`, `assets/og.png`: the share card, rebuilt from `review/site-creative/og-card.html` with `render-og.py`.
- `assets/food/fire-and-finn-roll-1200.jpg`: 1200px roll variant for 3x phones.
- `assets/logo-compact.svg`: same drawing, 24 KB instead of 87 (svgo, one-decimal precision, zero-pixel diff).
- `assets/food/hero-hibachi-800.jpg`, `fire-and-finn-roll-800.jpg`: 800px hero variants for 2x phones and 1x desktops.
- `README.md`: file list updated.
