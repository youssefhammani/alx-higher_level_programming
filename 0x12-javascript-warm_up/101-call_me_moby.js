#!/usr/bin/node

// Define a function named callMeMoby that executes another function x times
function callMeMoby(x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}

// Make the function visible outside the file
module.exports = {
  callMeMoby: callMeMoby
};
