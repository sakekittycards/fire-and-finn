/* Fire & Finn — site settings and small behaviors.
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
  const status = document.getElementById("status");
  const text = document.getElementById("status-text");
  if (status && text) {
    try {
      const parts = new Intl.DateTimeFormat("en-US", {
        timeZone: "America/New_York", hour: "numeric", minute: "numeric", hourCycle: "h23",
      }).formatToParts(new Date());
      const h = Number(parts.find((p) => p.type === "hour").value) % 24;
      const m = Number(parts.find((p) => p.type === "minute").value);
      const now = h + m / 60;
      if (now >= HOURS.open && now < HOURS.close) {
        status.classList.add("open");
        text.textContent = "Open now, until 8pm";
      } else if (now < HOURS.open) {
        text.textContent = "Opens today at 11am";
      } else {
        text.textContent = "Closed for the night, opens 11am";
      }
    } catch (e) { /* keep the default "Open daily 11am–8pm" text */ }
  }

  // Fire and water in the hero: embers rise on the left, bubbles on the right.
  // Skipped entirely when the visitor prefers reduced motion.
  const hero = document.querySelector(".hero");
  if (hero && !window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    const box = document.createElement("div");
    box.className = "particles"; box.setAttribute("aria-hidden", "true");
    for (let i = 0; i < 24; i++) {
      const ember = i < 14;
      const p = document.createElement("i");
      p.className = ember ? "ember" : "bubble";
      const left = ember ? 3 + Math.random() * 44 : 56 + Math.random() * 41;
      const size = ember ? 2 + Math.random() * 4 : 3 + Math.random() * 5;
      const dur = (ember ? 7 : 10) + Math.random() * 8;
      p.style.cssText = `left:${left.toFixed(1)}%;width:${size.toFixed(1)}px;height:${size.toFixed(1)}px;` +
        `animation-duration:${dur.toFixed(1)}s;animation-delay:${(-Math.random() * dur).toFixed(1)}s;--sway:${(Math.random() * 60 - 30).toFixed(0)}px`;
      box.appendChild(p);
    }
    hero.appendChild(box);
  }

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
