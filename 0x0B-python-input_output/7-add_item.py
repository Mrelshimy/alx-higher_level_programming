#!/usr/bin/python3
""" Function to add all args to list and save to file"""
import json
import sys
from "5-save_to_json_file" import save_to_json_file
from "6-load_from_json_file" import load_from_json_file


a = list(sys.argv[:])
fp = open(add_item.json, "a")
save_to_json_file(a, fp)
