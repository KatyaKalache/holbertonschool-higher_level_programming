#!/usr/bin/node
// Prints x times "C is fun", x is number of argumetns passed
const myVar = 'C is fun';
let max = process.argv[2];
let i = 0;
if (parseInt(process.argv[2])) {
  for (; i < max; i++) {
    console.log(myVar);
  }
} else {
  console.log('Missing number of occurrences');
}
