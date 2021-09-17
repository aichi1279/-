import math
import copy
n = int(input())


if n %3==0:
    print(0)
    exit()

list=[]
var_n = n
for i in range(18):
    list.append(str(var_n %10))
    var_n//=10
    if var_n==0:
        break

for i in range(len(list)):
    tmp=list[i]
    list[i]=list[len(list)-i-1]
    list[len(list)-i-1] = tmp

#print(list)
mini= pow(10,18)

for key1 in list:
    count=1
    sub_ls = copy.copy(list)
    sub_ls.remove(key1)
    if len(sub_ls)==0:
        break

    num = int("".join(sub_ls))
    if num!=0 and num%3==0:
        mini = 1
        break

    for key2 in sub_ls:
        sub_ls.remove(key2)
        if len(sub_ls)==0:
            break
        count+=1
        str="".join(sub_ls)
        num2 =int(str)
        if num2!=0 and num2%3==0 and mini>count:
            mini = count


if mini==pow(10,18):
    print(-1)
else:
    print(count)
