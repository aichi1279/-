S = list(input())
T = list(input())

border = (ord(T[0])-ord(S[0]))%26
for i in range(len(S)):
    if border != (ord(T[i])-ord(S[i]))%26:
        print("No")
        exit()

print("Yes")
