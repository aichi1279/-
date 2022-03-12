import cython
N, X = map(int,input().split())
S = input()

#↓ 以下のUコマンドがくる直前のコマンドを削除することために
#  スタックを利用する！ Uの直前を無条件に消せば良い点に注意されたい
stk = []
for i in range(N):
    if S[i] == 'U' and len(stk) != 0 and (stk[-1]=='L' or stk[-1]=='R'):
        stk.pop()
    else:
        stk.append(S[i])
#---------------------------------------------------#

for c in stk:
    if c == 'U':
        X = X >> 1
    elif c == 'L':
        X = X << 1
    else: #'R'の指令の時
        X = (X << 1) + 1

print(X)
