#!/bin/bash
# a Bash script that displays only body of a 200 status code response
curl -sw "%{http_code}" "$1"
