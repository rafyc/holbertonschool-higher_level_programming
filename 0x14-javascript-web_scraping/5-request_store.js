#!/usr/bin/node
const fs = require('fs');
const axios = require('axios');

axios.get(process.argv[2])
  .then((response) => {
    fs.writeFile(process.argv[3], response.data, (err) => {
      if (err) throw err;
    });
  })
  .catch(err => {
    console.log(err);
  });
