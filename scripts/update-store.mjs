// Refreshes assets/store.json (the saved copy of both game stores) from the games' public store lists.
// Run by .github/workflows/update-store.yml every few hours, or by hand: node scripts/update-store.mjs
// A game that does not answer (asleep on Render's free plan, or down) keeps its last saved copy.
import { readFileSync, writeFileSync } from 'node:fs';

const FILE = new URL('../assets/store.json', import.meta.url);
const SOURCES = {
  dustborn: 'https://dustborn-server.onrender.com/api/shop/catalog',
  'dark-alliance': 'https://dark-alliance-njj8.onrender.com/api/store/catalog',
};

const old = JSON.parse(readFileSync(FILE, 'utf8'));
const next = { ...old, games: { ...old.games } };
let changed = false;

async function fetchCatalog(url) {
  // A sleeping free server can take up to a minute to wake, so try a few times.
  for (let i = 0; i < 4; i++) {
    try {
      const r = await fetch(url, { signal: AbortSignal.timeout(75000), headers: { Accept: 'application/json' } });
      if (r.ok && (r.headers.get('content-type') || '').includes('json')) return await r.json();
      console.log(`  ${url} answered ${r.status}`);
    } catch (e) { console.log(`  ${url} failed: ${e.message}`); }
    await new Promise((ok) => setTimeout(ok, 15000));
  }
  return null;
}

for (const [game, url] of Object.entries(SOURCES)) {
  console.log(`Fetching ${game}…`);
  const c = await fetchCatalog(url);
  const list = c && (c.packs || c.products);
  if (!Array.isArray(list) || list.length === 0) { console.log(`  kept the saved ${game} store`); continue; }
  const strip = (x) => JSON.stringify({ ...x, fetched: undefined });
  if (!old.games[game] || strip(old.games[game]) !== strip(c)) {
    next.games[game] = { ...c, fetched: new Date().toISOString() };
    changed = true;
    console.log(`  ${game} store changed: ${list.length} items`);
  } else console.log(`  ${game} store unchanged`);
}

if (changed) {
  next.updated = new Date().toISOString();
  writeFileSync(FILE, JSON.stringify(next, null, 2) + '\n');
  console.log('Saved assets/store.json');
} else console.log('Nothing changed.');
