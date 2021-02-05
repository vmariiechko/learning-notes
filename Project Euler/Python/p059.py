with open('p059_cipher.txt', 'r') as f:
	cipher = f.readlines()

ciphertext = cipher[0].split(',')
a_to_z_ascii = [ord('a'), ord('z')+1]


def count_score(plaintext):
	result = 0

	for char in plaintext:
		if 65 <= char <= 90:
			result += 1
		elif 97 <= char <= 123:
			result += 2
		elif char == 0x7F or char < 0x20:
			result -= 5

	return result


def decrypt(ciphertext, key):
	return [(int(c) ^ key[i % len(key)]) for (i, c) in enumerate(ciphertext)]


original_key = max(((x,y,z) for x in range(*a_to_z_ascii)
				    		for y in range(*a_to_z_ascii)
				    		for z in range(*a_to_z_ascii)),
					key=lambda key: count_score(decrypt(ciphertext, key)))

answer = sum(decrypt(ciphertext, original_key))
print(answer)