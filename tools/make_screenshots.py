"""Capture store screenshots with headless Chrome. Usage: python3 make_screenshots.py BASE_URL OUT_DIR
BASE_URL must serve the site with tools/shots.html and tools/feature.html copied to its root."""
import subprocess, sys, time, urllib.parse
from pathlib import Path

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
base, out = sys.argv[1].rstrip("/"), Path(sys.argv[2])
SHOTS = [("1-home", "home", "Press Start. That's it."), ("2-breathe-in", "in", "Follow the square"),
         ("3-voice-and-sound", "options", "Pick a voice. Add rain or waves."), ("4-breathe-out", "out", "Breathe out. Let go."),
         ("5-well-done", "done", "Calm in five minutes")]
DEVICES = [("iphone-6.9in-1290x2796", 430, 932, 3), ("ipad-13in-2064x2752", 1032, 1376, 2), ("android-phone-1080x1920", 360, 640, 3)]

def grab(url, path, w, h, scale):
    cmd = [CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--no-first-run", f"--user-data-dir={out / '.chrome-profile'}",
           f"--window-size={w},{h}", f"--force-device-scale-factor={scale}", "--virtual-time-budget=4000", f"--screenshot={path}", url]
    for attempt in range(4):
        r = subprocess.run(cmd, capture_output=True, timeout=90)
        if r.returncode == 0 and path.exists():
            print("wrote", path.name); return
        time.sleep(2)
    raise SystemExit(f"failed: {path.name}: {r.stderr.decode()[-400:]}")

for dev, w, h, scale in DEVICES:
    d = out / dev; d.mkdir(parents=True, exist_ok=True)
    for name, shot, cap in SHOTS:
        grab(f"{base}/shots.html?shot={shot}&cap={urllib.parse.quote(cap)}", d / f"{name}.png", w, h, scale)
grab(f"{base}/feature.html", out / "google-play-feature-1024x500.png", 1024, 500, 1)
