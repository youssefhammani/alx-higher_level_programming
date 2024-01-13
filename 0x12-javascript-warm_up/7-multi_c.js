#!/usr/bin/node
// prints 3 lines: (like 1-multi_languages.js) but by
// using an array of string and a loop

if (process.argv[2]) {
  const numOccurrences = parseInt(process.argv[2]);

  if (!isNaN(numOccurrences) && numOccurrences > 0) {
    for (let i = 0; i < numOccurrences; i++) {
      console.log('C is fun');
    }
  } else {
    console.log('Missing number of occurrences');
  }
} else {
  console.log('Missing number of occurrences');
}
