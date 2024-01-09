#!/usr/bin/node

const args = process.argv.slice(2);
if (args.length >= 2) {
  function add (a, b) {
    return a + b;
  }
  const result = add(parseInt(args[0]), parseInt(args[1]));
  console.log(result);
}
