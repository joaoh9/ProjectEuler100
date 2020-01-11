import functools

x3 = 3
x5 = 5
total = 0

while x3 < 1000:
  total += x3
  x3 += 3


while x5 < 1000:
  total += x5
  x5 += 5


x15 = 15
minus = 0

while x15 < 1000:
  minus += x15;
  x15 += 15

print(total - minus)
