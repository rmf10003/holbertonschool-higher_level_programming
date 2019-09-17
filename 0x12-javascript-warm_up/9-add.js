#!/usr/bin/node
function add (a, b) {
  return a + b;
}
const a1 = parseInt(process.argv[2]);
const b1 = parseInt(process.argv[3]);

console.log(add(a1, b1));
