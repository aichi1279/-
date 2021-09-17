def g1(num):#大きい順
    ls = list(str(num))
    ls = sorted(ls,reverse=True)
    s = ""
    for key in ls:
        s += key
    return s



def g2(num):#小さい順
    ls = list(str(num).replace('0',''))
    ls.sort()
    s = ""
    for key in ls:
        s += key

    return s



def main():
    num ,k = map(int, input().split())

    for i in range(k):
        if g1(num)!='' and g2(num)!='':
            num = int(g1(num)) - int(g2(num))

        elif g1(num)=='' and g2(num)!='':
            num = - int(g2(num))

        elif g1(num)!='' and g2(num)=='':
            num = int(g1(num))

        else:
            num = 0

    print(num)


if __name__ == "__main__":
    main()
