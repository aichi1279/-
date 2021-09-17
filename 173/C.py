
h,w,k = map(int, input().split())

mat = []
for i in range(h):
    mat.append(list(input()))

ans =0

for s in range(2**h):
    b_h = '{:06b}'.format(s) #sを2進数に直す。:bが2進数への変換、06が6桁で0埋めすることを表す。
    for t in range(2**w):
        b_w = '{:06b}'.format(t)
        black = 0 #黒の数を数える
        for i in range(h):
            for j in range(w):
                if mat[i][j]=='#' and b_h[-(i+1)] == '0' and b_w[-(j+1)]=='0':
                    # 該当のマスが黒かつ、赤く塗られていない（2進数で0）場合
                    black += 1
        if black==k:
            ans +=1
print(ans)
