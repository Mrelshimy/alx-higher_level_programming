#!/usr/bin/node
const a = parseInt(process.argv[2]);
function factorial (a) {
  if (a > 0) {
    return a * factorial(a - 1);
  } else {
    return 1;
  }
}
const facResult = factorial(a);
console.log(facResult);
