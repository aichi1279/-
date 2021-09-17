x, y = map(int, input().split())

if x > y and y+3>x:
    print("Yes")
elif y > x and x+3>y:
    print("Yes")
else:
    print("No")
