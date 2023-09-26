#!/usr/bin/node
// This script reads and prints the content of a file.

const fs = require('fs');
const FileName = process.argv[2];
fs.readFile(FileName, 'utf8', function (err, line) {
  if (err) {
    console.log(err);
  } else {
    console.log(line);
  }
});
