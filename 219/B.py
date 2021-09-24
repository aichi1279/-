S1 = input()
S2 = input()
S3 = input()

table = [S1,S2,S3]
T = input()

T_list = list(T)
ans = ""
for key in T_list:
    ans += table[int(key)-1]

print(ans)
