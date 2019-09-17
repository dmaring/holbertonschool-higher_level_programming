#!/usr/bin/node
const x = parseInt(process.argv[2]);
if (isNaN(x)) {
  console.log('Missing size');
} else if (x === 1) {
  console.log('X');
} else {
  let row = 'X';
  for (let t = 0; t < x - 1; t++) {
    row = row + 'X';
  }
  for (let i = 0; i < x; i++) {
    console.log(row);
  }
}
