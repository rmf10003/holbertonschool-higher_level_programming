#!/bin/bash
# send POST request and display body of response with set vars
curl "$1" -X POST -s -d "email=hr@holbertonschool.com&subject=I+will+always+be+here+for+PLD"
