S,T,X = map(int,input().split())

if S <= X < T:
    print("Yes")
elif T < S and ((S <= X < T+24) or  (S <= X+24 < T+24)):
    print("Yes")
else:
    print("No")
