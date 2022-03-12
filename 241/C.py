N = int(input())
S = []
for _ in range(N):
    s = input().replace('.','0')
    s = s.replace('#','1')
    S.append([int(key) for key in list(s)])

for i in range(N):
    for j in range(N):

        index = sum(S[i][j:min(j+6, N)])
        if index >= 4:
            print("Yes")
            exit()

        index = sum([S[k][j] for k in range(i, min(i+6,N))])
        if index >= 4:
            print("Yes")
            exit()

        if j+5 < N and  i+5 < N and sum([S[i+k][j+k] for k in range(6)]) >= 4:
            print("Yes")
            exit()
        if j+5 < N and  i+5 < N and sum([S[i+k][j+5-k] for k in range(6)])>= 4:
            print("Yes")
            exit()

print("No")
