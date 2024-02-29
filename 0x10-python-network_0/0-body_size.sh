#!/usr/bin/env bash
# a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

curl -c "$1" | wc -c
