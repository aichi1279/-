N, K = map(int,input().split())
c_list = [key for key in input().split()]
#print(c_list)

ans = 0
hash = {} #種類別頻度管理
now = 0
for i in range(N):
    # 追加処理
    if c_list[i] not in hash or hash[c_list[i]] == 0:
        now += 1
        hash[c_list[i]] = 1
    else:
        hash[c_list[i]] += 1

    # 削除処理
    if i+1 > K:
        #print(c_list[i-K])
        hash[c_list[i-K]] -= 1
        if hash[c_list[i-K]] == 0:
            now -= 1

    ans = max(ans,now)


print(ans)



""" #アルゴリズムの要件を満たせない.本当はhashによる種類別頻度管理

from collections import deque
tmp = deque()
for i in range(K-1):
    tmp.append(c_list[i])

ans = 0
for i in range(K-1,N):
    tmp.append(c_list[i])
    kind_num = len(set(tmp))

    if ans  < kind_num:
        ans = kind_num
    elif ans == K:
        break
    tmp.popleft()

print(ans)
"""
