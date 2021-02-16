from eulertools import Fibonacci_recursion


n = 1
s = 0

while True:
	fib = Fibonacci_recursion(n)

	if fib >= 4000000:
		break
	elif fib % 2 == 0:
		s += fib

	n += 1

print(s)