n,m = map(int, input().split())
if m==0:
    print(1)
    exit()

A_list = list(map(int,input().split()))
A_list.sort()
list = [i+1 for i in range(n)]

if A_list==list:
    print(0)
    exit()

A_list.append(0)
A_list.append(n)
A_list = set(A_list)
differ = n
for i in A_list:
    for j in A_list:
        if i == j:
            continue
        elif abs(i-j)< differ and differ > 1:
            differ = abs(i-j)-1

#print(differ)

A_list.remove(0)
for i in A_list:
    list[i-1] = 0

#print(list)
count=0s
for i in range(len(list)-differ+1):
    if list[i]==0:
        continue
    for j in range(differ):
        list[i+j] = 0
    count+=1
print(count)
