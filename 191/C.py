h,w = map(int,input().split())

matrix = []
for i in range(h):
    line = list(input())
    matrix.append(line)

#print(matrix)

cnt = 0
for i in range(len(matrix)-1):
    for j in range(len(matrix[i])-1):
        cnt += ( (matrix[i][j]=='#')+(matrix[i][j+1]=='#')+
        (matrix[i+1][j]=='#')+(matrix[i+1][j+1]=='#'))%2
        
print(cnt)
