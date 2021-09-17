a ,b = input().split()
b = bin(int(b))[2:]
a = bin(int(a))[2:]

if len(a) > len(b):
    for _ in range(len(a)-len(b)):
        b = "0"+b
else:
    for _ in range(len(b)-len(a)):
        a = "0"+a

#print(str(a)+":"+str(b))
b = list(b)
a = list(a)

c = ''
for i in range(len(b)):
    if b[i]==a[i]:
        c += '0'
    else:
        c += '1'

print(int(c,2))
