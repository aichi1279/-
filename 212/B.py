n = input()

mem = -1
same = 1
cnt = 1

for key in list(n):
    if mem==-1:
        mem=int(key)
        continue

    if (mem+1)%10 == int(key):
        same += 1
    if mem == int(key):
        cnt += 1

    mem = int(key)

if cnt == 4 or same == 4:
    print("Weak")
else:
    print("Strong")
