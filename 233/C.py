N,X = map(int,input().split())

bags = []
lprod = 1
for _ in range(N):
    tmp = [int(key)for key in input().split()]
    l, a = tmp[0], tmp[1:]
    bags.append(a)
    lprod *= l

ans = 0
for i in range(lprod):
    ind = i
    prod = 1
    for bag in bags:
        prod *= bag[ind % len(bag)]
        ind //= len(bag)
        if prod > X:
            break
    if prod == X:
        ans += 1
print(ans)

"""
2bit変化を利用した２値全探索を思い出してほしい。
全探索にはよく利用されるが、このやり方で、複雑なパターンの全探索が
可能になるため、よく理解しておくこと。
"""
