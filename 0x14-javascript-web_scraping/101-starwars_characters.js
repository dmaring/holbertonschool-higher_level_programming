#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const myList = [];
let completedRequests = 0;

function getCharNames (charIdList) {
  for (let i = 0; i < charIdList.length; i++) {
    request.get(charIdList[i], (e, r, body) => {
      myList[i] = JSON.parse(body).name;
      completedRequests++;
      if (completedRequests === charIdList.length) {
        for (let i = 0; i < myList.length; i++) {
          console.log(myList[i]);
        }
      }
    });
  }
}

request
  .get('http://swapi.co/api/films/' + movieId, 'utf8', (e, r, body) => {
    getCharNames(JSON.parse(body).characters);
  });
