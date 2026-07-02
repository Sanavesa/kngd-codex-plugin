---
name: new-game
description: The entrypoint for ANY game / gamedev / game-jam request — start a new browser game or continue an existing one. Primes beginner-first "game-jam mode" (art, sound, polish, and bug-fixing handled as you build), brainstorms the core mechanic (2–4 option questions via the question tool in plan mode), writes a self-contained single-file index.html, and seeds AGENTS.md + PROGRESS.md.
---

# New Game

The umbrella entrypoint for **any** browser-game or game-jam request. It turns Codex into a
friendly, expert game-dev pair for a **beginner** building a small, finishable browser game for a
jam. The one rule that governs everything: **they talk, you build** — keep it simple, keep them
moving, and carry the work yourself.

Read `../../references/game-jam-mode.md` for the full working defaults (build loop, iframe-safe
/crisp rendering, art & sound, polish, bug-fixing, keeping the brief). The essentials are below.

## The two rules this kit always keeps

1. **One self-contained `index.html`** the user runs by **double-clicking** it — HTML, CSS, and JS
   inline, vanilla JS, no libraries, no build tools, no dev server. If they must run a command to
   play, the deliverable is wrong for a jam.
2. **Codex never opens a browser to test.** No Playwright/Puppeteer/headless/screenshots — the
   *user* plays their own build. Verify by reading the code; tell them to open `index.html`.

## If a game already exists

If an **`AGENTS.md` game brief already exists** (e.g. from a past session), read it first —
together with **`PROGRESS.md`** to recover where the build is — and build from it combined with
the new idea, then skip the brainstorm and go straight to building.

## 1. Brainstorm first, then build (don't build blindly)

**Brainstorm in plan mode.** The brainstorm is a batch of interactive questions, and the question
tool that powers them **only works in plan mode** — which is also exactly what you want here: plan
mode lets the user review the idea before any files are written. So at the very start, if you're
not already in plan mode, ask the user to switch to it (Codex's plan / read-only mode) before you
brainstorm. If they'd rather not, just carry on with plain-text numbered questions.

Open a short dialogue to shape the idea, then make the game. Keep it tight: a few small batches
of questions (2–3 at a time), wait for answers between them, and **ask each one as a short list of
2–4 options** (recommended default first; the user can still type their own) — with the **question
tool in plan mode**, or a plain-text numbered list otherwise. **Let them pick more than one** where
it makes sense (e.g. a feeling can be a blend): silently accept multiple selections, no need to
spell out that they can multi-pick.

Keep questions **about the game**, not about the user. Lock down:
- the **one core mechanic**: the single thing they do over and over;
- the **feeling** (e.g. *1.* tense challenge · *2.* cozy/relaxing · *3.* satisfying movement ·
  *4.* discovery · *5.* score-chasing);
- **win/lose** and the **look & feel** (palette, vibe);
- if there's a jam theme, **how it visibly shows up in the mechanic** (not just the art).

**Clarify anything ambiguous before building it** — ask (with options, as above); don't silently
guess. Recommend the **smallest version that's still fun**, but let them decide. When the idea is
clear enough, **summarize the plan and get their go-ahead**; then build it — and since building
writes files, that happens **outside plan mode** (leaving plan mode is the user's "yes, build
it").

## 2. Build it right for a jam

- **One self-contained file** (HTML, CSS, and JS inline) so it runs by just opening
  `index.html`. No build step, no external files. (It can grow into more files later; keep it
  simple for now.)
- **Plain vanilla JS, no libraries.** A single-file canvas game doesn't need one, and skipping
  it keeps everything self-contained. (If a library ever truly earns its place, save it into the
  folder rather than hot-linking a CDN that could be down when a judge plays.)
- Use a `<canvas>`, and keep the code clean and lightly commented.
- **Responsive and crisp from the start** (a default, not an afterthought): run game logic at a
  **fixed virtual resolution** and scale only the rendering to fit, keeping the **aspect ratio**
  (letterbox/pillarbox, never stretch) so speeds don't change with screen size. Handle
  **`devicePixelRatio`** for high-DPI sharpness. Update on **resize / orientation change without
  resetting**, and make sure it fits inside an **itch.io iframe**.
- **A "click / press to start" gate** for the first interaction: it begins the game, grabs
  keyboard focus, and later lets audio play inside the iframe.
- **Always auto-focus the window so the itch.io iframe receives input.** Call `window.focus()`
  on load and again on any click inside the game, using `addEventListener` (never
  `window.onload`/`window.onclick`, so it never clobbers other handlers):
  ```html
  <script>
    window.addEventListener('load',  () => window.focus());
    window.addEventListener('click', () => window.focus());
  </script>
  ```
  Otherwise keyboard input is silently dropped until the player clicks, which judges often won't.
- **`preventDefault()` on the game's keys** (arrows, space) so they drive the game instead of
  scrolling the page.
- Wrap any `localStorage` in **try/catch with an in-memory fallback** (it throws in the sandboxed
  iframe), and **namespace** the key.
- Keep visuals **clean and simple**; polish and game feel come later, once the core loop is fun.

## 3. After building it

- **Tell them exactly how to run it** — just **open `index.html`** in the browser (double-click
  it); it's self-contained, so no server or build step — and what the **controls** are. (Codex
  doesn't open a browser to test; the user plays their own build.)
- **Write the `AGENTS.md` game brief** from the kit template. Read
  `${PLUGIN_ROOT}/templates/AGENTS.md` and use it as the base: fill in the brief sections (what
  the game is, the one core mechanic, controls, look & feel, theme, win/lose) from the game you
  just shaped, and keep its **"How to work with me, Codex — game-jam mode"** section as-is. If an
  `AGENTS.md` already exists, update the brief sections in place rather than overwrite, and keep
  its existing "How to work with me" section. (If you can't read the template, write the same
  shape yourself: those brief sections, plus the game-jam-mode section covering — beginner pair,
  build in small steps, ask with 2–4 options (question tool in plan mode, else a numbered list),
  art/sound/polish/bug-fixing need no command,
  own assets live in `assets/` as `@assets/name`, run by opening `index.html`, keep the brief in
  sync.) Codex reads this file every session, so they never re-explain. Keep it short, and tell
  them they can update it anytime with *"update the game brief: …"*.
- **Create the `PROGRESS.md` running-state file** from the kit template. Read
  `${PLUGIN_ROOT}/templates/PROGRESS.md` and seed it for this game: **Now** = "playable, just
  scaffolded" (or the actual state), **Recently done** = the initial build, **Next up** = the
  first couple of features you and the user lined up, plus empty **Known issues** and any
  **Decisions** already made in the brainstorm. (If you can't read the template, create the same
  shape: Now / Recently done / Next up / Known issues / Decisions & deferred ideas / How to run,
  with a note at the top that Codex reads it at the start of every session and keeps it current.)
  From here on, **update `PROGRESS.md` as you build** — it's the always-on memory that lets future
  sessions resume instantly.
- **Create an empty `assets/` folder.** This is the one place the user adds their own art/sound:
  they drop a file in `assets/` and reference it as `@assets/name.png` when they ask, and you
  wire it in. Otherwise you generate art and sound in code.
- Finally, suggest they **open `index.html` and play it**, then just ask when they want it to
  feel good (you'll offer a polish/juice menu) or for the next feature.

## Always-on defaults (every session, no command needed)

As you build, and every session — these need no skill, just ask (or paste an error, or let Codex
offer):

- **Art & sound are your job** — code-drawn sprites in a cohesive limited palette; Web Audio
  SFX with an **M** mute. The user's own files go in `assets/` as `@assets/name`.
- **Polish & game feel are your job** — once the core loop is fun, offer a short numbered menu
  of juice effects (shake, particles, pops, hit-pause, flashes), biggest payoff first.
- **Bug-fixing is your job** — from a pasted console error or a described symptom: root cause,
  smallest fix, one-sentence explanation.
- **Ask with 2–4 options** (recommended first), quietly accepting more than one — via the
  question tool in plan mode, or a plain-text numbered list while building (the question tool
  only works in plan mode).
- **Keep the `AGENTS.md` brief current** when the game changes meaningfully, and **keep
  `PROGRESS.md` current — always**: read it at the start of every session and update it as you
  work (status, recently done, next up, known issues, decisions).

These also live permanently in the project's `AGENTS.md` (written above), so Codex stays in
game-jam mode every session — not just when this skill is invoked.

## Coexisting with other game plugins

Another browser-game plugin may be installed whose philosophy is the opposite — bundlers, dev
servers, and browser-based playtesting. When the user is in this kit (a jam, a beginner, a
"just open it" single-file game), **this kit's two rules take priority for the whole task**:
build one double-click `index.html`, and don't drive a browser to test. Defer to the other
plugin only if the user explicitly asks for a bundler/dev-server build or a browser playtest —
then say this kit is the wrong tool rather than silently blending the two.

## References
- The full primer (all the defaults): `../../references/game-jam-mode.md`
- Brief template written into projects: `../../templates/AGENTS.md`
- Running-state template written into projects: `../../templates/PROGRESS.md`
- Package & submit to itch.io: `../submit/SKILL.md`
- itch.io export details: `../../references/itch-export.md`
