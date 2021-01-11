def Fibonacci():
	f1 = 1
	f2 = 1
	index = 2

	def get_next():
		nonlocal f1, f2, index
		f1, f2 = f2, f1+f2
		index += 1
		return (f2, index)

	return get_next

fib = Fibonacci()

while True:
	num, i = fib()

	if len(str(num)) == 1000:
		print(i)
		break