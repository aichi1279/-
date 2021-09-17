from fractions import Fraction
n = int(input())

list=[]
for i in range(n):
    x,y = map(int, input().split())
    list.append([x,y])


for i in range(n):
    for j in range(n):
        if i == j :
            continue

        if list[i][0]==list[j][0]:
            x = list[j][0]
        elif list[i][1]==list[j][1]:
            y = list[i][1]
        else:
            a = Fraction( list[i][1]-list[j][1] , list[i][0]-list[j][0] )
            b = list[i][1] - (a * list[i][0])

        for k in range(n):
            if i==k or j==k:
                continue
            elif list[i][0]==list[j][0] and x==list[k][0]:
                #print(list[i],list[j],list[k],1)
                print("Yes")
                exit()
            elif list[i][1]==list[j][1] and y==list[k][1]:
                #print(list[i],list[j],list[k],2)
                print("Yes")
                exit()
            elif list[i][0]!=list[j][0] and list[i][1]!=list[j][1] and list[k][1] == (a*list[k][0])+b:
                #print(list[i],list[j],list[k],3)
                print("Yes")
                exit()

print("No")
