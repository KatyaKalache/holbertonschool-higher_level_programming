#!/usr/bin/node
// Writes a class Square that inherits from Square of 5-square.js
const Square = require('./5-square').Square;
exports.Square = Square;
Square.prototype.charPrint = function (c) {
  let value = ('C').repeat(this.width);
  let xValue = ('X').repeat(this.width);
  let i = 0;
  let j = 0;
  if (c) {
    for (; i < this.height; i++) {
      for (; j < this.width; j++) {
      }
      console.log(value);
    }
  } else {
    for (; i < this.height; i++) {
      for (; j < this.width; j++) {
      }
      console.log(xValue);
    }
  }
};
