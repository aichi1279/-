import math

n = int(input())

list = list(map(int, input().split()))
dict = [0]*10000

for key in list:
    for i in range(1,int(math.sqrt(key)+1)):
        if key%i==0 and  key/i != i:
            dict[i]+= 1
            dict[int(key/i)]+= 1
        elif key%i==0 and  key/i == i:
            dict[i]+= 1


direc = max(dict[2:])
i=0

for key in dict:
    if direc==key:
        ans=i
    i+=1
print(ans)
