#!/usr/bin/node
// Prints a square
let size = (parseInt(process.argv[2]));
let i = 0;
let value = ('X').repeat(size);

if (!parseInt(process.argv[2])) {
  console.log('Missing size');
}
for (; i < size; i++) {
  console.log(value);
}
