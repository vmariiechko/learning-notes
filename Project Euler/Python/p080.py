from eulertools import sqrt

DIGITS = 100
MULTIPLIER = 100**DIGITS

answer = sum( 
	sum(int(c) for c in str(sqrt(i * MULTIPLIER))[:DIGITS]) 
	for i in range(DIGITS)
	if sqrt(i)**2 != i
	)
print(answer)