import sys
from math import sqrt, gcd, ceil

s = 1000

# Brute force
for a in range(3, int((s-3)/3) ):
	for b in range(a+1, int((s-a-1)/2) ):
		
		c = s - a - b

		if a*a + b*b == c*c:
			print(a,b,c)
			print(a*b*c)
			sys.exit()


# Parametrisation
s2 = s/2
mlimit = ceil(sqrt(s2))-1

for m in range(2,mlimit):

	if s2 % m == 0:
		sm = s2 / m

		while sm % 2 == 0:
			sm = sm / 2

		if m % 2 == 1:
			k = m+2
		else:
			k = m+1

		while k < 2*m and k <= sm:
			if sm % k == 0 and gcd(k,m) == 1:
				d = s2 / (k*m)
				n = k-m
				a = d*(m*m-n*n)
				b = 2*d*m*n
				c = d*(m*m+n*n)
				print(a,b,c)
				print(a*b*c)

			k = k+2