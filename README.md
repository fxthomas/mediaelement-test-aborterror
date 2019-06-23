Test case for an issue affecting MediaElement.js (and not HTML5 MediaElement)
on Firefox. It appears (for me) to work on Chrome.

The server script purposefully waits 10s between headers and data, in order to
avoid triggering any race conditions there.

Instructions
============

* Install Python 3
* Run `python runserver.py`
* Click on one of the 3 links:
    * http://localhost:8080/test_audio_vanilla.html (Without MediaElement.js)
    * http://localhost:8080/test_audio_mejs_wo_player.html (With MediaElement.js, w/o player controls)
    * http://localhost:8080/test_audio_mejs.html (With MediaElement.js)
    * http://localhost:8080/test_audio_mejs_workaround.html (with MediaElement.js workaround)
    * http://localhost:8080/test_audio_mejs_fix_mejs.html (with MediaElement.js code changes)

Tests
=====

* `test_audio_vanilla.html`: Test with standard HTML5 (without MEJS). This
  appears to work.

* `test_audio_mejs_wo_player.html`: Test with MEJS, without the player. This
  appears to work.

* `test_audio_mejs.html`: Test with MEJS, with the player. This fails with
  `AbortError` for me.

* `test_audio_mejs_workaround.html`: Workaround for MEJS with the player. This
  appears to work, but still shows errors in the stream and has other issues
  (such as having an edge case where the last song continues on loop).

* `test_audio_mejs_fix_mejs.html`: Test with the following patch on MEJS. This
  appears to work, and explains the root cause of the issue : the MEJS callback
  is called, I think, after Airsonic's ; calling stop while the stream is still
  loading makes Firefox stop everything and print `AbortError` on the console.

```diff
diff --git a/src/js/player.js b/src/js/player.js
index 04262d73..0feeb9a1 100644
--- a/src/js/player.js
+++ b/src/js/player.js
@@ -828,11 +828,12 @@ class MediaElementPlayer {
 					}
 				}
 
-				if (typeof t.media.renderer.stop === 'function') {
-					t.media.renderer.stop();
-				} else {
-					t.pause();
-				}
+				// Commented out for Airsonic test
+				// if (typeof t.media.renderer.stop === 'function') {
+				// 	t.media.renderer.stop();
+				// } else {
+				// 	t.pause();
+				// }
 
 				if (t.setProgressRail) {
 					t.setProgressRail();
```
