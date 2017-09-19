#!/usr/bin/node
// Prints the first argument passed to it
const messageNotFound = 'No argument'
if (process.argv.length <= 2) {
  console.log(messageNotFound);
} else {
  console.log(String(process.argv.slice(2)));
}
