#!/usr/bin/node

const axios = require('axios');

axios.get(process.argv[2])
  .then(res => {
    console.log('Code: ', res.status);
  })
  .catch(err => {
    console.log('Code: ', err.response.status);
  });
