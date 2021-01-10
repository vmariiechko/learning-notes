with open("p022_names.txt", "r") as file:
	names = file.read()

names = names.replace('","', ' ').replace('"','')
l_names = list(names.split(" "))
l_names = sorted(l_names)

print(l_names[937])
print(ord(l_names[937][1])-64)

answer = 0 

for i in range(len(l_names)):

	apha_val = 0

	for letter in l_names[i]:
		apha_val += ord(letter)-64

	answer += (i+1) * apha_val

print(answer)