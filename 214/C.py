N = int(input())
S = [int(key) for key in input().split()]
T = [int(key) for key in input().split()]

pair = []
for i in range(N):
    pair.append((S[i],T[i]))
    #print((S[i],T[i]))

mini_T = min(T)
eye = T.index(mini_T)
before = mini_T + S[eye]
ans = [0] * N
ans[eye] = mini_T
for i in range(eye+1,eye+N):
    i = i % N
    if pair[i][1] < before:
        ans[i] = pair[i][1]
        before = pair[i][1]+pair[i][0]
    else:
        ans[i] = before
        before += pair[i][0]

for i in range(N):
    print(ans[i])
