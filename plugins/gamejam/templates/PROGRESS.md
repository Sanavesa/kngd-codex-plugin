# Progress — running state

> **Codex maintains this file; it is the memory that carries the game between sessions.** Read it
> at the **start of every session** to recover where the build is, and **keep it updated** as you
> work (after each meaningful step, bug fixed, or decision, and before stopping). Keep it honest
> and current — a fresh session should be able to resume from this alone.
>
> `AGENTS.md` = what the game *is* (stable). This file = where the build *is right now* (volatile).
> Keep them from overlapping: durable design facts live in `AGENTS.md`, working state lives here.

## Now (current status)
<Is it playable end-to-end right now (start → play → win/lose → restart)? What's the latest
working state? One or two lines.>

## Recently done
<Newest first — a light changelog of what changed and when. e.g. "- Added double jump.">
-

## Next up (TODO)
<Ordered — the smallest next steps that add fun. e.g. "1. Score +1 per pipe. 2. Title screen.">
-

## Known issues / bugs
<Open problems and anything flaky. e.g. "- Player can clip through the floor at high speed.">
-

## Decisions & deferred ideas
<Why we chose things, and what we intentionally cut or postponed — so we don't relitigate it.
e.g. "- Deferred multiplayer (scope). - Chose fixed 320×180 virtual resolution.">
-

## How to run
Open `index.html` in the browser (double-click). Hard-refresh with Ctrl/Cmd+Shift+R if a change
doesn't show up.
