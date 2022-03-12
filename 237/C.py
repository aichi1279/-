S = input()
#S = "b"*10**5

left_cnt = 0
for i in range(1,len(S)):#10**6!!
    if S[-i] == 'a':
        left_cnt += 1
    else:
        break

right_cnt = 0
for i in range(len(S)):
    if S[i] == 'a':
        left_cnt += 1
    else:
        break

S = 'a'*max(left_cnt-right_cnt, 0) + S
for i in range((len(S)//2) +1):
    if S[i]!=S[len(S)-1-i]:
        print('No')
        exit()

print('Yes')
