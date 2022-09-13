#!/usr/bin/node

const axios = require('axios');

axios.get('https://swapi-api.hbtn.io/api/films/' + process.argv[2])
  .then(function (response) {
    console.log(response.data.title);
  })
  .catch(err => {
    console.log(err);
  });
