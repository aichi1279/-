N = int(input())

l = [0]*N
r = [0]*N
for i in range(N):
    t, l[i], r[i] = map(int,input().split())
    if t==2:
        r[i]-= 0.1
    elif t==3:
        l[i] += 0.1
    elif t==4:
        l[i] += 0.1
        r[i]-= 0.1

ans = 0
for i in range(N):
    for j in range(i+1,N):
        #if (max(l[i],l[j]) <= min(r[i],r[j])):
        #    print("[{},{}]:[{},{}] ".format(l[i],r[i], l[j],r[j]))
        ans += (max(l[i],l[j]) <= min(r[i],r[j]))

print(ans)
