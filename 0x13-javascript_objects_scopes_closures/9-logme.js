#!/usr/bin/node
let counta = 0;

exports.logMe = function (item) {
  console.log(`${counta}: ${item}`);
  counta += 1;
};
