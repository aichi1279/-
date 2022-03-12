# Correct!!
"""
問題文↓
https://atcoder.jp/contests/abc234/tasks/abc234_d

解説では、heapq(ヒープキュー)を利用していた。
heapqとは、ヒープのデータ構造をもったリストのことである。
別名：優先度付きキューとも呼ばれる。

ヒープ（英: heap）とは、
「子要素は親要素より常に大きいか等しい（または常に小さいか等しい）」という制約を持つ木構造の事。
単に「ヒープ」という場合、二分木を使った二分ヒープを指すことが多いため、そちらを参照すること。
"""

import heapq #優先度付きキュー(優先度付きリスト)のライブラリ
N ,K = map(int,input().split())
P_i = [int(key) for key in input().split()]

que = P_i[:K]
print(min(que))
heapq.heapify(que) #デフォルトでは、小さい方が上に来るようになっている
for i in range(K, N):
    mini = heapq.heappop(que)
    into = max(P_i[i], mini)
    heapq.heappush(que, into)

    ans = heapq.heappop(que)
    print(ans)
    heapq.heappush(que, ans)
