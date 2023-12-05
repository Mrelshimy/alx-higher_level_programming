#!/usr/bin/python3
""" Function to add all args to list and save to file"""
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


a = list(sys.argv[:])
#old = load_from_json_file('add_item.json')
fp = open('add_item'.json, "a")
save_to_json_file(a, fp)
