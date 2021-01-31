from math import comb

answer = sum(1 for i in range(1,101) for j in range(2,i-1) if comb(i,j) > 1000000)
print(answer)