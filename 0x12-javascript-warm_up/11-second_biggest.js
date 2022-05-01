#!/usr/bin/node
// The script searches the second biggest integer in the list of argument
if (process.argv[3]) {
  let BIG = parseInt(process.argv[2]);
  let secondBig = NaN;
  let temp;
  for (let i = 3; i < process.argv.length; i++) {
    temp = parseInt(process.argv[i]);
    if (temp > BIG) {
      secondBig = BIG;
      BIG = temp;
    } else if (isNaN(secondBig)) {
      secondBig = temp;
    } else if (temp > secondBig) {
      secondBig = temp;
    }
  }
  console.log(secondBig);
} else {
  console.log(0);
}
