#!/usr/bin/node
exports.Rectangle = function Rectangle (w, h) {
  if (w < 1 || h < 1 || !w || !h) {
    return;
  }

  this.width = w;
  this.height = h;

  this.print = function () {
    let value = ('X').repeat(w);
    let i = 0;
    let j = 0;
    for (; i < h; i++) {
      for (; j < w; j++) {
      }
      console.log(value);
    }
  };
};
