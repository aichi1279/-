n = int(input())

J_hash = {}
list = ["AC","WA","TLE","RE"]
for i in range(n):
    s = input()
    if s in J_hash:
        J_hash[s] += 1
    else:
        J_hash[s] = 1

for key in list:
    if key in J_hash:
        print(key+" x "+str(J_hash[key]))
    else:
        print(key+" x 0")
