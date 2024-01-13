#!/usr/bin/node

// Check if at least two arguments are passed and print them in the specified format
if (process.argv[2] && process.argv[3]) {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
} else {
  console.log('undefined is undefined');
}
