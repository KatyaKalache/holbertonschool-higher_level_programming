#!/usr/bin/node
// writes text into a file: both passed as argv
const fs = require('fs');
const file = process.argv[2];
const text = process.argv[3];
fs.writeFile(file, text, 'utf8', function (err, data) {
  if (err) {
    return console.log(err);
  }
  console.log(data);
});
