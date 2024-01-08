#!/usr/bin/node

const args = process.argv.slice(2);

if (args === undefined) {
  console.log('Not a number');
} else {
  const intValue = parseInt(args);
  if (isNaN(intValue)) {
    console.log('Not a number');
  } else {
    console.log('My number:',intValue);
  }
}
