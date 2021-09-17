n = input()

if len(n)%2 == 1:
    front = n[:len(n)//2]
    last = n[len(n)//2+1:]
else:
    front = n[:len(n)//2]
    last = n[len(n)//2:]


if list(front)==list(reversed(list(last))):
    print("Yes")
    exit()

for i in range(len(n)):
    n = '0'+ n
    if len(n)%2 == 1:
        front = n[:len(n)//2]
        last = n[len(n)//2+1:]
    else:
        front = n[:len(n)//2]
        last = n[len(n)//2:]

    if list(front) == list(reversed(list(last))):
        print("Yes")
        exit()

print("No")
