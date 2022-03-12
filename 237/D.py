N = int(input())
S = input()
ans = "0"

pos = 0
for i,sig in enumerate(list(S)):
    #print(ans, pos)
    if sig == 'L':
        ans = ans[:pos]+str(i+1)+ans[pos:]
    else:
        ans = ans[:pos+1]+str(i+1)+ans[pos+1:]
        pos += 1

print(' '.join(list(ans)))
