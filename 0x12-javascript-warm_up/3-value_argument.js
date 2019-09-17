#!/usr/bin/node
const clargs = process.argv;
if (clargs[2] === undefined) {
  console.log('No argument');
} else {
  console.log(clargs[2]);
}
