n, k = map(int,input().split())

list = [str(key+1)+'0' for key in range(n)]

sum = 0
for key1 in list:
    for key2 in range(1,k+1):
        s = key1 + str(key2)
        #print(s)
        sum += int(s)

print(sum)
