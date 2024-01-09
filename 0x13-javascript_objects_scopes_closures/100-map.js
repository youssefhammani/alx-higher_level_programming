#!/usr/bin/node
const list = require('./100-datajs').list;
console.log(list);
console.log(list.map((value, index) => value * index));
