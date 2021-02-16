def is_pandigital(num):
	return "".join(sorted(str(num))) == '123456789'


answer = "1"

for i in range(9,9999):

	temp = "".join([str(i*n) for n in range(1,6)])

	if is_pandigital(temp[:9]):
		answer = max(answer, temp)

print(answer[:9])