x = input()
m = int(input())

#int(x,数字):  2<=数字<=36

str_set = set(list(x))
maxi = 0
for num in str_set:
    maxi = max(maxi,int(num)+1)

count = 0
ans = int(x, maxi)
while ans<=m:
    maxi += 1
    count += 1
    ans = int(x, maxi)

print(count)


def ten_n():
