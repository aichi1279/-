s = input()

s_list = list(s)

flag = True
for num in range(len(s_list)):
    if (num+1) % 2 == 1 and (s_list[num]>='a' and s_list[num]<='z'):
        continue
    elif (num+1) % 2 == 0 and (s_list[num]>='A' and s_list[num]<='Z'):
        continue
    flag = False

if flag:
    print("Yes")
else:
    print("No")
