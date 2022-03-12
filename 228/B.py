N, X = map(int,input().split())
A_list = [int(key) for key in input().split()]

searched = [0]*len(A_list)
lock_on = X
while searched[lock_on-1] == 0:
    searched[lock_on-1] = 1
    lock_on = A_list[lock_on-1]

print(sum(searched))
