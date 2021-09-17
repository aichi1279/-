
A, B, C = map(int,input().split())
MOD = 998244353

sum = (A*(A+1)) // 2
sum %= MOD

sum *= (B*(B+1)) // 2
sum %= MOD

sum *= (C*(C+1)) //2
sum %=MOD

print(sum)
