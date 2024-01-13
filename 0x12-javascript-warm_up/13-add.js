#!/usr/bin/node

// Define a function named add that takes two parameters and returns their sum
function add (a, b) {
  return a + b;
}

// Make the function visible outside the file
module.exports = {
  add: add
};
