#!/usr/bin/node

const request = require('request');

request.get(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, (err, responce, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    for (const character of data.characters) {
      request.get(character, (error, responce, newData) => {
        if (error) {
          console.error(error);
        } else {
          const charData = JSON.parse(newData);
          console.log(charData.name);
        }
      });
    }
  }
}
);
