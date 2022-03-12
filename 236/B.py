N = int(input())
A_ls = [int(key) for key in input().split()]

hash = {}
for key in A_ls:
    if key in hash:
        hash[key] += 1
    else:
        hash[key] = 1

for key in hash.keys():
    if hash[key]!=4:
        print(key)
        exit()
