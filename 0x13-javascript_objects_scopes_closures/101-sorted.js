#!/usr/bin/node
const dict = require('./101-data').dict;
const nullDict = {};

for (const key in dict) {
  if (nullDict[dict[key]] !== undefined) {
    nullDict[dict[key]].push(key);
  } else {
    nullDict[dict[key]] = [key];
  }
}

console.log(nullDict);
