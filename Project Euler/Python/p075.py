from eulertools import sqrt
from math import gcd 

LIMIT = 1500000


triples = set()
for i in range(3, sqrt(LIMIT) + 1, 2):
	for j in range(i - 2, 0, -2):
		if gcd(i, j) == 1:
			a = i * j
			b = (i**2 - j**2) // 2
			c = (i**2 + j**2) // 2

			if a + b + c <= LIMIT:
				triples.add((a, b, c))

ways = [0] * (LIMIT + 1)
for triple in triples:
	sigma = sum(triple)

	for i in range(sigma, len(ways), sigma):
		ways[i] += 1

print(ways.count(1))