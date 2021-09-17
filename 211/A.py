a,b = map(int,input().split())

c = (a-b)*10**5 / (3*10**5)
c += b
if ".0" in str(c):
    print(int(c))
else:
    print(c)
