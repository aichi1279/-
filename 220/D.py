from collections import deque
import copy
"""
動的計画法的な解き方でなかった。
例えば、動的計画法の考え方だと、
「FG..」と「GF..」の処理が行われた場合、同じになるはずだ。
table[1][1]には、table[0][1]とtable[1][0]から行くことができるが、
でそれぞれの処理結果が異なってしまう。

# table[0][0] = [2,7,6] の場合を考える！
・table[0][1]→table[1][1] ex) [9,6] -> [4]
・table[1][0]→table[1][1] ex) [4,6] -> [0]

よって、動的計画法での解答は通用しない。
"""

N = int(input())
A_list = [int(key) for key in input().split()]

table = {}
table[(0,0)] = A_list
tmp = deque(A_list)

for j in range(1,N+1):
    x = tmp.popleft()
    y = tmp.popleft()
    tmp.appendleft((x+y)%10)
    table[(0,j)] = list(tmp)
    if len(tmp) == 1:
        break

tmp = deque(A_list)
for i in range(1,N+1):
    x = tmp.popleft()
    y = tmp.popleft()
    tmp.appendleft((x*y)%10)
    table[(i,0)] = list(tmp)
    if len(tmp) == 1:
        break

#for key in table.keys():
#    print(str(key)+" "+str(table[key]))

for i in range(1,N+1):
    for j in range(1,N+1):
        table[(i,j)] =
