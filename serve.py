from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

ROOT = Path(__file__).resolve().parent

class Handler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        admin = path.split("?", 1)[0].startswith("/admin/")
        self.directory = str(ROOT / ("supplier-admin" if admin else "docs"))
        return super().translate_path(path[len("/admin"):] if admin else path)

if __name__ == "__main__":
    print("Shop: http://localhost:8767/", flush=True)
    print("Admin: http://localhost:8767/admin/", flush=True)
    ThreadingHTTPServer(("127.0.0.1", 8767), Handler).serve_forever()
