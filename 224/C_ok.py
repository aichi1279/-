N = int(input())
x_ls = []
y_ls = []
for _ in range(N):
    x, y = map(int, input().split())
    x_ls.append(x)
    y_ls.append(y)

cnt = 0
for i in range(N):
    for j in range(N):
        if i==j:
            continue
        for k in range(N):
            if i==k or j==k:
                continue
            S  = (x_ls[i]-x_ls[k])*(y_ls[j]-y_ls[k])-(x_ls[j]-x_ls[k])*(y_ls[i]-y_ls[k])
            #print(S)
            S *= -1
            if S > 0:
                cnt += 1

print(cnt//3)
