mod = 998244353
N = int(input())
As = [int(key) for key in input().split()]
Bs = [int(key) for key in input().split()]
M = 3000

dp = [1]*(M+1)
for i in range(N):
    index = [0]*(M+1)
    for j in range(As[i], Bs[i]+1):
        index[j] = dp[j]

    dp = index

    for j in range(M):
        dp[j+1] += dp[j]
        dp[j+1] %= mod

print(dp[M])
