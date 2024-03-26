#!/usr/bin/node

const request = require('request');

request.get(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, (err, responce, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    const results = data.results;
    for (const result of results) {
      for (const character of result.characters) {
        request.get(character, (error, responce, data) => {
          if (error) {
            console.error(error);
          } else {
            data = JSON.parse(data);
            console.log(data.name);
          }
        });
      }
    }
  }
}
);
