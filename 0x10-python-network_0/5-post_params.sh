#!/bin/bash
# a Bash script that displays only body of a 200 status code response
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
