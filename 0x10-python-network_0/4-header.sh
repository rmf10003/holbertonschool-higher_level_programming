#!/bin/bash
# send GET  request to URL and display body of response w/ header var set
curl "$1" -sX GET -H "X-HolbertonSchool-User-Id: 98"
