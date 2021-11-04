#!/usr/bin/env python3

import http.server
import socketserver

class NoCachingIndexRequestHandler(http.server.SimpleHTTPRequestHandler):
  def end_headers(self):
    if self.path == "/index.html" or self.path == "/":
      self.send_header("Cache-Control", "max-age=0, no-cache, no-store, must-revalidate")
      self.send_header("Pragma", "no-cache")
      self.send_header("Expires", "0")
    http.server.SimpleHTTPRequestHandler.end_headers(self)

if __name__ == '__main__':
  with socketserver.TCPServer(("", 80), NoCachingIndexRequestHandler) as server:
    server.serve_forever()
