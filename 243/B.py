N = int(input())
A = [int(key) for key in input().split()]
B = [int(key) for key in input().split()]

AB = []
AB.extend(A.copy())
AB.extend(B.copy())

dict = {}
for key in AB:
    if key in dict:
        dict[key] += 1
    else:
        dict[key] = 1

sorted_ls = sorted(dict.items(), key=lambda x:x[1], reverse=True)
kouho = [key[0] for key in sorted_ls if key[1]==2]
ans2 = len(kouho)

ans1 = 0
for key in kouho:
    for i in range(N):
        if key == A[i] == B[i]:
            ans1 += 1

print(ans1)
print(ans2-ans1)
