n = int(input())
A_list = [int(key) for key in input().split()]
B_list = [int(key) for key in input().split()]
C_list = [int(key) for key in input().split()]

a_hash = {}
for key in A_list:
    if key in a_hash:
        a_hash[key] += 1
    else:
        a_hash[key] = 1

c_hash = {}
for key in C_list:
    if key in c_hash:
        c_hash[key] += 1
    else:
        c_hash[key] = 1

cnt = 0
i = 1
for B in B_list:
    flag1 = False
    flag2 = False
    if i in c_hash:
        C_cnt = c_hash[i]
        flag1 = True
    if B in a_hash:
        A_cnt = a_hash[B]
        flag2 = True
    i += 1
    if flag1 and flag2:
        cnt += A_cnt *C_cnt
print(cnt)
