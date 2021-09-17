n, x = map(int, input().split())

V_P_list = []
for i in range(n):
    v, p = map(int, input().split())
    V_P_list.append((v,p))

count = 0
sum = 0
for key in V_P_list:
    count += 1
    sum += (key[0]*key[1])
    if sum > x*100:
        print(count)
        exit()

print(-1)
