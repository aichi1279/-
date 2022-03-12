N, W = map(int,input().split())
AB_list = []
for _ in range(N):
    a,b = map(int,input().split())
    AB_list.append((a,b))

AB_list = sorted(AB_list, reverse=True)

#print(AB_list)
ans = 0
for tup in AB_list:
    if W-tup[1]>=0:
        W -= tup[1]
        ans += tup[0]*tup[1]
    elif W>=0 and W-tup[1] < 0:
        ans += tup[0]*W
        break
print(ans)
