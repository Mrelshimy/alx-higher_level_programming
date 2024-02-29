#!/bin/bash
# a Bash script that displays the size of the body of http response
curl -s "$1" | wc -c
