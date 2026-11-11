"""Local preview server for the Box Breath site. Usage: python3 serve.py [port]"""
import functools, http.server, os, sys
from pathlib import Path

site = str(Path(__file__).resolve().parent.parent / "site")
port = int(os.environ.get("PORT") or (sys.argv[1] if len(sys.argv) > 1 else 8765))
handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=site)
http.server.ThreadingHTTPServer(("127.0.0.1", port), handler).serve_forever()
