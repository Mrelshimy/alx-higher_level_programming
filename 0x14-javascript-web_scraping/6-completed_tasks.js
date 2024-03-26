#!/usr/bin/node

const request = require('request');

request.get(process.argv[2], 'utf8', (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const compTasks = {};
  const data = JSON.parse(body);
  data.forEach((todo) => {
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
