n,m = map(int,input().split())

A_list = list(map(int,input().split()))
B_list = list(map(int,input().split()))

mem = set()
for key in A_list:
    if key not in B_list and key not in mem:
        mem.add(key)

for key in B_list:
    if key not in A_list and key not in mem:
        mem.add(key)

res = str(sorted(mem))
res = res.replace('[','')
res = res.replace(']','')
res = res.replace(',','')
print(res)
