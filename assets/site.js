(() => {
  // Lightbox: any element with data-full opens that image large.
  const lb = document.createElement("dialog");
  lb.className = "lb";
  lb.innerHTML = '<button type="button" aria-label="Close">×</button><img alt=""><p></p>';
  document.body.appendChild(lb);
  const lbImg = lb.querySelector("img"), lbCap = lb.querySelector("p");
  lb.querySelector("button").addEventListener("click", () => lb.close());
  lb.addEventListener("click", e => { if (e.target === lb) lb.close(); });
  document.addEventListener("click", e => {
    const t = e.target.closest("[data-full]");
    if (!t) return;
    lbImg.src = t.dataset.full;
    lbImg.alt = t.querySelector("img")?.alt || "";
    lbCap.textContent = t.dataset.cap || "";
    if (lb.showModal) lb.showModal(); else lb.setAttribute("open", "");
  });

  // Studio art from the Art folder: hide the section if none of the pictures are there.
  const art = document.getElementById("studio-art");
  if (art) {
    const imgs = [...art.querySelectorAll("img")];
    let failed = 0;
    const check = () => { if (failed === imgs.length) art.hidden = true; };
    imgs.forEach(img => {
      const fail = () => { img.closest("button").hidden = true; failed++; check(); };
      if (img.complete && img.naturalWidth === 0) fail(); else img.addEventListener("error", fail);
    });
  }

  // Contact form: no mail service is connected yet, so say so plainly.
  const form = document.getElementById("contact-form");
  if (form) {
    const note = document.getElementById("contact-note");
    form.addEventListener("submit", e => {
      e.preventDefault();
      const email = document.getElementById("c-email");
      if (!email.value || !email.checkValidity()) { note.textContent = "Enter a valid email address so we can reply."; email.focus(); return; }
      note.textContent = "Thanks. Sign-ups aren't connected to email yet, so this message wasn't sent.";
      form.reset();
    });
  }

  const yr = document.getElementById("yr");
  if (yr) yr.textContent = new Date().getFullYear();
})();
