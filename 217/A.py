S,T = input().split()

leng = min(len(S),len(T))

for i in range(leng):
    if S[i] == T[i]:
        continue
    elif S[i] < T[i]:
        print("Yes")
        exit()
    else:
        print("No")
        exit()

if len(S)<len(T):
    print("Yes")
else:
    print("No")
