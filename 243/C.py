N = int(input())
pos = []
for _ in range(N):
    x,y = map(int, input().split())
    pos.append((x,y))

D = input()
hash = {}
for i, p in enumerate(pos):
    if p[1] in hash:
        if D[i] == "R":
            if hash[p[1]][0] != None:
                hash[p[1]][0] = min(hash[p[1]][0], p[0])
            else:
                hash[p[1]][0] = p[0]
        else:
            if hash[p[1]][1] != None:
                hash[p[1]][1] = max(hash[p[1]][1], p[0])
            else:
                hash[p[1]][1] = p[0]

    else:
        hash[p[1]] = [None, None]
        if D[i] == "R":
            hash[p[1]][0] = p[0]
        else:
            hash[p[1]][1] = p[0]

ans = False
for y in hash.keys():
    if hash[y][0] != None and hash[y][1] != None:
        #print(hash[y][0] , hash[y][1])
        ans += (hash[y][0] < hash[y][1])
    #print(hash[y][0] , hash[y][1])

if ans:
    print("Yes")
else:
    print("No")
