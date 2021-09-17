H,W,N = map(int,input().split())
A, B = [], []
for _ in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)

Xdict = {key:i+1 for i,key in enumerate(sorted(list(set(A))))}
Ydict = {key:i+1 for i,key in enumerate(sorted(list(set(B))))}

for  i in range(N):
    print(Xdict[A[i]], Ydict[B[i]])
