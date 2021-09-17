n,m,t = map(int, input().split())

A = [0]
B = [0]
const_n = n

for i in range(m):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)

for i in range(1,len(A)):
    if n-(A[i]-B[i-1]) <= 0:
        print("No")
        exit()
    else:
        #print(str(A[i])+":"+str(B[i]))
        n -= A[i]-B[i-1]
        #print(n)
        n += B[i]-A[i]
        if n > const_n:
            n = const_n
        #print(n)


n -= t-B[len(B)-1]
if n >0:
    print("Yes")
else:
    print("No")
