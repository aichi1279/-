N, M = map(int, input().split())
B = [[int(key) for key in input().split()] for _ in range(N)]

ij_lis = []
bottom_i, bottom_j = 0, 0
for j in range(7):
    indic = B[0][0] - (j+1)
    if indic % 7 == 0:
        i = indic // 7
        bottom_i = i+1
        bottom_j = j+1

if bottom_i+N > (10**100)+1 or bottom_j+M > 8:
    print("No")
    exit()
elif bottom_i==0 or bottom_j==0:
    print("No")
    exit()

for i in range(bottom_i, bottom_i+N):
    for j in range(bottom_j, bottom_j+M):
        correct = (i-1)*7 +j
        if B[i-bottom_i][j-bottom_j]!=correct:
            print("No")
            exit()
print("Yes")
