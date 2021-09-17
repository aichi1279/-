a, b = map(int,input().split())


s = ""
if a>b:
    for i in range(a):
        s += str(b)
    print(s)
else:
    for i in range(b):
        s += str(a)
    print(s)
