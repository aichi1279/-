L,Q = map(int,input().split())

def search(x, index):
    left = 0
    right = len(index)
    before = -1
    m = (left+right)//2
    while before != m:
        if x >index[m]:
            left = m
        elif x < index[m]:
            right = m
        before = m
        m = (left+right)//2
    return index[m],index[m+1]

index = [0,L]
for i in range(Q):
    c,x  = map(int,input().split())
    if c==1:
        index.append(x)
        index.sort()
    else:
        pre_x, after_x = search(x, index)
        print(after_x-pre_x)
