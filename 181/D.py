s = str(input())

if int(s)%8==0:
    print("Yes")
    exit()

crite = list(range(1,10))
hash={}
sp = s.split()

for i in sp:
    if i in hash:
        hash[i] += 1
    else:
        hash[i] = 0
