n = int(input())

def solve(n):
    bottom,top = 0,10**10

    while top-bottom > 1:
        mid = (bottom + top)//2
        sum = mid*(mid+1) //2

        if sum >= n:
            top = mid
        else:
            bottom = mid

    return top


print(solve(n))
