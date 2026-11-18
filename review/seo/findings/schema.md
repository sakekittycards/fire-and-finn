# Schema / structured data findings: fireandfinn.com

Audited 2026-11-18. Rendered capture: the rendered page (captured with the skill renderer) (2 blocks on the rendered homepage, both valid JSON; the Menu block exists only after JS runs).

**Schema score: 71 / 100.** Solid base (valid Restaurant, address, hours, rendered Menu). Points lost for: no @id or entity linking, a second unlinked Restaurant node on the bridge page, no geo/hasMap/sameAs, no WebSite node (no site-name signal), `image` is a composite graphic, and a JS-only Menu block that is not linked to the Restaurant.

## 1. Validation table

| # | Block | Property | Severity | Issue / why | Fix |
|---|---|---|---|---|---|
| 1 | Home Restaurant | @id | Warn | No @id, so the bridge page's Restaurant cannot be recognised as the same entity. | Add `https://fireandfinn.com/#restaurant`. |
| 2 | Home Restaurant | geo | Warn | Recommended for LocalBusiness. Missing. | Add GeoCoordinates (coordinate note below). |
| 3 | Home Restaurant | hasMap | Info | Missing. | Google Maps URLs link built from the address (no invented IDs). |
| 4 | Home Restaurant | sameAs | Warn | Missing. Ties the new name to the DoorDash listing and any profiles the owner adds. | Add array. |
| 5 | Home Restaurant | acceptsReservations | Info | Documented for Restaurant; missing. | `false` (boolean, not the string "False"). |
| 6 | Home Restaurant | image | Warn | `og.jpg?v=2` is a 1200x630 designed share card (logo plus text), not a photo of the restaurant. Google prefers representative photos in several aspect ratios. | ImageObject with width/height now; ideally add real food or storefront photos (1:1, 4:3, 16:9). |
| 7 | Home Restaurant | alternateName[2] | Info | "Fire & Finn Hibachi · Sushi · Poke" is a tagline, not a name; mildly noisy for entity matching. Kept per brief. | Consider dropping. |
| 8 | Home Restaurant | menu / hasMenu | Info | Both are valid (Text, URL or Menu). Google ignores URL fragments, so `#menu` resolves to the homepage. A PDF URL in `menu` is legitimate, just not machine-readable. | Keep both as they are. |
| 9 | Home Restaurant | potentialAction OrderAction | Info | Structurally correct: OrderAction > EntryPoint with `urlTemplate`, `actionPlatform`, and `deliveryMethod` = `http://purl.org/goodrelations/v1#DeliveryModePickUp` (valid enum). Google's food-ordering feature is partner/feed-based, so expect no SERP effect. | Keep; harmless. |
| 10 | Home Restaurant | openingHoursSpecification | Pass | 7 days, 11:00-20:00, valid. | Add `specialOpeningHoursSpecification` only for closures or holiday hours. |
| 11 | Home Restaurant | priceRange | Pass | "$$" accepted. | Keep (printed prices run $8-$35 if a concrete range is wanted). |
| 12 | Home | WebSite | Warn | None. Google site names need WebSite markup on the homepage with `name`, optional `alternateName`, `url`. | Add. |
| 13 | Home Menu (JS) | whole block | Warn | Built at runtime by app.js; no @id; not referenced from the Restaurant; invisible to non-rendering consumers. | See section 4. |
| 14 | Bridge WebPage | about (Restaurant) | Error | Duplicate Restaurant with no @id and fewer properties than the homepage one: two competing descriptions of one entity. | Share the @id (section 3). |
| 15 | Bridge WebPage | isPartOf WebSite | Warn | Anonymous WebSite node, no @id. | Add `#website` @id. |
| 16 | Bridge WebPage | primaryImageOfPage | Info | Plain URL accepted; ImageObject preferred. | Optional. |
| 17 | Both | @context, URLs, phone | Pass | `https://schema.org`; absolute URLs; international phone format. | None. |

Sources: https://developers.google.com/search/docs/appearance/structured-data/local-business ; https://schema.org/Restaurant ; https://schema.org/Menu ; https://developers.google.com/search/docs/appearance/site-names ; https://developers.google.com/search/docs/appearance/structured-data/breadcrumb

**Coordinate note.** The brief gave longitude -82.0653259. Nominatim (OpenStreetMap, way 11016070, type=house) returns lat 26.4396719, lon **-82.0653299**. That is a one-digit difference (about 0.4 m); I used -82.0653299. Only one source was reachable, so the owner should drop a pin check in Google Maps.

## 2. Revised homepage JSON-LD (replaces the existing block in `<head>`)

All existing values are kept. TripAdvisor, Yelp, Facebook, Instagram and Apple Maps are NOT in the JSON: placeholder text in live schema counts as an error and would break the "valid and real" rule. Add them to `sameAs` only once real URLs exist (list after the block). The Toast link stays out of `sameAs` because it is an order endpoint, not a profile. The Google Business Profile location id cannot be turned into a Maps place URL without the CID, so none was guessed.

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Restaurant",
      "@id": "https://fireandfinn.com/#restaurant",
      "name": "Fire & Finn",
      "alternateName": ["Island Panda", "Fire & Finn Hibachi · Sushi · Poke"],
      "url": "https://fireandfinn.com/",
      "image": {
        "@type": "ImageObject",
        "url": "https://fireandfinn.com/assets/og.jpg?v=2",
        "width": 1200,
        "height": 630
      },
      "logo": {
        "@type": "ImageObject",
        "url": "https://fireandfinn.com/assets/logo.png",
        "width": 2000,
        "height": 931
      },
      "telephone": "+1-239-579-0783",
      "servesCuisine": ["Japanese", "Hibachi", "Sushi", "Poke"],
      "priceRange": "$$",
      "acceptsReservations": false,
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "2003 Periwinkle Way",
        "addressLocality": "Sanibel",
        "addressRegion": "FL",
        "postalCode": "33957",
        "addressCountry": "US"
      },
      "geo": {
        "@type": "GeoCoordinates",
        "latitude": 26.4396719,
        "longitude": -82.0653299
      },
      "hasMap": "https://www.google.com/maps/search/?api=1&query=2003+Periwinkle+Way+Sanibel+FL+33957",
      "openingHoursSpecification": [
        {
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
          "opens": "11:00",
          "closes": "20:00"
        }
      ],
      "hasMenu": "https://fireandfinn.com/#menu",
      "menu": "https://fireandfinn.com/menu.pdf",
      "sameAs": [
        "https://www.doordash.com/store/island-panda-sanibel-45540707/"
      ],
      "potentialAction": {
        "@type": "OrderAction",
        "target": {
          "@type": "EntryPoint",
          "urlTemplate": "https://order.toasttab.com/online/fire-and-finn-2003-periwinkle-way",
          "actionPlatform": [
            "http://schema.org/DesktopWebPlatform",
            "http://schema.org/MobileWebPlatform"
          ]
        },
        "deliveryMethod": "http://purl.org/goodrelations/v1#DeliveryModePickUp"
      }
    },
    {
      "@type": "WebSite",
      "@id": "https://fireandfinn.com/#website",
      "name": "Fire & Finn",
      "alternateName": "Fire and Finn",
      "url": "https://fireandfinn.com/",
      "publisher": { "@id": "https://fireandfinn.com/#restaurant" }
    }
  ]
}
```

Optional `sameAs` additions, only with verified URLs: TripAdvisor, Yelp, Facebook, Instagram, Apple Maps place, Google Maps place URL. The DoorDash URL carries the old name; it is still a true listing of this business and helps the rename.

## 3. Bridge page (`/island-panda/`)

Google reads each page on its own, so a bare `{"@id": ...}` pointing at another page resolves to nothing. The safe pattern is a minimal stub that shares the homepage `@id`: merge-friendly, no conflicting facts. Hours, hasMenu and the duplicated address are dropped from the stub because they live on the canonical node.

BreadcrumbList helps only a little (a Home > page trail in results) but is valid and nearly free, so include it. Do NOT add an OrderAction or other potentialAction here; the action belongs to the Restaurant entity once, on the homepage.

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://fireandfinn.com/island-panda/#webpage",
      "name": "Island Panda is now Fire & Finn",
      "url": "https://fireandfinn.com/island-panda/",
      "description": "Island Panda is now Fire & Finn. Same kitchen, same address, new name: hibachi, specialty rolls and build-your-own poke at 2003 Periwinkle Way, Sanibel, FL.",
      "isPartOf": {
        "@type": "WebSite",
        "@id": "https://fireandfinn.com/#website",
        "name": "Fire & Finn",
        "url": "https://fireandfinn.com/"
      },
      "primaryImageOfPage": {
        "@type": "ImageObject",
        "url": "https://fireandfinn.com/assets/og.jpg?v=2",
        "width": 1200,
        "height": 630
      },
      "breadcrumb": { "@id": "https://fireandfinn.com/island-panda/#breadcrumb" },
      "about": {
        "@type": "Restaurant",
        "@id": "https://fireandfinn.com/#restaurant",
        "name": "Fire & Finn",
        "alternateName": "Island Panda",
        "url": "https://fireandfinn.com/"
      }
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://fireandfinn.com/island-panda/#breadcrumb",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Fire & Finn", "item": "https://fireandfinn.com/" },
        { "@type": "ListItem", "position": 2, "name": "Island Panda is now Fire & Finn" }
      ]
    }
  ]
}
```

## 4. Menu JSON-LD (runtime-built, app.js around lines 166-199)

The rendered block is structurally valid: Menu > 6 MenuSection (Appetizers 6 items, Hibachi 9, Kids 3, Chef's Specialty Rolls 10, Classic Rolls 8, Poke Bowl 1), each MenuItem with an Offer in USD. Encoding is clean (the mojibake I saw once was my console). Google has no Menu rich result, so this helps entity understanding and AI crawlers, not a SERP feature.

Issues:
- **Names not byte-for-byte.** app.js synthesises "Hibachi: Steak", "Hibachi combo: Steak & Scallops" and "Poke Bowl, build your own". These strings are not printed on the menu. Given the no-alteration rule, this is the main concern.
- **Kids.** The price "15" is hardcoded in app.js for the `#kids` group, not read from the page, so it will silently drift if the printed price changes. Item names "Hibachi" and "Poke Bowl" duplicate the adult names with no qualifier (the section name carries the context).
- **Poke.** One $19 item whose description concatenates the three steps. Acceptable and honest; no per-ingredient offers, which is correct (do not invent upcharges).
- **Descriptions.** Lines are joined by a single space, giving run-ons like "cucumber & eel Outside: tuna". Use "; " as the joiner (markup only; printed text unchanged).
- **Asterisks.** Stripped from names but left in descriptions ("Tuna*"), so the marker is handled inconsistently.
- **Linking.** No @id and no tie to the Restaurant; `url` is only an anchor.

**Recommendation: a small generator script the owner runs after each menu edit, writing a static JSON-LD block into index.html between marker comments** (with a `--check` mode that fails when the block is stale). Trade-offs:
- Keep dynamic: zero upkeep, always matches the page, and Googlebot renders JS. Cost: invisible to non-rendering crawlers, plus the hidden hardcoded kids price and synthesised names.
- Hand-inlined static copy: crawlable, but it will drift the first time a price is edited. Worse than today.
- Generator: static output and no drift if the owner remembers to run it; costs one manual step on a site with no build.
Since there is no SERP payoff, keeping it dynamic and fixing the joiner, kids-price source and `@id` is a defensible low-effort alternative. Choose the generator only if non-Google and AI visibility matter to the owner.

## 5. Other schema: useful, ignored, harmful

- Useful: WebSite node (site name), geo, hasMap, sameAs, bridge BreadcrumbList, extra `image` aspect ratios from real photos, `specialOpeningHoursSpecification` for closures.
- Ignored but harmless: OrderAction (no Google surface here), Menu, priceRange, hasMap.
- Harmful or off-limits: FAQPage (no SERP feature since May 2026), HowTo, aggregateRating or Review nodes (no verified reviews; self-serving review markup breaches Google's policy), a second Restaurant with different data, placeholder `sameAs` URLs, and any facts not supplied (payment methods, founding date, amenities).

## Limitations
- Live site fetched once and rendered with Playwright. I did not run Google's Rich Results Test or Schema Markup Validator (no submission permitted), so Google-side acceptance is judged from documentation.
- Read index.html, island-panda/index.html and app.js from the worktree; the live homepage matched on every point checked.
- Coordinates verified against Nominatim only.
- Menu prices were not compared with menu.pdf.
- Only og.jpg (1200x630) and logo.png (2000x931) dimensions were checked, via `file`.
- OrderAction assessed from documentation; Google's ordering integration is a partner program and was not verified for this business.
