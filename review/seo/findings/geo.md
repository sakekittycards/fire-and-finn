# GEO / AI Search Readiness - fireandfinn.com (2026-11-18)

**AI Search Readiness: 58/100.** Citability 50, structure 70, multi-modal 55, authority/brand 35, technical 85 (weighted).
Technical access is good. The gap is that no plain-prose passage defines the business, and almost every third-party source still says "Island Panda".

## Verified facts
- robots.txt (live): `User-agent: *` / `Allow: /` / `Disallow: /menu-source/` / Sitemap. No AI bot is blocked: GPTBot, OAI-SearchBot, ClaudeBot, PerplexityBot, CCBot and Google-Extended all fall under `*`.
- No `nosnippet`, `max-snippet` or meta robots on either page (only 404.html has noindex). Static HTML, so no client-side rendering risk.
- Homepage has Restaurant JSON-LD with address, hours and OrderAction. Title and description include "Formerly Island Panda". The bridge page is titled "Island Panda is now Fire & Finn" and has its own JSON-LD.
- Old workers.dev host returns 301 to https://fireandfinn.com/ (checked with curl today). Engines drop the old copy only after recrawl.
- No llms.txt. Sitemap lists 3 URLs, lastmod 2026-11-08.

## Findings
| Severity | Finding | Evidence | Fix |
|---|---|---|---|
| High | No plain-prose passage says what the restaurant is, where, and that it was Island Panda. Homepage prose is fragments ("One kitchen, two temperatures..."). | Homepage text; "formerly" appears only in meta tags and JSON-LD | Add the draft passage below to the Visit section |
| High | Third-party mentions all use the old name, so engines that lean on the chamber, TripAdvisor, delivery apps and news will answer with "Island Panda" and old facts | Chamber listing, captivasanibel.com, santivachronicle.com, TripAdvisor, Postmates/Uber Eats | Mention plan below |
| High | Old workers.dev page was indexed with old content and ranked for "sushi Sanibel". Now a 301, but cached copies persist. | `curl -I` shows 301 to fireandfinn.com | Keep the 301. Submit the new URLs in Bing Webmaster Tools (URL submission/IndexNow) and Google Search Console |
| Medium | Bridge page answers "what happened" in short fragments ("Same kitchen. Same address. New name.") | Fetched text | Add one full sentence with both names, the month and the address |
| Medium | No sentence on the homepage ties "open every day 11am to 8pm" to the restaurant name in prose | Fetched text | Included in the draft passage |
| Low | JSON-LD may lack `alternateName: "Island Panda"` (not confirmed in markup) | index.html line 37 onward | Add it; it is true and helps entity matching |
| Low | No llms.txt | n/a | Optional; see section 3 |
| Info | No Facebook or Instagram, so fewer entity anchors | Brief | Do not create accounts just for this |

## 1. Likely assistant answers today (inferred, not observed)
I could not query ChatGPT, Perplexity, Copilot or AI Overviews. A Bing search fetch returned unrelated "island" results, so nothing below is measured. These are expectations from the sources named in the brief.
- "Island Panda Sanibel": ChatGPT and Copilot (Bing-grounded) will likely cite the chamber listing, the July 2026 ribbon-cutting stories (captivasanibel.com, santivachronicle.com), TripAdvisor and delivery apps, all as Island Panda. Perplexity may add fireandfinn.com/island-panda/ if indexed. Google AIO will lean on the Business Profile (already renamed) and may show both names.
- "is Island Panda still open": risk of "open, 11am-8pm" from old pages with no rename mention, or "unclear". The bridge page is the right source but needs one full-sentence answer.
- "sushi on Sanibel Island", "hibachi takeout Sanibel", "poke bowl Sanibel": drawn from Yelp/TripAdvisor/Google listings and "where to eat" lists. Fire & Finn is probably absent or listed as Island Panda. Poke is weakest because no prose sentence ties poke to Sanibel beyond the title and description.
- New name absent from: chamber, TripAdvisor, Uber Eats/Postmates, DoorDash public page, both news stories.

## 2. Citability
Liftable now: "Island Panda is now Fire & Finn." / "Same kitchen. Same address. New name." / the address line / "Every day, 11am to 8pm" / "Order ahead for pickup at 2003 Periwinkle Way and it's waiting when you walk in." Each is short and needs page context.
Missing: a self-contained 60-110 word block. Draft (74 words), top of the Visit section as visible text under a heading such as "About Fire & Finn":

```
Fire & Finn is a takeout restaurant at 2003 Periwinkle Way in Tahitian Gardens, Sanibel, Florida. It serves hibachi, sushi rolls and build-your-own poke bowls. The restaurant was called Island Panda until early November 2026, when it changed its name. The kitchen and address stayed the same. It is open every day from 11am to 8pm. Order online through Toast, or call (239) 579-0783 and pick up at the restaurant.
```
Put the rename sentences (name change, same kitchen and address) at the top of the bridge page as a full paragraph too. H1 and menu text stay untouched.

## 3. Crawler access and llms.txt
All AI bots are allowed, with no snippet restrictions. Nothing to change.
llms.txt: Google ignores it and no major engine is confirmed to use it for citation. At most it gives agents a tidy pointer. It takes five minutes; add it only knowing it probably changes nothing. Draft:
```
# Fire & Finn
> Takeout hibachi, sushi rolls and build-your-own poke at 2003 Periwinkle Way, Sanibel, FL 33957. Formerly Island Panda (renamed early November 2026). Open daily 11am-8pm. Phone (239) 579-0783.

## Pages
- [Home, menu, hours and ordering](https://fireandfinn.com/)
- [Island Panda is now Fire & Finn](https://fireandfinn.com/island-panda/): what changed and what did not
- [Menu PDF](https://fireandfinn.com/menu.pdf)
```

## 4. Mention plan (owner approves and sends each; nothing goes out from me)
Update existing (highest value, they carry the old name):
1. Sanibel-Captiva Chamber member listing: request the name change.
2. TripAdvisor: owner "manage listing" name and website change. Keep reviews.
3. Uber Eats/Postmates: merchant support. DoorDash public page: ask support to refresh.
4. captivasanibel.com, santivachronicle.com: ask for an editor's note linking fireandfinn.com. sanibelseaschool.org: ask to update the name.
New and realistic: a short local-news brief on the rename; Sanibel "where to eat" lists (ask editors, no payment); one post on r/sanibel or local Facebook groups from the owner's own account, disclosing ownership.
Do not buy reviews, post under other names, or claim awards or rankings.

Note to the chamber and papers:
```
Hello, Island Panda at 2003 Periwinkle Way (Tahitian Gardens) is now Fire & Finn. The name changed in early November 2026. The kitchen, address, phone (239) 579-0783 and hours (daily, 11am-8pm) are the same, and we still serve hibachi, sushi rolls and build-your-own poke for takeout. Nine of the specialty rolls have new names. Could you update our listing or story to Fire & Finn (formerly Island Panda) and link to fireandfinn.com? Details are at fireandfinn.com/island-panda/. Thank you.
```

## 5. Monthly hand check
Use ChatGPT with search, Perplexity, Copilot and Google AI Mode, in a fresh signed-out session. Ask:
1. "What is Fire & Finn on Sanibel?"
2. "What happened to Island Panda on Sanibel?"
3. "Is Island Panda still open?"
4. "Where can I get hibachi takeout on Sanibel Island?"
5. "Where can I get a poke bowl on Sanibel?"
Good answer: Fire & Finn (formerly Island Panda), 2003 Periwinkle Way, daily 11am-8pm, phone (239) 579-0783, link to fireandfinn.com, no "closed" claim. For Q4 and Q5, being listed at all is a win. Log the date, assistant, cited sources and wrong facts; wrong facts show which listing to fix.

## Limitations
No assistant was queried, so section 1 is inference. The Bing fetch was unusable. WebFetch strips markup, so the `alternateName` gap was only checked by grepping `@type`. Wikipedia, Reddit, YouTube and LinkedIn presence were not checked; I assumed none from the brief. The score is judgment, not a measured metric.
