N,M = map(int,input().split())

M_list = []
k_max = 0
for i in range(M):
    k = int(input())
    k_max = max(k,k_max)
    tutu = [int(key) for key in input().split()]
    M_list.append(tutu)

hash = {}
for i in range(k_max):
    hash[i] = []

for i in range(len(M_list)):
    for j in range(len(M_list[i])):
        hash[j].append(M_list[i][j])

for key in hash.keys():
    print( str(key)+":"+str(hash[key]) )
