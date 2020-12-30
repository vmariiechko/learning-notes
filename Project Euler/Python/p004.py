def is_palindrome(num):
	l = [int(x) for x in str(num)]

	if l[:] == l[::-1]:
		return True

	return False

# First solution:
answer = 0

for i in range(500,999):
	for j in range(500,999):
		if is_palindrome(i*j):
			answer = i*j if answer < i*j else answer

print(answer)

# Second solution (faster)
l = [i*j for i in range(500,999) for j in range(500,999) if is_palindrome(i*j)]

print(max(l))