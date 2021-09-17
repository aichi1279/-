S,K = input().split()
K = int(K)

kouho = list(S)
ans = set()
import itertools
kouho = itertools.permutations(kouho)

for key in kouho:
    ans.add(''.join(key))

ans = list(ans)
ans.sort()
print(ans[K-1])
