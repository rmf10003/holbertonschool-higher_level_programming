#!/usr/bin/node
const argv = process.argv.map(arg => parseInt(arg)).slice(2);
if (argv.length === 0 || argv.length === 1) {
  console.log(0);
  process.exit();
}
let second = 0; let first = argv[0];
for (let i = 0; i < argv.length; i++) {
  if (argv[i] > first) {
    second = first;
    first = argv[i];
  } else if (argv[i] > second) {
    second = argv[i];
  }
}
console.log(second);
