h ,w = map(int, input().split())

square_list=[]
mini = 100
for i in range(h):
    list = [int(i) for i in input().split()]
    for key in list:
        mini = min(mini,key)

    square_list.append(list)


sum = 0
for i in range(h):
    for j in range(w):
        sum += square_list[i][j]-mini

print(sum)
