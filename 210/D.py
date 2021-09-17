H,W,C = map(int,input().split())
A_list = []
for _ in range(H):
    inp = [int(key) for key in input().split()]
    A_list.append(inp)

#print(A_list)

kouho = []
for i in range(H):
    for j in range(W):
        kouho.append((i,j))

cost = 10**20
for key in kouho:
    i = key[0]
    j = key[1]
    for key2 in kouho:
        i_ = key2[0]
        j_ = key2[1]
        if key==key2:
            continue
        station = A_list[i][j] + A_list[i_][j_]
        line = (abs(i-i_)+abs(j-j_)) * C
        all = station + line
        if all < cost:
            cost = all
print(cost)
