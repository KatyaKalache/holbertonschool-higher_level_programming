#!/usr/bin/node
// Returns status code
const request = require('request');
const url = process.argv[2];
request.get(url, function (err, res) {
  if (err) {
    return console.log(err);
  }
  console.log('code:' + ' ' + res.statusCode);
});
