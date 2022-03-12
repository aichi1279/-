L,R = map(int,input().split())
S = input()
ans = S[:L-1]
last = S[R:]
reverse = S[L-1:R]

leng = len(reverse)
for i in range(leng):
    ans += reverse[leng-1 -i]

print(ans+last)
