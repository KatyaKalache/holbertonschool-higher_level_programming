#!/usr/bin/node
// Reverses a list
exports.esrever = function (list) {
  revList = [];
  let i = list.length - 1;
  for (; i >= 0; i--) {
    revList.push(list[i]);
  }
  return revList;
};
