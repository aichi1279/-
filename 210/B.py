n = int(input())
s = input()

for i in range(n):
    if int(s[i]) == 1:
        if i%2==0:
            print("Takahashi")
        else:
            print("Aoki")
        exit()
