#!/usr/bin/node

module.exports = class Square extends require('./5-square') {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      const arr = [];
      for (let i = 0; i < this.width; i++) {
        arr.push(c);
      }
      for (let i = 0; i < this.height; i++) {
        console.log(arr.join(''));
      }
    }
  }
};
