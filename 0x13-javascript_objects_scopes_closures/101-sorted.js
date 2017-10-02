#!/usr/bin/node
// Imports an array and computes a new array
let dict = require('./101-data.js').dict;
let newDict = {};
for (let key in dict) {
  if (newDict[dict[key]] === undefined) {
    newDict[dict[key]] = [];
    newDict[dict[key]].push(key);
  } else {
    newDict[dict[key]].push(key);
  }
}
console.log(newDict);
