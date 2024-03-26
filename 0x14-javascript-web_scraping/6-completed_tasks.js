#!/usr/bin/node

const request = require('request');

request.get(process.argv[2], { json: true }, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const compTasks = {};
  body.forEach((todo) => {
    if (todo.completed) {
      if (!compTasks[todo.userId]) {
        compTasks[todo.userId] = 1;
      } else {
        compTasks[todo.userId] += 1;
      }
    }
  });
  console.log(compTasks);
});
