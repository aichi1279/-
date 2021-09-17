p = int(input())

import math
list = [math.factorial(key) for key in range(1,11)]
list.sort(reverse=True)

cnt = 0
for key in list:
    if (p//key) != 0:
        cnt += p//key
        p = p % key


print(cnt)
