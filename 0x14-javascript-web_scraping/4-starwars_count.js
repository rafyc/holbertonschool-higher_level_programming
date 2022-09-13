#!/usr/bin/node

const axios = require('axios');
let count = 0;

axios.get(process.argv[2])
  .then((response) => {
    const numFilm = response.data.results.length;
    for (let i = 0; i < numFilm; i++) {
      const numChar = response.data.results[i].characters.length;
      for (let j = 0; j < numChar; j++) {
        const compChar = response.data.results[i].characters[j];
        if (compChar.includes('18')) {
          count += 1;
        }
      }
    } console.log(count);
  })
  .catch(err => {
    console.log(err);
  });
