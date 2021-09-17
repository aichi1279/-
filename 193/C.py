#https://qiita.com/bee2/items/4ab87d05cc03d53e19f9
#「pythonの高速化のために、用途別にcollection型(list/tuple/dictionary/set)の計算量をまとめる」

#pythonの高速化処理において、「listの処理速度は遅い！」
#スケールが大きくなるにつれ、線形的に処理速度が落ちる。

#-> よって できる限り　「set」　を使用すると良い。
# しかし、複数のデータを取り扱う場合は、listの方が管理しやすいため、listに統一した方が良いだろう。

#最悪なのは、list型をset型に変換して使用すること。　スケールアップした際に一番遅くなる要因。

n = int(input())
upper = int(n**0.5)+1

st = set()
sub_set = set()

for a in range(2,upper):
    if a in sub_set:
        continue

    b = 2
    while n >= a**b:
        if n >= a**b and a**b not in st:
            st.add(a**b)
        if a**b==b**a and b>a:
            sub_set.add(b)
        b += 1

print(n-len(st))
