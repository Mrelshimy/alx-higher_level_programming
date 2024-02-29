#!/bin/bash
# a Bash script that displays only body of a 200 status code response
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
