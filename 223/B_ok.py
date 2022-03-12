S = input()
Str = list(S)

from collections import deque

memo_ls = list()
tmp_deq = deque(Str.copy())
for left in range(len(S)):
    pop = tmp_deq.popleft()
    tmp_deq.append(pop)
    memo_ls.append(''.join(list(tmp_deq)))

tmp_deq = deque(Str.copy())
for right in range(len(S)):
    pop = tmp_deq.pop()
    tmp_deq.appendleft(pop)
    memo_ls.append(''.join(list(tmp_deq)))

memo_ls = list(set(memo_ls))
for i in range(len(memo_ls)-1):
    for j in range(i+1, len(memo_ls)):
        if memo_ls[i] > memo_ls[j]:
            tmp = memo_ls[i]
            memo_ls[i] = memo_ls[j]
            memo_ls[j] = tmp

min_ans = memo_ls[0]
max_ans = memo_ls[-1]

print(min_ans)
print(max_ans)
