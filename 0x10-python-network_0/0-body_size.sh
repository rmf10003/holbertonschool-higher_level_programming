#!/bin/bash
# display size of the body of HTTP response
curl -sI "$@" -X GET | grep Content-Length | cut -d: -f2 | tr -d ' '
