N = int(input())

list = []
maxi = 0
sum = 0
for _ in range(N-1):
    u,v,w = map(int,input().split())
    list.append((u,v,w))
    if w > maxi:
        maxi = w
    sum += maxi

ans = sum
for key in list:
    sum -= key[2]
    if key[2] == maxi:
        tmp = list.copy()
        tmp.remove(maxi)
        maxi = max(tmp)

    ans += sum

print(ans)
