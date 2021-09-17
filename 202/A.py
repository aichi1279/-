list = [int(i) for i in input().split()]
list.sort()

if (list[1]-list[0])==(list[2]-list[1]):
    print("Yes")
else:
    print("No")
