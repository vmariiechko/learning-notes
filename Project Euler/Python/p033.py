from math import gcd


# Brute force method (faster)
numerator = 1
dominator = 1
for n in range(11,99):

	if n % 10 == 0 or n % 11 == 0:
		continue

	n_str = str(n)

	for d in range(int(n_str[1]+'1'), int(n_str[1]+'9')+1):

		d_str = str(d)

		if n / d == int(n_str[0]) / int(d_str[1]):
			numerator *= n
			dominator *= d

print(dominator // gcd(numerator,dominator))


# Clever method (slower)
# n = 10*n1 + n0
# d = 10*d1 + d0
numerator = 1
dominator = 1
for d in range(12, 100):

	d0 = d % 10
	d1 = d // 10

	for n in range(10, d):

		n0 = n % 10
		n1 = n // 10

		if (n0 == d1 and n1*d == n*d0) or (n1 == d0 and n0*d == n*d1):
			numerator *= n
			dominator *= d

print(dominator // gcd(numerator,dominator))