# fireandfinn.com SEO — action plan

18 November 2026, revised after board convening 8. Two lists: what the site does (done in this branch, waiting on a push) and
what needs the owner, which after the board is three sign-ins rather than twelve chores. Each item says how we would know it
failed. Nothing here is a claim on the site; it is plumbing and listings.

## Site (this branch; pushed on the owner's word)

| # | Change | Fails if |
|---|---|---|
| S1 | Schema graph: @id, geo from Google's pin, map link, sameAs (Maps, TripAdvisor, Yelp, Apple Maps, DoorDash), WebSite node; bridge page linked by @id with a breadcrumb | Google's Rich Results Test shows an error on either page |
| S2 | Visit paragraph in the site's own lines (what and where; "Formerly Island Panda: same kitchen, same address, new name"); the duplicate footnote under the address removed | A Google snippet or AI answer for "what is Fire & Finn" still has nothing to quote a month after indexing |
| S3 | Bridge page: "Sanibel Island" in the title and lead; one descriptor ("takeout hibachi, specialty rolls and build-your-own poke bowls") across the meta description, schema and llms.txt | The bridge page does not rank for "island panda sanibel" once indexed |
| S4 | Menu JSON-LD uses printed names; kids price read from the page | A rendered copy of the Menu block shows a string that is not on the printed menu |
| S5 | Favicons at 96 px, og:locale, sitemap lastmod, robots `/review/`, llms.txt, IndexNow key, `.playwright-mcp/` ignored | The sitemap fails to parse in Search Console |

After the push, from the site session:

```bash
"$HOME/.claude/skills/seo/bin/claude-seo" run indexnow_submit.py --host fireandfinn.com --key 4c84c2dba7209a240503fec65a579b43 --key-location https://fireandfinn.com/4c84c2dba7209a240503fec65a579b43.txt --urls https://fireandfinn.com/ https://fireandfinn.com/island-panda/
```

and re-run PageSpeed when the API quota allows.

## Three asks of the owner

The sessions already run these accounts once he is signed in (the 7 November Business Profile edits and the 8 November
DoorDash edits went that way); he says "Publish it". So the asks are sign-ins, not walkthroughs.

| # | Ask | What the session then does | Fails if |
|---|---|---|---|
| A1 | **Sign in to Google in Chrome** (the Business Profile login) | Search Console: add `https://fireandfinn.com/` as a URL-prefix property and verify with the HTML-tag method (the tag goes in the site head; a Domain property would need a TXT record at GoDaddy instead, and the HTML methods do not work for Domain properties). Submit the sitemap. URL inspection → Request indexing for `/` and `/island-panda/`. Business Profile: remove the six mainland cities from the service area unless the kitchen delivers there; make "No dine-in" and the breezeway sentence agree (his call which way). **No category change**: the primary stays "Sushi takeaway" until Search Console has a baseline to measure against; the kitchen is "a take out restaurant at the moment" (owner, 8 Nov) and the map panel already reads "Sushi takeaway · Takeout" | `site:fireandfinn.com` still empty 7 days after the request; the profile still contradicts itself a week later |
| A2 | **Sign in to Cloudflare** (island-panda.com's DNS lives there) | DNS: proxy on (orange cloud) for the `@` A records and the `www` CNAME; SSL/TLS Full; Rules → Redirect Rules: hostname contains `island-panda.com` → 301 to `https://fireandfinn.com/island-panda/`, with a rule above it for paths containing `menu` → `https://fireandfinn.com/#menu`. Then remove `noindex` from the old page in the island-panda repo. Google documents an instant meta refresh as permanent already; the 301 is cleaner and is what Change of Address checks | `curl -I https://island-panda.com/` is not `301` with `Location: https://fireandfinn.com/island-panda/` |
| A3 | **Open "Get more reviews" in the Business Profile once** and paste the short link to the site session | The link goes in the Toast receipt footer only (the receipt goes home with the order). Nobody at the counter asks, nobody is filtered, no QR code, nothing on Yelp. Reply to every review within two days | A gap of more than 18 days with no new Google review is the specialist's threshold; treat it as a hint, not a rule |

## Session work once the sign-ins exist (in this order; no new asks)

| # | Do | Fails if |
|---|---|---|
| W1 | Bing Webmaster Tools: import from Search Console, confirm the sitemap | Bing `site:` still empty after two weeks |
| W2 | Change of Address in Search Console (needs A2 and a Domain property for island-panda.com, verified by TXT at Cloudflare). Google's tool wants the old homepage to 301 to the new homepage; ours lands on the bridge page by the owner's 8 November choice. If the pre-move check rejects that, skip the tool, keep the 301 for at least 180 days, and let the canonical and the bridge page carry the move | The tool rejects the redirect and nobody records it |
| W3 | Apple Business Connect: claim "Island Panda, 2003 Periwinkle Way", rename, website, hours | Apple Maps still says Island Panda after two weeks |
| W4 | Bing Places: import or claim, rename, website | Bing shows Island Panda after two weeks |
| W5 | Yelp: claim the unclaimed page, rename (Yelp may ask for proof: a signage photo or a receipt), fix the hours to daily 11 to 8, website | Old name or old hours after 30 days |
| W6 | TripAdvisor: Owner Center, claim listing d34381739, request the name change with the same proof, website | Old name after 30 days |
| W7 | DoorDash and Uber Eats: DoorDash support ticket for the consumer-facing name (portal already says Fire and Finn); Uber Eats name field is locked, so Help in Manager or merchants@uber.com from the admin email, which is the family's | Titles still read Island Panda a week after the ticket |
| W8 | Chamber and local press: the note below to the Sanibel-Captiva Chamber (its listing links to island-panda.com) and to the two outlets that ran the June ribbon-cutting (Island Reporter / captivasanibel.com, Santiva Chronicle), sent by the owner | No listing or story updated in 30 days |
| W9 | Real photos on the Business Profile and the delivery apps: a phone, in daylight, the actual dishes. The website photos are stand-ins and must not be uploaded as real | Profile still has no photo of the real food |
| W10 | Monthly AI check: ask ChatGPT, Perplexity, Copilot and Google AI Mode "What is Fire & Finn on Sanibel?", "What happened to Island Panda?", "Is Island Panda still open?", "Hibachi takeout on Sanibel?", "Poke bowl on Sanibel?"; note which source each cites and fix that listing | An assistant still says "closed" or gives the old hours |
| W11 | Category test, only once Search Console has four weeks of data: switch the primary to "Sushi restaurant" for three weeks and read the map-pack position for "sushi sanibel" before and after; revert if it drops | Changed without a baseline |
| S6 | /hibachi/, /sushi/ and /poke/ pages: only if Search Console shows 150+ monthly impressions for "hibachi sanibel" or "poke sanibel" with the homepage below position 8, and only with content that is not a copy of the menu | Pages built without that data are thin duplicates |

## Dependencies
A2 before W2. A1 before anything is measured. S1 to S5 are one push. W11 waits for a baseline.

## Leading indicators (Search Console, once A1 is done)
- Impressions and position for `fire and finn sanibel` and `island panda sanibel`; the bridge page should take the second.
- Impressions for `sushi sanibel`, `hibachi sanibel`, `poke sanibel` and the homepage's average position.
- Knowledge panel: review count stays at or above 74 (a drop would mean Google treated the rename as a new business).

## Note for the chamber and the papers (owner sends and dates it; edit freely)
Hello, Island Panda at 2003 Periwinkle Way in Tahitian Gardens is now Fire & Finn. The kitchen, the address, the phone
(239) 579-0783 and the hours (daily, 11am to 8pm) are the same, and we still serve hibachi, specialty rolls and
build-your-own poke bowls for takeout. Nine rolls have new names. Could you update our listing or story to Fire & Finn
(formerly Island Panda) and link to fireandfinn.com? The details are at fireandfinn.com/island-panda/. Thank you.
