N, K = map(int,input().split())
A_list = [int(key) for key in input().split()]

hash = {}
for key in sorted(A_list):
    hash[key] = K //N

K = K % N
for key in hash.keys():
    if K != 0:
        hash[key] += 1
    else:
        break
    K -= 1


for key in A_list:
    print(hash[key])
