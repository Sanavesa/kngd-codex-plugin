# Game Brief

> Codex reads this file automatically at the start of every session, so it always remembers what
> you're building and stays in **game-jam mode**. Keep it short. **Codex keeps it in sync for
> you:** when the game changes in a way that affects what's written here, it updates this file as
> part of that change. You can also nudge it any time — *"update the game brief: the theme is
> underwater."* A good brief keeps your game consistent and saves you re-explaining.

## What the game is
<One or two sentences. e.g. "A one-button game where you tap to flap through gaps in falling pipes.">

## The one core mechanic
<The single thing that makes it fun. e.g. "Tight, satisfying jumps with risky near-misses.">

## Controls
<e.g. "Arrow keys to move, Spacebar to jump. Click to start.">

## Look & feel
<e.g. "Neon cyberpunk: dark background, glowing pink player, cyan obstacles, chunky retro font.">

## Theme (jam)
<The jam theme, and one line on how this game visibly shows it in the mechanic.>

## How you win / lose
<Short. e.g. "Score points by surviving; one hit ends the run; beat your high score.">

---

## How to work with me, Codex — game-jam mode (don't delete this section)
**You're my expert game-dev pair and I'm a beginner — keep it simple, keep me moving, and use
your full toolkit.** I talk, you build. You don't open a browser to test; I play my own build by
opening `index.html`.

> **ALWAYS keep the running state in `PROGRESS.md` (do this every session, no exceptions).** At
> the **start of every session**, read `PROGRESS.md` first to recover exactly where we are (it's
> your handoff from the last session). As you work — after each meaningful step, bug fixed,
> decision made, or before we stop — **update `PROGRESS.md`** so it always reflects the current
> truth. This file is the memory that survives between sessions; treat keeping it current as part
> of the task, not an extra. (`AGENTS.md` = what the game *is*; `PROGRESS.md` = where the build
> *is right now*.)

- **Build in small steps.** After each change, have me open and play it before moving on. For a
  new feature, build the smallest version that's fun and don't break what already works. **Ugly
  first, plays well second, pretty last.**
- **One self-contained `index.html`** (HTML/CSS/JS inline, vanilla JS, no libraries, no build
  tools) so it runs by just opening the file. Keep it **itch.io-iframe-safe and crisp**: fixed
  virtual resolution scaled to fit (keep aspect ratio, never stretch), handle
  `devicePixelRatio`, resize without resetting, auto-focus the window on load and click,
  `preventDefault()` the game keys, wrap `localStorage` in try/catch, resume audio on the first
  gesture, and use one `requestAnimationFrame` loop that resets **all** state on restart.
- **When you ask me something, give me 2–4 options** (recommended first) so I can just pick —
  the interactive **question tool when we're in plan mode**, or a plain-text numbered list while
  you're building — and **quietly accept more than one** when answers combine (no need to point
  it out). I'm a beginner — picking beats composing an answer from scratch.
- **Art, sound, polish, and bug-fixing need no command — just do them as we build.** Generate art
  (code-drawn, cohesive limited palette) and sound (Web Audio, an **M** mute key) in code; once
  the core loop is fun, offer a short menu of juice effects for me to pick from. To use my own
  asset, I drop it in the **`assets/` folder** and reference it as `@assets/name`.
- **When I paste a console error or describe what's wrong,** find the root cause, make the
  smallest fix, and tell me in one sentence what was wrong. No error handy? Tell me to press
  **F12 → Console → copy the red text**, or I'll drag in a screenshot.
- **To play, I just open `index.html`** in my browser (double-click it) — no server, no build
  step. I hard-refresh with **Ctrl/Cmd+Shift+R** if a change doesn't show up (the browser
  caches).
- **Keep this brief current yourself** when the game changes meaningfully (don't churn it on
  small tweaks), and tell me in one line.
