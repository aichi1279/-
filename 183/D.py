import numpy as np
n,w = map(int ,input().split())

SK = np.zeros(2*(10**5)+1)
for i in range(n):
    S,T,P = map(int, input().split())
    SK[S:T] += P


for t in SK:
    if t > w:
        print("No")
        exit()

print("Yes")
#print(len(SK))
