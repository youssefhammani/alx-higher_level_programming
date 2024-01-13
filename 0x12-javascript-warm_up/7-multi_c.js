#!/usr/bin/node

// Check if the first argument is provided
if (process.argv[2]) {
  // Convert the first argument to an integer
  const numOccurrences = parseInt(process.argv[2]);

  // Check if the conversion is successful
  if (!isNaN(numOccurrences) && numOccurrences > 0) {
    // Use a loop to print "C is fun" x times
    for (let i = 0; i < numOccurrences; i++) {
      console.log('C is fun');
    }
  } else {
    // Print an error message if the conversion fails or the number is not positive
    console.log('Missing number of occurrences');
  }
} else {
  // Print an error message if no argument is provided
  console.log('Missing number of occurrences');
}
