#!/usr/bin/python3
""" script that adds all args to a python list and saves them to a file in json"""
from sys import argv
import json


load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
try:
    py_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    py_list = []
    save_to_json_file(py_list, "add_item.json")
for arg in argv[1:]:
    py_list.append(arg)
save_to_json_file(py_list, "add_item.json")
