#!/usr/bin/node

const request = require('request');

request.get(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, (err, responce, body) => {
  if (err) {
    console.log(err);
  } else {
    const episode = body.JSONparse();
    console.log(`${episode.title}`);
  }
});
