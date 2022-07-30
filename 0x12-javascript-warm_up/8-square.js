#!/usr/local/bin/node

const num = parseInt(process.argv[2]);

if (process.argv[2] === undefined) {
  console.log('Missing size');
}
for (let i = 0; i < num; i++) {
  console.log('X'.repeat(num));
}
