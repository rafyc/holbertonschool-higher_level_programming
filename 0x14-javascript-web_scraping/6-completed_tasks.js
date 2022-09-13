#!/usr/bin/node

const axios = require('axios');
const myDict = {};

axios.get(process.argv[2])
  .then((response) => {
    for (let i = 0; i < response.data.length; i++) {
      if (response.data[i].completed === true) {
        if (myDict[response.data[i].userId] === undefined) {
          myDict[response.data[i].userId] = 0;
        }
        myDict[response.data[i].userId] += 1;
      }
    }
    console.log(myDict);
  })
  .catch(err => {
    console.log(err);
  });
