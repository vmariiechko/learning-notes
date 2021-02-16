def has_same_digits(a,b):
	return sorted(str(a)) == sorted(str(b))


x = 1
while True:
	if all(has_same_digits(x, x*i) for i in [2,3,4,5,6]):
		answer = x
		break

	x += 1

print(answer)