#!/usr/bin/node
const x = parseInt(process.argv[2]);
if (isNaN(x)) {
  console.log(1);
}

function factorial (a) {
  if (a === 0) {
    return 1;
  } else {
    return a * (factorial(a - 1));
  }
}

console.log(factorial(x));
