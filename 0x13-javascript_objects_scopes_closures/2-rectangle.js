#!/usr/bin/node
exports.Rectangle = function Rectangle (w, h) {
  if (w < 1 || h < 1 || !w || !h) {
    return;
  }

  this.width = w;
  this.height = h;
};
