N = int(input())
A_list = [int(key) for key in input().split()]
X = int(input())

A_sum = 0
for key in A_list:
    A_sum += key
A_len = len(A_list)

loop = X//A_sum
cnt = loop * A_len
X -= (A_sum * loop)

ind = 0
for key in A_list:
    ind += key
    cnt += 1
    if X < ind:
        print(cnt)
        exit()
