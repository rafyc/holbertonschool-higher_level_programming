#!/usr/local/bin/node
if (process.argv.length < 4) {
  console.log(0);
} else {
  const myNum = [];
  for (let i = 2; i < process.argv.length; i++) {
    if (!isNaN(process.argv[i])) myNum.push(process.argv[i]);
  }

  myNum.sort((a, b) => a - b);
  console.log(myNum);
  console.log(myNum[myNum.length - 2]);
}
