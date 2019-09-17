#!/usr/bin/node
const clargs = process.argv;
const i = parseInt(clargs[2]);
if (isNaN(i)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + i);
}
