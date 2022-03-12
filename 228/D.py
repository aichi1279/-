N = 2**20
Q = int(input())
A = [-1]*N

h_manage = [0]*N
for _ in range(Q):#2* 10**5
    t, x = map(int,input().split())
    if t == 1:
        h = x%N
        h_manage[h] += 1
        if h_manage[h] == 1:
            A[h] = x
            continue

        while A[h]!= -1:
            if h_manage[h] <= 1:
                A[h+h_manage[h]] = x
                h_manage[h] += 1
                break
            h += h_manage[h]-1
            h %= N

    else:
        print(A[x%N])
