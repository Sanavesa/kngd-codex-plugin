# KNGD (plugin)

Beginner-friendly Codex skills for building an HTML5 game in a jam. Built on a real engine —
**Phaser** for 2D, **three.js** for 3D — loaded from a CDN, so there's **no build step**: just one
`index.html` you open in the browser and submit to itch.io. You talk, Codex builds.

## Skills (2)

| Skill | What it does |
|---|---|
| `new-game` | The entrypoint for any game request — primes "game-jam mode", brainstorms the idea (2–4 option questions via the question tool in plan mode), builds a complete single-file `index.html`, writes the `AGENTS.md` brief, seeds the `PROGRESS.md` running-state file, and sets up an `assets/` folder. Also continues an existing game. |
| `submit` | Package the game for itch.io — build the upload-ready zip and print the publishing checklist (files only; you write your own itch page). |

**Art, sound, polish, and bug-fixing need no skill:** just ask (or paste an error / let Codex
offer). It generates art and sound in code, adds game-feel juice from a menu, and fixes bugs from
a console error or your description, as part of building, every session. To **play**, open
`index.html` in your browser — it double-clicks open (2D **and** 3D; the engine loads from a CDN,
and your images/audio in `assets/` load through HTML elements). To use your **own**
asset, drop the file in the
**`assets/` folder** and reference it as `@assets/name.png`.

The always-on primer is bundled into the `AGENTS.md` that `new-game` writes into your game folder,
so Codex stays in game-jam mode every session. `new-game` also seeds a **`PROGRESS.md`**
running-state file, and Codex reads it at the start of every session and keeps it updated as it
builds — the memory that lets a fresh session resume with zero re-explaining (`AGENTS.md` = what
the game *is*; `PROGRESS.md` = where the build *is now*). Full primer:
[`references/game-jam-mode.md`](references/game-jam-mode.md).

Install and full docs: see the [marketplace README](../../README.md).
