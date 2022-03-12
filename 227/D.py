N, K = map(int,input().split())
A = [int(key)for key in input().split()]

ok, ng = 0, 10**15//K
while ng-ok > 1:
    mid = (ok+ng) // 2
    sum = 0
    for i in range(len(A)):
        sum += min(A[i], mid)
    if sum >= K*mid:
        ok = mid
    else:
        ng = mid


print(ok)
