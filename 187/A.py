a ,b = map(int,input().split())

sum_a = 0
while True:
    if a == 0:
        break
    sum_a += a % 10
    a = a // 10

sum_b = 0
while True:
    if b == 0:
        break
    sum_b += b % 10
    b = b // 10

print(max(sum_a,sum_b))
