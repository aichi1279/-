n = int(input())

list = []
hash = {}
for _ in range(n):
    st = input().split()
    s,t = st[0], int(st[1])

    if len(list)<=1:
        list.append(t)
    elif min(list)< t:
        list.remove(min(list))
        list.append(t)

    hash[s] = t

for key in hash.keys():
    if hash[key]== min(list):
        print(key)
        break
