"""
https://qiita.com/drken/items/dc53c683d6de8aeacf5a#3-a-%E5%95%8F%E9%A1%8C%E3%81%8B%E3%82%89-e-%E5%95%8F%E9%A1%8C%E3%81%BE%E3%81%A7
"""
N = int(input())
h = [int(key) for key in input().split()]

INF = 10**20
dp = [INF for _ in range(N)]
dp[0] = 0

for i in range(1,N):
    #i-1から遷移した場合
    dp[i] = min(dp[i], dp[i-1]+ abs(h[i]-h[i-1]) )
    if i > 1:
        dp[i] = min(dp[i], dp[i-2] + abs(h[i]-h[i-2]) )

print(dp[N-1])
