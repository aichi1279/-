N, P = map(int,input().split())
A_list = [int(key) for key in input().split()]

cnt = 0
for key in A_list:
    if P > key:
        cnt+=1

print(cnt)
