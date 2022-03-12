N,W = map(int,input().split())
V = 1010
INF = 10**20

weight = []
value = []
for _ in range(N):
    w,v = map(int,input().split())
    weight.append(w)
    value.append(v)

weight.append(0)
value.append(0)
"""
DPのキーは制約条件の軽い要素(value or weight)を選ぶことができる。特にナップザック問題で..
"""

dp = [[0 for _ in range(V+1)] for _ in range(N+2)] # Valueを格納
dp[0][0] = 0
for i in range(N+1):
    for sum_v in range(V):
        # i番目の品物を選べる場合
        if sum_v-value[i] >= 0:
            dp[i+1][sum_v] = max(dp[i+1][sum_v], dp[i][sum_v-value[i]]+ weight[i] )

        # i番目の品物を選ばない場合
        dp[i+1][sum_v] = max(dp[i+1][sum_v], dp[i][sum_v])

#最適値の出力
ans = 0
for sum_v in range(V):
    if dp[N][sum_v] <= W:
        ans = sum_v

for line in dp:
    print(max(dp[N]))
