SQUARES = [(i**2 // 10, i**2 % 10) for i in range(1, 10)]


def Hamming_weight(num):
	return bin(num).count("1")


def is_valid_arrangement(x, y):
	if test_bit(x, 6) or test_bit(x, 9):
		x |= 64 | 512
	if test_bit(y, 6) or test_bit(y, 9):
		y |= 64 | 512

	return all((test_bit(x,tens) and test_bit(y,ones)) or
			   (test_bit(x,ones) and test_bit(y,tens)) 
			   for (tens,ones) in SQUARES)


def test_bit(x, i):
	return ((x >> i) & 1) != 0


# binomial(10,6)=210 for one cube, as we have two cubes: 
# 210*210=44100 - possible arrangements to check
answer = sum(1
			 for i in range(2**10)
			 for j in range(i, 2**10)
			 if Hamming_weight(i) == Hamming_weight(j) == 6 and is_valid_arrangement(i, j))
print(answer)