n = int(input())
A = list( map(int, input().split()) )+[0]

cand = [-1]
ans = 0

for i in range(len(A)):
    while A[cand[-1]] > A[i]:
        #print(i, cand[-1],A[cand[-1]])
        ans = max(ans,  (i-cand[-2]-1) * A[cand[-1]]   )
        cand.pop()
    cand.append(i)

print(ans)














#---------------------------------------------------#
"""# N^2の手法
maxi_eat = 0
sat_l = 0
sat_r = 0
for l in range(n):
    for r in range(l,n):
        if l == r:
            eat = A_list[l]
        else:
            mini = min(A_list[l:r+1])
            eat = mini*(r-l+1)

        maxi_eat = max(maxi_eat, eat)

#print((sat_l,sat_r,maxi_eat))
print(maxi_eat)
"""
