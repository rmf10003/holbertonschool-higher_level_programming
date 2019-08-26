#!/usr/bin/python3
"""fetch url using urllib"""
import urllib.request


with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    html = response.read()
    print("Body response:\n\t- type: " + str(type(html)))
    print("\t- content: " + str(html))
    print("\t- utf8 content: " + html.decode("utf-8"))
