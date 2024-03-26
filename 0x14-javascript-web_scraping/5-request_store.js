#!/usr/bin/node

const fs = require('fs');
const request = require('request');

request.get(process.argv[2], (err, responce, body) => {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(process.argv[3], body, 'utf8', err => {
      if (err) {
        console.error(err);
      }
    });
  }
});
