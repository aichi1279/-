l = int(input())

upper = 1
for i in range(11):
    upper *= l-1-i #l-1 !

under = 1
for i in range(1,11):
    under *= i+1 #11!


ans = upper//under

print(ans)
