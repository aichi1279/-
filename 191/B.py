n,x = map(int,input().split())

A_list = list(map(int,input().split()))


ans_list = []
for key in A_list:
    if key != x:
        ans_list.append(key)

for key in ans_list:
    print(key,end=" ")

print()
