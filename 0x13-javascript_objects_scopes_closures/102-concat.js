#!/usr/bin/node
// Concats text from 2 files and write it to the third one
const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', function read (err, dataA) {
  if (err) {
    return console.log(err);
  }
  fs.readFile(process.argv[3], 'utf8', function read (err, dataB) {
    if (err) {
      return console.log(err);
    }
    fs.writeFile(process.argv[4], dataA + '\n' + dataB);
  });
});
