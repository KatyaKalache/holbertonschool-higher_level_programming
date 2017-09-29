#!/usr/bin/node
// Counts number of items
let i = 0;
exports.logMe = function (item) {
  console.log(i + ':', item);
  i++;
};
