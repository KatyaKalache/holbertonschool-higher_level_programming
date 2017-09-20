#!/usr/bin/node
// Prints 3 lines using an array of string and a loop
const myVar1 = 'C is fun';
const myVar2 = 'Python is cool';
const myVar3 = 'Javascript is amazing';
const arr = [myVar1, myVar2, myVar3];
let i = 0;
for (; i < arr.length; i++) {
  console.log(arr[i]);
}
