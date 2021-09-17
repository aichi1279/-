a,b,c,d = map(int,input().split())


red = 0
dist1,dist2 = 1, 0
while a > red*d:
    if dist1-dist2<=0:
        print(-1)
        exit()
    dist1 = abs(a - red*d)
    red += c
    a += b
    dist2 = abs(a - red*d)

print(red//c)
