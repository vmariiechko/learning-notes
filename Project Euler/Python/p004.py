from eulertools import is_palindrome


# First solution:
answer = 0

for i in range(500,999):
	for j in range(500,999):
		if is_palindrome(str(i*j)):
			answer = i*j if answer < i*j else answer

print(answer)


# Second solution (faster)
l = [i*j for i in range(500,999) for j in range(500,999) if is_palindrome(str(i*j))]

print(max(l))