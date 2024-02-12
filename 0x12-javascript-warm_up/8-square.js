#!/usr/bin/node
let i = process.argv[2]
if (isNaN(process.argv[2])) {
  console.log('Missing size')
} else if (process.argv[2] <= 0) {
  // do nothing
} else {
  while (i > 0) {
    let j = process.argv[2]
    while (j > 0) {
      process.stdout.write('X')
      j--
    }
    process.stdout.write('\n')
    i--
  }
}
