#!/usr/bin/node

const num = parseInt(process.argv[2]);

if (process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
}
for (let i = 0; i < num; i++) {
  console.log('C is fun');
}
