import copy
import itertools
n, k = map(int, input().split())

T = []
for i in range(n):
    tmp = list(map(int, input().split()))
    T.append(tmp)

perm = [str(i) for i in range(n)]

p = itertools.permutations(perm, n)

path=[]
for v in p:
    if v[0][0]=='0':
        path.append(v)

count=0
score_list=[]
for v in path:
    #print(v)
    score = 0
    for i in range(1,n):
        start = int(v[i-1])
        end=int(v[i])
        score += T[end][start]
        if i == n-1:
            score += T[0][end]
    score_list.append(score)
    if score == k:
        count+=1

#print(score_list)
print(count)
