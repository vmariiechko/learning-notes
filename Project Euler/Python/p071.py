from math import floor

LIMIT = 1000000

maxnumerator = 0
maxdenominator = 1

for d in range(1, LIMIT + 1):
	n = floor(d * 3 / 7)

	if d % 7 == 0:
		n -= 1

	if n * maxdenominator > d *maxnumerator:
		maxnumerator = n
		maxdenominator = d

print(maxnumerator)