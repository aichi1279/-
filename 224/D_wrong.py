M = int(input())
M_list = [[int(key)-1 for key in input().split()] for _ in range(M)]
P = [int(key) for key in input().split()]

G = [[0 for _ in range(9)] for _ in range(9)]
for i_j in M_list:
    G[i_j[0]][i_j[1]] = 1
    G[i_j[1]][i_j[0]] = 1

S = [key for key in range(1,9)]

for line in G:
    print(line)

def DFS(G,S,P):
