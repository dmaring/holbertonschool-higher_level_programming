#!/bin/bash
# a script that sends a POST request
curl -s -X POST "$1" -d @"$2" -H "Content-Type: application/json"
