#!/usr/bin/node
const parSquare = require('./5-square');

class Square extends parSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (letter) {
    if (letter === undefined) {
      letter = 'X';
    }
    let row = '';
    for (let t = 0; t < this.width; t++) {
      row = row + letter;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(row);
    }
  }
}

module.exports = Square;
