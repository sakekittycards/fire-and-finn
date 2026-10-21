# fireandfinn.com

Static site for Fire & Finn, Hibachi · Sushi, 2003 Periwinkle Way, Sanibel, FL. Same setup as the Island Panda site: plain HTML, CSS and a little JavaScript, hosted on GitHub Pages.

## Files
- `index.html`: the whole site (hero, the Fire / Finn split, full menu, visit).
- `styles.css`: brand system. Orange is the hot side (hibachi), blue is the cold side (sushi & poke).
- `app.js`: settings at the top (ordering link, phone, social links, hours) and the open/closed line.
- `menu.pdf`: the printed menu, linked from the Menu section. Replace it whenever the menu changes.
- `assets/`: logo, flame and wave marks cut from the logo, favicon, share image, fonts (Tenor Sans and Jost, SIL Open Font License).
- `CNAME`: the custom domain for GitHub Pages.

## Things you will change
- **Online ordering:** paste the Toast link into `ORDER_URL` at the top of `app.js`. Until then every Order button calls the restaurant instead.
- **Social links:** fill in `SOCIAL` in `app.js`. Empty values stay hidden.
- **Menu:** edit the Menu section of `index.html` and drop in a new `menu.pdf`. Keep the printed menu and the site in step.
- **Hours:** `HOURS` in `app.js` drives the open/closed line; the text in the Visit section and footer is written out by hand.

## Preview locally
```bash
python -m http.server 8788
```
Then open http://localhost:8788/.

## Going live (not done yet)
1. Create the GitHub repo (for example `sakekittycards/fire-and-finn`), push `main`.
2. Repo Settings → Pages → Source: Deploy from a branch, `main`, `/ (root)`. The `CNAME` file sets the domain.
3. DNS for fireandfinn.com (at GoDaddy, or in Cloudflare if the zone moves there): four A records on `@` → 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153, and a CNAME on `www` → `sakekittycards.github.io`.
4. Wait for the Pages certificate, then turn on Enforce HTTPS.
5. Point island-panda.com at the new site once Fire & Finn opens.
