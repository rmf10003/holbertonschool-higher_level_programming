#!/usr/bin/python3
"""fetch url using urllib"""
import urllib.request


with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    html = response.read()
    for item in html:
        print(item)
