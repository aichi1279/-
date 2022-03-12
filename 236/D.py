N = int(input()) # 2*N 人
bags = []
for _ in range(2*N -1):
    A = [int(key) for key in input().split()]
    bags.append(A)

#舞踏会の満足度はA_ij の排他的論理和　'^' 使うよ〜


line = 1
for i in range(2, 2*N):
    line *= i

ans = []
for i in range(line):
    maxi = 0
    select = []
    added = set()
    for j,bag in enumerate(bags):
        if j in added:
            i /= len(bag)
            continue

        #select.append(int(i%len(bag)))
        kouho = bag[int(i%len(bag))]

        #indicator
        maxi = int(bin(maxi ^ kouho), 2)
        #maxi += kouho
        i /= len(bag)


    #print(select,maxi)
    ans.append(maxi)

print(max(ans))
