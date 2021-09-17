import math

h, w ,a ,b = map(int,input().split())

all = 0
mem = set()
for i in range(h):
    for j in range(w):
        print('. ',end="")
        if i+1<=h and str((i,j))+':'+str((i+1,j)) not in mem and str((i+1,j))+':'+str((i,j)) not in mem:
            mem.add(str((i,j))+':'+str((i+1,j)))
        if i+1<=w :
            mem.add(str((i,j))+':'+str((i,j+1)))
            mem.add(str((i,j+1))+':'+str((i,j)))
    print()


all = h * (w-1) * 2
