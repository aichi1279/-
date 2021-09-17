s = list(input())

kouho = []
cond = []
for i in range(10):
    if s[i]=="o" or s[i]=="?":
        kouho.append(str(i))
    if s[i]=="o":
        cond.append(str(i))


if len(cond)>4:
    print(0)
    exit()

res = set()
for key1 in kouho:
    for key2 in kouho:
        for key3 in kouho:
            for key4 in kouho:
                res.add(key1+key2+key3+key4)
cnt = 0
for key in res:
    d_cnt = 0
    for i in cond:
        if str(i) in key:
            d_cnt += 1
    if d_cnt == len(cond):
        cnt += 1
print(cnt)
