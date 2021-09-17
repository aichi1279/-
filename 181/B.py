n = int(input())

sum=0
for i in range(n):
    a,b = map(int, input().split())
    sum_a = (a *(a-1)) //2
    sum_b = (b *(b+1)) //2
    sum += (sum_b - sum_a)

print(sum)
