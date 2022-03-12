N = int(input())
AB = [[int(key) for key in input().split()] for _ in range(N-1)]

hash = {}
for key in AB:
    if key[0] in hash:
        hash[key[0]] += 1
    else:
        hash[key[0]] = 1

    if key[1] in hash:
        hash[key[1]] += 1
    else:
        hash[key[1]] = 1

for key in hash.keys():
    if hash[key]==N-1:
        print("Yes")
        exit()
print("No")
