---
name: submit
description: Package the game for an itch.io jam submission — produce the upload-ready zip (index.html at the archive root) and print the publishing checklist. Prepares the files only; it does not write the itch.io page copy. Use when the user wants to submit, upload, export, or ship their game to itch.io or a game jam.
---

# Submit (itch.io Export)

Get the user's game **files** ready to submit to the itch.io jam: produce the upload-ready
**zip** and the **checklist**. This skill prepares the game for upload only — it does **not**
write the itch.io page copy (premise, features, credits); the user fills that in themselves on
itch. Read `../../references/itch-export.md` for the itch specifics (zip layout, iframe/embed
settings). Codex verifies the build by reading it — the *user* plays their own build; don't drive
a browser.

## 1. Quick pre-flight

- Make sure the game actually runs (no console errors). If it hasn't been played recently, remind
  the user to **open `index.html` and play a full round themselves** (and hand it to someone else)
  so they catch anything broken before judges do.
- **Are they on track to finish?** Is the core loop playable end-to-end *right now* (start → play
  → win/lose → restart)? If not, that's the only priority; everything else waits. If time is
  short, help sort what's left into **"needed to be complete"** vs **"nice to have,"** name the
  smallest version that's still fun, and flag anything risky to **cut**. Either way: **upload a
  working build now**, then keep polishing and re-submit.

## 2. Build the zip

- **Settle the game's name first.** Use the name already in use, the **Title** in the project's
  `AGENTS.md` brief, or the `<title>` in `index.html`. **Only if none exists, ask** (suggest one
  from the game); don't invent one silently. The user will use this name when they set up the
  itch page.
- **Confirm the entry file is `index.html`.** itch serves the game online, so **CDN links load
  fine** — the Phaser/three.js CDN tags work as-is at judging time. Just make sure every URL is
  **`https://`** (itch blocks `http://` as mixed content) and that the engine URL **pins a
  version** so it can't shift under you. If the main file has another name, tell the user — itch
  needs `index.html`.
- **Put all generated artifacts in a `submission/` folder** at the project root (create it if
  needed) — it's regenerated build output, kept apart from the game's own files. **Create the zip
  with `index.html` at the ROOT of the archive** (not in a subfolder), including the `assets/`
  folder and anything else the game needs, using the bundled script:
  ```bash
  python3 "${PLUGIN_ROOT}/scripts/package_for_itch.py" <game-dir> -o <game-dir>/submission/game.zip
  ```
  The script guarantees the root layout, warns on `http://` mixed content (blocked on itch), and
  notes any CDN dependency. It also **excludes the dev-only files** (`AGENTS.md`, `PROGRESS.md`, and
  the `play.py`/`play.command`/`play.bat`/`play.ps1` launcher) so they
  don't ship in the game. **Tell the user the exact path** to `submission/game.zip`.

## 3. Publishing checklist

Print this for the user to follow on itch.io (also in the reference). They write their own page
copy — this checklist just tells them what to do with the zip:

- Suggested **genre/tags** and the best **screenshot/GIF** moment (judges scan visuals first).
- [ ] Upload **`submission/game.zip`**.
- [ ] Tick **"This file will be played in the browser."**
- [ ] Fill in **title, short description, controls, credits** (the itch page is theirs to write).
- [ ] Set a **thumbnail/cover** image.
- [ ] Configure **embed size + Fullscreen button** (Mobile friendly if touch).
- [ ] **Submit.**
- [ ] Open the game **from the jam page** and confirm it actually plays.

## Offer the game shell

If the game lacks a **title screen, how-to-play, or game-over/restart**, offer to add that shell
now as clean game states (with an iframe-safe, namespaced-`localStorage` high score). It's cheap
presentation points, and the controls then appear *inside* the game too, not just on the page.

## Remind the user

Upload a working version **early**, then re-run this skill to rebuild `submission/game.zip` as
the game gets polished.

## References
- itch export details + embed settings + checklist: `../../references/itch-export.md`
- The packaging script: `../../scripts/package_for_itch.py`
- Working defaults: `../../references/game-jam-mode.md`
