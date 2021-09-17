n, k = map(int,input().split())
hash = {}
for _ in range(n):
    a,b = map(int,input().split())
    if a in hash:
        hash[a] += b
    else:
        hash[a] = b

taro_in = k
pre_loc = 0
sorted_list = sorted(hash.items(),key = lambda x:x[0])
#print(sorted_list)

for i in range(len(sorted_list)):
    taro_in -= (sorted_list[i][0]-pre_loc)
    #print(taro_in)
    if taro_in < 0:
         res = sorted_list[i][0]+taro_in
         print(res)
         exit()
    taro_in += sorted_list[i][1]
    pre_loc = sorted_list[i][0]


print(sorted_list[-1][0]+taro_in)
