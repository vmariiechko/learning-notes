def is_palindrome(num):
	return num == num[::-1]


def lychrel_num(num):

	for i in range(51):

		num = num + int(str(num)[::-1])

		if is_palindrome(str(num)):
			return False

	return True


answer = sum(1 for i in range(10000) if lychrel_num(i))
print(answer)