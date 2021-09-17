n = int(input())

tree_list = [int(key) for key in input().split()]
sum = 0

for i in range(n):
    if tree_list[i] -10 > 0:
        sum += tree_list[i]-10

print(sum)
