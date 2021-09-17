n, k = map(int,input().split())

N_field = []
for _ in range(n):
    tmp = [int(key) for key in input().split()]
    N_field.append(tmp)

C_list = []
for X in range(n-k+1):#X1
    for Y in range(n-k+1):#Y1
        tmp = []
        for x in range(k):#x
            res_x = X+x
            for y in range(k):
                res_y = Y+y
                tmp.append((res_x,res_y))
        C_list.append(tmp)


median = ((k**2)//2) + 1
ans = 10**10
for ex in C_list:
    tmp = []
    for key in ex:
        tmp.append(N_field[key[0]][key[1]])
    tmp.sort(reverse=True)
    res = tmp[median-1]
    #print(res)
    if ans > res:
        ans = res
print(ans)
