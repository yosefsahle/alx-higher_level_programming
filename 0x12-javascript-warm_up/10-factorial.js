#!/usr/bin/node
const firstArg = process.argv[2];
function factorial (firstArg) {
  if (isNaN(firstArg) || firstArg === 1) {
    return (1);
  } else {
    return (firstArg * factorial(firstArg - 1));
  }
}
console.log(factorial(parseInt(firstArg)));
