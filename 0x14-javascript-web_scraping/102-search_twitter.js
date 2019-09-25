#!/usr/bin/node
const request = require('request');
const base64 = require('base-64');
const utf8 = require('utf8');

const consumerKey = process.argv[2];
const consumerSecret = process.argv[3];
const searchString = process.argv[4];

// Obtain a bearer token
// Concat consumerKey and consumerSecret
const concated = consumerKey + ':' + consumerSecret;
const bytes = utf8.encode(concated);
const encoded = base64.encode(bytes);

const options = {
  url: 'https://api.twitter.com/oauth2/token',
  headers: {
    Authorization: 'Basic ' + encoded,
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
  },
  body: 'grant_type=client_credentials'
};

request.post(options, (e, r, body) => {
  request.get(
    {
      url: 'https://api.twitter.com/1.1/search/tweets.json',
      qs: {
        q: searchString,
        count: 5
      },
      headers: {
        authorization: 'Bearer ' + JSON.parse(body).access_token
      }
    },
    (e, r, body) => {
      const statuses = (JSON.parse(body).statuses);
      for (let i = 0; i < statuses.length; i++) {
        console.log(`[${statuses[i].id}] ${statuses[i].text} by ${statuses[i].user.name}\n`);
      }
    }
  );
});
