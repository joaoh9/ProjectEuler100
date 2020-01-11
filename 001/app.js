const max = 1000;
let x3 = 3;
let x5 = 5;

let total = 0;

while (x3 < 1000) {
  total += x3;
  x3 += 3;
}

while (x5 < 1000) {
  total += x5;
  x5 += 5;
}

let x15 = 15;
let minus = 0;

while (x15 < 1000) {
  minus += x15;
  x15 += 15;
}

console.log(total - minus);
