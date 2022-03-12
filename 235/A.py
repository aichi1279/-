num = list(input())
keta = [100,10,1]
junnjo = [1,2,3,2,3,1,3,1,2]

ans = 0
cnt = 0
for key in junnjo:
    ans += int(num[key-1]) *keta[cnt%3]
    cnt+=1

print(ans)
