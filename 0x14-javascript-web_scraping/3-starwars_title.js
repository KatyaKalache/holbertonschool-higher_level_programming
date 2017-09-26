#!/usr/bin/node
// Returns status code
const request = require('request');
const url = 'http://swapi.co/api/films/';
const argument = process.argv[2];
request.get(url + argument, function (err, res, body) {
  if (err) {
    return console.log(err);
  }
  let jsonFormat = JSON.parse(body);
  let title = jsonFormat['title'];
  console.log(title);
});
