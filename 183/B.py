x1, y1,x2, y2  = map(int, input().split())

if y1==y2:
    print( (x1+x2)/2 )
    exit()
else:
    y2 = y2 * -1
    a = (y2-y1) / (x2-x1)
    b = y1 - (a *x1)
    x = (0-b) / a
    print("{:.10f}".format(x))
    exit()
