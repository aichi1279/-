import math
n = int(input())

if n < 1000:
    print(0)
    exit()

list = [10**15,10**12,10**9,10**6,10**3]
count = 0
flag = True
for i in range(len(list)):
    if list[i] > n:
        continue
    if flag:
        count += ((n-list[i])*math.log10(list[i])//3) + 1
        flag = False
    else:
        count += ((list[i-1]-list[i])*math.log10(list[i])//3)+ 1


"""#公式正解
ans = 0
if n >= 10**3: ans += n - 999
if n >= 10**6: ans += n - 999999
if n >= 10**9: ans += n - 999999999
if n >= 10**12: ans += n - 999999999999
if n >= 10**15: ans += n - 999999999999999
print(ans)
"""

print(int(count))
