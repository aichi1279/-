
n,m = map(int,input().split())

conditions = []
for i in range(m):
    a,b = map(int,input().split())
    conditions.append((a,b))


k = int(input())
people = []
for i in range(k):
    c,d = map(int, input().split())
    people.append((c,d))

cnt = [0] *110
ans = 0

for bit in range(1 << k):
    for i in range(k):
        cnt[people[i][(bit >> i) % 2]] += 1

    tmp = 0
    for (a,b) in conditions:
        if cnt[a] > 0 and cnt[b] > 0:
            tmp += 1
    ans = max(ans ,tmp)

    for i in range(k):
        cnt[people[i][(bit >> i) % 2]] -= 1

print(ans)
