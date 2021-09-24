X = input()
N = int(input())

import string
en_dict = {}
de_dict = {}
for i,key in enumerate(list(string.ascii_lowercase)):
    en_dict[X[i]] = key
    de_dict[key] = X[i]

#dict_list = sorted(dict.items(), key=lambda x:x[0])

ans = []
for i in range(N):
    s = input()
    cnv = ""
    for key in list(s):
        cnv += en_dict[key]
    ans.append(cnv)
ans.sort()

for key in ans:
    decnv = ""
    for cha in list(key):
        decnv += de_dict[cha]
    print(decnv)
