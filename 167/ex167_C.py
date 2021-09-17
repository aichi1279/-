import numpy as np

def func(ans, b_list, a_list, c_list, k, x):
    if k == 0:
        b_list = np.asarray(b_list)
        x_list = np.dot(b_list, a_list)
        if np.all(x_list >=x):
            return np.inner(c_list, b_list)
        else:
            return ans

    ans = min(ans , func(ans , b_list + [1], a_list, c_list, k-1, x))
    ans = min(ans, func(ans, b_list + [0], a_list, c_list, k-1, x))
    return ans

def main():
    n, m, x = map(int, input().split())
    c_list = []
    a_list = []
    for i in range(0,n):
        c, *a = map(int, input().split())
        c_list.append(c)
        a_list.append(a)

    ans = float("inf")
    c_list = np.asarray(c_list)
    a_list = np.asarray(a_list)
    ans = min(ans, func(ans, [1], a_list, c_list, n - 1, x))
    ans = min(ans, func(ans, [0], a_list, c_list, n - 1, x))
    if ans ==float("inf"):
        print(-1)
    else:
        print(ans)

if __name__ == "__main__":
    main()
