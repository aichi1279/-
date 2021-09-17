N,M = map(int,input().split())
A = [int(key) for key in input().split()]

import math
for i in range(1,M+1):
    for j in range(N):
        if math.gcd(A[j],i)!= 1:
            break
        elif j == N-1 and  math.gcd(A[j],i)== 1:
            print(i)
