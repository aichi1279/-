#--------- TLEとREで　完敗！--------------
N = int(input())
s = input()
q = int(input())

reverse_judge = False
list_s = list(s)

for _ in range(q):
    T, A, B = map(int, input().split())
    A -= 1
    B -= 1

    if T==1:
        if not reverse_judge:
            tmp = list_s[A]
            list_s[A] = list_s[B]
            list_s[B] = tmp
        else:
            if A < N and B < N:
                tmp = list_s[A+N]
                list_s[A+N] = list_s[B+N]
                list_s[B+N] = tmp
            elif A < N and B >= N:
                tmp = list_s[A+N]
                list_s[A+N] = list_s[B-N]
                list_s[B-N] = tmp
            else:
                tmp = list_s[A-N]
                list_s[A-N] = list_s[B-N]
                list_s[B-N] = tmp

    elif T==2:
        if reverse_judge==False:
            reverse_judge=True
        else:
            reverse_judge=False


s = "".join(list_s)
if reverse_judge:
    front = s[:N]
    last = s[N:]
    s = last+front
print(s)
