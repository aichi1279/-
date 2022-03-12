"""
https://qiita.com/drken/items/dc53c683d6de8aeacf5a#3-a-%E5%95%8F%E9%A1%8C%E3%81%8B%E3%82%89-e-%E5%95%8F%E9%A1%8C%E3%81%BE%E3%81%A7
"""
N = int(input())

keys = []
for _ in range(N):
    a,b,c = map(int, input().split())
    keys.append((a,b,c))
keys.append((0,0,0))

MINUS = -100
dp = [[MINUS for _ in range(3)] for _ in range(N+1)]
dp[0][0],dp[0][1],dp[0][2] = 0,0,0

for i in range(1,N+1):
    for j in range(3):
        for k in range(3):
            if j==k: continue
            dp[i][j] = max(dp[i][j], dp[i-1][k]+keys[i-1][k])

print(max(dp[N]))

#for line in dp:
#    print(line)
