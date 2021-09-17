n = int(input())

sum=0
list = []
check_ls = []
for i in range(n):
    a, b = map(int, input().split())
    sum += a
    list.append((a,b))
    check_ls.append((a+b,i))

check_ls.sort()
sorted_list = []
for i in range(len(check_ls)):
    sorted_list.append(list[check_ls[len(check_ls)-i-1][1]])

#print(sorted_list)


count = 0
takahasi_score = 0
aoki_score = sum

for tuple in sorted_list:
    count += 1
    takahasi_score += tuple[1]+tuple[0]
    aoki_score -=  tuple[0]

    if takahasi_score > aoki_score:
        print(count)
        exit()
