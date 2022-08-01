#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
} else {
  const myNum = [];
  for (let i = 2; i < process.argv.length; i++) {
    myNum.push(parseInt(process.argv[i]));
  }
  myNum.sort();
  console.log(myNum[myNum.length - 2]);
}
