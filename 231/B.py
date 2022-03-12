N = int(input())
hash = {}
for _ in range(N):
    name = input()
    if name in hash:
        hash[name] += 1
    else:
        hash[name] = 1

sorted_hash = sorted(hash.items(), key=lambda x:x[1],reverse=True)
print(sorted_hash[0][0])
