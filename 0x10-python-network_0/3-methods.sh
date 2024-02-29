#!/bin/bash
# a Bash script that displays only body of a 200 status code response
curl -sX OPTIONS -I "$1" | grep -i "Allow:" | cut -d ' ' -f 2-
