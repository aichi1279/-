n, k = map(int, input().split())

snk_list = [i+1 for i in range(n)]
set = set()

for i in range(k):
    d = int(input())
    list = input().split(" ")


    for sunuke in list:
        if sunuke not in set:
            set.add(sunuke)

print(n-len(set))
