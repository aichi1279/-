N, Q = map(int, input().split())
A_ls = [int(key) for key in input().split()]
hash = {}
for i,key in enumerate(A_ls):
    if key in hash:
        hash[key].append(i)
    else:
        hash[key] = [i]

for _ in range(Q):
    x, k = map(int, input().split())
    if x not in hash or len(hash[x]) < k:
        print(-1)
        continue

    print(hash[x][k-1]+1)
    
