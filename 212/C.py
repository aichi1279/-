


def bs_find_closest(data, target):
    if len(data) == 0:
        return None
    if len(data) == 1:
        return data[0]
    min_diff = float('inf')
    min_diff_right = float('inf')
    min_diff_left = float('inf')

    imin = 0
    imax = len(data) - 1
    closest_num = None
    while imin <= imax:
        imid = imin + (imax - imin) // 2
        #　中心の左右の値と目標との差を計算する。
        if imid + 1 < len(data):
            min_diff_right = abs(data[imid+1] - target)
        if imid > 0:
            min_diff_left = abs(data[imid-1] - target)

        # 最初の差と最も最小に近い値を更新する。
        if min_diff_left < min_diff:
            min_diff = min_diff_left
            closest_num = data[imid-1]
        if min_diff_right < min_diff:
            min_diff = min_diff_right
            closest_num = data[imid+1]
        # 2分探索する。
        if data[imid] < target:
            imin = imid + 1
        elif data[imid] > target:
            imax = imid -1
        else:
            return data[imid]
    return closest_num


def main():
    N,M = map(int,input().split())
    A_list = list(map(int,input().split()))
    B_list = list(map(int,input().split()))

    A_list.sort()
    B_list.sort()

    ans = 10**10
    for i in range(len(A_list)):
        target = bs_find_closest(B_list, A_list[i])
        ans = min(ans, abs(A_list[i]-target) )

    print(ans)





if __name__ == '__main__':
    main()
