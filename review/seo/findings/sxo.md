# SXO findings: fireandfinn.com (read 2026-11-18)

**SXO Gap Score: 58/100** (separate from SEO Health Score). Page type 11/15, content depth 8/15, UX 13/15, schema 11/15 (Restaurant, hours, OrderAction, hasMenu present), media 10/15, authority 3/15 (no reviews or third-party mentions under the new name), freshness 2/10 (rename not yet indexed).

## Primary finding
No hard page-type mismatch. For "sushi/hibachi sanibel" the SERP is local intent: map pack plus directories (OpenTable, TripAdvisor, Uber Eats, Wanderlog) plus resort and chamber content. A restaurant homepage with menu, hours, phone and order button is the right type, so mismatch is MEDIUM at worst. The gaps are vocabulary and entity: the page never says "takeout" (0 occurrences in index.html), says "Japanese" only in one menu item and schema, and never mentions outdoor seating. "Sanibel" appears only in title, meta, address and map. Authority is the bigger problem than page type.

## Per-query SERP table (WebSearch result lists, not rendered SERPs)
| Query | Top results mix | Map pack | AIO | Intent | Own site can win? |
|---|---|---|---|---|---|
| sushi sanibel | Shima via Times of the Islands, OpenTable (many country domains), Uber Eats, TripAdvisor, Sundial blog, 2016 WINK news. Old workers.dev Island Panda URL appears | Yes | Moderate | Pick a place; menu, hours | Top 10 plausible once entity is named. Pack is GBP-only |
| hibachi sanibel | Uber Eats category, captivasanibel.com ribbon-cutting (July 2026), WINK 2016, Sundial, OpenTable, resort lists | Yes | Moderate | Sit-down vs takeout | Plausible. Takeout hibachi is not what Shima's pages offer |
| poke bowl sanibel | Wanderlog, Spoondrift guides, HappyCow, off-island noise, old Island Panda URL | Yes | Low-moderate | Nearest poke | Best opening: few strong on-island poke pages |
| takeout sanibel island | Listicles, VCB takeout PDF, atly, Wanderlog, Uber Eats, chamber directory, 2017-2020 guides | Yes | Moderate (list) | Browse a list | Mostly lists plus GBP. Own site only via citations |
| japanese restaurant sanibel | Shima-dominant: Times of the Islands, Sundial blog, OpenTable, Uber Eats, Wanderlog | Yes | Moderate | Sit-down Japanese | Hard. Compete only on the takeout angle |
| island panda sanibel | Ribbon-cutting articles (captivasanibel.com, Santiva Chronicle), TripAdvisor, noise (Panda Island, Ding Darling) | Yes, branded | Low | Navigational, rename doubt | /island-panda/ can win if indexed |
| fire and finn sanibel | Nothing relevant (fire-district and prescribed-burn pages) | Only once GBP indexed | None | Navigational | Brand not indexed yet; own site should take it on crawl |
| sanibel restaurants open now / lunch | OpenTable features, TripAdvisor lunch list, 2023-24 "now open" lists, post-hurricane guides | Yes ("open now" is GBP-driven) | Moderate | Immediate, hours-driven | GBP wins; site contributes only structured hours |

Own site can win: branded queries, poke and takeout-hibachi long tail, the rename query. GBP-only: map pack, "open now", near-me and review-based results. Directories and lists are won by presence on those platforms (TripAdvisor, OpenTable, Uber Eats, chamber directory), not by on-site work.

## Mismatch and gaps vs "sushi/hibachi sanibel"
- Menu, hours, phone and order are in the hero and status line, which also carries address and "Formerly Island Panda". Good.
- Missing: "takeout", "Japanese", "Sanibel Island" in body text, "outdoor seating only". Searchers weighing Shima (reservations; Tue-Sat dinner per listings) get no stated contrast: daily 11am-8pm, order and pick up.
- Third-party snippets still show the old name and stale hours, so the homepage must state current facts plainly.

## Personas (0-10)
| Persona | Score | Why |
|---|---|---|
| Tourist on phone at beach | 7 | Call/Order, hours, address in hero. Lacks "takeout", "outdoor seating only" |
| Seasonal regular, "did Island Panda close?" | 7 | "Formerly Island Panda" in the status line links to the explainer. Needs a plain same-address line |
| Local family, hibachi for kids | 6 | #kids anchor exists, but the first screen never signals kids' options |
| Visitor comparing with Shima | 5 | No stated differentiator: takeout, daily hours, outdoor seating are all unsaid |
First 10 seconds for all: name plus rename, "takeout", hours, tap to call, a path to the menu.

## Category pages verdict: not now
/hibachi/, /sushi/, /poke/ would be thin duplicates. The menu must stay byte-identical and there is no build step, so each page would copy the same dishes, tripling maintenance and drift risk. They are justified only if they hold distinct information the owner supplies (for example how hibachi is boxed for pickup). Instead keep the #hibachi/#rolls/#poke anchors, use query words in section headings where the design allows, and keep schema (hasMenu, servesCuisine) accurate.
Trigger to build (Search Console, 90 days, after the new name is indexed): "hibachi sanibel" or "poke sanibel" gets 150+ impressions per month with the homepage averaging below position 8, or three or more hibachi/poke queries each exceed 50 impressions at under 2% CTR. These thresholds are my suggestions; I had no volume data. Below them, a page costs more than it returns.

## Three on-page changes
1. Hero lead (placement: `<p class="lead">`). Replace with: "Takeout hibachi, sushi rolls and build-your-own poke on Sanibel Island." H1 untouched.
2. Status line (placement: first line of `.status`, after the hours). Add: "Takeout, outdoor seating only." Both facts come from the owner brief.
3. Visit lead (placement: `.visit-lead`). Replace "In Tahitian Gardens on Periwinkle Way, the main road through Sanibel." with "Takeout at 2003 Periwinkle Way in Tahitian Gardens, Sanibel Island. Formerly Island Panda, same address, renamed November 2026." Owner to confirm "same address" wording. Mirror this in the GBP description, since GBP drives the pack.

Highest value: change 1 plus the GBP update.

## Limitations
- WebSearch returns result lists, not rendered Google SERPs. I did not see the map pack or its ranking, AI Overviews, PAA, or personalized and local-device results.
- Positions are inferred from result order. No Search Console data, so thresholds are estimates.
- "fire and finn sanibel" returned nothing relevant: the brand may be unindexed or the tool may lag.
- Tool summaries cited old Island Panda hours (Fri/Sat only), probably stale third-party data.
- The page was read from the repo checkout (index.html), not fetched live through the renderer.
