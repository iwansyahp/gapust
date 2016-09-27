#!/bin/bash

# A simple bash command for starting the GAE dev_appserver. The GAE SDK must be installed locally.
../../apps_extras/google_appengine_python/dev_appserver.py  --host=0.0.0.0 --port=8080 --use_mtime_file_watcher no .
