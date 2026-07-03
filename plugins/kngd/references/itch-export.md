# itch.io Export Reference

How a single-file browser game maps onto itch.io HTML5 hosting: zip layout, embed settings, and
the publishing checklist. The `submit` skill uses this. (The itch page copy is the user's to
write — this kit only prepares the files.)

## itch runs your game over HTTPS in an iframe

itch serves HTML5 games from an HTTPS sandbox domain inside an `<iframe>`. An `index.html` that
already follows game-jam mode (engine from an HTTPS CDN, iframe-safe scaling, auto-focus, audio-
on-gesture, namespaced `localStorage` in try/catch) runs on itch **unchanged** — no rewrite. Only
a few things differ from local double-click:

1. **The game lives in an iframe.** It must grab keyboard focus (`window.focus()` on load and
   click) or judges' keys do nothing. Fullscreen and pointer lock need a user gesture; itch
   provides a Fullscreen button.
2. **`http://` subresources are blocked** as mixed content (itch is HTTPS). Use `https://`.
3. **CDN links work** — this kit builds on Phaser/three.js loaded from a CDN, and itch runs the
   game online, so the engine loads normally at judging time. Just keep every URL **`https://`**
   (see above) and **pin the engine version** in the URL so a new release can't change behavior.
4. **Every asset loader works** (a plus over local double-click). Because itch serves over HTTP,
   `fetch`-based formats — JSON atlases/tilemaps, GLTF/OBJ models — that a `file://` double-click
   can't read load **fine** here. An asset that needed a local server during dev works unchanged on
   itch; just make sure it's included in the zip.

## Zip requirements (the #1 cause of "won't load")

- The archive must contain **`index.html` at its ROOT**, not inside a subfolder. Zipping the
  *folder* (producing `mygame/index.html`) is the classic mistake — itch shows a blank page.
- Include everything the game needs: `index.html`, the `assets/` folder, any sibling `.js`/`.css`.
- Use the bundled script — it always puts `index.html` at the zip root and warns about the
  gotchas above:
  ```bash
  python3 "${PLUGIN_ROOT}/scripts/package_for_itch.py" path/to/game -o path/to/game/submission/game.zip
  ```

## Embed settings on the itch dashboard

- Tick **"This file will be played in the browser."**
- **Viewport / embed size:** if the game uses a full-window canvas, enable the **Fullscreen
  button** and set a sensible frame size (e.g. 960×640, or match your canvas). Enable **Mobile
  friendly** if you handle touch.
- Leave **"Automatically start on page load"** off if the game needs a click to start
  audio/focus (most do).

## Publishing checklist

The `submit` skill prepares the **files** (the zip); the itch page copy — title, pitch, controls,
credits — is the user's to write. This checklist covers the upload steps:

- Suggested **genre/tags** and the best **screenshot/GIF** moment (judges scan visuals first).
- [ ] Upload **`submission/game.zip`**.
- [ ] Tick **"This file will be played in the browser."**
- [ ] Fill in **title, short description, controls, credits** (the itch page is theirs to write).
- [ ] Set a **thumbnail/cover** image.
- [ ] Configure **embed size + Fullscreen button** (and Mobile friendly if touch).
- [ ] **Submit.**
- [ ] Open the game **from the jam page** and confirm it actually plays.

## Optional: butler CLI (fast re-uploads while polishing)

[butler](https://itch.io/docs/butler/) pushes builds without the web uploader:
```bash
butler push submission/game.zip <user>/<game>:html5
```
Re-run the packaging script, then `butler push` again each time you iterate.
