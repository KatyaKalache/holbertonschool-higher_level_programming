#!/usr/bin/node
// Returns the number of occurrences in a list
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  let matchCount = 0;
  for (; counter < list.length; counter++) {
    if (searchElement === list[counter]) {
      matchCount += 1;
      return matchCount;
    }
  }
};
