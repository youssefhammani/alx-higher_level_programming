#!/usr/bin/node

// Define the myObject with type and value properties
const myObject = {
  type: 'object',
  value: 12
};

console.log(myObject);

// Add a new function named incr to myObject that increments the value property
myObject.incr = function () {
  this.value += 1;
};

myObject.incr();
console.log(myObject);

myObject.incr();
console.log(myObject);

myObject.incr();
console.log(myObject);
