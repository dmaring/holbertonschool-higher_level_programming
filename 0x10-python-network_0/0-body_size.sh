#!/bin/bash
#a script that gets the donwloaded body size

curl "$1" -s -o /dev/null  -w "%{size_download}\n"
