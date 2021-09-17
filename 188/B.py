n = int(input())

A_list = list(map(int,input().split()))
B_list = list(map(int,input().split()))

sum = 0
for i in range(n):
    sum += A_list[i]*B_list[i]

if sum == 0:
    print("Yes")
else:
    print("No")
