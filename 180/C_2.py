import math

n= int(input())

list=[]
for i in range(1, int(math.sqrt(n))+1):
    if n %i ==0 and n/i != i:
        list.append(i)
        list.append(int(n/i))
    elif  n %i ==0 and n/i == i:
        list.append(i)


list.sort()
for i in range(len(list)):
    print(list[i])
