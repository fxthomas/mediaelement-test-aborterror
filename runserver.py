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
    print("Go to the following pages to test!")
    print("  http://localhost:8080/test_audio_vanilla.html (Without MediaElement.js")
    print("  http://localhost:8080/test_audio_mejs.html (With MediaElement.js")
    print("  http://localhost:8080/test_audio_mejs_fix.html (With MediaElement.js workaround")
    with socketserver.TCPServer(("", 8080), Handler) as httpd:
        httpd.serve_forever()
