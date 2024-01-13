#!/usr/bin/node

// Function to add two integers
function add (a, b) {
  return parseInt(a) + parseInt(b);
}

// Check if both arguments are provided
if (process.argv[2] && process.argv[3]) {
  // Call the add function and use console.log(...) to print the result
  console.log(add(process.argv[2], process.argv[3]));
} else {
  // Print an error message if any argument is missing
  console.log("NaN");
}
