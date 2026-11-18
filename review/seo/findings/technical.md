# Technical SEO: fireandfinn.com (measured 2026-11-18)

**Score: 76/100.** On-site basics are clean (canonicals, sitemap, 404, image dimensions, font preloads). Points lost for the old-domain redirect method, no search-engine verification, and a hero fade-in that delays LCP.

## Findings

| Sev | Finding | Evidence | Fix |
|---|---|---|---|
| High | Old domain is a 200 page with meta refresh + noindex, not a 301 | `curl https://island-panda.com/` 200; `/menu` also 200; source has noindex, refresh 0, canonical, JS replace | True 301 (see Q1) |
| High | No Search Console / Bing verification, so sitemap and the domain move are unconfirmed | Brief; empty `site:` | Checklist below |
| Medium | workers.dev host still indexed with old content; now 301s to homepage | 1 hop to https://fireandfinn.com/ | Leave the 301; let it recrawl. Do not add noindex or robots blocks there |
| Medium | `/menu-source/` is Disallowed but publicly 200 (7.0 MB, includes menu-v8.html with no noindex) | `curl -I /menu-source/menu-v8.html` 200 | Robots does not hide anything and disallowed URLs can still be indexed as bare links. Move it off the published branch or accept it |
| Medium | Hero images fade from opacity 0 (`settle` 1.2s, +.12s delay), so LCP paints about 1.2-1.3s after the image arrives. Hero text is also hidden until delays up to .6s plus .8s | styles.css:170-179 | Shorten to about .4s, or animate transform only |
| Medium | Both hero images preloaded with `fetchpriority=high`; they stack on mobile, so the below-fold roll competes with the LCP image | index.html:32-33,102,107 | Make the roll low priority on narrow screens |
| Medium | Menu JSON-LD exists only after JS runs | Raw: 1 ld+json block. Rendered: 2, second is a valid 6,787-byte Menu | See Q3 |
| Low | Bridge head thinner than homepage: no apple-touch-icon, no 128px icon. Google wants favicons in multiples of 48px; 32 and 128 both miss | island-panda/index.html:22 | Add a 48 or 96px icon to both pages; apple-touch-icon on the bridge |
| Low | Sitemap changefreq and priority are ignored by Google; "weekly" overstates cadence | sitemap.xml | Delete them; keep lastmod |
| Low | No og:locale; no twitter:title/description (crawlers fall back to og) | index.html:10-23 | Optional |
| Low | /index.html and /island-panda/index.html serve duplicate 200s | curl, 0 hops | Canonical covers it |
| Info | lastmod (2026-11-08 both pages, 2026-10-22 menu.pdf) matches last git commits | git log | Accurate; change only with content |
| Info | /review/ is 404 live; nothing to disallow. menu.pdf (265 KB) is fine in the sitemap, low value but harmless | curl | None |
| Info | `?v=13` is harmless; Pages serves max-age=600 anyway. Mixed-case paths 404 | headers | Bump v on CSS/JS edits |

## Measured hops (curl -L)

| Request | Hops | Result |
|---|---|---|
| http://fireandfinn.com/, http://www., https://www. | 1 | https apex |
| http://www.fireandfinn.com/island-panda | 2 | https apex /island-panda/ |
| /island-panda | 1 | /island-panda/ |
| /index.html, /island-panda/index.html, `/?utm_source=x`, /menu.pdf, /sitemap.xml | 0 | 200 |
| /menu, /nope, /Island-Panda/, /INDEX.html, /review/ | 0 | 404 |
| http://island-panda.com/, https://www.island-panda.com/ | 1 | https://island-panda.com/ (200, no redirect) |
| island-panda.baussmgmt.workers.dev | 1 | https://fireandfinn.com/ |

No chain exceeds 2 hops. Canonicals are self-referential and consistent.

## Q1: old-domain redirect
- Google's "Redirects and Google Search" page lists meta refresh as a supported type. From memory, an instant refresh is treated as permanent and a delayed one as temporary, with server-side redirects recommended. I did not re-fetch it; confirm the wording.
- noindex hurts. It asks Google to drop the old URL, which contradicts the canonical and refresh that say "consolidate", and a noindexed page may not pass signals. With a true 301 it never matters.
- Change of Address expects a verified old property and a site-wide 301. A 200 refresh page will very likely fail its check (could not run the tool).
- **Recommendation:** make island-panda.com and www answer 301 to https://fireandfinn.com/island-panda/, and /menu* to https://fireandfinn.com/#menu. Easiest is a Cloudflare Redirect Rule (hostname must be proxied); otherwise return `Response.redirect(url, 301)` from the Worker. Then remove noindex. Then, if wanted, run Change of Address; the old homepage lands on the bridge page, not the new homepage, so confirm the tool accepts that.

## Q3: JSON-LD rendering
- Confirmed: Menu block is built at runtime (app.js:197-198); Restaurant block is static.
- Googlebot renders JS, with a delay. Bingbot renders less reliably. GPTBot, ClaudeBot, PerplexityBot and similar generally do not run JS, so they never see it, but they do see the full menu as plain HTML text, which is the stronger signal.
- **Recommendation:** keep it dynamic. Inlining 6.8 KB by hand with no build step risks drift against a hand-edited menu, and a stale price in schema is worse than none. If inlined later, generate it with a pre-commit script.

## Q5: mobile and CWV (source analysis)
- LCP candidate: hero-hibachi. A 390px phone at 2x-3x picks the 800 or 1024px file, so 192-302 KB, plus the roll at 74-115 KB: about 266-417 KB. At 1x it is 145 + 58 = 203 KB. Desktop pulls 302 KB + 133 KB.
- CLS low: images have width/height and aspect-ratio; animations and parallax use transform/opacity. Fonts use swap with no size-adjust fallback (small reflow possible); four preloads, about 67 KB.
- INP low risk: scroll handlers are passive. Watch paint cost from backdrop-filter on the fixed header and menu bar, and the ember animations with will-change, on low-end phones.
- Fixed bottom bar (48px buttons plus safe-area): I did not verify the footer reserves matching space.

## Indexing checklist
1. Search Console: add the Domain property for fireandfinn.com; verify via DNS TXT at GoDaddy. Alternatives: HTML file in repo root, or meta tag in the head (both work on Pages).
2. Same for island-panda.com (TXT at Cloudflare). A Worker can serve the HTML file if DNS is a problem.
3. Submit https://fireandfinn.com/sitemap.xml. Inspect `/` and `/island-panda/`; Request indexing.
4. Ship the 301 first, then Change of Address (old to new).
5. Bing Webmaster Tools: import from Search Console, resubmit the sitemap.
6. IndexNow: host `/<key>.txt` in the repo root; optional, not submitted.

## Top 5 actions (dependency order)
1. Verify fireandfinn.com in Search Console. Fails if: still unverified after 48h.
2. Submit the sitemap and request indexing for the two pages. Fails if: sitemap is not "Success", or "URL is not on Google" after 7 days.
3. Replace the island-panda.com refresh page with a 301 and drop noindex. Fails if: `curl -sI https://island-panda.com/` is not 301 with the right Location.
4. Verify island-panda.com, then run Change of Address. Fails if: the tool rejects the redirect.
5. Import to Bing; shorten the hero fade to about .4s. Fails if: Bing shows 0 pages after 2 weeks, or LCP does not improve.

## Limitations
No PSI, CrUX or Lighthouse data. Google's redirect docs not re-read live. Change of Address cannot be run without Search Console. Index state of old hosts not checked. Footer clearance behind the bar and real-device paint cost not measured. Bing's meta-refresh handling is undocumented to my knowledge.
