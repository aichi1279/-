mod = 998244353
N = int(input())
As = [int(key) for key in input().split()]
Bs = [int(key) for key in input().split()]

M = 3000
dp = [1 for _ in range(M+1)]

for i in range(N):
    nx = [0] *(M+1)
    # 初期化
    for j in range(As[i], Bs[i]+1):
        nx[j] = dp[j]
    dp = nx

    for i in range(M):
        dp[i+1] += dp[i]
        dp[i+1] %= mod

print(dp[M])
