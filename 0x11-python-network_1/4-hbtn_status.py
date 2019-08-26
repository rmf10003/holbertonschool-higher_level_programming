#!/usr/bin/python3
"""use requests module to fetch a page given a url"""
import requests

r = requests.get('https://intranet.hbtn.io/status')
print("Body response:\n\t- type: " + str(type(r.text)))
print("\t- content: " + str(r.text))
