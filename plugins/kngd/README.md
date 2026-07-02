# KNGD (plugin)

Beginner-friendly Codex skills for building an HTML5 game in a jam. No engine, no build tools —
just one self-contained `index.html` you run by double-clicking, submitted to itch.io. You talk,
Codex builds.

## Skills (2)

| Skill | What it does |
|---|---|
| `new-game` | The entrypoint for any game request — primes "game-jam mode", brainstorms the idea (2–4 option questions via the question tool in plan mode), builds a complete single-file `index.html`, writes the `AGENTS.md` brief, seeds the `PROGRESS.md` running-state file, and sets up an `assets/` folder. Also continues an existing game. |
| `submit` | Package the game for itch.io — build the upload-ready zip and print the publishing checklist (files only; you write your own itch page). |

**Art, sound, polish, and bug-fixing need no skill:** just ask (or paste an error / let Codex
offer). It generates art and sound in code, adds game-feel juice from a menu, and fixes bugs from
a console error or your description, as part of building, every session. To **play**, just open
`index.html` in your browser (double-click it). To use your **own** asset, drop the file in the
**`assets/` folder** and reference it as `@assets/name.png`.

The always-on primer is bundled into the `AGENTS.md` that `new-game` writes into your game folder,
so Codex stays in game-jam mode every session. `new-game` also seeds a **`PROGRESS.md`**
running-state file, and Codex reads it at the start of every session and keeps it updated as it
builds — the memory that lets a fresh session resume with zero re-explaining (`AGENTS.md` = what
the game *is*; `PROGRESS.md` = where the build *is now*). Full primer:
[`references/game-jam-mode.md`](references/game-jam-mode.md).

Install and full docs: see the [marketplace README](../../README.md).
