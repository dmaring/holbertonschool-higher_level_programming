#!/usr/bin/node
let count = 0;
exports.logMe = function (item) {
  function increase () {
    count++;
    console.log(count + ': ' + item);
  }
  increase();
};
