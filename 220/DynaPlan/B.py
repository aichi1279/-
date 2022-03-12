"""
https://qiita.com/drken/items/dc53c683d6de8aeacf5a#3-a-%E5%95%8F%E9%A1%8C%E3%81%8B%E3%82%89-e-%E5%95%8F%E9%A1%8C%E3%81%BE%E3%81%A7
"""
N, K = map(int, input().split())
h = [int(key) for key in input().split()]

INF = 10**20
dp = [INF for _ in range(N*2)]
dp[0] = 0

for i in range(1,N):
    for j in range(K):
        if i-(j+1) < 0:
            break
        dp[i] = min(dp[i], dp[i-(j+1)]+ abs(h[i]-h[i-(j+1)]))

print(dp[N-1])
