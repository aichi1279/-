N,K = map(int,input().split())
A = [int(key) for key in input().split()]

##手法１　計算量 O(n^2) 計算量的に通らない
"""
S = [0] + A.copy()
for i in range(1, len(S)):
    S[i] += S[i-1]

ans = 0
judge = True
for r in range(1, N+1):
    for l in range(1, r+1):
        judge = judge & (l<=r)
        if K == S[r] - S[l-1]:  # a_n = (S_n) - (S_n-1) の応用
            ans += 1            # K = (S_n) - (S_n-1..)をcheck

#print(judge)
"""

## 解答　計算量 O(n*log(n))で通る
"""
ans = 0
hash = {}
for r in range(1, N+1):
    if S[r-1] not in hash:
        hash[S[r-1]] = 1
    else:
        hash[S[r-1]] += 1

    if (S[r]-K) in hash:
        ans += hash[S[r]-K]
"""

## 別解答　計算量 O(n*log(n))で通る
ans = 0
mk_S = 0
sum_cnt = {0:1}
for a in A:
    mk_S += a
    l = mk_S - K
    if l in sum_cnt:
        ans += sum_cnt[l]
    if mk_S not in sum_cnt:
        sum_cnt[mk_S] = 0
    sum_cnt[mk_S] += 1

print(ans)
