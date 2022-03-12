# InCorrect !!
N ,K = map(int,input().split())
P_i = [int(key) for key in input().split()]


def bin_search(lis, this_):
    left = 0
    right = len(lis)
    mid = (left+right)//2
    before = 0

    while mid!=before:
        if lis[mid] == this_:
            break
        elif lis[mid] > this_:
            left = mid
        else:
            right = mid

        before = mid
        mid = (left+right)//2

    #埋め込み位置の左右の特定を忘れるな！！
    if lis[mid] > this_:
        return mid+1
    else:
        return mid




K_ascend = sorted(P_i[:K],reverse=True)

print(K_ascend[-1])
for i in range(K, len(P_i)):
    kouho = P_i[i]
    if K_ascend[-1] > kouho:
        print(K_ascend[-1])
        continue

    k = bin_search(K_ascend, kouho)
    ###
    tmp = K_ascend[:k]
    tmp.append(kouho)
    tmp.extend(K_ascend[k:])
    K_ascend = tmp.copy()
    K_ascend.pop()
    ####

    print(K_ascend[-1])
