#!/usr/bin/node
// Increments and calls a function
exports.addMeMaybe = function (number, theFunction) {
  let j = 0;
  for (let i = 0; i <= number; i++) {
    j = j + 1;
  }
  theFunction(j);
};
