n = int(input())

A_list = [int(key) for key in input().split()]

hash={}

for key in A_list:
    if key in hash:
        hash[key] += 1
    else:
        hash[key] = 1

for key in hash.keys():
    if hash[key]>1:
        print("No")
        exit()


print("Yes")
