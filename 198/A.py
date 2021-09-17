n = int(input())
n -= 2

C = set()
for i in range(n+1):
    C.add((i+1,n-i+1))

print(len(C))
