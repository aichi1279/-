n = int(input())

sum=1
for i in range(2,n+1):
    flag=0
    if sum%i ==0:
        continue
    elif i==25:
        sum *=5
        continue
    elif i==16:
        sum*=2
        continue
    sum *= i

sum += 1
if sum >= n and sum <= 10**13:
    print(sum)
