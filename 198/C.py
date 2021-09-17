import math
r, x,y = map(int,input().split())

dist = (x**2+y**2)**0.5

ans = math.ceil(dist/r)
if dist >= r:
    print(ans)
else:
    print(ans+1)
