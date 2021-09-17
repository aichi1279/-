import math
x = int(input())
rate = 1.01

n = (math.log(x,10)-2)//(math.log(101,10)-2)

print(int(n+1))
