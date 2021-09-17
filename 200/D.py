from collections import deque
# listのコストを減らしたモジュール
# 「.append()と.pop() 」は、listモジュールでコストは　O(1)　

# dequeなら、コストO(1)で
#「.append()と.pop()」だけでなく、「.appendleft()と.popleft()」

s = deque()

rev = False
for i in input():
    if i == 'R':
        rev = not rev
    elif rev:
        if s and s[0] == i:
            s.popleft()
        else:
            s.appendleft(i)
    else:
        if s and s[-1] == i:
            s.pop()
        else:
            s.append(i)
if rev:
    s = reversed(s)   #やっぱりリバースは最後に一回のみなんだな〜
print("".join(s))
