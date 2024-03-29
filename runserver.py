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
    print("")
    print("Should work:")
    print("  http://localhost:8080/test_audio_vanilla.html (Without MediaElement.js)")
    print("  http://localhost:8080/test_audio_mejs_wo_player.html (With MediaElement.js, w/o player controls)")
    print("")
    print("Should fail to play the 2nd song:")
    print("  http://localhost:8080/test_audio_mejs.html (With MediaElement.js)")
    print("")
    print("Workarounds:")
    print("  http://localhost:8080/test_audio_mejs_workaround.html (with MediaElement.js workaround)")
    print("")
    print("MEJS fixes:")
    print("  http://localhost:8080/test_audio_mejs_fix_mejs.html (with MediaElement.js code changes)")
    print("  http://localhost:8080/test_audio_mejs_fix_event_order.html (with manual MediaElement.js init)")
    print("")
    print("For comparison, additional logs added to the scripts:")
    print("  http://localhost:8080/test_audio_mejs_with_logs.html (issue present)")
    print("  http://localhost:8080/test_audio_mejs_fix_event_order_with_logs.html (with manual MediaElement.js init)")
    print("")
    with socketserver.TCPServer(("", 8080), Handler) as httpd:
        httpd.serve_forever()
