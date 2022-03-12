N, Q = map(int,input().split())
A_list = [int(key) for key in input().split()]
A_list.sort()
#print("-------------")

def bi_search(A_list, x):#二分探索木
    left = 0
    right = len(A_list)
    mid = (left+right)//2
    before = 0
    while mid != before:
        if A_list[mid]==x:
            return len(A_list)-mid
        elif A_list[mid]< x:
            left = mid
        else:
            right = mid
        before = mid
        mid = (left+right)//2

    if mid==len(A_list)-1 and A_list[mid]<x:
        return 0
    elif mid==0 and A_list[mid]>x:
        return len(A_list)
    else:
        return len(A_list)-(mid+1)


for i in range(Q):
    x = int(input())
    ans = bi_search(A_list,x)
    print(ans)
