n = int(input())
sub_n = n
list = [str(i) for i in range(1,n+1)]

ans_list=[]
count = 0
for key in list:
    if '7' in key:
        ans_list.append(key)

list = [format(i, 'o') for i in range(1,n+1)]
for key in list:
    if '7' in key:
        tmp = str(int(key,8))
        #print(tmp)
        ans_list.append(tmp)

ans_list = set(ans_list)
print(n - len(ans_list))
