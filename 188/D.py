n, C = map(int, input().split())

list = []
maxi = 0
for i in range(n):
    a,b,c = map(int,input().split())
    if a == b:
        list.append((a,c,i))
        continue
    if maxi < b:
        maxi = b

    list.append((a,c,i))
    list.append((b,c,i))

list.sort()

time_list = [0]*b
botom_list=[]
sum = 0
for i in range(len(list)):
    if list[i][2] in botom_list:
        time_list[list[i][0]-1] += sum
        sum -= list[i][1]
        continue
    sum += list[i][1]
    time_list[list[i][0]-1] += sum
    botom_list.append(list[i][2])

cost = 0
print(time_list)
for i in range(len(time_list)):
    if time_list[i] > C:
        cost += C
    else:
        cost += time_list[i]

print(cost)
