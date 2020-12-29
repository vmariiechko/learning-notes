def Fibonacci(n):
	a, b = 1, 2

	if n in [1,2]:
		return n

	for i in range(n-2):
		a, b = b, a+b

	return b

n = 1
s = 0

while True:
	fib = Fibonacci(n)

	if fib >= 4000000:
		break
	elif fib % 2 == 0:
		s += fib

	n += 1

print(s)
