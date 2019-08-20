#!/bin/bash
# find out what http methods the server accepts
curl "$1" -X OPTIONS -sI | grep Allow: | cut -d' ' -f2-
