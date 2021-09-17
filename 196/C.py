n = input()

if len(n)%2 == 0:
    m = len(n)//2
    front = n[:m]
    last = n[m:]
elif len(n)==1:
    print(0)
    exit()
else:
    m = (len(n)-1)//2
    front = ""
    last = ""
    for i in range(m):
        front += "9"
        last += "9"

count =0
for i in range(1,int(front)+1):
    tmp = str(i) + str(i)
    #print(tmp)
    if int(tmp) <= int(n):
        count += 1


print(count)
