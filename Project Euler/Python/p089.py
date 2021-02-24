# *empty*, I, II, III, IV, V, VI, VII, VIII, IX
DIGIT_LENGTHS = [0, 1, 2, 3, 2, 1, 2, 3, 4, 2]
PREFIXES = [
	("M" , 1000),
	("CM",  900),
	("D" ,  500),
	("CD",  400),
	("C" ,  100),
	("XC",   90),
	("L" ,   50),
	("XL",   40),
	("X" ,   10),
	("IX",    9),
	("V" ,    5),
	("IV",    4),
	("I" ,    1),
]


with open("p089_roman.txt", "r") as f:
	roman_numerals = f.readlines()

roman_numerals = [num.replace("\n", "") for num in roman_numerals]


def parse_numeral(num):
	result = 0 

	while len(num) > 0:
		for (pref, val) in PREFIXES:
			if num.startswith(pref):
				result += val
				num = num[len(pref) : ]
				break

	return result


def numeral_len(num):
	result = 0

	if num >= 4000:
		result += 2

	while num > 0:
		result += DIGIT_LENGTHS[num % 10]
		num //= 10
	return result


answer = sum(len(num) - numeral_len(parse_numeral(num)) for num in roman_numerals)
print(answer)