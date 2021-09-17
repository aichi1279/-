n = int(input())
list = list(map(int,input().split()))

hash={}
for key in list:
    if key in hash:
        hash[key] += 1
    else:
        hash[key] = 1

abs_hash={}
for key in hash.keys():
    for key2 in hash.keys():
        if key == key2:
            continue
        if abs(key-key2) in abs_hash:
            abs_hash[abs(key-key2)] += hash[key]*hash[key2]
        else:
            abs_hash[abs(key-key2)] = hash[key]*hash[key2]

ans = 0
for key in abs_hash.keys():
    #print(str(key)+":"+str(abs_hash[key]))

    ans += (abs_hash[key]) * key**2

print(ans//2)
