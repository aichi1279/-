n = int(input())

count=0
list=[]
for i in range(n):
    x, y = map(int, input().split())
    list.append((x,y))

for i in range(len(list)):
    for j in range(i+1,len(list)):
        a = (list[i][1]-list[j][1]) / (list[i][0]-list[j][0])
        #print(a)
        if a <= 1 and a >=-1:
            count+=1

print(count)
