#!/usr/bin/node
// Prints a message depending of the number of arguments passed
const messageFound = 'Argument found';
const messageNotFound = 'No argument';
if (process.argv[2] === undefined) {
  console.log(messageNotFound);
} else {
  console.log(messageFound);
}
