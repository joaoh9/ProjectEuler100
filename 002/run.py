first = 1
second = 2

_next = second + first

sumEven = 2

while _next < 4000000:
  if _next % 2 == 0:
    sumEven += _next
  
  first = second
  second = _next
  _next = second + first


print(sumEven)
