n, m = map(int,input().split())
H = list(map(int,input().split()))

set = {i+1 for i in range(n)}
for i in range(m):
    a,b = map(int,input().split())

    if a in set and H[a-1] <= H[b-1]:
        set.remove(a)
    if b in set and H[a-1] >= H[b-1]:
        set.remove(b)


print(len(set))
l
