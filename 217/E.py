Q = int(input())

from collections import deque

D = deque()
for i in range(Q):
    query = input()
    if "1" in query:
        x = query.split(" ")[1]
        D.append(x)
    elif query=="2":
        print(D.popleft())
    elif query=="3":
        D = deque(sorted(list(D)))
