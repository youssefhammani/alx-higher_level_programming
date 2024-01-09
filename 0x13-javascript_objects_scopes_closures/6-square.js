#!/usr/bin/node

const SquareParent = require('./5-square');

class Square extends SquareParent {
  constructor (size) {
    super(size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
	    let s = '';
	    for (let j = 0; j < this.width; j++) {
		    s +=c;
	    }
    }
  }
}

module.exports = Square;
