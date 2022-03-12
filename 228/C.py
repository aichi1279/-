N, K = map(int,input().split())
P_table = [[int(key) for key in input().split()] for _ in range(N)]

sum_score = []
for i in range(N):
    sum_score.append((sum(P_table[i]),i))

sorted_score = sorted(sum_score)
K_rank = []
for i in range(K):
    K_rank.append(sorted_score[N-i-1][0])

mini_K = min(K_rank)
#print(sorted_score)
#print(K_rank)

for i in range(N):
    if mini_K <= (sum_score[i][0]+300):
        print("Yes")
    else:
        print("No")
