#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      return 'Rectangle {}';
    }
  }

  rotate () {
    let ex = 0;
    ex = this.width;
    this.width = this.height;
    this.height = ex;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
