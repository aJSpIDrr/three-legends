#!/usr/bin/env python3
"""Builds the Three Legends site: index.html, dustborn.html, dark-alliance.html.
Run from the website folder:  python3 src/build.py
Also writes src/artifact-index.html (the home page without its <html>/<head> wrapper) for the online preview."""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DISCORD = "https://discord.gg/jhuXgywS7g"
PLAY_DUSTBORN = "https://dustborn.onrender.com/"
PLAY_DA = "https://dark-alliance-play.onrender.com/"
PLAY_SVG = '<svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>'

def play_btn(url, label, cls="btn play-btn"):
    return f'<a class="{cls}" href="{url}" target="_blank" rel="noopener">{PLAY_SVG}<span>{label}</span></a>'

DISCORD_SVG = ('<svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" fill="currentColor"><path d="M20.317 4.37a19.79 19.79 0 0 0-4.885-1.515.074.074 0 0 0-.079.037c-.21.375-.444.864-.608 1.25a18.27 18.27 0 0 0-5.487 0 12.64 12.64 0 0 0-.617-1.25.077.077 0 0 0-.079-.037A19.74 19.74 0 0 0 3.677 4.37a.07.07 0 0 0-.032.027C.533 9.046-.32 13.58.099 18.057a.082.082 0 0 0 .031.057 19.9 19.9 0 0 0 5.993 3.03.078.078 0 0 0 .084-.028c.462-.63.874-1.295 1.226-1.994a.076.076 0 0 0-.041-.106 13.1 13.1 0 0 1-1.872-.892.077.077 0 0 1-.008-.128c.126-.094.252-.192.372-.291a.074.074 0 0 1 .077-.01c3.928 1.793 8.18 1.793 12.062 0a.074.074 0 0 1 .078.01c.12.098.246.198.373.292a.077.077 0 0 1-.006.127 12.3 12.3 0 0 1-1.873.892.077.077 0 0 0-.041.107c.36.698.772 1.362 1.225 1.993a.076.076 0 0 0 .084.028 19.84 19.84 0 0 0 6.002-3.03.077.077 0 0 0 .032-.054c.5-5.177-.838-9.674-3.549-13.66a.061.061 0 0 0-.031-.03zM8.02 15.33c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.956-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.956 2.418-2.157 2.418zm7.975 0c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.955-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.946 2.418-2.157 2.418z"/></svg>')

FONTS = {
    "studio": "family=Cinzel:wght@500;700&family=Chivo:wght@400;600;700&family=Chivo+Mono:wght@400;500;600",
    "dustborn": "family=Staatliches&family=Barlow+Semi+Condensed:wght@400;600;700",
    "da": "family=Grenze+Gotisch:wght@500;700;800&family=Alegreya+Sans:wght@400;500;700;800",
}

def head(title, desc, body_class, fonts):
    fam = "&".join(FONTS[f] for f in fonts)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0d0b0f">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?{fam}&display=swap">
<link rel="stylesheet" href="assets/site.css">
<link rel="icon" href="favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="64x64" href="assets/favicon-64.png">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<meta property="og:image" content="assets/three-legends-banner.webp">
</head>
<body class="{body_class}">
'''

def header(current):
    def link(href, label, key, extra=""):
        cur = ' aria-current="page"' if key == current else ""
        return f'<a href="{href}"{cur}{extra}>{label}</a>'
    return f'''<header class="top">
  <div class="wrap">
    <a class="brand" href="index.html" aria-label="Three Legends home"><img src="assets/three-legends-emblem-sm.webp" width="360" height="257" alt="Three Legends"></a>
    <nav aria-label="Main">
      {link("index.html", "Home", "home", ' class="hide-sm"')}
      {link("dustborn.html", "Dustborn", "dustborn")}
      {link("dark-alliance.html", "Dark Alliance", "da")}
      {link("index.html#contact", "Contact", "contact", ' class="hide-sm"')}
      <a class="discord" href="{DISCORD}" target="_blank" rel="noopener" aria-label="Join our Discord" title="Join our Discord">{DISCORD_SVG}</a>
    </nav>
  </div>
</header>
'''

FOOTER = f'''<footer>
  <div class="wrap">
    <a href="index.html"><img src="assets/three-legends-emblem-sm.webp" width="360" height="257" alt="Three Legends"></a>
    <nav aria-label="Footer">
      <a href="index.html">Home</a>
      <a href="dustborn.html">Dustborn</a>
      <a href="dark-alliance.html">Dark Alliance</a>
      <a href="{DISCORD}" target="_blank" rel="noopener" class="fdiscord">{DISCORD_SVG}<span>Discord</span></a>
    </nav>
    <span>© <span id="yr">2026</span> Three Legends</span>
  </div>
</footer>
<script src="assets/site.js"></script>
<script src="assets/store.js"></script>
</body>
</html>
'''

def discord_btn(label="Join our Discord", cls="btn discord-btn"):
    return f'<a class="{cls}" href="{DISCORD}" target="_blank" rel="noopener">{DISCORD_SVG}<span>{label}</span></a>'

def gal_item(src, title="", sub="", alt=None):
    alt = alt if alt is not None else (title or "Game art")
    cap = f'<span class="cap"><b>{title}</b><small>{sub}</small></span>' if title else ""
    capt = (title + (" · " + sub if sub else "")) if title else alt
    return f'<button type="button" data-full="{src}" data-cap="{capt}"><img src="{src}" alt="{alt}" loading="lazy">{cap}</button>'

def shot(src, title, text):
    return f'''<figure><button type="button" class="phone" data-full="{src}" data-cap="{title}"><img src="{src}" alt="{title} screen" loading="lazy" width="420" height="860"></button><figcaption><b>{title}</b>{text}</figcaption></figure>'''

def feats(items):
    return '<ul class="feats">' + "".join(f"<li><b>{t}</b><p>{d}</p></li>" for t, d in items) + "</ul>"

# =================================================================== HOME
home = head("Three Legends", "Three Legends: three brothers making browser RPGs. Home of Dustborn and Dark Alliance.", "studio", ["studio", "dustborn", "da"]) + header("home") + f'''
<main id="home">
  <section class="crest" aria-label="Three Legends">
    <img class="banner" src="assets/three-legends-banner.webp" srcset="assets/three-legends-banner-sm.webp 1000w, assets/three-legends-banner.webp 1672w" sizes="(max-width: 1672px) 100vw, 1672px" width="1672" height="941" alt="Three Legends: Three brothers. One legendary journey. An archer, a knight and a wizard look out over a castle under a blood-red sky, with a dragon overhead. Play, explore, conquer.">
    <div class="wrap">
      <p class="lead">We are Three Legends, a small independent studio run by three brothers. We make online RPGs that you play in your browser, on your phone or your PC. Two worlds so far, with more on the way.</p>
      <div class="btns" style="justify-content:center">
        <a class="btn" href="#games">See our games</a>
        {discord_btn(cls="btn ghost discord-btn")}
      </div>
    </div>
  </section>

  <section class="band" id="about" aria-labelledby="about-title">
    <div class="wrap">
      <div class="head">
        <p class="eyebrow">Who we are</p>
        <h2 id="about-title">Three brothers, one studio</h2>
        <p class="lead muted">We grew up playing the same games, arguing over the same bosses and trading the same loot. Now we build our own.</p>
      </div>
      <div class="who">
        <div><h3>Who we are</h3><p>Three brothers who share one studio and one goal: make games we would play ourselves. We design, write, draw and build everything in-house.</p></div>
        <div><h3>What we do</h3><p>Online role-playing games that live in your browser. No download and no install. Check in a few times a day, run missions, fight rivals and build something together with your friends.</p></div>
        <div><h3>How we work</h3><p>Every game gets its own world, its own painted art and its own rules. We put playable builds in front of players early and keep changing them based on what you tell us.</p></div>
      </div>
    </div>
  </section>

  <section class="band" id="games" aria-labelledby="games-title">
    <div class="wrap">
      <div class="head">
        <p class="eyebrow">Our games</p>
        <h2 id="games-title">Two worlds so far</h2>
      </div>
      <div class="games">
        <a class="gcard dust" href="dustborn.html">
          <img src="assets/dustborn/hero.webp" alt="" loading="lazy">
          <div class="gbody">
            <p class="meta">Game 01 · Post-apocalyptic RPG · Playtest</p>
            <h3>Dustborn</h3>
            <p>Scavenge by day. Raid by night. Trust nobody. Lead a crew across fourteen regions of wasteland, from the Outskirts to the Citadel of Ash.</p>
            <span class="go">Explore Dustborn</span>
          </div>
        </a>
        <a class="gcard dark" href="dark-alliance.html">
          <img src="assets/dark-alliance/hero.webp" alt="" loading="lazy" style="object-position:center top">
          <div class="gbody">
            <p class="meta">Game 02 · Dark fantasy RPG · In development</p>
            <h3>Dark Alliance</h3>
            <p>Master missions. Break your rivals. Raise an empire from the ash. Rise from Outcast to Legend across eight blood-soaked chapters.</p>
            <span class="go">Explore Dark Alliance</span>
          </div>
        </a>
      </div>
    </div>
  </section>

  <section class="band" aria-labelledby="pillars-title">
    <div class="wrap">
      <div class="head">
        <p class="eyebrow">In every Three Legends game</p>
        <h2 id="pillars-title">Play. Explore. Conquer.</h2>
      </div>
      <ul class="pillars">
        <li><b>Epic quests</b><span>Missions and boss fights that carry you through a whole world, region by region.</span></li>
        <li><b>Powerful loot</b><span>Weapons, rides, mounts and relics. Every upgrade shows up in your next fight.</span></li>
        <li><b>Climb the ranks</b><span>Leaderboards, titles and trophies for the players who keep pushing.</span></li>
        <li><b>Join a community</b><span>Crews, alliances, chat and bounties. You are never playing alone.</span></li>
        <li><b>Play anywhere</b><span>Runs in the browser on phone and PC. Pick up where you left off.</span></li>
      </ul>
    </div>
  </section>

  <section class="band" id="contact" aria-labelledby="contact-title">
    <div class="wrap split">
      <div class="stack">
        <p class="eyebrow">Contact</p>
        <h2 id="contact-title" style="font-family:var(--f-display);font-size:clamp(2rem,4.4vw,3.2rem)">Come say hello</h2>
        <p class="lead muted">The fastest way to reach us is our Discord. Ask questions, report bugs, share ideas and hear about new builds first.</p>
        <div class="btns">{discord_btn()}</div>
      </div>
      <form id="contact-form" novalidate>
        <label for="c-name">Name<input id="c-name" name="name" autocomplete="name"></label>
        <label for="c-email">Email<input id="c-email" name="email" type="email" autocomplete="email" required></label>
        <label for="c-msg">Message<textarea id="c-msg" name="message"></textarea></label>
        <button class="btn" type="submit">Send</button>
        <p class="note" id="contact-note" role="status"></p>
      </form>
    </div>
  </section>
</main>
''' + FOOTER

# =================================================================== DUSTBORN
regions = [
    (1, "The Outskirts", "Operation Junk King", "junk"), (6, "Rust Flats", "Operation Rustjaw", "rustjaw"),
    (14, "Drowned Mall", "Operation Undertow", "undertow"), (22, "Ash Highway", "Operation Warlord", "warlord"),
    (30, "Glass Crater", "Operation Maw", "maw"), (40, "Sunken Rail Yards", "The Iron Conductor", "conductor"),
    (55, "The Bone Fields", "The Marrow King", "marrow"), (70, "Cinder Refinery", "Furnace Mother", "furnace"),
    (85, "Storm Coast", "The Drowned Admiral", "admiral"), (100, "Iron Necropolis", "The Gravewarden", "gravewarden"),
    (120, "Rad Jungle", "Mother Bloom", "bloom"), (140, "The Sky Wrecks", "Cinderwing", "cinderwing"),
    (160, "Black Glass Desert", "The Mirage", "mirage"), (180, "Citadel of Ash", "The Ash Emperor", "emperor"),
]
route_db = "".join(f'<li><span class="lv">Lv<b>{lv}</b></span><img src="assets/dustborn/boss_{k}.webp" alt="{b}" loading="lazy"><span class="nm">{n}<small>Boss: {b}</small></span></li>' for lv, n, b, k in regions)

dust = head("Dustborn · Three Legends", "Dustborn: a post-apocalyptic online RPG by Three Legends. Scavenge by day. Raid by night. Trust nobody.", "dustborn", ["studio", "dustborn"]) + header("dustborn") + f'''
<main>
  <section class="ghero" aria-labelledby="db-title">
    <img class="bg" src="assets/dustborn/hero.webp" alt="" fetchpriority="high">
    <div class="wrap">
      <p class="eyebrow">Game 01 · A Three Legends game</p>
      <h1 id="db-title">Dustborn</h1>
      <p class="tagline">Scavenge by day. Raid by night. Trust nobody.</p>
      <div class="facts"><span>Post-apocalyptic RPG</span><span>Online multiplayer</span><span>Phone &amp; PC browser</span><span>Status: playtest</span></div>
      <div class="btns">{play_btn(PLAY_DUSTBORN, "Play Dustborn")}<a class="btn ghost" href="#screens">See it in action</a>{discord_btn(cls="btn ghost discord-btn")}</div>
      <p class="playnote">Free in your browser on phone or PC. No download needed.</p>
    </div>
  </section>

  <section class="band" aria-labelledby="db-about">
    <div class="wrap split">
      <div class="stack">
        <p class="eyebrow">The game</p>
        <h2 id="db-about" style="font-family:var(--f-display);font-weight:400;font-size:clamp(2rem,4.4vw,3.2rem)">The old world is buried. You were born on top of it.</h2>
        <p class="lead">Dustborn is an online RPG set in a burned-out wasteland. You lead a crew of scavengers, take jobs for caps and salvage, and fight your way through fourteen regions, each one guarded by a boss.</p>
        <p class="muted">Other players are out there too. Raid their camps for caps, put a price on their heads, or team up to bring down the roaming hordes. Build outposts that earn while you sleep, and turn salvage into guns and war rigs at the Workbench.</p>
      </div>
      <button type="button" class="phone" style="border-radius:18px;cursor:zoom-in" data-full="assets/dustborn/scene_rust_sunset.webp" data-cap="Rust sunset over the wasteland"><img src="assets/dustborn/scene_rust_sunset.webp" alt="A rusted wasteland at sunset" style="aspect-ratio:16/10;object-fit:cover"></button>
    </div>
  </section>

  <section class="band" aria-labelledby="db-play">
    <div class="wrap">
      <div class="head"><p class="eyebrow">How it plays</p><h2 id="db-play">Life in the wastes</h2></div>
      {feats([
        ("Jobs", "Jobs cost energy and pay caps, XP and salvage. Each has its odds; if it goes wrong you lose a little health. Run a job 3 or 10 times in one go, master it for a salvage reward, and clear a whole region for a big payout."),
        ("Your crew", "Everyone in your crew carries one of your guns and one of your rides, best first. Hire drifters or bring friends to grow."),
        ("Raids", "From level 4, spend ammo to raid other crews. Your attack against their defense, plus a little luck, decides it. Winners take part of the loser's unprotected caps."),
        ("Wanted wall", "Pay to post a crew on the wall. Anyone who knocks them out claims the reward, whatever their level."),
        ("Roaming hordes", "Hordes show up for a few hours and only fight crews in their level range. Top damage dealers and whoever lands the final blow earn scrip."),
        ("Outposts", "Outposts earn every hour, even while you are offline, until they fill up. Upgrade your safe to protect more of your caps."),
        ("Workshop & Bazaar", "Buy gear from the Trader, build stronger gear at the Workbench from region blueprints, or buy rare tech with scrip."),
        ("Every day", "Spin the Scav Wheel, check in to grow your streak, and finish two daily jobs for scrip."),
      ])}
    </div>
  </section>

  <section class="band store" id="store" aria-labelledby="db-store">
    <div class="wrap" data-store="dustborn">
      <div class="head"><p class="eyebrow">Store</p><h2 id="db-store">Get scrip</h2><p class="muted">Scrip packs you can buy in the game. Optional: everything in Dustborn can also be earned by playing.</p><p class="store-status" role="status"></p></div>
      <div class="store-grid"></div>
      <p class="store-note muted"></p>
    </div>
  </section>

  <section class="band" id="screens" aria-labelledby="db-shots">
    <div class="wrap">
      <div class="head"><p class="eyebrow">In-game</p><h2 id="db-shots">Screenshots</h2><p class="muted">Taken from the current playtest build. Tap a screen to see it larger.</p></div>
      <div class="shots">
        {shot("assets/shots/db_gate.webp", "Sign in", "Enter the wastes from any browser.")}
        {shot("assets/shots/db_camp.webp", "Camp", "Your home base: daily wheel, check-ins, alerts and every part of the game.")}
        {shot("assets/shots/db_jobs.webp", "Jobs", "Pick a job, check the odds, run it once or ten times.")}
        {shot("assets/shots/db_outposts.webp", "Outposts", "Buy settlements that earn caps every hour.")}
        {shot("assets/shots/db_bazaar.webp", "The Bazaar", "Rare gear for scrip and grit.")}
        {shot("assets/shots/db_wanted.webp", "Wanted wall", "Put a price on a rival crew.")}
        {shot("assets/shots/db_workshop.webp", "Workshop", "Guns, blades and rides from the Trader and the Workbench.")}
        {shot("assets/shots/db_crew.webp", "Crew profile", "Your stats, titles, banner and history.")}
      </div>
    </div>
  </section>

  <section class="band" aria-labelledby="db-route">
    <div class="wrap">
      <div class="head"><p class="eyebrow">The road ahead</p><h2 id="db-route">Fourteen regions, fourteen bosses</h2><p class="muted">Each region unlocks at a level and ends with a boss who guards Workbench blueprints.</p></div>
      <ol class="route">{route_db}</ol>
    </div>
  </section>

  <section class="band" aria-labelledby="db-art">
    <div class="wrap stack" style="gap:40px">
      <div class="head" style="margin:0"><p class="eyebrow">Art</p><h2 id="db-art">The wasteland, painted</h2></div>
      <div class="stack"><h3 class="eyebrow">Places</h3>
        <div class="gal">
          {gal_item("assets/dustborn/scene_dust_dawn.webp", "Dust Dawn")}
          {gal_item("assets/dustborn/scene_red_canyon.webp", "Red Canyon")}
          {gal_item("assets/dustborn/scene_frost_line.webp", "Frost Line")}
          {gal_item("assets/dustborn/scene_glass_storm.webp", "Glass Storm")}
          {gal_item("assets/dustborn/scene_maw_walker.webp", "Maw Walker")}
          {gal_item("assets/dustborn/scene_neon_ruins.webp", "Neon Ruins")}
          {gal_item("assets/dustborn/scene_violet_hour.webp", "Violet Hour")}
          {gal_item("assets/dustborn/market.webp", "The Market")}
        </div>
      </div>
      <div class="stack"><h3 class="eyebrow">Bosses</h3>
        <div class="gal tall">
          {gal_item("assets/dustborn/boss_junk.webp", "Junk King", "The Outskirts")}
          {gal_item("assets/dustborn/boss_conductor.webp", "The Iron Conductor", "Sunken Rail Yards")}
          {gal_item("assets/dustborn/boss_admiral.webp", "The Drowned Admiral", "Storm Coast")}
          {gal_item("assets/dustborn/boss_emperor.webp", "The Ash Emperor", "Citadel of Ash")}
        </div>
      </div>
      <div class="stack"><h3 class="eyebrow">Outposts</h3>
        <div class="gal three">
          {gal_item("assets/dustborn/outpost_scrap_stall.webp", "Scrap Stall")}
          {gal_item("assets/dustborn/outpost_water_still.webp", "Water Still")}
          {gal_item("assets/dustborn/outpost_mushroom_farm.webp", "Mushroom Farm")}
          {gal_item("assets/dustborn/outpost_fuel_refinery.webp", "Fuel Refinery")}
          {gal_item("assets/dustborn/outpost_dam_fortress.webp", "Dam Fortress")}
          {gal_item("assets/dustborn/outpost_airship_dock.webp", "Airship Dock")}
        </div>
      </div>
      <div class="stack"><h3 class="eyebrow">Roaming hordes</h3>
        <div class="gal square">
          {gal_item("assets/dustborn/horde_ash_legion.webp", "The Ash Legion")}
          {gal_item("assets/dustborn/horde_rail_wraiths.webp", "Rail Wraiths")}
          {gal_item("assets/dustborn/horde_mutant_horde.webp", "Mutant Horde")}
          {gal_item("assets/dustborn/horde_stormbrood.webp", "Stormbrood")}
        </div>
      </div>
      <div class="stack"><h3 class="eyebrow">Guns &amp; rides</h3>
        <div class="gal square">
          {gal_item("assets/dustborn/gear_war_rig.webp", "War Rig")}
          {gal_item("assets/dustborn/gear_rust_buggy.webp", "Rust Buggy")}
          {gal_item("assets/dustborn/gear_sand_dread.webp", "War Mammoth")}
          {gal_item("assets/dustborn/gear_land_crawler.webp", "Land Crawler")}
          {gal_item("assets/dustborn/gear_gyrocopter.webp", "Scrap Gyrocopter")}
          {gal_item("assets/dustborn/gear_combat_shotgun.webp", "Combat Shotgun")}
          {gal_item("assets/dustborn/gear_gauss_cannon.webp", "Gauss Cannon")}
          {gal_item("assets/dustborn/gear_chain_cleaver.webp", "Chain Cleaver")}
        </div>
      </div>
    </div>
  </section>

  <section class="strip"><div class="wrap"><p>The wasteland is waiting. Join the playtest crew.</p><div class="btns">{play_btn(PLAY_DUSTBORN, "Play Dustborn", "btn play-btn dark")}{discord_btn()}</div></div></section>
</main>
''' + FOOTER

# =================================================================== DARK ALLIANCE
chapters = [
    (1, "Outcast", "The Ashen Mire", "the Mire Hag"), (5, "Sellsword", "Gallowmere", "Hangman Vorl"),
    (12, "Reaver", "Thornwood", "the Antlered Mother"), (20, "Knight", "The Black Abbey", "Abbot Malachar"),
    (30, "Warden", "Ironfang Pass", "the Pale Giant"), (42, "Champion", "The Drowned Keep", "the Admiral of the Deep"),
    (55, "Dreadlord", "The Cinder Wastes", "the Ember Wyrm"), (70, "Legend", "The Throne of Night", "the Hollow King"),
]
route_da = "".join(f'<li><span class="lv">Lv<b>{lv}</b></span><img src="assets/dark-alliance/boss_{i}.webp" alt="{b[0].upper() + b[1:]}" loading="lazy"><span class="nm">{n}: {p}<small>Boss: {b}</small></span></li>' for i, (lv, n, p, b) in enumerate(chapters))

classes = [
    ("Knight", "Oathbound", "Defence force +15% and maximum health +15%."),
    ("Reaver", "Plunder", "Attack force +15% and 15% more gold from missions, victories and bounties."),
    ("Warlock", "Ever-Burning", "Energy and stamina return a third faster."),
    ("Revenant", "Undying", "Wounds close three times as fast, and the bonesetter charges half."),
]
cls_html = "".join(f'<article class="cls"><img src="assets/dark-alliance/class_{i}.webp" alt="{n}" loading="lazy"><div><h3>{n}</h3><span class="boon">{b}</span><p>{d}</p></div></article>' for i, (n, b, d) in enumerate(classes))

da = head("Dark Alliance · Three Legends", "Dark Alliance: a dark fantasy online RPG by Three Legends. Master missions. Break your rivals. Raise an empire from the ash.", "da", ["studio", "da"]) + header("da") + f'''
<main>
  <section class="ghero" aria-labelledby="da-title">
    <img class="bg" src="assets/dark-alliance/hero.webp" alt="" fetchpriority="high">
    <div class="wrap">
      <p class="eyebrow">Game 02 · A Three Legends game</p>
      <h1 id="da-title">Dark Alliance</h1>
      <p class="tagline">Master missions. Break your rivals. Raise an empire from the ash.</p>
      <div class="facts"><span>Dark fantasy RPG</span><span>Clans, sieges &amp; world bosses</span><span>Phone &amp; PC browser</span><span>Status: in development</span></div>
      <div class="btns">{play_btn(PLAY_DA, "Play Dark Alliance")}<a class="btn ghost" href="#screens">See it in action</a>{discord_btn(cls="btn ghost discord-btn")}</div>
      <p class="playnote">Free in your browser on phone or PC. No download needed. The first visit can take up to a minute while the realm wakes up.</p>
    </div>
  </section>

  <section class="band" aria-labelledby="da-about">
    <div class="wrap split">
      <div class="stack">
        <p class="eyebrow">The game</p>
        <h2 id="da-about" style="font-family:var(--f-display);font-weight:800;font-size:clamp(2.2rem,4.6vw,3.4rem)">Name your lord. Raise your banner.</h2>
        <p class="lead">Dark Alliance is an online RPG set in a gothic world of plague roads, drowned keeps and burning saints. You start as an Outcast in the Ashen Mire and fight your way up to the Throne of Night.</p>
        <p class="muted">Every mission pays gold and experience. Every battle is won by the lords who stand behind you, so you build an alliance, arm it, and lead it into battle against rival houses. Buy land for steady income, hide your gold in the vault, and hunt down the lords with a price on their heads.</p>
      </div>
      <button type="button" class="phone" style="border-radius:6px;cursor:zoom-in" data-full="assets/dark-alliance/scene_loc1.webp" data-cap="A castle under a blood-red sky"><img src="assets/dark-alliance/scene_loc1.webp" alt="A dark castle under a blood-red sky" style="aspect-ratio:16/10;object-fit:cover"></button>
    </div>
  </section>

  <section class="band" aria-labelledby="da-classes">
    <div class="wrap">
      <div class="head"><p class="eyebrow">Choose a sigil</p><h2 id="da-classes">Four paths to power</h2><p class="muted">Your sigil gives you one lasting boon for the whole game.</p></div>
      <div class="classes">{cls_html}</div>
    </div>
  </section>

  <section class="band" aria-labelledby="da-play">
    <div class="wrap">
      <div class="head"><p class="eyebrow">How it plays</p><h2 id="da-play">Five places to go</h2><p class="muted">Everything in the game sits under five tabs: Home, Battle, Shop, Allies and Hero.</p></div>
      {feats([
        ("Home", "The Realm shows your lord, live events and everything happening around you. Missions and Updates sit right beside it."),
        ("Missions", "Eight chapters with five missions each. Missions cost energy and pay XP and gold. Master each one three times over, then face the chapter boss to open the road ahead."),
        ("Battle", "Fight rival lords for their gold, hunt marked lords on the Bounty board, and join the realm against the World Boss, the Invasion and the Tourney."),
        ("Shop", "Items, Relics and Equipment for every lord you lead, land and buildings for your Empire, blessings at the Altar, and the Vault to keep your gold safe."),
        ("Allies", "Found or join a clan, chat live, fill the clan treasury, upgrade the Training Grounds and take on Clan Sieges together. Climb the Ranking with your Alliance."),
        ("Hero", "Your lord, your stats and your sigil. Spend your points and shape how you fight."),
        ("World events", "World Bosses arrive on a timer, Invasions and Tourneys run live, and Clan Sieges pit your whole clan against titans like Ymrak the Frost Titan."),
        ("Empire income", "Your lands pay gold every hour. Keep upkeep below income, collect often, and bank what you can before a rival takes it."),
      ])}
      <div class="stack" style="margin-top:28px"><h3 class="eyebrow">Attack abilities: choose two before every fight</h3>
        <ul class="chips"><li>Bloodlust</li><li>Plunder</li><li>Hex</li><li>Ward</li><li>Ruin <span>· level 20</span></li><li>Leech <span>· level 25</span></li><li>Retribution <span>· level 30</span></li></ul>
      </div>
    </div>
  </section>

  <section class="band store" id="store" aria-labelledby="da-store">
    <div class="wrap" data-store="dark-alliance">
      <div class="head"><p class="eyebrow">Store</p><h2 id="da-store">The Store</h2><p class="muted">Soul shards, gold and perks you can buy in the game. Optional: you can play the whole game for free.</p><p class="store-status" role="status"></p></div>
      <div class="store-grid"></div>
      <p class="store-note muted"></p>
    </div>
  </section>

  <section class="band" id="screens" aria-labelledby="da-shots">
    <div class="wrap">
      <div class="head"><p class="eyebrow">In-game</p><h2 id="da-shots">Screenshots</h2><p class="muted">From the current build of the game. Tap a screen to see it larger.</p></div>
      <div class="shots">
        {shot("assets/shots/da_realm.webp", "Home: the Realm", "Your lord, live events and everything happening in the realm.")}
        {shot("assets/shots/da_news.webp", "Empire & news", "Collect your hourly gold, read updates and strike back at rivals.")}
        {shot("assets/shots/da_battle.webp", "Battle", "Pick two abilities, then choose your target.")}
        {shot("assets/shots/da_items.webp", "Shop: Items", "Weapons, mounts, retainers and dark arts for every lord you lead.")}
        {shot("assets/shots/da_clan.webp", "Allies: Clan", "Clan chat, a shared treasury and clan upgrades.")}
      </div>
    </div>
  </section>

  <section class="band" aria-labelledby="da-route">
    <div class="wrap">
      <div class="head"><p class="eyebrow">The road to the throne</p><h2 id="da-route">Eight chapters, eight bosses</h2><p class="muted">From the plague roads of the Ashen Mire to the Throne of Night.</p></div>
      <ol class="route">{route_da}</ol>
    </div>
  </section>

  <section class="band" aria-labelledby="da-art">
    <div class="wrap stack" style="gap:40px">
      <div class="head" style="margin:0"><p class="eyebrow">Art</p><h2 id="da-art">Painted in blood and ash</h2></div>
      <div class="stack"><h3 class="eyebrow">Places</h3>
        <div class="gal">
          {gal_item("assets/dark-alliance/scene_loc0.webp", "Gallowmere", alt="A gothic town by a river")}
          {gal_item("assets/dark-alliance/scene_s2b_0.webp", "The Cinder Wastes", alt="A city burning under red skies")}
          {gal_item("assets/dark-alliance/scene_s1b_1.webp", "Ironfang Pass", alt="Frozen spires under a blue night")}
          {gal_item("assets/dark-alliance/scene_s1c_4.webp", "Thornwood", alt="A green haunted forest")}
          {gal_item("assets/dark-alliance/scene_s2a_1.webp", "The Black Abbey", alt="A violet gothic abbey")}
          {gal_item("assets/dark-alliance/scene_s3_1.webp", "The Ashen Mire", alt="A ruined bridge and broken walls")}
          {gal_item("assets/dark-alliance/scene_s2b_3.webp", "The Throne of Night", alt="Black towers under the moon")}
          {gal_item("assets/dark-alliance/scene_s1b_3.webp", "The Drowned Keep", alt="A dark keep on a cliff")}
        </div>
      </div>
      <div class="stack"><h3 class="eyebrow">Bosses</h3>
        <div class="gal square">
          {gal_item("assets/dark-alliance/boss_0.webp", "The Mire Hag", "Chapter 1")}
          {gal_item("assets/dark-alliance/boss_2.webp", "The Antlered Mother", "Chapter 3")}
          {gal_item("assets/dark-alliance/boss_3.webp", "Abbot Malachar", "Chapter 4")}
          {gal_item("assets/dark-alliance/boss_4.webp", "The Pale Giant", "Chapter 5")}
          {gal_item("assets/dark-alliance/boss_5.webp", "The Admiral of the Deep", "Chapter 6")}
          {gal_item("assets/dark-alliance/boss_6.webp", "The Ember Wyrm", "Chapter 7")}
          {gal_item("assets/dark-alliance/boss_7.webp", "The Hollow King", "Chapter 8")}
          {gal_item("assets/dark-alliance/boss_1.webp", "Hangman Vorl", "Chapter 2")}
        </div>
      </div>
      <div class="stack"><h3 class="eyebrow">The realm</h3>
        <div class="gal square">
          {gal_item("assets/dark-alliance/art_tl_all.webp", "Alliance")}
          {gal_item("assets/dark-alliance/art_tl_inv.webp", "Invasion")}
          {gal_item("assets/dark-alliance/art_tl_tou.webp", "Tourney")}
          {gal_item("assets/dark-alliance/art_tl_vau.webp", "Vault")}
          {gal_item("assets/dark-alliance/art_tl_bat.webp", "Battle")}
          {gal_item("assets/dark-alliance/art_tl_cla.webp", "Clan")}
          {gal_item("assets/dark-alliance/art_tl_alt.webp", "Altar")}
          {gal_item("assets/dark-alliance/art_tl_hea.webp", "Heal")}
        </div>
      </div>
      <div class="stack"><h3 class="eyebrow">Foes &amp; relics</h3>
        <div class="gal square">
          {gal_item("assets/dark-alliance/foe_e0_1.webp", "Bog ghouls")}
          {gal_item("assets/dark-alliance/foe_e4_4.webp", "Frost bear")}
          {gal_item("assets/dark-alliance/foe_e7_2.webp", "Mirror legion")}
          {gal_item("assets/dark-alliance/foe_e4_3.webp", "Frost reaver")}
          {gal_item("assets/dark-alliance/art_ixw.webp", "Blood blade")}
          {gal_item("assets/dark-alliance/art_ixa.webp", "Grimoire")}
          {gal_item("assets/dark-alliance/art_ixm.webp", "Bone carriage")}
          {gal_item("assets/dark-alliance/art_ixr.webp", "Crimson relic")}
        </div>
      </div>
    </div>
  </section>

  <section class="strip"><div class="wrap"><p>Glory goes to the bold. Join the alliance.</p><div class="btns">{play_btn(PLAY_DA, "Play Dark Alliance", "btn play-btn dark")}{discord_btn()}</div></div></section>
</main>
''' + FOOTER

pages = {"index.html": home, "dustborn.html": dust, "dark-alliance.html": da}
for name, html in pages.items():
    open(os.path.join(ROOT, name), "w").write(html)

# Preview copy of the home page without the document wrapper (the preview host adds its own).
inner = re.sub(r"^<!doctype html>\s*<html[^>]*>\s*<head>\s*<meta charset=\"utf-8\">\s*<meta name=\"viewport\"[^>]*>\s*", "", home)
inner = inner.replace("</head>\n<body class=\"studio\">\n", "<script>document.body.classList.add('studio')</script>\n", 1).replace("</body>\n</html>\n", "")
open(os.path.join(ROOT, "src", "artifact-index.html"), "w").write(inner)
print("built", list(pages))
