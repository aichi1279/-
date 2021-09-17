n ,a ,x ,y = map(int,input().split())

if a >= n:
    print(x*n)
else:
    print( (x*a+y*(n-a)) )
