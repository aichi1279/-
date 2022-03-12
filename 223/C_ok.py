N = int(input())
AB_ls = [[int(key) for key in input().split()] for _ in range(N)]
sec_ls = []
sec_sum = 0
for i in range(N):
    sec = AB_ls[i][0]*10**6
    sec /= AB_ls[i][1]
    sec_sum += sec
    sec_ls.append(sec)#10**6倍の状態です

middle = sec_sum /2

sum_dist = 0
for i in range(N):
    if middle > sec_ls[i]:
        sum_dist += AB_ls[i][0]
        middle -= sec_ls[i]
    else:
        sum_dist += AB_ls[i][1] * (middle/10**6)
        break

print(sum_dist)
