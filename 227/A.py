N,K,A = map(int,input().split())

for _ in range(K-1):
    A = (A%N) + 1

print(A)
