def is_double_palindrome(num):
	l_decimal = [int(x) for x in str(num)]
	l_binary = [x for x in str(bin(num))][2:]


	if l_decimal[:] == l_decimal[::-1] and l_binary[:] == l_binary[::-1]:
		return True

	return False


answer = sum(i for i in range(1000000) if is_double_palindrome(i))

print(answer)