X,Y = map(int,input().split())

if Y-X <= 0:
    print(0)
else:
    ans = (Y-X)//10
    if (Y-X)%10!=0:
        ans += 1
    print(ans)
