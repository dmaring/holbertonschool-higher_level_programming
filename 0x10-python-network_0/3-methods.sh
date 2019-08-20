#!/bin/bash
# a script that gets the allowed methods for a URL
curl -s -I "$1" | grep Allow: | cut -d " " --complement -f 1
