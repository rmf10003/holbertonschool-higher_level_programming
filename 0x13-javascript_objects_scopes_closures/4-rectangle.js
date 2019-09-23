#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const arr = [];
    for (let i = 0; i < this.width; i++) {
      arr.push('X');
    }
    for (let i = 0; i < this.height; i++) {
      console.log(arr.join(''));
    }
  }

  rotate () {
    const x = this.width;
    this.width = this.height;
    this.height = x;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
};
