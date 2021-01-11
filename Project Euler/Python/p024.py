import itertools

digits = list(range(10))

answer = itertools.islice(itertools.permutations(digits), 999999, None)

print("".join(str(i) for i in next(answer)))