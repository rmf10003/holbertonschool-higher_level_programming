#!/bin/bash
# send JSON POST request
curl "$1" -sX POST -H "Content-Type: application/json" -d @"$2"
