#!/usr/bin/env python3
"""Serve the complete built site locally, with a real custom 404 response."""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlsplit
import argparse

ROOT = Path(__file__).resolve().parents[1] / '_site'

class PreviewHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        route = unquote(urlsplit(path).path)
        if '..' in route.split('/') or any(part.startswith('.') for part in route.split('/') if part):
            return str(ROOT / '.preview-route-not-found')
        target = (ROOT / route.lstrip('/')).resolve()
        return str(target if target.is_relative_to(ROOT) else ROOT / '.preview-route-not-found')

    def end_headers(self):
        self.send_header('X-Robots-Tag', 'noindex, nofollow')
        self.send_header('Cache-Control', 'no-cache')
        super().end_headers()

    def list_directory(self, path):
        self.send_error(404)

    def send_error(self, code, message=None, explain=None):
        if code == 404 and (ROOT / '404.html').is_file():
            content = (ROOT / '404.html').read_bytes()
            self.send_response(404)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.send_header('Content-Length', str(len(content)))
            self.end_headers()
            if self.command != 'HEAD':
                self.wfile.write(content)
        else:
            super().send_error(code, message, explain)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port', default=8768, type=int)
    options = parser.parse_args()
    if not (ROOT / 'index.html').is_file():
        parser.error('Build the site first with scripts/site build')
    server = ThreadingHTTPServer(('127.0.0.1', options.port), PreviewHandler)
    print(f'Homepage: http://127.0.0.1:{options.port}/', flush=True)
    print(f'Projects: http://127.0.0.1:{options.port}/projects/', flush=True)
    print(f'Writing:  http://127.0.0.1:{options.port}/blog/', flush=True)
    server.serve_forever()
