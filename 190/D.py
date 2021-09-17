n = int(input())

d = 1

cnt = 0
for d in range(1,n+1):
    if d*d > n :break
    if n % d!= 0:break
    other = n // d
    if d % 2 == 1:
        cnt += 1
    if d != other and other %2 == 1:
        cnt += 1

print(cnt*2)
