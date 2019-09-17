#!/usr/bin/node
const clargs = process.argv;
if (clargs.length === 2) {
  console.log('No argument');
} else if (clargs.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
