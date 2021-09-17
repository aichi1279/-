N = int(input())

ans = "A"
cnt = 1
P = 1
way = N
way_list = []

while way//2 != 0:
    way_list.append(way)
    way = way//2
way_list.sort()
print(way_list)

for key in way_list:
    while key >= P*2:
        P *= 2
        ans += "B"
        cnt += 1
    if key != P:
        cnt += key-P
        ans += "A"*(key-P)
        P = key

print(ans)
#print(cnt)
