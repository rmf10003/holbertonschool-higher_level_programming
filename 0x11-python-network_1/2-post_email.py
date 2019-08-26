#!/usr/bin/python3
"""take in URL, send a request to URL and display value of X-Reqeust-Id var"""
import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    values = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    try:
        req = urllib.request.Request(url, data)
        with urllib.request.urlopen(req) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except Exception as e:
        print(e)
