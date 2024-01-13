#!/usr/bin/node

// Check if there are at least two arguments
if (process.argv.length < 4) {
  // Print 0 if there are no or only one argument
  console.log(0);
} else {
  // Convert all arguments to integers
  const numbers = process.argv.slice(2).map(Number);

  // Sort the array in descending order
  const sortedNumbers = numbers.sort((a, b) => b - a);

  // Print the second element (index 1) in the sorted array
  console.log(sortedNumbers[1]);
}
