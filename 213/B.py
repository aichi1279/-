n = int(input())
A = [int(key) for key in input().split()]

maxi = (-1, 0)
ans = (0, 0)
for i in range(len(A)):
    if A[i] > maxi[1]:
        ans = maxi
        maxi = (i+1, A[i])
    elif A[i] > ans[1]:
        ans = (i+1,A[i])

print(ans[0])
