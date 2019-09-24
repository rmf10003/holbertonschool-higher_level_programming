#!/usr/bin/node
const fs = require('fs');

const str = process.argv[3];

fs.writeFile(process.argv[2], str, 'utf8', (err) => {
  if (err) { console.log(err); }
});
