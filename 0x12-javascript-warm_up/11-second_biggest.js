#!/usr/bin/node
const len = process.argv.length;
if (len < 3) {
  console.log(0);
} else if (len === 3) {
  console.log(1);
} else {
  const args = process.argv.slice(2);
  args.sort();
  args.reverse();
  console.log(args[1]);
}
