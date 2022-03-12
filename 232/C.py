N, M = map(int,input().split())
####### 入力1 ########
auth_G = [[0]*N for _ in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    auth_G[A-1][B-1] = 1
    auth_G[B-1][A-1] = 1
#####################

####### 入力2 ########
check_G = [[0]*N for _ in range(N)]
for i in range(M):
    C, D = map(int, input().split())
    check_G[C-1][D-1] = 1
    check_G[D-1][C-1] = 1
#####################

if auth_G == check_G:
    print("Yes")
    exit()

for line_i in range(N):
    for line_j in range(N):
        if line_i == line_j:
            continue

        check = check_G.copy()
        tmp = check[line_i]
        check[line_i] = check[line_j]
        check[line_j] = tmp
        if auth_G == check:
            print("Yes")
            exit()
        """"
        for i in range(N):
            for j in range(N):
                if i==j:
                    continue
                tmp = check[i][j]
                check[i][j] = check[j][i]
                check[j][i] = tmp

        for row_i in range(N):
            for row_j in range(N):
                if row_i == row_j:
                    continue
                tmp = check[row_i]
                check[row_i] = check[row_j]
                check[row_j] = tmp
                if T_auth == check:
                    print("Yes")
                    exit()
        """

print("No")
