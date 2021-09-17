#天才! 200を割った余りに注目すると200通りしか存在しないことに気づく
n = int(input())
list = [int(key)%200 for key in input().split()]
hash = {}
for key in list:
    if key in hash:
        hash[key] += 1
    else:
        hash[key] = 1


cnt = 0
#200 * 200だから二重ループが可能
for key in hash:
    cnt += (hash[key]*(hash[key]-1)) // 2

print(cnt)
