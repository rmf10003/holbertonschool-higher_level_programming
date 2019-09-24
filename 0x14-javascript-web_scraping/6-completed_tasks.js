#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const obj = {};

request.get(url, { json: true }, function (error, response, todos) {
  if (error) {}
  for (const task of todos) {
    if (!(task.userId in obj)) {
      obj[task.userId] = 0;
    }
  }
  for (const task of todos) {
    if (task.completed === true) {
      obj[task.userId]++;
    }
  }
  for (const prop in obj) {
    if (obj[prop] === 0) {
      delete obj[prop];
    }
  }
  console.log(obj);
});
