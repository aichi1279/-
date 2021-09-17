S, T = map(int,input().split())

list = []
for a in range(101):
    for b in range(101):
        if a+b > S:
            break
        for c in range(101-a-b):
            if a+b+c <= S:
                list.append((a,b,c))

cnt = 0
for key in list:
    tmp = key[0]*key[1]*key[2]
    if tmp <= T:
        cnt += 1

print(cnt)
