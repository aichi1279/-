"""
問題文↓
https://atcoder.jp/contests/abc235/tasks/abc235_d
"""

from collections import deque
#↑ 幅優先探索には、FIFOのリストが必要なため、popleftを利用できるdequeが必須

a, N = map(int,input().split())
#黒板には最初　1が記載されている

M = 1
while M <= N:
    M *= 10

d = [-1]* M
Q = deque()
d[1] = 0
Q.append(1)

while len(Q):       # 幅優先探索 FIFOのリストを用意し、そのリストがなくなったら終了
    c = Q.popleft() # 探索候補の取り出し
    dc = d[c]

    op1 = a *c
    if op1 < M and d[op1] == -1: # 定義域のM以下で、未到達の場合にのみ結果を保存
        d[op1] = dc + 1
        Q.append(op1) # 次の探索候補1を格納

    if c >= 10 and c % 10 != 0:# 問題文の条件を満たしたら
        s = str(c)
        op2 = int(s[-1] + s[:-1])
        if op2 < M and d[op2] == -1:# 定義域のM以下で、未到達の場合に限り結果を保存
            d[op2] = dc + 1
            Q.append(op2)# 次の探索候補2を格納

print(d[N])
