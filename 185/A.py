a1,a2,a3,a4 = map(int, input().split())

tmp = min(a1,a2)
tmp2 = min(a3,a4)
ans = min(tmp,tmp2)

print(ans)
