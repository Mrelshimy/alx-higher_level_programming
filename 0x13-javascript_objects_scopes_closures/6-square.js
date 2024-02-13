#!/usr/bin/node

const SquareOne = require('./5-square');

class Square extends SquareOne {
  charPrint (c) {
    let i = this.height;
    for (;i > 0; i--) {
      let j = this.width;
      for (;j > 0; j--) {
        process.stdout.write(c || 'X');
      }
      process.stdout.write('\n');
    }
  }
}
module.exports = Square;
