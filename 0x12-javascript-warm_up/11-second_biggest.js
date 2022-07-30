#!/usr/local/bin/node

const myNum = [];
for (let i = 2; i < process.argv.length; i++) {
  myNum.push(parseInt(process.argv[i]));
}

myNum.sort();
console.log(myNum[myNum.length - 2]);
