#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = this.height;
    for (;i > 0; i--) {
      let j = this.width;
      for (;j > 0; j--) {
        process.stdout.write('X');
      }
      process.stdout.write('\n');
    }
  }
}
module.exports = Rectangle;
