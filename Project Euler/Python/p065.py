denominator = 0
numerator = 1


def e_term(i):
	if i == 0:
		return 2
	elif i % 3 == 2:
		return i // 3 * 2 + 2
	else:
		return 1


for i in reversed(range(100)):
	numerator, denominator = e_term(i) * numerator + denominator, numerator

answer = sum(int(char) for char in str(numerator))
print(answer)