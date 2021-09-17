N = int(input())
input_perm = [int(key) for key in input().split()]

ans = [0]*N
for i in range(N):
     ans[input_perm[i]-1] = i+1

str_ans = ""
for key in ans:
    str_ans += str(key)+" "

str_ans = str_ans[:-1]
print(str_ans)
