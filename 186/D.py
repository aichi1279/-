import copy

n = int(input())

list = list(map(int, input().split()))
for i in range(len(list)-1):
    list[i+1] -= list[i]

sub_list = copy.copy(list)

sum = 0
for i in range(n):
    for key in sub_list[i:]:
        sum += abs(sub_list[i]-key)

    sub_list = copy.copy(list)

print(sum)
