S = list(input())

hash = {}
for key in S:
    if key in hash:
        hash[key] += 1
    else:
        hash[key] = 1

sorted_ls = sorted(hash.items(), key=lambda x:x[0])

ans = ""
for pair in sorted_ls:
    ans += pair[0]*pair[1]

print(ans)
