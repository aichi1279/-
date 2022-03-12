import heapq

heap =[]
Q = int(input())
for _ in range(Q):
    tuple = [int(key) for key in input().split()]
    if len(tuple)==2:
        heapq.heappush(heap, tuple[1])
    elif tuple[0]==2:
        tmp = [key for key in heap if key <= tuple[1]]
        ans = heapq.nlargest(tuple[2], tmp)
        if len(ans)==tuple[2]:
            print(ans[-1])
        else:
            print(-1)
    elif tuple[0]==3:
        tmp = [key for key in heap if key >= tuple[1]]
        ans = heapq.nsmallest(tuple[2], tmp)
        if len(ans)==tuple[2]:
            print(ans[-1])
        else:
            print(-1)
