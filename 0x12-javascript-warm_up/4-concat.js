#!/usr/bin/node

const args = process.argv.slice(2);

if (!args[2]) {
  console.log(args[0] + ' is ' + args[1]);
}
