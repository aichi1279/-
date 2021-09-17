n = int(input())

task_list = []
for  i in range(n):
    a,b = map(int,input().split())
    task_list.append((a,b))

rep = 10**6
ans = (0,0)
for i in range(len(task_list)):
    for j in range(len(task_list)):
        if i == j:
            if rep > (task_list[i][0]+task_list[i][1]):
                rep = task_list[i][0]+task_list[i][1]
            continue

        elif rep > max(task_list[i][0],task_list[j][1]):
            rep = max(task_list[i][0],task_list[j][1])
            ex = (task_list[i][0],task_list[j][1])
print(rep)
