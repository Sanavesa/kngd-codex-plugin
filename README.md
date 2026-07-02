# KNGD — a Codex plugin

**Kuwait National Game Development** — a beginner-friendly game-jam kit for **Codex**. You talk, Codex builds: brainstorm an idea,
build a self-contained `index.html` you run by double-clicking, and submit it to itch.io. Art,
sound, polish, and bug-fixing just happen as you go — no engine, no build tools, no commands.

## Install

**Codex app**

1. Open *Add plugin marketplace*.
2. Set **Source** to `https://github.com/Sanavesa/KNGD-codex-plugin`.
3. Install **KNGD** when it appears in the plugin browser.

**Codex CLI**

1. Add the marketplace:
   ```bash
   codex plugin marketplace add https://github.com/Sanavesa/KNGD-codex-plugin
   ```
2. Run `/plugins` and install **KNGD**.

## How to use

### 1. Start a game

Turn on **plan mode**, then send `@new-game` with your idea:

```
@new-game a tiny space shooter
```

Codex brainstorms the idea with you, then builds a complete `index.html`.

### 2. Iterate

Just talk — Codex handles the rest:

- **Change anything** — describe it in plain language.
- **Fix a bug** — paste the console error.
- **Add polish** — ask for art, sound, or juice anytime (or let Codex offer).
- **Use your own asset** — drop the file in `assets/` and reference it as `@assets/name.png`.

### 3. Play

Double-click `index.html` in your browser.

### 4. Submit to itch.io

Send `@submit`. Codex builds an upload-ready zip and prints the publishing checklist.

---

That's it. Codex stays in "game-jam mode" every session via the `AGENTS.md` it writes into your
game folder, so you never re-explain your game.
