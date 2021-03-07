from itertools import count


with open("p079_keylog.txt", "r") as f:
	login_attempts = f.readlines()
login_attempts = [i.replace("\n", "") for i in login_attempts]


def is_consistent(guess):
	return all(is_subsequence(s, guess) for s in login_attempts)


def is_subsequence(attempt, guess):
	i = 0

	for c in guess:
		if c == attempt[i]:
			i += 1
			if i == len(attempt):
				return True

	return False


unique_chars = sorted(set(). union(*login_attempts))
base = len(unique_chars)


def calc_answer(): 
	for length in count(base):
		indexes = [0] * length

		while True:
			guess = "".join(unique_chars[j] for j in indexes)

			if is_consistent(guess):
				return guess

			i = 0
			while i < length and indexes[i] == base - 1:
				indexes[i] = 0
				i += 1

			if i == length:
				break
			indexes[i] += 1


print(calc_answer())