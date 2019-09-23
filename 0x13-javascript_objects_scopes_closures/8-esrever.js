#!/usr/bin/node
exports.esrever = function (list) {
  const retArray = [];
  for (let i = list.length - 1; i >= 0; i--) {
    retArray.push(list[i]);
  }
  return (retArray);
};
