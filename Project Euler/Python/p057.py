LIMIT = 1000

answer = 0
numerator = 0
denominator = 1

for _ in range(LIMIT):
	numerator, denominator = denominator, denominator*2 + numerator

	if len(str(numerator + denominator)) > len(str(denominator)):
		answer += 1

print(answer)