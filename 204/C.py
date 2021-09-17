import sys
sys.setrecursionlimit(10000)
#再帰回数の上限を設定できる(10000)


n,m = map(int,input().split())
G = [[] for i in range(n)]#テーブル配列の定義方法
#G[i]は都市iから道路で直接繋がっている都市リスト

for i in range(m):
    a,b = map(int,input().split())
    G[a-1].append(b-1)


#dfs
def dfs(v):
    if temp[v]: return #同じ頂点を2度以上調べないためのreturn
    temp[v]=True
    for vv in G[v]: dfs(vv)


ans = 0
#都市iからスタートする場合
for i in range(n):
    temp = [False]*n

    # temp[j]は都市jに到達可能かどうかを表す。
    dfs(i)

    ans += sum(temp)

print(ans)
