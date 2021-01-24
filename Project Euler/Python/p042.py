# Read all words
with open("p042_words.txt", "r") as file:
	words = file.read()


# Transfer/Initialize
words = words[1:][:-1].split('","')
triangle_nums = [1]


def calculate_word_value(word):
	return sum([ord(letter) - ord("A") + 1 for letter in word])


# Calculate all triangle words up to the possible maximum
max_len = len(max(words))
max_letter = (ord("Z")-ord("A")+1)
max_triangle_num = max_len * int(0.5*max_letter*(max_letter+1))
i = 2
while triangle_nums[-1] < max_triangle_num + 1:
	triangle_nums.append(int(0.5*i*(i+1)))
	i += 1


answer = sum(1 for word in words if calculate_word_value(word) in triangle_nums)
print(answer)