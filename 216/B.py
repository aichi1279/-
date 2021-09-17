N = int(input())

memo = set()
judge = False
for i in range(N):
    first, last = input().split()
    merge = first+" "+last
    if merge in memo:
        judge = True
    else:
        memo.add(merge)

if judge:
    print("Yes")
else:
    print("No")
