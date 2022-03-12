N, M = map(int, input().split())
A_ls = [int(key) for key in input().split()]
A_hash = {}
for a in A_ls:
    if a in A_hash:
        A_hash[a] += 1
    else:
        A_hash[a] = 1

B_ls = [int(key) for key in input().split()]
B_hash = {}
for b in B_ls:
    if b in B_hash:
        B_hash[b] += 1
    else:
        B_hash[b] = 1



for b in B_hash.keys():
    if b not in A_hash or A_hash[b] < B_hash[b]:
        print("No")
        exit()
print("Yes")
