from eulertools import Fibonacci_closure


fib = Fibonacci_closure()

while True:
	num, i = fib()

	if len(str(num)) == 1000:
		print(i)
		break