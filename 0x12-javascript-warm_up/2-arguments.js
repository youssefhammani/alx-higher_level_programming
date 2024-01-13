#!/usr/bin/node

// Check the number of arguments passed
const numArgs = process.argv.length;

// Use console.log(...) to print the appropriate message based on the number of arguments
if (numArgs === 2) {
  console.log('No argument');
} else if (numArgs === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
