import math
x,y,a,b = map(int , input().split())

exp=0

while True:
    if x*a > x+b:
        count = int((y-x)/b)
        if count<=0 or y<x:
            print(exp)
            exit()
        x += b*count
        exp += count
        
    else:
        x *= a
        if  y<x:
            print(exp)
            exit()
        exp +=1
