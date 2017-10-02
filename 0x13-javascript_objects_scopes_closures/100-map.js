!/usr/bin/node
// Imports an array and computes a new array
let list = require('./100-data.js').list;
let array = [];
console.log(list);
list.map(function (i, j) {
  let value = i * j;
  array.push(value);
});
console.log(array);
