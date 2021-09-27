A,B,C = map(int,input().split())

for key in range(A,B+1):
    if key % C == 0:
        print(key)
        exit()

print(-1)
