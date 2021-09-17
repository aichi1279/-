n = int(input())

list=[]

for i in range(1, n+1):
    if i*i >n+1 : break
    if n % i == 0:
        list.append(i)
        if n // i != i:
            list.append(n//i) 

for i in sorted(list):
    print(i)
