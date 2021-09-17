n = int(input())

list = list(map(int,input().split()))

set = set()
for i in range(len(list)-2):
    for j in range(i+1,len(list)-1):
        for k in ragne(j+1,len(list)):
            maxi = max(list[i],list[j],list[k])
            mini = min(list[i],list[j],list[k])
            if maxi != key[i] and mini != key[i]:
                mid = key[i]
            elif  maxi != key[j] and mini != key[j]:
                mid = key[j]
            else:
                mid = key[k]
            set.add((maxi,mid,mini))

count = 0
for key in set:
    if key[0] < key[1]+key[2]:
        count += 1
print(count)
