from math import sqrt, floor, log


# Brute force solution:
def evenly_divisible(num):
	for i in range(2,21):
		if num % i > 0:
			return False
	return True


answer = 0

for i in range(2520,999999999,10):
	if evenly_divisible(i):
		answer = i
		print(i)
		break

print(answer)


# Second solution:
n = 20	# range of numbers from 2 to 20
p = [2,3,5,7,11,13,17,19]	# prime numbers
limit = sqrt(n)
a = [1 for i in range(len(p))]	# power of prime numbers

for i in range(len(p)):
	if p[i] < limit:
		a[i] = floor( log(n)/log(p[i]) )
	else:
		break

answer = 1

for i in range(len(p)):
	answer *= p[i]**a[i]

print(answer)