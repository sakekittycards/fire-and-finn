/* Fire & Finn — site settings and behaviors.
   Everything a person is likely to change lives in the block below. */

// ===================== SETTINGS =====================
// Toast online-ordering link. Same Toast location as Island Panda (Restaurant ID 300224);
// when the location is renamed in Toast after the rebrand, check whether this URL changes.
// Leave empty to make every Order button fall back to the phone number.
const ORDER_URL = "https://order.toasttab.com/online/island-panda-2003-periwinkle-way";

const PHONE_TEL = "tel:+12395790783";

// Full URLs. An empty value hides that link.
const SOCIAL = {
  instagram: "",
  facebook: "",
};

// Daily hours, Eastern time (24-hour clock).
const HOURS = { open: 11, close: 20 };
// ====================================================

(function () {
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Order buttons: live link, or call-to-order while there is no link yet.
  const live = ORDER_URL.trim().length > 0;
  document.querySelectorAll("[data-order]").forEach((a) => {
    if (live) {
      a.href = ORDER_URL;
      a.target = "_blank";
      a.rel = "noopener";
      if (a.dataset.live) a.textContent = a.dataset.live;
    } else {
      a.href = PHONE_TEL;
      if (a.dataset.call) a.textContent = a.dataset.call;
    }
  });

  // Open / closed line in the hero, from the Eastern-time clock.
  // Every element that shows the status gets the same words; the Order buttons get a green dot while the kitchen is open.
  const status = document.getElementById("status");
  try {
    const parts = new Intl.DateTimeFormat("en-US", {
      timeZone: "America/New_York", hour: "numeric", minute: "numeric", hourCycle: "h23",
    }).formatToParts(new Date());
    const h = Number(parts.find((p) => p.type === "hour").value) % 24;
    const m = Number(parts.find((p) => p.type === "minute").value);
    const now = h + m / 60;
    const isOpen = now >= HOURS.open && now < HOURS.close;
    const msg = isOpen ? "Open now, until 8pm" : (now < HOURS.open ? "Opens today at 11am" : "Closed for the night, opens 11am");
    if (status) status.classList.toggle("open", isOpen);
    document.body.classList.toggle("is-open", isOpen);
    document.querySelectorAll("#status-text, [data-status-text]").forEach((el) => { el.textContent = msg; });
  } catch (e) { /* keep the default "Open daily 11am–8pm" text */ }

  // Mobile navigation.
  const header = document.getElementById("site-header");
  const toggle = document.querySelector(".nav-toggle");
  const nav = document.getElementById("site-nav");
  if (header && toggle && nav) {
    const setOpen = (open) => {
      header.classList.toggle("open", open);
      toggle.setAttribute("aria-expanded", String(open));
      toggle.setAttribute("aria-label", open ? "Close the menu" : "Open the menu");
    };
    toggle.addEventListener("click", () => setOpen(!header.classList.contains("open")));
    nav.addEventListener("click", (e) => { if (e.target.closest("a")) setOpen(false); });
    document.addEventListener("keydown", (e) => { if (e.key === "Escape") setOpen(false); });
    document.addEventListener("click", (e) => {
      if (header.classList.contains("open") && !header.contains(e.target)) setOpen(false);
    });
  }

  // The header is clear over the hero and turns solid once the page moves.
  if (header) {
    const onScroll = () => header.classList.toggle("scrolled", window.scrollY > 24);
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }

  // Slow depth on the big photos: they drift a few pixels against the page as it scrolls. Wide screens only, never for reduced motion.
  const drifting = Array.from(document.querySelectorAll("[data-parallax]"));
  if (drifting.length && !reduce && window.matchMedia("(min-width: 1000px)").matches) {
    document.documentElement.classList.add("parallax-on");
    let queued = false;
    const update = () => {
      queued = false;
      const vh = window.innerHeight;
      drifting.forEach((el) => {
        const r = el.parentElement.getBoundingClientRect();
        if (r.bottom < -100 || r.top > vh + 100) return;
        const p = (r.top + r.height / 2 - vh / 2) / vh;          // -0.5 above centre … 0.5 below
        const amp = Number(el.dataset.parallax) || 18;
        el.style.transform = `translate3d(0, ${(-p * amp).toFixed(1)}px, 0) scale(1.08)`;
      });
    };
    const ask = () => { if (!queued) { queued = true; requestAnimationFrame(update); } };
    window.addEventListener("scroll", ask, { passive: true });
    window.addEventListener("resize", ask);
    update();
  }

  // A few embers rising behind the hero copy (the waterline is SVG, animated in CSS).
  if (!reduce) {
    document.querySelectorAll(".embers").forEach((embers) => {
      for (let i = 0; i < 8; i++) {   // a few, slow, small: noticed second, not first
        const s = document.createElement("i");
        const dur = 10 + Math.random() * 8;
        s.style.cssText =
          `left:${(4 + Math.random() * 88).toFixed(1)}%;--h:${(10 + Math.random() * 16).toFixed(0)}px;` +
          `--d:${dur.toFixed(1)}s;--delay:${(-Math.random() * dur).toFixed(1)}s;--sway:${(Math.random() * 60 - 30).toFixed(0)}px`;
        embers.appendChild(s);
      }
    });
  }

  // Gentle section entrances. Fail-safe: whatever happens, everything is visible within two seconds.
  const revealEls = document.querySelectorAll(".reveal");
  const showAll = () => revealEls.forEach((el) => el.classList.add("in"));
  if ("IntersectionObserver" in window && !reduce) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((en) => { if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); } });
    }, { rootMargin: "0px 0px -5% 0px", threshold: 0 });
    revealEls.forEach((el) => io.observe(el));
    setTimeout(showAll, 1800);
  } else {
    showAll();
  }

  // Menu category navigation: highlight the category on screen, keep its pill in view.
  const links = Array.from(document.querySelectorAll(".menu-nav a"));
  const groups = links.map((a) => document.querySelector(a.getAttribute("href"))).filter(Boolean);
  if (links.length && groups.length && "IntersectionObserver" in window) {
    const navWrap = document.querySelector(".menu-nav .wrap");
    const menuNav = document.querySelector(".menu-nav");
    const setActive = (id) => {
      links.forEach((a) => {
        const on = a.getAttribute("href") === "#" + id;
        a.classList.toggle("active", on);
        if (on) a.setAttribute("aria-current", "true"); else a.removeAttribute("aria-current");
      });
      const g = document.getElementById(id);   // the pill takes the section's colour: orange for the hot side, blue for the cold
      menuNav.classList.toggle("hot", !!g && g.classList.contains("hot"));
      menuNav.classList.toggle("cold", !!g && g.classList.contains("cold"));
      const active = navWrap.querySelector("a.active");
      if (active) {
        const left = active.offsetLeft - (navWrap.clientWidth - active.offsetWidth) / 2;
        navWrap.scrollTo({ left: Math.max(0, left), behavior: reduce ? "auto" : "smooth" });
      }
    };
    const spy = new IntersectionObserver((entries) => {
      const visible = entries.filter((e) => e.isIntersecting).sort((a, b) => b.intersectionRatio - a.intersectionRatio);
      if (visible[0]) setActive(visible[0].target.id);
    }, { rootMargin: "-30% 0px -55% 0px", threshold: [0, 0.2, 0.5, 1] });
    groups.forEach((g) => spy.observe(g));
  }

  // Prices read as dollars to screen readers; the active category pill is marked current.
  document.querySelectorAll(".price, .proteins .p").forEach((el) => {
    const n = el.textContent.trim();
    if (/^\d+$/.test(n)) el.setAttribute("aria-label", "$" + n);
  });

  // Menu structured data, built from the menu on the page so it always matches it.
  try {
    const sections = [];
    document.querySelectorAll(".menu .group").forEach((g) => {
      const name = (g.querySelector("h3") || {}).childNodes;
      const title = name ? Array.from(name).filter((n) => n.nodeType === 3).map((n) => n.textContent).join("").trim() : "";
      const items = [];
      const add = (nameText, price, desc) => {
        const item = { "@type": "MenuItem", "name": nameText.replace(/\*$/, "").trim() };
        if (desc) item.description = desc;
        if (price) item.offers = { "@type": "Offer", "price": price, "priceCurrency": "USD" };
        items.push(item);
      };
      g.querySelectorAll(".dish, .feature").forEach((d) => {
        const n = d.querySelector(".name"); if (!n) return;
        const nameText = Array.from(n.childNodes).filter((x) => x.nodeType === 3 || !x.classList || (!x.classList.contains("raw") && !x.classList.contains("kicker"))).map((x) => x.textContent).join("");
        const p = d.querySelector(".price");
        const desc = Array.from(d.querySelectorAll(".desc, .parts p")).map((e) => e.textContent.replace(/\s+/g, " ").trim()).join(" ");
        add(nameText, p ? p.textContent.trim() : (g.id === "kids" ? "15" : ""), desc);
      });
      g.querySelectorAll(".proteins li").forEach((li) => {
        const base = li.closest(".combos") ? "Hibachi combo" : "Hibachi";
        add(base + ": " + li.querySelector(".n").textContent.replace(/\*/g, "").trim(), li.querySelector(".p").textContent.trim(), "");
      });
      const poke = g.querySelector(".poke-head");
      if (poke) add("Poke Bowl, build your own", poke.querySelector(".price").textContent.trim(),
        Array.from(g.querySelectorAll(".step")).map((s) => {
          const t = s.querySelector(".t"); const body = Array.from(s.querySelectorAll("p")).map((p) => p.textContent.replace(/\s+/g, " ").trim()).join(" ");
          return (t ? t.textContent.trim() + ": " : "") + body;
        }).join(" "));
      if (items.length) sections.push({ "@type": "MenuSection", "name": title, "hasMenuItem": items });
    });
    if (sections.length) {
      const s = document.createElement("script"); s.type = "application/ld+json";
      s.textContent = JSON.stringify({ "@context": "https://schema.org", "@type": "Menu", "name": "Fire & Finn menu", "url": "https://fireandfinn.com/#menu", "hasMenuSection": sections });
      document.head.appendChild(s);
    }
  } catch (e) { /* structured data is a bonus, never a blocker */ }

  // Social links, only when a URL is set.
  const social = document.getElementById("social");
  if (social) {
    const labels = { instagram: "Instagram", facebook: "Facebook" };
    Object.keys(SOCIAL).forEach((k) => {
      if (!SOCIAL[k]) return;
      const a = document.createElement("a");
      a.href = SOCIAL[k]; a.target = "_blank"; a.rel = "noopener"; a.textContent = labels[k] || k;
      social.appendChild(a);
    });
  }
})();
