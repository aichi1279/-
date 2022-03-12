N,W = map(int,input().split())
weight = []
value = []
for _ in range(N):
    w,v = map(int,input().split())
    weight.append(w)
    value.append(v)

weight.append(0)
value.append(0)
dp = [[0 for _ in range(W+1)] for _ in range(N+2)] # Valueを格納
# i番目以下の品物で重さW以下で価値を最大化するDP
for i in range(N+1):
    for sum_w in range(W+1):
        #品物iを選べる場合
        if sum_w - weight[i] >= 0:
            dp[i+1][sum_w] = max(dp[i+1][sum_w],dp[i][sum_w-weight[i]]+ value[i])

        # 品物iを選ばない場合
        dp[i+1][sum_w] = max(dp[i+1][sum_w], dp[i][sum_w])

print(dp[-1][-1])
