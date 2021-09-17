import math

n = int(input())

list = list(map(int ,input().split()))

maxi = 0
sum = 0
squre_sum=0
for i in range(len(list)):
    if list[i]<0:
        list[i] *= -1
    if maxi<list[i]:
        maxi = list[i]
    sum += list[i]
    squre_sum += list[i]**2



print(sum)
print(math.sqrt(squre_sum))
print(maxi)
