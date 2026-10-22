# Fire & Finn — website photo briefs

Shot list for the photos the site is still missing, written so they can be handed to a photographer or pasted into an image generator. Every dish is described exactly as the menu sells it; nothing is invented. Rules that apply to every shot:

- No text, logos, menus, branded packaging, shirts or signage anywhere in the frame (nothing from Island Panda).
- Only ingredients the menu lists for that dish. No garnishes the kitchen does not use.
- Palette: near-black or charcoal backgrounds, warm light on hibachi, cool daylight on sushi and poke. Props in black ceramic, slate, bamboo and blue-glazed ceramic.
- Shallow depth of field, real steam and sauce texture, no heavy filters, no HDR look.
- Deliver as JPEG, quality 85, sRGB, at the pixel sizes below (the site shows them at half that size on phones, full size on large screens).

Where each file goes is noted. Replace the file at that path, keep the file name, and the site picks it up with no code changes except where a `PHOTO SLOT` comment in `index.html` says to swap a placeholder for the image tag.

---

## 1. Hero plate — `assets/food/hero-hibachi.jpg` (1500 × 1200, 5:4)

**Subject:** Steak & Scallops hibachi, plated. Sliced seared steak (medium, pink center) and four golden-seared scallops over fried rice, with the hibachi vegetables: sliced mushrooms, zucchini half-moons, onion petals and bean sprouts. Two small ramekins at the edge of the frame: yum yum sauce (pale pink-orange) and garlic steak sauce (dark brown).
**Composition:** Plate fills about 70% of the frame, set slightly off-center to the lower right so the upper left stays quieter. Ramekins and a folded dark napkin complete the lower left. Nothing else on the table.
**Angle:** 35–40° from above, camera close, 50 mm equivalent.
**Lighting:** One warm key light from the upper left (like the glow of the flat-top), soft fill from the right, visible wisps of steam rising from the rice. Highlights warm amber, shadows deep charcoal.
**Color:** Charcoal matte plate on a black slate or dark wood surface. Warm oranges and browns in the food against the dark ground; no blue props in this shot.
**Placement:** Becomes the large hero image (`.art-main`). The roll photo then moves to the small frame (`.art-small`), so the hero reads hot plate, cold plate.

## 2. Hibachi on the flat-top — `assets/food/hibachi-plate.jpg` (1500 × 1000, 3:2)

**Subject:** Chicken hibachi mid-cook on a steel flat-top: diced chicken with a seared crust, mushrooms, zucchini, onion and bean sprouts being turned with two flat spatulas. A small lick of flame at the far edge of the grill, out of focus. Fried rice in a mound to one side.
**Composition:** Food in the lower two thirds, spatulas entering from the right, grill surface running out of focus to the top. Tight crop, no people's faces, hands and forearms are fine (plain dark sleeves, no logos).
**Angle:** Low, nearly at grill level, 30° above the surface.
**Lighting:** Warm key from the flame side, strong rim light on the steam, dark background. Steam and sizzle visible.
**Color:** Steel grey grill, golden-brown chicken, green zucchini, white sprouts, amber highlights.
**Placement:** The Hibachi row in "Three ways to eat here" (`#exp-hibachi`). Replace the `.exp-placeholder` block with the `<img class="exp-photo">` tag shown in the `PHOTO SLOT` comment.

## 3. Fire & Finn Roll — `assets/food/fire-and-finn-roll.jpg` (1500 × 1000, 3:2)

**Subject:** The chef's signature roll exactly as made: inside, tempura shrimp, cucumber and eel; outside, slices of tuna and avocado layered along the top with tempura flakes; finished with eel sauce and spicy mayo drizzled across. Eight pieces in a line, the tempura shrimp tail standing up at one end.
**Composition:** Roll runs diagonally across the frame on a long rectangular plate, the near end in sharp focus, the far end softening. A small mound of pickled ginger and wasabi at one corner, nothing else.
**Angle:** 20° above the plate, close, so the layers of tuna and avocado read clearly.
**Lighting:** Cool, soft daylight from a window on the left, a touch of warm fill on the sauce so the drizzle shines.
**Color:** Blue-glazed ceramic plate (the site's water blue), deep red tuna, pale green avocado, golden tempura flakes, dark eel sauce. Dark wood or slate table.
**Placement:** The Sushi row (`#exp-sushi`) and the small hero frame. The current file is a generated image inherited from the old site; this shot replaces it with the real roll.

## 4. Poke bowl, built — `assets/food/poke-bowl.jpg` (1500 × 1500, 1:1) plus a 3:2 crop

**Subject:** A build-your-own bowl over sushi rice with cubed raw tuna, and the toppings the menu lists: pineapple, avocado, cucumber, seaweed salad, edamame and masago, arranged in distinct wedges so each is recognizable. Spicy mayo drizzled over the tuna, a small dish of ponzu beside the bowl.
**Composition:** Bowl centered for the square crop; for the 3:2 version shift it to the right third and let the ponzu dish and a pair of plain chopsticks sit on the left.
**Angle:** Straight down (90°) for the square; 45° for the 3:2.
**Lighting:** Bright, cool, even daylight, soft shadows, everything looking just-cut and cold.
**Color:** Black matte bowl, white rice, red tuna, yellow pineapple, green avocado, edamame and seaweed, orange masago. Light grey or pale wood surface.
**Placement:** Square version in the hero's small frame (`.art-small`) until the hibachi hero exists, then the Poke row (`#exp-poke`) uses the 3:2 crop. The existing poke photo is real and stays until this one is shot.

## 5. Spicy Lava Drops — `assets/food/spicy-lava-drops.jpg` (1500 × 1000, 3:2)

**Subject:** The deep-fried roll as served: spicy krab, cream cheese and jalapeño inside a crisp golden tempura shell, cut into pieces and stacked, eel sauce and spicy mayo zig-zagged over the top. Steam or a crackle of the crust visible on the cut face.
**Composition:** Pieces stacked loosely in the center on a dark plate, one piece turned to show the cream-cheese center, sauce pooling slightly.
**Angle:** 30° above, close.
**Lighting:** Warm key light (this is the hot item on the cold side), dark background, crust highlights crisp.
**Color:** Golden crust, white cream cheese, flecks of green jalapeño, dark eel sauce, pale spicy mayo, black plate.
**Placement:** Optional second image for the Sushi row or a future gallery; also the best candidate for social posts.

## 6. The craft — `assets/food/sushi-craft.jpg` (1500 × 1000, 3:2)

**Subject:** Hands rolling sushi on a bamboo mat: nori, sushi rice spread thin, a line of cucumber and tempura shrimp being rolled. A sharp knife and a damp cloth beside the mat.
**Composition:** Mat on the diagonal, hands at the center, the knife and a finished uncut roll at the top edge, out of focus.
**Angle:** 45° above, from the chef's side.
**Lighting:** Cool, soft daylight, the rice glossy and the nori matte.
**Color:** Natural bamboo, white rice, black nori, dark surface. No logos on sleeves or gloves.
**Placement:** Alternate for the Sushi row, or a band image behind "Order ahead" instead of the sushi boat.

---

Priority order if only one or two can be shot: **1, then 2.** The hibachi half of the brand has no photograph anywhere on the site today.
