x1,y1, x2,y2 = map(int,input().split())
x2 = x2-x1
y2 = y2-y1
x1, y1 = 0, 0 #解は0,1,2に限定される
mid = (x2/2, y2/2)
x_ls = [-2,-1,0,1,2]

if x2!=0 and y2!= 0:
    a = -1 / (y2/ x2)# x2が0の場合に対応できない
    b = mid[1] - (a*mid[0])
    for x in x_ls:
        y = a*x +b
        if x**2 + y**2==5 and (y*10)%10==0:
            print("Yes")
            exit()
elif x2==0:
    y = y2/2
    for x in x_ls:
        if x**2 + y**2==5 and (y*10)%10==0:
            print("Yes")
            exit()
elif y2==0:
    x = x2/2
    for y in x_ls:
        if x**2 + y**2==5 and (x*10)%10==0:
            print("Yes")
            exit()

print("No")
