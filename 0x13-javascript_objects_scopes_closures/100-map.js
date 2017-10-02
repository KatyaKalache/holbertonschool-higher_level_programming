#!/usr/bin/node
// Imports an array and computes a new array
let list = require('./100-data.js').list;
let array = [];
console.log(list);
let new_list = list.map(function (i, j) {
  let value = i*j;
  array.push(value);
});
