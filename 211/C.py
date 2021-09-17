s = input()
N = len(s)+1
T = "chokudai"

dp = [[1]]*N
for _ in range(1,9):
    dp[0].append(0)

for i in range(1,N):
    for j in range(1,9):
        if s[i-1]==T[j-1]:
            dp[i][j] = dp[i-1][j]+dp[i-1][j-1]
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N-1][8])
