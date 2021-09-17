h, w , x ,y = map(int, input().split())

list = []
for i in range(h):
    list.append(input())

sub_x = y-1
sub_y = x-1
count = 1
set = set()
while  sub_x < w-1 and list[sub_y][sub_x+1]!="#":
    if (sub_x+1,sub_y) not in set:
        count += 1
        set.add((sub_x+1,sub_y))

    sub_x += 1

sub_x = y-1
while  sub_x > 0  and list[sub_y][sub_x-1]!="#":
    if (sub_x-1,sub_y) not in set:
        set.add((sub_x-1,sub_y))
        count += 1

    sub_x -= 1


sub_x = y-1
while  sub_y < h-1 and list[sub_y+1][sub_x]!="#":
    if (sub_x,sub_y+1) not in set:
        set.add((sub_x,sub_y+1))
        count += 1
    sub_y += 1


sub_y = x-1
while sub_y > 0 and list[sub_y-1][sub_x]!="#":
    if (sub_x,sub_y-1) not in set:
        set.add((sub_x,sub_y-1))
        count += 1
    sub_y -= 1



#for key in set:
#    print(key)


print(count)
