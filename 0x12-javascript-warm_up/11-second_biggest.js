#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
} else {
  process.argv.sort((a, b) => a - b);
  process.argv.reverse();
  console.log(process.argv);
}
