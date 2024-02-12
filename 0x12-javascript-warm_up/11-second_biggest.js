#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
} else {
  process.argv.sort();
  process.argv.reverse();
  console.log(process.argv[1]);
}
