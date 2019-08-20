#!/bin/bash
# a script that sends a POST request
curl -s -X POST -d "email=hr@holbertonschool.com" -d "subject=I will always be there for PLD" "$1"
