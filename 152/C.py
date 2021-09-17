n = int(input())
n_list = list(map(int,input().split()))

count = 1
mini = n_list[0]

for i in range(1,n):
    if mini > n_list[i]:
        count += 1
        mini = n_list[i]


print(count)
