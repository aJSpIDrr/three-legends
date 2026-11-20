// Store section on each game page.
// 1. Shows the saved copy (assets/store.json, refreshed every few hours by a GitHub job) straight away.
// 2. Then asks the game itself for its current store list and redraws if anything changed.
(() => {
  const box = document.querySelector('[data-store]');
  if (!box) return;
  const game = box.dataset.store;

  const GAMES = {
    dustborn: {
      live: 'https://dustborn-server.onrender.com/api/shop/catalog',
      buy: 'https://dustborn.onrender.com/#/bazaar',
      where: 'In the game: Bazaar → Get scrip.',
      bonus: 'Your first pack gives double scrip.',
      items: (c) => (c.packs || []).map((p) => ({
        name: p.name, price: p.price, tag: p.id === 'war_chest' ? 'Best value' : p.id === 'satchel' ? 'Popular' : null,
        what: `${p.scrip} scrip`, text: 'Scrip is the rare currency for rare gear, boosts and services.',
        img: p.img ? `https://dustborn.onrender.com/assets/${p.img}.webp` : null,
      })),
    },
    'dark-alliance': {
      live: 'https://dark-alliance-njj8.onrender.com/api/store/catalog',
      buy: 'https://dark-alliance-play.onrender.com/',
      where: 'In the game: Shop → Store.',
      bonus: 'Your first purchase gives double soul shards.',
      items: (c) => (c.products || []).map((p) => ({
        name: p.name, price: p.price, tag: p.tag || (p.once ? 'One per lord' : null),
        what: p.kind === 'shards' ? `${p.shards} soul shards` : p.kind === 'gold' ? 'Gold that grows with your level'
          : p.kind === 'starter' ? 'Starter bundle' : p.kind === 'perk' ? 'Permanent perk' : '',
        text: p.text || '',
        img: p.art ? `https://dark-alliance-play.onrender.com/art/${p.art}.webp` : null,
      })),
    },
  };
  const G = GAMES[game];
  if (!G) return;

  const SIGN = { ZAR: 'R', USD: '$', EUR: '€', GBP: '£', NGN: '₦', GHS: 'GH₵', KES: 'KSh ' };
  const money = (n, cur) => {
    if (!(n > 0)) return '';
    const s = Number(n).toFixed(2);
    return SIGN[cur] ? SIGN[cur] + s : `${s} ${cur}`;
  };
  const esc = (s) => String(s ?? '').replace(/[&<>"]/g, (ch) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[ch]));

  let shown = '';
  function draw(c, live) {
    const items = G.items(c).filter((x) => x.name && x.price > 0);
    if (!items.length) return;
    const key = JSON.stringify([c.currency, c.enabled, items]);
    if (key === shown) { mark(live); return; }
    shown = key;
    const open = c.enabled !== false;
    box.querySelector('.store-grid').innerHTML = items.map((x) => `
      <article class="sitem">
        <div class="sitem-art">${x.img ? `<img src="${esc(x.img)}" alt="" loading="lazy" onerror="this.remove()">` : ''}${x.tag ? `<span class="stag">${esc(x.tag)}</span>` : ''}</div>
        <div class="sitem-body">
          <h3>${esc(x.name)}</h3>
          ${x.what ? `<p class="swhat">${esc(x.what)}</p>` : ''}
          ${x.text ? `<p class="stext">${esc(x.text)}</p>` : ''}
          <div class="sbuy">
            <span class="sprice">${esc(money(x.price, c.currency))}</span>
            ${open ? `<a class="btn" href="${G.buy}" target="_blank" rel="noopener">Buy in game</a>` : '<span class="ssoon">Coming soon</span>'}
          </div>
        </div>
      </article>`).join('');
    box.querySelector('.store-note').textContent =
      `${c.firstPurchaseDouble ? G.bonus + ' ' : ''}Prices in ${c.currency}. ${G.where} You sign in to the game to buy, and payment is handled securely by Paystack.`;
    mark(live);
  }
  function mark(live) {
    const s = box.querySelector('.store-status');
    if (s) s.textContent = live ? 'Live prices from the game' : 'Checking the game for the latest prices…';
    if (s) s.classList.toggle('on', !!live);
  }

  fetch('assets/store.json', { cache: 'no-cache' })
    .then((r) => r.json()).then((d) => { const c = d.games && d.games[game]; if (c && !shown) draw(c, false); })
    .catch(() => {});

  const ctl = typeof AbortController === 'function' ? new AbortController() : null;
  const timer = setTimeout(() => ctl && ctl.abort(), 90000);   // a sleeping free server can take a minute to wake
  fetch(G.live, { signal: ctl && ctl.signal, headers: { Accept: 'application/json' } })
    .then((r) => (r.ok ? r.json() : null))
    .then((c) => { if (c && (c.packs || c.products)) draw(c, true); else mark(false); })
    .catch(() => { const s = box.querySelector('.store-status'); if (s) s.textContent = ''; })
    .finally(() => clearTimeout(timer));
})();
