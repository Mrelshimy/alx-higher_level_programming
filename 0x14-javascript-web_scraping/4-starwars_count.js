#!/usr/bin/node

const request = require('request');
let count = 0;

request.get(process.argv[2], (err, responce, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    const results = data.results;
    for (const result of results) {
      for (const character of result.characters) {
        if (character.includes('18')) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
