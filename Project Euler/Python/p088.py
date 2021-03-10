LIMIT = 12000
min_product_sum = [None] * (LIMIT + 1)


def factorize(num, maxfactor, remain, k, sum):
	if remain == 1:
		if sum > num:
			raise AssertionError()

		k += num - sum

		if k <= LIMIT and (min_product_sum[k] is None or num < min_product_sum[k]):
			min_product_sum[k] = num
	else:
		for i in range(2, maxfactor + 1):
			if remain % i == 0:
				factor = i
				factorize(num, min(factor, maxfactor), remain // factor, k + 1, sum + factor)


# Possible max solution for k doesn't exceeds 2k 
for i in range(2, LIMIT * 2 + 1):
	factorize(i, i, i, 0, 0)

answer = sum(set(min_product_sum[2:]))
print(answer)