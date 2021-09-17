import sys
sys.setrecursionlimit(10**9)

n = int(input())

G = [[] for _ in range(n)] #グラフの描画法、しっかり覚えよう
for _ in range(n-1):
    a,b = map(int,input().split())
    a-=1
    b-=1
    G[a].append(b)
    G[b].append(a)
for key in G:
    key.sort()

ans = []
visited = {0}
def dfs(root):
    ans.append(root+1)
    for child in G[root]:
        if child not in visited:
            visited.add(child)
            dfs(child)
            ans.append(root+1)

dfs(0)
print(" ".join(map(str,ans)))
