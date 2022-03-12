N = int(input())
A = [int(key) for key in input().split()]
S_A = [0] + [360 - sum(A[:i])%360 for i in range(1,N+1)]

S_A.sort()
#print(S_A)

ans = 360 - (S_A[-1]- S_A[0])
for i in range(1, N+1):
    ans = max(ans, S_A[i]-S_A[i-1])

print(ans)
