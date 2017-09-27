#!/usr/bin/node
// Writes api query into a file
const fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];
const request = require('request');
request.get(url, function (err, res, req) {
  if (err) {
    return console.log(err);
  }
  fs.writeFile(file, req, 'utf8');
});
