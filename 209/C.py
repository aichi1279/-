n = int(input())
C = list(map(int, input().split()))

C.sort()
ans = 1
cnt = 0
for i in range(n):
    ans *= max(C[i]-i, 0)
    ans = ans%((10**9)+7)#ループ内に入れないと大規模計算からTLEになる
    #大きな値の計算には注意

print(ans)
