A = [int(key) for key in input().split()]

ans = 0
for i in range(3):
    ans = A[ans]
print(ans)
