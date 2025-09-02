# PaperBoi 📰🚲🏠 (Pygame-Web Edition)

Play the emoji Paperboy arcade game in your browser, thanks to [pygame-web](https://github.com/pygame-web/pygame-web)!

## How to Play

- **Move:** Arrow keys (← ↑ ↓ →)
- **Throw Newspaper:** Spacebar
- Deliver newspapers to houses (🏠), avoid road obstacles, and earn points!

## Requirements

- Modern browser (Chrome, Edge, Firefox, Safari)
- No install needed!

## Local Development

Open `index.html` in your browser using a local HTTP server (not by double-clicking).
For example, with Python 3:
```bash
python -m http.server
```
Then visit [http://localhost:8000](http://localhost:8000)

## Deploy on Vercel

- Push your project to GitHub.
- Import it on [vercel.com](https://vercel.com/) as a static project.
- Your Pygame game will run in-browser!

## How It Works

- Loads `main.py` and runs it via `pygame-web` (compiled to WebAssembly).
- All graphics are emoji (via system fonts).

## Caveats

- Not all Pygame features are supported in the browser.
- Some emoji may not render identically on all platforms.
- If you see a blank screen, check browser console for errors.

## Credits

- [pygame-web](https://github.com/pygame-web/pygame-web)
- Original game by [PRIME8s](https://github.com/PRIME8s)