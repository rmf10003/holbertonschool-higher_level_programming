#!/usr/bin/node
const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const fPath = process.argv[3];

request.get(url).pipe(fs.createWriteStream(fPath, 'utf8'));
