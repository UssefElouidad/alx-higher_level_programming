#!/usr/bin/node

const args = process.argv.slice(2);
if (args.length >= 2) {
  function add (a, b) {
    return parseInt(a) + parseInt(b);
  }
  const result = add(args[0], args[1]);
  console.log(result);
}
