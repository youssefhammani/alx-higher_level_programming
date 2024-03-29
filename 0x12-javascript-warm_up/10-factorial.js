#!/usr/bin/node

// Recursive function to compute the factorial
function factorial (n) {
  // Base case: factorial of 0 or 1 is 1
  if ((isNaN(n)) || n === 1) {
    return 1;
  } else {
    // Recursive case: n! = n * (n-1)!
    return n * factorial(n - 1);
  }
}

console.log(factorial(parseInt(process.argv[2])));
