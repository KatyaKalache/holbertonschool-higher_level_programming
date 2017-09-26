#!/usr/bin/node
// Reads text from a file passed as an argument
const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', function (err, data) {
  if (err) {
    return console.log(err);
  }
  console.log(data);
});
