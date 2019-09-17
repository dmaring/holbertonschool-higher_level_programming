#!/usr/bin/node
const x = parseInt(process.argv[2]);
if (x === undefined || isNaN(x)) {
  console.log(1);
} else {
  console.log(factorial(x));
}

function factorial (a) {
  if (a === 0) {
    return 1;
  } else {
    return a * (factorial(a - 1));
  }
}
