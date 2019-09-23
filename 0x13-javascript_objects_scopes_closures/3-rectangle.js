#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
      this.print = function () {
        let row = '';
        for (let t = 0; t < this.width; t++) {
          row = row + 'X';
        }
        for (let i = 0; i < this.height; i++) {
          console.log(row);
        }
      };
    }
  }
}

module.exports = Rectangle;
