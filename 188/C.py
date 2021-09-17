n = int(input())

A_list = list(map(int,input().split()))

A_front = A_list[:(2**n)//2]
A_back = A_list[(2**n)//2:]

list1 = []
count = 0
for talent in A_front:
    count += 1
    if len(list1)==0 or list1[0] < talent:
        list1 = []
        list1.append(talent)
        list1.append(count)

list2 = []
count = (2**n)//2
for talent in A_back:
    count += 1
    if len(list2)==0 or list2[0] < talent:
         list2 = []
         list2.append(talent)
         list2.append(count)


if list1[0] > list2[0]:
    print(list2[1])
else:
    print(list1[1])
