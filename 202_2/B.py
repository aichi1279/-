s = list(input())

res = ""
for i in range(len(s)):
    key = s[len(s)-i-1]
    if key=='6':
        key = '9'
    elif key=='9':
        key = '6'
    res += key

print(res)
