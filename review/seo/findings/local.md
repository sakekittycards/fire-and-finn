# Local SEO findings: Fire & Finn (2026-11-18)

Type: brick-and-mortar takeout restaurant (address shown, no SAB intent). Vertical: restaurant. Proximity (about 55% of ranking variance per the Search Atlas study) is outside our control.

## Score: 49/100
| Dimension | Weight | Score | Why |
|---|---|---|---|
| GBP signals | 25 | 14 | Verified, renamed, menu and site linked. Category unproven, dine-in and service-area contradictions, 0 posts live |
| Reviews | 20 | 9 | About 20 old reviews unverified, velocity unknown, no cadence |
| Local on-page | 20 | 11 | One page; no dedicated hibachi/sushi/poke pages (the #1 local organic factor per Whitespark) |
| NAP and citations | 15 | 5 | Every third-party citation still says Island Panda |
| Local schema | 10 | 6 | Good Restaurant base; no geo, sameAs, @id, hasMap |
| Local links | 10 | 4 | All press and the chamber listing carry the old name |

## Key fact I could not verify
Google's category list could not be fetched. The GBP API page (https://developers.google.com/my-business/reference/rest/v4/categories/list) only describes `categories.list`, and pleper.com loads its list dynamically. The category names below come from my own knowledge, not a fetch. Confirm each in the GBP category dropdown before saving. Source for the guideline quotes: https://support.google.com/business/answer/3038177

## 1. Category recommendation
- Primary: **Sushi restaurant**. It is the broadest match for "sushi sanibel", the biggest query. The business has seating and a full restaurant menu, so "restaurant" is more accurate than "takeaway". Google's own test is "This business *is* a ...".
- Secondaries (max 4): **Japanese restaurant** ("japanese food sanibel"), **Poke bar** ("poke sanibel"), **Takeout restaurant** ("takeout sanibel"), and **Teppanyaki restaurant** ("hibachi sanibel").
- Caveat on Teppanyaki: it implies a tableside grill. If the hibachi is cooked in the kitchen for takeout, use "Japanese steakhouse" or skip both. The owner decides.
- "Sushi takeaway" is a defensible primary only if the owner calls the business takeout-only. It conflicts with the seating attributes and is the narrower label.
- Google says to "choose the fewest number of categories" that describe the core business, so 4 secondaries is the ceiling, not a target.
- Test: change the primary once, then watch "sushi sanibel" in the map pack for 3 weeks.

## 2. Rebrand playbook, ordered by impact
Warning: Google's guideline says a name change that alters proper nouns may not qualify as a rebrand, and then "the business is treated as new". Island Panda to Fire & Finn changes the proper nouns. The profile is verified now, but keep proof (signage photo, Toast receipt, Florida fictitious-name filing, a dated invoice) in case of a suspension or lost reviews.

| # | Platform | How | Feeds |
|---|---|---|---|
| 1 | Google | Done. Fix category, attributes, publish posts | Maps, Search, Gemini |
| 2 | Bing Places | Claim or import from Google, then edit name | Copilot, ChatGPT search (Bing-backed, widely reported) |
| 3 | Apple Business Connect | Claim the place, edit name, hours, website | Apple Maps, Siri |
| 4 | Yelp | Claim the Island Panda login, edit the name in Business Support; if locked, use the support form. Help pages did not render, so steps are unverified | Alexa, Siri ratings (industry knowledge) |
| 5 | TripAdvisor | Owner Center, then a listing-correction request for the name. Help article did not render, so unverified | Travel queries, AI answers citing TripAdvisor |
| 6 | Foursquare | Suggest-edit or claim | Data feed to Apple Maps and other apps |
| 7 | DoorDash | Public title and h1 lag the portal; recheck in 48 to 72 hours, else ticket | Delivery category pages |
| 8 | Uber Eats | Support ticket required (name field disabled) | Same |
| 9 | Chamber directory | Email the chamber | Local link and mention |
| 10 | Facebook/Instagram | Do not create just for SEO; if made, use the exact NAP | Weak |

The "Feeds" column is industry knowledge, not verified here. Treat it as likely, not proven.

## 3. NAP
Canonical: **Fire & Finn, 2003 Periwinkle Way, Sanibel, FL 33957, (239) 579-0783**.
- "&" vs "and": do not edit the GBP name again now, since name edits can trigger re-review. Use "Fire & Finn" on the site and on new listings (Yelp, TripAdvisor, Apple, Bing). Keep "Fire and Finn" in schema `alternateName`. Aggregators usually treat the two as equivalent.
- "Formerly Island Panda": put it in descriptions, the About text, the site footer and the story page. Never in a name field (Google bars extra words in the name).
- Service area: delete Estero, Naples, Cape Coral, Fort Myers, Bonita Springs and Barefoot Beach unless the restaurant itself delivers there. A storefront takeout place that does not deliver should list none.
- Dine-in contradiction: the owner must choose. If people eat in the breezeway, switch "No dine-in" off. If not, remove the breezeway wording from the description.

## 4. Review cadence
- Thresholds from the skill references (local-seo-signals.md): about 10 reviews is where a ranking boost shows; an 18-day gap is where rankings fall off.
- Target: at least 1 new review every 14 days, 4 to 6 per month as the goal. Confirm the 20 old reviews carried over to the renamed profile.
- Where the Google review link (short g.page URL) may live: Toast receipt footer if editable (unverified), a counter card as plain text, the website footer, the order-confirmation message, and a GBP post. Ask everyone, never filter by sentiment.
- Reply to every review within 48 hours. Mention the rename once, naturally.
- Yelp: "Find us on Yelp" only. TripAdvisor: no incentives.
- Do not display the old self-reported 5.0 or the Postmates 4.8 as current numbers.

## 5. Schema
Current JSON-LD: /index.html lines 36 to 70 (Restaurant, alternateName ["Island Panda", ...]).
Add: `@id` ("https://fireandfinn.com/#restaurant"), `geo` (26.43967, -82.06533; check against the GBP pin, since Nominatim can be off by 10 m or more), `hasMap` (the GBP Maps URL the owner copies), `acceptsReservations: false`, `sameAs` with GBP/Maps, TripAdvisor, Toast, DoorDash and Uber Eats. Add DoorDash, Uber and TripAdvisor only after each page shows the new name. Add `areaServed` only if delivery is real. Add "Fire and Finn" to `alternateName`.
Do not add: `aggregateRating` or `review` (self-serving, unverified); Yelp, Facebook or Instagram URLs that do not exist; FAQPage; photos of AI stand-ins as menu-item images. Keep `Restaurant`.

## 6. Local links and pitch
Realistic sources: Sanibel-Captiva Chamber listing; Santiva Chronicle and captivasanibel.com (both ran the July ribbon-cutting); Island Reporter/Islander (not checked); Sanibel Sea School's recommendations; any local "best of" list that already includes Island Panda.
Pitch: "Hi, I'm [name] at the restaurant at 2003 Periwinkle Way in Tahitian Gardens. You listed or wrote about us as Island Panda. As of November we are Fire & Finn: same kitchen, same address, same phone (239-579-0783), still hibachi, sushi rolls and build-your-own poke, open daily 11 to 8. Would you update the name and link to fireandfinn.com? A short note that we are 'formerly Island Panda' would help people find us."

## Findings
| Sev | Finding | Evidence | Fix |
|---|---|---|---|
| High | Primary category may be the narrow "Sushi takeaway" | Brief; https://support.google.com/business/answer/3038177 | Switch to Sushi restaurant, test |
| High | "No dine-in" contradicts seating and breezeway text | GBP attributes (brief) | Owner decides, align both |
| High | Rename may be treated as a new business | https://support.google.com/business/answer/3038177 | Keep proof; watch reviews and status |
| High | All citations carry the old name | Brief | Playbook above |
| Med | Service area lists 6 cities with no delivery | Brief | Remove |
| Med | Posts drafted but not published | Brief | Publish with the owner's go-ahead |
| Med | Schema lacks geo, sameAs, @id, hasMap | /index.html JSON-LD | Add per section 5 |
| Med | No dedicated hibachi, sushi, poke pages | Single-page site | Build after the rebrand settles |
| Low | "&" vs "and" mismatch | GBP vs site | Standardize on new listings |

## Top 10 actions
1. Fix the dine-in and service-area contradictions (owner, GBP). Fails if GBP still shows "No dine-in" beside breezeway text a week later.
2. Change the primary category and set secondaries (owner). Fails if "sushi sanibel" map rank does not improve in 3 weeks.
3. Publish the three GBP posts, then one per week (owner). Fails if the Posts tab is empty after 7 days.
4. Put the Google review link in 3 places (owner). Fails if a gap over 18 days appears.
5. Update Apple Business Connect and Bing Places (owner). Fails if searching the new name in Apple Maps or Bing still returns Island Panda after 2 weeks.
6. Claim Yelp and TripAdvisor and rename (owner). Fails if the old name is still live after 30 days.
7. Ask the chamber and 3 local outlets to update the name (owner). Fails if no source updates in 30 days.
8. Chase DoorDash and Uber Eats name changes (owner). Fails if titles still read Island Panda after 7 days.
9. Add the schema fields in section 5 (site change). Fails if the Rich Results Test or Schema validator shows errors.
10. Add dedicated hibachi, sushi and poke sections or pages with "Sanibel" in the copy (site change). Fails if no ranking for "hibachi sanibel" after 8 weeks.

## Limitations
No live GBP, review or map-pack data (no DataForSEO, no logins). The category list was not fetched, so names are from memory. Yelp and TripAdvisor help pages returned empty shells, so those steps are unverified. Siri, Alexa, Copilot and ChatGPT data-source claims are common knowledge, not confirmed. Review count and rating are self-reported. Citation presence on Yelp and BBB was not directly checked. Proximity cannot be changed.
