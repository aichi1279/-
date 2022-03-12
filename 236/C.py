N, M = map(int,input().split())
S_ls = [key for key in input().split()]
T_ls = [key for key in input().split()]

cnt = 0
i = 0
cnt_mem = []
for s in S_ls:
    if s == T_ls[i]:
        cnt_mem.append(cnt)
        i += 1
        cnt = 0

    else:
        cnt += 1

i = 1
for k,key in enumerate(T_ls):
    print("Yes")
    if k != len(T_ls)-1:
        No = "No\n"*cnt_mem[i]
        print(No,end='')
    i += 1
