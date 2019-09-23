#!/usr/bin/node

const list = require('./100-data').list;
const newList = list.map((currentValue, index) => currentValue * index);
console.log(list);
console.log(newList);
