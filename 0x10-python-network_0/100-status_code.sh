#!/bin/bash
# a script that gets the downloaded body size of GET request
curl "$1" -s -o /dev/null  -w "%{http_code}"
