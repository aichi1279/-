a,b = map(int,input().split())

list = [key for key in range(a,b+1)]
res = 1
for oen in list:
    for two in list:



while True:
    b = a
    a = b%a
    if a==0:
        break

print(b)
