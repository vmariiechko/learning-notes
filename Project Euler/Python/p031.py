num_ways_to_form_sum = [1] + [0] * 200
COINS = [1, 2, 5, 10, 20, 50, 100, 200]

for coin in COINS:
	for j in range(len(num_ways_to_form_sum) - coin):
		num_ways_to_form_sum[j + coin] += num_ways_to_form_sum[j]

print(num_ways_to_form_sum[-1])