X = input()

if X[0]=='-':
    if X[-1]=='0':
        print(X[:-1])
    else:
        if len(X) == 2:
            print(-1)
        else:
            X = int(X[:-1])-1
            print(X)
else:
    if len(X) == 1:
        print(0)
    else:
        print(X[:-1])
