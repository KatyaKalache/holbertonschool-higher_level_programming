#!/usr/bin/node
// Prints a message depending of the number of arguments passed
const messageFound = 'Argument found';
const messageFoundPlural = 'Arguments found';
const messageNotFound = 'No argument';
if (process.argv[2] === undefined) {
  console.log(messageNotFound);
} else if (process.argv[3] === undefined) {
  console.log(messageFound);
} else {
  console.log(messageFoundPlural);
}
