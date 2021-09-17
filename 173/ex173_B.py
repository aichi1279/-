import sys

s=[]
for line in sys.stdin:
    s.append(line)
    if len(s)==1:
        n = int(s[0])
    n-=1
    if n<0:
        break

s.pop(0)

hash={}
for key in s:
    if  key in hash:
        hash[key]+=1
    else:
        hash[key]=1

list=["AC\n", "TLE\n", "WA\n","RE\n"]

for key in hash.keys():
    count=0
    for one in list:
        if key == one:
            print(one[:-1]+" × "+str(hash[key]))
            list.pop(count)
        count+=1


for rest in list:
    print(rest[:-1]+" × "+str(0))
