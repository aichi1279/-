import math
N = int(input())
bags = []
for _ in range(2*N-1):
    bag = [int(key) for key in input().split()]
    bags.append(bag)


total_perm = math.prod([key for key in range(1, 2*N, 2)])

members = sorted([int(key) for key in range(2*N)],reverse=True)
#各ペアの片方を残った番号最小値のメンバーに固定

max_ans = 0
for perm in range(total_perm):
    tmp = set(members.copy())
    i = 0
    ans = 0
    while len(tmp):
        pair_1 = tmp.pop()
        pair_2 = list(tmp)[ perm%(len(tmp)) ]
        ans = int( bin( bags[pair_1][ pair_2-pair_1-1 ] ^ ans ) , 2)

        tmp.remove(pair_2)
        perm = perm // ((2*N-1) -2*i)

        i += 1

    max_ans = max(max_ans, ans)

print(max_ans)
