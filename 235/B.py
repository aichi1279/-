N = int(input())
H_ls = [int(key) for key in input().split()]

max_H = 0
for i in range(N):
    if max_H < H_ls[i]:
        max_H = H_ls[i]
    else:
        break

print(max_H)
