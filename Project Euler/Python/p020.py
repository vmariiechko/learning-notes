from math import factorial

fact = factorial(100)

l = list(map(int,str(fact)))

print(sum(l))

