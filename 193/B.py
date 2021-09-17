n = int(input())
mat = []
for i in range(n):
    a,p,x = map(int,input().split())
    mat.append((a,p,x))

ans = 0
for sk in mat:
    time = sk[0]
    price = sk[1]
    stock = sk[2]
    if ans > price and stock-time > 0:
        ans = price
    elif ans==0 and stock-time > 0:
        ans = price

if ans == 0:
    print(-1)
else:
    print(ans)
