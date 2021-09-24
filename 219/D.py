N = int(input())
X,Y = map(int,input().split())

N_ex = []
for i in range(N):
    A,B = map(int,input().split())
    N_ex.append((A,B))

A_cnt = 0
B_cnt = 0
cnt = 0
while X > A_cnt or Y > B_cnt:
    cnt += 1
    for key in N_ex:
        if (key[0]+A_cnt) >= X and (key[1]+B_cnt) >= Y:
            A_cnt += key[0]
            B_cnt += key[1]
            print(cnt)
            exit()

    if X-A_cnt > Y-B_cnt:
        N_ex.sort(key=lambda x:x[0],reverse=True)
    else:
        N_ex.sort(key=lambda x:x[1],reverse=True)

    if len(N_ex) >= 2:
        if N_ex[0][0]+N_ex[0][1] > N_ex[1][0]+N_ex[1][1]:
            A_cnt += N_ex[0][0]
            B_cnt += N_ex[0][1]
            N_ex.pop(0)
        else:
            A_cnt += N_ex[1][0]
            B_cnt += N_ex[1][1]
            N_ex.pop(1)
    elif len(N_ex) == 1:
        A_cnt += N_ex[0][0]
        B_cnt += N_ex[0][1]
        N_ex.pop(0)

    if len(N_ex) == 0:
        print(-1)
        exit()
