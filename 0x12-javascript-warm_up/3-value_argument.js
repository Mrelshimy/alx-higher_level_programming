#!/usr/bin/node
if (process.argv.length <= 2) {
  console.log('No argument');
}
if (process.argv[2]) {
  console.log(process.argv[2]);
}
