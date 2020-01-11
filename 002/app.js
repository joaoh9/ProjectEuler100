let first = 1;
let second = 2;

let next = second + first;

let sumEven = 2;

while (next < 4000000) {
  if (next % 2 == 0) {
    sumEven += next;
  }
  first = second;
  second = next;
  next = second + first;
}

console.log(sumEven);
