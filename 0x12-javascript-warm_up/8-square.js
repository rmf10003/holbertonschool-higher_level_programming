#!/usr/bin/node
const x = parseInt(process.argv[2]);
if (isNaN(x)) {
  console.log('Missing size');
}
const arr = [];
for (let i = 0; i < x; i++) {
  arr.push('X');
}
for (let i = 0; i < x; i++) {
  console.log(arr.join(''));
}
