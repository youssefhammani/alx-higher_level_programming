#!/usr/bin/node

// Define a function named addMeMaybe that increments a number and calls another function
exports.addMeMaybe = function (number, theFunction) {
  number += 1; // Increment the number
  theFunction(number); // Call the provided function with the incremented number
};
