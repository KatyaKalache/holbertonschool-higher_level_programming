#!/usr/bin/node
// Returns status code
const request = require('request');
const url = process.argv[2];
const wedgeUrl = 'https://swapi.co/api/people/18/';
let i = 0;
let matchCount = 0;
request.get(url, function (err, res, results) {
  if (err) {
    return console.log(err);
  }
  let jsonFormat = JSON.parse(results);
  let movieList = jsonFormat['results'];
  for (; i < movieList.length; i++) {
    let charList = movieList[i]['characters'];
    for (let j = 0; j < charList.length; j++) {
      if (charList[j] === wedgeUrl) {
        matchCount++;
      }
    }
  }
  console.log(matchCount);
});
