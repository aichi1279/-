
n = int(input())
A = list(map(int, input().split()))

front = []
last = []
for i in range(1,len(A)):
    front.append(A[:i])
    last.append(A[i:len(A)])

ans = 2**30
for i in range(len(front)):
    or_one = 0
    or_two = 0
    ls = front[i]
    ls2 = last[i]
    for i in range(len(ls)):
        or_one = or_one | ls[i]
    for j in range(len(ls2)):
        or_two = or_two | ls2[j]

    if ans > or_one^or_two:
        ans = or_one^or_two



print(ans)
