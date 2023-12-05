#!/usr/bin/python3
""" Function to add all args to list and save to file"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

a = list(sys.argv[1:])

try:
    old = load_from_json_file('add_item.json')
except Exception:
    old = []

old.extend(a)
save_to_json_file(old, 'add_item.json')
