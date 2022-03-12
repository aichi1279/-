N = int(input())
ps = []
for _ in range(N):
    x,y = map(int, input().split())
    ps.append((x,y))

ans = 0
for i in range(len(ps)-1):
    for j in range(i+1, len(ps)):
        dist = ((ps[i][0]-ps[j][0])**2 + (ps[i][1]-ps[j][1])**2)**0.5
        if dist > ans:
            ans = dist

print(ans)
