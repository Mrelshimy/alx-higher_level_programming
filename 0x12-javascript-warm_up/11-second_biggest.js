#!/usr/bin/node
let flag = 0;
if (process.argv.length < 4) {
  console.log(0);
} else {
  process.argv.sort();
  process.argv.reverse();
  for (let i = 2; i < process.argv.length; i++) {
    if (process.argv[i] > 0) {
      flag = 1;
      break;
    }
  }
  if (flag === 1) {
    console.log(process.argv[1]);
  } else {
    console.log(process.argv[process.argv.length - 2]);
  }
}
