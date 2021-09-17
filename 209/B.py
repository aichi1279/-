n,x = map(int,input().split())
A_list = [int(key) for key in input().split()]

for i in range(len(A_list)):
    if (i+1) %2 == 0:
        A_list[i] -= 1

if x >= sum(A_list):
    print("Yes")
else:
    print("No")
