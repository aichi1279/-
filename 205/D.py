n, q = map(int,input().split())
A_list = [int(key) for key in input().split()]
#A_list = [0] + A_list

print(A_list)

def bi_search(k, A_list):
    left = 0
    right = len(A_list)

    mid = (right+left)//2
    add = 0
    while left < right:
        print("left:right:mid = {}:{}:{}".format(left,right,mid))
        if k  <  A_list[mid]:
            right = mid - 1
        elif A_list[mid] < k:
            left = mid + 1
        else:
            add = mid
            break

        add = right
        mid = (right+left)//2

    return add



for _ in range(q):
    k = int(input())
    #---この処理を改良する必要あり---#
    """
    i, cnt, res = 0, 0 ,0
    while True:

        i += 1
        if i in A_list:
            cnt += 1

        if (i-cnt)==k:
            res = i
            break
    """
    #-------二分探索の試行--------#
    res = k + bi_search(k,A_list)

    print(res)
