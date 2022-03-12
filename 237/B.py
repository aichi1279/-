H, W = map(int,input().split())
table = ""
A = []
for i in range(H):
    A.append([int(key) for key in input().split()])

B = [[0 for _ in range(H)] for _ in range(W)]
for i in range(H):
    for j in range(W):
        B[j][i] = A[i][j]

for key in B:
    [print(str(i)+" ", end="") for i in key]
    print()
