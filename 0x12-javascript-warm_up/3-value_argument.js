#!/usr/bin/node

// Check if any argument is passed and print the first argument
if (process.argv[2]) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
