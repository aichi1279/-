N = int(input())
#PyPyでないと処理速度的に厳しい！！！

a = 1
b = 1
c = N
ans = 0
while a <= b and a <=c :
    while b <= c:
        ans += (c-b)+1
        #print((a,b,c))
        b += 1
        c = N //(b*a)

    a += 1
    b = a
    c = N //(a*b)

print(ans)
