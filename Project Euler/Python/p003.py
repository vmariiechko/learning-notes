l = []
num = 600851475143

for i in range(1,9999,2):
	if num % i == 0 and num > 0:
		num /= i
		l.append(i)

print(l)