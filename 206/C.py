n = int(input())

A_list = [int(key) for key in input().split()]
hash = {}
for key in A_list:
    if key in hash:
        hash[key] += 1
    else:
        hash[key] = 1


import math
def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

All = comb(n,2)

for key in hash.keys():
    if hash[key]>=2:
        All -= comb(hash[key],2)

res = All
print(res)
