Test case for an issue affecting MediaElement.js (and not HTML5 MediaElement)
on Firefox. It appears (for me) to work on Chrome.

The server script purposefully waits 10s between headers and data, in order to
avoid triggering any race conditions there.

* Install Python 3
* Run `python runserver.py`
* Click on one of the 3 links:
    - http://localhost:8080/test_audio_vanilla.html (Without MediaElement.js")
    - http://localhost:8080/test_audio_mejs.html (With MediaElement.js")
    - http://localhost:8080/test_audio_mejs_fix.html (With MediaElement.js workaround")
