#!/usr/bin/python
# coding=utf-8

from http.server import SimpleHTTPRequestHandler
import socketserver
import time

class Handler(SimpleHTTPRequestHandler):
    def flush_headers(self):
        super().flush_headers()
        if self.path.endswith(".mp3"):
            self.log_message("Sent headers for %s, waiting.", self.path)
            time.sleep(10)
            self.log_message("Sent headers for %s, done.", self.path)


if __name__ == '__main__':
    with socketserver.TCPServer(("", 8080), Handler) as httpd:
        httpd.serve_forever()
