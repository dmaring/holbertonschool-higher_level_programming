#!/usr/bin/node
const len = process.argv.length;
if (len < 3) {
  console.log(0);
} else if (len === 3) {
  console.log(0);
} else {
  const args = process.argv.slice(2);
  args.sort(function (a, b) { return a - b; });
  args.reverse();
  console.log(parseInt(args[1]));
}
