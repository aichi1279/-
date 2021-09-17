a, b, k = map(int,input().split())

input = ""
for i in range(a):
    input += '0'
for i in range(b):
    input += '1'

list =list(input)
collec = []
for i in range(len(list)):
    for j in range(len(list)):
        if list[i] != list[j]:
            tmp  = list[i]
            list[i] = list[j]
            list[j] = tmp

        if list not in collec:
            collec.append(list)

#input = input.replace('0','a')
#input = input.replace('1','b')
print(collec)
