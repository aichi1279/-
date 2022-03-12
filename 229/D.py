S = input()
K = int(input())

data_ls = []
dot_cnt = 0
X_cnt = 0
for i in range(len(S)):
    if S[i]=='X':
        X_cnt += 1
        if dot_cnt>0:
            data_ls.append((dot_cnt,'.'))
            dot_cnt = 0
    else:
        dot_cnt += 1
        if X_cnt>0:
            data_ls.append((X_cnt,'X'))
            X_cnt = 0


ans_ls = []
if len(data_ls)==0:
    print(len(S))
    exit()


if data_ls[0][1]=='.':
    for i in range(0,len(data_ls),2):
        cnt = 0
        sum = 0
        while K>cnt:
            if i==0 and K >= data_ls[i][0]:
                cnt += data_ls[i][0]
                sum += data_ls[i][0]
                continue
            elif i==0 and K < data_ls[i][0]:
                cnt,sum = K,K
                break
            elif K > cnt+data_ls[i][0]:
                cnt += data_ls[i][0]
                sum += data_ls[i-1][0] + data_ls[i][0]
            else:
                cnt += K-cnt
                sum += K-cnt + data_ls[i-1][0]
            i += 2
            if i>=len(data_ls):
                sum += data_ls[i-2][0]
                break

        ans_ls.append(sum)
else:
    for i in range(1,len(data_ls)-1,2):
        cnt = 0
        sum = 0
        while K>cnt:
            if K >= cnt+data_ls[i][0]:
                cnt += data_ls[i][0]
                sum += data_ls[i-1][0] + data_ls[i][0]

            else:
                cnt += K
                sum += K-cnt + data_ls[i-1][0]
                #print(data_ls[i-1])

            i += 2
            if i>=len(data_ls):
                sum += data_ls[i-2][0]
                break

        ans_ls.append(sum)

print(max(ans_ls))
