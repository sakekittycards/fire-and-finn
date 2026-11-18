# fireandfinn.com SEO audit — report

Branch `claude/fire-finn-seo-optimization-8b9480`, 18 November 2026. Nothing pushed, nothing deployed.
Measured against the live site (main at 5abb4d4) with the claude-seo toolkit and curl, with Google and Bing searched by hand
in a browser, and with five specialist passes (technical, local, schema, AI search, search intent) whose full findings are in
`findings/`. `ACTION-PLAN.md` beside this file says what the site does (this branch) and what the owner does (accounts we do not hold).

## The one finding

**Google has no page of fireandfinn.com in its index.** `site:fireandfinn.com` returned "did not match any documents" on
18 November; Bing shows nothing either. The site has been live since 22 October. At the same time `site:island-panda.com`
still returns the two old Island Panda pages with their old titles and snippets ("Sashimi-grade fish, tropical poke bowls...")
and the old preview host, island-panda.baussmgmt.workers.dev, still ranks for "sushi Sanibel" and "hibachi Sanibel" with the
old content, even though it now answers with a 301.

Until the new site is indexed nothing else in this report matters, and the fastest fix is not on the site: verify
fireandfinn.com in Google Search Console, submit the sitemap and request indexing of the two pages. That needs the owner's
Google login. Everything the site itself can do to help is in this branch.

The Google Business Profile is the good news. It is renamed "Fire and Finn", verified, shows 4.6 stars from 74 reviews, links
the website and the menu at fireandfinn.com and carries a live "Order pickup" button. For a takeout restaurant the map pack is
where most customers arrive, and that part already works.

## SEO Health Score: 67/100

Weights are the claude-seo standard. Local SEO is scored separately below because it is the lever that matters for a restaurant.

| Category | Weight | Score | In a line |
|---|---|---|---|
| Technical | 22% | 70 | On-site basics clean (canonicals, sitemap, 404, https, www); no Search Console; the old domain is a refresh page, not a 301 |
| Content | 23% | 60 | The whole menu is on the page; no plain-prose paragraph said what the place is, where it is, and that it was Island Panda |
| On-page | 20% | 65 | Title and description are right; "takeout", "Sanibel Island" and "Japanese" barely appeared in body text |
| Schema | 10% | 71 | Valid Restaurant block; no @id, geo, map link, sameAs or WebSite node; the bridge page duplicated the entity |
| Performance | 10% | 75, unmeasured | PageSpeed's API was rate-limited and a local Lighthouse run was blocked; judged from source (preloads, srcset, passive scroll, dimensions on every image) |
| AI search readiness | 10% | 58 | Every crawler allowed, no snippet limits; nothing citable in prose; every third party still says Island Panda |
| Images | 5% | 85 | Alt text, width and height, srcset and lazy loading on every photo |

**Local SEO: 55/100** (seo-local method: GBP 14/25, reviews 15/20, local on-page 11/20, citations 5/15, schema 6/10, local
links 4/10). The specialist scored reviews 9/20 on an old self-reported figure of 20; the live knowledge panel shows 74 reviews
at 4.6, so that line is corrected here. Citations and links are the hole: every third-party listing and both July news
stories still carry the old name.

## What was found, by category

### Indexing and the old name (Critical)
- Google: 0 pages of fireandfinn.com; 2 pages of island-panda.com (old content). Bing: 0 pages of fireandfinn.com.
- island-panda.com is served by GitHub Pages (its DNS is at Cloudflare but the records point at GitHub and are not proxied), so
  the `_redirects` file in that repo does nothing there. The page is a 200 with a 0-second meta refresh, `noindex` and a
  canonical to /island-panda/. Google documents an instant meta refresh as a permanent redirect, so it is not wrong, but Search
  Console's Change of Address needs a real 301 from the old homepage, and the `noindex` on a page that is meant to consolidate
  works against the canonical. The old workers.dev host does send a 301 (Cloudflare honours the `_redirects` file there).
- No Search Console or Bing Webmaster Tools property exists for either domain, as far as anything on the site or in the project
  record shows.

### Technical (score 70; `findings/technical.md`)
- Redirect chains: none longer than 2 hops; http, www and the bare /island-panda path all resolve in one hop. Canonicals are
  self-referential on both pages.
- `/menu-source/` is disallowed in robots.txt but publicly served (7 MB, including the print-menu HTML). Harmless, but robots
  does not hide it; it only stops crawling.
- The Menu JSON-LD exists only after JavaScript runs. Googlebot renders it; AI crawlers do not, but they read the same menu as
  plain HTML, which is the stronger signal. Kept dynamic (the menu is hand-edited and a stale static copy would be worse than none).
- Favicons were 32 and 128 px; Google asks for a multiple of 48. The bridge page had no apple-touch-icon.
- Sitemap carried `changefreq` and `priority`, which Google ignores.

### Content and on-page (scores 60 and 65; `findings/sxo.md`, `findings/geo.md`)
- The page type is right for "sushi sanibel" and "hibachi sanibel": a restaurant homepage with menu, prices, hours, phone and
  an order button is what the intent wants. The gap is vocabulary. "takeout" appeared 0 times; "Sanibel" only in the title,
  description, address and map; "Japanese" once in a menu item.
- No sentence anywhere said, in prose, what Fire & Finn is and that it was Island Panda. "Formerly Island Panda" lived in a
  status line, a Visit footnote and the metadata. An AI answer or a Google snippet had nothing to lift.
- The bridge page answered "what happened" in fragments ("Same kitchen. Same address. New name.") with no month and no
  "Sanibel" in the title.
- Separate /hibachi/, /sushi/ and /poke/ pages: not now. With the menu byte-for-byte the printed one and no build step they would
  be thin duplicates. The trigger to revisit is in the action plan.

### Schema (score 71; `findings/schema.md`)
- Restaurant block valid, with address, hours, phone, cuisine, price range, OrderAction. Missing: @id, geo, hasMap, sameAs,
  acceptsReservations, a WebSite node (Google's site-name signal). The bridge page carried a second, unlinked Restaurant.
- The runtime Menu block invented names the printed menu does not use ("Hibachi: Steak", "Poke Bowl, build your own"),
  hard-coded the kids price, and joined description lines with spaces.

### Local (score 55; `findings/local.md`)
- Primary GBP category is "Sushi takeaway". The specialist recommends "Sushi restaurant" with Japanese restaurant, Poke bar
  and Takeout restaurant as secondaries, and only adds a hibachi category if one exists in Google's list that fits a kitchen
  grill rather than a tableside one. Category names could not be fetched from Google and must be confirmed in the dashboard.
- GBP contradictions: "No dine-in" beside a description that mentions breezeway seating; a service area of six mainland
  cities left over from delivery apps.
- Citations still under the old name: Apple Maps (hours right, name wrong), Yelp (unclaimed; hours wrong: 11 to 7 four days a
  week), TripAdvisor (3.4 from 5 reviews), DoorDash public page (portal renamed on 8 November, public title and h1 still Island
  Panda on 18 November), Uber Eats / Postmates, the Sanibel-Captiva Chamber member listing (links to island-panda.com), the
  two ribbon-cutting stories, Sanibel Sea School's recommendations.
- Google's own guideline warns that a rename that changes the proper nouns can be "treated as new"; the profile is verified
  and intact, but proof of the rename (signage photo, a Toast receipt, the fictitious-name filing) is worth keeping on file.

### AI search (score 58; `findings/geo.md`)
- robots.txt allows every agent, there are no snippet limits, the pages are static. Technically open.
- What ChatGPT, Copilot and Perplexity would say today is inferred, not observed: they lean on Bing, Yelp, TripAdvisor and local
  news, all of which still say Island Panda. The fix is the citation work above plus a citable passage on the site.
- `llms.txt` was added because it costs ten lines; Google ignores it and no major engine is confirmed to use it.

## What this branch changes on the site

1. **Restaurant schema** rebuilt as a graph: `@id`, `geo` from Google's own pin (26.4385265, -82.0666332), `hasMap` and
   `sameAs` using the real Maps listing (CID 258235692591613504, checked: it opens "Fire and Finn"), plus the TripAdvisor,
   Yelp, Apple Maps and DoorDash listings of this business, `acceptsReservations: false`, `image` and `logo` as ImageObjects
   with dimensions, a one-line description, "Fire and Finn" as an alternate name, and a `WebSite` node so Google can read the
   site name. The tagline was dropped from `alternateName`; it is not a name.
2. **Bridge page schema** now points at the homepage Restaurant by `@id` instead of duplicating it, and carries a breadcrumb.
3. **A short factual paragraph in Visit** (two sentences, quiet type, after the buttons) in the site's own lines: what Fire & Finn
   is and where, then "Formerly Island Panda: same kitchen, same address, new name" linking to the bridge page. The "Formerly Island
   Panda" footnote under the address went, so the old name is still said twice on the page, now once in a sentence a person or a
   search engine can use. The hero line, the lead and the menu are untouched. (Board, convening 8: the first draft was 62 words
   with the phone and "November 2026"; it restated the screen above it in a second register, and nobody has dated the rename
   in the owner's words, so both went.)
4. **Bridge page**: title gains "— Sanibel Island, FL"; the lead names Sanibel Island. The meta description says "Takeout"
   where it said "Fast-casual", so the site, the schema and llms.txt share one descriptor (board, convening 8).
5. **Menu JSON-LD** (app.js): names are the printed ones ("Steak", "Steak & Scallops", "Build your own bowl over sushi rice"),
   the kids price is read from the "15 each" heading instead of being hard-coded, asterisks are stripped everywhere, description
   lines join with "; ", the block has an `@id`.
6. **Housekeeping**: `og:locale`; a 96 px favicon on both pages and an apple-touch-icon on the bridge; sitemap without
   `changefreq`/`priority` and with today's `lastmod`; `/review/` disallowed in robots.txt (screenshots and reports are not
   content); `llms.txt`; an IndexNow key file at the root so Bing and friends can be pinged after a push; cache-bust v14.

Not changed, on purpose: the hero entrance (1.2 s image settle). The technical pass flagged it as delaying LCP by about 1.2 s;
the board's engineer measured it (twelve Playwright loads, fast and throttled): Chrome ignores opacity-0 paints for LCP, so the
fade costs nothing, and on slow 4G the larger lever is the 302 KB hero file a 3x phone chooses. That finding in
`findings/technical.md` is wrong on this point and is left as the specialist's record.

## Synthesis

- **Perceive.** Everything above was collected before scoring. The surprise was the index: a four-week-old site with a verified
  Business Profile linking to it and zero Google pages. The assumption "Google will find it from the profile" did not hold.
- **Analyze.** The highest-leverage constraint is indexing; it gates every on-page and AI gain. The second is the old name on
  every third-party surface; that is what AI assistants and directories read. On-page work is third, and the site needed only
  vocabulary and one paragraph, not a rewrite.
- **Validate.** Human cost checked: the paragraph is 62 quiet words at the bottom of Visit, the brand line and menu are
  untouched, no claims were added (every sentence traces to a fact already published on the site, the profile or the news).
  The owner's capacity: the off-site list is long, so the action plan ranks it and marks the first three as the ones that
  matter this week. Falsifiability: every action in the plan has a "how we would know this failed" line.
- **Act.** The site changes are in this branch; the owner's checklist is in the action plan; the leading indicators to watch are
  Search Console impressions for the two pages and the brand query, and the map-pack position for "sushi sanibel".

## What could not be measured
- Core Web Vitals: PageSpeed's keyless API was rate-limited for the whole session and a local Lighthouse run was blocked by the
  session's permission settings. The page was judged from source; re-run `/seo google pagespeed https://fireandfinn.com/`.
- Search Console and Bing data: no property exists yet.
- Map-pack rank, review velocity and GBP Insights: no login and no DataForSEO.
- Assistant answers (ChatGPT, Perplexity, Copilot): inferred from their sources, not queried.
- Google's current category list: not fetchable; names must be confirmed in the Business Profile editor.

## What the next audit should look for
Run it two weeks after the owner's Search Console and redirect steps are done. Check, in this order: `site:fireandfinn.com`
shows both pages; `site:island-panda.com` shows nothing or the bridge page; the knowledge panel still reads "Fire and Finn"
with the review count intact; Apple Maps, Yelp, TripAdvisor and DoorDash show the new name; Search Console reports impressions
for "island panda sanibel" landing on /island-panda/. If "hibachi sanibel" or "poke sanibel" reach 150 impressions a month with
the homepage below position 8, reopen the category-page question with real numbers.
