#!/bin/bash
# send request to URL and display status code of response
curl "$1" -sI -o /dev/null -w "%{http_code}"
