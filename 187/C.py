n = int(input())

hash = {}
for i in range(n):
    s = input()
    hash[s] = 0


for key in hash.keys():
    if ("!"+key) in hash:
        print(key)
        exit()

print("satisfiable")
