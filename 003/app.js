const GOAL_NUMBER = 600851475143;

function log(n) {
  console.log(n);
}

let primes = [2];

function getArr(start, end) {
  const arr = [];
  for (let i = start; i < end; i += 1) {
    arr.push(i);
  }
  return arr;
}

function nextPrime(lastPrime, arr) {
  let i = lastPrime + 1;
  while (arr[i] == false) {
    i += 1;
  }
  primes.push(arr[i]);
  return arr[i];
}

function erastothenes(prime, arr, end) {
  for (let i = prime + prime; i < end; i += prime) {
    arr[i] = false;
  }
}

let np = 2;

let start = 0;
let end = 100;

const arr = getArr(start, end);
arr[0] = false;
arr[1] = false;

while (end < 10000) {
  while (np < end) {
    erastothenes(np, arr, end);
    np = nextPrime(np, arr);
    console.log(np);
  }
  start += end + 1;
  end += end;
}

const first1000primes = arr.filter(e => e != false);
//console.log(first1000primes);
