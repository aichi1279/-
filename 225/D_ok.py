N,Q = map(int, input().split())
Querys = [[int(key) for key in input().split()] for _ in range(Q)]
# ↑ 入力層

import sys
sys.setrecursionlimit(10**9)
#どうもAtCoderの環境ではデフォルトでは再帰呼び出しの上限が
#1,000回のようで、それを超えて再帰呼び出しする場合はこの指定が必要です。

def To_front(aim, last_hash):
    if aim in last_hash:
        aim = To_front(last_hash[aim],last_hash)
    return aim

def To_last(first, front_hash, ans_ls):
    if first in front_hash:
        ans_ls.append(front_hash[first])
        To_last(front_hash[first], front_hash, ans_ls)

    return ans_ls
# ↑ 関数層

# ↓ 処理層
front_hash = {}
last_hash = {}
for q in Querys:
    num = int(q[0])

    if num==1:
        pre = q[1]
        next = q[2]
        front_hash[pre] = next
        last_hash[next] = pre
    elif num==2:
        pre = q[1]
        next = q[2]
        front_hash.pop(pre)
        last_hash.pop(next)
    else:
        aim = q[1]
        first = To_front(aim,last_hash)
        #print(first)
        ans_ls = [first]
        ans_ls = To_last(first, front_hash, ans_ls)
        if len(ans_ls)<=1:
            print("1 "+str(first))
            continue
        else:
            nber = str(len(ans_ls))
            line = str(ans_ls).replace("[","")
            line = line.replace(",","")
            line = line.replace("]","")
            print(nber+" "+line)
