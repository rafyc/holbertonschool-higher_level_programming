#!/usr/local/bin/node

exports.esrever = function (list) {
  const newList = [];
  let i = list.length - 1;
  while (i >= 0) {
    newList.push(list[i]);
    i--;
  }
  console.log(list.length);
  return newList;
};
