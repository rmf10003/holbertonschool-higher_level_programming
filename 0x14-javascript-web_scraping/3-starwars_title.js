#!/usr/bin/node
const request = require('request');
const url = 'http://swapi.co/api/films/' + process.argv[2];
request.get(url, { json: true }, (error, response, body) => {
  if (error) {}
  console.log(body.title);
});
