#!/usr/bin/node
const myList = require('./100-data').list;
const mapFunc = function (num, index) {
  return (num * index);
};
const mapList = myList.map(mapFunc);

console.log(myList);
console.log(mapList);
