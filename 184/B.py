n,x = map(int,input().split())
s = input()

list = list(s)

for one in list:
    if one=='x' and x > 0:
        x -= 1
    elif one=='o':
        x += 1


print(max(x,0))
