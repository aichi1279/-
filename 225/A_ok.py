S = input()

hash = {}
ans = 6
for key in list(S):
    if key in hash:
        hash[key] += 1
    else:
        hash[key] = 1

def mul(n):
    res = 1
    for i in range(n):
        res *= i+1
    return res

for key in hash.keys():
    ans /= mul(hash[key])

print(int(ans))
