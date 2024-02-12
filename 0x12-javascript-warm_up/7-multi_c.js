#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences')
}
if (process.argv[2] <= 0) {
  // do nothing
} else {
  let x = process.argv[2]
  while (x > 0) {
    console.log('C is fun')
    x--
  }
}
