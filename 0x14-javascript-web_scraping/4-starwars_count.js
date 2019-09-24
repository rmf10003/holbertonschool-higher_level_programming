#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let num = 0;

request.get(url, { json: true }, (error, response, films) => {
  if (error) {}
  for (const film of films.results) {
    for (const character of film.characters) {
      if (character.endsWith('/18/')) {
        num++;
      }
    }
  }
  console.log(num);
});
