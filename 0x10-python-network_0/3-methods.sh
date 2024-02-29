#!/bin/bash
# a Bash script that displays only body of a 200 status code response
curl -sI "$1" | grep "ALLOW" | cut -d " " -f 2-
