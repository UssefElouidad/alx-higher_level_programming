#!/usr/bin/node

const Square = require('./5-square');

class Square1 extends Square {
  costructor (size) {
  }

  charPrint(c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
	    console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square1;
