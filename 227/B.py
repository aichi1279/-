N = int(input())
S = [int(key) for key in input().split()]

ans_list = []
for a in range(1,201):
    for b in range(1,201):
        ans_list.append(4*a*b+3*a+3*b)

cnt = 0
for kouho in S:
    if kouho not in ans_list:
        cnt += 1
print(cnt)
